"""Exact finite checks for last-discovery probabilities on weighted cycles.

This script is independent of all nonstandard third-party packages and uses
exact rational arithmetic. Finite checks support, but cannot prove, the
assertions over every cycle size and every exchangeable edge law.
"""
from fractions import Fraction as Q
from itertools import permutations
from functools import lru_cache

def formula(resistance, k):
    r = tuple(map(Q, resistance))
    n = len(r)
    assert n >= 3 and 1 <= k < n and all(z > 0 for z in r)
    R = sum((r[(k+j) % n] for j in range(1, n-1)), Q(0))
    A = sum(r[j] for j in range(k + 1, n))
    return (1 - A / R) * r[k] / (R + r[k]) + A / R * r[k-1] / (R + r[k-1])

def linear_solve(M, b):
    n = len(b)
    x = [list(map(Q, row)) + [Q(b[i])] for i, row in enumerate(M)]
    for col in range(n):
        pivot = next((i for i in range(col, n) if x[i][col]), None)
        assert pivot is not None
        x[col], x[pivot] = x[pivot], x[col]
        v = x[col][col]
        x[col] = [z / v for z in x[col]]
        for i in range(n):
            if i != col:
                v = x[i][col]
                if v:
                    x[i] = [a - v * c for a, c in zip(x[i], x[col])]
    return [row[-1] for row in x]

def direct_absorption(resistance, last):
    """Unrelated approach: solve absorbing Markov equations by visited subsets."""
    r = tuple(map(Q, resistance))
    n = len(r)
    N = (1 << n) - 1
    @lru_cache(None)
    def solve(mask):
        if mask == N:
            return tuple(Q(0) for _ in range(n))
        inside = tuple(i for i in range(n) if mask & (1 << i))
        mat = [[Q(int(i == j)) for j in inside] for i in inside]
        rhs = [Q(0) for _ in inside]
        for a, u in enumerate(inside):
            for v, edge_index in (((u+1) % n, u), ((u-1) % n, (u-1) % n)):
                # Each conductance is the reciprocal of its edge resistance.
                cw = r[(u-1) % n]
                ccw = r[u]
                prob = (cw if edge_index == u else ccw) / (ccw + cw)
                if mask & (1 << v):
                    mat[a][inside.index(v)] -= prob
                elif (mask | (1 << v)) == N:
                    rhs[a] += prob * int(v == last)
                else:
                    rhs[a] += prob * solve(mask | (1 << v))[v]
        sol = linear_solve(mat, rhs)
        out = [Q(0)]*n
        for v, value in zip(inside, sol):
            out[v] = value
        return tuple(out)
    return solve(1)[0]

def main():
    count = 0
    # Direct independent finite-state Markov computations.
    for n in range(3, 6):
        cases = [tuple(Q(i*i+1) for i in range(n)), tuple(Q(i+2, i+1) for i in range(n))]
        for r in cases:
            for k in range(1,n):
                assert direct_absorption(r,k) == formula(r,k), (n, r, k)
                count+=1
            assert sum((formula(r,k) for k in range(1,n)), Q(0)) == 1
            count+=1
    # Exhaustive permutation averages for fixed multisets of nonidentical weights.
    for n in range(3,7):
        r=tuple(Q(i*i+1) for i in range(n))
        ps=list(permutations(r))
        for k in range(1,n):
            assert sum((formula(z,k) for z in ps), Q(0)) == Q(len(ps),n-1)
            count+=1
    # Conditioning on a random unordered multiset, including repeated entries.
    for r in [(1,1,1,2,3), (1,2,2,4), (1,1,1)]:
        ps=set(permutations(r));n=len(r)
        for k in range(1,n):
            assert sum((formula(z,k) for z in ps), Q(0)) == Q(len(ps),n-1)
            count+=1
    # A single nonuniform edge: exact explicit nonuniform counterexample.
    for n in range(3,10):
        for w in (Q(1,5),Q(1,2),Q(2),Q(5)):
            r=(Q(1),)*(n-1)+(1/w,)
            den = 1+(n-2)*w
            for k in range(1,n):
                wanted=(w if k<n-1 else 1)/den
                assert formula(r,k)==wanted,(n,w,k)
                count+=1
    print('PASS',count,'exact rational consistency assertions; no infinite proof inferred')

if __name__=='__main__':main()
