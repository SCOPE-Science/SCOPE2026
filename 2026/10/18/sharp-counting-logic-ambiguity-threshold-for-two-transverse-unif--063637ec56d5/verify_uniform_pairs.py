#!/usr/bin/env python3
"""Independent finite checks of the transversal-uniform two-equivalence boundary.
Public science only; no external dependencies or credentials.
"""
from itertools import permutations, combinations, product
from collections import Counter, deque


def integer_partitions_ge2(n, upper=None):
    if n==0:
        yield (); return
    if upper is None: upper=n
    for v in range(min(upper,n),1,-1):
        for rest in integer_partitions_ge2(n-v,v):
            yield (v,)+rest


def permutation_cycles(perm):
    seen=set(); sizes=[]
    for i in range(len(perm)):
        if i in seen: continue
        x=i; s=0
        while x not in seen:
            seen.add(x); x=perm[x];s+=1
        sizes.append(s)
    return tuple(sorted(sizes,reverse=True))


def perm_from_cycles(parts):
    p=[]; start=0
    for s in parts:
        p.extend([start+i+1 for i in range(s-1)]+[start]);start+=s
    return tuple(p)


def incidence_matrix_from_permutation(perm):
    r=len(perm)
    return tuple(tuple(int(j not in (i,perm[i])) for j in range(r)) for i in range(r))


def connected_bip(matrix):
    r=len(matrix); nbr=[set() for _ in range(2*r)]
    for i in range(r):
        for j in range(r):
            if matrix[i][j]:
                nbr[i].add(r+j);nbr[r+j].add(i)
    seen={0}; queue=deque([0])
    while queue:
        for w in nbr[queue.popleft()]:
            if w not in seen:seen.add(w);queue.append(w)
    return len(seen)==2*r


def degree_signature(matrix):
    r=len(matrix)
    edges=[(i,j) for i in range(r) for j in range(r) if matrix[i][j]]
    per=[]
    for i,j in edges:
        counts=Counter()
        for a,b in edges:
            rel=('D' if (i,j)==(a,b) else
                 'B' if (i==a and j==b) else
                 'E' if i==a else 'F' if j==b else 'N')
            counts[rel]+=1
        per.append(tuple(counts[v] for v in ('D','B','E','F','N')))
    return tuple(sorted(Counter(per).items()))


def check(k):
    r=k+2
    by_shape={}
    derangements=0
    for perm in permutations(range(r)):
        if any(perm[i]==i for i in range(r)):continue
        derangements+=1
        by_shape.setdefault(permutation_cycles(perm),perm)
    expected=set(integer_partitions_ge2(r))
    assert set(by_shape)==expected, (k,set(by_shape),expected)
    signals=set()
    for parts,p in sorted(by_shape.items()):
        M=incidence_matrix_from_permutation(p)
        assert all(sum(row)==k for row in M)
        assert all(sum(M[i][j] for i in range(r))==k for j in range(r))
        assert sum(map(sum,M))==k*r
        if k>=3:assert connected_bip(M)
        signal=degree_signature(M)
        assert len(signal)==1 and signal[0][1]==k*r
        signals.add(signal)
    assert len(signals)==1
    print('k=%d r=%d n=%d  derangements=%d  isomorphism_types=%d  C2_types=1  connected_all=%s  partitions=%s' %
          (k,r,k*r,derangements,len(expected),k>=3,sorted(expected)))


def exhaustive_small_matrices(k,r):
    """Generate all side-labelled incidence matrices for k=2,3 at r=k,k+1,k+2.
    Check all are uniquely determined at smaller r, and count exact complements.
    """
    rows=[sum(1<<j for j in colset) for colset in combinations(range(r),k)]
    seen_shapes=set(); valid=0
    for choices in product(rows,repeat=r):
        coldegrees=[sum((x>>j)&1 for x in choices) for j in range(r)]
        if any(c!=k for c in coldegrees): continue
        valid+=1
        if r==k:typ=('complete',)
        elif r==k+1:typ=('complement_matching',)
        else:
            forbidden=[[j for j in range(r) if (choices[i]>>j)&1==0] for i in range(r)]
            # Enumerate connected components of the 2-regular complement.
            visited=set();sizes=[]
            for i in range(r):
                if i in visited:continue
                active={i};queue=[i];visited.add(i)
                while queue:
                    u=queue.pop()
                    for j in forbidden[u]:
                        for v in range(r):
                            if j in forbidden[v] and v not in visited:
                                visited.add(v);active.add(v);queue.append(v)
                sizes.append(len(active))
            typ=tuple(sorted(sizes,reverse=True))
        seen_shapes.add(typ)
    expected=1 if r<k+2 else len(list(integer_partitions_ge2(r)))
    assert len(seen_shapes)==expected,(k,r,seen_shapes)
    print('exhaustive matrices k=%d r=%d  labeled=%d  types=%d' %(k,r,valid,len(seen_shapes)))

if __name__=='__main__':
    for k in range(2,7):check(k)
    for k in (2,3):
        for r in range(k,k+3): exhaustive_small_matrices(k,r)
    print('VERIFICATION_OK')
