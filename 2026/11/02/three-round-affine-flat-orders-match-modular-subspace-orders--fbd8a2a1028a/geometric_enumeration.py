#!/usr/bin/env python3
"""Independent direct three-round profiles from finite-field subspace incidence.

Uses explicit bit-set families over prime fields and scans third elements;
does not use the symbolic extension-table formulas.
"""
import itertools

def rref_bases(n,p,k):
    for pivots in itertools.combinations(range(n),k):
        positions=[(i,j) for i in range(k) for j in range(n)
                   if j not in pivots and j>pivots[i]]
        for values in itertools.product(range(p),repeat=len(positions)):
            rows=[[0]*n for _ in range(k)]
            for i,j in enumerate(pivots):rows[i][j]=1
            for (i,j),v in zip(positions,values):rows[i][j]=v
            yield rows

def flats(n,p,affine):
    points=list(itertools.product(range(p),repeat=n))
    ids={v:i for i,v in enumerate(points)}
    values=[];ranks=[];directions=[];representatives={}
    if affine:
        values.append(0);ranks.append(0);directions.append(0)
        representatives[0]=0
    for k in range(n+1):
        for basis in rref_bases(n,p,k):
            vectors=[tuple(sum(c*row[j] for c,row in zip(co,basis))%p
                           for j in range(n))
                     for co in itertools.product(range(p),repeat=k)]
            direction=0
            for v in vectors:direction|=1<<ids[v]
            if affine:
                seen=set()
                for shift in points:
                    b=0
                    for v in vectors:
                        v2=tuple((v[j]+shift[j])%p for j in range(n))
                        b|=1<<ids[v2]
                    if b in seen:continue
                    seen.add(b)
                    values.append(b);ranks.append(k+1)
                    directions.append(direction);representatives[k+1]=len(values)-1
            else:
                values.append(direction);ranks.append(k)
                directions.append(direction);representatives[k]=len(values)-1
    return values,ranks,directions,representatives

def relation(a,b):
    if a==b:return 0
    if a&b==a:return 1
    if a&b==b:return 2
    return 3

def structure_profile(n,p,affine):
    F,R,D,reps=flats(n,p,affine)
    nflat=len(F)
    qlog={p**j:j for j in range(n+1)}
    pointed=[];pair_orbits=0
    for rank,i in sorted(reps.items()):
        x=F[i]
        orbit={}
        for j,y in enumerate(F):
            inter=qlog[(D[i]&D[j]).bit_count()] if x and y else -1
            # An affine orbit is determined by directional intersection and
            # whether affine flats meet; linear orbits need only intersection.
            key=(R[j],inter,bool(x&y) if affine else True)
            orbit.setdefault(key,j)
        types=set()
        for j in orbit.values():
            mask=0
            for z in F:
                mask|=1<<(4*relation(x,z)+relation(F[j],z))
            types.add((relation(x,F[j]),mask))
            pair_orbits+=1
        pointed.append(frozenset(types))
    return frozenset(pointed),len(F),pair_orbits

def run():
    saved={}
    cases=[(1,2,True),(1,3,True),(1,5,True),(2,2,True),
           (2,3,True),(2,5,True),(3,2,True),(3,3,True),
           (4,2,True),(4,3,True),(5,2,True),(6,2,True),
           (2,2,False),(2,3,False),(3,2,False),(3,3,False),
           (4,2,False),(4,3,False),(5,2,False),(6,2,False)]
    for n,p,affine in cases:
        theory,size,orbits=structure_profile(n,p,affine)
        saved[n,p,affine]=theory
        print(f'PASS observed {"affine" if affine else "linear"}: '
              f'dimension={n}, p={p}, flats={size}, pair_orbits={orbits}')
    assert saved[1,2,True]!=saved[1,3,True]
    assert saved[1,3,True]==saved[1,5,True]
    assert saved[2,2,True]==saved[2,3,True]==saved[2,5,True]
    assert saved[3,2,True]==saved[3,3,True]
    assert saved[4,2,True]==saved[4,3,True]
    assert saved[5,2,True]==saved[6,2,True]
    for d in range(2,6):
        assert saved[d,2,True]==saved[d+1,2,False],d
    assert saved[1,3,True]==saved[2,2,False]
    assert len({saved[1,2,True],saved[1,3,True],
                *[saved[d,2,True] for d in range(2,7)]})==6
    print('PASS: direct field-independence in available dimensions')
    print('PASS: affine/projective comparison in dimensions two through five')
    print('PASS: stable affine dimensions five and six')
    print('PASS: six directly observed theories')

if __name__=='__main__':
    run()
