"""Reproduce the integral degree-three symmetry module for three unordered points on the Pappus graph.
Requires Python 3.10+ standard library only. Run: python verify.py
"""
import itertools, collections, math, json, hashlib

# LCF coordinates of the 18-vertex Pappus graph.
N=18
LCF=[5,7,-7,7,-7,-5]*3
adj=[set() for _ in range(N)]
for i in range(N):
    for j in ((i+1)%N,(i+LCF[i])%N):
        adj[i].add(j); adj[j].add(i)
assert all(len(x)==3 for x in adj)
Edges=tuple(sorted((i,j) for i in range(N) for j in adj[i] if i<j))
assert len(Edges)==27
edge_index={e:i for i,e in enumerate(Edges)}
incident={v:tuple(sorted(edge_index[tuple(sorted((v,w)))] for w in adj[v])) for v in range(N)}
reference={v:incident[v][0] for v in range(N)}
alternative={v:incident[v][1:] for v in range(N)}

# Weight-three component of the reduced Swiatkowski chain model.
C3=tuple(cell for v in itertools.combinations(range(N),3)
         for cell in itertools.product(*[[(w,e) for e in alternative[w]] for w in v]))
C2=tuple((decoration,e) for v,w in itertools.combinations(range(N),2)
         for decoration in itertools.product(*[[(x,f) for f in alternative[x]] for x in (v,w)])
         for e in range(len(Edges)))
index3={c:i for i,c in enumerate(C3)}
index2={c:i for i,c in enumerate(C2)}
assert (len(C3),len(C2))==(6528,16524)

def boundary(cell):
    for i,(v,e) in enumerate(cell):
        rest=cell[:i]+cell[i+1:]
        sign=(-1)**i
        yield index2[(rest,e)],sign
        yield index2[(rest,reference[v])],-sign

