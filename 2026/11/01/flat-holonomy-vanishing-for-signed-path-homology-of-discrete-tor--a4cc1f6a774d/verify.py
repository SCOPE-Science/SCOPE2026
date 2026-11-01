#!/usr/bin/env python3
"""Independent finite checks for flat signed Cartesian-cycle GLMY examples.

The matrices are cubical local-system boundaries, not an implementation of
arbitrary GLMY path complexes. Agreement corroborates, but does not prove,
the all-degree path-homology comparison.
"""
from itertools import product, combinations
from math import comb

PRIMES = (1000003, 1000033)

def vertices(sizes):
    return list(product(*(range(m) for m in sizes)))

def move(x, j, sizes):
    y = list(x)
    y[j] = (y[j] + 1) % sizes[j]
    return tuple(y)

def sign(x, j, sizes, twists):
    return -1 if (twists[j] and x[j] == sizes[j] - 1) else 1

def boundary(sizes, twists, p):
    d = len(sizes)
    verts = vertices(sizes)
    srcsub = list(combinations(range(d), p))
    if p == 0:
        return [], len(verts)
    dstsub = list(combinations(range(d), p-1))
    targets = {(x,S): k for k,(x,S) in enumerate(product(verts, dstsub))}
    cols = []
    for x in verts:
        for S in srcsub:
            col = {}
            for k, j in enumerate(S):
                other = tuple(i for i in S if i != j)
                s = (-1)**k
                y = move(x,j,sizes)
                a,b = targets[(y,other)], targets[(x,other)]
                col[a] = col.get(a,0) + s*sign(x,j,sizes,twists)
                col[b] = col.get(b,0) - s
            cols.append({r:v for r,v in col.items() if v})
    return cols, len(targets)

def rank_mod(cols, p):
    piv = {}
    for col in cols:
        row = {k:(v%p) for k,v in col.items() if v%p}
        while row:
            k = min(row)
            if k not in piv:
                x = pow(row[k], -1, p)
                piv[k] = {a:(v*x)%p for a,v in row.items() if v}
                break
            c = row[k]
            for j, v in piv[k].items():
                w = (row.get(j,0)-c*v)%p
                if w: row[j]=w
                elif j in row:del row[j]
    return len(piv)

def check_d2(sizes, twists):
    d=len(sizes)
    mats=[boundary(sizes,twists,p)[0] for p in range(d+1)]
    ranks = [[rank_mod(mat,prime) for mat in mats] for prime in PRIMES]
    assert ranks[0]==ranks[1], (sizes,twists,ranks)
    r=ranks[0]
    beta=[comb(d,p)*__import__('math').prod(sizes)-r[p]- (r[p+1] if p<d else 0) for p in range(d+1)]
    expected= [comb(d,p) for p in range(d+1)] if not any(twists) else [0]*(d+1)
    assert beta==expected, (sizes,twists,beta,expected)
    # Every oriented square is flat, so the cubical differential squares to zero.
    for x in vertices(sizes):
        for i,j in combinations(range(d),2):
            y=move(x,i,sizes);z=move(x,j,sizes)
            assert sign(x,i,sizes,twists)*sign(y,j,sizes,twists)==sign(x,j,sizes,twists)*sign(z,i,sizes,twists)
    return len(vertices(sizes)),sum(len(m) for m in mats),r,beta

