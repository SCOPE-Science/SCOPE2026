"""Exact arithmetic reproducibility checks for one open doubling-map theorem."""
from fractions import Fraction as Q
from functools import reduce

M = ((1,1,1,0,0), (0,0,0,1,1), (1,0,0,0,0),
     (0,1,0,0,0), (0,0,0,1,1))
length = (Q(1,3),Q(1,6),Q(1,6),Q(1,12),Q(1,6))
parts = ((Q(0),Q(1,3)), (Q(1,3),Q(1,2)),
         (Q(1,2),Q(2,3)), (Q(2,3),Q(3,4)),
         (Q(5,6),Q(1)))

def power_mv(v):
    return tuple(sum(m*vj for m,vj in zip(row,v)) for row in M)

def gf_coeffs(n):
    # From 3(4-2z-z^2)^2 F = z(44-4z-15z^2-3z^3).
    # Denominator = 48-48z-12z^2+12z^3+3z^4.
    p=[Q(0)]*(n+1)
    for k in range(1,n+1):
        rhs=Q({1:44,2:-4,3:-15,4:-3}.get(k,0))
        for j,a in ((1,-48),(2,-12),(3,12),(4,3)):
            if k>=j: rhs -= a*p[k-j]
        p[k]=rhs/48
    return p

def enumerate_survivors(n):
    # Independent geometry: repeated inverse images of the surviving set.
    # Endpoints are null, so intervals are represented by interiors.
    intervals = [(Q(0),Q(3,4)),(Q(5,6),Q(1))]
    for _ in range(1,n):
        inv=[]
        for a,b in intervals:
            inv.extend(((a/2,b/2),((a+1)/2,(b+1)/2)))
        next_intervals=[]
        for a,b in inv:
            for c,d in ((Q(0),Q(3,4)),(Q(5,6),Q(1))):
                lo=max(a,c);hi=min(b,d)
                if lo<hi:next_intervals.append((lo,hi))
        intervals=next_intervals
    return intervals

def test():
    probs=gf_coeffs(30)
    v=length
    for n in range(1,31):
        mat=sum(v)/2**(n-1)
        assert mat==probs[n],('matrix-gf',n,mat,probs[n])
        if n<=12:
            pieces=enumerate_survivors(n)
            direct=sum((b-a for a,b in pieces),Q(0))
            assert direct==probs[n],('geometry',n,direct,probs[n])
        v=power_mv(v)
    # The switch time exact decomposition at selected n, with state order A,C and B,D,E.
    U=((1,1),(1,0));V=((0,1,1),(1,0,0),(0,1,1)); C=((1,0,0),(0,0,0))
    def apply(A,v):return tuple(sum(a*w for a,w in zip(row,v)) for row in A)
    for n in (2,3,4,6,9,14,20,30):
        ell_u=(length[0],length[2]);ell_v=(length[1],length[3],length[4])
        tot=sum(apply(U,ell_u)) if False else Q(0)
        curr_u=ell_u
        for k in range(n-1):curr_u=apply(U,curr_u)
        upstream=sum(curr_u)
        curr_v=ell_v
        for k in range(n-1):curr_v=apply(V,curr_v)
        downstream=sum(curr_v)
        switches=Q(0)
        for j in range(1,n):
            w=ell_v
            for _ in range(n-1-j):w=apply(V,w)
            w=apply(C,w)
            for _ in range(j-1):w=apply(U,w)
            switches+=sum(w)
        assert (upstream+downstream+switches)/2**(n-1)==probs[n],('switch',n)
    print('VERIFY_OK: 30 transfer-vs-generating-function, 12 independent exact-geometry, 8 exact phase-decomposition checks')

if __name__=='__main__':test()
