#!/usr/bin/env python3
"""Independent, exact finite-extension singular-locus test for plane cubics.

For a singular plane cubic over GF(3), there is a singular geometric point
of degree at most 3: an integral cubic has at most one singular point;
a line+conic meets in degree 2; three geometric lines are defined over
an extension of degree at most 3, and two meet. Therefore testing points
on P^2 over GF(3), GF(9), GF(27) is conclusive for every cubic.
"""
from itertools import product

EXPS = [(3-i-j,i,j) for i in range(4) for j in range(4-i)]
# Columns correspond, in this order, to X^3, X^2 Z, X Z^2, Z^3,
# X^2 Y, XYZ, Y Z^2, X Y^2, Y^2 Z, Y^3.
F = (2,0,1,0,0,0,0,0,1,0)
G = (1,2,0,0,0,0,1,1,0,0)
H = (0,0,0,1,2,0,0,0,1,2)
FORMS=(F,G,H)
PARAMS=tuple(t for t in product(range(3),repeat=3)
             if any(t) and next(x for x in t if x)==1)
assert len(PARAMS)==13

class Field:
    def __init__(self,k,modulus):
        self.k=k; self.q=3**k
        def digs(x):return [(x//3**i)%3 for i in range(k)]
        def enc(v):return sum((c%3)*3**i for i,c in enumerate(v))
        q=self.q
        self.add=[[enc([(digs(a)[i]+digs(b)[i])%3 for i in range(k)])
                   for b in range(q)] for a in range(q)]
        self.mul=[]
        for a in range(q):
            row=[]
            for b in range(q):
                p=[0]*(2*k-1)
                for i,u in enumerate(digs(a)):
                    for j,v in enumerate(digs(b)):
                        p[i+j]=(p[i+j]+u*v)%3
                for r in range(2*k-2,k-1,-1):
                    c=p[r]
                    for j in range(k):p[r-k+j]=(p[r-k+j]-c*modulus[j])%3
                row.append(enc(p[:k]))
            self.mul.append(row)
        self.inv=[0]*q
        for a in range(1,q):
            self.inv[a]=next(b for b in range(1,q) if self.mul[a][b]==1)
        self.power=[[1]*4 for _ in range(q)]
        for a in range(q):
            for d in range(1,4):self.power[a][d]=self.mul[self.power[a][d-1]][a]
    def evaluate(self,c,P):
        total=0
        for val,(i,j,k) in zip(c,EXPS):
            if val:
                term=self.mul[self.mul[self.power[P[0]][i]][self.power[P[1]][j]]][self.power[P[2]][k]]
                total=self.add[total][self.mul[val][term]]
        return total
    def projective_points(self):
        q=self.q
        return [(1,a,b) for a,b in product(range(q),repeat=2)] + \
               [(0,1,a) for a in range(q)] + [(0,0,1)]

def deriv(c,v):
    # The formal partial derivative is a quadratic form.
    return [((coef*exps[v])%3, tuple(exps[j]-(j==v) for j in range(3)))
            for coef,exps in zip(c,EXPS) if coef and exps[v]%3]

def quad_eval(field,terms,P):
    total=0
    for coef,(i,j,k) in terms:
        u=field.mul[field.mul[field.power[P[0]][i]][field.power[P[1]][j]]][field.power[P[2]][k]]
        total=field.add[total][field.mul[coef][u]]
    return total

fields=[Field(1,[0]),Field(2,[1,0]),Field(3,[1,2,0])]
for abc in PARAMS:
    coeff=[sum(a*form[i] for a,form in zip(abc,FORMS))%3 for i in range(10)]
    derivs=[deriv(coeff,v) for v in range(3)]
    checked=[]
    for fld in fields:
        points=fld.projective_points()
        checked.append(len(points))
        for P in points:
            if fld.evaluate(coeff,P)==0 and all(quad_eval(fld,dd,P)==0 for dd in derivs):
                raise AssertionError(('singular cubic',abc,'extension degree',fld.k,'point',P))
    print('%s no singular points over degrees 1,2,3 (%s)' % (abc,checked))
print('PASS: all 13 geometrically smooth by cubic singularity field-degree bound')
