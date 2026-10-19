#!/usr/bin/env python3
"""Finite checks of the discrete polygonal runner-up identity (not a proof)."""
from itertools import combinations
from cmath import exp
from math import pi,sin,sqrt

checks=0
compared=0
maxerr=0.0
for N in range(4,19):
    root=[exp(2j*pi*t/N) for t in range(N)]
    for k in range(2,N-1):
        if k>N-2: continue
        M=sin(pi*k/N)/sin(pi/N)
        R=sqrt(max(0,M*M-4*(sin(pi*k/N)**2-sin(pi/N)**2)))
        imasks={frozenset((a+j)%N for j in range(k)) for a in range(N)}
        nearmasks={frozenset([*((a+j)%N for j in range(k-1)), (a+k)%N]) for a in range(N)}
        nearmasks|={frozenset([a%N,*((a+j)%N for j in range(2,k+1))]) for a in range(N)}
        assert not (nearmasks & imasks)
        others=[]
        near_max=[]
        actualbest=-1
        bestmasks=set()
        for tup in combinations(range(N),k):
            s=frozenset(tup)
            v=abs(sum(root[t] for t in tup))
            if s in imasks:
                assert abs(v-M)<1e-8
                continue
            compared+=1
            if v>actualbest+1e-9:
                actualbest=v; bestmasks={s}
            elif abs(v-actualbest)<1e-9:
                bestmasks.add(s)
            if s in nearmasks: near_max.append(v)
        if not near_max: raise AssertionError((N,k))
        assert abs(actualbest-R)<1e-8, (N,k,actualbest,R)
        assert bestmasks==nearmasks, (N,k,len(bestmasks),len(nearmasks),list(bestmasks^nearmasks)[:3])
        maxerr=max(maxerr,abs(actualbest-R))
        checks+=1
print(f'VERIFY_OK N=4..18, parameter_pairs={checks}, noninterval_subsets={compared}, maximum_error={maxerr:.3e}')
