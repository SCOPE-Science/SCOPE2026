#!/usr/bin/env python3
"""Exact symbolic checks for the cubic-jerk Hopf normal form and physical period."""
import sympy as S
w=S.symbols('w',positive=True,real=True)
i=S.I
M=S.Matrix([[0,1,0],[0,0,1],[-2*w*w,-w*w,-2]])
q=S.Matrix([1,i*w,-w*w]);qb=S.conjugate(q)
L=S.Matrix([[2*i*w,2+i*w,1]])/(-2*w*w+4*i*w)
def zero(x):return S.simplify(S.expand_complex(x))==0
assert all(zero(v) for v in M*q-i*w*q)
assert zero((L*q)[0]-1)
def B(u,v):
 return S.Matrix([0,0,-6*w*u[0]*v[0]-2*w*(u[0]*v[1]+u[1]*v[0])-2*w*u[1]*v[1]])
def C(u,v,t):
 return S.Matrix([0,0,-6*u[0]*v[0]*t[0]-2*(u[0]*v[0]*t[1]+u[0]*v[1]*t[0]+u[1]*v[0]*t[0])-2*(u[0]*v[1]*t[1]+u[1]*v[0]*t[1]+u[1]*v[1]*t[0])])
G=S.factor((L*(C(q,q,qb)-2*B(q,M.inv()*B(q,qb))+B(qb,(2*i*w*S.eye(3)-M).inv()*B(q,q))))[0])
assert zero(S.re(G)+2*(w*w+1)/(w*w+4))
assert zero(S.im(G)+(4*w**4+43*w*w+72)/(3*w*(w*w+4)))
l1=S.re(G)/(2*w)
assert zero(l1+(w*w+1)/(w*(w*w+4)))
deriv=w*w/(-2*w*w+4*i*w)
assert zero(S.re(deriv)+w*w/(2*(w*w+4)))
assert zero(S.im(deriv)+w/(w*w+4))
radial_radius_sq=w*w/(2*(w*w+1))
freqdelta=-S.im(deriv)+S.im(G)*radial_radius_sq/2
assert zero(freqdelta+w*(4*w*w+15)/(12*(w*w+1)))
# Independent Fourier solvability from the scalar third-order equation.
D=lambda f:{k:S.simplify(i*k*w*v) for k,v in f.items()}
def add(*fs):
 out={}
 for f in fs:
  for k,v in f.items():out[k]=out.get(k,0)+v
 return {k:S.factor(v) for k,v in out.items()}
def mul(*fs):
 out={0:S.Integer(1)}
 for f in fs:
  tmp={}
  for k,v in out.items():
   for kk,vv in f.items():tmp[k+kk]=tmp.get(k+kk,0)+v*vv
  out=tmp
 return {k:S.factor(v) for k,v in out.items()}
def sc(c,f):return {k:S.factor(c*v) for k,v in f.items()}
def lin(k):
 z=i*k*w
 return S.factor(z**3+2*z*z+w*w*z+2*w*w)
x1={-1:S.Rational(1,2),1:S.Rational(1,2)}
quad=add(sc(3*w,mul(x1,x1)),sc(2*w,mul(x1,D(x1))),sc(w,mul(D(x1),D(x1))))
x2={k:S.factor(-v/lin(k)) for k,v in quad.items()}
assert all(zero(x2[k]-S.conjugate(x2[-k])) for k in x2)
cubic=add(sc(6*w,mul(x1,x2)),sc(2*w,add(mul(x1,D(x2)),mul(x2,D(x1)))),sc(2*w,mul(D(x1),D(x2))),mul(x1,x1,x1),mul(x1,x1,D(x1)),mul(x1,D(x1),D(x1)))
Delta,Omega2=S.symbols('Delta Omega2',real=True)
res=S.factor(cubic[1]+Delta*w*w/2+Omega2*((3*i**3)*w*w+4*(i**2)*w+w*w*i)/2)
sol=S.solve([S.re(S.expand_complex(res)),S.im(S.expand_complex(res))],[Delta,Omega2],simplify=True)
assert zero(sol[Delta]-(w*w+1)/(2*w*w))
assert zero(sol[Omega2]+(4*w*w+15)/(24*w))
assert zero(freqdelta-sol[Omega2]/sol[Delta])
print('VERIFY_OK: full complex Hopf contraction and independent Fourier solvability')
