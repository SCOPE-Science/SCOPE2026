"""Bright-algebra step (exact, replayable): singular locus of the three quadrics
Q_{jk}: y_j*y_k - y_i*y_l relations + coefficient ratio constraints for
D: x0^4 + (7/2)x1^4 + 4x2^4 - (17/2)x3^4 = 0.
Classical criterion (Bright thesis / paper Alg 1): Br1/Br0 rogues from triples
(e_ijk) with product condition on ratios a_i*a_j/(a_k*a_l) being a square.
Here report: all six ratios, squarefree parts, in {±1,±2,±7,±17,±14,±34,...}."""
from fractions import Fraction
import math
def sqfree_part(fr):
    # squarefree part of a rational (up to squares): numerator*denominator squarefree kernel
    n, d = fr.numerator, fr.denominator
    m = abs(n*d)
    # reduce: for each prime p with p^2|m divide out
    p=2
    out=1
    mm=m
    while p*p<=mm:
        e=0
        while mm%p==0:
            mm//=p; e+=1
        if e%2==1: out*=p
        p+=1 if p==2 else 2
    if mm>1: out*=mm
    return out if fr>0 else -out
a=[Fraction(1),Fraction(7,2),Fraction(4),Fraction(-17,2)]
names=['a0','a1','a2','a3']
for i in range(4):
    for j in range(i+1,4):
        k,l=[x for x in range(4) if x not in (i,j)]
        r=a[i]*a[j]/(a[k]*a[l])
        print(f"({names[i]}*{names[j]})/({names[k]}*{names[l]}) = {r}  sqfree={sqfree_part(r)}  square={sqfree_part(r)==1}")
