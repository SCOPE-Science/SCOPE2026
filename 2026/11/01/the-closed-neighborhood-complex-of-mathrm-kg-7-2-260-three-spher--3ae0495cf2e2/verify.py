#!/usr/bin/env python3
"""Exact finite verification of the closed-neighborhood KG(7,2) theorem.
Requires Python 3.9+ standard library only. All assertions are exact.
"""
from itertools import combinations
from collections import Counter, deque, defaultdict
from functools import lru_cache
from fractions import Fraction
from math import factorial, prod

N = 7
DUADS = list(combinations(range(N), 2))
INDEX = {e:i for i,e in enumerate(DUADS)}
EXPECTED_F = (21,210,1330,5355,9177,9632,6930,3465,1155,231,21)
EXPECTED_CHARACTER = {
    (7,):1,(6,1):0,(5,2):0,(5,1,1):0,(4,3):0,(4,2,1):0,
    (4,1,1,1):0,(3,3,1):-4,(3,2,2):2,(3,2,1,1):0,
    (3,1,1,1,1):2,(2,2,2,1):0,(2,2,1,1,1):-4,
    (2,1,1,1,1,1):0,(1,1,1,1,1,1,1):260,
}
EXPECTED_IRREPS = {
    (5,2):1,(5,1,1):1,(4,2,1):2,(4,1,1,1):1,
    (3,3,1):1,(3,2,2):1,(3,2,1,1):2,
    (3,1,1,1,1):1,(2,2,1,1,1):1,
}

def partitions(n, upper=None):
    if n == 0:
        yield ()
        return
    if upper is None: upper=n
    for p in range(min(n, upper), 0, -1):
        for q in partitions(n-p, p):
            yield (p,)+q

def generate_complex():
    facets=[]
    for j,e in enumerate(DUADS):
        facet=tuple(i for i,f in enumerate(DUADS) if i==j or set(e).isdisjoint(f))
        assert len(facet)==11
        facets.append(facet)
    assert len(set(facets))==21
    masks=set()
    for facet in facets:
        for r in range(1,len(facet)+1):
            for subset in combinations(facet,r):
                masks.add(sum(1<<i for i in subset))
    dims=Counter(face.bit_count()-1 for face in masks)
    assert tuple(dims[k] for k in range(11))==EXPECTED_F
    # An alternate characterization checks membership without relying on a chosen facet.
    for m in masks:
        assert any(all(not m>>i&1 or i==j or set(e).isdisjoint(DUADS[i])
                       for i in range(21)) for j,e in enumerate(DUADS))
    # Verify all 2^21 possible vertex sets against the defining centers,
    # independently of the subset-generation construction.
    fullfacet=[sum(1<<i for i in f) for f in facets]
    for test in range(1,1<<21):
        in_complex=any((test & f)==test for f in fullfacet)
        assert in_complex==(test in masks)
    print('FACES_OK',len(masks),'facets',len(facets),
          'exhaustive_subsets',(1<<21)-1,'f_vector',EXPECTED_F,flush=True)
    return masks

def matching(faces):
    active=set(faces);pairs=[]
    for v in range(21):
        bit=1<<v
        for lower in list(active):
            if not lower&bit and lower|bit in active:
                upper=lower|bit
                active.remove(lower);active.remove(upper)
                pairs.append((lower,upper))
    assert len(pairs)==18633
    assert Counter(f.bit_count()-1 for f in active)==Counter({0:1,3:260})
    assert 2*len(pairs)+len(active)==len(faces)
    assert len(set(a for pair in pairs for a in pair))==2*len(pairs)
    print('MATCHING_OK','pairs',len(pairs),'critical',{0:1,3:260},flush=True)
    return pairs,active

def check_acyclic(faces,pairs):
    arrows={x:[] for x in faces}
    indeg=dict.fromkeys(faces,0)
    lower_to_upper=dict(pairs)
    incidences=0
    for upper in faces:
        bits=upper
        while bits:
            bit=bits&-bits
            bits-=bit
            lower=upper^bit
            if not lower:continue
            incidences+=1
            if lower_to_upper.get(lower)==upper:
                source,target=lower,upper
            else:
                source,target=upper,lower
            arrows[source].append(target)
            indeg[target]+=1
    assert incidences==218673
    queue=deque(x for x in faces if indeg[x]==0)
    visited=0
    while queue:
        v=queue.popleft();visited+=1
        for w in arrows[v]:
            indeg[w]-=1
            if indeg[w]==0:queue.append(w)
    assert visited==len(faces)
    # Finite exact directed topological sorting, not a sampled cycle search.
    print('ACYCLIC_OK','cells',visited,'hasse_incidences',incidences,flush=True)


