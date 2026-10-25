"""Finite exact checks for equivariant higher independence complexes.
Run: python verify_higher_independence.py
Uses only the standard Python library.
"""
from itertools import combinations, permutations, product
from math import comb, factorial


def det_poly_on_permutation(perm, n):
    seen=set(); p=[1]
    for v in range(n):
        if v in seen: continue
        x=v; length=0
        while x not in seen:
            seen.add(x); length+=1; x=perm[x]
        factor=[0]*(length+1);factor[0]=1;factor[length]=(-1)**(length+1)
        new=[0]*(len(p)+length)
        for i,a in enumerate(p):
            for j,b in enumerate(factor): new[i+j]+=a*b
        p=new
    return p


def div_one_plus_t(p):
    q=[]
    for a in p:
        q.append(a-(q[-1] if q else 0))
    assert q[-1]==0
    return q[:-1]


def sign_of_sort(seq):
    return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))


def faces_of_higher_independence(parts,r):
    vertex_count=sum(parts)
    which=[]
    for i,m in enumerate(parts):which.extend([i]*m)
    result=[]
    for k in range(vertex_count+1):
        for f in combinations(range(vertex_count),k):
            if k<=r or len({which[v] for v in f})<=1:result.append(f)
    return result


def lefschetz(perm,faces):
    # Reduced Lefschetz (the empty face is in degree -1).
    out=0
    for face in faces:
        mapped=tuple(perm[v] for v in face)
        if tuple(sorted(mapped))!=face: continue
        out+=(-1)**(len(face)-1)*sign_of_sort(mapped)
    return out


def predicted_character(perm,parts,r):
    n=len(perm)
    offsets=[0]
    for m in parts:offsets.append(offsets[-1]+m)
    a=div_one_plus_t(det_poly_on_permutation(perm,n))
    result=a[r] if r<len(a) else 0
    for i,m in enumerate(parts):
        start=offsets[i]
        if set(perm[start:start+m])==set(range(start,start+m)):
            restricted=tuple(perm[start+j]-start for j in range(m))
            b=div_one_plus_t(det_poly_on_permutation(restricted,m))
            result-=b[r] if r<len(b) else 0
    return result


def enumerate_automorphisms(parts, exchange_parts=False):
    s=len(parts);assert not exchange_parts or len(set(parts))==1
    starts=[0]
    for m in parts:starts.append(starts[-1]+m)
    part_perms=list(permutations(range(s))) if exchange_parts else [tuple(range(s))]
    internal=[list(permutations(range(m))) for m in parts]
    for part_perm in part_perms:
        for local in product(*internal):
            mapping=[0]*starts[-1]
            for i,m in enumerate(parts):
                for j in range(m):mapping[starts[i]+j]=starts[part_perm[i]]+local[i][j]
            yield tuple(mapping)



def mod2_homology(faces, dimension):
    """Reduced chain ranks over F2, independent of the character check."""
    by_dimension={d:[] for d in range(-1,dimension+2)}
    for face in faces:
        d=len(face)-1
        if d<=dimension+1: by_dimension[d].append(face)
    ranks={-1:0}
    for d in range(0, dimension+2):
        lower={f:i for i,f in enumerate(by_dimension[d-1])}
        pivots={}
        for face in by_dimension[d]:
            col=0
            for j in range(len(face)):
                col ^= 1<<lower[face[:j]+face[j+1:]]
            while col:
                k=col.bit_length()-1
                if k in pivots: col^=pivots[k]
                else:
                    pivots[k]=col
                    break
        ranks[d]=len(pivots)
    betti={d:len(by_dimension[d])-ranks[d]-ranks[d+1] for d in range(0,dimension+1)}
    return betti


def compute_for(parts,r,exchange=False):
    faces=faces_of_higher_independence(parts,r)
    expected_rank=comb(sum(parts)-1,r)-sum(comb(m-1,r) if m-1>=r else 0 for m in parts)
    assert lefschetz(tuple(range(sum(parts))),faces)==(-1)**(r-1)*expected_rank
    betti=mod2_homology(faces,r)
    assert all(b==(expected_rank if d==r-1 else 0) for d,b in betti.items()),(parts,r,betti)
    group_size=0; sum_chi=0
    for g in enumerate_automorphisms(parts,exchange):
        value=predicted_character(g,parts,r)
        assert lefschetz(g,faces)==(-1)**(r-1)*value, (parts,r,g,value)
        group_size+=1;sum_chi+=value
    assert sum_chi%group_size==0
    invariants=sum_chi//group_size
    expected=0 if exchange else (comb(len(parts)-1,r) if len(parts)-1>=r else 0)
    assert invariants==expected,(parts,r,exchange,invariants,expected)
    print(f'parts={parts} r={r} total_faces={len(faces)} automorphisms={group_size} rank={expected_rank} invariant_rank={invariants} checks=passed')


if __name__=='__main__':
    compute_for((2,3),2)
    compute_for((2,2,2),2)
    compute_for((2,2,2),2,exchange=True)
    compute_for((2,2,2,2),2)
    compute_for((2,2,2,2),2,exchange=True)
    compute_for((2,2,2,2),3)
    compute_for((2,2,2,2),3,exchange=True)
    compute_for((3,2,2),3)
    print('HIGHER_INDEPENDENCE_EQUIVARIANT_CHECKS_PASSED')
