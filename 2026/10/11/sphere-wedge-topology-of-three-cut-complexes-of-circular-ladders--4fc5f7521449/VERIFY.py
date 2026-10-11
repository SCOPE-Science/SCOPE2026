"""Independent finite checks of the circular-ladder three-cut theorem.
Only standard Python is required. The proof for all n>=5 is in RESULT.md.
"""
from itertools import combinations
from math import comb


def build(n):
    N=2*n
    adj=[set() for _ in range(N)]
    def edge(a,b):
        adj[a].add(b);adj[b].add(a)
    for j in range(n):
        edge(j,(j+1)%n)
        edge(n+j,n+(j+1)%n)
        edge(j,n+j)
    return adj


def triangles_and_squares(n,adj):
    N=2*n
    tris=[t for t in combinations(range(N),3)
          if sum(b in adj[a] for a,b in combinations(t,2))>=2]
    fours=[q for q in combinations(range(N),4)
           if all(t in tris for t in combinations(q,3))]
    return tris, fours


def col_boundary(simplex):
    return {simplex[:i]+simplex[i+1:]: (-1)**i
            for i in range(len(simplex))}


def rank_mod_p(cols,p):
    pivots={}
    for col in cols:
        v={row:val%p for row,val in col.items() if val%p}
        while v:
            row=min(v)
            if row not in pivots:
                inv=pow(v[row],-1,p)
                pivots[row]={k:c*inv%p for k,c in v.items() if c*inv%p}
                break
            mult=v[row];basis=pivots[row]
            for k,c in basis.items():
                z=(v.get(k,0)-mult*c)%p
                if z:v[k]=z
                else:v.pop(k,None)
    return len(pivots)


def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
           -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
           +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def main():
    for n in (5,6,7,8,9):
        N=2*n
        adj=build(n)
        tris,fours=triangles_and_squares(n,adj)
        assert len(tris)==6*n and len(fours)==n
        tris_set=set(tris)
        squares={tuple(sorted((j,(j+1)%n,n+j,n+(j+1)%n))) for j in range(n)}
        assert set(fours)==squares
        tcols={t:col_boundary(t) for t in tris}
        # For n>=5, cycle-specific topological classification reduces to a unit minor.
        ring=[]
        for row in (0,n):
            for j in range(n):
                ring.append(tuple(sorted(((j-1)%n+row,j+row,(j+1)%n+row))))
        assert len(set(ring))==2*n and set(ring)<=tris_set
        ring_chords=[tuple(sorted((t[0],t[2]))) if t[1] in adj[t[0]] and t[1] in adj[t[2]] else None for t in ring]
        # Sort-based indices do not preserve cycle orientation; instead find endpoints by adjacency.
        ring_chords=[]
        for t in ring:
            centre=next(v for v in t if sum(w in adj[v] for w in t if w!=v)==2)
            ring_chords.append(tuple(x for x in t if x!=centre))
        assert len(set(ring_chords))==2*n
        for chord, own in zip(ring_chords,ring):
            assert [t for t in tris if chord in list(combinations(t,2))]==[own]
        # Each square: three independent boundary columns, supported in private diagonal/upper-edge rows.
        for j in range(n):
            A=j;B=(j+1)%n;C=n+B;D=n+A
            rows=[tuple(sorted(e)) for e in ((A,C),(B,D),(A,B))]
            cols=[tuple(sorted(t)) for t in ((A,B,C),(B,C,D),(C,D,A))]
            mat=[[tcols[col].get(edge,0) for col in cols] for edge in rows]
            assert abs(det3(mat))==1,(n,j,mat)
            # The three rows occur only in triangles of this square, aside from ring-only paths.
            for rowedge in rows:
                elsewhere=[t for t in tris if rowedge in list(combinations(t,2))
                           and t not in ring]
                assert set(elsewhere)<={tuple(sorted(t)) for t in combinations((A,B,C,D),3)}
        # Independent full boundary ranks in three fields and both chain degrees.
        for p in (2,3,5):
            assert rank_mod_p([tcols[t] for t in tris],p)==5*n,(n,p,'d2')
            assert rank_mod_p([col_boundary(q) for q in fours],p)==n,(n,p,'d3')
        b=comb(N-1,2)-5*n
        assert b==2*n*n-8*n+1
        # Euler characteristic of Alexander dual, combinatorial check.
        assert (N-comb(N,2)+len(tris)-len(fours))==1-b
        print(f'n={n}, connected_triples={len(tris)}, squares={len(fours)}, '
              f'd2_rank={5*n}, d3_rank={n}, beta1={b}, unimodular_blocks={n}')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
