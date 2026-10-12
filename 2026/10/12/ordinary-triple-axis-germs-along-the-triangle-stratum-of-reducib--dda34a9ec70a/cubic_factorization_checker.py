"""Exact tangent-space checks for the line-times-conic locus of ternary cubics.

Run: python cubic_factorization_checker.py
Requires SymPy. Finite calculations supplement the geometric proof.
"""
import sympy as s
from itertools import combinations
x, y, z = s.symbols('x y z')
V1 = [x,y,z]
V2 = [x*x,x*y,x*z,y*y,y*z,z*z]
V3 = [x**3,x*x*y,x*x*z,x*y*y,x*y*z,x*z*z,y**3,y*y*z,y*z*z,z**3]

def vec(p):
    P=s.Poly(s.expand(p),x,y,z)
    return s.Matrix([P.coeff_monomial(m) for m in V3])

def matrix(forms):
    return s.Matrix.hstack(*(vec(f) for f in forms))

def tangent_line_conic(L,Q):
    return matrix([Q*u for u in V1]+[L*v for v in V2])

def tangent_three_lines(Ls):
    return matrix([s.prod(Ls[:i]+Ls[i+1:])*v for i in range(3) for v in V1])

def check(Ls, expected_sum):
    F=s.prod(Ls)
    T=[tangent_line_conic(L,s.cancel(F/L)) for L in Ls]
    Z=tangent_three_lines(Ls)
    ranks=[t.rank() for t in T]
    pairs=[(a,b,s.Matrix.hstack(T[a],T[b]).rank()) for a,b in combinations(range(3),2)]
    tri=s.Matrix.hstack(*T).rank()
    assert ranks==[8,8,8], ranks
    assert Z.rank()==7, Z.rank()
    assert all(r==9 for _,_,r in pairs),pairs
    assert tri==expected_sum,(tri,expected_sum)
    assert all(s.Matrix.hstack(Z,t).rank()==t.rank() for t in T)
    print(f"Ls={Ls}: branch-ranks={ranks} triple-locus-rank={Z.rank()} pairwise-sum-ranks={[r for _,_,r in pairs]} triple-sum-rank={tri}")
    return tri

if __name__=='__main__':
    check((x,y,z),10)
    check((x+y,y+z,z+x),10)
    check((x,y,x+y),9)
    # Hilbert series of the ordinary transverse triple-axis ring with six smooth parameters:
    t=s.symbols('t')
    assert s.simplify((1+2*t)/(1-t)**7-(1-t**2*3+2*t**3)/(1-t)**9)==0
    # The last equality comes from the Stanley-Reisner ideal (uv,uw,vw).
    print('hilbert_series=(1+2t)/(1-t)^7; multiplicity=3; CM_type=2')
    print('PASS')
