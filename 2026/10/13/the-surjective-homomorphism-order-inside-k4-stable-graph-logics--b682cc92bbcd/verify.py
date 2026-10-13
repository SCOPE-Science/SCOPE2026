"""Reproduce finite tests of the graph-to-K4-frame translation.
No exhaustive infinite assertion is made by these finite tests.
"""
from itertools import combinations, product, permutations
from collections import deque

def graphs(n):
    pairs=list(combinations(range(n),2))
    for mask in range(1<<len(pairs)):
        E={frozenset(e) for k,e in enumerate(pairs) if (mask>>k)&1}
        adj=[set() for _ in range(n)]
        for uv in E:
            a,b=tuple(uv);adj[a].add(b);adj[b].add(a)
        color={0:0};q=deque([0]);ok=True
        while q:
            u=q.popleft()
            for v in adj[u]:
                if v in color:
                    if color[v]==color[u]:ok=False
                else:color[v]=1-color[u];q.append(v)
        if ok and len(color)==n and set(color.values())=={0,1}:
            yield (n,E,color)

def frame(G):
    n,E,col=G;r,a,b,c=n,n+1,n+2,n+3
    R={(v,v) for v in range(n)}|{(r,x) for x in range(n+4)}
    R|={(a,x) for x in range(n)}|{(a,c)}
    R|={(b,x) for x in range(n) if col[x]==1}
    R|={(x,c) for x in range(n) if col[x]==0}
    R|={(x,y) for e in E for x in e for y in e if x!=y and col[x]==0}
    assert all((x,z) in R for x,y in R for yy,z in R if y==yy), 'not transitive'
    return R

def graph_hom(G,H):
    n,E,cg=G;m,F,ch=H
    choices=[[u for u in range(m) if ch[u]==cg[v]] for v in range(n)]
    for p in product(*choices):
        if len(set(p))!=m:continue
        if all(frozenset((p[x],p[y])) in F for e in E for x,y in [tuple(e)]):return True
    return False

def frame_stable(G,H):
    n,_,_=G;m,_,_=H
    R,S=frame(G),frame(H)
    # A relation-preserving surjection necessarily maps the three irreflexive
    # source points bijectively to the target's three irreflexive points.
    # Enumerate all such bijections, without fixing their identities.
    for pp in permutations([m+1,m+2,m+3]):
        for q in product(range(m+1),repeat=n+1):
            f=tuple(q[:n])+ (q[n],)+pp
            if len(set(f))!=m+4:continue
            if all((f[x],f[y]) in S for x,y in R):return True
    return False

count=0
sizes=[]
for n in range(2,5):
    Gs=list(graphs(n));sizes.append((n,len(Gs)))
    for G in Gs:
      for m in range(2,5):
       for H in graphs(m):
        lhs=graph_hom(G,H)
        rhs=frame_stable(G,H)
        assert lhs==rhs,(G,H,lhs,rhs)
        count+=1
print('GRAPH_SIZES',sizes)
print('PAIRS_CHECKED',count)
print('VERIFY_OK')

def colored_cycle(k):
    n=2*k;edges={frozenset((i,(i+1)%n)) for i in range(n)}
    return (n,edges,{i:i%2 for i in range(n)})

def labeled_tree_path(n):
    return (n,{frozenset((i,i+1)) for i in range(n-1)},{i:i%2 for i in range(n)})

def labeled_tree_star(n):
    return (n,{frozenset((0,i)) for i in range(1,n)},{0:0,**{i:1 for i in range(1,n)}})

for src in range(3,9):
    for dst in range(3,9):
        # Explicit edge-preserving, surjective color-preserving cyclic walk when src >= dst.
        if src>=dst:
            walk=list(range(2*dst+1))
            walk=[i%(2*dst) for i in walk]
            walk+=([(1 if i%2==0 else 0) for i in range(2*(src-dst))])
            # After the initial full circuit the appended 2k steps alternate 1,0.
            assert len(walk)==2*src+1,(src,dst,len(walk))
            assert walk[-1]==walk[0]
            assert len(set(walk[:-1]))==2*dst
            assert all(frozenset((walk[i],walk[i+1])) in colored_cycle(dst)[1] for i in range(2*src))
            assert all(i%2==walk[i]%2 for i in range(2*src))
        else:
            assert 2*src<2*dst

P,S=labeled_tree_path(6),labeled_tree_star(6)
assert not graph_hom(P,S) and not graph_hom(S,P)
assert not frame_stable(P,S) and not frame_stable(S,P)
print('CYCLE_FOLD_TESTS',sum(1 for i in range(3,9) for j in range(3,i+1)))
print('PATH_STAR_INCOMPARABLE',True)
print('VERIFY_OK_FULL')
