"""Exact six-year paired-stage intervention checks.

Run: python verify.py (requires SymPy 1.12 or later).
No external datasets or internet connections are used.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
import sympy as sp

x, y, z, w, u, v = sp.symbols('a b c d u v', positive=True)
L = sp.Matrix([[x, y], [z, w]])
P = L * sp.diag(u, 1)
Q = L * sp.diag(1, v)

def matrix_of_word(word, a=P, b=Q):
    out = sp.eye(2)
    for letter in word:
        out *= (a if letter == 'J' else b)
    return out

words = {''.join('J' if i in idx else 'A' for i in range(6))
         for idx in combinations(range(6), 3)}
assert len(words) == 20
orbits = {}
unseen = set(words)
while unseen:
    key = min(unseen)
    orbit = {key[i:] + key[:i] for i in range(6)}
    assert orbit <= words
    orbits[key] = orbit
    unseen -= orbit
assert sorted((key, len(value)) for key, value in orbits.items()) == [
    ('AAAJJJ', 6), ('AAJAJJ', 6), ('AAJJAJ', 6), ('AJAJAJ', 2)]
# The four representatives above reverse the usual J/A choice; the proof is letter symmetric.
# Work with four conventional J-first representatives, each of which is cyclically equivalent.
block, mix1, mix2, alternating = 'JJJAAA', 'JJAJAA', 'JJAAJA', 'JAJAJA'
rep = [block, mix1, mix2, alternating]
assert len(set(rep)) == 4
assert {frozenset(w[i:] + w[:i] for i in range(6)) for w in rep} == set(map(frozenset,orbits.values()))
T = [sp.expand(sp.trace(matrix_of_word(wd))) for wd in rep]
D = [sp.factor(matrix_of_word(wd).det()) for wd in rep]
assert len(set(D)) == 1
assert sp.factor(D[0] - (x*w-y*z)**6*(u*v)**3) == 0
assert sp.factor(T[1]-T[2]) == 0
factor1 = -y*z*(x*w-y*z)*(w+x*u)*(x+w*v)*(1-u*v)**2
factor2 = -y*z*(x*w-y*z)*(y*z*(1+u*v)+x*x*u+w*w*v)*(1-u*v)**2
assert sp.factor(T[1]-T[0]-factor1) == 0
assert sp.factor(T[3]-T[1]-factor2) == 0
# Symbolically rule out any other trace class: all 20 balanced words map to representatives.
rep_orbit = {wd[i:]+wd[:i]:j for j,wd in enumerate(rep) for i in range(6)}
assert len(rep_orbit)==20
for wd in words:
    assert sp.factor(sp.trace(matrix_of_word(wd))-T[rep_orbit[wd]])==0

# Exact-rational, direct-multiplication tests, with a second independent implementation.
def matmul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def matrices(a,b,c,d,hj,ha):
    Lj=((a,b),(c,d))
    D1=((hj,Fraction(0)),(Fraction(0),Fraction(1)))
    D2=((Fraction(1),Fraction(0)),(Fraction(0),ha))
    return matmul(Lj,D1), matmul(Lj,D2)
def trace_product(word,A,B):
    M=((Fraction(1),Fraction(0)),(Fraction(0),Fraction(1)))
    for q in word:
        M=matmul(M,A if q=='J' else B)
    return M[0][0]+M[1][1], M[0][0]*M[1][1]-M[0][1]*M[1][0]

cases=0
fracs=[Fraction(1,5),Fraction(1,2),Fraction(2,3),Fraction(3,4)]
for a,d in product(fracs,repeat=2):
    for b,c in product([Fraction(1,3),Fraction(1),Fraction(2)], [Fraction(1,4),Fraction(1,2)]):
        for hj,ha in [(Fraction(1,2), Fraction(2,3)), (Fraction(3,4),Fraction(2,3))]:
            A,B=matrices(a,b,c,d,hj,ha)
            traces=[trace_product(wd,A,B)[0] for wd in rep]
            dets={trace_product(wd,A,B)[1] for wd in words}
            assert len(dets)==1
            assert traces[1]==traces[2]
            diff= a*d-b*c
            if diff<0: assert traces[0]<traces[1]<traces[3]
            if diff>0: assert traces[0]>traces[1]>traces[3]
            if diff==0: assert len(set(traces))==1
            for wd in words:
                tr,_=trace_product(wd,A,B)
                assert tr==traces[rep_orbit[wd]]
            cases+=1

# One explicit exact growth/decline separation example.
a,b,c,d,hj,ha=map(Fraction,['1/5','5/4','3/5','1/2','1/2','2/3'])
A,B=matrices(a,b,c,d,hj,ha)
polys=[trace_product(wd,A,B) for wd in [block,mix1,alternating]]
assert [1-t+delta>0 for t,delta in polys]==[True,True,False]
assert 0<polys[0][1]<1 and len({delta for _,delta in polys})==1
assert [t for t,_ in polys]==[Fraction(5691779,6750000),Fraction(6159779,6750000),Fraction(7895279,6750000)]
print('VERIFY_OK: symbolic six-season polynomial identities, 20-word exhaustive partition, '
      f'{cases} independent exact-rational parameter tests, growth/decline witness')
