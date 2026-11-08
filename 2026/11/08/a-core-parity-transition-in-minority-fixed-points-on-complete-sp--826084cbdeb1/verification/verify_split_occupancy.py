"""Independent occupancy enumeration of minority fixed configurations."""
from math import comb

def occupancy(a,b):
    res=0
    for k in range(a+1):
        for l in range(b+1):
            # clique 1 needs at least half of neighbors of color 0
            if k and not 2*(k-1+l)<=a+b-1: continue
            # clique 0 needs at least half of neighbors of color 1
            if k<a and not 2*((a-k-1)+(b-l))<=a+b-1: continue
            # independent 1 must have at least as many 0 clique neighbors
            if l and not 2*k<=a: continue
            # independent 0 must have at least as many 1 clique neighbors
            if l<b and not 2*k>=a: continue
            res+=comb(a,k)*comb(b,l)
    return res

def closed(a,b):
    if a%2==1:return 2
    return 2+comb(a,a//2)*(comb(b,b//2) if b%2==0 else 2*comb(b,b//2))

if __name__=='__main__':
    for a in range(1,21):
        for b in range(a, a+25):
            assert occupancy(a,b)==closed(a,b),(a,b,occupancy(a,b),closed(a,b))
    for a in range(1,9):
        print('a=%d b=%d fixed=%d; b=%d fixed=%d' %(a,a,occupancy(a,a),a+1,occupancy(a,a+1)))
    print('PASS split occupancy; 500 parameter pairs')