def check_mod2(faces):
    # Independent rank computation on the original simplicial chain complex,
    # not the Morse complex. Rows and columns use exact Python integer bitsets.
    by_dim=defaultdict(list)
    for f in faces:by_dim[f.bit_count()-1].append(f)
    expected=(0,20,190,1140,3955,5222,4410,2520,945,210,21)
    ranks=[0]
    for d in range(1,11):
        lower_idx={v:i for i,v in enumerate(by_dim[d-1])}
        pivots={};rank=0
        for f in by_dim[d]:
            x=f;b=0
            while x:
                bit=x&-x;x-=bit
                b ^= 1<<lower_idx[f^bit]
            while b:
                pivot=b.bit_length()-1
                if pivot not in pivots:
                    pivots[pivot]=b;rank+=1;break
                b ^= pivots[pivot]
        ranks.append(rank)
    assert tuple(ranks)==expected
    betti=[len(by_dim[d])-ranks[d]-(ranks[d+1] if d<10 else 0)
           for d in range(11)]
    assert betti==[1,0,0,260,0,0,0,0,0,0,0]
    print('MOD2_OK','ranks',expected,'betti3',260,flush=True)

def make_permutation(cycletype):
    perm=list(range(N));first=0
    for r in cycletype:
        for i in range(r):perm[first+i]=first+(i+1)%r
        first+=r
    assert first==N
    return [INDEX[tuple(sorted((perm[a],perm[b])))] for a,b in DUADS]

def induced_orbits(action):
    seen=set();res=[]
    for i in range(len(action)):
        if i in seen:continue
        cycle=[];j=i
        while j not in seen:
            seen.add(j);cycle.append(j);j=action[j]
        res.append(sum(1<<v for v in cycle))
    return res

def char_from_orbits(faces,action):
    orbits=induced_orbits(action)
    answer=0
    for selection in range(1<<len(orbits)):
        face=0
        for i,orbit in enumerate(orbits):
            if selection>>i&1:face |=orbit
        if face==0 or face in faces:
            answer+=(-1)**selection.bit_count()
    return answer

def char_from_signed_chains(faces,action):
    # Independent signed oriented-simplex trace; H0 is trivial and H3 is sole
    # positive-degree group, hence tr(H3)=1-L where L is the ordinary Lefschetz number.
    lef=0
    for face in faces:
        indices=[i for i in range(len(action)) if face>>i&1]
        images=[action[i] for i in indices]
        if set(indices)!=set(images):continue
        inversions=sum(a>b for i,a in enumerate(images) for b in images[i+1:])
        lef+=(-1)**(len(indices)-1+inversions)
    return 1-lef

def rim_hook(lam,nu):
    cells={(i,j) for i,row in enumerate(lam) for j in range(row)}-{
        (i,j) for i,row in enumerate(nu) for j in range(row)}
    if not cells:return None
    start=next(iter(cells));seen={start};queue=[start]
    for i,j in queue:
        for u in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
            if u in cells and u not in seen:
                seen.add(u);queue.append(u)
    if len(seen)!=len(cells):return None
    if any((i+1,j) in cells and (i,j+1) in cells and (i+1,j+1) in cells
           for i,j in cells):return None
    return len({i for i,j in cells})-1

@lru_cache(None)
def mn(lam,mu):
    if not mu:return int(not lam)
    if not lam:return 0
    r=mu[0];tot=0
    for nu in partitions(sum(lam)-r):
        if len(nu)>len(lam) or any(nu[i]>lam[i] for i in range(len(nu))):continue
        h=rim_hook(lam,nu)
        if h is not None:tot+=(-1)**h*mn(nu,mu[1:])
    return tot

def z(mu):
    return prod(k**v*factorial(v) for k,v in Counter(mu).items())

def character_check(faces):
    chars={}
    for mu in partitions(N):
        action=make_permutation(mu)
        a=char_from_orbits(faces,action)
        b=char_from_signed_chains(faces,action)
        assert a==b, (mu,a,b)
        chars[mu]=a
    assert chars==EXPECTED_CHARACTER
    assert chars[(1,)*N]==260
    assert chars[(7,)]==1
    parts=list(partitions(N))
    for la in parts:
        for lb in parts:
            inner=sum((Fraction(mn(la,mu)*mn(lb,mu),z(mu)) for mu in parts), Fraction())
            assert inner==int(la==lb),('orthogonality',la,lb,inner)
    coeff={}
    for la in parts:
        val=sum((Fraction(chars[mu]*mn(la,mu),z(mu)) for mu in parts),Fraction())
        assert val.denominator==1
        if val: coeff[la]=int(val)
    assert coeff==EXPECTED_IRREPS
    assert sum(m*mn(la,(1,)*N) for la,m in coeff.items())==260
    print('CHARACTER_OK',chars,flush=True)
    print('SPECHT_OK',coeff,'dimension',260,flush=True)

def main():
    faces=generate_complex()
    assert 1+sum((-1)**f.bit_count() for f in faces)==260
    pair,critical=matching(faces)
    check_acyclic(faces,pair)
    check_mod2(faces)
    character_check(faces)
    print('ALL_VERIFY_OK',flush=True)
if __name__=='__main__':main()
