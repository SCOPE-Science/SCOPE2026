"""Finite exact checks of equational spectra for Takasaki core groupoids.

Represent finite abelian groups as tuples of cyclic coordinate moduli.  This
checks two-variable generated term coefficients, their exact equalizer sizes,
and the reconstructed elementary divisors. The infinite theorem uses its proof.
"""
from math import gcd,lcm,prod
from fractions import Fraction
from itertools import product
from collections import Counter


def items(moduli):
    return list(product(*(range(d) for d in moduli)))


def operation(a,b,moduli):
    return tuple((2*y-x) % m for x,y,m in zip(a,b,moduli))


def torsion_count(moduli,d):
    return prod(gcd(m,d) for m in moduli)


def spectrum(moduli):
    exp=lcm(*moduli)
    size=prod(moduli)
    return {Fraction(torsion_count(moduli,d),size) for d in range(exp+1)}


def check(moduli):
    A=items(moduli); N=len(A); exp=lcm(*moduli)
    # The generated two-variable term functions are exactly coefficient classes
    # a*x+(1-a)*y mod exp.  Generate term syntax with 2b-a closure.
    generated={0,1}; changed=True
    while changed:
        seen=generated | {(2*b-a)%exp for a in generated for b in generated}
        changed=len(seen)>len(generated); generated=seen
    assert generated == set(range(exp)),(moduli,generated)
    # Direct evaluation of all pairs of generated two-variable term functions.
    observed=set()
    for a in generated:
        for b in generated:
            solutions=0
            for x in A:
                for y in A:
                    tx=tuple((a*xx+(1-a)*yy)%m for xx,yy,m in zip(x,y,moduli))
                    ty=tuple((b*xx+(1-b)*yy)%m for xx,yy,m in zip(x,y,moduli))
                    solutions += tx==ty
            prob=Fraction(solutions,N*N)
            assert prob==Fraction(torsion_count(moduli,a-b),N),(moduli,a,b,prob)
            observed.add(prob)
    assert observed==spectrum(moduli),(moduli,observed,spectrum(moduli))
    # Reconstruct p-primary cyclic block multiplicities from the unordered set.
    nums={N*z for z in observed}
    assert all(int(z)==z for z in nums)
    wanted=Counter()
    for m in moduli:
        f=m;p=2
        while p*p<=f:
            if f%p==0:
                j=0
                while f%p==0: f//=p;j+=1
                wanted[(p,j)]+=1
            p+=1
        if f>1: wanted[(f,1)]+=1
    got=Counter()
    primes={p for p,j in wanted}
    for p in primes:
        exps=sorted({0}|{k for k in range(1,20) if p**k in nums})
        # Only all torsion cardinalities up to full p-primary order appear.
        ranks=[exps[i]-exps[i-1] for i in range(1,len(exps))]+[0]
        for i,r in enumerate(ranks[:-1]):
            amount=r-ranks[i+1]
            if amount:got[(p,i+1)]+=amount
    assert wanted==got,(moduli,wanted,got)
    return N,len(observed),exp

if __name__=='__main__':
    choices=[(2,),(3,),(4,),(6,),(8,),(9,),(2,2),(2,3),(2,4),(2,2,2),(3,3),(2,2,3),(3,4),(2,2,4),(4,4)]
    for group in choices:
        result=check(group)
        print('PASS',group,'order-spectrum-exponent',result)
    print('VERIFY_OK',len(choices))
