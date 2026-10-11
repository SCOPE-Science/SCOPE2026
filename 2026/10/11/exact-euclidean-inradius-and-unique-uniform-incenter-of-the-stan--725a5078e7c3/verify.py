#!/usr/bin/env python3
import math

checks=0
for n in range(2,101):
    N=n+1
    M=(1<<n)-1
    r=M/math.sqrt(n*N)
    mu=M/N

    singleton_distance=mu/math.sqrt(n/N)
    assert abs(singleton_distance-r) < 1e-10*max(1.0,r)

    equal_sizes=[]
    for k in range(1,N):
        if k==1:
            z=0
        else:
            z=(1<<(k-1))-1
            # Exact monotonicity consequence used in the proof.
            assert N*(N-1)*z <= k*(k-1)*M
        slack=k*mu-z
        norm=math.sqrt(k*(N-k)/N)
        d=slack/norm
        assert d+1e-10*max(1.0,r) >= r
        if abs(d-r) < 1e-9*max(1.0,r):
            equal_sizes.append(k)
        checks+=1

    if n==2:
        assert equal_sizes==[1,2]
    else:
        assert equal_sizes==[1]

    # Direct stepwise monotonicity of F(j).
    for j in range(2,N):
        numerator=(j-3)*(1<<(j-1))+2
        assert numerator>=0

print(f"VERIFY_OK standard-stellohedron-inradius n=2..100 tube_size_checks={checks}")
