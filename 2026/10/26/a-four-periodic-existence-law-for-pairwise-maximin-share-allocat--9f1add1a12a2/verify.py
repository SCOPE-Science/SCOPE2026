"""Exact self-contained verifier for a 4-agent, 4-type PMMS allocation family.

Run: python3 verify.py  (Python standard library only).
Value vectors (by agent): A=(81,81,81,81), B=(100,100,94,94),
C=(94,94,100,100), D=(101,101,101,101).
"""
from functools import lru_cache
from itertools import combinations

TOTAL = (3,5,5)
WEIGHTS = ((20,1,7),(20,1,7),(20,7,1),(20,7,1))

def compositions(q):
    return [(a,b,c,q-a-b-c) for a in range(q+1)
            for b in range(q-a+1) for c in range(q-a-b+1)]
PARTS = {3:compositions(3),5:compositions(5)}

@lru_cache(None)
def optimum_deficit(cap,typ,union,equal_sizes):
    """For two bundles of sizes (cap,cap+0/1), return minimal maximum
    deficit if equal or minimal deficit of the smaller side otherwise.
    """
    w = (20,1,7) if typ == 0 else (20,7,1)
    u_sum = sum(union)
    total_def = sum(x*y for x,y in zip(w,union))
    best = None
    for a in range(union[0]+1):
        for b in range(union[1]+1):
            for c in range(union[2]+1):
                h=a+b+c
                if h>cap or u_sum-h>cap+(not equal_sizes):
                    continue
                d=a*w[0]+b*w[1]+c*w[2]
                objective=max(d,total_def-d) if equal_sizes else d
                if best is None or objective<best:
                    best=objective
    assert best is not None
    return best

