#!/usr/bin/env python3
"""Standalone finite checks for overlapping-clique clique-free homology.

Only ordinary finite simplicial linear algebra and signed Lefschetz traces
are checked; the general theorem requires its separate spectral-sequence proof.
"""
from itertools import combinations, permutations, product
from collections import defaultdict
from math import comb


def faces(a, b, s, t):
    n = a + b + s
    aa = set(range(a)); bb = set(range(a, a+b))
    cc = set(range(a+b, n))
    # Build the graph first; test every candidate face against all t-cliques.
    e = set()
    for block in [aa|cc, bb|cc]:
        e.update(tuple(sorted(uv)) for uv in combinations(block,2))
    forbidden = []
    for sub in combinations(range(n), t):
        if all(tuple(sorted(uv)) in e for uv in combinations(sub,2)):
            forbidden.append(sum(1 << v for v in sub))
    result = defaultdict(list)
    for mask in range(1, 1 << n):
        if not any((mask & bad) == bad for bad in forbidden):
            result[mask.bit_count()-1].append(mask)
    return result


def bettis_mod2(ff):
    ranks = {}
    for d in sorted(ff):
        if d == 0: continue
        low = {mask:i for i, mask in enumerate(ff[d-1])}
        pivots = {}
        for mask in ff[d]:
            vec = 0; bit = mask
            while bit:
                v = bit & -bit; bit -= v
                vec ^= 1 << low[mask ^ v]
            while vec:
                h = vec.bit_length() - 1
                if h in pivots: vec ^= pivots[h]
                else:
                    pivots[h] = vec; break
        ranks[d] = len(pivots)
    out = {d:len(v)-ranks.get(d,0)-ranks.get(d+1,0) for d,v in ff.items()}
    out[0] -= 1
    return {d:b for d,b in out.items() if b}


def expected(a,b,s,t):
    k=t-1
    return {2*k-j-1:comb(s,j)*comb(a-1,k-j)*comb(b-1,k-j)
            for j in range(min(k,s)+1)
            if (k-j)<=a-1 and (k-j)<=b-1
            and comb(s,j)*comb(a-1,k-j)*comb(b-1,k-j)}


def cycle_lengths(p):
    seen=set(); lengths=[]
    for i in range(len(p)):
        if i in seen:continue
        cycle=[]; x=i
        while x not in seen:
            seen.add(x); cycle.append(x); x=p[x]
        lengths.append(len(cycle))
    return lengths


def signed_subset_poly(p):
    z=[1]
    for length in cycle_lengths(p):
        z += [0]*length
        for d in range(len(z)-1,length-1,-1):
            z[d] += (-1)**(length+1)*z[d-length]
    return z


def aug_exterior_trace(p,d):
    if d<0 or d>len(p)-1:return 0
    pol=signed_subset_poly(p)
    q=0
    for i in range(d+1):q=pol[i]-q
    return q


def predicted_euler(a,b,s,t,pa,pb,pc):
    k=t-1; cp=signed_subset_poly(pc)
    return sum((-1)**(2*k-j-1)*cp[j]*aug_exterior_trace(pa,k-j)*aug_exterior_trace(pb,k-j)
               for j in range(min(k,s)+1))


def fixed_face_euler(ff, p):
    # Alternating signed trace on augmented simplicial chains.
    outcome=-1
    for d, masks in ff.items():
        for mask in masks:
            vv=[i for i in range(len(p)) if mask>>i & 1]
            image=[p[i] for i in vv]
            if set(image)!=set(vv):continue
            flips=sum(image[i]>image[j] for i in range(len(image)) for j in range(i+1,len(image)))
            outcome+=(-1)**(d+flips)
    return outcome


def make_perm(pa,pb,pc,a,b):
    return tuple(pa)+tuple(a+i for i in pb)+tuple(a+b+i for i in pc)


def main():
    params=[(2,2,2,3),(3,3,2,3),(3,4,2,3),(2,4,3,3),
            (4,4,2,3),(4,4,2,4),(4,4,3,4),(4,5,2,4),
            (1,3,2,3),(3,3,3,3),(3,3,1,3)]
    for a,b,s,t in params:
        ff=faces(a,b,s,t)
        measured=bettis_mod2(ff)
        theory=expected(a,b,s,t)
        assert measured==theory,(a,b,s,t,measured,theory)
        print(f'BETTI a={a} b={b} s={s} t={t}: {measured}; nonempty_faces={sum(map(len,ff.values()))}')
    # Direct signed Lefschetz traces, computed independently from face orbits.
    trials=0
    for a,b,s,t in [(2,2,2,3),(3,3,2,3),(3,4,2,3),(4,4,3,4)]:
        ff=faces(a,b,s,t)
        pas=list(permutations(range(a)))
        pbs=list(permutations(range(b)))
        pcs=list(permutations(range(s)))
        choices=list(product(pas,pbs,pcs))
        # Full checks in small cases, deterministic thinning in larger cases.
        if len(choices)>300:
            step=max(1,len(choices)//120)
            choices=choices[::step]
        for pa,pb,pc in choices:
            observed=fixed_face_euler(ff,make_perm(pa,pb,pc,a,b))
            predicted=predicted_euler(a,b,s,t,pa,pb,pc)
            assert observed==predicted,(a,b,s,t,pa,pb,pc,observed,predicted)
            trials+=1
    print('SIGNED LEFSCHETZ COMPARISONS:',trials)
    print('ALL FINITE CHECKS PASS')

if __name__=='__main__': main()
