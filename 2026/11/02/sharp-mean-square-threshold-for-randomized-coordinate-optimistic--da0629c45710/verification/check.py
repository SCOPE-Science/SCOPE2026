import sympy as S
s,z,l,g=S.symbols('s z l g')
G=S.Rational(9,10); c=S.sqrt(s)
M=S.Matrix([[1+2*s,-4*s*g,2*s*g**2,2*c*g],[1,0,0,c*g],[1,0,0,0],[-c,c*g,0,0]])
P=S.expand(M.charpoly(l).as_expr())
expected=l**4-(1+2*s)*l**3+s*(6*g-3*g*g)*l**2-g*g*s*(1+2*s)*l+2*g**4*s*s
assert S.simplify(P-expected)==0
pp=S.factor(P.subs(l,1)); assert S.simplify(pp-2*s*(g-1)*(g*g*(1+g)*s-2*g+1))==0
s0=S.Rational(800,1539)
assert S.simplify(s0-(2*G-1)/(G*G*(1+G)))==0
w=S.symbols('w'); Q=S.Poly(S.expand((1-w)**4*P.subs({l:(1+w)/(1-w),g:G})).cancel(),w)
a=[S.factor(Q.coeff_monomial(w**j)) for j in range(5)]
d2=S.factor(a[3]*a[2]-a[4]*a[1]);d3=S.factor(a[3]*a[2]*a[1]-a[4]*a[1]**2-a[3]**2*a[0])
r=S.symbols('r',positive=True)
for b in a+[d2,d3]:
    degree=S.Poly(b,s).degree()
    trans=S.Poly(S.cancel((1+r)**degree*b.subs(s,s0*r/(1+r))),r)
    coeffs=trans.all_coeffs()
    assert all(v>=0 for v in coeffs) and any(v>0 for v in coeffs),(b,coeffs)
# Moment GF from exact matrix; denominator and numerator rational in the squared step (square roots cancel)
M0=M.subs(g,G)
a0=S.Matrix([1,1,1,0]); Z=S.simplify((S.eye(4)-z*M0).inv()[0,:].dot(a0))
D=S.factor((S.eye(4)-z*M0).det()); N=S.factor(Z*D)
assert S.simplify(Z-N/D)==0
res=S.factor(S.resultant(S.Poly(D,z),S.Poly(N,z),z))
assert res != 0
crit=S.factor(S.limit((1-z)*Z.subs(s,s0),z,1,dir='-'))
assert crit==S.Rational(1089,3217),crit
# deterministic Schur for t=3/4, g=9/10 (roots in disk)
t=S.Rational(3,4); g0=G
A=-1+S.I*t;B=-S.I*t*g0
abs2=lambda q:S.expand_complex(q*S.conjugate(q)).simplify()
assert abs2(B)<1 and S.simplify((1-abs2(B))**2-abs2(A-S.conjugate(A)*B))>0
# Exact brute-force enumerated update of the first 6 steps for a generic vector
T=S.Rational(3,4); JJ=S.Matrix([[0,-1],[1,0]])
def nxt(x,y,i):
  Pj=S.diag(1,0) if i==0 else S.diag(0,1)
  return S.simplify(x-2*T*Pj*JJ*(x-G*y))
states=[(S.Matrix([1,2]),S.Matrix([1,2]),S.Rational(1))]
mm=M0.subs(s,T*T);mom=S.Matrix([5,5,5,0])
for k in range(7):
  b=sum([prob*(x.dot(x)) for x,y,prob in states]);assert b==mom[0],(k,b,mom[0])
  ss=[]
  for x,y,prob in states:
   for i in (0,1):ss.append((nxt(x,y,i),x,prob/2))
  states=ss;mom=mm*mom
print('VERIFY_OK exact moment recurrence, quartic, seven Hurwitz certificate families, pole and critical residue, deterministic Schur, 7 exact finite trees', 's0=',s0,'crit=',crit)
