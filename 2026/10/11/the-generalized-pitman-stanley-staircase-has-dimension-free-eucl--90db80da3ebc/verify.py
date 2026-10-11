#!/usr/bin/env python3
import math

cases=0
for n in range(1,101):
    for m in range(2,51):
        r=1/(2+(m-1)*math.sqrt(2))
        y=[r*(1+(m-j)*math.sqrt(2)) for j in range(1,m+1)]

        assert abs(y[-1]-r)<1e-12
        assert abs(y[0]-(1-r))<1e-12
        for j in range(m-1):
            assert abs((y[j]-y[j+1])-r*math.sqrt(2))<1e-12

        for i in range(1,n+1):
            for j in range(m):
                assert y[j]+1e-12 >= r
            assert i*y[-1]+1e-12 >= r*math.sqrt(i)
            for j in range(m-1):
                assert i*(y[j]-y[j+1])+1e-12 >= r*math.sqrt(2*i)
            assert i*y[0] <= i-r*math.sqrt(i)+1e-12

        lhs=(1-r) - r - (m-1)*r*math.sqrt(2)
        assert abs(lhs)<1e-12

        if n>=2:
            eps=min(r*(i-math.sqrt(i))/(i-1) for i in range(2,n+1))/2
            assert eps>0
            for i in range(2,n+1):
                assert i*r+(i-1)*eps > r*math.sqrt(i)
                assert i*r*math.sqrt(2) > r*math.sqrt(2*i)
                assert i*(1-r)+(i-1)*eps < i-r*math.sqrt(i)
        cases+=1

print(f"VERIFY_OK generalized-Pitman-Stanley-inradius cases={cases} n<=100 m<=50")