def integral_kernel_basis(prime=101):
    # Sparse Gaussian elimination: prime-field rank gives an integer-rank lower bound.
    pivots={}; pivot_chains={}; basis=[]
    for column,cell in enumerate(C3):
        remainder=collections.defaultdict(int)
        for row,sign in boundary(cell): remainder[row]=(remainder[row]+sign)%prime
        remainder={i:a for i,a in remainder.items() if a}
        expansion={column:1}
        while remainder:
            leading=max(remainder); coefficient=remainder[leading]
            if leading not in pivots:
                inverse=pow(coefficient,-1,prime)
                pivots[leading]={i:a*inverse%prime for i,a in remainder.items()}
                pivot_chains[leading]={i:a*inverse%prime for i,a in expansion.items()}
                break
            for i,a in pivots[leading].items():
                value=(remainder.get(i,0)-coefficient*a)%prime
                if value:remainder[i]=value
                else:remainder.pop(i,None)
            for i,a in pivot_chains[leading].items():
                value=(expansion.get(i,0)-coefficient*a)%prime
                if value:expansion[i]=value
                else:expansion.pop(i,None)
        if not remainder:
            # Lift small coefficients and verify each relation over Z, not only mod prime.
            integral={i:(a if a<=prime//2 else a-prime) for i,a in expansion.items()}
            delta=collections.defaultdict(int)
            for i,a in integral.items():
                for r,s in boundary(C3[i]):delta[r]+=s*a
            assert all(v==0 for v in delta.values())
            basis.append(integral)
    free=[max(x) for x in basis]
    assert len(pivots)==6521 and len(basis)==7
    assert [[b.get(f,0) for f in free] for b in basis]==[[int(i==j) for j in range(7)] for i in range(7)]
    # Mod-101 rank >= 6521, seven integral independent kernel elements imply rank <= 6521.
    # Identity coordinates on seven free positions prove they span the entire integral kernel.
    return basis,free,len(pivots)

def automorphisms():
    results=[]
    def visit(partial,used):
        if len(partial)==N:
            results.append(tuple(partial[i] for i in range(N)));return
        remaining=[v for v in range(N) if v not in partial]
        v=max(remaining,key=lambda a:(sum(u in partial for u in adj[a]),
                                     sum(u in partial for u in range(N) if u!=a and u not in adj[a])))
        for w in range(N):
            if w in used:continue
            if all((u in adj[v])==(partial[u] in adj[w]) for u in partial):
                partial[v]=w;used.add(w);visit(partial,used);used.remove(w);del partial[v]
    visit({},set())
    assert len(results)==216
    return sorted(results)

def edge_action(g):
    return [edge_index[tuple(sorted((g[a],g[b])))] for a,b in Edges]

def basis_action(g,em,cell):
    targets=[]
    for v,e in cell:
        w=g[v];aa=em[e];bb=em[reference[v]]
        terms=[]
        if aa!=reference[w]:terms.append(((w,aa),1))
        if bb!=reference[w]:terms.append(((w,bb),-1))
        targets.append(terms)
    positions=[g[v] for v,e in cell]
    sign=(-1)**sum(positions[i]>positions[j] for i in range(3) for j in range(i+1,3))
    out=collections.defaultdict(int)
    for option in itertools.product(*targets):
        transformed=tuple(sorted(t for t,s in option))
        out[index3[transformed]]+=sign*math.prod(s for t,s in option)
    return {i:a for i,a in out.items() if a}

def action_matrix(g,basis,free):
    em=edge_action(g)
    cols=[]
    for b in basis:
        image=collections.defaultdict(int)
        for idx,a in b.items():
            for k,s in basis_action(g,em,C3[idx]).items():image[k]+=a*s
        coordinates=[image.get(f,0) for f in free]
        # Exact integral chain equality, not only equality in finite-field homology.
        reconstruction=collections.defaultdict(int)
        for j,a in enumerate(coordinates):
            for k,s in basis[j].items():reconstruction[k]+=a*s
        assert all(reconstruction.get(k,0)==image.get(k,0) for k in set(image)|set(reconstruction))
        cols.append(coordinates)
    return tuple(tuple(cols[j][i] for j in range(7)) for i in range(7))

def compose(a,b):return tuple(a[b[i]] for i in range(N))
def inverse(a):return tuple(a.index(i) for i in range(N))
def ctype(a):
    seen=set();lengths=[]
    for i in range(N):
        if i not in seen:
            t=0;j=i
            while j not in seen:seen.add(j);t+=1;j=a[j]
            lengths.append(t)
    return tuple(sorted(lengths,reverse=True))
def rank_rat(A):
    from fractions import Fraction
    b=[[Fraction(x) for x in row] for row in A]
    r=0
    for j in range(len(b[0])):
        k=next((k for k in range(r,len(b)) if b[k][j]),None)
        if k is None:continue
        b[r],b[k]=b[k],b[r]
        z=b[r][j];b[r]=[v/z for v in b[r]]
        for i in range(len(b)):
            if i!=r and b[i][j]:
                z=b[i][j];b[i]=[a-z*c for a,c in zip(b[i],b[r])]
        r+=1
        if r==len(b):break
    return r

def run():
    basis,free,rank=integral_kernel_basis()
    group=automorphisms()
    matrices={g:action_matrix(g,basis,free) for g in group}
    trace={g:sum(matrices[g][i][i] for i in range(7)) for g in group}
    identity=tuple(range(N))
    kernel=[g for g in group if matrices[g]==tuple(tuple(int(i==j) for j in range(7)) for i in range(7))]
    assert len(kernel)==3 and all(ctype(g)==(3,)*6 for g in kernel if g!=identity)
    unseen=set(group);classes=[];class_members=[]
    while unseen:
        g=min(unseen)
        orbit={compose(compose(h,g),inverse(h)) for h in group}
        assert orbit<=unseen
        unseen-=orbit;class_members.append(orbit)
        classes.append({'class_size':len(orbit),'order':math.lcm(*ctype(g)),
                        'vertex_cycle_type':list(ctype(g)),'H3_trace':trace[g],
                        'representative':list(g)})
        assert all(trace[h]==trace[g] for h in orbit)
    classes.sort(key=lambda x:(x['class_size'],x['order'],x['vertex_cycle_type'],x['H3_trace']))
    assert len(classes)==13
    assert sum(trace.values())==0
    assert sum(v*v for v in trace.values())==648 # 216 times character norm 3
    # Central class sum for the 9 involutions fixing 6 vertices.
    special=next(o for o in class_members if len(o)==9)
    Z=[[sum(matrices[g][i][j] for g in special) for j in range(7)] for i in range(7)]
    eig={str(x):7-rank_rat([[Z[i][j]-x*int(i==j) for j in range(7)] for i in range(7)])
         for x in (9,-9,0)}
    assert eig=={'9':1,'-9':2,'0':4}
    # Three pairwise-distinct central eigenvalues, plus character norm three, imply three irreducible summands.
    results={'graph_vertices':N,'graph_edges':len(Edges),'automorphisms':len(group),
             'top_chain_rank':len(C3),'next_chain_rank':len(C2),
             'boundary_rank_mod_101':rank,'integral_basis_size':len(basis),
             'integral_basis_support_sizes':[len(b) for b in basis],
             'free_coordinates':free,'automorphism_action_kernel_order':len(kernel),
             'full_group_H3_invariants':sum(trace.values())//len(group),
             'character_inner_product':sum(v*v for v in trace.values())//len(group),
             'central_involution_class_eigenspace_dimensions':eig,
             'conjugacy_classes':classes}
    print(json.dumps(results,ensure_ascii=False,separators=(',',':')))

if __name__=='__main__':run()
