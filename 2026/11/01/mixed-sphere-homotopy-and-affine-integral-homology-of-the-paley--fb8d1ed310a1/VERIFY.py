#!/usr/bin/env python3
"""Exact finite checks for the two-independence complex of the Paley graph on 13 vertices.

Run with Python 3 and the standard library: python3 verify_paley13.py
The mathematical interpretation of the integral Morse matrix is explained in RESULT.md.
"""
from collections import Counter, deque
from itertools import combinations

P=13
SQUARES={i*i % P for i in range(1,P)}
NEIGHBOR=[sum(1<<j for j in range(P) if (j-i)%P in SQUARES) for i in range(P)]

def all_faces():
    forbidden=set()
    for v in range(P):
        near=[u for u in range(P) if NEIGHBOR[v]>>u&1]
        for u,w in combinations(near,2):
            forbidden.add((1<<v)|(1<<u)|(1<<w))
    fs=[]
    for mask in range(1,1<<P):
        # First test: the induced degree of each selected vertex is at most one.
        degrees_ok=all((NEIGHBOR[v]&mask).bit_count()<=1 for v in range(P) if mask>>v&1)
        # Second test: no triple inducing a vertex with two neighbors is selected.
        triples_ok=not any(mask&triple==triple for triple in forbidden)
        assert degrees_ok==triples_ok
        if degrees_ok:fs.append(mask)
    return set(fs),len(forbidden)

def dim(mask):return mask.bit_count()-1

def boundary(mask,faces):
    vertices=[i for i in range(P) if mask>>i&1]
    return {mask^(1<<v):(-1)**j for j,v in enumerate(vertices) if mask^(1<<v) in faces}

def match(faces):
    remaining=set(faces);pairs=[]
    for v in range(P):
        e=1<<v
        for s in sorted(remaining):
            t=s|e
            if not s&e and t in remaining:
                remaining.remove(s);remaining.remove(t);pairs.append((s,t))
    assert 2*len(pairs)+len(remaining)==len(faces)
    return pairs,remaining

def acyclic(faces,pairs):
    edges={u:[] for u in faces};indeg={u:0 for u in faces}
    matched=set(pairs)
    for top in faces:
        for v in range(P):
            if not top>>v&1:continue
            low=top^(1<<v)
            if low not in faces:continue
            u,w=(low,top) if (low,top) in matched else (top,low)
            edges[u].append(w);indeg[w]+=1
    q=deque(x for x in faces if indeg[x]==0)
    count=0
    while q:
        x=q.popleft();count+=1
        for y in edges[x]:
            indeg[y]-=1
            if indeg[y]==0:q.append(y)
    return count,len([0 for x in edges for y in edges[x]])

def check_d_squared(d):
    for top,lower in d.items():
        dd={}
        for mid,a in lower.items():
            for bottom,b in d[mid].items():
                dd[bottom]=dd.get(bottom,0)+a*b
        assert all(v==0 for v in dd.values()),(top,dd)

def cancellation(faces,pairs):
    # Algebraic elementary Morse reduction over Z with only unit pivots.
    D={s:boundary(s,faces) for s in faces}
    check_d_squared(D)
    for low,high in pairs:
        coeff=D[high].get(low,0)
        assert coeff in (-1,1)
        for cell in list(D):
            if cell==high or dim(cell)!=dim(high):continue
            num=D[cell].get(low,0)
            if num:
                assert num % coeff==0
                ratio=num//coeff
                for b,c in D[high].items():
                    value=D[cell].get(b,0)-ratio*c
                    if value:D[cell][b]=value
                    else:D[cell].pop(b,None)
        for cell in D:
            if dim(cell)==dim(high)+1:D[cell].pop(high,None)
        D.pop(low);D.pop(high)
    check_d_squared(D)
    return D

def det(matrix):
    # Exact fraction-free small determinant via the Leibniz expansion.
    n=len(matrix)
    if n==0:return 1
    if n==1:return matrix[0][0]
    return sum((-1)**j*matrix[0][j]*det([row[:j]+row[j+1:] for row in matrix[1:]]) for j in range(n))

def mod_rank(rows,prime):
    A=[[v%prime for v in row] for row in rows]
    if not A:return 0
    R,C=len(A),len(A[0]);i=0
    for j in range(C):
        r=next((t for t in range(i,R) if A[t][j]),None)
        if r is None:continue
        A[i],A[r]=A[r],A[i]
        inv=pow(A[i][j],-1,prime)
        A[i]=[(v*inv)%prime for v in A[i]]
        for t in range(R):
            if t==i:continue
            f=A[t][j]
            if f:A[t]=[(x-f*y)%prime for x,y in zip(A[t],A[i])]
        i+=1
        if i==R:break
    return i

def sign_of_list(a):
    return (-1)**sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))

