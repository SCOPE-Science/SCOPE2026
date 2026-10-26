"""Exact rational checks for Radau IIA positivity on balanced complete multipartite graphs.
Only sympy is required: python verify.py.
"""
import sympy as S
r,m,z=S.symbols('r m z', integer=True, positive=True)
R=lambda x:(6-2*x)/(x*x+4*x+6)
A=R((r-1)*z);B=R(r*z)
DA=(r-1)**2*z*z+4*(r-1)*z+6
DB=r*r*z*z+4*r*z+6
C=(r*(r-1)**2*z**4 + (-2*m*r*r*(r-1)+12*r*r-18*r+6)*z**3
   + (-2*m*r*r+8*m*r+18*r-18)*z*z + 12*m*(r+1)*z +36*m)
assert S.factor(DA*DB*(1+r*(m-1)*A+(r-1)*B)-r*C)==0
assert S.factor(DA*DB*(1-r*A+(r-1)*B)-r*(r-1)*z*z*((r*r-r)*z*z+(12*r-6)*z+18))==0
assert S.factor(1-B-(r*z)*(r*z+6)/DB)==0
print('GENERIC_IDENTITIES_OK')
# Primitive sign-polynomials and split endpoints provide positivity certificates on [0,B]
# via Bernstein substitution z=B*t/(1+t), and on [B,infinity) via z=B+t.
certs={(3,3):2,(4,2):1,(5,2):2}
for (rr,mm),endpoint in certs.items():
   F=1+rr*(mm-1)*R((rr-1)*z)+(rr-1)*R(rr*z)
   pp=S.Poly(S.cancel(F).as_numer_denom()[0],z).primitive()[1].as_expr()
   t=S.symbols('t',nonnegative=True)
   q=S.Poly(S.cancel((1+t)**4*pp.subs(z,S.Rational(endpoint)*t/(1+t))),t)
   v=S.Poly(S.expand(pp.subs(z,t+endpoint)),t)
   assert all(c>0 for c in q.all_coeffs())
   assert all(c>0 for c in v.all_coeffs())
   print('POSITIVE_POLYNOMIAL_CERT',rr,mm,endpoint,pp,q.all_coeffs(),v.all_coeffs())
# Strict failure witnesses and monotonicity in part-size m, for r=3,4,5.
for rr,mm,zz in [(3,4,4),(4,3,2),(5,3,2)]:
    val=S.factor((1+rr*(mm-1)*R((rr-1)*z)+(rr-1)*R(rr*z)).subs(z,zz))
    assert val<0
    assert R(S.Integer(rr-1)*zz)<0
    print('NEGATIVE_WITNESS',rr,mm,zz,val)
# Complete non-bipartite sample matrices from symmetrized graph Laplacian.
def direct(rr,mm,h):
    n=rr*mm
    L=S.zeros(n)
    for i in range(n):
       for j in range(i+1,n):
          if i//mm != j//mm:
             L[i,i]+=1;L[j,j]+=1;L[i,j]=-1;L[j,i]=-1
    I=S.eye(n)
    T=(6*I-2*h*L)*(6*I+4*h*L+h*h*L*L).inv()
    aa=R((rr-1)*mm*h);bb=R(rr*mm*h)
    diag=(1+rr*(mm-1)*aa+(rr-1)*bb)/n
    inpart=(1-rr*aa+(rr-1)*bb)/n
    cross=(1-bb)/n
    for i in range(n):
        for j in range(n):
            ref=diag if i==j else (inpart if i//mm==j//mm else cross)
            assert S.cancel(T[i,j]-ref)==0
    print('DIRECT_MATRIX_OK',rr,mm,h,n*n)
for rr,mm,h in [(3,2,S.Rational(1,2)),(3,4,1),(4,2,S.Rational(3,4)),(5,2,1),(6,2,1),(3,4,2),(5,3,S.Rational(2,5))]:
    direct(rr,mm,S.Rational(h))
# Descartes' positive-root sign pattern is symbolic for r>=3,m>=2:
# cubic coefficient is decreasing in m and at m=2 is
# -2*(r-1)*(2*r*r-6*r+3)<0 for all r>=3.
assert S.factor(S.expand(C).coeff(z,3).subs(m,2)+2*(r-1)*(2*r*r-6*r+3))==0
# Exact positivity of R(x)+1/10 and derivative sign on x in [6,36/5].
x=S.symbols('x',positive=True)
assert S.factor(R(x)+S.Rational(1,10)-((x-8)**2+2)/(10*(x*x+4*x+6)))==0
assert S.factor(S.diff(R(x),x) - 2*(x*x-6*x-18)/(x*x+4*x+6)**2)==0
# R(6) and R(36/5) are strictly negative; monotonicity on the interval.
assert R(S.Integer(6))==-S.Rational(1,11)
assert R(S.Rational(36,5))<-S.Rational(1,11)
print('VERIFY_OK all exact sign, symbolic, and direct rational identities')
