#!/usr/bin/env python3
"""Independent exact rational-point counts for all 15 diagonal twist cosets.

Uses explicit quadratic fields and cube-residue enumeration, not curve-zeta
algorithms or the character-product routine.
"""
from collections import Counter

def factors(n):
    out=[]
    for k in range(2,n+1):
        if k*k>n: break
        if n%k==0:
            out.append(k)
            while n%k==0:n//=k
    if n>1:out.append(n)
    return out

def verify(p):
    assert p in (11,29)
    d=next(x for x in range(2,p) if pow(x,(p-1)//2,p)==p-1)
    q=p*p
    # a*p+b encodes a+b*w, where w*w=d; the field identity is p.
    def mul(x,y):
        a,b=divmod(x,p); c,e=divmod(y,p)
        return ((a*c+d*b*e)%p)*p+(a*e+b*c)%p
    def power(x,n):
        out=p
        while n:
            if n&1:out=mul(out,x)
            x=mul(x,x);n//=2
        return out
    def add(x,y):
        a,b=divmod(x,p); c,e=divmod(y,p)
        return ((a+c)%p)*p+(b+e)%p
    def neg(x):
        a,b=divmod(x,p)
        return (-a%p)*p+(-b%p)
    g=next(x for x in range(1,q) if all(power(x,(q-1)//ell)!=p for ell in factors(q-1)))
    elems=[p]
    for _ in range(q-2): elems.append(mul(elems[-1],g))
    assert len(set(elems))==q-1
    cube_set={power(t,3) for t in elems}
    t_data=[(power(t,5),power(t,q-2)) for t in elems]
    out=[]
    for r in range(15):
        a=power(g,r)
        n=2 # unique ramified points above t=0 and t=infinity
        for t5,inv_t in t_data:
            v=mul(neg(add(a,t5)),inv_t)
            if v==0:n+=1
            elif v in cube_set:n+=3
        # a^4*b has 15th-power class 4r, and gcd(4r,15)=gcd(r,15).
        gg=__import__('math').gcd(r,15)
        delta={15:10,1:0,3:0,5:-5}[gg]
        predicted=q+1+p*delta
        assert n==predicted,(p,r,n,predicted)
        out.append(n)
    print('FIELD',p, 'QUADRATIC_NONRESIDUE',d,'GENERATOR_INDEX',g)
    print('R0_TO_R14_POINT_COUNTS',out)
    print('FREQUENCIES',sorted(Counter(out).items()))
    print('VERIFY_COUNTS_OK',p)

if __name__=='__main__':
    verify(11)
    verify(29)
