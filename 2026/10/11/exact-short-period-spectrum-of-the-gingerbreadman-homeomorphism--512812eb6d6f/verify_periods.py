#!/usr/bin/env python3
"""Exact rational exhaustive sign-word checker for the gingerbreadman map.

No numerical solver or external dependencies. Enumerates every sign itinerary of
length 1 through 11 and solves each affine periodicity system over Q; Fourier-
Motzkin elimination decides sign feasibility also for singular systems.
"""
from fractions import Fraction as Q
from itertools import product
from collections import defaultdict


def linear_solutions(signs):
    """Return affine rational solutions x=x0+sum_j t_j*v_j, or None."""
    n = len(signs)
    a = [[Q(0) for _ in range(n+1)] for k in range(n)]
    for i, sig in enumerate(signs):
        a[i][(i-1) % n] += 1
        a[i][(i+1) % n] += 1
        a[i][i] -= sig
        a[i][-1] = 1
    pivots = []
    row = 0
    for col in range(n):
        pivot = next((k for k in range(row, n) if a[k][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        div = a[row][col]
        a[row] = [e / div for e in a[row]]
        for k in range(n):
            if k != row and a[k][col]:
                t = a[k][col]
                a[k] = [v - t*w for v,w in zip(a[k], a[row])]
        pivots.append(col)
        row += 1
    if any(not any(a[k][i] for i in range(n)) and a[k][-1] for k in range(n)):
        return None
    free = [i for i in range(n) if i not in pivots]
    x0 = [Q(0)] * n
    direction = [[Q(0)] * n for _ in free]
    for j,f in enumerate(free):
        direction[j][f] = 1
    for r,p in enumerate(pivots):
        x0[p] = a[r][-1]
        for j,f in enumerate(free):
            direction[j][p] = -a[r][f]
    return x0, direction


def fm_feasible(inequalities, dimensions):
    """Test affine rational feasibility via exact Fourier-Motzkin elimination.

    Each tuple (c0,c1,..,cd) means c0+sum ci*ti >= 0.
    """
    inequalities = list(inequalities)
    for dim in range(dimensions, 0, -1):
        pos, neg, zero = [], [], []
        for v in inequalities:
            if v[dim] > 0:
                pos.append(v)
            elif v[dim] < 0:
                neg.append(v)
            else:
                zero.append(v[:dim])
        if pos and neg:
            for p in pos:
                for m in neg:
                    zero.append(tuple(-m[dim]*p[k]+p[dim]*m[k] for k in range(dim)))
        inequalities = zero
        if any(all(w == 0 for w in v[1:]) and v[0] < 0 for v in inequalities):
            return False
    return all(v[0] >= 0 for v in inequalities)


def itinerary_feasible(signs, sol):
    x0, vecs = sol
    constraints = [(signs[i]*x0[i],) + tuple(signs[i]*v[i] for v in vecs)
                   for i in range(len(signs))]
    return fm_feasible(constraints, len(vecs))


def f(x,y):
    return (1-y+abs(x),x)


def orbit(x,y,n):
    result = []
    for _ in range(n):
        result.append((x,y))
        x,y = f(x,y)
    assert result[0] == (x,y), (result,x,y)
    return result


def canonical(cycle):
    v = tuple(cycle)
    return min(tuple(v[j:]+v[:j]) for j in range(len(v)))


def prime_period(points):
    for i in range(1,len(points)+1):
        if len(points)%i==0 and all(points[j]==points[j%i] for j in range(len(points))):
            return i
    return len(points)


def monodromy(xs):
    m = ((1,0),(0,1))
    def mm(a,b):
        return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    for x in xs:
        s = 1 if x>0 else -1 if x<0 else None
        if s is None:
            return None
        m = mm(((s,-1),(1,0)),m)
    return m


def main():
    isolated_orbits = defaultdict(set)
    stats = []
    for n in range(1,12):
        feasible_signs = 0
        singular_feasible = 0
        isolated = set()
        singular_rejected = 0
        for s in product((1,-1), repeat=n):
            sol = linear_solutions(s)
            if sol is None:
                continue
            if not itinerary_feasible(s, sol):
                if sol[1]:
                    singular_rejected += 1
                continue
            feasible_signs += 1
            if sol[1]:
                singular_feasible += 1
                continue
            xs = sol[0]
            pairs = orbit(xs[0], xs[-1], n)
            c = canonical(pairs)
            isolated.add(c)
            if prime_period(pairs)==n:
                isolated_orbits[n].add(c)
        stats.append((n,feasible_signs,singular_feasible,len(isolated),len(isolated_orbits[n]),singular_rejected))
        print('n=%2d feasible_signs=%3d singular_feasible=%3d isolated_points_orbits=%2d primitive_isolated_orbits=%2d singular_rejected=%3d'%stats[-1])
        if n in (5,11):
            for c in sorted(isolated_orbits[n]):
                xs = tuple(v[0] for v in c)
                print('  xs=',xs,'monodromy=',monodromy(xs))
    # Witness for p=6, and p=1 is the sole fixed point.
    six = orbit(Q(1,2),Q(1,4),6)
    print('six-cycle witness:',six, 'minimal period:',prime_period(six))
    assert prime_period(six)==6
    assert [n for n in range(1,12) if isolated_orbits[n] or any(i==n and j for i,_,j,_,_,_ in stats)]==[1,5,6,11]
    assert len(isolated_orbits[5])==2
    assert len(isolated_orbits[11])==2
    assert [(v[1],v[2],v[4]) for v in stats] == [(1,0,1),(1,0,0),(1,0,0),(1,0,0),(11,0,2),(13,7,1),(1,0,0),(1,0,0),(1,0,0),(11,0,0),(23,0,2)]
    assert {sum(monodromy(tuple(v[0] for v in c))[i][i] for i in range(2)) for c in isolated_orbits[5]} == {1,3}
    assert {sum(monodromy(tuple(v[0] for v in c))[i][i] for i in range(2)) for c in isolated_orbits[11]} == {-5,5}
    print('CERT_OK: primitive periods through 11 = {1,5,6,11}; two 5-orbits and two 11-orbits')

if __name__=='__main__':
    main()
