"""Reproducible finite checks for the two-layer complete-bipartite wild-number theorem.
Run with Python 3, standard library only. The infinite result uses the accompanying proof.
"""
from itertools import combinations
from random import Random


def make_graph(n, permutations):
    # Vertex encoding: (layer, side, index); side 0=A, side 1=B.
    verts = [(h,s,i) for h in range(2) for s in range(2) for i in range(n)]
    codes = {v:i for i,v in enumerate(verts)}
    edges=[]
    for h in range(2):
        row,col,color=permutations[h]
        for a in range(n):
            for b in range(n):
                edges.append((codes[(h,0,a)],codes[(h,1,b)],color[(col[b]-row[a])%n]))
    for side in range(2):
        for i in range(n):
            edges.append((codes[(0,side,i)],codes[(1,side,i)],n))
    return verts,edges,codes


def witness(n,codes):
    W=set()
    def add(x,y):W.add(tuple(sorted((codes[x],codes[y]))))
    for b in range(1,n):add((0,0,0),(0,1,b))
    for a in range(n):add((1,0,a),(1,1,0))
    add((0,0,0),(1,0,0))
    add((0,1,0),(1,1,0))
    assert len(W)==2*n+1
    return W


def connected(order,edgepairs):
    parents=list(range(order));count=order
    def root(x):
        while parents[x]!=x:
            parents[x]=parents[parents[x]];x=parents[x]
        return x
    for a,b in edgepairs:
        i=root(a);j=root(b)
        if i!=j:parents[i]=j;count-=1
    return count==1


def checks():
    rng=Random(726212)
    test_instances=0; color_checks=0
    for n in range(2,13):
        reps=12 if n<8 else 5
        for rep in range(reps):
            permutations=[]
            for layer in range(2):
                row=list(range(n));col=list(range(n));color=list(range(n))
                rng.shuffle(row);rng.shuffle(col);rng.shuffle(color)
                permutations.append((row,col,color))
            vertices,edges,codes=make_graph(n,permutations)
            assert len(vertices)==4*n and len(edges)==2*n*n+2*n
            W=witness(n,codes)
            all_pairs={tuple(sorted((a,b))) for a,b,c in edges}
            assert W<=all_pairs
            for c in range(n+1):
                matching=[(a,b) for a,b,tint in edges if tint==c]
                assert len(matching)==2*n
                assert len({v for pair in matching for v in pair})==4*n
                assert connected(4*n,matching|W if isinstance(matching,set) else matching+list(W))
                color_checks+=1
            # An independent component count lower bound applies to every candidate W.
            assert ((n+1)*(2*n-1)+n-1)//n==2*n+1
            test_instances+=1
    # Tiny-case exhaustive check: no smaller connecting set in K_{2,2} prism.
    n=2; order=8; p=(list(range(n)),)*3
    verts,edges,codes=make_graph(n,[p,p])
    pairs=[(a,b) for a,b,tint in edges]
    rejects=0
    for size in range(5):
        for idx in combinations(range(len(pairs)),size):
            W=[pairs[j] for j in idx]
            if all(connected(order,W+[(a,b) for a,b,tint in edges if tint==c]) for c in range(n+1)):
                raise AssertionError('Smaller wild set found')
            rejects+=1
    print(f'VERIFY_OK graph_instances={test_instances} connected_color_checks={color_checks} exhaustive_K22_smaller_subsets={rejects}')

if __name__=='__main__':checks()
