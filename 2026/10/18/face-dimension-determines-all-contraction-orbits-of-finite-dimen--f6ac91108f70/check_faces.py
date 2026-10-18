"""Exact sample checks for contractive maps between strata of a hexagonal-prism norm.
The infinite-dimensional-quantifier-free theorem is proved separately; these finite
samples merely test the constructive formula on a non-cubical unit ball.
Requires sympy (rational linear algebra)."""
from sympy import Matrix, Rational
from itertools import product
H = [(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]
V = [Matrix([a,b,c]) for (a,b),c in product(H,(-1,1))]
facets=[Matrix([[1,0,0]]),Matrix([[-1,0,0]]),Matrix([[0,1,0]]),Matrix([[0,-1,0]]),Matrix([[1,-1,0]]),Matrix([[-1,1,0]]),Matrix([[0,0,1]]),Matrix([[0,0,-1]])]

def norm(v):
    a,b,c=v
    return max(abs(a),abs(b),abs(a-b),abs(c))

def exposing(x):
    active=[f for f in facets if (f*x)[0]==1]
    assert active
    f=sum(active,Matrix([[0,0,0]]))/len(active)
    face=[v for v in V if (f*v)[0]==1]
    d=Matrix.hstack(*[v-face[0] for v in face]).rank() if len(face)>1 else 0
    assert (f*x)[0]==1
    return f,face,d

def tangent_basis(x,f,face):
    ans=[]
    for v in face:
        w=v-x
        if Matrix.hstack(*(ans+[w])).rank()>len(ans):
            ans.append(w)
    for w in f.nullspace():
        if Matrix.hstack(*(ans+[w])).rank()>len(ans):
            ans.append(w)
    assert len(ans)==2 and (f*Matrix.hstack(*ans))==Matrix([[0,0]])
    return ans

def realization(x,y):
    f,fx,k=exposing(x);g,fy,l=exposing(y)
    assert k<=l
    U=tangent_basis(x,f,fx);W=tangent_basis(y,g,fy)
    SX=Matrix.hstack(x,*U)
    assert SX.det()!=0
    for j in range(1,40):
        eps=Rational(1,2**j)
        T=Matrix.hstack(y,eps*W[0],eps*W[1])*SX.inv()
        if all(norm(T*v)<=1 for v in V):
            assert T.det()!=0 and T*x==y
            return j,T
    raise AssertionError('no small contraction found')

reps={
    'vertex-in':Matrix([1,0,1]),
    'edge-in':Matrix([1,Rational(1,2),1]),
    'facet-in':Matrix([1,Rational(1,2),0]),
    'vertex-out':Matrix([-1,0,-1]),
    'edge-out':Matrix([Rational(1,2),1,-1]),
    'facet-out':Matrix([-Rational(1,2),-1,0]),
}
assert [exposing(reps[s])[2] for s in ('vertex-in','edge-in','facet-in')]==[0,1,2]
count=0
for in_key in ('vertex-in','edge-in','facet-in'):
 for out_key in ('vertex-out','edge-out','facet-out'):
  x,y=reps[in_key],reps[out_key]
  assert norm(x)==norm(y)==1
  if exposing(x)[2]<=exposing(y)[2]:
   j,T=realization(x,y)
   print(in_key,'->',out_key,'eps=2^-'+str(j),'det=',T.det())
   count+=1
assert count==6
print('PASS: six ordered face-dimension cases and every one of 12 vertices checked exactly')
