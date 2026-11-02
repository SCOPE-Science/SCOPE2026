"""Exact-rational checks for the affine torus period-circle formulas.

All formulas apply to the two-torus R/Z squared; calculations here check
selected finite instances and are not substitutes for their proofs.
"""
from fractions import Fraction as Q
from math import gcd


def frac(x):
    return x % 1


def F(x, y, e, f):
    return (frac(3*x+2*y+e), frac(x+2*y+f))


def iterate(x, y, e, f, n):
    for _ in range(n):
        x, y = F(x, y, e, f)
    return x, y


def fixed_formula(n, e, f, u, j):
    delta = e-2*f
    L = 4**n-1
    S = L//3
    W = (L-3*n)//9
    v = frac((Q(j) - S*u - S*f - delta*W)/L)
    x = frac(u+2*v)
    y = v
    return x, y


for e, f, q in [
    (Q(1,10),Q(1,5),10), (Q(1,2),Q(0),2),
    (Q(1,3),Q(0),3), (Q(0),Q(0),1),
    (Q(5,7),Q(1,7),7), (Q(1,7),Q(1,14),1)
]:
    delta = frac(e-2*f)
    assert delta.denominator == q
    for n in [q,2*q]:
        L, S = 4**n-1, (4**n-1)//3
        assert gcd(L,S)==S
        assert (L-3*n)%9==0
        for u in [Q(0),Q(1,7),Q(19,41)]:
            for j in [0,1,2, L//2,L-1]:
                x,y = fixed_formula(n,e,f,u,j)
                assert iterate(x,y,e,f,n)==(x,y)
                assert frac(x-2*y)==u
                if n==q:
                    for m in range(1,q):
                        assert iterate(x,y,e,f,m)!=(x,y)
    print('checked denominator',q, 'and forcing',e,f)

# For q=1,2,3 the exact primitive-period component count agrees with
# the subtraction of the circle components at earlier admissible periods.
for q in (1,2,3):
    for k in range(1,5):
        fixed_count = (4**(q*k)-1)//3
        previous = 0
        for d in range(1,k):
            if k%d == 0:
                from math import isqrt
                def mobius(v):
                    ps=0
                    for p in range(2,isqrt(v)+1):
                        if v%p==0:
                            v//=p;ps+=1
                            if v%p==0:return 0
                            while v%p==0:v//=p
                    if v>1:ps+=1
                    return (-1)**ps
                primitive_d=sum(mobius(d//j)*(4**(q*j)-1)//3 for j in range(1,d+1) if d%j==0)
                previous += primitive_d
        assert fixed_count - previous>0
print('All exact-rational sample checks passed')
