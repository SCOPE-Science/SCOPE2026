"""Independent exact rational CTMC check for four-person household final sizes."""
from fractions import Fraction as Q
from functools import lru_cache
from math import comb

@lru_cache(None)
def survivors(s,i,rate):
    if i==0:
        return {s:Q(1)}
    infection=rate*s
    recovery=Q(1)
    total=infection+recovery
    d={}
    for target,prob in [(survivors(s-1,i+1,rate),infection/total)] if s else []:
        for j,val in target.items():d[j]=d.get(j,Q(0))+prob*val
    for j,val in survivors(s,i-1,rate).items():
        d[j]=d.get(j,Q(0))+recovery/total*val
    return d

if __name__ == '__main__':
    rate=Q(1); escape=Q(1,2); n=4
    PD=[Q(0)]*5
    for k in range(5):
        weight=Q(comb(n,k))*escape**(n-k)*(1-escape)**k
        for s,prob in survivors(n-k,k,rate).items():
            PD[n-s]+=weight*prob
    MU={k:sum((k-s)*prob for s,prob in survivors(k-1,1,rate).items()) for k in range(1,5)}
    assert sum(PD)==1
    print('CTMC_P',*[str(z) for z in PD])
    print('CTMC_MU',MU)
