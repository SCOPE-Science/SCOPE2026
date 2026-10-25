#!/usr/bin/env python3
"""Exact integral reduced-chain certificate for multipath complexes of bidirected K(2,n).
Only the Python standard library is required.  Indices are zero based.
"""
from itertools import combinations
from collections import Counter
from math import gcd


def complex_data(n):
    # A,B are vertices 0,1; leaves are 2,...,n+1.
    arcs = [(u,v) for i in range(n) for h in (0,1)
            for u,v in ((h,2+i),(2+i,h))]
    def multipath(S):
        follow, incoming = {}, set()
        for e in S:
            u,v = arcs[e]
            if u in follow or v in incoming:
                return False
            follow[u] = v
            incoming.add(v)
        for u in follow:
            v = u
            for _ in range(len(S)):
                v = follow.get(v)
                if v is None:
                    break
                if v == u:
                    return False
        return True
    # A multipath in K(2,n) uses at most four arcs: each hub can
    # contribute at most one incoming and one outgoing arc.
    faces = {0: [()]}
    for k in range(1, 5):
        faces[k] = [S for S in combinations(range(4*n),k) if multipath(S)]
    for k in range(1,5):
        fs=set(faces[k-1])
        assert all(S[:j]+S[j+1:] in fs for S in faces[k] for j in range(k))
    chains = {k: set(range(len(faces[k]))) for k in range(5)}
    differentials = {}
    for k in range(1,5):
        idx={face:i for i,face in enumerate(faces[k-1])}
        differentials[k]={i:{idx[S[:j]+S[j+1:]]:(-1)**j
                                for j in range(k)}
                          for i,S in enumerate(faces[k])}
    return arcs,faces,chains,differentials


def check_d_squared_zero(chains, ds):
    for k in range(2,5):
        for a in chains[k]:
            dd={}
            for b,c in ds[k][a].items():
                for q,v in ds[k-1][b].items():
                    dd[q]=dd.get(q,0)+c*v
            assert all(z==0 for z in dd.values())


def cancel_unit_pairs(chains, ds):
    """Perform exact unimodular chain cancellation in descending degree.

    For a unit incidence u from a k-cell a to a (k-1)-cell b,
    the surviving degree-k differential is the Schur complement
    D'[r,x]=D[r,x]-D[r,a]*D[b,x]/u.  Rows a in D_(k+1)
    and columns b in D_(k-1) are then removed.  This splits off
    a contractible two-generator chain over Z and preserves integral homology.
    """
    pivot_counts=Counter()
    check_d_squared_zero(chains,ds)
    while True:
        selected=None
        for k in range(4,1,-1):
            for a in sorted(chains[k]):
                for b,u in sorted(ds[k][a].items()):
                    if abs(u)==1:
                        selected=(k,a,b,u)
                        break
                if selected is not None:break
            if selected is not None:break
        if selected is None:break
        k,a,b,u=selected
        assert a in chains[k] and b in chains[k-1] and abs(u)==1
        oldcol=dict(ds[k][a])
        for x in sorted(chains[k]):
            if x==a:continue
            c=ds[k][x].get(b,0)
            if c:
                for r,v in oldcol.items():
                    updated=ds[k][x].get(r,0)-c*v//u
                    if updated:ds[k][x][r]=updated
                    else:ds[k][x].pop(r,None)
            ds[k][x].pop(b,None)
        chains[k].remove(a)
        del ds[k][a]
        chains[k-1].remove(b)
        if k<4:
            for x in chains[k+1]:ds[k+1][x].pop(a,None)
        if k>1:del ds[k-1][b]
        pivot_counts[k]+=1
        check_d_squared_zero(chains,ds)
    # Degree zero now means empty-face chain; the augmentation C_0 -> Z
    # is represented by one incidence from a remaining vertex to ()
    # if the complex is nonempty.  Cancel this unit separately.
    if chains[0]:
        p=next(iter(chains[0]))
        for a in sorted(chains[1]):
            if abs(ds[1][a].get(p,0))==1:
                u=ds[1][a][p]
                col=ds[1][a]
                for x in chains[1]:
                    if x==a:continue
                    c=ds[1][x].get(p,0)
                    if c:
                        for r,v in col.items():
                            value=ds[1][x].get(r,0)-c*v//u
                            if value:ds[1][x][r]=value
                            else:ds[1][x].pop(r,None)
                    ds[1][x].pop(p,None)
                chains[1].remove(a);del ds[1][a]
                chains[0].remove(p)
                for x in chains[2]:ds[2][x].pop(a,None)
                pivot_counts[1]+=1
                break
    check_d_squared_zero(chains,ds)
    remaining={k:len(chains[k]) for k in chains}
    boundary={k:{a:dict(ds[k][a]) for a in sorted(chains[k]) if ds[k][a]}
              for k in ds}
    return pivot_counts,remaining,boundary


def independent_rank_mod_p(faces,p):
    """Separate modular rank calculation on unreduced simplicial boundaries."""
    dims=[len(faces[k]) for k in range(5)]
    ranks={0:0,5:0}
    for k in range(1,5):
        ids={f:i for i,f in enumerate(faces[k-1])}
        pivots={}
        for S in faces[k]:
            col={ids[S[:j]+S[j+1:]]:(-1)**j%p for j in range(k)}
            while col:
                r=min(col)
                c=col[r]
                if r not in pivots:
                    inv=pow(c,-1,p)
                    pivots[r]={i:(v*inv)%p for i,v in col.items() if v%p}
                    break
                for i,v in pivots[r].items():
                    nv=(col.get(i,0)-c*v)%p
                    if nv:col[i]=nv
                    else:col.pop(i,None)
        ranks[k]=len(pivots)
    return ranks,[dims[k]-ranks[k]-ranks[k+1] for k in range(1,5)]


def main():
    expected={
        1:({2:2,1:1},[0,1,0,0,0]),
        2:({3:6,2:7,1:1},[0,0,3,2,0]),
        3:({4:12,3:30,2:11,1:1},[0,0,1,6,0]),
        4:({4:71,3:65,2:15,1:1},[0,0,0,8,1])}
    for n in (1,2,3,4):
        arcs,faces,chains,ds=complex_data(n)
        initial=[len(faces[k]) for k in range(5)]
        ranks2,betti2=independent_rank_mod_p(faces,2)
        ranks3,betti3=independent_rank_mod_p(faces,3)
        count,remaining,boundary=cancel_unit_pairs(chains,ds)
        exp_piv,exp_critical=expected[n]
        assert dict(count)==exp_piv
        assert [remaining[k] for k in range(5)]==exp_critical
        print('n=',n,'f(-1..3)=',initial,'unit pivots=',dict(count),
              'critical(-1..3)=',exp_critical,flush=True)
        print(' mod2 reduced Betti H0..H3=',betti2,
              'mod3=',betti3,flush=True)
        if n<4:
            assert all(not entries for entries in boundary.values())
        else:
            assert list(boundary[4])==[71]
            coeff=list(boundary[4][71].values())
            assert sorted(coeff)==[-2,2,2]
            assert gcd(*coeff)==2
            assert all(not boundary[k] for k in (1,2,3))
            assert betti2==[0,0,8,1] and betti3==[0,0,7,0]
            print(' residual boundary from one 3-cell to eight 2-cells:',
                  boundary[4][71],'; gcd=',gcd(*coeff),flush=True)
    print('PASS: all exact integral chain reductions and field checks.')

if __name__=='__main__':main()
