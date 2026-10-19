#!/usr/bin/env python3
"""Exact rational check of tetrahedral tangential harmonic samples.

Run: python3 verify_tetra.py   (requires sympy).
The all-degree argument also uses the classical Legendre Bernstein bound,
whose elementary numerical consequence is checked here with rational squares.
"""
import sympy as S
from fractions import Fraction
from itertools import product

V = [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
B = [[(b,-a,0),(c,0,-a)] for a,b,c in V]
idx = [(i,j) for i in range(4) for j in range(2)]
def dot(a,b): return sum(x*y for x,y in zip(a,b))
D,X,Y=S.symbols('D X Y')

def gram(D0,X0,Y0):
    return S.Matrix(8,8,lambda a,b: (
        D0*dot(B[idx[a][0]][idx[a][1]], B[idx[b][0]][idx[b][1]])
        if idx[a][0]==idx[b][0] else
        X0*dot(B[idx[a][0]][idx[a][1]], B[idx[b][0]][idx[b][1]])
        + Y0*S.Rational(dot(B[idx[a][0]][idx[a][1]],V[idx[b][0]])*
                           dot(V[idx[a][0]],B[idx[b][0]][idx[b][1]]),3)))

K=gram(D,X,Y)
expected=-(-3*D+3*X-4*Y)**2*(-3*D+3*X+4*Y)**3*(9*D+15*X+4*Y)**3/S.Integer(2187)
assert S.factor(K.det(method='domain-ge')-expected)==0, 'Gram determinant factorization'
t=S.symbols('t')
rank_seq=[];zeros={}
for degree in range(13):
    p=S.legendre(degree,t)
    d=S.Rational(degree*(degree+1),2)
    x=S.diff(p,t).subs(t,S.Rational(-1,3))
    y=S.diff(p,t,2).subs(t,S.Rational(-1,3))
    M=gram(d,x,y)
    rank_seq.append(M.rank())
    zeros[degree]=[name for name,value in zip(('A','B','C'),
        (-3*d+3*x-4*y,-3*d+3*x+4*y,9*d+15*x+4*y)) if value==0]
assert rank_seq==[0,3,5,6,8,5,8,8,8,8,8,8,8],rank_seq
assert zeros=={0:['A','B','C'],1:['A','B'],2:['B'],3:['A'],4:[],5:['B'],
                6:[],7:[],8:[],9:[],10:[],11:[],12:[]},zeros

# An independent route for the exceptional ranks: homogeneous harmonic
# polynomials over Q and their exact tangential directional derivatives.
a,b,c=S.symbols('a b c')
for degree in (1,2,3,4,5,6):
    mons=[a**i*b**j*c**(degree-i-j) for i in range(degree+1) for j in range(degree+1-i)]
    lo=[a**i*b**j*c**(degree-2-i-j) for i in range(degree-1) for j in range(degree-1-i)] if degree>=2 else []
    lap=S.Matrix([[S.expand(sum(S.diff(m,z,2) for z in (a,b,c))).coeff(a,i).coeff(b,j).coeff(c,degree-2-i-j) for m in mons]
          for i in range(degree-1) for j in range(degree-1-i)]) if degree>=2 else S.zeros(0,len(mons))
    harm=lap.nullspace()
    assert len(harm)==2*degree+1
    fns=[sum(u*m for u,m in zip(vec,mons)) for vec in harm]
    E=S.Matrix([[sum(v*S.diff(f,z) for v,z in zip(B[i][j],(a,b,c))).subs(dict(zip((a,b,c),V[i])))
                for f in fns] for i,j in idx])
    assert E.rank()==rank_seq[degree],(degree,E.rank(),rank_seq[degree])

# Exact rational verification of every strict numerical inequality used in the
# Bernstein-bound tail; no floating-point thresholds are involved.
assert 576 < 49*12       # 1/sqrt(12) < 7/24
assert 1024 < 9*117      # 1/(3 sqrt(13)) < 3/32
assert Fraction(9,56)*(Fraction(7,24)+Fraction(3,32)) < Fraction(1,16)
assert 324 < 25*13       # 3/sqrt(13) < 5/6
assert Fraction(2,16)+Fraction(5,6)<1
assert Fraction(18,16)+Fraction(5,2)<9
print('VERIFY_OK determinant_factor=exact rank_0_to_12='+str(rank_seq)+
      ' direct_harmonics_1_to_6=exact Bernstein_tail_13_plus=certified')
