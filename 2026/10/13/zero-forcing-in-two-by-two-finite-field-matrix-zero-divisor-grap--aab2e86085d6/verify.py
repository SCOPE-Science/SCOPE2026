from itertools import product, combinations

def type_vertices(q):
    n=q+1; s=q-1
    return [(i,k,t) for i in range(n) for k in range(n) for t in range(s)]

def adjacent(a,b):
    i,k,t=a; j,l,u=b
    if (i,k,t)==(j,l,u): return False
    if (i,k)==(j,l):
        return i==k
    return j==k or l==i

def chosen_white(q):
    n=q+1
    return {(0,k,0) for k in range(n)} | {(i,0,0) for i in range(1,q)}

def force(q,blue,source,target):
    V=type_vertices(q)
    assert source in blue and target not in blue
    whites=[v for v in V if v not in blue and adjacent(source,v)]
    assert whites==[target], (q,source,target,whites[:20],len(whites))
    blue.add(target)

def check_forcing(q):
    V=type_vertices(q); W=chosen_white(q); blue=set(V)-W
    # T_{1,q} -> T_{0,1}
    force(q,blue,(1,q,0),(0,1,0))
    # T_{1,i} -> T_{i,0}, 1<=i<=q-1
    for i in range(1,q):
        force(q,blue,(1,i,0),(i,0,0))
    # newly blue T_{0,1} -> T_{0,0}
    force(q,blue,(0,1,0),(0,0,0))
    # T_{i,1} -> T_{0,i}, 2<=i<=q-1
    for i in range(2,q):
        force(q,blue,(i,1,0),(0,i,0))
    # newly blue T_{0,0} -> T_{0,q}
    force(q,blue,(0,0,0),(0,q,0))
    assert len(blue)==len(V)
    assert len(W)==2*q
    return len(V)-len(W)

def bipartite_profile_rule(q,Wtypes):
    # Each type is a cell (row=image, column=kernel).  A source (i,k)
    # sees row k union column i.
    W=set(Wtypes); n=q+1
    while W:
        move=None
        for i in range(n):
            for k in range(n):
                seen=[(j,l) for (j,l) in W if j==k or l==i]
                if len(seen)==1:
                    move=seen[0]; break
            if move is not None: break
        if move is None: return False
        W.remove(move)
    return True

def has_cycle_bipartite(n,E):
    adj=[set() for _ in range(2*n)]
    for r,c in E:
        u=r; v=n+c
        adj[u].add(v); adj[v].add(u)
    seen=set()
    def dfs(u,p):
        seen.add(u)
        for v in adj[u]:
            if v==p: continue
            if v in seen: return True
            if dfs(v,u): return True
        return False
    return any(u not in seen and dfs(u,-1) for u in range(2*n))

def exhaustive_type_profiles(q):
    n=q+1; cells=[(i,k) for i in range(n) for k in range(n)]
    best=-1; count=0
    for mask in range(1<<len(cells)):
        W=[cells[z] for z in range(len(cells)) if (mask>>z)&1]
        ok=bipartite_profile_rule(q,W)
        if ok:
            if len(W)>best: best=len(W); count=1
            elif len(W)==best: count+=1
            assert not has_cycle_bipartite(n,W)
    return best,count

def matmul(A,B,q):
    return ((A[0]*B[0]+A[1]*B[2])%q,
            (A[0]*B[1]+A[1]*B[3])%q,
            (A[2]*B[0]+A[3]*B[2])%q,
            (A[2]*B[1]+A[3]*B[3])%q)

def det(A,q): return (A[0]*A[3]-A[1]*A[2])%q

def canon_line(v,q):
    a,b=v
    assert (a,b)!=(0,0)
    if a%q:
        inv=pow(a,-1,q); return (1,(b*inv)%q)
    return (0,1)

def image_kernel(A,q):
    # image from a nonzero column
    c1=(A[0],A[2]); c2=(A[1],A[3])
    im=canon_line(c1 if c1!=(0,0) else c2,q)
    # kernel: a nonzero solution to A(x,y)=0; (-b,a) from a nonzero row
    r1=(A[0],A[1]); r2=(A[2],A[3])
    a,b=r1 if r1!=(0,0) else r2
    ker=canon_line(((-b)%q,a%q),q)
    return im,ker

def direct_check(q):
    mats=[A for A in product(range(q),repeat=4) if A!=(0,0,0,0) and det(A,q)==0]
    lines=[(1,m) for m in range(q)]+[(0,1)]
    idx={L:i for i,L in enumerate(lines)}
    classes={}
    tags={}
    for A in mats:
        I,K=image_kernel(A,q); tag=(idx[I],idx[K]); tags[A]=tag
        classes.setdefault(tag,[]).append(A)
    assert len(classes)==(q+1)**2
    assert set(map(len,classes.values()))=={q-1}
    zero=(0,0,0,0)
    for A,B in combinations(mats,2):
        actual=(matmul(A,B,q)==zero or matmul(B,A,q)==zero)
        i,k=tags[A]; j,l=tags[B]
        predicted=(j==k or l==i)
        assert actual==predicted,(q,A,B,tags[A],tags[B],actual,predicted)
    return len(mats)

def minor_check(q):
    if q<3: return None
    V=set(type_vertices(q)); branches=[]
    for i in range(1,q+1):
        branches.append({(0,i,0),(i,0,0)})
    for t in range(q-1):
        branches.append({(0,0,t)})
    branches.append({(0,1,1)})
    branches.append({(1,0,1)})
    assert len(branches)==2*q+1
    used=set()
    for B in branches:
        assert not (used&B); used |= B
        if len(B)>1:
            x,y=tuple(B); assert adjacent(x,y)
    for A,B in combinations(branches,2):
        assert any(adjacent(x,y) for x in A for y in B)
    return len(branches)

for q in range(2,10):
    z=check_forcing(q)
    N=(q-1)*(q+1)**2
    assert z==N-2*q
    print(f'q={q}: N={N}, explicit forcing set size={z}, omitted={2*q}')

for q in (2,3):
    best,count=exhaustive_type_profiles(q)
    assert best==2*q
    print(f'q={q}: exhaustive type profiles max omitted={best}, profile_count={count}')

for q in (2,3,5):
    N=direct_check(q)
    assert N==(q-1)*(q+1)**2
    print(f'F_{q}: direct M2 multiplication matches image-kernel graph on {N} vertices')

for q in (3,4,5,7,9):
    k=minor_check(q)
    assert k==2*q+1
    print(f'q={q}: explicit K_{k} minor certificate OK')

print('VERIFY_OK')
