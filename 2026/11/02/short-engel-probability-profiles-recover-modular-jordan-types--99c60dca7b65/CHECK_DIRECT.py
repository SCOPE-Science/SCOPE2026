#!/usr/bin/env python3
"""Direct finite group-law enumeration of iterated Engel word distributions."""
from collections import Counter
from fractions import Fraction
from itertools import product


def configuration(p, partition):
    d=sum(partition)
    edges=[]; offset=0
    for size in partition:
        for i in range(offset,offset+size-1): edges.append(i)
        offset+=size
    def N(v):
        w=[0]*d
        for i in edges: w[i]=v[i+1]
        return tuple(w)
    def T(v):
        z=N(v)
        return tuple((v[i]+z[i])%p for i in range(d))
    def act(v,k):
        for _ in range(k%p): v=T(v)
        return v
    vectors=list(product(range(p),repeat=d)); zero=(0,)*d
    elements=[(v,a) for v in vectors for a in range(p)]
    def mult(x,y):
        v,a=x; w,b=y; z=act(w,a)
        return (tuple((v[i]+z[i])%p for i in range(d)),(a+b)%p)
    def inverse(x):
        v,a=x
        w=act(v,(-a)%p)
        return (tuple(-t%p for t in w),-a%p)
    def comm(x,y):
        return mult(mult(mult(inverse(x),inverse(y)),x),y)
    def Nk(v,k):
        for _ in range(k):v=N(v)
        return v
    return d,vectors,zero,elements,comm,Nk

def verify(p,blocks):
    d,vectors,zero,elements,comm,Nk=configuration(p,blocks)
    total=len(elements)**2
    supports={k:set(Nk(v,k) for v in vectors) for k in range(1,p+1)}
    observed=[Counter() for k in range(1,p+1)]
    for x in elements:
        for y in elements:
            z=comm(x,y)
            for k in range(1,p+1):
                if k>=2:z=comm(z,y)
                assert z[1]==0
                observed[k-1][z[0]]+=1
    for k,counts in enumerate(observed,1):
        u=supports[k]
        spike=Fraction(1,p*p) if k==1 else Fraction(1,p)
        for z in vectors:
            prob=(spike if z==zero else 0)+(1-spike)/len(u) if z in u else (spike if z==zero else 0)
            expected=prob*total
            assert expected.denominator==1, (p,blocks,k,z,expected)
            assert counts[z]==expected.numerator,(p,blocks,k,z,counts[z],expected)
        assert sum(counts.values())==total
    print('CASE_OK',p,blocks,'group_order',len(elements),'image_sizes',[len(supports[k]) for k in range(1,p+1)],
        'word_lengths',p,'pairs',total)

if __name__=='__main__':
    for p,blocks in [(3,(3,1)),(3,(2,2)),(3,(2,1)),(5,(3,)),(5,(2,))]:
        verify(p,blocks)
    print('VERIFY_OK')
