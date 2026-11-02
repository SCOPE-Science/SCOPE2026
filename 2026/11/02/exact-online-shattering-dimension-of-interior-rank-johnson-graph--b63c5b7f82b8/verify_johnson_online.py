"""Self-contained verification of adaptive neighborhood decision trees in Johnson graphs.

Usage: python verify_johnson_online.py johnson_adaptive_trees.json
Only Python's standard library is required.
"""
from functools import lru_cache
from itertools import combinations
import json
import sys

def all_masks(n,k):
    v=list(combinations(range(n),k))
    masks=[]
    for a in v:
        A=set(a)
        masks.append(sum((1<<i) for i,b in enumerate(v) if len(A.intersection(b))==k-1))
    return v,masks

def feasible_dimension(n,k):
    v,masks=all_masks(n,k)
    full=(1<<len(v))-1
    @lru_cache(None)
    def yes(s,d):
        if d==0:return True
        if s.bit_count()<(1<<d):return False
        for m in masks:
            pos=s&m;neg=s^pos
            if pos.bit_count()>=(1<<(d-1)) and neg.bit_count()>=(1<<(d-1)):
                if yes(pos,d-1) and yes(neg,d-1):return True
        return False
    depth=0
    for d in range(1,7):
        if not yes(full,d):break
        depth=d
    return depth

def verify_case(case):
    n,k,depth=case['n'],case['k'],case['depth']
    centers=set(combinations(range(n),k))
    used=[];internal=[]
    def go(node,level,path):
        if level==depth:
            assert set(node)=={'center'}
            c=tuple(node['center']);assert c in centers
            for q,b in path:
                assert (len(set(q)&set(c))==k-1)==bool(b),(n,k,c,q,b)
            used.append(c);return
        assert set(node)=={'query','zero','one'}
        q=tuple(node['query']);assert q in centers
        internal.append(q)
        go(node['zero'],level+1,path+[(q,0)])
        go(node['one'],level+1,path+[(q,1)])
    go(case['tree'],0,[])
    assert len(internal)==2**depth-1
    assert len(used)==2**depth and len(set(used))==len(used)
    assert feasible_dimension(n,k)==depth
    return (n,k,depth,len(internal),len(used))

def check_trace_pattern(n,k):
    v=[frozenset(s) for s in combinations(range(n),k)]
    S=frozenset(range(k-1));a,b=k-1,k
    A={S|{c} for c in range(n) if c not in S and c not in {a,b}}
    B={(S-{s})|{a,b} for s in S}
    C=A|B
    assert len(C)==n-2
    for q in v:
        trace={c for c in C if len(q&c)==k-1}
        if q in {S|{a},S|{b}}:assert trace==C
        elif q in A:assert trace==A-{q}
        elif q in B:assert trace==B-{q}
        else:assert len(trace)<=2
    return len(v)

def main():
    path=sys.argv[1] if len(sys.argv)>1 else 'johnson_adaptive_trees.json'
    with open(path,encoding='utf-8') as f: data=json.load(f)
    assert data['schema_version']==1
    info=[verify_case(c) for c in data['cases']]
    print('TREE_CERTIFICATES_PASS',info)
    traces=[]
    for n,k in ((6,3),(8,4),(9,4),(10,4),(10,5),(11,5)):
        traces.append((n,k,check_trace_pattern(n,k)))
    print('COMMON_NEIGHBOR_TRACE_PATTERNS_PASS',traces)
    table=[]
    for n in range(6,14):
        for k in range(3,n//2+1):
            if n-k<3:continue
            actual=feasible_dimension(n,k)
            expected=5 if min(k,n-k)>=4 and max(k,n-k)>=6 else 4
            assert actual==expected,(n,k,actual,expected)
            table.append((n,k,actual))
    print('EXACT_DEPTH_SMALL_PARAMETER_GRID_PASS',len(table),table)
    print('JOHNSON_ONLINE_DIMENSION_ALL_CHECKS_PASS')

if __name__=='__main__':main()
