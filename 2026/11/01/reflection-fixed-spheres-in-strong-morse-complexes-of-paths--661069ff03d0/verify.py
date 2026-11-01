#!/usr/bin/env python3
"""Finite checks for a fixed-point model of path strong-Morse complexes.

Run without dependencies: python3 verify.py. The all-parameter theorem is proved
separately by comparator constraints and a graph-neighborhood recurrence.
"""
from itertools import permutations, combinations, product
from collections import defaultdict


def graph_edges(m):
    nv = 2*m - 1
    edges = {frozenset((i,i+1)) for i in range(nv-1)}
    edges |= {frozenset((j,j+3)) for j in range(1,nv-3,2)}
    return nv,edges


def independent_faces(m):
    nv,edges = graph_edges(m)
    out=set()
    for mask in range(1<<nv):
        if not any((mask>>i & 1) and (mask>>j & 1) for i,j in (tuple(edge) for edge in edges)):
            out.add(mask)
    return out


def gradient_mask_from_order(order):
    n=len(order)-1
    position={v:i for i,v in enumerate(order)}
    mask=0
    for v in range(n+1):
        low=[u for u in (v-1,v+1) if 0<=u<=n and position[u]<position[v]]
        if len(low)==1:
            edge=min(v,low[0]); parity=0 if v==edge else 1
            mask|=1<<(2*edge+parity)
    return mask


def geom_fixed_faces_permutation(n):
    m=n//2
    pairs=[]
    for j in range(m):
        for parity in (0,1):
            idx=2*j+parity
            reflected=2*(n-1-j)+(1-parity)
            pairs.append((idx,reflected))
    attainable=set()
    for order in permutations(range(n+1)):
        mask=gradient_mask_from_order(order)
        f=0
        for j,(u,v) in enumerate(pairs):
            if mask>>u &1 and mask>>v &1:f|=1<<j
        attainable.add(f)
    ffaces=set()
    for maximal in attainable:
        sub=maximal
        while True:
            ffaces.add(sub)
            if not sub:break
            sub=(sub-1)&maximal
    return ffaces


def forbidden_word_faces(n):
    # Existence of a total vertex ordering reduces to consistency of
    # inequalities between adjacent path-vertex ranks.
    faces=[]
    for word in product((0,1,2),repeat=n):  # 0: blank, 1: right, 2: left
        incompatible=False
        for i in range(n-1):
            if word[i]==2 and word[i+1]==1:incompatible=True
        for i in range(n-2):
            if word[i]==2 and word[i+2]==1:incompatible=True
        if not incompatible:faces.append(word)
    return faces


def geometric_fixed_faces_from_words(n):
    m=n//2
    attainable=set()
    for word in forbidden_word_faces(n):
        mask=0
        for i in range(m):
            j=n-i-1
            for d in (1,2):
                if word[i]==d and word[j]==3-d:
                    mask |= 1 << (2*i+(d==2))
        attainable.add(mask)
    return attainable


def permutation_recurrence(m):
    nv,edges=graph_edges(m)
    neig={i:set() for i in range(nv)}
    for edge in edges:
        a,b=tuple(edge);neig[a].add(b);neig[b].add(a)
    assert neig[0]=={1}
    assert neig[1]=={0,2,4}
    keep=sorted(set(range(nv))-{0,1,2,4})
    phi={0:3}
    for j in range(1,2*m-5):
        phi[j]=j+5 if j%2 else j+3
    assert sorted(phi.values())==keep,(m,phi,keep)
    smaller_nv,smaller_edges=graph_edges(m-2)
    assert smaller_nv==len(keep)
    mapped={frozenset((phi[i],phi[j])) for edge in smaller_edges for i,j in [tuple(edge)]}
    remaining={edge for edge in edges if set(edge)<=set(keep)}
    assert mapped==remaining,(m,mapped^remaining)


def reduced_f2_betti(faces):
    degrees=defaultdict(list)
    for f in faces:
        degrees[f.bit_count()-1].append(f)
    ranks={}
    for d in sorted(degrees):
        if d<1:continue
        row={f:i for i,f in enumerate(degrees[d-1])}
        pivots={}
        for f in degrees[d]:
            col=0
            tmp=f
            while tmp:
                bit=tmp & -tmp
                col ^= 1<<row[f^bit]
                tmp -= bit
            while col:
                high=col.bit_length()-1
                if high in pivots:
                    col^=pivots[high]
                else:
                    pivots[high]=col
                    break
        ranks[d]=len(pivots)
    result={}
    for d in degrees:
        if d>=0:
            b=len(degrees[d])-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0)
            if b:result[d]=b
    return result


def main():
    norder=0
    for n in range(1,9):
        f=geom_fixed_faces_permutation(n)
        norder+=__import__('math').factorial(n+1)
        if n==1:
            assert f=={0}
        else:
            target=independent_faces(n//2)
            assert f==target,('gradient fixed mismatch',n, f^target)
    print('GRADIENT_PERMUTATION_OK n=1..8 orders='+str(norder))
    scanned=0
    for n in range(2,13):
        actual=geometric_fixed_faces_from_words(n)
        target=independent_faces(n//2)
        scanned+=3**n
        assert actual==target,('word fixed mismatch',n,actual^target)
    print('WORD_CONSTRAINT_OK n=2..12 words='+str(scanned))
    for m in range(3,31):permutation_recurrence(m)
    print('GRAPH_RECURRENCE_OK m=3..30')
    for m in range(1,8):
        result=reduced_f2_betti(independent_faces(m))
        target={m//2-1:1} if m%2==0 else {}
        assert result==target,('homology mismatch',m,result,target)
    print('FINITE_HOMOLOGY_OK m=1..7')
    print('VERIFY_OK')

if __name__=='__main__':main()
