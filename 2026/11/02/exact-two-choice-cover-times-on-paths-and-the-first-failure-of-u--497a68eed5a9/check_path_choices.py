#!/usr/bin/env python3
"""Exact finite-state checks for two-candidate walk cover times on paths.

Run: python3 check_path_choices.py
Pure Python standard library; all identities use fractions.Fraction.
"""
from fractions import Fraction as Q
from itertools import product

TESTS = 0

def check(condition, message):
    global TESTS
    TESTS += 1
    if not condition:
        raise AssertionError(message)


def one_way(N, x):
    """Optimal mean time to reach right endpoint N from x on path 0,...,N."""
    return sum((Q(2) - Q(1, 3**j) for j in range(x, N)), Q(0))


def exit_time(N, x):
    """Optimal mean time from x to {0,N}."""
    d = min(x, N-x)
    m = N//2
    if N%2 == 0:
        return Q(2*d) - Q(3**(d+1)-3, 2*3**m)
    return Q(2*d) - Q(3**(d+1)-3, 3**(m+1))


def remaining(N, l, r, x):
    """Optimal remaining time after interval [l,r] has been visited."""
    check(0 <= l <= x <= r <= N, (N,l,r,x))
    if l == 0 and r == N:
        return Q(0)
    if l == 0:
        return one_way(N, x)
    if r == N:
        return one_way(N, N-x)
    return one_way(N, 0) + exit_time(N, x)


def lin_solve(A, b):
    """Exact Gaussian elimination for a rational linear system."""
    M = [list(row) + [val] for row, val in zip(A, b)]
    n = len(M)
    for j in range(n):
        k = next((r for r in range(j,n) if M[r][j]), None)
        check(k is not None, ('singular policy',j))
        M[j],M[k] = M[k],M[j]
        z = M[j][j]
        M[j] = [v/z for v in M[j]]
        for k in range(n):
            if k == j:continue
            z = M[k][j]
            if z:
                M[k] = [u-z*v for u,v in zip(M[k],M[j])]
    return [row[-1] for row in M]


def evaluate_policy(N, target, flags):
    """Solve hitting time for one deterministic stationary preference policy."""
    states = [x for x in range(N+1) if x not in target]
    idx = {x:i for i,x in enumerate(states)}
    A = [[Q(int(i==j)) for j in range(len(states))] for i in range(len(states))]
    b = [Q(1) for _ in states]
    for i,x in enumerate(states):
        if x == 0:
            transitions = [(1,Q(1))]
        elif x == N:
            transitions = [(N-1,Q(1))]
        elif flags[x-1] == 0:
            transitions = [(x-1,Q(3,4)),(x+1,Q(1,4))]
        else:
            transitions = [(x-1,Q(1,4)),(x+1,Q(3,4))]
        for y,p in transitions:
            if y in idx:A[i][idx[y]] -= p
    sol = lin_solve(A,b)
    return dict(zip(states,sol))


def independent_policy_enumeration(N, target):
    """Enumerate every preference policy and take coordinatewise exact minima."""
    best={x:None for x in range(N+1) if x not in target}
    for flags in product((0,1),repeat=max(N-1,0)):
        vals = evaluate_policy(N,target,flags)
        for x,v in vals.items():
            if best[x] is None or v<best[x]: best[x]=v
    return best


def main():
    # Verify optimality by entirely explicit finite-state Bellman equations.
    for n in range(2,22):
        N=n-1
        for l in range(n):
            for r in range(l,n):
                for x in range(l,r+1):
                    v=remaining(N,l,r,x)
                    if l==0 and r==N:
                        check(v==0, ('terminal',n,l,r,x))
                        continue
                    neigh=[y for y in (x-1,x+1) if 0<=y<=N]
                    fut=[remaining(N,min(l,y),max(r,y),y) for y in neigh]
                    w = Q(1)+ (fut[0] if len(fut)==1 else
                               (3*min(fut)+max(fut))/4)
                    check(v == w, ('Bellman',n,l,r,x,v,w))
        # Verify that no unvisited-neighbor priority violation exists on P_n, n<=5.
        if n<=5:
            for l in range(n):
                for r in range(l,n):
                    for x in range(l,r+1):
                        neigh=[y for y in (x-1,x+1) if 0<=y<=N]
                        seen=[y for y in neigh if l<=y<=r]
                        unseen=[y for y in neigh if y<l or y>r]
                        if seen and unseen:
                            y=seen[0];z=unseen[0]
                            check(remaining(N,min(l,z),max(r,z),z)<=remaining(N,l,r,y),
                                  ('early greedy violation',n,l,r,x,y,z))
        if n>=5:
            u=remaining(N,1,2,1)
            v=remaining(N,1,3,3)
            if n%2:
                delta=Q(4)-Q(4,3**((n-5)//2))
            else:
                delta=Q(4)-Q(8,3**((n-4)//2))
            check(v-u==delta,('gap',n,v-u,delta))
            if n>=6:check(delta>0,('strict',n))
            else:check(delta==0,('tie',n))
    # Independent computation: enumerate all deterministic stationary
    # two-neighbor preference maps, solve their full exact linear systems,
    # take optimal coordinatewise values. This does not use Bellman recurrences.
    for N in range(1,9):
        for target in ({N},{0,N}):
            values=independent_policy_enumeration(N,target)
            for x,v in values.items():
                pred=one_way(N,x) if len(target)==1 else exit_time(N,x)
                check(v==pred, ('policy enumeration',N,tuple(sorted(target)),x,v,pred))
    check(remaining(5,1,2,1)==Q(833,81),'P6 seen continuation')
    check(remaining(5,1,3,3)==Q(941,81),'P6 unseen continuation')
    check(remaining(5,1,3,3)-remaining(5,1,2,1)==Q(4,3),'P6 gap')
    print('PASS: %s exact rational checks; n=2..21 Bellman and n=2..9 all-policy enumeration; P6 gap=4/3.'%TESTS)

if __name__=='__main__':main()
