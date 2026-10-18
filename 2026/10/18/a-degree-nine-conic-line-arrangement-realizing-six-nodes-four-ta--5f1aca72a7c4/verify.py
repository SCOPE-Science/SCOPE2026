#!/usr/bin/env python3
"""Exact certificate for a nine-degree line-conic arrangement.

Requires Python 3 and SymPy. All calculations are over Q(sqrt(2)), Q,
or the explicitly stated finite field F_101; no floating-point tests.
"""
import sympy as s
from sympy.polys.matrices import DomainMatrix

x, y, z = s.symbols('x y z')
r = s.sqrt(2)
B = x*x + 6*x*z + z*z - 4*y*y
Q = x*z - y*y
F = s.expand(Q*y*(x-y)*(z-y)*(B*B - 16*y*y*(x-z)**2))
T = [-1+r, -1-r, 1+r, 1-r]
lines = [("Y", s.Matrix([0,1,0])), ("X-Y", s.Matrix([1,-1,0])),
         ("Z-Y", s.Matrix([0,-1,1]))]
lines += [(name, s.Matrix([s.expand(t*t), -2*t, 1]))
          for name,t in zip('ABCD',T)]


def zero(a):
    return s.simplify(s.expand(a)) == 0


def same(P, W):
    return all(zero(c) for c in P.cross(W))


def at(P, poly):
    return s.expand(poly.subs({x:P[0], y:P[1], z:P[2]}, simultaneous=True))

# Verify the exact factorization of the quartic into the four tangent lines.
quartic = s.prod([v[0]*x+v[1]*y+v[2]*z for _,v in lines[3:]])
assert zero(quartic-(B*B-16*y*y*(x-z)**2))
assert len(lines) == 7
for i,(_,li) in enumerate(lines):
    for _,lj in lines[i+1:]:
        assert any(not zero(c) for c in li.cross(lj))

# Complete partition of the 21 unordered pairs of lines by projective point.
points=[]
for i in range(7):
    for j in range(i+1,7):
        P=lines[i][1].cross(lines[j][1])
        pos=next((idx for idx,(W,_) in enumerate(points) if same(P,W)),None)
        if pos is None:
            points.append([P,{i,j}])
        else:
            points[pos][1].update([i,j])
assert sum(len(I)*(len(I)-1)//2 for _,I in points)==21
assert len(points)==13
triples=[(P,I) for P,I in points if len(I)==3]
doubles=[(P,I) for P,I in points if len(I)==2]
assert len(triples)==4 and len(doubles)==9
assert all(not zero(at(P,Q)) for P,_ in triples)
assert {tuple(sorted(lines[i][0] for i in I)) for P,I in triples} == {
    ('A','D','Y'), ('B','C','Y'), ('C','D','X-Y'), ('A','B','Z-Y')}

# Only the three vertices of the secant triangle lie on Q.
conic_doubles=[(P,I) for P,I in doubles if zero(at(P,Q))]
assert len(conic_doubles)==3
assert {tuple(sorted(lines[i][0] for i in I)) for P,I in conic_doubles} == {
    ('X-Y','Y'),('Y','Z-Y'),('X-Y','Z-Y')}
for P,I in conic_doubles:
    tangent=s.Matrix([P[2],-2*P[1],P[0]])
    assert all(not same(tangent,lines[i][1]) for i in I)

# Four ordinary conic-line contacts at pairwise distinct points.
contacts=[]
for t,(_,v) in zip(T,lines[3:]):
    P=s.Matrix([1,t,t*t])
    assert zero(at(P,Q))
    assert same(v,s.Matrix([P[2],-2*P[1],P[0]]))
    assert all(not same(P,W) for W,_ in points)
    assert all(not zero(at(P, l[0]*x+l[1]*y+l[2]*z))
               for _,l in lines[:3])
    assert all(not same(P,W) for W in contacts)
    contacts.append(P)
# Three ordinary mixed triple points + four tacnodes + four line-only
# triple points + six nodes account for all intercomponent intersections:
# 21 line-line pairs and 14 conic-line intersection multiplicities.
assert 3*2 + 4*2 == 14
nodes = len(doubles) - len(conic_doubles)
triple_count = len(triples) + len(conic_doubles)
tacnodes = len(contacts)
assert (nodes,tacnodes,triple_count)==(6,4,7)
tau = nodes+3*tacnodes+4*triple_count
assert tau==46

# The degree-4 syzygy coefficient map has size 91 x 45. The displayed
# minor is nonsingular modulo 101 and therefore over Q.
partials = [s.Poly(s.diff(F,v),x,y,z) for v in (x,y,z)]

def syzygy_matrix(d):
    mon=[(i,j,d-i-j) for i in range(d+1) for j in range(d+1-i)]
    target=[(i,j,d+8-i-j) for i in range(d+9) for j in range(d+9-i)]
    loc={power:i for i,power in enumerate(target)}
    arr=[[0]*(3*len(mon)) for _ in target]
    for v,pf in enumerate(partials):
        for idx,m in enumerate(mon):
            for power,coef in pf.terms():
                k=tuple(a+b for a,b in zip(m,power))
                arr[loc[k]][v*len(mon)+idx]=int(coef)
    return arr,mon

A4,mon4=syzygy_matrix(4)
assert len(A4)==91 and len(A4[0])==45
rows=[2,3,4,5,6,15,16,17,18,27,28,29,38,39,48,
      7,8,19,20,21,22,23,24,25,30,31,32,40,41,49,
      26,33,34,35,36,37,12,9,10,42,43,44,45,46,50]
assert len(rows)==45 and len(set(rows))==45

def determinant_modp(matrix,p):
    mat=[[a%p for a in row] for row in matrix]
    n=len(mat)
    assert all(len(row)==n for row in mat)
    det=1
    for c in range(n):
        i=next((k for k in range(c,n) if mat[k][c]!=0),None)
        if i is None:return 0
        if i!=c:
            mat[i],mat[c]=mat[c],mat[i]
            det=-det
        pivot=mat[c][c]
        det=det*pivot%p
        inv=pow(pivot,-1,p)
        for j in range(c+1,n):
            a=mat[j][c]*inv%p
            if a:
                for k in range(c,n):
                    mat[j][k]=(mat[j][k]-a*mat[c][k])%p
    return det%p
assert determinant_modp([A4[i] for i in rows],101)==89

# An exact (characteristic-zero, not modular) degree-five syzygy exists.
A5,mon5=syzygy_matrix(5)
N=DomainMatrix.from_Matrix(s.Matrix(A5)).nullspace()
assert N.shape == (4,63)
first=N.to_Matrix().tolist()[0]
syzygy=[sum(first[j+offset*len(mon5)]*x**a*y**b*z**c
              for j,(a,b,c) in enumerate(mon5)) for offset in range(3)]
assert any(p!=0 for p in syzygy)
assert zero(sum(syzygy[i]*partials[i].as_expr() for i in range(3)))
# Thus mdr(F)=5, and the du Plessis-Wall bound is attained:
assert 64 - 5*(8-5) - 3 == tau
print('PASS: 7 lines, 1 smooth conic; (n2,t2,n3)=(6,4,7), tau=46')
print('PASS: projective degree-4 Jacobian syzygy matrix has full rank 45')
print('PASS: exact degree-5 syzygies, mdr=5; maximal Tjurina bound 46')
