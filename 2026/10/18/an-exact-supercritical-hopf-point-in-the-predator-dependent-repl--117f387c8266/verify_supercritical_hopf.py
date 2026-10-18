"""Rigorous interval confirmation of the first Lyapunov coefficient at a three-species Hopf point.
Requires sympy and mpmath. All model parameters and root endpoints are rational.
"""
import sympy as s
from mpmath import iv
from functools import lru_cache
iv.dps=90
x,P,Y,K=s.symbols('x P Y K')
a,b,c,d=map(s.Rational,['16/5','3/4','3','4/5'])
ap,bp,cp,dp=map(s.Rational,['1/2','3/5','7/20','3/10']);beta=s.Integer(2)
r=s.expand(a*x*x+(b+c)*x*(1-x)+d*(1-x)**2)
delta=s.expand(ap*x*x+(bp+cp)*x*(1-x)+dp*(1-x)**2)
d0=s.expand((a-c)*x+(b-d)*(1-x));d1=s.expand((ap-cp)*x+(bp-dp)*(1-x))
m=s.cancel(d0/d1); F=s.cancel(r-delta*m);kappa=s.cancel(1/(delta*F))
f=s.Matrix([x*(1-x)*(d0-d1*Y),(r-P/K-delta*Y)*P,beta*(-1+delta*P)*Y]); z=[x,P,Y]
subs={Y:m,P:1/delta,K:kappa}
J=f.jacobian(z).subs(subs).applyfunc(s.cancel)
a1=s.cancel(-s.trace(J));a2=s.cancel((s.trace(J)**2-s.trace(J*J))/2);a3=s.cancel(-J.det());H=s.cancel(a1*a2-a3)
# Exact Hurwitz determinant factorization.
rootpoly=s.Poly(67455*x**8-1105515*x**7+5246054*x**6-9041754*x**5+3370659*x**4+3356225*x**3-826776*x**2+296532*x-146880,x)
assert s.cancel(H-rootpoly.as_expr()/(36000*(x-3)*(x-2)**3*(3*x+2)))==0
L=s.Rational('0.338132677197410152848169921736')
U=s.Rational('0.338132677197410152848169921738')
assert rootpoly.eval(L)<0<rootpoly.eval(U)
@lru_cache(None)
def terms(ex):
 n,d=s.fraction(s.cancel(ex)); n=s.Poly(n,x);d=s.Poly(d,x)
 # Evaluate exact rational functions using integer-coefficient Horner arithmetic.
 def ints(poly):
  cs=poly.all_coeffs();factor=__import__("functools").reduce(__import__("math").lcm,[int(c.q) for c in cs],1);return tuple(int(c*factor) for c in cs),int(factor)
 na,ns=ints(n); da,ds=ints(d)
 return na,da,ds,ns
T=iv.mpf([str(L),str(U)])
def horner(cs):
 o=iv.mpf(0)
 for c in cs:o=o*T+iv.mpf(c)
 return o
def ev(ex):
 n,d,ds,ns=terms(s.cancel(ex))
 return horner(n)*iv.mpf(ds)/(horner(d)*iv.mpf(ns))
def matvect(A,v):return [sum((A[i][j]*v[j] for j in range(3)),iv.mpc(0)) for i in range(3)]
def det3(A):
 return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
def solve3(A,y):
 de=det3(A);v=[]
 for j in range(3):
  Aj=[[y[i] if col==j else A[i][col] for col in range(3)] for i in range(3)]
  v.append(det3(Aj)/de)
 return v
JA=[[ev(J[i,j]) for j in range(3)] for i in range(3)]; ww=iv.sqrt(ev(a2));I=iv.mpc(0,1)
# Anchor the right eigenvector at third coordinate 1; analogous for left eigenvector.
q3=iv.mpc(1);q1=-JA[0][2]/(JA[0][0]-I*ww);q2=-(JA[1][0]*q1+JA[1][2]*q3)/(JA[1][1]-I*ww);qv=[q1,q2,q3]
p3=iv.mpc(1);p2=-JA[2][1]/(JA[1][1]+I*ww);p1=(-I*ww-JA[1][2]*p2)/JA[0][2];pv=[p1,p2,p3]
conj=lambda v:iv.mpc(v.real,-v.imag)
sc=sum((conj(pv[j])*qv[j] for j in range(3)),iv.mpc(0))
pv=[v*conj(1/sc) for v in pv]
def dotp(v):return sum((conj(pv[j])*v[j] for j in range(3)),iv.mpc(0))
B=[[[ev(s.diff(f[i],z[j],z[k]).subs(subs)) for k in range(3)] for j in range(3)] for i in range(3)]
C=[[[[ev(s.diff(f[i],z[j],z[k],z[l]).subs(subs)) for l in range(3)] for k in range(3)] for j in range(3)] for i in range(3)]
def bil(u,v):return [sum((B[i][j][k]*u[j]*v[k] for j in range(3) for k in range(3)),iv.mpc(0)) for i in range(3)]
def tri(u,v,w):return [sum((C[i][j][k][l]*u[j]*v[k]*w[l] for j in range(3) for k in range(3) for l in range(3)),iv.mpc(0)) for i in range(3)]
conjq=[conj(v) for v in qv]
t1=tri(qv,qv,conjq)
t2=bil(qv,solve3(JA,bil(qv,conjq)))
S=[[ (2*I*ww if j==k else iv.mpc(0)) -JA[j][k] for k in range(3)] for j in range(3)]
t3=bil(conjq,solve3(S,bil(qv,qv)))
result=[t1[i]-2*t2[i]+t3[i] for i in range(3)]
G=dotp(result)
l1=G.real/(2*ww)
# Boundary checks and the Hopf-vector relations enclose exact zero at the root.
assert (ev(m).a>0 and ev(F).a>0 and ev(delta).a>0
        and ev(1/delta).a>0 and ev(kappa).a>0)
assert ev(s.diff(kappa,x)).b < 0
assert (rootpoly.eval(L)<0 and rootpoly.eval(U)>0)
def contains_zero(v):return v.a<=0<=v.b
for res in [matvect(JA,qv)[i]-I*ww*qv[i] for i in range(3)]:
 assert contains_zero(res.real) and contains_zero(res.imag),res
for i in range(3):
 leftres=sum((JA[j][i]*pv[j] for j in range(3)),iv.mpc(0))+I*ww*pv[i]
 assert contains_zero(leftres.real) and contains_zero(leftres.imag),leftres
for name,v in [('Pprime',ev(s.diff(rootpoly.as_expr(),x))),('a1',ev(a1)),('a2',ev(a2)),('a3',ev(a3)),('Hprime',ev(s.diff(H,x))),('kappaprime',ev(s.diff(kappa,x))),('omega',ww),('scalar',dotp(qv)),('l1',l1)]:print(name,v)
assert ev(s.diff(rootpoly.as_expr(),x)).a>0
assert ev(a1).a>0 and ev(a2).a>0 and ev(a3).a>0
assert ev(s.diff(H,x)).a>0 and ev(s.diff(kappa,x)).b<0
assert l1.b < 0
print('CERTIFIED: unique root in specified rational interval, transversal Hopf pair, negative Lyapunov coefficient.')
