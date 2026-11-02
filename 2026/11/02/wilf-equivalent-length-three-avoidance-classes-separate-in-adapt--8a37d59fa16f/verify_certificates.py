"""Independent exact reconstruction and verification of length-three avoidance dimensions.

No precomputed masks or leaf witnesses are trusted: they are regenerated from
one-line permutations, then every leaf assertion and an exhaustive independent
upper-depth decision recursion are checked. Run in the containing directory.
"""
from itertools import permutations,combinations
from functools import lru_cache
from pathlib import Path
import json,math

def pattern_of_three(a,b,c):
    triples=(a,b,c)
    order=sorted(range(3),key=lambda i:triples[i])
    out=[0,0,0]
    for rank,index in enumerate(order,1):out[index]=rank
    return tuple(out)

def catalog(n,tau):
    out=[]
    for pi in permutations(range(1,n+1)):
        if all(pattern_of_three(pi[i],pi[j],pi[k])!=tau
               for i,j,k in combinations(range(n),3)):
            out.append(pi)
    return out

def bit_columns(rows):
    n=len(rows[0]); q=list(combinations(range(1,n+1),2))
    cols=[]
    for a,b in q:
        m=0
        for j,row in enumerate(rows):
            if row.index(a)<row.index(b):m|=1<<j
        cols.append(m)
    return q,cols

def upper_decision(rows,depth):
    q,masks=bit_columns(rows)
    @lru_cache(maxsize=None)
    def exists(bitset,remaining):
        if remaining==0:return bitset!=0
        if bitset.bit_count()<2**remaining:return False
        threshold=2**(remaining-1)
        for m in masks:
            yes=bitset&m;no=bitset^yes
            if yes.bit_count()<threshold or no.bit_count()<threshold:continue
            if exists(no,remaining-1) and exists(yes,remaining-1):return True
        return False
    exists_val=exists((1<<len(rows))-1,depth)
    return exists_val,exists.cache_info().currsize

def tree_check(tree,rows,expected_depth):
    seen=[];tested=0;queries_count=0
    def verify(node,trace,level):
        nonlocal tested,queries_count
        if node[0]=='L':
            assert level==expected_depth
            assert len(node)==2 and type(node[1]) is int and 0<=node[1]<len(rows)
            item=rows[node[1]]
            assert all((item.index(a)<item.index(b))==bool(v) for a,b,v in trace)
            seen.append(node[1]);tested+=1
            return
        assert node[0]=='Q' and len(node)==5 and level<expected_depth
        _,a,b,left,right=node
        assert 1<=a<b<=len(rows[0])
        queries_count+=1
        verify(left,trace+[(a,b,0)],level+1)
        verify(right,trace+[(a,b,1)],level+1)
    verify(tree,[],0)
    assert len(seen)==2**expected_depth and len(set(seen))==len(seen)
    assert tested==2**expected_depth and queries_count==2**expected_depth-1
    return queries_count,tested

def main():
    path=Path(__file__).resolve().parent/'SHATTERING_TREES.json'
    data=json.loads(path.read_text(encoding='utf8'))
    assert data['schema_version']==1 and len(data['records'])==12
    reps={(r['pattern'],r['n']):r for r in data['records']}
    expected_A=(2,3,4,6,7,9)
    expected_B=(2,3,5,6,8,9)
    total_nodes=total_leaves=total_states=0
    for n in range(3,9):
        for name,expect in [('123',expected_A[n-3]),('132',expected_B[n-3])]:
            tau=tuple(int(x) for x in name)
            rows=catalog(n,tau)
            record=reps[name,n]
            assert record['class_size']==len(rows)==math.comb(2*n,n)//(n+1)
            assert record['depth']==expect and record['upper_depth_test']==expect+1
            nodes,leaves=tree_check(record['tree'],rows,expect)
            possible,states=upper_decision(rows,expect+1)
            assert not possible
            total_nodes+=nodes;total_leaves+=leaves;total_states+=states
            print('VERIFIED',name,n,len(rows),expect,'upper_states',states,
                  'tree_nodes',nodes,'leaf_witnesses',leaves)
    # All six forbidden patterns reduce to two representatives under
    # reversal of positions and complement of values, each inducing only
    # relabelings and/or flips of the same pairwise-comparison queries.
    print('PATTERN_CLASS_WITNESS_CHECKS_PASS',len(data['records']),total_nodes,
          total_leaves,total_states)
if __name__=='__main__':main()
