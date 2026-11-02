"""Exact rational certificate for orthographic wireframe crossing classifications.
Run with: python3 verify_wireframe.py. Uses only the Python standard library.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd
from functools import reduce

def edge_pairs(vertices, graph):
    return [(graph[i], graph[j]) for i,j in combinations(range(len(graph)),2)
            if len(set(graph[i]+graph[j])) == 4]

def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def det(a,b): return a[0]*b[1]-a[1]*b[0]
def orient(a,b,c): return det(sub(b,a),sub(c,a))
def intersect(a,b,c,d):
    return orient(a,b,c)*orient(a,b,d)<0 and orient(c,d,a)*orient(c,d,b)<0

def count(vertices, edges):
    return sum(intersect(vertices[a[0]],vertices[a[1]],vertices[b[0]],vertices[b[1]])
               for a,b in edge_pairs(vertices, edges))

def classify_cube(s,t):
    V=list(product((-1,1),repeat=3)); Q=[(F(x)-s*z,F(y)-t*z) for x,y,z in V]
    E=[(i,j) for i,j in combinations(range(8),2) if sum(x!=y for x,y in zip(V[i],V[j]))==1]
    return count(Q,E)

def classify_octa(s,t):
    Q=[(F(1),F(0)),(F(-1),F(0)),(F(0),F(1)),(F(0),F(-1)),(s,t),(-s,-t)]
    E=[(i,j) for i,j in combinations(range(6),2) if i//2 != j//2]
    return count(Q,E)

def pol_add(a,b):
    c=dict(a)
    for k,v in b.items():c[k]=c.get(k,0)+v
    return {k:v for k,v in c.items() if v}
def pol_neg(a):return {k:-v for k,v in a.items()}
def pol_sub(a,b):return pol_add(a,pol_neg(b))
def pol_mul(a,b):
    c={}
    for (i,j),x in a.items():
        for (k,l),y in b.items():c[(i+k,j+l)]=c.get((i+k,j+l),0)+x*y
    return {k:v for k,v in c.items() if v}
def pol_det(a,b):return pol_sub(pol_mul(a[0],b[1]),pol_mul(a[1],b[0]))
def pol_point_sub(a,b):return (pol_sub(a[0],b[0]),pol_sub(a[1],b[1]))
def pol_orient(a,b,c):return pol_det(pol_point_sub(b,a),pol_point_sub(c,a))
S={(1,0):1};T={(0,1):1};ONE={(0,0):1}
def constant(v):return {(0,0):int(v)} if v else {}
def formal_factor_types(Q,E):
    ans=set();total=0
    for (a,b),(c,d) in edge_pairs(Q,E):
        for z in (pol_orient(Q[a],Q[b],Q[c]),pol_orient(Q[a],Q[b],Q[d]),
                  pol_orient(Q[c],Q[d],Q[a]),pol_orient(Q[c],Q[d],Q[b])):
            if not z:continue
            assert all(i+j<=1 for i,j in z),('unexpected nonlinear determinant',z)
            c=tuple(z.get((i,j),0) for i,j in [(0,0),(1,0),(0,1)])
            g=reduce(gcd,map(abs,c));c=tuple(k//g for k in c)
            if next(k for k in c if k)!=abs(next(k for k in c if k)):
                c=tuple(-k for k in c)
            ans.add(c);total+=1
    return ans,total

def symbolic_cube():
    V=list(product((-1,1),repeat=3))
    Q=[(pol_sub(constant(x),pol_mul(constant(z),S)),
        pol_sub(constant(y),pol_mul(constant(z),T))) for x,y,z in V]
    E=[(i,j) for i,j in combinations(range(8),2) if sum(x!=y for x,y in zip(V[i],V[j]))==1]
    return formal_factor_types(Q,E)
def symbolic_octa():
    Q=[(ONE,constant(0)),(constant(-1),constant(0)),(constant(0),ONE),
       (constant(0),constant(-1)),(S,T),(pol_neg(S),pol_neg(T))]
    E=[(i,j) for i,j in combinations(range(6),2) if i//2!=j//2]
    return formal_factor_types(Q,E)

def main():
    cforms,cnum=symbolic_cube();oforms,onum=symbolic_octa()
    assert cforms=={(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,-1,0),
                    (1,0,1),(1,0,-1),(0,1,1),(0,1,-1)},cforms
    assert oforms=={(1,0,0),(0,1,0),(0,0,1),(1,1,1),(1,-1,-1),(1,1,-1),(1,-1,1)},oforms
    cw=[(F(1,4),F(1,2)),(F(1,2),F(1,4)),(F(1,2),F(2)),
        (F(2),F(1,2)),(F(2),F(3)),(F(3),F(2))]
    ow=[(F(1,4),F(1,4)),(F(3),F(1,2)),(F(1,2),F(3)),(F(1),F(1))]
    cv=[classify_cube(s,t) for s,t in cw]
    ov=[classify_octa(s,t) for s,t in ow]
    assert cv==[2]*6,cv
    assert ov==[2,2,2,6],ov
    print('PASS: cube 6 chambers, counts',cv,'octahedron 4 chambers, counts',ov)
    print('PASS: exact symbolic triple-orientation determinant checks: cube',cnum,'octahedron',onum)
    print('Cube possible vanishing boundaries for positive parameters: s=1,t=1,s=t')
    print('Octahedron possible vanishing boundaries: s+t=1,s=t+1,t=s+1')
if __name__=='__main__':main()
