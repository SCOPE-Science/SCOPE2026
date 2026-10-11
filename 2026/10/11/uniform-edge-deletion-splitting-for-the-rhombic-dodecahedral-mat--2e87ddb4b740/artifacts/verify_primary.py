#!/usr/bin/env python3
"""Exact finite simplicial and signed-Morse verification for a polyhedral graph."""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from fractions import Fraction
from itertools import permutations, product


def graph():
    # Cube corners 0..7 indexed by binary tuples in lexicographic order.
    # Face centers 8+2*j+s represent {b_j=s}, j=0,1,2, s=0,1.
    return tuple(sorted((i, 8 + 2*j + b[j]) for i,b in enumerate(product((0,1),repeat=3)) for j in range(3)))


def faces(edges):
    bad=[]
    for a,b in edges:
        bad.append(sum(1<<j for j,(c,d) in enumerate(edges) if a==c or a==d or b==c or b==d))
    arr=[0]
    for f in arr:
        for j in range(f.bit_length(),len(edges)):
            if not (f & bad[j]):
                arr.append(f|(1<<j))
    assert len(set(arr))==len(arr)
    return arr


def matching_and_acyclic(faces_,n):
    fset=set(faces_); partner={}
    for i in range(n):
        bit=1<<i
        for f in faces_:
            h=f|bit
            if f!=h and h in fset and f not in partner and h not in partner:
                partner[f]=h; partner[h]=f
    assert 0 in partner and partner[0].bit_count()==1
    root=partner.pop(0); assert partner.pop(root)==0
    nodes=[f for f in faces_ if f]
    indeg=defaultdict(int);out=defaultdict(list); incidences=0
    for f in nodes:
        for i in range(f.bit_length()):
            if not (f&(1<<i)): continue
            lower=f^(1<<i)
            if not lower:continue
            if partner.get(lower)==f: u,v=lower,f
            else:u,v=f,lower
            out[u].append(v);indeg[v]+=1;incidences+=1
    dq=deque(f for f in nodes if indeg[f]==0);reached=0
    while dq:
        u=dq.popleft();reached+=1
        for v in out[u]:
            indeg[v]-=1
            if indeg[v]==0:dq.append(v)
    assert reached==len(nodes),f'gradient cycle: {reached} / {len(nodes)}'
    for a,b in partner.items():
        assert partner.get(b)==a and abs(a.bit_count()-b.bit_count())==1
        assert a in fset and b in fset
    return partner,root,incidences


def signed_boundary(f):
    return [(f^(1<<i), -1 if k%2 else 1) for k,i in enumerate(i for i in range(f.bit_length()) if f&(1<<i))]


