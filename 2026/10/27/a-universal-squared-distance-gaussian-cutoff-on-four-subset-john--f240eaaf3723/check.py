"""Exact rational checks for the squared-Johnson-distance kernel on four-subsets.
Run with Python 3.10+; no nonstandard dependencies.
"""
from fractions import Fraction
from math import comb
from itertools import combinations

def C(n, k):
    return comb(n, k) if 0 <= k <= n else 0

def E(n, j, i):
    return sum((-1)**t*C(j,t)*C(4-j,i-t)*C(n-4-j,i-t)
               for t in range(i+1))

def eig(n, j, q):
    return sum(E(n,j,i)*q**(i*i) for i in range(5))

def gram(n, q):
    sets = list(combinations(range(n), 4))
    S = [set(x) for x in sets]
    return sets, [[q**((4-len(a&b))**2) for b in S] for a in S]

def harmonic(sets, j):
    pairs = [(2*t,2*t+1) for t in range(j)]
    out = []
    for A in sets:
        z=1
        for a,b in pairs:
            z *= (int(a in A)-int(b in A))
        out.append(z)
    return out

def test():
    steps=0
    for n in (8,9):
        for q in (Fraction(1,4),Fraction(1,3),Fraction(13,25),Fraction(19,20)):
            sets,G=gram(n,q)
            for j in (3,4):
                v=harmonic(sets,j)
                lam=eig(n,j,q)
                assert any(v)
                for row,z in zip(G,v):
                    assert sum(row[t]*v[t] for t in range(len(v))) == lam*z
                    steps+=1
            N=C(n,4)
            mul=[C(n,j)-C(n,j-1) for j in range(5)]
            assert sum(mul[j]*eig(n,j,q) for j in range(5)) == N
            assert sum(mul[j]*eig(n,j,q)**2 for j in range(5)) == N*sum(C(4,i)*C(n-4,i)*q**(2*i*i) for i in range(5))
            steps+=2
    def F(q): return sum((-1)**i*C(4,i)*q**(i*i) for i in range(5))
    assert F(Fraction(1,4))>0 and F(Fraction(1,3))<0
    assert eig(8,3,Fraction(13,25))<0
    assert eig(8,4,Fraction(19,20))>0 and eig(8,3,Fraction(19,20))<0
    lo,hi=Fraction(1,4),Fraction(1,3)
    for _ in range(135):
        mid=(lo+hi)/2
        if F(mid)>0:lo=mid
        else:hi=mid
    print('exact matrix-vector identities / spectral moments:',steps)
    print('threshold interval:',float(lo),float(hi))
    print('rational witness signs all checked')
if __name__=='__main__': test()
