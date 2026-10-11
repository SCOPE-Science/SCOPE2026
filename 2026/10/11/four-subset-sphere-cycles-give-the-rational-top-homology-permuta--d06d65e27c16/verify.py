"""Exact finite checks for the four-subset sphere character of Cov(m,2)."""
from itertools import combinations, permutations, product
from collections import defaultdict

Q=101

def edges(m):
    return tuple(combinations(range(m),2))

def is_cover_two(face,m):
    return any(all(a in uv or b in uv for a,b in face)
               for uv in combinations(range(m),2))

def map_edge(e,colors):
    a,b = colors[e[0]],colors[e[1]]
    return tuple(sorted((a,b))) if a!=b else tuple(sorted((a,(a+1)%4)))

def rank_mod(rows,n):
    piv={}; rank=0
    for row in rows:
        v={k:1 for k in row}
        while v:
            k=min(v)
            if k not in piv:
                piv[k]=v;rank+=1;break
            pivot=piv[k]
            x=v[k] * pow(pivot[k],-1,Q)%Q
            for j,b in pivot.items():
                y=(v.get(j,0)-x*b)%Q
                if y:v[j]=y
                else:v.pop(j,None)
    return rank

def test():
    # Four graph vertices yield the boundary of a five-simplex.
    em=edges(4)
    assert len(em)==6
    for mask in range(1<<6):
        face=[em[j] for j in range(6) if mask>>j&1]
        assert is_cover_two(face,4)==(mask!=63)
    # Relabeling tetrahedron vertices preserves orientation of its six edge-vertices.
    pos={e:j for j,e in enumerate(em)}
    for p in permutations(range(4)):
        perm=[pos[tuple(sorted((p[a],p[b])))] for a,b in em]
        inversions=sum(perm[a]>perm[b] for a in range(6) for b in range(a+1,6))
        assert inversions%2==0
    # Explicit edge images and induced cycles, including collapsed colors.
    map_checks=0
    for m in (4,5,6):
        Es=edges(m)
        colorings=list(product(range(4),repeat=m))
        if m==6: colorings=colorings[::29]
        for f in colorings:
            mapped={e:map_edge(e,f) for e in Es}
            for uv in combinations(range(m),2):
                source=[e for e in Es if e[0] in uv or e[1] in uv]
                im=set(mapped[e] for e in source)
                assert is_cover_two(im,4)
                map_checks+=1
            for T in combinations(range(m),4):
                im=[mapped[e] for e in combinations(T,2)]
                if len(set(f[x] for x in T))==4:
                    assert len(set(im))==6
                else:
                    assert len(set(im))<=4
                map_checks+=1
    # The 4-color transversal evaluations have full column rank.
    rank_data=[]
    for m in range(4,9):
        T=list(combinations(range(m),4))
        rows=[]
        for f in product(range(4),repeat=m):
            row=[j for j,U in enumerate(T) if len({f[x] for x in U})==4]
            if row:rows.append(row)
        r=rank_mod(rows,len(T))
        assert r==len(T), (m,r,len(T))
        rank_data.append((m,len(T),len(rows)))
    # Fourier isolator at a fixed four-set: its coefficient is -24*4^(m-4).
    for m in range(4,8):
        T=tuple(range(4))
        U=tuple(range(1,5)) if m>=5 else T
        for S in (T,U):
            coeff=0j
            for f in product(range(4),repeat=m):
                if len({f[x] for x in S})==4:
                    coeff+=1j**sum(f[x] for x in T)
            expected=-24*(4**(m-4)) if S==T else 0
            assert abs(coeff-expected)<1e-8,(m,S,coeff,expected)
    print('VERIFY_OK; vertex map and orientation checks:',map_checks,'; full ranks:',rank_data)

if __name__=='__main__': test()
