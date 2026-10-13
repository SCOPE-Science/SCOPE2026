#!/usr/bin/env python3
"""Exact finite diagnostic for a connected one-step secondary-extinction model.

This test checks polynomial derivative signs for the first three instances.
The general arbitrarily-many-maxima statement requires the separate proof.
"""
from fractions import Fraction

def sizes(k):
    return [100**j for j in range(k)]

def qvar_polynomial(k):
    s=sizes(k); n=sum(s)
    coeff={}
    def add(deg,c): coeff[deg]=coeff.get(deg,0)+c
    for z in s:
        add(z,1); add(2*z,-1)
    add(n,1);add(2*n,-1)
    for z in s:
        add(n,2);add(n+z,-2)
    return {a:b for a,b in coeff.items() if b!=0}

def sign_at(coeff, num,den):
    d=max(coeff)
    # Exact sign of q V'(q) at q=num/den, clearing positive denominator.
    # Terms combine identically to derivative of the variance polynomial.
    T=0
    for e,c in coeff.items():
        T+=e*c*pow(num,e)*pow(den,d-e)
    return (T>0)-(T<0)

def independent_state_crosscheck(k):
    """Enumerate the independent block-extinction states, not primary states."""
    s=sizes(k)
    probs=[Fraction(2,3)**z for z in s]
    total=Fraction(0); second=Fraction(0)
    for mask in range(1<<k):
        mass=Fraction(1)
        ext=0
        for j,p in enumerate(probs):
            if (mask>>j)&1:
                mass*=p; ext+=1
            else:
                mass*=(1-p)
        if mask==(1<<k)-1:
            ext+=1
        total+=mass*ext
        second+=mass*ext*ext
    variance=second-total*total
    q=Fraction(2,3)
    calculated=sum(Fraction(c)*q**degree for degree,c in qvar_polynomial(k).items())
    assert variance==calculated,(k,variance,calculated)

def verify(k):
    independent_state_crosscheck(k)
    coeff=qvar_polynomial(k)
    s=sizes(k)
    pairs=[]
    for z in s:
        minus=sign_at(coeff,z,z+2)
        plus=sign_at(coeff,5*z,5*z+1)
        assert (minus,plus)==(1,-1),(k,z,minus,plus)
        pairs.append((minus,plus))
    return k,len(coeff),pairs

if __name__=='__main__':
    results=[verify(k) for k in (1,2,3)]
    print('VERIFY_OK '+repr(results))
