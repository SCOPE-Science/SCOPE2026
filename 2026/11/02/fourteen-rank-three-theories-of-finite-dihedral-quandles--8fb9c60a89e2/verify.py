#!/usr/bin/env python3
"""Reproducible finite and symbolic checks for a rank-three relational kei classification.

Only Python's standard library is used. Mathematical universal statements rely
on the algebraic candidate/overlap lemmas explained in RESULT.md.
"""
from collections import defaultdict
from hashlib import sha256
from math import gcd
from pathlib import Path
import json

REPRESENTATIVES = (2,3,4,5,6,7,8,9,10,12,16,18,20,24)
SPECIAL = frozenset((2,3,4,5,6,8))


def atomic_flags(n, d, t):
    """The nine atomic invariants for (0,d,t), encoded in indicated order."""
    bits = (
        d % n == 0, t % n == 0, (t-d) % n == 0,
        (2*d) % n == 0, (2*t) % n == 0, (2*(t-d)) % n == 0,
        (d+t) % n == 0, (t-2*d) % n == 0, (2*t-d) % n == 0,
    )
    return sum(int(b) << i for i, b in enumerate(bits))


def direct_atomic(n, a, b, c):
    """Independent literal enumeration of all equality and ternary R atoms."""
    x = (a,b,c)
    out = 0
    bit = 0
    for i,j in ((0,1),(0,2),(1,2)):
        out |= (x[i] == x[j]) << bit
        bit += 1
    for i in range(3):
        for j in range(3):
            for k in range(3):
                out |= ((2*x[j]-x[i]-x[k]) % n == 0) << bit
                bit += 1
    return out


