#!/usr/bin/env python3
"""Exact finite checks for second-radius Rips complexes of GP(n,3).

This is a finite diagnostic for the uniform mathematical proof in RESULT.md.
Python 3 standard library only.
"""
from collections import Counter
from itertools import combinations, product


def graph(n):
    g = [set() for _ in range(2*n)]
    def edge(a,b):
        assert a != b
        g[a].add(b); g[b].add(a)
    for i in range(n):
        edge(i,(i+1)%n)
        edge(i,n+i)
        edge(n+i,n+(i+3)%n)
    assert all(len(x)==3 for x in g)
    return g


def square_graph(g):
    h = [set(v) for v in g]
    for i in range(len(g)):
        for x in g[i]:
            h[i].update(g[x])
        h[i].discard(i)
    return h


def faces_of_square(h):
    faces = [set() for _ in range(5)]
    def extend(t,cands):
        if t:
            assert len(t) <= 4
            faces[len(t)-1].add(tuple(t))
        for j,v in enumerate(cands):
            nxt=[w for w in cands[j+1:] if w in h[v]]
            extend(t+(v,),nxt)
    extend((),list(range(len(h))))
    return faces


def neighborhood_core(g):
    c=[set() for _ in range(5)]
    for v in range(len(g)):
        T=tuple(sorted((v,*g[v])))
        for d in range(1,5):
            for t in combinations(T,d):c[d-1].add(t)
    return c


def specials(n):
    result=set()
    for i in range(n):
        result.add(tuple(sorted((i,(i+2)%n,n+(i+3)%n))))
        result.add(tuple(sorted(((i+1)%n,(i+3)%n,n+i))))
    assert len(result)==2*n
    return result


def cycles6(g):
    cycles=set()
    def canonical(p):
        m=min(p)
        a=p.index(m)
        x=p[a:]+p[:a]
        y=[x[0]]+list(reversed(x[1:]))
        return min(tuple(x),tuple(y))
    for a in range(len(g)):
        def walk(p):
            if len(p)==6:
                if p[-1] in g[a]:cycles.add(canonical(p))
                return
            for b in g[p[-1]]:
                if b not in p and b>=a:walk(p+[b])
        walk([a])
    return cycles


def standard_hexagons(n):
    out=set()
    for i in range(n):
        p=[i,(i+1)%n,(i+2)%n,(i+3)%n,n+(i+3)%n,n+i]
        a=p.index(min(p)); x=p[a:]+p[:a];y=[x[0]]+list(reversed(x[1:]))
        out.add(min(tuple(x),tuple(y)))
    return out


def rank_mod2(c):
    ranks=[]
    for d in range(1,len(c)):
        basis={}
        lower={s:i for i,s in enumerate(sorted(c[d-1]))}
        for s in sorted(c[d]):
            x=0
            for j in range(len(s)):
                t=s[:j]+s[j+1:]
                x^=1<<lower[t]
            while x:
                bit=x.bit_length()-1
                if bit not in basis:
                    basis[bit]=x
                    break
                x^=basis[bit]
        ranks.append(len(basis))
    f=[len(a) for a in c]
    betti=[f[0]-ranks[0]-1]
    for d in range(1,len(f)):
        betti.append(f[d]-ranks[d-1]-(ranks[d] if d<len(ranks) else 0))
    return ranks,betti


def test_collapse(g,core):
    live=[set(a) for a in core]
    removed=0
    for v in range(len(g)):
        neighbors=tuple(sorted(g[v]))
        tetra=tuple(sorted((v,*neighbors)))
        tr=neighbors
        assert tetra in live[3] and tr in live[2]
        assert sum(set(tr)<=set(x) for x in live[3])==1
        live[3].remove(tetra);live[2].remove(tr)
        removed+=1
        for a,b in combinations(neighbors,2):
            e=(a,b)
            tri=tuple(sorted((a,b,v)))
            assert e in live[1] and tri in live[2]
            assert sum(set(e)<=set(x) for x in live[2])==1
            assert not any(set(e)<=set(x) for x in live[3])
            live[1].remove(e);live[2].remove(tri)
            removed+=1
    assert removed==4*len(g)
    assert len(live[2])==len(live[3])==len(live[4])==0
    assert live[1]=={tuple(sorted((i,j))) for i in range(len(g)) for j in g[i] if i<j}
    return removed


