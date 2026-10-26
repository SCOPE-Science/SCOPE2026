"""Finite pathwise verification for two-server FCFS tandem delay transfer."""
from itertools import product
from fractions import Fraction as Q

def departures(arrivals, services, c):
    x=y=Q(0)
    second=[]
    waiting1=[]
    waiting2=[]
    for a,s in zip(arrivals,services):
        w1=max(x-a,Q(0))
        x=max(a,x)+c
        w2=max(y-x,Q(0))
        y=max(x,y)+s
        waiting1.append(w1)
        waiting2.append(w2)
        second.append(y)
    return second, waiting1, waiting2

count=0
for c in [Q(0),Q(1,4),Q(1,2),Q(1)]:
    for gaps in product([Q(0),Q(1,4),Q(1),Q(2)],repeat=3):
        arrivals=[Q(0)]
        for g in gaps: arrivals.append(arrivals[-1]+g)
        for extras in product([Q(0),Q(1,4),Q(1)],repeat=4):
            services=[c+e for e in extras]
            ys,w1,w2=departures(arrivals,services,c)
            zs,_,_=departures(arrivals,services,Q(0))
            assert all(y==z+c for y,z in zip(ys,zs))
            count+=1
assert departures([Q(0),Q(1,10)], [Q(1,5),Q(1)],Q(1,2))[0][-1] != departures([Q(0),Q(1,10)],[Q(1,5),Q(1)],Q(0))[0][-1]+Q(1,2)
print('exact verified paths:',count)