def roots_of_doubling(n, value):
    g = gcd(n,2)
    if value % g:
        return ()
    mod = n//g
    base = ((value//g)*pow(2//g,-1,mod)) % mod if mod>1 else 0
    return tuple((base+i*mod) % n for i in range(g))


def candidate_profile(n,d):
    """Exact profile using all exceptional witnesses and one generic witness.

    When n>=9, at most eight points are exceptional. This is an
    exhaustive symbolic method, not a sample of the witness set.
    """
    if n<9:
        return frozenset(atomic_flags(n,d,t) for t in range(n))
    exceptional = set(v % n for v in (0,d,-d,2*d))
    for value in (0,2*d,d):
        exceptional.update(roots_of_doubling(n,value))
    assert len(exceptional)<=8, (n,d,exceptional)
    generic = next(t for t in range(9) if t not in exceptional)
    return frozenset(atomic_flags(n,d,t) for t in (*exceptional,generic))


def orbit_differences(n):
    """Representatives of multiplication-by-units orbits, indexed by gcd."""
    return tuple(d for d in range(n) if d==0 or d==gcd(d,n))


def direct_flag_signature(n):
    return frozenset(candidate_profile(n,d) for d in orbit_differences(n))


def parameter_key(n,d):
    order = n//gcd(n,d)
    has_half = n%2==1 or d%2==0
    return (n%2==0, min(5,order), has_half)


# All possible keys for n>=9 and one genuine realized example for each.
KEY_WITNESSES = {
    (False,1,True):(9,0),
    (False,3,True):(9,3),
    (False,5,True):(11,1),
    (True,1,True):(10,0),
    (True,2,False):(10,5),
    (True,2,True):(12,6),
    (True,3,True):(12,4),
    (True,4,False):(12,3),
    (True,4,True):(16,4),
    (True,5,False):(10,1),
    (True,5,True):(10,2),
}
KEY_PROFILES = {key:candidate_profile(*sample)
                for key,sample in KEY_WITNESSES.items()}
assert all(parameter_key(*sample)==key for key,sample in KEY_WITNESSES.items())


def universal_signature(n):
    """The formula established for n>=9, using only divisibility data."""
    if n<9:
        return direct_flag_signature(n)
    if n%2:
        keys = [(False,1,True),(False,5,True)]
        if n%3==0:
            keys.append((False,3,True))
    else:
        keys = [(True,1,True),(True,5,False),(True,5,True)]
        keys.append((True,2,True if n%4==0 else False))
        if n%3==0:
            keys.append((True,3,True))
        if n%4==0:
            keys.append((True,4,True if n%8==0 else False))
    return frozenset(KEY_PROFILES[k] for k in keys)


def digest(sig):
    ordered = tuple(sorted(tuple(sorted(p)) for p in sig))
    return sha256(repr(ordered).encode('ascii')).hexdigest()[:16]


def literal_recursive_signature(n, atom_map, reverse_map):
    """Actual full three-move Hintikka-type recursion, no orbit shortcuts.

    The flag/atom dictionaries are independently populated from full tables,
    so the compressed and full encodings must be mutually injective.
    """
    all_first = set()
    for x in range(n):
        possible_second = set()
        for y in range(n):
            possible_third = set()
            for z in range(n):
                a = direct_atomic(n,x,y,z)
                f = atomic_flags(n,(y-x)%n,(z-x)%n)
                assert atom_map.setdefault(f,a)==a
                assert reverse_map.setdefault(a,f)==f
                possible_third.add(a)
            possible_second.add(frozenset(possible_third))
        all_first.add(frozenset(possible_second))
    assert len(all_first)==1, 'Expected transitivity by translations'
    (first_type,) = all_first
    return frozenset(frozenset(reverse_map[a] for a in prof)
                     for prof in first_type)


def main():
    print('RANK_THREE_DIHEDRAL_QUANDLES_BEGIN')
    atom_map,reverse_map={},{}
    for n in REPRESENTATIVES:
        from_literal=literal_recursive_signature(n,atom_map,reverse_map)
        from_candidates=direct_flag_signature(n)
        assert from_literal==from_candidates, (n,'independent implementations disagree')
        print(f'EXACT_EF_REP n={n} pair_profiles={len(from_literal)} ' +
              f'fingerprint={digest(from_literal)}')
    print('LITERAL_ATOM_TO_NINE_FLAG_BIJECTION_OK',len(atom_map),'triple_types')
    sigs={n:universal_signature(n) for n in REPRESENTATIVES}
    assert len(set(sigs.values()))==len(REPRESENTATIVES)
    print('FOURTEEN_PAIRWISE_DISTINCT_RANK_THREE_CLASSES_OK')
    certificate=json.loads((Path(__file__).parent/'type_certificate.json').read_text(encoding='utf-8'))
    all_profiles=sorted({p for sig in sigs.values() for p in sig},key=lambda p:tuple(sorted(p)))
    labels={p:f'P{i+1}' for i,p in enumerate(all_profiles)}
    assert certificate['pair_profile_labels']=={labels[p]:sorted(p) for p in all_profiles}
    assert certificate['rank_three_class_representatives']=={
        str(n):sorted((labels[p] for p in sigs[n]),key=lambda x:int(x[1:]))
        for n in REPRESENTATIVES}
    assert certificate['universal_key_examples']==[
        {'key':[int(k[0]),k[1],int(k[2])],
         'example_modulus':v[0], 'example_difference':v[1],
         'pair_profile_label':labels[KEY_PROFILES[k]]}
        for k,v in sorted(KEY_WITNESSES.items())]
    print('REPRODUCIBLE_NINETEEN_PROFILE_CERTIFICATE_OK')
    assert max(REPRESENTATIVES)==24
    # Extensive consistency checks; no checked finite range is claimed to
    # replace the universal overlap lemma in RESULT.md.
    groups=defaultdict(set)
    for n in range(9,501):
        for d in orbit_differences(n):
            key=parameter_key(n,d)
            got=candidate_profile(n,d)
            assert got==KEY_PROFILES[key],(n,d,key)
            groups[key].add(n)
        assert direct_flag_signature(n)==universal_signature(n),n
        rep=next(k for k in REPRESENTATIVES if k not in SPECIAL
                 and gcd(n,24)==gcd(k,24))
        assert universal_signature(n)==universal_signature(rep)
    assert set(groups)==set(KEY_WITNESSES)
    print('ELEVEN_SYMBOLIC_PAIR_KEYS_OK tested_moduli=9..500')
    print('EIGHT_GCD24_STABLE_CLASSES_OK tested_moduli=9..500')
    assert len({universal_signature(n) for n in range(2,501)})==14
    print('EXACT_CLASSES_OK n_ge_2=14 stable_gcd_modulus=24 ' +
          'exceptions=2,3,4,5,6,8 smallest_representative_bound=24')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