def inversion_sign(y):
    return -1 if sum(y[i]>y[j] for i in range(len(y)) for j in range(i+1,len(y)))%2 else 1


def sphere_chain(n,i):
    w=[i%n,(i+1)%n,(i+2)%n,(i+3)%n,n+(i+3)%n,n+(i%n)]
    out=Counter()
    for t in product((0,1),repeat=3):
        tri=(w[3*t[0]],w[1+3*t[1]],w[2+3*t[2]])
        out[tuple(sorted(tri))] += ((-1)**sum(t))*inversion_sign(tri)
    return {k:v for k,v in out.items() if v}


def check_chain_boundary(c):
    boundary=Counter()
    for tri,v in c.items():
        for j in range(3):
            boundary[tri[:j]+tri[j+1:]]+=((-1)**j)*v
    assert all(not v for v in boundary.values())


def act(c,n,refl=False):
    res=Counter()
    for simplex,coeff in c.items():
        perm=[]
        for v in simplex:
            j=v%n
            perm.append((n if v>=n else 0)+ ((-j)%n if refl else (j+1)%n))
        res[tuple(sorted(perm))] += coeff*inversion_sign(perm)
    return {k:v for k,v in res.items() if v}


def check(n,do_homology=False,do_collapse=False,do_spheres=False):
    g=graph(n); h=square_graph(g); full=faces_of_square(h); core=neighborhood_core(g)
    missing=[full[d]-core[d] for d in range(5)]
    assert not missing[0] and not missing[1] and not missing[3] and not missing[4]
    assert missing[2]==specials(n)
    assert [len(c) for c in full]==[2*n,9*n,10*n,2*n,0]
    assert cycles6(g)==standard_hexagons(n)
    if do_collapse:assert test_collapse(g,core)==8*n
    if do_spheres:
        for i in range(n):
            z=sphere_chain(n,i)
            assert len(z)==8
            assert set(z).issubset(full[2])
            check_chain_boundary(z)
            assert act(z,n)==sphere_chain(n,(i+1)%n)
            assert act(z,n,refl=True)==sphere_chain(n,(-i-3)%n)
            assert tuple(sorted((i,(i+2)%n,n+(i+3)%n))) in z
    if do_homology:
        ranks,betti=rank_mod2(full)
        assert betti==[0,1,n,0,0],(n,ranks,betti)
        return ranks,betti


def main():
    for n in range(19,73):
        ranks,betti=check(n,do_homology=n in (19,20,21,24,27,30,42,60,72),
                           do_collapse=n in (19,20,21,24,30,42,60,72),
                           do_spheres=n in (19,20,21,24,30,42,60,72)) or (None,None)
        if ranks:print('n',n,'fvector',[2*n,9*n,10*n,2*n], 'boundary ranks mod2',ranks,'reduced betti',betti)
    n=18; c=faces_of_square(square_graph(graph(n)))
    ranks,betti=rank_mod2(c)
    assert betti==[0,0,23,0,0],(ranks,betti)
    print('n=18 exception: fvector',[len(a) for a in c], 'boundary ranks mod2',ranks,'reduced betti',betti)
    print('54 consecutive cases n=19..72 checked for exact face classification and all hexagons.')
    print('8 cases additionally checked for elementary collapse, integral oriented sphere cycles, dihedral action.')
    print('VERIFY_OK_GP_N_3_SCALE_TWO_WEDGE_AND_DIHEDRAL_MODULE')

if __name__=='__main__':main()
