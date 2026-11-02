#!/usr/bin/env python3
"""Independent exact symbolic and finite-field checks for a quartic Hessian."""
import itertools
import sympy as sp

v=sp.symbols('u0:4'); x=list(v)+[-sum(v)]
def ee(xs,k):
    return sp.expand(sum(sp.prod(c) for c in itertools.combinations(xs,k)))
f=ee(x,3); h=ee(x,4)
def in_f3(poly):
    return sp.Poly(poly,*v,modulus=3).is_zero
hf=sp.factor(sp.det(sp.hessian(f,v)))
assert in_f3(hf-h), 'cubic Hessian identity failed'
print('HESSIAN_EQUALS_FOURTH_ELEMENTARY_SYMMETRIC_MOD3=YES')
# Nodes of the quartic have projective classes with exactly one positive and one negative,
# or one positive and four negative, in F3.
nodes=set()
for i,j in itertools.combinations(range(5),2):
    a=[0]*5;a[i]=1;a[j]=2
    nodes.add(tuple(a))
for i in range(5):
    a=[2]*5;a[i]=1
    # normalize projectively so first nonzero coordinate is 1
    if a[0]==2: a=[(2*t)%3 for t in a]
    nodes.add(tuple(a))
assert len(nodes)==15
# All nodes on the zero locus and satisfying Jacobian criterion.
X=sp.symbols('X0:5')
e4=ee(X,4)
de4=[sp.diff(e4,t) for t in X]
for p in nodes:
    subs=dict(zip(X,p))
    assert int(e4.subs(subs))%3==0
    assert len({int(g.subs(subs))%3 for g in de4})==1
print('CANDIDATE_RATIONAL_NODES=15 (10 PAIR-SUPPORT + 5 ALL-NONZERO)')
# Local charts X0=1, X1=a, X2=b, X3=c, X4=-1-a-b-c.
a,b,c=sp.symbols('a b c')
local=ee([1,a,b,c,-1-a-b-c],4)
for name, p in [('PAIR_SUPPORT',(2,0,0)),('ALL_NONZERO',(2,2,2))]:
    mat=sp.hessian(local,[a,b,c]).subs({a:p[0],b:p[1],c:p[2]})
    assert int(mat.det())%3 !=0
    print(name+'_LOCAL_QUADRATIC_HESSIAN_DET_MOD3='+str(int(mat.det())%3))
# GF(3), GF(9) = GF(3)[theta] / (theta^2+1).
def tables(q):
    if q==3:
        add=lambda i,j:(i+j)%3
        mul=lambda i,j:(i*j)%3
    else:
        def add(i,j):return (i%3+j%3)%3 + 3*((i//3+j//3)%3)
        def mul(i,j):return ((i%3)*(j%3)+2*(i//3)*(j//3))%3 + 3*(((i%3)*(j//3)+(i//3)*(j%3))%3)
    aa=[[add(i,j) for j in range(q)] for i in range(q)]
    mm=[[mul(i,j) for j in range(q)] for i in range(q)]
    neg=[next(j for j in range(q) if aa[i][j]==0) for i in range(q)]
    return aa,mm,neg

def count(q):
    add,mul,neg=tables(q)
    count=0
    for first in range(4):
        for tail in itertools.product(range(q),repeat=3-first):
            v=[0]*first+[1]+list(tail)
            # five coordinates on sum-zero hyperplane
            s=0
            for z in v:s=add[s][z]
            v.append(neg[s])
            e=[1,0,0,0,0]
            for val in v:
                for k in range(4,0,-1):
                    e[k]=add[e[k]][mul[val][e[k-1]]]
            if e[4]==0:count+=1
    return count
p1,p2=count(3),count(9)
assert (p1,p2)==(25,145),(p1,p2)
print('HESSIAN_F3_POINTS='+str(p1))
print('HESSIAN_F9_POINTS='+str(p2))
r1=p1+15*3;r2=p2+15*9
assert (r1,r2)==(70,280)
print('RESOLUTION_F3_POINTS='+str(r1))
print('RESOLUTION_F9_POINTS='+str(r2))
s1=r1-1-3**2;s2=r2-1-9**2
assert (s1,s2)==(60,198)
assert s1//3==20 and s2//9==22
print('K3_FROBENIUS_NORMALIZED_EIGENVALUES=+1_MULTIPLICITY_21,-1_MULTIPLICITY_1')
print('VERIFY_OK')
