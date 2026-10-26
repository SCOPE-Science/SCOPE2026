#!/usr/bin/env python3
"""Independent rank-three type and Ehrenfeucht–Fraisse checks for cyclic tripartite digraphs.
Reproducible with CPython 3.10+: python cyclic_tripartite_verify.py
"""
from itertools import product,combinations
from collections import defaultdict
from functools import lru_cache

CAP=3
TRIPLES=list(product(range(1,CAP+1),repeat=3))

def vertices(sizes):
    return tuple((part,index) for part,size in enumerate(sizes) for index in range(size))

def edge(x,y):
    return x[0]!=y[0] and (y[0]-x[0])%3==1

def diagram(t):
    return tuple((int(a==b),int(edge(a,b)),int(edge(b,a)))
                 for i,a in enumerate(t) for b in t[i:])

# Exact first-order Hintikka characters for the entire finite vertex set.
# Atomic part includes complete directed edge information and equalities.
@lru_cache(None)
def character(sizes,tup,remaining):
    if remaining==0:
        return ('atom', diagram(tup))
    return (diagram(tup), frozenset(character(sizes,tup+(v,),remaining-1)
                                  for v in vertices(sizes)))

def exact_type_groups(rank):
    d=defaultdict(list)
    for sizes in TRIPLES:
        d[character(sizes,(),rank)].append(sizes)
    return list(d.values())

# Independently coded direct two-structure game, with one fresh representative
# from each clone class; this is complete by within-class permutation symmetry.
def representative_moves(sizes,played):
    used=set(played)
    candidates=list(dict.fromkeys(played))
    for part,num in enumerate(sizes):
        for j in range(num):
            if (part,j) not in used:
                candidates.append((part,j))
                break
    return candidates

def duplicator_wins(A,B,rank):
    @lru_cache(None)
    def win(xs,ys,left):
        if diagram(xs)!=diagram(ys):
            return False
        if left==0:
            return True
        X=representative_moves(A,xs)
        Y=representative_moves(B,ys)
        # The challenger may choose the structure on each round.
        for x in X:
            if not any(win(xs+(x,),ys+(y,),left-1) for y in Y):
                return False
        for y in Y:
            if not any(win(xs+(x,),ys+(y,),left-1) for x in X):
                return False
        return True
    return win((),(),rank)

def normalize_group(groups):
    return sorted((tuple(sorted(g)) for g in groups),key=lambda g:(len(g),g))

def cyclic_representative(t):
    return min((t,t[1:]+t[:1],t[2:]+t[:2]))

def main():
    groups={r:exact_type_groups(r) for r in (1,2,3)}
    for r in (1,2,3):
        print('HINTIKKA_RANK_OK',r,'classes',len(groups[r]))
    assert [len(groups[r]) for r in (1,2,3)]==[1,3,10]
    pointed_to_code={}
    code_to_pointed={}
    for sizes in TRIPLES:
        for i in range(3):
            rooted=character(sizes,((i,0),),2)
            code=(min(sizes[i],3),min(sizes[(i+1)%3],2),min(sizes[(i+2)%3],2))
            if rooted in pointed_to_code:
                assert pointed_to_code[rooted]==code
            if code in code_to_pointed:
                assert code_to_pointed[code]==rooted
            pointed_to_code[rooted]=code
            code_to_pointed[code]=rooted
    assert len(pointed_to_code)==len(code_to_pointed)==12
    print('POINTED_TWO_ROUND_CODE_OK','types',len(pointed_to_code))
    for A in TRIPLES:
        code_set={ (min(A[i],3),min(A[(i+1)%3],2),min(A[(i+2)%3],2)) for i in range(3)}
        for B in TRIPLES:
            other={ (min(B[i],3),min(B[(i+1)%3],2),min(B[(i+2)%3],2)) for i in range(3)}
            assert (code_set==other)==(character(A,(),3)==character(B,(),3))
    print('UNPOINTED_CODE_EQUIVALENCE_OK','ordered_pairs',len(TRIPLES)**2)
    expected=[
      {(1,1,1)},
      {(1,1,2)},
      {(1,1,3)},
      {(1,2,2)},
      {(1,2,3)},
      {(1,3,2)},
      {(1,3,3)},
      {(2,2,2)},
      {(2,2,3),(2,3,3)},
      {(3,3,3)},
    ]
    seen=[]
    for group in groups[3]:
        seen.append({cyclic_representative(t) for t in group})
    assert sorted(map(sorted,seen))==sorted(map(sorted,expected))
    print('TEN_CLASS_TABLE_OK',len(seen))
    for r in (2,3):
        sigmap={t:i for i,g in enumerate(groups[r]) for t in g}
        for i,A in enumerate(TRIPLES):
            for B in TRIPLES[i:]:
                pred=duplicator_wins(A,B,r)
                assert pred==(sigmap[A]==sigmap[B]),(r,A,B,pred)
        print('INDEPENDENT_GAME_AGREEMENT_OK','rank',r,'pairs',len(TRIPLES)*(len(TRIPLES)+1)//2)
    for r in (1,2,3):
        for sizes in TRIPLES:
            bigger=tuple(n+3 if n==3 else n for n in sizes)
            assert duplicator_wins(sizes,bigger,r),(r,sizes,bigger)
    print('BOUNDARY_TRUNCATION_CHECK_OK',len(TRIPLES),'rank=1..3')
    maxima=[min(sum(t) for t in group) for group in groups[3]]
    assert max(maxima)==9
    assert sum(1 for m in maxima if m==9)==1
    print('SHARP_REPRESENTATIVE_OK','max_vertices',max(maxima))
    assert duplicator_wins((2,2,3),(2,3,3),3)
    assert not duplicator_wins((2,2,3),(2,3,3),4)
    print('EXCEPTIONAL_MERGER_BOUNDARY_OK','rank3_equal','rank4_distinct')
    print('VERIFY_OK')
if __name__=='__main__':main()
