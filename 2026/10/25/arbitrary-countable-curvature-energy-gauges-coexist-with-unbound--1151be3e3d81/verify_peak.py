"""Exact symbolic check of the quadratic four-dimensional curvature model."""
import sympy as sp
x1,x2,x3,x4=xs=sp.symbols('x1 x2 x3 x4',real=True)
P=sp.Matrix([
 [x2*x2-x3*x3,-x1*x2,x1*x3,0],
 [-x1*x2,x1*x1-x4*x4,0,x2*x4],
 [x1*x3,0,-x1*x1+x4*x4,-x3*x4],
 [0,x2*x4,-x3*x4,-x2*x2+x3*x3]
])
assert sp.expand(sp.trace(P))==0
for j in range(4):
 assert sp.expand(sum(sp.diff(P[i,j],xs[i]) for i in range(4)))==0
 assert sp.expand(sum(xs[i]*P[i,j] for i in range(4)))==0
for i in range(4):
 for j in range(4):
  assert sp.expand(sum(sp.diff(P[i,j],z,2) for z in xs))==0
# Normal-coordinate curvature at zero for g = delta + t P,
# so the parameter t is a_j log(epsilon_j) in the metric.
D=lambda i,j,k,l:sp.diff(P[i,j],xs[k],xs[l])
r4=[]
for i in range(4):
 for j in range(4):
  for k in range(4):
   for l in range(4):
    r=sp.expand((D(i,l,j,k)+D(j,k,i,l)-D(i,k,j,l)-D(j,l,i,k))/2)
    r4.append(r)
ric=sp.zeros(4)
for i in range(4):
 for j in range(4):
  ric[i,j]=sum(r4[((k*4+i)*4+k)*4+j] for k in range(4))
assert all(v==0 for v in ric)
normsq=sum(z*z for z in r4)
assert normsq==144,(normsq,ric)
print('Quadratic model: trace/divergence/Laplacian/radial identities PASS')
print('Linearized Ricci contraction = 0; full curvature coefficient squared =',normsq)
print('At a bump center |Rm| = 12 * a_j * log(1/epsilon_j).')
