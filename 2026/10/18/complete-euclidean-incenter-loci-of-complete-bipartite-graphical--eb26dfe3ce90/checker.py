#!/usr/bin/env python3
"""Exact integer cut certificates and center-contact rank for complete-bipartite graphical zonotopes."""
from fractions import Fraction
from itertools import combinations
from math import isqrt

def rank(M):
    A=[[Fraction(v) for v in row] for row in M]
    if not A:return 0
    piv=0
    for col in range(len(A[0])):
        j=next((i for i in range(piv,len(A)) if A[i][col]),None)
        if j is None:continue
        A[piv],A[j]=A[j],A[piv]
        t=A[piv][col];A[piv]=[v/t for v in A[piv]]
        for i in range(len(A)):
            if i!=piv and A[i][col]:
                w=A[i][col];A[i]=[x-w*y for x,y in zip(A[i],A[piv])]
        piv+=1
        if piv==len(A):break
    return piv

def one(p,q):
    assert 2<=p<=q
    n=p+q
    A=range(p);B=range(p,n)
    cutsets=[]
    for mask in range(1,1<<(n-1)):
        # One representative per complementary cut; n-1 bit mask avoids final vertex
        S={i for i in range(n-1) if mask>>i&1}
        a=len(S&set(A));b=len(S&set(B))
        D=a*(q-b)+b*(p-a)
        s=a+b
        u=s*(n-s)
        # square of ratio D / ||Pi1_S||, divided by the reference ratio p*sqrt(n/(n-1))
        # D/sqrt(u/n) >= p*sqrt(n/(n-1)) iff D^2*(n-1) >= p^2*u
        relation=D*D*(n-1)-p*p*u
        cutsets.append((S,a,b,D,u,relation))
    if (p,q)==(2,2):
        # centered sphere radius 1, cut tangent iff D^2*n==4*u
        touching=[v for v in cutsets if v[3]**2*n==4*v[4]]
        assert len(touching)==2
        assert all(v[3]**2*n>=4*v[4] for v in cutsets)
    else:
        touching=[v for v in cutsets if v[-1]==0]
        assert len(touching)==(q if p<q else n),((p,q),len(touching))
        assert all(v[-1]>=0 for v in cutsets)
        assert all((v[-1]>0) or (len(v[0])==1 or len(v[0])==n-1) for v in cutsets)
    normal_rows=[]
    for v in touching:
        S=v[0];normal_rows.append([n*(i in S)-len(S) for i in range(n)])
    r=rank(normal_rows)
    predicted=2 if (p,q)==(2,2) else (q if p<q else n-1)
    assert r==predicted,((p,q),r,predicted)
    return len(touching),n-1-r

if __name__=='__main__':
    total=0
    for n in range(4,15):
      for p in range(2,n//2+1):
        q=n-p
        z,dim=one(p,q)
        print('K(%d,%d): antipodal contact facet-pairs %d, center dimension %d'%(p,q,z,dim))
        total+=1
    print('PASS %d exact complete-cut profiles'%(total))

# Finite high-precision cross-check of the explicit 2-by-q endpoint contacts.
# This supplements (and does not replace) the all-q analytical proof.
def endpoint_profile(q):
    from decimal import Decimal, localcontext
    from math import comb
    with localcontext() as ctx:
        ctx.prec=75
        n=q+2
        F=((q+2)**2)//4
        t=Decimal(q)/2-(Decimal(F)/Decimal(q+1)).sqrt()
        r=(Decimal(n)/Decimal(q+1)).sqrt()
        assert t>0
        counts=[]
        for sign in (-1,1):
            c=[sign*t,-sign*t]+[Decimal(0)]*q
            tang=0
            for mask in range(1,1<<(n-1)):
                subset=[i for i in range(n-1) if mask>>i&1]
                a=sum(i<2 for i in subset)
                b=len(subset)-a
                s=a+b
                D=a*(q-b)+b*(2-a)
                val=abs(sum((c[i] for i in subset),Decimal(0))) + r*(Decimal(s*(n-s))/Decimal(n)).sqrt()
                gap=Decimal(D)/2-val
                assert gap>Decimal('-1e-60'),(q,mask,str(gap))
                if abs(gap)<Decimal('1e-60'):
                    tang+=1
            # count represented unoriented cut pairs; each facet orientation separately.
            expected=q+(comb(q,q//2) if q%2==0 else 2*comb(q,(q-1)//2))
            assert tang==expected,(q,tang,expected)
            counts.append(tang)
        assert counts[0]==counts[1]
        return counts[0]*1

if __name__=='__main__':
    for q in range(3,12):
        print('K(2,%d): endpoint distinct facet-pair constraints tight %d'%(q,endpoint_profile(q)))
    print('PASS 9 high-precision endpoint contact profiles')
