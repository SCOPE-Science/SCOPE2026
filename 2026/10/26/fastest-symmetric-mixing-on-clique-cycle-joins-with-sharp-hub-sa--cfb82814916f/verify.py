"""Reproduce numerical and algebraic comparisons for K_r join C_n fastest mixing.
Scientific theorem and its infinite-domain proof are in RESULT.md; finite checks are supplementary.
"""
import math
import numpy as np
from scipy.optimize import linprog


def shape(r, n):
    e = 2 * (1 - math.cos(2 * math.pi / n))
    d = 2 * (1 - math.cos(2 * math.pi * (n // 2) / n))
    q = (d - e) / (d + e)
    a_inter = (1 + q) / (n + r + r * q)
    a = min(1 / n, a_inter)
    b = 2 * (1 - r * a) / (e + d)
    h = 1 - n * a
    c = h / r
    mu = q * (1 - r * a)
    return a, b, c, mu, q, e, d


def matrix(r, n, a, b, c):
    N = r + n
    P = np.zeros((N,N))
    for i in range(r):
        for j in range(r):
            if i != j:
                P[i,j] = c
        P[i,r:] = a
    for i in range(n):
        P[r+i,:r] = a
        P[r+i,r+(i-1)%n] = b
        P[r+i,r+(i+1)%n] = b
    for i in range(N):
        P[i,i] = 1 - P[i].sum()
    return P


def lp_opt(r, n):
    # Variables a,b,c,t; |linear eigenvalues| <= t.
    entries = [(n+r,0,0), (n,0,r)]
    entries += [(r,2*(1-math.cos(2*math.pi*j/n)),0) for j in range(1,n)]
    A = []; B = []
    for va,vb,vc in entries:
        A.append([-va,-vb,-vc,-1]); B.append(-1)  # 1-linear <= t
        A.append([ va, vb, vc,-1]); B.append( 1)  # -1+linear <= t
    A.extend([[n,0,r-1,0],[r,2,0,0]])
    B.extend([1,1])
    return linprog([0,0,0,1],A_ub=A,b_ub=B,bounds=[(0,None)]*4,method='highs')


def check():
    eig = 0
    opt = 0
    phase = 0
    for r in range(2,13):
        for n in range(4,23):
            a,b,c,mu,q,e,d = shape(r,n)
            assert 0 <= a <= 1/n + 1e-12
            assert n*a+(r-1)*c<=1+1e-12
            assert r*a+2*b<=1+1e-12
            assert abs(q-(d-e)/(d+e))<1e-12
            # Closed-form phase is independent of floating-point optimization.
            predicted = (n >= 2*r+1 if r >= 5 else n >= 2*r+2)
            assert predicted == (q*(n-r) > r - 1e-10)
            phase += 1
            if r <= 8 and n <= 17:
                res=lp_opt(r,n)
                assert res.success, res.message
                assert abs(res.fun-mu)<2e-8,(r,n,res.fun,mu)
                opt+=1
            if r<=6 and n<=13:
                P=matrix(r,n,a,b,c)
                assert (P.min()>=-1e-13) and np.max(abs(P.sum(axis=1)-1))<1e-12
                spectrum=np.linalg.eigvalsh(P)
                assert abs(spectrum[-1]-1)<1e-12
                measured=np.max(np.abs(spectrum[:-1]))
                assert abs(measured-mu)<3e-11,(r,n,measured,mu)
                eig+=1
    print(f'VERIFY_OK phase_pairs={phase} invariant_LP_comparisons={opt} direct_full_spectra={eig}')

if __name__=='__main__':check()
