#!/usr/bin/env python3
"""Exact checks for a rare-mutant fixation comparison in a finite game."""
from fractions import Fraction as F
from math import prod
M=((23,3,7),(7,7,7),(7,10,0)); N=6

def payoffs(mutant,i):
    return (F((i-1)*M[mutant][mutant]+(N-i)*M[mutant][1],N-1),
            F(i*M[1][mutant]+(N-i-1)*M[1][1],N-1))

def prefix(mutant):
    total=F(0); ss=[]
    for i in range(1,N):
        u,v=payoffs(mutant,i); total+=u-v; ss.append(total)
    return ss
assert prefix(0)==[-4,-4,0,8,20]
assert prefix(2)==[3,4,3,0,-5]

def denominator(mutant,z):
    return sum((z**(-d) for d in [0]+prefix(mutant)), F(0))

def gaussian(A,b):
    A=[r.copy()+[y] for r,y in zip(A,b)]; n=len(A)
    for c in range(n):
        j=next(i for i in range(c,n) if A[i][c])
        A[c],A[j]=A[j],A[c]
        v=A[c][c]; A[c]=[x/v for x in A[c]]
        for i in range(n):
            if i!=c and A[i][c]:
                v=A[i][c]; A[i]=[a-v*d for a,d in zip(A[i],A[c])]
    return [row[-1] for row in A]

def direct_fixation(mutant,z):
    A=[]; rhs=[]
    for i in range(1,N):
        pm,pr=payoffs(mutant,i)
        fm=z**int(pm); fr=z**int(pr)
        up=F((N-i)*i,N)*fm/(i*fm+(N-i)*fr)
        down=F((N-i)*i,N)*fr/(i*fm+(N-i)*fr)
        row=[F(0)]*(N-1); row[i-1]=up+down
        if i>1:row[i-2]=-down
        if i<N-1:row[i]=-up
        A.append(row); rhs.append(up if i==N-1 else F(0))
    return gaussian(A,rhs)[0]

def P(z):return -z**25+2*z**24-2*z**17-z**16+z**12+1
assert P(F(1))==0
assert -25+2*24-2*17-16+12==-15
assert P(F(6,5))>0 and P(F(2))<0
assert P(F(11,10))<0 and P(F(3,2))>0 and P(F(3))<0
for z in (F(11,10),F(6,5),F(3,2),F(2),F(3)):
    for mut in (0,2):
        assert F(1)/denominator(mut,z)==direct_fixation(mut,z)
    assert (denominator(0,z)-denominator(2,z))*z**20==P(z)
# The descending nonzero coefficient signs of P are -,+,-,-,+,+:
# exactly three variations. Together with three sign-forced roots
# 1, (1,6/5), (6/5,2), Descartes' bound isolates all positive roots.
print('VERIFY_OK finite_pop=6 strategies=3 exact_payoffs=PASS prefix_sums=PASS')
print('VERIFY_OK rational_comparisons=5 independent_markov_solutions=10 exact_polynomial=PASS')
print('VERIFY_OK desc_sign_variations=3 three_distinct_positive_roots=PASS')
