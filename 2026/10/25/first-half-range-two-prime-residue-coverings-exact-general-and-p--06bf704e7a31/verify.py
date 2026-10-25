"""Exact certificates for the first half-range two-prime residue coverings.

Uses only the Python standard library. This finite theorem does not
make an asymptotic or infinite-modulus claim.
"""
import json
from math import gcd,isqrt
from pathlib import Path

HERE=Path(__file__).resolve().parent

def is_prime(n):
    return n>=2 and all(n%d for d in range(2,isqrt(n)+1))

def primes_at_most(n):
    return [x for x in range(2,n+1) if is_prime(x)]

def units(q):
    return {a for a in range(q) if gcd(a,q)==1}

def is_prime_power(q):
    for p in range(2,q+1):
        if q%p==0 and is_prime(p):
            r=q
            while r%p==0:r//=p
            return r==1
    return False

def two_prime_image(q,bound):
    choices=[p for p in primes_at_most(bound) if gcd(p,q)==1]
    return {p*r%q for p in choices for r in choices}

def absent_by_inverses(q,bound,a):
    """Independent coverage test: no candidate p has a/p in prime residues."""
    choices=[p for p in primes_at_most(bound) if gcd(p,q)==1]
    residue_choices={p%q for p in choices}
    return all((a*pow(p,-1,q))%q not in residue_choices for p in choices)

def check():
    upper=json.loads((HERE/'coverings.json').read_text(encoding='utf-8'))
    obs=json.loads((HERE/'obstructions.json').read_text(encoding='utf-8'))
    assert set(upper)=={'96','256'}
    for q,bound in ((96,47),(256,127)):
        pairs={int(a):v for a,v in upper[str(q)].items()}
        assert set(pairs)==units(q)
        for a,pair in pairs.items():
            assert type(pair) is list and len(pair)==2
            p,r=pair
            assert all(is_prime(t) and t<=bound for t in (p,r))
            assert p*r%q==a
        assert two_prime_image(q,bound)==units(q)
    expected=set((q,q//2) for q in range(2,256)
                 if q<96 or is_prime_power(q))
    expected.update([(96,43),(256,113)])
    assert len(expected)==len(obs)==131
    assert {(z['modulus'],z['bound']) for z in obs}==expected
    for z in obs:
        q,bound,a=z['modulus'],z['bound'],z['absent_unit']
        assert 1<=a<q and gcd(a,q)==1
        assert absent_by_inverses(q,bound,a),(q,a)
        assert a not in two_prime_image(q,bound)
    assert max(primes_at_most(43))==43
    assert max(primes_at_most(126))==113
    assert 47==min(p for p in primes_at_most(47) if p>43)
    assert 127==min(p for p in primes_at_most(127) if p>113)
    print('CERTIFICATE_OK upper_units=160 obstruction_moduli=131 first_general=96 first_prime_power=256 thresholds=47,127')

if __name__=='__main__':check()
