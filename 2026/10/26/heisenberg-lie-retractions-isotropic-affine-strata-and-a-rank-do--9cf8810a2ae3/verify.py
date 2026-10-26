"""Independent finite-field tests for the Heisenberg Lie-retraction rank formula.

Run: python3 verify.py
Uses only the Python standard library.  The proof is in RESULT.md.
"""
from collections import Counter
from itertools import product
from math import prod

def gaussian(n, r, q):
    if not 0 <= r <= n:
        return 0
    top = prod(q**(n-i)-1 for i in range(r))
    bot = prod(q**(r-i)-1 for i in range(r))
    return top // bot

def isotropic_count(n, r, q):
    return gaussian(n, r, q) * prod(q**(n-i)+1 for i in range(r))

def predicted(n, q):
    return {r: isotropic_count(n, r, q) * q**(r*(2*n-r+1)) for r in range(n+1)}

def mul(A, B, p):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) % p
             for j in range(len(B[0]))] for i in range(len(A))]

def rank(A, p):
    T = [row[:] for row in A]
    h, w = len(T), len(T[0]); pivot = 0
    for col in range(w):
        j = next((j for j in range(pivot,h) if T[j][col] % p), None)
        if j is None: continue
        T[pivot], T[j] = T[j], T[pivot]
        v = pow(T[pivot][col], -1, p)
        T[pivot] = [v*x % p for x in T[pivot]]
        for t in range(h):
            if t == pivot: continue
            v = T[t][col]
            T[t] = [(a-v*b)%p for a,b in zip(T[t],T[pivot])]
        pivot += 1
        if pivot == h: break
    return pivot

def n1(p):
    J = [[0,1],[-1%p,0]]
    tally = Counter()
    for coeffs in product(range(p), repeat=7):
        a,b,d,e,l0,l1,c = coeffs
        A = [[a,b],[d,e]]
        AT = [[a,d],[b,e]]
        if mul(mul(AT,J,p),A,p) != [[c*x%p for x in row] for row in J]:
            continue
        if mul(A,A,p) != A: continue
        if c*c%p != c: continue
        if (l0*a+l1*d+c*l0)%p != l0: continue
        if (l0*b+l1*e+c*l1)%p != l1: continue
        F = [[a,b,0],[d,e,0],[l0,l1,c]]
        if mul(F,F,p) != F: raise AssertionError('non-idempotent')
        tally[rank(F,p)] += 1
    assert tally == Counter({0:1,1:predicted(1,p)[1],3:1}), (p,tally)
    print('n=1, p=',p,':',dict(sorted(tally.items())))

def product_rows(A,B):
    return [__import__('functools').reduce(int.__xor__,
        (B[k] for k in range(len(B)) if row & (1<<k)),0) for row in A]

def rk2(rows):
    base=[0]*4
    count=0
    for vec in rows:
        v=vec
        for i in range(3,-1,-1):
            if v>>i & 1:
                if base[i]: v^=base[i]
                else: base[i]=v; count+=1; break
    return count

def n2_binary():
    # Basis x1,x2,y1,y2; form matrix J=[0 I;-I 0].
    J=(4,8,1,2)
    tally=Counter()
    for code in range(1<<16):
        A=tuple((code>>(4*i))&15 for i in range(4))
        if tuple(product_rows(A,A)) != A: continue
        # Isotropy of all image-basis vectors, equivalently A^T J A=0.
        cols = [sum(((A[i]>>j)&1)<<i for i in range(4)) for j in range(4)]
        if any(
            (sum((((cols[a]>>i)&1)*((cols[b]>>k)&1)*((J[i]>>k)&1))
                 for i in range(4) for k in range(4)) % 2)
            for a in range(4) for b in range(a+1,4)
        ): continue
        r=rk2(A)
        # Every functional on image A extends uniquely via ell=ell*A.
        tally[r] += 2**r
    assert tally==Counter(predicted(2,2)),(tally,predicted(2,2))
    print('n=2, p=2:',dict(sorted(tally.items())),'plus identity')

def dimension(n,r):
    return 4*n*r-(5*r*r-3*r)//2

def dimension_tests():
    for n in range(1,30):
        d=[dimension(n,r) for r in range(n+1)]
        assert all(d[r]-d[r-1] == 4*n-5*r+4 for r in range(1,n+1))
        assert set(i for i,x in enumerate(d) if x==max(d)) == set(
            i for i in range(n+1) if 0 <= 4*n-5*i+4 and (i==n or 4*n-5*(i+1)+4<=0))
    print('dimension finite differences and maximizing ranks: OK')

if __name__=='__main__':
    n1(2); n1(3); n1(5)
    n2_binary(); dimension_tests()
    print('HEISENBERG_RETRACTIONS_OK')
