#!/usr/bin/env python3
"""Independent rational-volume checks for two-level ultrametric Lipschitz balls.

Directly count lattice points in integer dilates of the anchored difference-
constraint polytope. The constraint matrix is an anchored network incidence
matrix, hence integral right-hand sides give integral vertices. The leading
finite difference of the Ehrhart polynomial gives exact coordinate volume.
"""
from fractions import Fraction
from math import factorial, lcm


def direct_lattice_count(sizes, radii, Q, dilation):
    N = sum(sizes)
    group = tuple(j for j, n in enumerate(sizes) for _ in range(n))
    x = [0] * N
    def walk(i):
        if i == N:
            return 1
        total = 0
        for v in range(-Q*dilation, Q*dilation + 1):
            if all(abs(v-x[h]) <= dilation * (Q*radii[group[i]] if group[h] == group[i] else Q)
                   for h in range(i)):
                x[i] = v
                total += walk(i+1)
        return total
    return walk(1)


def formula(sizes, radii):
    overall = Fraction(1)
    for n,t in zip(sizes,radii):
        overall *= t**(n-1)
    value = Fraction(0)
    for j,n in enumerate(sizes):
        summand = Fraction(n)
        for i,(m,t) in enumerate(zip(sizes,radii)):
            if i != j:
                summand *= m-(m-1)*t
        value += summand
    return overall * value


def ehrhart_volume(sizes,radii):
    Q = lcm(*(r.denominator for r in radii))
    d = sum(sizes)-1
    count = [direct_lattice_count(sizes,radii,Q,s) for s in range(d+1)]
    v = count
    for _ in range(d):
        v = [b-a for a,b in zip(v,v[1:])]
    return Fraction(v[0], factorial(d)*Q**d)


def compositions(n,k):
    if k==1:
        yield (n,)
    else:
        for x in range(1,n-k+2):
            for rem in compositions(n-x,k-1):
                yield (x,)+rem


def main():
    cases = [
        ((1,1),(1,2)), ((2,1),(1,2)), ((2,2),(1,2)),
        ((3,1),(1,2)), ((1,1,2),(1,2)), ((2,1,1),(2,3)),
        ((3,2),(1,2)), ((1,2,2),(2,3)), ((1,1,3),(1,3)),
        ((2,2,1),(1,3)), ((1,1,1,2),(1,2)),
        ((1,3),(2,3)), ((2,2),(2,3)), ((1,1,1),(1,3)),
    ]
    checked=0
    for sizes,(p,q) in cases:
        radii = (Fraction(p,q),)*len(sizes)
        assert formula(sizes,radii)==ehrhart_volume(sizes,radii), (sizes,radii)
        checked+=1
    heterogeneous = [
        ((2,1),('1/2','2/3')), ((2,2),('1/2','3/4')),
        ((2,2),('1/2','2/3')), ((1,2,1),('1/3','2/3','1/2')),
        ((3,1),('1/3','1/2')), ((1,1,2),('1/2','3/4','1/2')),
    ]
    for sizes,strings in heterogeneous:
        radii = tuple(Fraction(s) for s in strings)
        assert formula(sizes,radii)==ehrhart_volume(sizes,radii), (sizes,radii)
        checked+=1
    transfers=0
    for N in range(3,13):
        for k in range(2,min(N,5)+1):
            for sizes in compositions(N,k):
                for i in range(k):
                    for j in range(k):
                        if sizes[i] >= sizes[j]+2:
                            new=list(sizes)
                            new[i]-=1;new[j]+=1
                            assert formula(new,(Fraction(2,3),)*k)>formula(sizes,(Fraction(2,3),)*k)
                            transfers+=1
    print(f'EXACT_EHRHART_VOLUME_PASS {checked} configurations (including 6 nonuniform radii)')
    print(f'STRICT_BALANCING_CHECK_PASS {transfers} transfers')

if __name__=='__main__':
    main()
