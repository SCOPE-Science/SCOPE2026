#!/usr/bin/env python3
"""Exact cellular and equivariant calculation for two indistinguishable points on the Heawood graph.

Requires Python >=3.10 and SymPy. The graph is the point--line incidence graph of PG(2,2).
"""
from collections import Counter, defaultdict
from itertools import combinations, product
from sympy import SparseMatrix, ZZ, zeros
from sympy.matrices.normalforms import smith_normal_form


def dot2(a,b):
    return (a & b).bit_count() & 1


def make_graph():
    edges=sorted((p-1, 7+l-1) for p in range(1,8) for l in range(1,8) if dot2(p,l)==0)
    assert len(edges)==21
    assert Counter(u for e in edges for u in e)==Counter({v:3 for v in range(14)})
    return edges


def chain_data(E):
    vertices=range(14)
    c0=list(combinations(vertices,2))
    c1=sorted((e,v) for e,(a,b) in enumerate(E) for v in vertices if v!=a and v!=b)
    c2=[(i,j) for i,j in combinations(range(len(E)),2) if set(E[i]).isdisjoint(E[j])]
    assert (len(c0),len(c1),len(c2))==(91,252,168)
    vmap={c:i for i,c in enumerate(c0)}
    emap={c:i for i,c in enumerate(c1)}
    d1=SparseMatrix(len(c0),len(c1),{})
    d2=SparseMatrix(len(c1),len(c2),{})
    for j,(eid,v) in enumerate(c1):
        a,b=E[eid]
        d1[vmap[tuple(sorted((b,v)))],j]+=1
        d1[vmap[tuple(sorted((a,v)))],j]-=1
    for j,(eid,fid) in enumerate(c2):
        a,b=E[eid];c,d=E[fid]
        for row,sign in [((fid,b),1),((fid,a),-1),((eid,d),-1),((eid,c),1)]:
            d2[emap[row],j]+=sign
    assert d1*d2==zeros(d1.rows,d2.cols)
    return c0,c1,c2,d1,d2


def rank_prime(A,p):
    # Sparse-column elimination, no floating point.
    piv={}
    for j in range(A.cols):
        col={int(i):int(v)%p for (i,k),v in A.todok().items() if k==j and v%p}
        while col:
            t=min(col)
            if t not in piv:
                z=pow(col[t],-1,p)
                piv[t]={i:(v*z)%p for i,v in col.items()}
                break
            q=col[t]
            for i,v in piv[t].items():
                w=(col.get(i,0)-q*v)%p
                if w: col[i]=w
                else:col.pop(i,None)
    return len(piv)


def top_nullspace(A,p=101):
    # Reduced-echelon basis for ker(A) over F_p; each basis vector has one distinct free column.
    a=[[0]*A.cols for _ in range(A.rows)]
    for (i,j),v in A.todok().items():a[i][j]=int(v)%p
    r=0;pivot=[]
    for j in range(A.cols):
        k=next((i for i in range(r,A.rows) if a[i][j]),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r]
        z=pow(a[r][j],-1,p);a[r]=[(v*z)%p for v in a[r]]
        for i in range(A.rows):
            if i!=r and a[i][j]:
                z=a[i][j];a[i]=[(v-z*w)%p for v,w in zip(a[i],a[r])]
        pivot.append(j);r+=1
        if r==A.rows:break
    free=[j for j in range(A.cols) if j not in pivot]
    B=[]
    for j in free:
        b=[0]*A.cols;b[j]=1
        for i,k in enumerate(pivot):b[k]=(-a[i][j])%p
        B.append(b)
    assert len(free)==14
    assert all(not any(sum(int(A[i,j])*b[j] for j in range(A.cols))%p for i in range(A.rows)) for b in B)
    return free,B


def automorphisms(E):
    all_edges={tuple(sorted(e)) for e in E}
    elements=[]
    for triple in product(range(1,8),repeat=3):
        im=[0]*8
        for x in range(1,8):im[x]=(triple[0] if x&1 else 0)^(triple[1] if x&2 else 0)^(triple[2] if x&4 else 0)
        if len(set(im))!=8:continue
        pt=[im[x]-1 for x in range(1,8)]
        ln=[]
        for w in range(1,8):
            q=next(t for t in range(1,8) if all(dot2(t,im[x])==dot2(w,x) for x in range(1,8)))
            ln.append(7+q-1)
        perm=tuple(pt+ln)
        assert {tuple(sorted((perm[a],perm[b]))) for a,b in E}==all_edges
        elements.append(perm)
    assert len(elements)==168 and len(set(elements))==168
    return elements


def order_of(g):
    order=0;x=list(range(len(g)))
    while True:
        x=[g[v] for v in x];order+=1
        if x==list(range(len(g))):return order


def signed_edge_image(E,edge_idx,g,edge_lookup):
    a,b=E[edge_idx];aa,bb=g[a],g[b]
    return edge_lookup[tuple(sorted((aa,bb)))],(1 if aa<bb else -1)


