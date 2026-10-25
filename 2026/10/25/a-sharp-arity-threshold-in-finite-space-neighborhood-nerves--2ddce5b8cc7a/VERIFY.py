#!/usr/bin/env python3
"""Finite exact checks for k-wise neighborhood nerves of rank-1/k Boolean spaces.
This script supplements, not replaces, the all-parameter mathematical proof.
"""
from itertools import combinations
from math import comb


def vertices(n, k):
    ts = list(combinations(range(n), k))
    return ts, {s: n+i for i, s in enumerate(ts)}


def faces(n, k, r):
    ts, apex = vertices(n, k)
    fs = [range(n)] if r <= k else ts
    fs += [tuple(s) + (apex[s],) for s in ts]
    out = set()
    for facet in fs:
        for j in range(1, len(facet)+1):
            out.update(combinations(facet,j))
    return sorted(out, key=lambda f:(len(f), f))


def gf2rank(vectors):
    piv={}
    for x in vectors:
        while x:
            p=x.bit_length()-1
            if p in piv:
                x^=piv[p]
            else:
                piv[p]=x
                break
    return len(piv)


def betti(faces_list):
    groups={}
    for f in faces_list:
        groups.setdefault(len(f)-1,[]).append(f)
    dim=max(groups)
    ranks={0:1}
    for j in range(1,dim+1):
        idx={f:i for i,f in enumerate(groups[j-1])}
        columns=[]
        for f in groups[j]:
            c=0
            for sub in combinations(f,len(f)-1):
                c^=1<<idx[sub]
            columns.append(c)
        ranks[j]=gf2rank(columns)
    ranks[dim+1]=0
    return tuple(len(groups.get(j,[]))-ranks[j]-ranks[j+1] for j in range(dim+1))


def representative_permutations(n):
    def partitions(total, bound):
        if total==0:
            yield ()
        for a in range(min(total,bound),0,-1):
            for tail in partitions(total-a,a):
                yield (a,)+tail
    for lens in partitions(n,n):
        sigma=[0]*n
        start=0
        for ell in lens:
            for a in range(ell):
                sigma[start+a]=start+(a+1)%ell
            start+=ell
        yield lens, sigma


def sign_sequence(images):
    parity=0
    for i in range(len(images)):
        for j in range(i+1,len(images)):
            if images[i]>images[j]:parity^=1
    return -1 if parity else 1


def chain_lefschetz(n,k,fs,sigma):
    ts, apex=vertices(n,k)
    inverse={v:t for t,v in apex.items()}
    total=-1  # augmented empty face in reduced Euler trace
    for f in fs:
        image=[sigma[v] if v<n else apex[tuple(sorted(sigma[i] for i in inverse[v]))] for v in f]
        if tuple(sorted(image))==f:
            total += (-1 if len(f)%2==0 else 1)*sign_sequence(image)
    return total


def wedge_character(n,k,lens):
    coeff=[0]*(k+1)
    coeff[0]=1
    for ell in lens:
        for i in range(k-ell,-1,-1):
            coeff[i+ell]+=(-1 if ell%2==0 else 1)*coeff[i]
    quotient=[]
    for a in coeff:
        quotient.append(a-(quotient[-1] if quotient else 0))
    return quotient[k]


def literal_neighborhood_faces(n,k,r):
    ts, apex=vertices(n,k)
    universe=list(range(n))+list(apex.values())
    opens=[]
    for i in range(n):
        opens.append(frozenset([i]+[apex[t] for t in ts if i in t]))
    for t in ts:
        opens.append(frozenset([apex[t]]))
    out=set()
    for length in range(1,len(universe)+1):
        for f in combinations(universe,length):
            good=True
            for j in range(1,min(r,length)+1):
                for sub in combinations(f,j):
                    intersect=set(universe)
                    for v in sub:intersect.intersection_update(opens[v])
                    if not intersect:
                        good=False
                        break
                if not good:break
            if good:out.add(f)
    return out


def main():
    cases=0; faces_total=0; character_tests=0; literals=0
    for n in range(3,8):
        for k in range(2,n):
            for r in (2,k,k+1,k+2):
                fs=faces(n,k,r)
                b=betti(fs)
                expected=(0,)*(len(b))
                if r>k:
                    expected=tuple(comb(n-1,k) if j==k-1 else 0 for j in range(len(b)))
                assert b==expected, (n,k,r,b,expected)
                if n<=4:
                    assert set(fs)==literal_neighborhood_faces(n,k,r),(n,k,r)
                    literals+=1
                faces_total+=len(fs)
                cases+=1
                for lens,sigma in representative_permutations(n):
                    Lef=chain_lefschetz(n,k,fs,sigma)
                    target=0 if r<=k else ((-1)**(k-1))*wedge_character(n,k,lens)
                    assert Lef==target,(n,k,r,lens,Lef,target)
                    character_tests+=1
    print('FINITE_NEIGHBORHOOD_CASES',cases)
    print('TOTAL_ENUMERATED_NONEMPTY_FACES',faces_total)
    print('LITERAL_TOPOLOGY_COMPARISONS',literals)
    print('SIGNED_EQUIVARIANT_LEFSCHETZ_CHECKS',character_tests)
    print('VERIFY_OK')
if __name__=='__main__': main()
