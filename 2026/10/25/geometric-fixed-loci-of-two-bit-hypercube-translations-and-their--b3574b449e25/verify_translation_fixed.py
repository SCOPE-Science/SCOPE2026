#!/usr/bin/env python3
"""Independent finite checks of low-scale cube translation fixed-point complexes."""
from itertools import combinations


def wt(x):
    return x.bit_count()


def orbits(n, w):
    t = (1 << w) - 1
    seen = set()
    out = []
    for x in range(1 << n):
        if x in seen:
            continue
        o = frozenset((x, x ^ t))
        assert len(o) == 2
        seen.update(o)
        out.append(o)
    return out


def diameter_ok(a, b, scale):
    return all(wt(x ^ y) <= scale for x in a for y in b)


def admissible_orbit(o, scale):
    x, y = tuple(o)
    return wt(x ^ y) <= scale


def brute_graph(n, w, scale):
    oo = [o for o in orbits(n, w) if admissible_orbit(o, scale)]
    edges = set()
    for i, j in combinations(range(len(oo)), 2):
        if diameter_ok(oo[i], oo[j], scale):
            edges.add((i, j))
    return oo, edges


def connected_components(N, edges):
    adj = [set() for _ in range(N)]
    for i,j in edges:
        adj[i].add(j)
        adj[j].add(i)
    seen = set()
    cc=0
    for i in range(N):
        if i in seen: continue
        cc+=1
        stack=[i]
        seen.add(i)
        while stack:
            for j in adj[stack.pop()]:
                if j not in seen:
                    seen.add(j)
                    stack.append(j)
    return cc,adj


def check_one(n,w):
    for r in (0,1,2):
        oo,edges=brute_graph(n,w,r)
        if w>r:
            assert not oo and not edges
            continue
        assert w<=2
        if r==1:
            assert w==1 and len(oo)==(1<<(n-1)) and not edges
            continue
        assert r==2
        assert len(oo)==(1<<(n-1))
        assert len(edges)==(n-1)*(1<<(n-2))
        cc,adj=connected_components(len(oo),edges)
        assert cc==1
        assert not any((adj[i] & adj[j]) for i,j in edges), (n,w,'triangle')
        if w==1:
            ids={min(o)>>1:i for i,o in enumerate(oo)}
            for i,j in combinations(range(1<<(n-1)),2):
                a,b=ids[i],ids[j]
                assert ((min(a,b),max(a,b)) in edges) == (wt(i^j)==1)
        else:
            m=n-2
            ids={((x>>1)&1,x>>2):i for i,o in enumerate(oo) for x in o if not (x&1)}
            assert len(ids)==(1<<(n-1))
            # The explicit cube coordinates are (p XOR parity(z), z).
            def phi(p,z): return (z<<1)|(p^(wt(z)%2))
            labels={phi(p,z):i for (p,z),i in ids.items()}
            assert len(labels)==len(ids)
            for a,b in combinations(range(1<<(n-1)),2):
                i,j=labels[a],labels[b]
                assert ((min(i,j),max(i,j)) in edges)==(wt(a^b)==1)
        rank=len(edges)-len(oo)+cc
        assert rank==(n-3)*(1<<(n-2))+1
    return True


def check_characters(n):
    m=n-2
    V=1<<(m+1)
    E=(m+1)*(1<<m)
    generators=[(1,0)]+[(1,1<<j) for j in range(m)]
    def chi_trace(a,b):
        total=0
        for dp in (0,1):
            for dz in range(1<<m):
                c0=V if (dp,dz)==(0,0) else 0
                c1=E if (dp,dz)==(0,0) else (-(1<<m) if (dp,dz) in generators else 0)
                h1=c1-c0+1
                sign=-1 if ((a*dp+wt(b&dz))%2) else 1
                total+=h1*sign
        assert total%V==0
        return total//V
    for a in (0,1):
        for b in range(1<<m):
            actual=chi_trace(a,b)
            expected=(m-wt(b)) if a==1 else (max(wt(b)-1,0))
            assert actual==expected,(n,a,b,actual,expected)
    assert sum(chi_trace(a,b) for a in (0,1) for b in range(1<<m)) == (n-3)*(1<<(n-2))+1



def verify_scale_three_deaths(n):
    """Every cube square has an explicit integral triangular filling at scale three."""
    m=n-2
    gens=[(1,0)]+[(1,1<<i) for i in range(m)]
    def add(v,s): return (v[0]^s[0],v[1]^s[1])
    def orb(v):
        p,z=v
        x=(z<<2)|(p<<1)
        return (x,x^3)
    def edge(x,y):
        return (tuple(sorted((x,y))),1 if x<y else -1)
    def bd_tri(T):
        a,b,c=T
        terms=((b,c,1),(a,c,-1),(a,b,1))
        out={}
        for x,y,coef in terms:
            k,sgn=edge(x,y)
            out[k]=out.get(k,0)+coef*sgn
        return out
    def check_triple(T):
        xx=set()
        for v in T: xx.update(orb(v))
        return all(wt(a^b)<=3 for a,b in combinations(xx,2))
    sq_ct=0
    for p in (0,1):
        for z in range(1<<m):
            v=(p,z)
            for j,k in combinations(range(m+1),2):
                v0=v; v1=add(v0,gens[j]); v2=add(v1,gens[k]); v3=add(v0,gens[k])
                cycle=(v0,v1,v2,v3)
                if j==0 or k==0:
                    tris=[(v0,v1,v2),(v0,v2,v3)]
                else:
                    center=add(v0,gens[0])
                    assert center not in cycle
                    tris=[(center,cycle[i],cycle[(i+1)%4]) for i in range(4)]
                bd={}
                for tri in tris:
                    assert check_triple(tri),(n,j,k,tri)
                    for e,c in bd_tri(tri).items(): bd[e]=bd.get(e,0)+c
                expect={}
                for i in range(4):
                    e,c=edge(cycle[i],cycle[(i+1)%4])
                    expect[e]=expect.get(e,0)+c
                assert {e:c for e,c in bd.items() if c}!={}
                assert {e:c for e,c in bd.items() if c}=={e:c for e,c in expect.items() if c}
                sq_ct+=1
    return sq_ct

def main():
    N=0
    squares=0
    for n in range(2,8):
        for w in range(1,n+1):
            check_one(n,w)
            N+=1
        check_characters(n)
        squares+=verify_scale_three_deaths(n)
        print(f'n={n}: all support weights and Fourier multiplicities match')
    print(f'VERIFY_OK support_cases={N} scale_three_square_fillings={squares}; all orbit-graph, homology, and character checks passed')


if __name__=='__main__':
    main()
