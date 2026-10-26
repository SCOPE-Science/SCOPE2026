"""Direct exact counting for joint squareful local factors."""
from fractions import Fraction
from itertools import combinations_with_replacement
import random

def model(p, slopes):
    residues={pow(x,2,p) for x in range(1,p)}
    buckets={}
    for t in slopes:
        t%=p*p
        assert t%p and t%p in residues
        buckets.setdefault(t%p,set()).add(t)
    s=len(buckets)
    t=sum(len(vals)==1 for vals in buckets.values())
    return Fraction(1)-Fraction(2,p+1)*(s-Fraction(t,p))

def direct(p,slopes):
    modulus=p*p; total=good=0
    for x in range(modulus):
        for y in range(modulus):
            if x%p==0 and y%p==0:continue
            total+=1
            if all((x*x-z*y*y)%p !=0 or (x*x-z*y*y)%modulus==0 for z in slopes):good+=1
    assert total==modulus*modulus-p*p
    return Fraction(good,total)

def minformula(p,k):
    m=min(k,(p-1)//2)
    return Fraction(1)-Fraction(2,p+1)*(m-Fraction(max(0,2*m-k),p))

rng=random.Random(20261020)
checks=0
for p in (3,5,7,11):
    residues=sorted({pow(x,2,p) for x in range(1,p)})
    choices=[r+p*z for r in residues for z in range(p)]
    for k in range(1,8):
        for sample in range(22 if p<=7 else 9):
            slopes=[rng.choice(choices) for _ in range(k)]
            a=direct(p,slopes);b=model(p,slopes)
            assert a==b,(p,k,slopes,a,b)
            assert a>=minformula(p,k),(p,k,a,minformula(p,k))
            checks+=1
        m=min(k,(p-1)//2)
        slopes=residues[:m]
        for i in range(min(m,k-m)):
            slopes.append(residues[i]+p)
        while len(slopes)<k:slopes.append(residues[0])
        assert len(slopes)==k
        assert model(p,slopes)==minformula(p,k),(p,k,slopes)
        assert direct(p,slopes)==minformula(p,k),(p,k,slopes)
        checks+=1
print('CERTIFICATE_OK primitive_pair_counts',checks,'primes',4,'k',range(1,8))
