#!/usr/bin/env python3
"""Independent finite checks of bidirected linear multipath fixed spaces and characters."""
from collections import defaultdict
from itertools import product

def faces(n):
    # None=no arrow, 0=forward, 1=backward; neighboring nonzero arcs must agree.
    for a in product((-1,0,1), repeat=n):
        if any(a[i]!=-1 and a[i+1]!=-1 and a[i]!=a[i+1] for i in range(n-1)):
            continue
        yield tuple(2*i+a[i] for i in range(n) if a[i]!=-1)

def permutation(v,n,k):
    i,s=divmod(v,2)
    return {'F':2*i+1-s,'R':2*(n-1-i)+1-s,'J':2*(n-1-i)+s}[k]

def sign_permutation(seq):
    return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))

def traces(n):
    acc={x:0 for x in 'FRJ'}
    for f in faces(n):
        for k in acc:
            im=tuple(permutation(v,n,k) for v in f)
            if set(im)==set(f):
                acc[k] += (-1 if len(f)%2==0 else 1)*sign_permutation(im)
    d=(n-1)//2
    return tuple((-1)**d*acc[k] for k in 'FRJ')

def mod2_betti(n):
    fs=defaultdict(list)
    for f in faces(n): fs[len(f)-1].append(sum(1<<v for v in f))
    ranks={}
    for d in range(1,max(fs)+1):
        targets={x:i for i,x in enumerate(fs[d-1])}
        piv={}; rank=0
        for mask in fs[d]:
            b=0; sub=mask
            while sub:
                bit=sub&-sub; sub-=bit
                b^=1<<targets[mask^bit]
            while b:
                p=b.bit_length()-1
                if p not in piv: piv[p]=b;rank+=1;break
                b^=piv[p]
        ranks[d]=rank
    reduced = {}
    for d in range(max(fs)+1):
        value=len(fs[d])-ranks.get(d,0)-ranks.get(d+1,0)
        if d==0:value-=1
        if value:reduced[d]=value
    return reduced

def orbit_map(n,k):
    m=(n+1)//2
    if k=='R':
        return [[2*i+s,2*(n-1-i)+1-s] for i in range(m-1) for s in (0,1)]
    if k=='J':
        out=[[2*i+s,2*(n-1-i)+s] for i in range(m-1) for s in (0,1)]
        out += ([[2*(m-1)+s] if n%2 else [2*(m-1)+s, 2*m+s] for s in (0,1)])
        return out
    raise ValueError(k)

def check_fixed_orbits(n,k):
    m=(n+1)//2
    o=orbit_map(n,k)
    target=m-1 if k=='R' else m
    # Verify all orbit unions agree with all and only target faces.
    origin={tuple(sorted(f)) for f in faces(n)}
    target_faces={tuple(sorted(f)) for f in faces(target)}
    for choices in product((-1,0,1), repeat=target):
        labels=tuple(2*i+s for i,s in enumerate(choices) if s>=0)
        union=tuple(sorted(v for a in labels for v in o[a]))
        assert (union in origin)==(labels in target_faces),(n,k,labels,union)
    # Each setwise invariant nonempty face is a union of those permitted orbits.
    all_orbits=[]; seen=set()
    for v in range(2*n):
        if v in seen: continue
        u=permutation(v,n,k)
        orb=frozenset((v,u));seen.update(orb)
        if frozenset(orb) not in {frozenset(x) for x in o}:
            assert not any(orb.issubset(f) for f in origin)

for n in range(1,13):
    m=(n+1)//2
    got=traces(n)
    wanted=((-1)**m,(-1)**((m+1)//2),(-1)**(m+(m+1)//2))
    assert got==wanted,(n,got,wanted)
    check_fixed_orbits(n,'R')
    check_fixed_orbits(n,'J')
    if n<=6:
        assert mod2_betti(n)=={m-1:1},(n,mod2_betti(n))
    print(f'n={n:2d} dim={m-1:2d} traces(F,R,RF)={got} fixed orbit complexes: BL_{m-1},BL_{m}; mod2='+ (str(mod2_betti(n)) if n<=6 else 'not computed'))
print('PASS: 12 direct signed character checks; 24 orbit-complex comparisons; 6 independent GF(2) homology checks.')
