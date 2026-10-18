#!/usr/bin/env python3
"""Independent stationary linear-system and current check for finite rings."""
from itertools import combinations
from math import exp
import numpy as np

for L in range(3, 12):
    states = list(combinations(range(L), 2))
    lookup = {s:i for i, s in enumerate(states)}
    for z in (0.13, 0.37, 0.8):
        P = np.zeros((len(states),len(states)))
        signed = np.zeros(len(states))
        for x, state in enumerate(states):
            ss = set(state)
            def add(new, probability, displacement):
                rotated = tuple(sorted((i-1) % L for i in new))
                P[x,lookup[rotated]] += probability
                signed[x] += probability * displacement
            if 0 not in ss:
                add(ss, 1, 0)
                continue
            available = [d for d in (-1,1) if d % L not in ss]
            if not available:
                add(ss, 1, 0)
                continue
            stay = z if len(available)==1 else z*z
            add(ss, stay, 0)
            for d in available:
                add((ss-{0})|{d%L}, (1-stay)/len(available), d)
        assert np.max(abs(P.sum(axis=1)-1)) < 1e-14
        A=P.T-np.eye(len(states)); A[-1,:]=1
        b=np.zeros(len(states));b[-1]=1
        numerical=np.linalg.solve(A,b)
        weights=np.array([z if i==0 and j==L-1 else
                          1 if i==0 else z*z if j==L-1 else
                          (1+z*z)/2 for i,j in states])
        expected=weights/weights.sum()
        T=(L-2)*(L+1)*(1+z*z)/4+z
        theoretical=-(1-z)**2/T
        assert max(abs(numerical-expected)) < 1e-12, (L,z)
        assert abs(numerical@signed-theoretical) < 1e-12, (L,z)
    print(f'L={L:2d}: independent linear solve and current confirmed at 3 parameter values')
print('PASS: numerical diagnostics; these tests are not an all-size proof.')
