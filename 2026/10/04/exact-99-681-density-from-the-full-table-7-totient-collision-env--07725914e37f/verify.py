#!/usr/bin/env python3
from math import gcd
from fractions import Fraction
import json
from pathlib import Path

def phi(n):
    out=n
    p=2
    x=n
    while p*p<=x:
        if x%p==0:
            while x%p==0:
                x//=p
            out=out//p*(p-1)
        p += 1 if p==2 else 2
    if x>1:
        out=out//x*(x-1)
    return out

def prime_support(n):
    out=set()
    p=2
    x=n
    while p*p<=x:
        if x%p==0:
            out.add(p)
            while x%p==0:
                x//=p
        p += 1 if p==2 else 2
    if x>1:
        out.add(x)
    return out

def f1(n):
    return (n+1)*phi(n)

def main():
    data=json.loads(Path(__file__).with_name("pairs.json").read_text())
    pairs=[tuple(x) for x in data["pairs"]]
    assert len(pairs)==28
    assert len(set(pairs))==28

    supports=[]
    for a,b in pairs:
        assert a!=b
        assert f1(a)==f1(b)
        supports.append(prime_support(a*b))

    # Events "gcd(c,a*b)=1" with a support properly containing another
    # event support are redundant in the union.
    minimal=[]
    for i,S in enumerate(supports):
        if not any(T < S for j,T in enumerate(supports) if i!=j):
            minimal.append(S)
    assert len(minimal)==24

    primes=sorted(set().union(*minimal))
    assert len(primes)==36
    modulus=1
    for p in primes:
        modulus*=p
    assert modulus==data["raw_modulus"]

    # Exact residue-class dynamic program modulo the squarefree modulus.
    # A bit is set when the corresponding coprimality event has been
    # "hit" by at least one prime divisor of c, so a full mask means
    # every certificate fails.
    masks={p:0 for p in primes}
    for i,S in enumerate(minimal):
        for p in S:
            masks[p] |= 1<<i

    weights={0:1}
    for p in primes:
        pm=masks[p]
        nxt={}
        for mask,w in weights.items():
            # p does not divide c: p-1 residue classes modulo p.
            nxt[mask]=nxt.get(mask,0)+w*(p-1)
            # p divides c: one residue class modulo p.
            hit=mask|pm
            nxt[hit]=nxt.get(hit,0)+w
        weights=nxt

    full=(1<<len(minimal))-1
    uncovered=weights[full]
    certified=modulus-uncovered
    assert certified==data["certified_residue_count"]

    frac=Fraction(certified,modulus)
    assert frac.numerator==data["reduced_density_numerator"]
    assert frac.denominator==data["reduced_density_denominator"]
    assert 0.9968101176584 < float(frac) < 0.9968101176585

    # The source's stated lower bound is strictly weaker.
    assert float(frac) > 0.981728

    print("VERIFY_OK")
    print("table7_pairs=28")
    print("irredundant_supports=24")
    print("relevant_primes=36")
    print("raw_modulus="+str(modulus))
    print("certified_residue_count="+str(certified))
    print("density_fraction=%d/%d"%(frac.numerator,frac.denominator))
    print("density_decimal=%.16f"%float(frac))

if __name__=="__main__":
    main()
