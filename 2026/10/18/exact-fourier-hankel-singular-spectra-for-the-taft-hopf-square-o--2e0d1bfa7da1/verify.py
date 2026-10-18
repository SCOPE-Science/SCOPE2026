"""Reproduce the Taft Hopf-square block and Fourier/SVD formulas.
Public mathematical verification only; requires Python 3 and NumPy.
"""
import cmath
import math
import numpy as np


def multiply(n, q, a, b):
    """Multiply sparse Taft elements in PBW basis (r,s)."""
    out = {}
    for (r, s), v in a.items():
        for (t, u), w in b.items():
            if r + t < n:
                key = (r + t, (s + u) % n)
                out[key] = out.get(key, 0j) + v * w * q ** (s * t)
    return out


def tensor_product(n, q, a, b):
    """Multiply sparse elements in Taft tensor Taft."""
    out = {}
    for (r, s, t, u), v in a.items():
        for (h, i, j, k), w in b.items():
            if r + h < n and t + j < n:
                key = (r + h, (s + i) % n, t + j, (u + k) % n)
                out[key] = out.get(key, 0j) + v*w*q**(s*h+u*j)
    return out


def delta_direct(n, q, r, b):
    one = {(0,0,0,0): 1+0j}
    dx = {(1,0,0,0): 1+0j, (0,1,1,0): 1+0j}
    t = one
    for _ in range(r):
        t = tensor_product(n,q,t,dx)
    dg = {(0,b,0,b): 1+0j}
    t = tensor_product(n,q,t,dg)
    answer = {}
    for (i,j,k,l), v in t.items():
        y = multiply(n,q,{(i,j):v},{(k,l):1+0j})
        for key, coeff in y.items():
            answer[key] = answer.get(key,0j)+coeff
    return answer


def qbin_table(n,q):
    rows = [[1+0j]]
    for r in range(1,n):
        prev = rows[-1]
        rows.append([(prev[j] if j<len(prev) else 0j) +
                     ((q**(r-j))*prev[j-1] if j>0 else 0j)
                     for j in range(r+1)])
    return rows


def check(n):
    q = cmath.exp(2j*math.pi/n)
    qb = qbin_table(n,q)
    F = np.array([[q**(a*d)/math.sqrt(n) for d in range(n)] for a in range(n)], dtype=complex)
    assert np.max(np.abs(F.conj().T@F-np.eye(n))) < 3e-11
    for r in range(n):
        B = np.zeros((n,n),dtype=complex)
        for b in range(n):
            for j in range(r+1):
                B[(2*b+j)%n,b] += qb[r][j]*q**(j*(j+b))
            if n <= 8:
                brute = delta_direct(n,q,r,b)
                for d in range(n):
                    assert abs(brute.get((r,d),0j)-B[d,b])<4e-9, (n,r,b,d)
                assert all(s==r for (s,d) in brute)
        K = np.array([q**(c*c)*sum(qb[r][j]*q**(j*(j+c)) for j in range(r+1)) for c in range(n)])
        H = np.array([[K[(a+b)%n] for b in range(n)] for a in range(n)])
        D = np.diag(np.array([q**(-a*a) for a in range(n)]))
        assert np.max(np.abs(F@B-D@H@D/math.sqrt(n))) < 7e-9, ('factorization',n,r)
        lam = [sum(K[c]*q**(-k*c) for c in range(n))/math.sqrt(n) for k in range(n)]
        singular = sorted(np.linalg.svd(B,compute_uv=False))
        expected = sorted(abs(z) for z in lam)
        assert max(abs(u-v) for u,v in zip(singular,expected)) < 5e-9, ('spectrum',n,r)
        if r==1:
            if n % 2 == 0:
                expected1=[math.sqrt(2)]*n
                assert np.max(np.abs(B.conj().T@B-2*np.eye(n)))<5e-9
            else:
                expected1=sorted(abs(1+q**k) for k in range(n))
            assert max(abs(u-v) for u,v in zip(singular,expected1))<5e-9, ('first layer',n)
    return n

if __name__=='__main__':
    checked=[check(n) for n in range(2,13)]
    print('VERIFY_OK: n='+','.join(map(str,checked))+'; all degrees; direct coproduct through n=8')
