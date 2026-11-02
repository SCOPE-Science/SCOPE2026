"""Exact symbolic and rational checks for a one-year seed-bank occupancy model.

Requires Python 3 and SymPy. All checks use exact arithmetic.
"""
from fractions import Fraction as F
from itertools import product
import sympy as sp


def probs(c, g0, g1, d):
    return {(y, z): (1-d)*(1-(1-c)*(1-g0)**y*(1-g1)**z)
            for y, z in product((0,1), repeat=2)}


def invert(q):
    a = q[1,0]-q[0,0]
    b = q[0,1]-q[0,0]
    r = q[1,0]+q[0,1]-q[0,0]-q[1,1]
    assert a > 0 and b > 0 and 0 < r < min(a,b)
    w = a*b/r
    u = q[0,0]+w
    assert 0 < u < 1
    return (q[0,0]/u, a/w, b/w, 1-u)


def stationary_pairs(q):
    # Ratios from balance in the four-state chain of consecutive visible pairs.
    r1 = q[0,0]/(1-q[0,1])
    r2 = q[1,0]/(1-q[1,1])
    p00 = 1/(1 + 2*r1 + r1*r2)
    return {(0,0):p00, (0,1):r1*p00,
            (1,0):r1*p00, (1,1):r1*r2*p00}


def check_exact_grid():
    vals = [F(1,7), F(1,4), F(2,5), F(3,4)]
    count=0
    for c, g0, g1, d in product(vals, repeat=4):
        q=probs(c,g0,g1,d)
        assert invert(q)==(c,g0,g1,d)
        p=stationary_pairs(q)
        assert sum(p.values())==1
        # Consecutive-pair transition: (z,y) -> (y,k), k=1 with prob q[y,z].
        for y,z in product((0,1), repeat=2):
            incoming=sum(p[x,z] * (q[z,x] if y else (1-q[z,x])) for x in (0,1))
            assert incoming == p[z,y]
            triple_1=p[z,y]*q[y,z]
            assert triple_1/p[z,y]==q[y,z]
        count+=1
    return count


def check_symbolic():
    c,g0,g1,d=sp.symbols('c g0 g1 d')
    q=probs(c,g0,g1,d)
    a=sp.factor(q[1,0]-q[0,0]);b=sp.factor(q[0,1]-q[0,0]);
    r=sp.factor(q[1,0]+q[0,1]-q[0,0]-q[1,1]);
    w=sp.factor(a*b/r)
    u=sp.factor(q[0,0]+w)
    assert sp.simplify(w-(1-d)*(1-c))==0
    assert sp.simplify(u-(1-d))==0
    assert sp.simplify(a/w-g0)==0
    assert sp.simplify(b/w-g1)==0
    assert sp.simplify(q[0,0]/u-c)==0
    jac=sp.Matrix([q[0,0],q[1,0],q[0,1],q[1,1]]).jacobian([c,g0,g1,d])
    assert sp.simplify(jac.det() + (1-c)**2*(1-d)**3*g0*g1)==0
    return str(sp.factor(jac.det()))


def check_boundary():
    c,g0,d=F(1,5),F(1,2),F(1,4)
    first=probs(c,g0,F(0),d)
    assert first[0,0]==first[0,1]
    assert first[1,0]==first[1,1]
    assert first[1,0]+first[0,1]-first[0,0]-first[1,1]==0
    q=probs(F(1,5),F(1,2),F(1,3),F(1,4))
    assert [q[0,0],q[1,0],q[0,1],q[1,1]]==[F(3,20),F(9,20),F(7,20),F(11,20)]
    return q

if __name__=='__main__':
    print('symbolic jacobian:',check_symbolic())
    print('exact rational parameter tuples:',check_exact_grid())
    print('boundary and example:',check_boundary())
    print('PASS')
