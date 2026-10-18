#!/usr/bin/env python3
"""Reproduce the connected-four-face and integral-topology certificates.

Only Python's standard library is required. The general homotopy theorem has
an independent mathematical proof; finite checks detect sign and range errors.
"""
from itertools import combinations
from math import comb


def adj_matrix(n, edges):
    a = [set() for _ in range(n)]
    for i,j in edges:
        assert 0 <= i < n and 0 <= j < n and i != j
        a[i].add(j); a[j].add(i)
    return a


def connected(s,a):
    s=set(s)
    if not s: return False
    reached={next(iter(s))}
    while True:
        nxt=reached | {u for v in reached for u in a[v] if u in s}
        if nxt==reached: break
        reached=nxt
    return reached==s


def has_short_cycle(a, max_length=5):
    n=len(a)
    for k in range(3,max_length+1):
        for subset in combinations(range(n),k):
            root=subset[0]; rest=subset[1:]
            # Examine simple cycles by depth-first search, without external tools.
            def dfs(current,used):
                if len(used)==k:
                    return root in a[current]
                return any(dfs(v,used+(v,)) for v in subset if v not in used and v in a[current])
            if dfs(root,(root,)):
                return True
    return False


def connected_fours(a):
    n=len(a)
    return [t for t in combinations(range(n),4) if connected(t,a)]


def closed_five_check(a):
    for s in combinations(range(len(a)),5):
        assert any(not connected(t,a) for t in combinations(s,4)),s


def free_face_certificate(a):
    four=connected_fours(a)
    incidence={}
    for t in four:
        for tri in combinations(t,3):
            incidence.setdefault(tri,[]).append(t)
    choices={}
    for t in four:
        admissible=[tri for tri in combinations(t,3) if len(incidence[tri])==1]
        assert admissible,('no free triangle',t)
        choices[t]=admissible[0]
    assert len(set(choices.values()))==len(four)
    return four, choices


def rank_f2(columns):
    piv={}
    for x in columns:
        while x:
            bit=x.bit_length()-1
            if bit in piv: x^=piv[bit]
            else:
                piv[bit]=x
                break
    return len(piv)


def direct_cut_homology_mod2(a):
    n=len(a); d=n-5
    verts=tuple(range(n))
    # The full codimension-one skeleton and disconnected-four facets.
    rows=list(combinations(verts,n-5))
    row_index={s:i for i,s in enumerate(rows)}
    facets=[s for s in combinations(verts,n-4)
            if not connected(tuple(v for v in verts if v not in s),a)]
    columns=[]
    for facet in facets:
        b=0
        for t in combinations(facet,n-5): b^=1<<row_index[t]
        columns.append(b)
    rank_top=rank_f2(columns)
    htop=len(facets)-rank_top
    # In the complete (d-1)-skeleton, rank of boundary d-1 equals C(n-1,d-1).
    hcodim=len(rows)-comb(n-1,d-1)-rank_top
    return htop,hcodim,len(facets),rank_top


def pattern(n,kind):
    if kind=='path': edges=[(i,i+1) for i in range(n-1)]
    elif kind=='cycle': edges=[(i,(i+1)%n) for i in range(n)]
    elif kind=='star': edges=[(0,i) for i in range(1,n)]
    elif kind=='forest': edges=[(i,i+1) for i in range(n//2-1)]+[(i,i+1) for i in range(n//2,n-1)]
    elif kind=='cycleleaf': edges=[(i,(i+1)%6) for i in range(6)]+[(i,i+1) for i in range(5,n-1)]
    elif kind=='twocycles':
        assert n>=12
        edges=[(i,(i+1)%6) for i in range(6)]+[(i,6+(i-6+1)%6) for i in range(6,12)]
    elif kind=='heawood':
        # Seven Fano points, seven lines via cyclic difference-set {0,1,3}.
        edges=[(p,7+l) for p in range(7) for l in range(7) if ((p-l)%7) in (0,1,3)]
    elif kind=='mobius-kantor':
        edges=[(i,(i+1)%8) for i in range(8)]
        edges += [(8+i,8+(i+3)%8) for i in range(8)]
        edges += [(i,8+i) for i in range(8)]
    else: raise ValueError(kind)
    return adj_matrix(n,edges)


def checks(a,name,check_direct=True):
    n=len(a)
    assert n>=6
    assert not has_short_cycle(a,5),(name,'girth')
    closed_five_check(a)
    four,choices=free_face_certificate(a)
    degrees=[len(x) for x in a]
    c4_formula=sum(comb(x,3) for x in degrees if x>=3)
    c4_formula+=sum((degrees[u]-1)*(degrees[v]-1) for u in range(n) for v in a[u] if u<v)
    assert len(four)==c4_formula,(name,len(four),c4_formula)
    beta=comb(n-1,3)-len(four)
    assert beta>=0
    if check_direct:
        top,codim,facets,rank=direct_cut_homology_mod2(a)
        assert (top,codim)==(beta,0),(name,top,codim,beta)
        assert facets==comb(n,4)-len(four)
    print(f'{name}: vertices={n}, connected_fours={len(four)}, beta={beta}, free_triangles={len(choices)}')


def main():
    count=0
    for n in range(6,11):
        for kind in ('path','star','forest','cycle'):
            checks(pattern(n,kind),f'{kind}-{n}',check_direct=True)
            count+=1
    for n in range(7,11):
        checks(pattern(n,'cycleleaf'),f'cycleleaf-{n}',check_direct=True)
        count+=1
    for n,kind in [(12,'twocycles'),(14,'heawood'),(16,'mobius-kantor')]:
        checks(pattern(n,kind),kind,check_direct=False)
        count+=1
    # An exhaustive labeled six-vertex census, without graph isomorphism pruning.
    n=6; allpairs=list(combinations(range(n),2)); tested=0
    for mask in range(1<<len(allpairs)):
        a=adj_matrix(n,[e for i,e in enumerate(allpairs) if mask&(1<<i)])
        if has_short_cycle(a,5): continue
        checks_quiet(a)
        tested+=1
    assert tested>1000
    print(f'VERIFY_OK families={count} exhaustive_labeled_six_vertex_graphs={tested}')


def checks_quiet(a):
    n=len(a)
    closed_five_check(a)
    four,choices=free_face_certificate(a)
    deg=[len(x) for x in a]
    expected=sum(comb(d,3) for d in deg if d>=3)+sum((deg[i]-1)*(deg[j]-1) for i in range(n) for j in a[i] if i<j)
    assert len(four)==expected
    beta=comb(n-1,3)-expected
    top,codim,_,_=direct_cut_homology_mod2(a)
    assert (top,codim)==(beta,0)

if __name__=='__main__':main()
