from itertools import combinations

MAX_ORDER=10

def partitions(n, lo=1):
    if n==0:
        yield (); return
    for a in range(lo,n+1):
        for rest in partitions(n-a,a): yield (a,)+rest

def verts(parts):
    return [(i,j) for i,n in enumerate(parts) for j in range(n)]

def adjacent(u,v): return u[0]!=v[0]

def dominates(V,S):
    S=set(S)
    return all(v in S or any(adjacent(v,u) for u in S) for v in V)

def connected(S):
    S=list(S)
    if not S: return False
    if len(S)==1: return True
    seen={S[0]}; stack=[S[0]]
    while stack:
        u=stack.pop()
        for v in S:
            if v not in seen and adjacent(u,v): seen.add(v); stack.append(v)
    return len(seen)==len(S)

def literal_accurate(V,D):
    D=set(D); s=len(D); C=[v for v in V if v not in D]
    if not dominates(V,D) or not connected(D): return False
    if len(C)<s: return True
    for X in combinations(C,s):
        if dominates(V,X): return False
    return True

def criterion(parts,mask):
    V=verts(parts); D=[V[i] for i in range(len(V)) if mask>>i&1]
    s=len(D); N=len(V)
    if not D: return False
    suppD={v[0] for v in D}
    # connected domination characterization
    conn_dom = (s==1 and parts[D[0][0]]==1) or (len(suppD)>=2)
    if not conn_dom: return False
    C=[V[i] for i in range(N) if not (mask>>i&1)]
    if s==1:
        # A singleton connected dominating set is accurate iff it is the unique singleton part.
        q=sum(n==1 for n in parts)
        return q==1
    if len(C)<s: return True
    suppC={v[0] for v in C}
    if len(suppC)>=2: return False
    if not C: return True
    j=next(iter(suppC))
    # If C is the whole part and has exactly s vertices, then C itself is a dominating s-set.
    if len(C)==parts[j] and parts[j]==s: return False
    return True

def gamma_formula(parts):
    N=sum(parts); r=len(parts); q=sum(n==1 for n in parts); M=max(parts)
    if q==1: return 1
    if r==2: return min(parts)+1
    if 2*M>N: return N-M
    return N//2+1

profiles=subset_checks=accurate_sets=criterion_checks=gamma_checks=bipartite_checks=0
for N in range(2,MAX_ORDER+1):
    for parts in partitions(N):
        if len(parts)<2: continue
        profiles+=1; V=verts(parts); sizes=[]
        for mask in range(1<<N):
            D=[V[i] for i in range(N) if mask>>i&1]
            a=literal_accurate(V,D); b=criterion(parts,mask)
            subset_checks+=1; criterion_checks+=1
            if a!=b: raise AssertionError(('criterion',parts,mask,a,b,D))
            if a: accurate_sets+=1; sizes.append(len(D))
        got=min(sizes); exp=gamma_formula(parts); gamma_checks+=1
        if got!=exp: raise AssertionError(('gamma',parts,got,exp))
        if len(parts)==2 and min(parts)>=2:
            bipartite_checks+=1
            if got!=min(parts)+1: raise AssertionError(('published bipartite',parts,got))
print(f'VERIFY_OK profiles={profiles} subset_checks={subset_checks} criterion_checks={criterion_checks} accurate_sets={accurate_sets} gamma_checks={gamma_checks} bipartite_checks={bipartite_checks} max_order={MAX_ORDER}')
