"""Exhaustive exact Littlestone and convexity checks for [2] x [n].

Only the Python standard library is needed. The finite proof is by full
version-space recursion, not sampling. A separate convexity enumeration
cross-check uses triple betweenness rather than ideal differences.
"""
from functools import lru_cache
from itertools import combinations
from math import floor, log2
from pathlib import Path
import json
import sys

EXPECTED_N = {1:(4,2),2:(13,3),3:(33,4),4:(71,5),5:(136,6),6:(239,7),7:(393,8),8:(613,8),9:(916,9),10:(1321,9)}

def ideals(n):
    out=[]
    for p in range(n+1):
        for q in range(p+1):
            out.append(((1<<p)-1)|(((1<<q)-1)<<n))
    return out

def class_differences(n):
    I=ideals(n)
    return sorted({B&~A for A in I for B in I if A&B==A})

def class_triples(n):
    # Independent check: enumerate EVERY subset of the 2n vertices.
    # The partial order is coordinatewise on (row,column).
    size=2*n
    interval=[]
    for a in range(size):
        ra,ca=divmod(a,n)
        for c in range(size):
            rc,cc=divmod(c,n)
            if ra<=rc and ca<=cc:
                m=0
                for b in range(size):
                    rb,cb=divmod(b,n)
                    if ra<=rb<=rc and ca<=cb<=cc:
                        m|=1<<b
                interval.append(((1<<a)|(1<<c),m))
    return [S for S in range(1<<size) if all(S&pair!=pair or S&mid==mid for pair,mid in interval)]

def exact_rank(n,H,need_witness=False):
    k=len(H)
    splits=[sum(1<<i for i,h in enumerate(H) if h>>x&1) for x in range(2*n)]
    top=(1<<k)-1
    @lru_cache(None)
    def R(v):
        if v.bit_count()<2:return 0
        ans=0
        for sm in splits:
            yes=v&sm; no=v&~sm
            if yes and no:
                ans=max(ans,1+min(R(yes),R(no)))
        return ans
    d=R(top)
    states=R.cache_info().currsize
    if not need_witness:return d,states,None
    def tree(v,depth):
        if depth==0:
            assert v
            i=(v&-v).bit_length()-1
            return {"witness":H[i]}
        for x,sm in enumerate(splits):
            yes=v&sm; no=v&~sm
            if yes and no and R(yes)>=depth-1 and R(no)>=depth-1:
                return {"query":x,"zero":tree(no,depth-1),"one":tree(yes,depth-1)}
        raise AssertionError((n,v,depth))
    return d,states,tree(top,d)

def check_witness(n,H,tree):
    leaves=[]; top=set(H)
    def visit(t,version,seen):
        if 'witness' in t:
            h=t['witness']
            assert len(version)>0 and h in version
            leaves.append(h)
            return 0
        x=t['query']
        assert 0<=x<2*n and x not in seen
        positive={h for h in version if h>>x&1}
        negative=version-positive
        assert positive and negative
        a=visit(t['zero'],negative,seen|{x})
        b=visit(t['one'],positive,seen|{x})
        assert a==b
        return a+1
    depth=visit(tree,top,set())
    assert len(leaves)==2**depth and len(set(leaves))==len(leaves)
    return depth,len(leaves)

def main():
    certs={}; stats=[]
    for n,(expected_count,expected_rank) in EXPECTED_N.items():
        H=class_differences(n)
        assert len(H)==expected_count,(n,len(H),expected_count)
        assert len(H)==(n**4+4*n**3+17*n**2+14*n+12)//12
        if n<=8:
            T=class_triples(n)
            assert H==T,('independent convexity mismatch',n)
        d,states,w=exact_rank(n,H,need_witness=n in (7,8,9,10))
        assert d==expected_rank,(n,d,expected_rank)
        if w:
            vd,leaves=check_witness(n,H,w)
            assert vd==d
            certs[str(n)]=w
        else:leaves=0
        count_upper=len(H).bit_length()-1
        print('EXACT',n,'concepts',len(H),'Ldim',d,'log_bound',count_upper,'states',states,'witness_leaves',leaves,flush=True)
        stats.append({'n':n,'hypotheses':len(H),'Ldim':d,'counting_bound':count_upper,'states':states})
    with open(str(Path(__file__).resolve().parent/'certificates.json'),'w',encoding='utf-8') as f:
        json.dump({'schema_version':1,'convention':'low n bits: first row; next n bits: second row', 'trees':certs},f,separators=(',',':'))
        f.write('\n')
    with open(str(Path(__file__).resolve().parent/'results.json'),'w',encoding='utf-8') as f:
        json.dump(stats,f,indent=2);f.write('\n')
    print('ALL_ORDER_CONVEX_LADDER_CHECKS_PASS')

if __name__=='__main__':main()
