"""Exact small-degree checks for squarefree multiplicative energy over F_2[T].
No proof of the infinite asymptotic is inferred from these finite checks.
"""
from collections import Counter
from itertools import combinations
from math import log1p, exp

def degree(f):
    return f.bit_length()-1

def rem(f,g):
    while f and degree(f)>=degree(g):
        f^=g << (degree(f)-degree(g))
    return f

def gcd(f,g):
    while g:
        f,g=g,rem(f,g)
    return f

def mul(f,g):
    ans=0
    while g:
        if g&1:ans^=f
        g>>=1;f<<=1
    return ans

def is_squarefree(f):
    derivative=sum(((f>>i)&1) << (i-1) for i in range(1,degree(f)+1,2))
    return gcd(f,derivative)==1


def mobius(n):
    p=2;r=1
    while p*p<=n:
        if n%p==0:
            n//=p;r=-r
            if n%p==0:return 0
        p+=1
    if n>1:r=-r
    return r

def irreducibles_degree(d,q=2):
    return sum(mobius(k)*q**(d//k) for k in range(1,d+1) if d%k==0)//d

def euler_partial(q=2,max_degree=25):
    lp=0.
    for d in range(1,max_degree+1):
        z=q**(-d)
        correction=-9*z*z+16*z**3-9*z**4+z**6
        lp+=irreducibles_degree(d,q)*log1p(correction)
    return exp(lp)

sqf={d:[(1<<d)|j for j in range(1<<d) if is_squarefree((1<<d)|j)] for d in range(7)}
for n in range(1,7):
    rep=Counter(mul(f,g) for f in sqf[n] for g in sqf[n])
    brute=sum(v*v for v in rep.values())
    canonical=0
    for k in range(n+1):
        for G in sqf[k]:
            for u in range(n-k+1):
                v=n-k-u
                for A in sqf[u]:
                    for D in sqf[u]:
                        if gcd(A,D)!=1:continue
                        for B in sqf[v]:
                            if gcd(A,B)!=1 or gcd(D,B)!=1:continue
                            for C in sqf[v]:
                                fs=(G,A,B,C,D)
                                if all(gcd(fs[i],fs[j])==1 for i,j in combinations(range(5),2)):
                                    canonical+=1
    assert brute==canonical,(n,brute,canonical)
    all_monic=[(1<<n)|j for j in range(1<<n)]
    r_all=Counter(mul(f,g) for f in all_monic for g in all_monic)
    all_brute=sum(t*t for t in r_all.values())
    all_formula=(1+n/2)*2**(2*n)
    assert all_brute==all_formula,(n,all_brute,all_formula)
    print(f'n={n} squarefree-count={len(sqf[n])} squarefree-energy={brute} unrestricted-energy={all_brute}')
print('q=2 C25=%.15f'%euler_partial(2,25))
print('q=3 C25=%.15f'%euler_partial(3,25))
print('VERIFY_OK')
