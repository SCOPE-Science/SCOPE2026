"""Exact finite verification of critical-density consecutive NSNP triples.

Uses integer trial factorization, cyclic subgroup enumeration, and an
independent Euler-criterion membership test. No external dependencies.
"""
from math import isqrt

LIMIT = 186624
EXPECTED_EXCEPTIONS = (7,13,19,25,37,49,73,97,109,163,487,577)


def factors(n):
    result={}
    p=2
    while p*p<=n:
        if n%p==0:
            e=0
            while n%p==0:
                n//=p;e+=1
            result[p]=e
        p=3 if p==2 else p+2
    if n>1:result[n]=1
    return result


def fields():
    # All solutions to 2**a * 3**b < LIMIT with a,b >=1.
    a=1
    rows=[]
    while 2**a*3+1<=LIMIT:
        b=1
        while 2**a*3**b+1<=LIMIT:
            q=2**a*3**b+1
            fact=factors(q)
            if len(fact)==1:
                p,e=next(iter(fact.items()))
                rows.append((q,p,e))
            b+=1
        a+=1
    return sorted(rows)


def work(q,p,e):
    if e==1:
        zero=0;one=1
        elts=range(q)
        add=lambda x,y:(x+y)%p
        mul=lambda x,y:(x*y)%p
    else:
        assert e==2
        d=next(t for t in range(2,p) if pow(t,(p-1)//2,p)==p-1)
        zero=(0,0);one=(1,0)
        elts=[(x,y) for y in range(p) for x in range(p)]
        add=lambda u,v:((u[0]+v[0])%p,(u[1]+v[1])%p)
        mul=lambda u,v:((u[0]*v[0]+d*u[1]*v[1])%p,(u[0]*v[1]+u[1]*v[0])%p)
    def power(x,n):
        y=one
        while n:
            if n&1:y=mul(y,x)
            x=mul(x,x);n>>=1
        return y
    # Primitive generator exists since finite-field multiplicative group is cyclic.
    g=next(x for x in elts if x!=zero and
            all(power(x,(q-1)//l)!=one for l in (2,3)))
    # Construct exact coset of sixth powers via primitive exponents.
    C=set()
    x=power(g,3)
    h=power(g,6)
    for _ in range((q-1)//6):
        assert x not in C
        C.add(x)
        x=mul(x,h)
    assert x==power(g,3)
    assert len(C)==(q-1)//6
    # Independent quadratic character and cubic-power membership test.
    test={x for x in elts if x!=zero and
          power(x,(q-1)//2)!=one and power(x,(q-1)//3)==one}
    assert C==test, (q,len(C),len(test))
    two=add(one,one)
    cnt=sum(add(x,one) in C and add(x,two) in C for x in C)
    return cnt


def main():
    rows=fields()
    assert len(rows)==31,(len(rows),rows)
    assert all(e<=2 for q,p,e in rows)
    data=[(q,work(q,p,e)) for q,p,e in rows]
    exceptions=tuple(q for q,n in data if n==0)
    assert exceptions==EXPECTED_EXCEPTIONS,(exceptions,EXPECTED_EXCEPTIONS)
    assert all(n>0 for q,n in data if q not in exceptions)
    print('FIELDS',len(rows),'EXCEPTIONS',list(exceptions))
    print('POSITIVE_COUNTS',[(q,n) for q,n in data if n>0])
    print('CERTIFICATE_OK')
if __name__=='__main__':main()
