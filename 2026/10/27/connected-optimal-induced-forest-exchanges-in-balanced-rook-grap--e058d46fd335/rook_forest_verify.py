"""Reproduce the balanced-rook induced-forest exchange census for n=2..5.

Requires Python 3.9+ (standard library only). This checker uses independent
edge-set exchanges, rather than the rotation formulas used in the proof.
"""
from collections import Counter, deque
from itertools import permutations
from math import factorial, comb


def arrangements(n):
    for left in permutations(range(n)):
        for right in permutations(range(n)):
            path = tuple(v for i in range(n) for v in (left[i], n+right[i]))
            edges = frozenset((min(path[i], path[i+1]), max(path[i], path[i+1])) for i in range(2*n-1))
            yield path, edges


def prefix_rotation_neighbors(path):
    n=len(path)//2
    results=set()
    for j in range(1,2*n):
        a=path[:j];b=path[j:]
        if j%2:
            results.add(a[::-1]+b[::-1])
            if j>1:results.add(a[::-1]+b)
            if j<2*n-1:results.add(a+b[::-1])
        else:
            results.add(b+a)
    results.discard(path)
    return results


def exchange_graph(n):
    arrangements_list=list(arrangements(n))
    paths=[a for a,_ in arrangements_list]
    edgesets=[e for _,e in arrangements_list]
    assert len(paths)==factorial(n)**2
    assert len(set(edgesets))==len(paths)
    index={e:i for i,e in enumerate(edgesets)}
    all_possible={(i,n+j) for i in range(n) for j in range(n)}
    nbrs=[]
    for ix,chosen in enumerate(edgesets):
        row=set()
        for removed in chosen:
            remainder=chosen-{removed}
            for added in all_possible-chosen:
                j=index.get(frozenset(remainder|{added}))
                if j is not None: row.add(j)
        assert ix not in row
        assert len(row)==4*n-5, (n,ix,len(row))
        if n<=4:
            from_formula={index[frozenset((min(q[t],q[t+1]),max(q[t],q[t+1])) for t in range(2*n-1))] for q in prefix_rotation_neighbors(paths[ix])}
            assert row==from_formula, (n,ix)
        nbrs.append(row)
    for i,row in enumerate(nbrs):
        for j in row:assert i in nbrs[j]
    count_edges=sum(map(len,nbrs))//2
    expected_edges=factorial(n)**2*(4*n-5)//2
    assert count_edges==expected_edges
    q=deque([0]);visited={0}
    while q:
        for v in nbrs[q.popleft()]:
            if v not in visited:visited.add(v);q.append(v)
    assert len(visited)==len(paths), (n,len(visited),len(paths))
    triangles=sum(sum(len(nbrs[j]&row) for j in row)//2 for row in nbrs)//3
    expected_triangles=factorial(n)**2*(2*n*n-5)//3
    assert triangles==expected_triangles, (n,triangles,expected_triangles)
    print('GRAPH_OK n={} vertices={} degree={} edges={} triangles={} connected=1'.format(n,len(paths),4*n-5,count_edges,triangles))


def is_forest_in_rook(n,edge_ids):
    # Construct the rook graph directly on cells (i,j) and test for cycles.
    parent={v:v for v in edge_ids};rank={v:0 for v in edge_ids}
    def find(v):
        while parent[v]!=v:
            parent[v]=parent[parent[v]];v=parent[v]
        return v
    for aa in range(len(edge_ids)):
        a=edge_ids[aa]
        for bb in range(aa+1,len(edge_ids)):
            b=edge_ids[bb]
            if a//n!=b//n and a%n!=b%n: continue
            u=find(a);v=find(b)
            if u==v:return False
            if rank[u]<rank[v]:u,v=v,u
            parent[v]=u
            if rank[u]==rank[v]:rank[u]+=1
    return True


def brute_rook(n):
    max_found=0;count=0
    for mask in range(1<<(n*n)):
        k=mask.bit_count()
        if k<2*n-1:continue
        ids=[i for i in range(n*n) if mask>>i&1]
        if is_forest_in_rook(n,ids):
            if k>max_found:max_found=k;count=0
            if k==max_found:count+=1
    assert max_found==2*n-1
    assert count==factorial(n)**2, (n,count)
    print('ROOK_INDEPENDENT_OK n={} max_forest={} maximizing_subsets={}'.format(n,max_found,count))


if __name__=='__main__':
    for n in range(2,5):brute_rook(n)
    for n in range(2,6):exchange_graph(n)
    print('VERIFY_OK')