def morse_matrix(partner,crit,lower_dim):
    lower=[f for f in crit if f.bit_count()==lower_dim+1]
    upper=[f for f in crit if f.bit_count()==lower_dim+2]
    assert lower and upper
    @lru_cache(maxsize=None)
    def project(f):
        if f not in partner: return {f:1}
        g=partner[f]
        if g.bit_count()<f.bit_count(): return {}
        inc=signed_boundary(g); pivot=dict(inc)[f]
        out={}
        for h,sgn in inc:
            if h==f:continue
            for q,val in project(h).items():
                out[q]=out.get(q,0)-(sgn//pivot)*val
        return {q:c for q,c in out.items() if c}
    A=[]
    for l in lower:
        A.append([])
    for h in upper:
        out={}
        for g,sgn in signed_boundary(h):
            for q,val in project(g).items():
                out[q]=out.get(q,0)+sgn*val
        for i,l in enumerate(lower):A[i].append(out.get(l,0))
    return A


def independent_columns(M):
    # rational Gaussian elimination: deterministic leftmost independent columns
    rows=len(M);cols=len(M[0]);mat=[[Fraction(v) for v in row] for row in M]
    pivots=[];row=0
    for col in range(cols):
        piv=next((r for r in range(row,rows) if mat[r][col]),None)
        if piv is None:continue
        mat[row],mat[piv]=mat[piv],mat[row]
        x=mat[row][col]
        mat[row]=[v/x for v in mat[row]]
        for rr in range(rows):
            if rr!=row and mat[rr][col]:
                x=mat[rr][col];mat[rr]=[a-x*b for a,b in zip(mat[rr],mat[row])]
        pivots.append(col);row+=1
        if row==rows:break
    assert len(pivots)==rows
    return pivots


def determinant(A):
    # fraction-free Bareiss exact determinant
    n=len(A);m=[list(map(int,r)) for r in A];sign=1;prev=1
    for k in range(n-1):
        if not m[k][k]:
            j=next((j for j in range(k+1,n) if m[j][k]),None)
            if j is None:return 0
            m[k],m[j]=m[j],m[k];sign*=-1
        pivot=m[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=m[i][j]*pivot-m[i][k]*m[k][j]
                assert num%prev==0
                m[i][j]=num//prev
            m[i][k]=0
        prev=pivot
    return sign*m[-1][-1]


def case(label,E,expected):
    F=faces(E);partner,root,inc=matching_and_acyclic(F,len(E))
    critical=[f for f in F if f and f not in partner]
    dims=Counter(f.bit_count()-1 for f in critical)
    target_dim,lower,upper,wedge=expected
    assert dims==Counter({0:1,target_dim-1:lower,target_dim:upper}),(label,dims)
    A=morse_matrix(partner,critical,target_dim-1)
    pivot=independent_columns(A)
    minor=[[row[j] for j in pivot] for row in A]
    det=determinant(minor)
    assert abs(det)==1
    assert upper-lower==wedge
    vec=[sum(f.bit_count()==k for f in F) for k in range(1,max(f.bit_count() for f in F)+1)]
    assert -1 + sum(((-1)**k)*num for k,num in enumerate(vec))==(-1)**target_dim*wedge
    print(f'{label}: edges={len(E)} nonempty_faces={len(F)-1} f_vector={vec} pairs={len(partner)//2} incidences={inc} critical={sorted(dims.items())} matrix={len(A)}x{len(A[0])} nonzero={sum(x!=0 for row in A for x in row)} pivot_columns={pivot} determinant={det} wedge={wedge} dim={target_dim}')


def main():
    E=graph()
    assert len(E)==24 and len(set(E))==24
    deg=Counter(u for e in E for u in e)
    assert Counter(deg.values())==Counter({3:8,4:6})
    e=E[0]; assert e==(0,8)
    Edelete=[z for z in E if z!=e]
    Elink=[z for z in E if not set(z)&set(e)]
    case('full',E,(4,14,53,39))
    case('delete',Edelete,(4,7,33,26))
    case('link',Elink,(3,3,16,13))
    # Coordinate permutations and bitwise xor maps preserve the incidence graph
    # and act transitively on edges (corner, incident face).
    corners=list(product((0,1),repeat=3))
    incidence={(i,8+2*j+b[j]) for i,b in enumerate(corners) for j in range(3)}
    images=set()
    for axes in permutations(range(3)):
        for offset in corners:
            transformed=set()
            for i,b in enumerate(corners):
                newb=tuple(b[axes[k]] ^ offset[k] for k in range(3))
                new_i=corners.index(newb)
                for j in range(3):
                    new_j=axes.index(j)
                    transformed.add((new_i,8+2*new_j+newb[new_j]))
            assert transformed==incidence
            # Image of the fixed incidence (000, coordinate-0 face with value 0).
            images.add((corners.index(offset),8+2*axes.index(0)+offset[axes.index(0)]))
    assert images==incidence
    print('AUTOMORPHISM_EDGE_TRANSITIVITY_OK edges=24')
    print('PRIMARY_VERIFIED')
if __name__=='__main__':main()
