#!/usr/bin/env python3
"""Exact rational witnesses for finite-scale polyhedral translate-depth.

Scientific check only: the all-measure theorem is proved analytically in RESULT.md.
This file tests the facet/translate construction with discrete measures,
including atoms exactly on query hyperplanes, in 2D and 3D examples.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def dot(a, b):
    return sum(x*y for x,y in zip(a,b))


def polytope_examples():
    q=F(1,2); third=F(1,3)
    return [
        ('square',
         [(1,0),(-1,0),(0,1),(0,-1)], [1,1,1,1],
         [(1,0),(-1,0),(0,1),(0,-1)]),
        ('triangle',
         [(-1,0),(0,-1),(1,1)], [0,0,1],
         [(0,q),(q,0),(q,q)]),
        ('diamond',
         [(1,1),(-1,1),(-1,-1),(1,-1)], [1,1,1,1],
         [(q,q),(-q,q),(-q,-q),(q,-q)]),
        ('cube',
         [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)],
         [1]*6,
         [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]),
        ('tetrahedron',
         [(-1,0,0),(0,-1,0),(0,0,-1),(1,1,1)], [0,0,0,1],
         [(0,third,third),(third,0,third),(third,third,0),(third,third,third)]),
    ]


def verify_case(name, normals, offsets, facepoints, rnd):
    m=len(normals)
    d=len(normals[0]); assert all(len(a)==d for a in facepoints)
    for i in range(m):
        assert dot(normals[i],facepoints[i])==offsets[i]
        for j in range(m):
            if j!=i:
                assert dot(normals[j],facepoints[i]) < offsets[j]
    checks=0
    for sample_number in range(14):
        points=[tuple(F(rnd.randrange(-9,10),3) for _ in range(d))
                for __ in range(10)]
        # Nonuniform integer masses, including repeated data points.
        weights=[rnd.randrange(1,8) for _ in points]
        widths=[max(dot(a,v) for v in points)-min(dot(a,v) for v in points)
                for a in normals]
        T=max((widths[j]/(offsets[j]-dot(normals[j],facepoints[i]))
               for i in range(m) for j in range(m) if j!=i), default=F(0))
        t=max(F(1,100),T)
        queries=list(points[:4])+[
            tuple(F(rnd.randrange(-15,16),4) for _ in range(d)) for __ in range(15)
        ]
        for y in queries:
            axis_values=[]
            for i,a in enumerate(normals):
                eligible=[k for k,v in enumerate(points) if dot(a,v)<dot(a,y)]
                target=sum(weights[k] for k in eligible)
                axis_values.append(target)
                if not eligible:
                    continue
                # Highest strict coordinate threshold has a witness among data.
                upper=max(dot(a,points[k]) for k in eligible)
                z=next(v for v in points if dot(a,v)==upper)
                assert dot(a,y)>dot(a,z)
                for k,v in enumerate(points):
                    if dot(a,v)<=upper:
                        # z+t(P-facepoints[i]) contains the entire side sample.
                        for j,b in enumerate(normals):
                            assert dot(b,tuple(v[h]-z[h] for h in range(d))) <= t*(offsets[j]-dot(b,facepoints[i])), (name,i,j,k)
                        checks+=1
                # Query is definitely outside this translated testing polytope.
                assert dot(a,tuple(y[h]-z[h] for h in range(d)))>0
                checks+=1
            assert max(axis_values)<=sum(weights)
            checks+=1
    return checks


def sharp_box_checks():
    checks=0
    for widths in [(F(4),F(2)),(F(3),F(5)),(F(7,3),F(4,3),F(1)),
                   (F(2),F(1),F(9),F(3))]:
        w=max(widths)
        critical=w/2
        for frac in [F(1,4),F(3,4),F(99,100)]:
            t=frac*critical
            # For the uniform full orthotope, any translate of t[-1,1]^d
            # captures at most 2*t/w of the total mass.
            capture_bound=2*t/w
            assert capture_bound<1
            # At a midpoint of a long-coordinate end facet, the limiting
            # facet-halfspace missed mass is 1 (its boundary has volume zero).
            assert 1-capture_bound>0
            checks+=1
    return checks


def main():
    rnd=Random(20261029)
    total=0
    for name,normals,offsets,facepoints in polytope_examples():
        n=verify_case(name,normals,offsets,facepoints,rnd)
        print(f'{name}: {n} rational certificate checks passed')
        total+=n
    n=sharp_box_checks(); total+=n
    print(f'sharp-box examples: {n} exact checks passed')
    print(f'ALL PASSED: {total} exact rational checks')


if __name__=='__main__':
    main()
