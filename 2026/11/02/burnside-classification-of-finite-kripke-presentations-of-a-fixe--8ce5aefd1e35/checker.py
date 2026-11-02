"""Independent finite orbit and modal-truth checks for type-restricted relations.

Run: python3 checker.py. Standard library only.
"""
from itertools import permutations, product
from math import factorial, gcd
from collections import Counter


def partition_tuples(n):
    if n == 0:
        yield ()
    else:
        for first in range(n, 0, -1):
            for rest in partition_tuples(n-first):
                if not rest or first >= rest[0]:
                    yield (first,)+rest


def centralizer(parts):
    c=Counter(parts)
    z=1
    for d,m in c.items():
        z *= d**m*factorial(m)
    return z


def symbolic_count(sizes, targets):
    """Independent cycle-partition Burnside sum as an exact rational number."""
    from fractions import Fraction
    ans=Fraction(0)
    for lambdas in product(*(list(partition_tuples(s)) for s in sizes)):
        w=Fraction(1)
        for parts in lambdas:
            w /= centralizer(parts)
        fixed=1
        for i,parts in enumerate(lambdas):
            for length in parts:
                for j in targets[i]:
                    cycles=sum(gcd(length,b) for b in lambdas[j])
                    fixed *= 2**cycles-1
        ans += w*fixed
    assert ans.denominator == 1
    return int(ans)


def class_rows(sizes, targets):
    n=sum(sizes)
    ranges=[]
    k=0
    for s in sizes:
        ranges.append(tuple(range(k,k+s)))
        k+=s
    allowed=[]
    for i,worlds in enumerate(ranges):
        choices=[]
        for t in range(1<<n):
            if all(((t>>v)&1) == 0 for j,rg in enumerate(ranges) if j not in targets[i] for v in rg) and all(any((t>>v)&1 for v in ranges[j]) for j in targets[i]):
                choices.append(t)
        allowed.extend([choices]*len(worlds))
    return ranges,allowed


def transform_relation(rows,pi):
    n=len(rows)
    out=[0]*n
    for i in range(n):
        out[pi[i]]=sum(1<<pi[j] for j in range(n) if rows[i]>>j&1)
    return tuple(out)


def direct_orbit_count(sizes,targets):
    ranges,choices=class_rows(sizes,targets)
    perms=[]
    for blockperms in product(*(list(permutations(rg)) for rg in ranges)):
        pi=list(range(sum(sizes)))
        for rg,img in zip(ranges,blockperms):
            for x,y in zip(rg,img):pi[x]=y
        perms.append(pi)
    seen=set()
    raw=0
    for rows in product(*choices):
        raw+=1
        if rows in seen: continue
        for pi in perms:
            seen.add(transform_relation(rows,pi))
    return raw,len(seen),sum(1 for rows in product(*choices) if rows==min(transform_relation(rows,pi) for pi in perms))


def formula_theory_agrees(n,original_rows,candidate_rows,atomic_masks):
    """Exact saturation of paired formula truth sets (no depth truncation)."""
    all_bits=(1<<n)-1
    def box(mask,rows):
        return sum(1<<i for i,t in enumerate(rows) if not(t & (all_bits^mask)))
    pairs={(0,0),(all_bits,all_bits)}|{(p,p) for p in atomic_masks}
    while True:
        new=set(pairs)
        new.update((all_bits^a,all_bits^b) for a,b in pairs)
        new.update((box(a,original_rows),box(b,candidate_rows)) for a,b in pairs)
        new.update((a&c,b&d) for a,b in pairs for c,d in pairs)
        if new==pairs:break
        pairs=new
    return all(a==b for a,b in pairs)


def check():
    cases=[((3,),((0,),),((0,),),343,70),
           ((4,),((0,),),((0,),),50625,2340),
           ((2,1),((0,1),(0,1)),((0,1),(0,1)),27,15),
           ((2,2),((0,1),(0,1)),((0,1),(0,1)),6561,1701)]
    for sizes,targets,_,raw_expected,orbit_expected in cases:
        raw,_,orbits=direct_orbit_count(sizes,targets)
        assert raw==raw_expected,(sizes,raw)
        symbolic=symbolic_count(sizes,targets)
        assert symbolic==orbit_expected==orbits,(sizes,symbolic,orbits)
        print('CASE',sizes,'labelled',raw,'orbits',orbits)
    # Direct semantic check of every binary relation on 3 worlds.
    all3=7
    for p_masks,expected in [((),343),((3,),27),((1,2),1)]:
        universal=(all3,all3,all3)
        actual=0
        for rows in product(range(8),repeat=3):
            actual+=formula_theory_agrees(3,universal,rows,p_masks)
        assert actual==expected,(p_masks,actual)
    print('ALL_CHECKS_OK')

if __name__=='__main__':check()
