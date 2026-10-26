"""Exact four-cycle qutrit certificate and sampled Fourier sharpness checks."""
from fractions import Fraction as Q
from itertools import product
from math import cos, sin, pi, sqrt

vectors = [(1,0,-1),(-1,2,-1),(-1,0,1),(1,-2,1)]
states = [tuple(Q(1,3)+Q(t,6) for t in v) for v in vectors]
assert all(min(s)>=0 and sum(s)==1 for s in states)
def squared_trace(i,j):
    return sum(abs(u-v) for u,v in zip(states[i],states[j]))**2

lhs = sum(squared_trace(t,(t+2)%4) for t in range(4))*Q(2,4)
rhs = sum(squared_trace(t,(t+a+b)%4) for t in range(4) for a,b in product((-1,0,1),repeat=2))*Q(1,36)
assert lhs==Q(20,9),(lhs,rhs)
assert rhs==Q(4,9),(lhs,rhs)
assert lhs/rhs==5

# For each sample, compute both sides of the exact qubit Bloch witness.
for m in (4,6,8,10,12):
    a=(1+2*cos(2*pi/m))/3
    for n in (1,2,3):
        points=list(product(range(m),repeat=n))
        def vec(x):
            t=2*pi*sum(x)/m
            return (cos(t),sin(t))
        def distance2(x,y):
            u,v=vec(x),vec(y)
            return sum((u[k]-v[k])**2 for k in range(2))
        far=sum(distance2(x,tuple((x[j]+(m//2 if j==i else 0))%m for j in range(n)))
                for x in points for i in range(n))/len(points)
        short=sum(distance2(x,tuple((x[i]+e[i])%m for i in range(n)))
                 for x in points for e in product((-1,0,1),repeat=n))/(len(points)*3**n)
        theoretical=2*n/(1-a**n)
        assert abs(far/short-theoretical)<1e-9,(m,n,far/short,theoretical)
print('PASS: exact qutrit ratio 5 and 15 qubit sharp-witness checks')
