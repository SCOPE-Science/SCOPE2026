#!/usr/bin/env python3
from itertools import permutations
from fractions import Fraction

def energy(tau):
    x=(0,)+tuple(tau)+(0,)
    return sum((x[i+1]-x[i])**2 for i in range(len(x)-1))

def formula_mean_E(d):
    return Fraction((d+1)**2*(d+2),6)

def formula_var_E(d):
    return Fraction((d-2)*(d+1)**2*(d+2)*(5*d+11),180)

checks=0
for d in range(2,9):
    vals=[energy(t) for t in permutations(range(1,d+1))]
    mean=Fraction(sum(vals),len(vals))
    var=Fraction(sum((Fraction(v)-mean)**2 for v in vals),len(vals))
    assert mean==formula_mean_E(d),(d,mean,formula_mean_E(d))
    assert var==formula_var_E(d),(d,var,formula_var_E(d))
    assert (var==0)==(d==2)

    # Check the centered-radius identity for representative positive rational M,N.
    M=Fraction(7,2)
    N=Fraction(3,5)
    baseline=Fraction(M*M*d*(d+1)*(d+2),12)+M*N*d*(d+1)
    mu=M*Fraction(d+2,2)
    for tau in permutations(range(1,d+1)):
        coeff=[]
        ext=(0,)+tau+(0,)
        for i in range(1,d+2):
            coeff.append(M*i+N*(ext[i-1]-ext[i]))
        direct=sum((x-mu)**2 for x in coeff)
        predicted=baseline+N*N*energy(tau)
        assert direct==predicted
        checks+=1

print(f"VERIFY_OK nested-permutohedron-radial-moments permutations={checks} d=2..8 exact=yes")
