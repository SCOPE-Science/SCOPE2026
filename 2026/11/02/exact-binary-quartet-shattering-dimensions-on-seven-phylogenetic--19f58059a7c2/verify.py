"""Independent proof-checking calculations for seven-leaf quartet concepts.

Usage: python verify.py
Uses standard Python only. The hierarchy enumerator and four-point-distance
predicate are independent of the edge-subdivision/split representation.
"""
from itertools import combinations
from functools import lru_cache
from pathlib import Path
import json
import construct

N=7
CERT=Path(__file__).with_name('quartet_certificate.json')

@lru_cache(None)
def rooted_shapes(labels):
    """All unordered full binary hierarchies on the specified leaves."""
    labels=tuple(labels)
    if len(labels)==1:
        return (labels[0],)
    smallest=labels[0]
    out=[]
    for k in range(1,len(labels)):
        for tail in combinations(labels[1:],k-1):
            left=(smallest,)+tail
            right=tuple(x for x in labels if x not in left)
            for ls in rooted_shapes(left):
                for rs in rooted_shapes(right):
                    out.append((ls,rs))
    return tuple(out)

def adjacency_from_rooted(shape):
    """Attach leaf 6 at the root of a binary hierarchy on leaves 0..5."""
    graph={6:set()}
    next_internal=[-1]
    def visit(s,parent=None):
        if isinstance(s,int):
            vertex=s
        else:
            vertex=next_internal[0]
            next_internal[0]-=1
        graph.setdefault(vertex,set())
        if parent is not None:
            graph[vertex].add(parent)
            graph[parent].add(vertex)
        if not isinstance(s,int):
            visit(s[0],vertex)
            visit(s[1],vertex)
        return vertex
    root=visit(shape)
    graph[6].add(root)
    graph[root].add(6)
    return graph

def distances(graph):
    result={}
    for a in range(N):
        d={a:0};stack=[a]
        while stack:
            x=stack.pop(0)
            for y in graph[x]:
                if y not in d:
                    d[y]=d[x]+1
                    stack.append(y)
        assert len(d)==len(graph)
        for b in range(a+1,N):result[(a,b)]=d[b]
    return result

def quartet_row_from_distances(dist,queries):
    def d(a,b):return dist[(min(a,b),max(a,b))]
    row=0
    for i,(a,b,c,e) in enumerate(queries):
        s1=d(a,b)+d(c,e)
        s2=d(a,c)+d(b,e)
        s3=d(a,e)+d(b,c)
        assert len({s1,s2,s3})==2 and min(s1,s2,s3)<max(s1,s2,s3)
        if s1 < s2 and s1 < s3:row|=1<<i
    return row

def exhaustive_vc_upper(masks,total):
    """Enumerate every 7-query support containing query 0.

    The natural action of S_7 is transitive on the 105 quartet queries,
    hence one fixed first query loses no shattered seven-query support.
    """
    nodes=[0]
    full=(1<<total)-1
    def visit(blocks,last,depth):
        nodes[0]+=1
        if depth==7:return True
        for j in range(last+1,len(masks)):
            z=masks[j]
            split=[]
            for b in blocks:
                neg,pos=b&~z,b&z
                if not neg or not pos:break
                split.extend((neg,pos))
            else:
                if visit(split,j,depth+1):return True
        return False
    exists=visit([full & ~masks[0], full & masks[0]],0,1)
    assert not exists
    assert nodes[0]==206992,nodes
    return nodes[0]

def verify():
    cert=json.loads(CERT.read_text(encoding='utf-8'))
    assert cert['schema_version']==1 and cert['concept_count']==945 and cert['query_count']==105
    q=construct.all_quartets(N)
    assert len(q)==105 and len(set(q))==105
    a=construct.all_unrooted_binary_trees(N)
    rows=[]
    for g in a:
        sp=construct.splits_of_tree(g)
        rows.append(sum((1<<i) for i,query in enumerate(q) if construct.displayed(sp,query)))
    assert len(set(rows))==945
    print('SUBDIVISION_ENUMERATOR_PASS',len(rows),flush=True)

    # Independently generate all trees by a root-adjoining construction.
    roots=rooted_shapes(tuple(range(N-1)))
    assert len(roots)==945
    independent_rows=[quartet_row_from_distances(distances(adjacency_from_rooted(s)),q) for s in roots]
    assert len(set(independent_rows))==945
    assert set(independent_rows)==set(rows)
    print('INDEPENDENT_ROOTED_FOUR_POINT_PASS',len(independent_rows),flush=True)

    masks=[sum(1<<i for i,row in enumerate(independent_rows) if row>>j&1) for j in range(len(q))]
    count=exhaustive_vc_upper(masks,len(independent_rows))
    print('VC_UPPER_SEVEN_IMPOSSIBLE_PASS','nodes',count,flush=True)

    support=cert['vc_lower_query_indices']
    vs=cert['vc_pattern_tree_indices']
    assert len(support)==6 and len(set(support))==6
    assert len(vs)==64 and len(set(vs))==64
    for pattern,idx in enumerate(vs):
        assert 0<=idx<len(rows)
        got=sum(((rows[idx]>>j)&1)<<k for k,j in enumerate(support))
        assert got==pattern,(pattern,got)
    print('VC_LOWER_SIX_PASS','patterns',len(vs),flush=True)

    decisions=cert['littlestone_internal_query_indices_heap_order']
    leaves=cert['littlestone_leaf_tree_indices_heap_order']
    assert len(decisions)==511 and len(leaves)==512 and len(set(leaves))==512
    # Leaf heap indices are 511+path, with bit=0 going to left/negative
    # and bit=1 going to right/positive.
    for path,idx in enumerate(leaves):
        assert 0<=idx<len(rows)
        node=0
        for level in range(9):
            qid=decisions[node]
            bit=(path>>(8-level))&1
            assert (rows[idx]>>qid)&1==bit,(path,level,qid)
            node=2*node+1+bit
        assert node==511+path
    assert (1<<10)>945
    print('LITTLESTONE_DEPTH_NINE_PASS','internal_nodes',511,'distinct_leaves',512,flush=True)
    print('SEVEN_LEAF_QUARTET_C_AND_CERTIFICATE_ALL_PASS',flush=True)

if __name__=='__main__':
    verify()