def cover_check(sizes, twists):
    d=len(sizes)
    vs=vertices(sizes)
    total=len(vs)
    # Signed double cover: move along an oriented edge (x, sheet) and flip
    # precisely when the original edge has negative sign.
    def lift_step(v,t,j):
        return (move(v,j,sizes),t^(sign(v,j,sizes,twists)<0))
    # A 2^s-fold product cover factors through the signed double cover.
    ms=tuple(m*(2 if twists[i] else 1) for i,m in enumerate(sizes))
    def phi(y):
        x=tuple(y[i]%sizes[i] for i in range(d))
        t=sum(y[i]//sizes[i] for i in range(d) if twists[i])%2
        return x,t
    for y in vertices(ms):
        x,t=phi(y)
        for j in range(d):
            Y=move(y,j,ms)
            assert phi(Y)==lift_step(x,t,j), (sizes,twists,y,j)
    if any(twists):
        assert len(vertices(ms))//(2*total)==2**(sum(twists)-1)
    else:
        assert len(vertices(ms))==total
    # Direct connectivity of both signed-cover sheets.
    start=(vs[0],0);seen={start};stack=[start]
    while stack:
        v,t=stack.pop()
        for j in range(d):
            for inc in (-1,1):
                if inc==1:
                    z,u=lift_step(v,t,j)
                else:
                    prev=list(v);prev[j]=(prev[j]-1)%sizes[j];prev=tuple(prev)
                    z,u=prev,t^(sign(prev,j,sizes,twists)<0)
                if (z,u) not in seen:seen.add((z,u));stack.append((z,u))
    assert len(seen)==(2*total if any(twists) else total)
    return len(seen)

def main():
    cases=0;cells=0
    for sizes in [(5,), (5,5), (5,6), (6,5), (5,5,5)]:
        d=len(sizes)
        for twists in product((0,1),repeat=d):
            n,ct,r,b=check_d2(sizes,twists)
            cover=cover_check(sizes,twists)
            cases+=1;cells+=ct
            print('OK sizes',sizes,'holonomy',twists,'betti',b,'ranks',r,'cover_component_size',cover)
    print('VERIFY_OK',cases,'signed_tori',cells,'cubical_cells')
if __name__=='__main__':
    main()

# Direct low-degree signed GLMY computation using the anti-invariant path basis.
# For triangle-free bidirected graphs every deletion of the middle vertex
# is either a backtrack (regularly zero) or a forbidden shortcut.
def signed_glmy_h1(sizes, twists, prime=1000003):
    vs=vertices(sizes)
    d=len(sizes)
    neighbors={x:set() for x in vs}
    for x in vs:
        for j in range(d):
            y=move(x,j,sizes)
            neighbors[x].add(y);neighbors[y].add(x)
    arcs=[(u,v) for u in vs for v in sorted(neighbors[u])]
    arow={a:i for i,a in enumerate(arcs)}
    vr={x:i for i,x in enumerate(vs)}
    # The degree-one signed boundary: (u,v) -> sign(u,v)*v-u.
    B1=[]
    def edge_sign(u,v):
        for j in range(d):
            if move(u,j,sizes)==v:return sign(u,j,sizes,twists)
            if move(v,j,sizes)==u:return sign(v,j,sizes,twists)
        raise ValueError((u,v))
    for u,v in arcs:
        B1.append({vr[u]:-1, vr[v]:edge_sign(u,v)})
    r1=rank_mod(B1,prime)
    # For a two-step path uvw, an omitted non-allowed regular shortcut
    # remembers both endpoint sheets; this is the subtle signed condition.
    ob_rows={}; M=[]; BM=[]
    for u,v in arcs:
        for w in sorted(neighbors[v]):
            col={arow[(u,v)]:1, arow[(v,w)]:edge_sign(u,v)}
            BM.append({i:val for i,val in col.items() if val})
            if u!=w:
                twist=edge_sign(u,v)*edge_sign(v,w)
                key=(u,w,twist)
                if key not in ob_rows:ob_rows[key]=len(ob_rows)
                M.append({ob_rows[key]:-1})
            else:M.append({})
    # rank [M; BM] - rank M is the rank of B restricted to ker M.
    nr=len(ob_rows)
    combo=[]
    for m,b in zip(M,BM):
        col=dict(m)
        for k,v in b.items():col[nr+k]=v
        combo.append(col)
    r2=rank_mod(combo,prime)-rank_mod(M,prime)
    beta0=len(vs)-r1
    beta1=len(arcs)-r1-r2
    expect0=0 if any(twists) else 1
    expect1=0 if any(twists) else d
    assert (beta0,beta1)==(expect0,expect1),(sizes,twists,beta0,beta1,r1,r2)
    return beta0,beta1,len(BM),nr

if __name__=='__main__':
    ct=0
    for ss in [(5,), (6,), (5,5),(5,6)]:
        for tw in product((0,1),repeat=len(ss)):
            b0,b1,n2,no=signed_glmy_h1(ss,tw)
            print('GLMY_DIRECT_OK',ss,tw,'b0,b1',(b0,b1),'two_paths',n2,'forbidden_rows',no)
            ct+=1
    print('GLMY_DIRECT_VERIFY_OK',ct,'signed models')
