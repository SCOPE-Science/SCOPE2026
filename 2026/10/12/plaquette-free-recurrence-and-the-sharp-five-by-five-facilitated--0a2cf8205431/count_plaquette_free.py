"""Independent polynomial transfer-matrix count of 2x2-vacancy-free torus states."""
from collections import defaultdict
from math import comb

N=5; LIM=8; masks=list(range(1<<N))
def permitted(a,b):
    common=a&b
    return (common & ((common<<1 | common>>(N-1)) & ((1<<N)-1)))==0

def count():
    coeff=[0]*(LIM+1)
    successors=[[b for b in masks if permitted(a,b)] for a in masks]
    for first in masks:
        dp={(first,first.bit_count()):1}
        for _ in range(N-1):
            nxt=defaultdict(int)
            for (prev,k),cnt in dp.items():
                for b in successors[prev]:
                    t=k+b.bit_count()
                    if t<=LIM:nxt[(b,t)]+=cnt
            dp=nxt
        for (last,k),cnt in dp.items():
            if permitted(last,first):coeff[k]+=cnt
    return coeff
if __name__=='__main__':
    a=count()
    assert a==[1,25,300,2300,12625,52605,171900,448450,941450],a
    for h,v in enumerate(a):print(f'holes={h} plaquette_free={v} total={comb(25,h)}')
    print('COUNT_OK')
