"""Finite face census for vertex-witness Cech complexes under absolute product norms.
The infinite universal statement is proved separately, not by finite census.
"""
from itertools import combinations,product
from math import sqrt

V=list(product((0,1),repeat=2))

def faces(norm,r):
    ret=[]
    for k in range(1,5):
        for q in combinations(V,k):
            if any(all(norm(abs(x[0]-y[0]),abs(x[1]-y[1]))<=r+1e-10 for y in q) for x in V):
                ret.append(q)
    return [sum(len(t)==j for t in ret) for j in range(1,5)]

N=[('maximum',lambda x,y:max(x,y),1),
   ('taxicab',lambda x,y:x+y,2),
   ('euclidean',lambda x,y:sqrt(x*x+y*y),sqrt(2)),
   ('cut-square',lambda x,y:max(x,y,(x+y)/1.5),4/3)]
for name,norm,c in N:
    assert faces(norm,0)==[4,0,0,0]
    assert faces(norm,1)==([4,6,4,1] if c==1 else [4,6,4,0])
    if c>1:
        assert faces(norm,(1+c)/2)==[4,6,4,0]
    assert faces(norm,c)==[4,6,4,1]
    print(name,'diagonal',c,'at_r1',faces(norm,1))
print('PASS: four normalized product norms, exact face changes and critical endpoints')
