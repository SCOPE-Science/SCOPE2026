"""Independent static-support and finite-certificate checks for order convexity."""
import json
from itertools import combinations
from math import comb
from pathlib import Path


def independent_order_convex(n):
    P=[(a,j) for a in range(2) for j in range(n)]
    pairs=[]
    for i,p in enumerate(P):
        for j,q in enumerate(P):
            if p[0]<=q[0] and p[1]<=q[1]:
                between=sum(1<<k for k,r in enumerate(P)
                            if p[0]<=r[0]<=q[0] and p[1]<=r[1]<=q[1])
                pairs.append((1<<i|1<<j,between))
    return {s for s in range(1<<(2*n)) if all((s&ends)!=ends or (s&v)==v for ends,v in pairs)}

def is_three_chain_free(S,n):
    pts=[divmod(i,n) for i in range(2*n) if S>>i&1]
    for a,b,c in combinations(pts,3):
        for x,y,z in ((a,b,c),(a,c,b),(b,a,c),(b,c,a),(c,a,b),(c,b,a)):
            if x[0]<=y[0]<=z[0] and x[1]<=y[1]<=z[1] and x!=y and y!=z:
                return False
    return True

def check_static():
    for n in range(1,9):
        cls=independent_order_convex(n)
        counts=[0]*5
        for k in range(5):
            for subset in combinations(range(2*n),k):
                s=sum(1<<x for x in subset)
                good=is_three_chain_free(s,n)
                if k<=4:
                    traces={h&s for h in cls}
                    assert (len(traces)==1<<k)==good,(n,k,subset)
                counts[k]+=good
        expected=[1,2*n,comb(2*n,2),comb(2*n,3)//2,n*(n-1)**2*(n-2)//12]
        assert counts==expected,(n,counts,expected)
        assert len(cls)==(n**4+4*n**3+17*n**2+14*n+12)//12
        print('STATIC_PASS',n,'shattered',counts,'convex_sets',len(cls),flush=True)


def verify_trees():
    data=json.load(open(Path(__file__).resolve().parent/'certificates.json',encoding='utf-8'))
    for ns,t in data['trees'].items():
        n=int(ns)
        # independent re-enumeration of hypotheses using all nested ideal pairs
        ideals=[]
        for p in range(n+1):
            for q in range(p+1):
                ideals.append(sum(1<<i for i in range(p)) | sum(1<<(n+j) for j in range(q)))
        H={J &~I for I in ideals for J in ideals if I & J==I}
        def run(node,S,used):
            if 'witness' in node:
                h=node['witness']
                assert h in S
                return [h],0
            j=node['query']
            assert j not in used and 0<=j<2*n
            A={h for h in S if h&(1<<j)}
            B=S-A
            assert A and B
            left,d0=run(node['zero'],B,used|{j})
            right,d1=run(node['one'],A,used|{j})
            assert d0==d1
            return left+right,1+d0
        witnesses,depth=run(t,H,set())
        assert len(set(witnesses))==len(witnesses)==1<<depth
        assert depth=={7:8,8:8,9:9,10:9}[n]
        print('ADAPTIVE_CERTIFICATE_PASS',n,'depth',depth,'leaves',len(witnesses),flush=True)

if __name__=='__main__':
    check_static()
    verify_trees()
    print('ALL_INDEPENDENT_STATIC_AND_CERTIFICATE_CHECKS_PASS')
