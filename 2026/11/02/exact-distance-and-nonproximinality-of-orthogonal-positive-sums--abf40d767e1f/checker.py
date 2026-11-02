#!/usr/bin/env python3
"""Finite consistency checks for alternating peak–valley distance formulas.

This program checks explicit rational piecewise-linear examples only. It does
not prove the theorems for arbitrary continuous functions.
"""
from fractions import Fraction as F
from itertools import combinations, product
from random import Random


def candidate_value(values, k):
    n = len(values)
    low = max(F(1, 2), min(values))
    best = low
    for indices in combinations(range(n), 2 * k - 1):
        highs = (values[indices[j]] for j in range(0, 2 * k - 1, 2))
        lows = (values[indices[j]] for j in range(1, 2 * k - 1, 2))
        cost = max(1 - min(highs), max(lows))
        best = min(best, cost)
    return best


def interpol(values, x):
    n = len(values) - 1
    if x == 1:
        return values[-1]
    j = int(x * n)
    v = x * n - j
    return (1 - v) * values[j] + v * values[j + 1]


def witness_grid(values, k, mesh_multiplier=4):
    n = len(values) - 1
    grid = [interpol(values, F(i, mesh_multiplier * n))
            for i in range(mesh_multiplier * n + 1)]
    best = F(1)
    for indices in combinations(range(len(grid)), 2 * k - 1):
        cost = max(1 - min(grid[indices[j]] for j in range(0, 2*k-1, 2)),
                   max(grid[indices[j]] for j in range(1, 2*k-1, 2)))
        best = min(best, cost)
    return best


def test_witness(values, k, points, delta):
    n = len(values) - 1
    alternating = list(range(2 * k - 1))
    assert len(points) == len(alternating)
    y = [values[i] for i in range(n + 1)]
    times = [F(i, n) for i in range(n + 1)]
    witness_times = [F(i, n) for i in points]
    assert all(witness_times[i] < witness_times[i+1]
               for i in range(len(witness_times)-1))
    assert max(1-y[points[i]] for i in range(0,len(points),2)) <= delta
    assert max(y[points[i]] for i in range(1,len(points),2)) <= delta
    wvalues = [F(1) if i%2==0 else F(0) for i in range(len(points))]

    def w(t):
        if t<=witness_times[0]:return F(1)
        if t>=witness_times[-1]:return F(1)
        for j in range(len(points)-1):
            if witness_times[j]<=t<=witness_times[j+1]:
                frac=(t-witness_times[j])/(witness_times[j+1]-witness_times[j])
                return wvalues[j]*(1-frac)+wvalues[j+1]*frac
        raise AssertionError
    for i in range(61):
        t=F(i,60); f=interpol(values,t)
        L=max(f-delta,F(0)); U=min(f+delta,F(1))
        g=L+(U-L)*w(t)
        assert F(0)<=g<=F(1) and abs(g-f)<=delta
    for j,t in enumerate(witness_times):
        f=interpol(values,t); L=max(f-delta,F(0)); U=min(f+delta,F(1))
        g=L+(U-L)*w(t)
        assert g == (F(1) if j%2==0 else F(0))


def run():
    count=0
    rng=Random(20261028)
    for n in range(3,8):
        for it in range(55):
            v=[F(rng.randrange(0,17),16) for _ in range(n+1)]
            v[rng.randrange(n+1)] = F(1)
            for k in range(2,min(4,n//2+1)):
                predicted = candidate_value(v,k)
                fine = witness_grid(v,k,mesh_multiplier=2)
                assert predicted <= fine
                count +=1
                if k+1<=min(4,n//2+1):
                    assert predicted <= candidate_value(v,k+1)
                    count+=1
    # A few exact known cases, including endpoint-sensitive failure of attainment
    for k in range(2,7):
        for n in range(2*k-2,2*k+6):
            v=[F(i,n) for i in range(n+1)]
            assert candidate_value(v,k)==F(1,2)
            count+=1
    # Every vertex witness is realizable by an explicit continuous g.
    for k,n in ((2,5),(3,7),(4,9)):
        for points in combinations(range(n+1),2*k-1):
            if points[0] !=0 or points[-1]!=n: continue
            vals=[F(1) if j%2==0 else F(0) for j in range(2*k-1)]
            v=[]
            for i in range(n+1):
                if i<=points[0]:v.append(vals[0]);continue
                if i>=points[-1]:v.append(vals[-1]);continue
                for j in range(len(points)-1):
                    if points[j]<=i<=points[j+1]:
                        v.append(vals[j]+(vals[j+1]-vals[j])*F(i-points[j],points[j+1]-points[j]));break
            test_witness(v,k,points,F(0))
            count+=1
    # threshold witness at delta>0 with rational positive data.
    for k,n in ((2,5),(3,7)):
        for _ in range(80):
            points=sorted(rng.sample(range(n+1),2*k-1))
            v=[F(rng.randrange(0,17),16) for _ in range(n+1)]
            v[points[0]]=F(1)
            delta=max([1-v[points[j]] for j in range(0,2*k-1,2)]+[v[points[j]] for j in range(1,2*k-1,2)])
            test_witness(v,k,points,delta)
            count+=1
    print(f"PASS: {count} rational finite consistency checks")


if __name__=='__main__':run()
