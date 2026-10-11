#!/usr/bin/env python3
"""Exact finite verification of double-star multipath homology and cone-link identities.
Uses standard Python only; this check supplements the general homotopy proof.
"""
from itertools import combinations

def arcs(a,b):
    assert a>=1 and b>=1
    undirected=[(0,1)]+[(0,i) for i in range(2,a+2)]+[(1,j) for j in range(a+2,a+b+2)]
    return [(u,v) for x,y in undirected for u,v in ((x,y),(y,x))]

def allowed(sub):
    source=[u for u,v in sub]; target=[v for u,v in sub]
    if len(set(source))<len(source) or len(set(target))<len(target): return False
    ds={u:v for u,v in sub}
    for v in ds:
        seen=set(); u=v
        while u in ds:
            if u in seen: return False
            seen.add(u); u=ds[u]
    return True

def faces(a,b):
    ed=arcs(a,b)
    f=[[] for _ in range(5)]
    for k in range(5):
        f[k]=[sum(1<<i for i in comb) for comb in combinations(range(len(ed)),k) if allowed([ed[i] for i in comb])]
    assert not any(allowed([ed[i] for i in comb]) for comb in combinations(range(len(ed)),5)),(a,b)
    return f

def rank_mod(rows,p):
    piv={}
    for bits in rows:
        v=bits.copy()
        while v:
            col=min(v); x=v[col]%p
            if not x: del v[col]; continue
            if col in piv:
                for k,z in piv[col].items():
                    v[k]=(v.get(k,0)-x*z)%p
                    if v[k]==0: del v[k]
            else:
                inv=pow(x,-1,p)
                piv[col]={k:(z*inv)%p for k,z in v.items() if z%p}
                break
    return len(piv)

def bettis(a,b,p):
    fs=faces(a,b)
    rk=[0]*5
    for k in range(1,5):
        ids={f:i for i,f in enumerate(fs[k-1])}
        boundaries=[]
        for F in fs[k]:
            bits=[i for i in range(2*(a+b+1)) if F&(1<<i)]
            row={ids[F^(1<<i)]: (1 if j%2==0 else p-1) for j,i in enumerate(bits)}
            boundaries.append(row)
        rk[k]=rank_mod(boundaries,p)
    # Index k corresponds to reduced degree k-1. In particular k=0 is reduced H_-1.
    reduced=[len(fs[k])-rk[k]- (rk[k+1] if k<4 else 0) for k in range(5)]
    return reduced, [len(x) for x in fs]

def predicted(a,b):
    lo,hi=sorted((a,b))
    if lo==1 and hi<=2: return [0,0,1,0,0]
    if lo==1: return [0,0,0,hi*hi-3*hi+1,0]
    if lo==2: return [0,0,0,hi*hi-hi-1,0]
    ra=a*a-3*a+1; rb=b*b-3*b+1
    return [0,0,0,2*(a-1)*(b-1),ra*rb]

def check_links(a,b):
    e=arcs(a,b)
    for central in (0,1):
        face_index=central
        actual={i for i in range(2,len(e)) if allowed([e[face_index],e[i]])}
        if central==0:
            expect={i for i in range(2,len(e)) if e[i][1]==0 or e[i][0]==1}
        else:
            expect={i for i in range(2,len(e)) if e[i][0]==0 or e[i][1]==1}
        assert actual==expect,(a,b,central,'vertices')
        for i,j in combinations(actual,2):
            # The only compatible pairs are one allowed arc incident at each hub.
            assert allowed([e[face_index],e[i],e[j]]) == ((e[i][0]==0 or e[i][1]==0) != (e[j][0]==0 or e[j][1]==0)),(a,b,central,i,j)
        assert not allowed([e[0],e[1]])

if __name__=='__main__':
    total=0
    for a in range(1,7):
        for b in range(a,7):
            check_links(a,b)
            expected=predicted(a,b)
            for p in (2,3,5):
                got,counts=bettis(a,b,p)
                assert got==expected, (a,b,p,got,expected)
            if (a,b) in ((1,1),(1,3),(2,2),(2,4),(3,3),(3,4),(4,4),(5,5),(6,6)):
                print('a,b',a,b,'face-counts',counts,'reduced-Betti-H-1-through-H3',expected)
            total+=1
    print('VERIFY_OK',total,'parameter pairs, three fields, and both central-edge links')
