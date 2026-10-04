from itertools import product
from collections import defaultdict, deque


def prufer_trees(n):
    if n == 1:
        yield [[]]
        return
    if n == 2:
        yield [[1], [0]]
        return
    for code in product(range(n), repeat=n-2):
        deg=[1]*n
        for x in code: deg[x]+=1
        adj=[[] for _ in range(n)]
        for x in code:
            leaf=next(i for i,d in enumerate(deg) if d==1)
            adj[leaf].append(x); adj[x].append(leaf)
            deg[leaf]-=1; deg[x]-=1
        a=[i for i,d in enumerate(deg) if d==1]
        u,v=a
        adj[u].append(v); adj[v].append(u)
        yield adj


def rooted_parent(adj, root):
    n=len(adj); p=[None]*n; p[root]=-1; q=deque([root])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if p[v] is None:
                p[v]=u; q.append(v)
    return p


def ancestors(parent,u):
    out=[]
    while u!=-1:
        out.append(u); u=parent[u]
    return out


def lca(parent,u,v):
    av=set(ancestors(parent,u))
    while v not in av: v=parent[v]
    return v


def meet_table(parent, verts):
    return tuple(lca(parent,i,j) for i in verts for j in verts)


def closed_old(parent,m):
    return all(lca(parent,i,j)<m for i in range(m) for j in range(m))


def closure(parent,S):
    S=set(S)
    changed=True
    while changed:
        changed=False
        cur=list(S)
        for u in cur:
            for v in cur:
                w=lca(parent,u,v)
                if w not in S:
                    S.add(w); changed=True
    return S


def extension_signature(parent,m,N):
    x=m
    old=tuple(range(m))
    if not closed_old(parent,m): return None
    C=closure(parent, list(old)+[x])
    if C!=set(range(N)): return None
    # Canonical qf diagram over fixed old labels: meet table on the generated
    # universe, with x fixed and (when present) the unique extra point z fixed.
    oldtab=meet_table(parent,old)
    full=meet_table(parent,tuple(range(N)))
    return oldtab,full


def check_extension_counts(max_m=4):
    grouped=defaultdict(set)
    for m in range(1,max_m+1):
        for N in (m+1,m+2):
            for adj in prufer_trees(N):
                for root in range(N):
                    p=rooted_parent(adj,root)
                    sig=extension_signature(p,m,N)
                    if sig is not None:
                        oldtab,full=sig
                        grouped[(m,oldtab)].add((N,full))
        counts={len(v) for (mm,_),v in grouped.items() if mm==m}
        assert counts=={3*m}, (m,counts)
        print('m',m,'old structures',sum(1 for mm,_ in grouped if mm==m),'nonalg signatures',3*m)


def increasing_parents(N):
    if N==1:
        yield [-1]; return
    for choices in product(*[range(i) for i in range(1,N)]):
        yield [-1]+list(choices)


def check_closure_bound(Nmax=7):
    for N in range(1,Nmax+1):
        for p in increasing_parents(N):
            for mask in range(1,1<<N):
                S=[i for i in range(N) if mask>>i & 1]
                c=closure(p,S)
                assert len(c)<=2*len(S)-1, (N,p,S,c)
    print('closure bound exhaustive through',Nmax,'vertices')

check_extension_counts()
check_closure_bound()
print('VERIFY_OK')
