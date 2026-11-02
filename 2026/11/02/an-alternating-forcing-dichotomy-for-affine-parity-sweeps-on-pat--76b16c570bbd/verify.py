#!/usr/bin/env python3
"""Reproducible finite-field checks for affine neighbor-parity path sweeps.

Every state is represented as a tuple of characteristic-two field labels;
addition is bitwise XOR, including for all elements of GF(4).
This script checks finite examples only. The all-size theorem is algebraic.
"""
from itertools import product, permutations
from math import gcd
import random


def local_update(x, i, b):
    y = list(x)
    v = x[i] ^ b[i]
    if i:
        v ^= x[i-1]
    if i+1 < len(x):
        v ^= x[i+1]
    y[i] = v
    return tuple(y)


def sweep(x, order, b):
    for i in order:
        x = local_update(x, i, b)
    return x


def Phi(x):
    u=[0]*(len(x)+1)
    for i,a in enumerate(x):
        u[i] ^= a
        u[i+1] ^= a
    return tuple(u)


def reflected(u,i,b_i):
    v=list(u)
    v[i],v[i+1]=v[i+1],v[i]
    v[i] ^= b_i
    v[i+1] ^= b_i
    return tuple(v)


def predicted_fixed(n,q,b,t):
    N=n+1;g=gcd(N,t);L=N//g
    # obstruction is the characteristic-two sum of the even-index offsets.
    obstruction=0
    for i in range(0,n,2): obstruction ^= b[i]
    exceptional = (n%2==1 and obstruction != 0)
    if exceptional and L%2==0: return 0
    return q**(g if (L%2==0 and not exceptional) else g-1)


def run_exhaustive(n,q):
    states=list(product(range(q),repeat=n))
    checked_cases=0; checked_states=0
    for b in product(range(q),repeat=n):
        for order in permutations(range(n)):
            Y={x:sweep(x,order,b) for x in states}
            assert len(set(Y.values()))==len(states), ('noninvertible', n,q,b,order)
            for x in states:
                y=x
                for step in range(n+1):y=Y[y]
                assert y==x, ('N-order failure', n,q,b,order,x)
            N=n+1
            for t in range(1,N+1):
                if N%t:continue
                count=0
                for x in states:
                    y=x
                    for _ in range(t):y=Y[y]
                    count+=(y==x)
                expected=predicted_fixed(n,q,b,t)
                assert count==expected, ('fixed count', n,q,b,order,t,count,expected)
            checked_cases+=1;checked_states+=len(states)
    return checked_cases,checked_states


def random_tests():
    rng=random.Random(20261027)
    trials=0
    for n in range(2,41):
        N=n+1
        for rep in range(24):
            q=2 if rep%2==0 else 4
            x=tuple(rng.randrange(q) for _ in range(n))
            b=tuple(rng.randrange(q) for _ in range(n))
            i=rng.randrange(n)
            assert Phi(local_update(x,i,b))==reflected(Phi(x),i,b[i])
            order=list(range(n));rng.shuffle(order)
            y=x
            for _ in range(N): y=sweep(y,order,b)
            assert y==x, ('N-order failure randomized',n,q,b,order,x)
            trials+=1
    return trials


def main():
    exact_cases=exact_states=0
    for n,q in [(2,2),(3,2),(4,2),(5,2),(2,4),(3,4)]:
        a,b=run_exhaustive(n,q)
        exact_cases+=a;exact_states+=b
        print(f'EXHAUSTIVE_OK n={n} q={q} configurations={a} state_checks={b}')
    rt=random_tests()
    print(f'LOCAL_CONJUGACY_AND_ORDER_RANDOM_OK trials={rt}')
    print(f'AFFINE_PATH_ORBITS_VERIFY_OK exact_cases={exact_cases} exact_state_checks={exact_states} randomized_trials={rt}')

if __name__=='__main__':main()
