"""Independent enumeration checks for idempotent-product statistics in Rees matrix semigroups.
Run: python verify.py
The theoretical infinite-parameter theorem is proved in RESULT.md; these are finite tests.
"""
from collections import Counter
from fractions import Fraction
from itertools import product, permutations
from math import comb


def group(name):
    if name.startswith('C'):
        h=int(name[1:]); return list(range(h)), lambda x,y:(x+y)%h, lambda x:(-x)%h
    el=list(permutations(range(3)))
    comp=lambda x,y: tuple(x[y[i]] for i in range(3))
    ident=(0,1,2)
    inv={x:next(y for y in el if comp(x,y)==ident and comp(y,x)==ident) for x in el}
    return el,comp,lambda x:inv[x]


def brute(P, elems, mul, inv):
    r=len(P); n=len(P[0]); unit=elems[0]
    if mul(unit,elems[0])!=unit:
        raise AssertionError('Identity element must come first')
    E=[(i,inv(P[lam][i]),lam) for lam in range(r) for i in range(n)]
    def prod(x,y):
        i,g,lam=x; j,h,mu=y
        return i,mul(mul(g,P[lam][j]),h),mu
    return sum(prod(prod(e,f),prod(e,f))==prod(e,f) for e in E for f in E)


def formula(P, elems, mul, inv):
    r=len(P); n=len(P[0]); answer=r*n*n
    for lam in range(r):
        for mu in range(lam+1,r):
            N=Counter(mul(P[lam][i],inv(P[mu][i])) for i in range(n))
            answer+=2*sum(z*z for z in N.values())
    return answer


def check(name,r,n):
    elems,mul,inv=group(name)
    h=len(elems); trials=h**(r*n)
    s=0; s2=0; minv=None; maxv=None
    for flat in product(elems,repeat=r*n):
        P=[flat[a*n:(a+1)*n] for a in range(r)]
        u=brute(P,elems,mul,inv)
        v=formula(P,elems,mul,inv)
        assert u==v, (name,r,n,P,u,v)
        s+=u; s2+=u*u
        minv=u if minv is None else min(minv,u)
        maxv=u if maxv is None else max(maxv,u)
    mean=Fraction(s,trials); variance=Fraction(s2,trials)-mean*mean
    c=comb(r,2)
    m_expect=Fraction(r*n*n,1)+2*c*(Fraction(n*n,h)+Fraction(n*(h-1),h))
    v_expect=Fraction(8*c*n*(n-1)*(h-1),h*h)
    assert mean==m_expect, (name,r,n,mean,m_expect)
    assert variance==v_expect, (name,r,n,variance,v_expect)
    print('PASS',name,'rows',r,'columns',n,'labelings',trials,
          'Bmean',str(mean),'Bvariance',str(variance),'min/max',minv,maxv)

if __name__=='__main__':
    for name,r,n in [('C2',2,2),('C2',3,3),('C3',2,3),('S3',2,2),('S3',3,2)]:
        check(name,r,n)
    print('ALL_CHECKS_OK')