def traces_of_action(E,c0,c1,c2,g):
    edge_lookup={e:i for i,e in enumerate(E)}
    tr_graph_v=sum(g[v]==v for v in range(14))
    tr_graph_e=sum(s for eid in range(len(E)) for j,s in [signed_edge_image(E,eid,g,edge_lookup)] if j==eid)
    t0=sum(tuple(sorted((g[a],g[b])))==(a,b) for a,b in c0)
    t1=sum(s for eid,v in c1 for j,s in [signed_edge_image(E,eid,g,edge_lookup)] if j==eid and g[v]==v)
    t2=0
    for ei,fi in c2:
        ei2,s=signed_edge_image(E,ei,g,edge_lookup)
        fi2,t=signed_edge_image(E,fi,g,edge_lookup)
        if tuple(sorted((ei2,fi2)))==(ei,fi):t2+=s*t*(1 if ei2<fi2 else -1)
    h1=1-tr_graph_v+tr_graph_e
    h2=t0-t1+t2-1+h1
    return t0,t1,t2,h1,h2


def direct_top_character(E,c2,g,free,basis,p=101):
    edge_lookup={e:i for i,e in enumerate(E)}
    c2_lookup={v:i for i,v in enumerate(c2)}
    moved=[]
    for ei,fi in c2:
        ei2,s=signed_edge_image(E,ei,g,edge_lookup)
        fi2,t=signed_edge_image(E,fi,g,edge_lookup)
        moved.append((c2_lookup[tuple(sorted((ei2,fi2)))],s*t*(1 if ei2<fi2 else -1)))
    trace=0
    for k,b in enumerate(basis):
        f=free[k]
        trace+=sum(s*b[i] for i,(j,s) in enumerate(moved) if j==f)
    value=trace%p
    return value if value<=p//2 else value-p


def main():
    E=make_graph()
    c0,c1,c2,d1,d2=chain_data(E)
    snf=smith_normal_form(d2,domain=ZZ)
    invariants=Counter(abs(int(snf[i,i])) for i in range(min(snf.rows,snf.cols)))
    assert invariants==Counter({1:153,2:1,0:14})
    ranks={p:(rank_prime(d1,p),rank_prime(d2,p)) for p in [2,3,101]}
    assert ranks=={2:(90,153),3:(90,154),101:(90,154)}
    # The sum-of-trajectories chain map from two particles to the graph
    # induces a surjection on rational H1: rank([d1;T])-rank(d1)=8.
    T=SparseMatrix(len(E),len(c1),{(eid,j):1 for j,(eid,v) in enumerate(c1)})
    assert T*d2==zeros(T.rows,d2.cols)
    assert rank_prime(d1.col_join(T),101)-ranks[101][0]==8
    free,basis=top_nullspace(d2,101)
    elements=automorphisms(E)
    group_counts=Counter();hom_chars=defaultdict(Counter)
    for g in elements:
        degree=order_of(g)
        t0,t1,t2,h1,h2=traces_of_action(E,c0,c1,c2,g)
        actual=direct_top_character(E,c2,g,free,basis)
        assert actual==h2,(degree,actual,h2)
        group_counts[degree]+=1
        hom_chars[degree][(h1,h2)]+=1
    assert group_counts==Counter({1:1,2:21,3:56,4:42,7:48})
    assert dict(hom_chars)=={1:Counter({(8,14):1}),2:Counter({(0,-2):21}),3:Counter({(-1,-1):56}),4:Counter({(0,2):42}),7:Counter({(1,0):48})}
    # χ8=(8,0,-1,0,1) and χ6=(6,-2,0,2,-1), ordered by element order.
    for order in [1,2,3,4,7]:
        ch2=next(iter(hom_chars[order]))[1]
        ch8={1:8,2:0,3:-1,4:0,7:1}[order]
        ch6={1:6,2:-2,3:0,4:2,7:-1}[order]
        assert ch2==ch8+ch6
    print('GRAPH vertices=14 edges=21 collineations=168')
    print('CUBICAL_CELL_COUNTS C0=91 C1=252 C2=168; d1*d2=0')
    print('SMITH_DIAGONAL_D2 1^153 2^1 0^14')
    print('BOUNDARY_RANKS_MOD_PRIMES '+repr({p:list(ranks[p]) for p in sorted(ranks)}))
    print('INTEGRAL_HOMOLOGY H0=Z H1=Z^8+Z/2 H2=Z^14')
    print('ELEMENT_ORDERS '+repr({o:group_counts[o] for o in [1,2,3,4,7]}))
    print('CHARACTERS H1_AND_H2_BY_ORDER '+repr({o:list(hom_chars[o])[0] for o in [1,2,3,4,7]}))
    print('SECOND_HOMOLOGY_Q_AS_GL3F2_MODULE rational_6_plus_Steinberg_8')
    print('DIRECT_F101_TOP_KERNEL_ACTION agrees with signed cellular Lefschetz for all 168 elements')
    print('VERIFY_OK')

if __name__=='__main__':main()
