#!/usr/bin/env python3
from itertools import combinations


def subsets(mask):
    s=mask
    while True:
        yield s
        if s==0: break
        s=(s-1)&mask

def valid_complex(n, fam):
    # faces are bitmasks 0..2^n-1; require empty face and every singleton,
    # and downward closure. Thus the declared vertex set is exactly [n].
    if not (fam & 1): return False
    for v in range(n):
        if not (fam >> (1<<v)) & 1: return False
    for f in range(1<<n):
        if (fam>>f)&1:
            for g in subsets(f):
                if not ((fam>>g)&1): return False
    return True

def face(fam, s): return ((fam>>s)&1) != 0

def in_star(fam, sigma, v):
    return face(fam, sigma | (1<<v))

def total_domination_number(n, fam):
    full=(1<<n)-1
    for k in range(n+1):
        for S_tuple in combinations(range(n), k):
            S=sum(1<<v for v in S_tuple)
            ok=True
            for v in range(n):
                witness=False
                for sigma in subsets(S):
                    if face(fam,sigma) and not face(fam,sigma | (1<<v)):
                        witness=True; break
                if not witness:
                    ok=False; break
            if ok:
                return k
    return None  # infinity

def all_subcomplexes_on_S(n, fam, S):
    # Enumerate downward-closed subfamilies of X|S. Empty subcomplex is allowed.
    faces=[f for f in range(1<<n) if (f & ~S)==0 and face(fam,f)]
    m=len(faces)
    idx={f:i for i,f in enumerate(faces)}
    # Brute force is tiny for n<=4. Empty face in a nonempty subcomplex follows closure.
    for lm in range(1<<m):
        ok=True
        used_vertices=0
        for i,f in enumerate(faces):
            if (lm>>i)&1:
                used_vertices |= f
                for g in subsets(f):
                    j=idx.get(g)
                    if j is None or not ((lm>>j)&1):
                        ok=False; break
                if not ok: break
        if ok:
            yield lm, faces, used_vertices

def is_r_conic_bruteforce(n, fam, r):
    full=(1<<n)-1
    # Enumerate possible ambient vertex subsets S and every subcomplex supported on S.
    # The actual vertex set of L is read from its faces, so duplicates do not affect truth.
    for S in subsets(full):
        if S.bit_count()>r: continue
        for lm, faces, used in all_subcomplexes_on_S(n,fam,S):
            if used.bit_count()>r: continue
            contained=False
            for v in range(n):
                if all(not ((lm>>i)&1) or in_star(fam,f,v) for i,f in enumerate(faces)):
                    contained=True; break
            if not contained:
                return False
    return True

def conicity_index(n, fam):
    # finite non-cones fail by r=n; cone => infinity.
    for r in range(0,n+1):
        if not is_r_conic_bruteforce(n,fam,r):
            return r-1
    return None

def join_complex(n1,f1,n2,f2):
    n=n1+n2
    fam=0
    for a in range(1<<n1):
        if not face(f1,a): continue
        for b in range(1<<n2):
            if face(f2,b):
                fam |= 1 << (a | (b<<n1))
    return n,fam

def join_s0_complex(k):
    # k copies of S^0 on pairs (2i,2i+1): a face selects at most one vertex per pair.
    n=2*k
    fam=0
    for s in range(1<<n):
        if all(not ((s>>(2*i))&1 and (s>>(2*i+1))&1) for i in range(k)):
            fam |= 1<<s
    return n,fam

def main():
    totals={}
    for n in range(1,5):
        checked=0
        maxfam=1<<(1<<n)
        for fam in range(maxfam):
            if not valid_complex(n,fam): continue
            checked += 1
            gamma=total_domination_number(n,fam)
            ci=conicity_index(n,fam)
            if gamma is None:
                assert ci is None, (n,fam,gamma,ci)
            else:
                assert ci == gamma-1, (n,fam,gamma,ci)
                for r in range(0,n+1):
                    assert is_r_conic_bruteforce(n,fam,r) == (gamma>r)
        totals[n]=checked
    print('LABELED_COMPLEXES_CHECKED', totals)
    # Independent finite check of additivity of total domination under joins.
    small={}
    for n in range(1,4):
        small[n]=[fam for fam in range(1<<(1<<n)) if valid_complex(n,fam)]
    join_pairs=0
    for n1 in range(1,4):
        for n2 in range(1,4):
            for f1 in small[n1]:
                for f2 in small[n2]:
                    g1=total_domination_number(n1,f1)
                    g2=total_domination_number(n2,f2)
                    n,j=join_complex(n1,f1,n2,f2)
                    gj=total_domination_number(n,j)
                    if g1 is None or g2 is None:
                        assert gj is None
                    else:
                        assert gj==g1+g2,(n1,n2,g1,g2,gj)
                    join_pairs+=1
    print('JOIN_PAIRS_CHECKED',join_pairs)
    for k in range(1,5):
        n,fam=join_s0_complex(k)
        gamma=total_domination_number(n,fam)
        # for k=4 n=8; avoid brute-force subcomplex enumeration, verify gamma directly and
        # use theorem's two logical directions as encoded above on smaller examples.
        assert gamma==2*k
        print(f'JOIN_{k}_S0_TOTAL_DOMINATION={gamma} EXPECTED_CONICITY={gamma-1}')
    print('EXHAUSTIVE_EQUIVALENCE_OK')

if __name__=='__main__': main()