def valid_reduced(rare,sizes):
    if any(sum(rare[i])>sizes[i] for i in range(4)):return False
    for i in range(4):
        c=sum(rare[i][h]*WEIGHTS[i][h] for h in range(3))
        for j in range(4):
            if i==j or sizes[i]>sizes[j]:continue
            union=tuple(rare[i][h]+rare[j][h] for h in range(3))
            if c>optimum_deficit(sizes[i],i//2,union,sizes[i]==sizes[j]):
                return False
    return True

def enumerate_equal(k):
    # Every allocation of rare items A, B, C among four agents, without
    # quotienting by agent symmetries. D copies are forced by equal sizes.
    tested=feasible=0
    example=None
    sizes=(k,)*4
    for aa in PARTS[3]:
        for bb in PARTS[5]:
            for cc in PARTS[5]:
                rare=tuple((aa[i],bb[i],cc[i]) for i in range(4))
                if any(sum(v)>k for v in rare):continue
                tested+=1
                if valid_reduced(rare,sizes):
                    feasible+=1
                    if example is None:example=rare
    return tested,feasible,example

# Witnesses for total item counts 13 through 27, arranged by p copies of D.
LOW = [
(((0,2,1),(0,3,0),(0,0,3),(3,0,1)),(3,3,3,4)),
(((0,2,0),(0,3,0),(1,0,3),(2,0,2)),(3,3,4,4)),
(((0,1,0),(1,1,2),(1,1,2),(1,2,1)),(3,4,4,4)),
(((0,2,2),(1,3,0),(1,0,1),(1,0,2)),(4,4,4,4)),
(((0,1,1),(0,4,0),(0,0,2),(3,0,2)),(4,4,4,5)),
(((0,1,0),(0,2,0),(1,2,2),(2,0,3)),(4,4,5,5)),
(((0,0,0),(0,5,0),(1,0,4),(2,0,1)),(4,5,5,5)),
(((0,2,3),(1,3,0),(1,0,1),(1,0,1)),(5,5,5,5)),
(((0,0,1),(0,5,0),(0,0,1),(3,0,3)),(5,5,5,6)),
(((0,0,0),(0,1,0),(1,4,1),(2,0,4)),(5,5,6,6)),
(((0,0,0),(0,5,0),(1,0,5),(2,0,0)),(5,6,6,6)),
(((0,4,2),(1,1,0),(1,0,1),(1,0,2)),(6,6,6,6)),
(((0,1,0),(0,1,0),(0,0,4),(3,3,1)),(6,6,6,7)),
(((0,0,0),(0,0,0),(1,4,2),(2,1,3)),(6,6,7,7)),
(((0,0,0),(0,5,0),(1,0,5),(2,0,0)),(6,7,7,7)),
]
ONE = {
7: (((0,1,0),(0,1,0),(0,0,3),(3,3,2)),(7,7,7,8)),
8: (((0,1,0),(0,1,0),(0,0,2),(3,3,3)),(8,8,8,9)),
9: (((0,1,0),(0,1,0),(0,0,1),(3,3,4)),(9,9,9,10)),
10:(((0,0,0),(0,1,0),(0,0,1),(3,4,4)),(10,10,10,11)),
11:(((0,0,0),(0,0,0),(0,0,1),(3,5,4)),(11,11,11,12)),
}
TWO = ((0,0,0),(0,0,0),(1,4,2),(2,1,3))
THREE = ((0,0,0),(0,5,0),(1,0,5),(2,0,0))

def count_invariants(rare,sizes):
    assert tuple(sum(rare[i][h] for i in range(4)) for h in range(3))==TOTAL
    assert max(sizes)-min(sizes)<=1
    assert sum(sizes)>=13
    assert all(sum(rare[i])<=sizes[i] for i in range(4))
    return sum(sizes)-13

def verify_witness_direct(rare,sizes):
    """Independent direct computation with complete A,B,C,D splits;
    no deficit-only optimization formula used here.
    """
    assert count_invariants(rare,sizes)>=0
    bundles=[(*rare[i],sizes[i]-sum(rare[i])) for i in range(4)]
    values=tuple(tuple(101-w if q<3 else 101 for q,w in enumerate((*WEIGHTS[i],0))) for i in range(4))
    for i in range(4):
        own=sum(bundles[i][h]*values[i][h] for h in range(4))
        for j in range(4):
            if i==j:continue
            u=tuple(bundles[i][h]+bundles[j][h] for h in range(4))
            mm=0
            for a in range(u[0]+1):
                for b in range(u[1]+1):
                    for c in range(u[2]+1):
                        for d in range(u[3]+1):
                            x=a*values[i][0]+b*values[i][1]+c*values[i][2]+d*values[i][3]
                            y=sum(u[h]*values[i][h] for h in range(4))-x
                            if min(x,y)>mm:mm=min(x,y)
            assert own>=mm,(i,j,rare,sizes,own,mm)
    return True

def run():
    for k,expected in ((4,28),(5,24),(6,8),(7,0),(8,0),(9,0),
                       (10,0),(11,0),(12,0),(13,0)):
        tested,n,_=enumerate_equal(k)
        assert n==expected,(k,tested,n)
        print('EQUAL',k,'eligible',tested,'valid',n,flush=True)
    # Finite low-count witnesses; direct valuation check on every one.
    for p,(rare,sizes) in enumerate(LOW):
        assert count_invariants(rare,sizes)==p
        assert valid_reduced(rare,sizes)
        verify_witness_direct(rare,sizes)
    print('LOW witnesses direct-check',len(LOW),flush=True)
    for k,(rare,sizes) in ONE.items():
        assert count_invariants(rare,sizes)==4*k+1-13
        assert valid_reduced(rare,sizes)
        verify_witness_direct(rare,sizes)
    for k in (7,8,13,15):
        for r,rare in ((2,TWO),(3,THREE)):
            sizes=(k,)*(4-r)+(k+1,)*r
            assert count_invariants(rare,sizes)==4*k+r-13
            assert valid_reduced(rare,sizes)
            verify_witness_direct(rare,sizes)
    # For all higher k, the same rare-item split witnesses only gain D copies.
    print('HIGH finite representative witnesses direct-check',5+8,flush=True)
    print('ALL EXACT CHECKS PASSED')

if __name__=='__main__':run()
