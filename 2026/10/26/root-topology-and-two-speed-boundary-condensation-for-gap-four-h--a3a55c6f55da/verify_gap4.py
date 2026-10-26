"""Exact symbolic verification of the gap-four Hartogs diagonal formulas.
Requires Python 3 and SymPy; no external files or network access.
The mathematical proof in RESULT.md states the analytic root arguments.
"""
import sympy as S
q,n,x,s,t,u=S.symbols('q n x s t u')
F=x*x*(x+2)*(x+4)
B=41*x**4+294*x**3+400*x**2-48*x+96
Cs={1:7*x**4+66*x**3+92*x**2-24*x+64,
    3:5*x**4+70*x**3+100*x**2-40*x+64}
coef={1:[(n+2)*(n+3)*(n+7)/96,
         (n+3)*(n*n+9*n+22)/16,
         (n+3)*(n+4)*(n+5)/8,
         (n+3)*(3*n*n+27*n+58)/16,
         (11*n**3+132*n*n+571*n+870)/48],
      3:[(n+1)*(n+5)*(n+6)/96,
         (n+5)*(n*n+7*n+14)/16,
         (n+3)*(n+4)*(n+5)/8,
         (n+5)*(3*n*n+21*n+34)/16,
         (11*n**3+132*n*n+571*n+882)/48]}
def sum1(lo,hi):return S.expand((hi*(hi+1)-(lo-1)*lo)/2)
def sum2(lo,hi):return S.expand((hi*(hi+1)*(2*hi+1)-(lo-1)*lo*(2*lo-1))/6)
def verify_case(residue,bounds):
 m=4*q+residue; nn=m-4
 out=[S.S(0) for _ in range(9)];out[4]=m*m
 for h,(lo,hi) in enumerate(bounds):
  A=S.expand(m*(h+1)*sum1(lo,hi)-4*sum2(lo,hi))
  C=S.expand(4*sum2(lo,hi)-m*h*sum1(lo,hi))
  D=S.expand(m*m*(h+1)*(hi-lo+1)-m*(h+5)*sum1(lo,hi)+4*sum2(lo,hi))
  E=S.expand(4*m*sum1(lo,hi)-4*sum2(lo,hi)-m*m*h*(hi-lo+1)+m*h*sum1(lo,hi))
  for index,amount in [(h,A),(h+1,C),(h+4,D),(h+5,E)]:out[index]+=amount
 out=[S.factor(o) for o in out]
 for j in range(9):
  assert S.simplify(out[j]-out[8-j])==0,(residue,j,'palindrome')
  assert S.simplify(out[j]-coef[residue][min(j,8-j)].subs(n,nn))==0,(residue,j,S.factor(out[j]-coef[residue][min(j,8-j)].subs(n,nn)))
 P=S.expand(out[4]+sum(out[4-j]*2*S.chebyshevt(j,x/2) for j in range(1,5)))
 expected=nn*nn*(nn+12)*F/96+nn*B/96+Cs[residue]/16
 assert S.simplify(P-expected.subs(n,nn))==0,(residue,'P')
 shifted=S.Poly(S.expand(P.subs(x,-2-t)),t)
 # Exactly two sign variations for q>=1; factored coefficient formulas are in RESULT.md.
 for z in [2,3]:
  assert S.expand(shifted.all_coeffs()[z].subs(q,5))<0
 assert S.expand(P.subs(x,-4)).subs(q,1)<0
 assert S.expand(P.subs(x,-2)-nn-4)==0
 print('Exact coefficient and transformed-quartic identities: residue',residue,'PASS')
for r,bounds in [(1,[(1,q),(q+1,2*q),(2*q+1,3*q),(3*q+1,4*q)]),
                 (3,[(1,q),(q+1,2*q+1),(2*q+2,3*q+2),(3*q+3,4*q+2)])]:
 verify_case(r,bounds)

def bernstein_coefficients(poly,a):
 v=S.Poly(S.expand(poly.subs(x,a+t)),t)
 return [S.factor(sum(v.nth(j)*S.binomial(k,j)/S.binomial(4,j) for j in range(k+1))) for k in range(5)]
for label,poly in [('B',B),('C1',Cs[1]),('C3',Cs[3])]:
 for a in [-2,-1,0,1]:
  z=bernstein_coefficients(poly,a)
  assert all(c>0 for c in z),(label,a,z)
 # On [2,infinity), all power-basis coefficients after shifting x=2+t are positive.
 v=S.Poly(S.expand(poly.subs(x,t+2)),t)
 assert all(c>0 for c in v.all_coeffs()),(label,v)
 print('Positivity on [-2,infinity) by exact Bernstein and shifted-monomial coefficients:',label,'PASS')
# Leading-order collision identities.
z,u=S.symbols('z u')
L=(z*z+1)**2*(z+1)**2*(z*z+4*z+1)
assert S.factor(S.together(z**4*F.subs(x,z+1/z)-L))==0
for center,displacement in [(S.I,-S.I*S.sqrt(3)),(-S.I,S.I*S.sqrt(3)),(-1,2*S.sqrt(3))]:
 # Q_n(center+displacement/n)=O(n^2) because the n^3 and n leading contributions cancel.
 pp=(n**3/96+n**2/8)*F+n*B/96
 expr=S.together(z**4*pp.subs(x,z+1/z))
 assert S.simplify(S.limit(expr.subs(z,center+displacement/n)/n,n,S.oo))==0,(center,'first-order root balance')
r=-2+S.sqrt(3)
c=17*S.sqrt(3)-S.Rational(51,2)
assert S.simplify(c*(1-1/r**2)+51)==0
print('All symbolic collision and Taylor-balance checks PASS')