def reduced_lefschetz(faces,mul,offset):
    total=-1 # reduced alternating trace: subtract the H_0 of a connected space
    by_dim=Counter();counts=Counter()
    for mask in faces:
        v=[i for i in range(P) if mask>>i&1]
        moved=[(mul*i+offset)%P for i in v]
        if set(v)==set(moved):
            term=(-1)**(len(v)-1)*sign_of_list(moved)
            total+=term
            by_dim[len(v)-1]+=term;counts[len(v)-1]+=1
    return total,dict(sorted(counts.items())),dict(sorted(by_dim.items()))

def main():
    faces,num_forbidden=all_faces()
    fvec=Counter(dim(s) for s in faces)
    assert [fvec[k] for k in range(4)]==[13,78,143,78]
    assert len(faces)==312
    facets=[s for s in faces if not any((s|(1<<v)) in faces for v in range(P) if not s>>v&1)]
    assert len(facets)==78 and all(dim(s)==3 for s in facets)
    pairs,critical=match(faces)
    critvec=Counter(dim(s) for s in critical)
    assert len(pairs)==149 and critvec=={0:1,2:6,3:7}
    visited,incidences=acyclic(faces,pairs)
    assert (visited,incidences)==(312,897)
    D=cancellation(faces,pairs)
    assert set(D)==critical
    rows=sorted(s for s in critical if dim(s)==2)
    cols=sorted(s for s in critical if dim(s)==3)
    M=[[D[col].get(row,0) for col in cols] for row in rows]
    assert len(M)==6 and all(len(x)==7 for x in M)
    expected=[[0,0,-1,1,0,0,1],
              [0,-1,0,1,0,0,0],
              [1,-1,0,0,0,0,0],
              [0,1,-1,0,0,0,1],
              [0,0,0,1,-1,0,0],
              [0,0,0,0,1,-1,1]]
    assert M==expected
    sub=[[M[i][j] for j in (0,1,2,3,4)] for i in (0,1,2,4,5)]
    minor=det(sub)
    assert abs(minor)==1
    assert all(mod_rank(M,p)==5 for p in (2,3,5,7,101))
    # Separate unreduced simplicial boundary ranks, using modular arithmetic.
    dims={d:sorted(s for s in faces if dim(s)==d) for d in range(4)}
    cmat={}
    for degree in (1,2,3):
        row_index={f:i for i,f in enumerate(dims[degree-1])}
        cmat[degree]=[[0]*len(dims[degree]) for _ in dims[degree-1]]
        for j,s in enumerate(dims[degree]):
            for lower,value in boundary(s,faces).items():
                cmat[degree][row_index[lower]][j]=value
    for p in (2,3,5,101):
        ranks={k:mod_rank(cmat[k],p) for k in (1,2,3)}
        assert ranks=={1:12,2:66,3:76},(p,ranks)
        b2=len(dims[2])-ranks[2]-ranks[3]
        b3=len(dims[3])-ranks[3]
        assert (b2,b3)==(1,2)
    # Exhaustive signed simplicial trace for every affine graph automorphism.
    residues=sorted(SQUARES)
    assert residues==[1,3,4,9,10,12]
    values={}
    for mul in residues:
        for off in range(P):
            assert all(((mul*i+off)-(mul*j+off))%P in SQUARES for i in range(P) for j in range(P) if (i-j)%P in SQUARES)
            values[mul,off]=reduced_lefschetz(faces,mul,off)[0]
    char=[values[pow(4,k,P),0] for k in range(6)]
    assert char==[-1,0,2,-3,2,0]
    assert all(values[mul,off]==values[mul,0] for mul in residues for off in range(P))
    print('GRAPH Paley(13) squares=',residues,'full_affine_group_order=',len(values))
    print('FACES independent_triples_forbidden=',num_forbidden,'face_vector=',[fvec[k] for k in range(4)],'all_facets_dimension_3=',len(facets))
    print('MORSE pairs=',len(pairs),'critical_counts=',dict(sorted(critvec.items())),'acyclic_hasse_vertices=',visited,'incidences=',incidences)
    print('INTEGRAL_MORSE_MATRIX rows=6 cols=7')
    for row in M:print(row)
    print('INTEGRAL_UNIT_MINOR rows=(0,1,2,4,5) cols=(0,1,2,3,4) determinant=',minor)
    print('RAW_BOUNDARY_RANKS all_primes_2_3_5_101= (12,66,76)')
    print('LEFSCHETZ powers_4=[%s]'%(','.join(map(str,char))))
    print('LEFSCHETZ m=4:',reduced_lefschetz(faces,4,0))
    print('LEFSCHETZ m=-1:',reduced_lefschetz(faces,12,0))
    print('LEFSCHETZ nonzero_translation:',reduced_lefschetz(faces,1,1))
    print('CONSEQUENCES reduced_H2_Z=Z reduced_H3_Z=Z^2, multiplier_4: H2=-1 H3=order_three_trace_minus_one')
    print('ALL_CHECKS_PASS')

if __name__=='__main__':main()
