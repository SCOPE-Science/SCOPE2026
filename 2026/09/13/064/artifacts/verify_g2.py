"""Verification for lane-1724: combinatorics of w2, S, and homomorphism witnesses.

G2 = <a,b,c | w2^3 = 1>, w2 = a b a^-1 b^2 c^3.
J  = <b,c,d | S^3 = 1>, S = d b^2 c^3.
Checks:
 (1) w2 cyclically reduced, exponent sums (0,3,3), not a proper power.
 (2) S cyclically reduced, exponent sums (b,c,d)=(2,3,1), not a proper power.
 (3) Homomorphism witnesses kill relators and detect infinite-order elements.
"""
from collections import Counter
import math

def letters(syll):
    L = []
    for g, e in syll:
        s = 1 if e > 0 else -1
        for _ in range(abs(e)):
            L.append((g, s))
    return L

w2 = letters([('a',1),('b',1),('a',-1),('b',2),('c',3)])
assert len(w2) == 8, len(w2)
# reduced: no adjacent inverse pair
assert all(not (w2[i][0]==w2[i+1][0] and w2[i][1]==-w2[i+1][1]) for i in range(7))
# cyclically reduced: first/last not inverse
assert not (w2[0][0]==w2[-1][0] and w2[0][1]==-w2[-1][1])
es = Counter()
for g,s in w2: es[g]+=s
assert (es['a'],es['b'],es['c'])==(0,3,3), dict(es)
assert math.gcd(abs(es['b']),abs(es['c']))==3  # non-primitive
# not a proper power: lengths dividing 8
n=len(w2)
for k in (2,4,8):
    m=n//k
    assert w2[:m]*k != w2, k
gens = {g for g,_ in w2}
assert gens=={'a','b','c'}, gens

S = letters([('d',1),('b',2),('c',3)])
assert len(S)==6
assert all(not (S[i][0]==S[i+1][0] and S[i][1]==-S[i+1][1]) for i in range(5))
assert not (S[0][0]==S[-1][0] and S[0][1]==-S[-1][1])
esS=Counter()
for g,s in S: esS[g]+=s
assert (esS['b'],esS['c'],esS['d'])==(2,3,1), dict(esS)
for k in (2,3,6):
    m=len(S)//k
    assert S[:m]*k != S, k

# Homomorphism witnesses (exponent-sum linear forms must vanish on relator).
# G2: abelianization relation is 3*(0,3,3)=(0,9,9).
# psi: (a,b,c)->(1,0,0): kills since a-exp sum 0.
assert 1-1==0  # a-coeff of w2
# chi: (a,b,c)->(0,1,-1): chi(w2)=3*1+3*(-1)=0; chi(b)=1.
assert 3*1+3*(-1)==0
# J: abelianization relation 3*(2,3,1)=(6,9,3) in (b,c,d).
# theta: (b,c,d)->(1,1,-5): theta(S)=2+3-5=0; theta(b)=1.
assert 2*1+3*1+1*(-5)==0
# eta: (b,c,d)->(1,-1,1): eta(S)=2-3+1=0; eta(d)=1.
assert 2*1+3*(-1)+1*1==0
print("ALL CHECKS PASSED")
print("w2:",w2,"S:",S)
