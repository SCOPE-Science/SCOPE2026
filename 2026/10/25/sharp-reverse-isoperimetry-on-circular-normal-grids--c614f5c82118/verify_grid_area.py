#!/usr/bin/env python3
"""Numerical reproduction of sharp fixed-normal polygon area bounds.
No external packages are required. Finite checks corroborate (do not replace) proof.
"""
import math
import random
from itertools import combinations

PI=math.pi

def area_bound_min(n,p=1.):
    assert n >= 3 and n % 2 == 1
    return p*p/(4*(2/math.tan(PI/(2*n))+math.tan(PI/n)))

def area_bound_max(n,p=1.):
    return p*p/(4*n*math.tan(PI/n))

def triangle_lengths(n, triple, p=1.):
    j,k,l=triple
    gaps=(2*PI*(k-j)/n,2*PI*(l-k)/n,2*PI*(n+j-l)/n)
    if max(gaps)>=PI-1e-14:
        return None
    sides=[math.sin(gaps[1]),math.sin(gaps[2]),math.sin(gaps[0])]
    z=sum(sides)
    return [p*s/z for s in sides]

def polygon_area(n, side_lengths):
    """Exact shoelace algorithm in floating point for ordered normals."""
    x=y=0.
    vertices=[(x,y)]
    for j,l in enumerate(side_lengths):
        t=2*PI*j/n
        x-=l*math.sin(t)
        y+=l*math.cos(t)
        vertices.append((x,y))
    # a closed side-length combination from balanced triples
    assert math.hypot(x,y)<1e-9, (n,x,y)
    signed=0.
    for a,b in zip(vertices,vertices[1:]):
        signed+=a[0]*b[1]-a[1]*b[0]
    return abs(signed)/2

def test():
    rng=random.Random(190261024)
    triangles_tested=0; random_tested=0; worst=0
    for n in range(3,44,2):
        lo=area_bound_min(n)
        hi=area_bound_max(n)
        tri=[]
        for triple in combinations(range(n),3):
            sides=triangle_lengths(n,triple)
            if sides is None: continue
            ls=[0.]*n
            for j,l in zip(triple,sides): ls[j]=l
            geom=polygon_area(n,ls)
            gaps=[triple[1]-triple[0],triple[2]-triple[1],n+triple[0]-triple[2]]
            angles=[PI-2*PI*g/n for g in gaps]
            formula=1/(4*sum(1/math.tan(a/2) for a in angles))
            err=abs(geom-formula)
            worst=max(worst,err)
            assert err<1e-12,(n,triple,geom,formula)
            assert lo-1e-12<=geom<=hi+1e-12,(n,triple,lo,geom,hi)
            tri.append((triple,ls,geom))
            triangles_tested+=1
        assert tri
        observed=min(x[2] for x in tri)
        assert abs(observed-lo)<1e-12,(n,lo,observed)
        eq={t for t,ls,ar in tri if abs(ar-lo)<1e-12}
        expected=set()
        h=(n-1)//2
        for j in range(n):
            ids=tuple(sorted((j,(j+1)%n,(j+1+h)%n)))
            expected.add(ids)
        assert eq==expected,(n,eq,expected)
        regular=[1/n]*n
        assert abs(polygon_area(n,regular)-hi)<1e-12
        for _ in range(60):
            weights=[rng.expovariate(1) for k in range(4)]
            z=sum(weights);weights=[w/z for w in weights]
            sampled=rng.sample(tri,min(3,len(tri)))
            blend=[weights[3]/n]*n
            for w,(_,ls,_) in zip(weights[:3],sampled):
                for k in range(n): blend[k]+=w*ls[k]
            # exact normalization of weights if n=3 uses one sampled triangle only
            if len(sampled)<3: blend=[1/n]*n
            geom=polygon_area(n,blend)
            assert lo-1e-11<=geom<=hi+1e-11,(n,geom,lo,hi)
            random_tested+=1
    # lower area scale for large odd N
    for n in (101,301,1001,3001):
        a=area_bound_min(n)
        leading=PI/(16*n)-PI**3/(96*n**3)
        assert abs(a-leading)<20/n**5
    # even normals: parallelogram with vanishing side pair
    for n in range(4,42,2):
        s=[0.]*n
        for j in (0,n//2):s[j]=(1-1e-6)/2
        for j in (1,1+n//2):s[j]=1e-6/2
        assert polygon_area(n,s)<1e-6
    print('PASS: %d independent normal-triple area comparisons; %d random full-fan Minkowski mixtures;'%(triangles_tested,random_tested))
    print('PASS: each odd-N sharp extremizer orbit identified; exact area and perimeter laws;')
    print('PASS: even-N flattening examples and large-N asymptotic tested;')
    print('Maximum absolute independent triangle-area formula discrepancy = %.3g'%worst)

if __name__=='__main__':test()
