"""Exact checks for the dichotomous-force oscillator's fourth-cumulant phase diagram.

Requires Python 3 and SymPy; numerical root display additionally uses mpmath.
The inequalities in the accompanying proof, not numerical root finding,
establish the global phase diagram.
"""
import sympy as s
from functools import lru_cache

eta, k, gamma = s.symbols('eta k gamma', positive=True)
h, g = s.symbols('h g', positive=True)
A = s.symbols('A', positive=True)
assertion_count = 0

def check(test, label):
    global assertion_count
    if test is not True and test != s.true:
        raise AssertionError(label)
    assertion_count += 1

@lru_cache(maxsize=None)
def moments(N):
    # (i,j,flag) is E[x**i*v**j*sigma**flag], where flag=0 or 1.
    # Symmetry forces flag==(i+j)%2 for nonzero moments.
    ans={(0,0,0): s.Integer(1)}
    for d in range(1,N+1):
        ids=[(i,d-i,d%2) for i in range(d+1)]
        vars_=s.symbols('z0:'+str(d+1))
        symbols=dict(zip(ids,vars_))
        equations=[]
        for (i,j,flag) in ids:
            rhs=s.Integer(0)
            if i:
                rhs+=i*symbols.get((i-1,j+1,flag),0)
            if j:
                rhs+=j*ans[(i,j-1,1-flag)]
                rhs-=j*eta*symbols[(i,j,flag)]
                rhs-=j*k*symbols[(i+1,j-1,flag)]
            if flag:
                rhs-=2*gamma*symbols[(i,j,flag)]
            equations.append(rhs)
        mat,vec=s.linear_eq_to_matrix(equations, vars_)
        solution=mat.inv()*vec
        for key,val in zip(ids,solution):
            ans[key]=s.factor(val)
    return ans

m=moments(4)
variance=s.factor(m[(2,0,0)])
fourth=s.factor(m[(4,0,0)])
cumulant=s.factor(fourth-3*variance**2)
P=(18*h**5+33*h**3+12*h
   +g*(138*h**4+238*h**2-18)
   +g**2*(408*h**3+448*h)
   +g**3*(576*h**2+208)
   +384*h*g**4+96*g**5)
positive_den=h*(3*h**2+4)*(1+2*h*g+4*g**2)**2*(9+6*h*g+4*g**2)*(1+2*h**2+6*h*g+4*g**2)
normalized_cumulant=-6*P/positive_den
check(s.simplify(variance-(eta+2*gamma)/(eta*k*(k+2*eta*gamma+4*gamma**2)))==0,'variance')
check(s.simplify(cumulant-normalized_cumulant.subs({h:eta/s.sqrt(k),g:gamma/s.sqrt(k)})/k**4)==0,'cumulant factorization')
check(s.simplify(s.limit(normalized_cumulant,g,0)+2)==0,'zero-flip fourth cumulant')
check(s.simplify(s.limit(normalized_cumulant,g,s.oo))==0,'fast-flip fourth cumulant')
check(s.expand(s.diff(P,g,2)-16*(120*g**3+288*g**2*h+216*g*h**2+78*g+51*h**3+56*h))==0,'strict convexity')
check(s.expand(s.diff(P,h)-(384*g**4+1152*g**3*h+1224*g**2*h**2+448*g**2+552*g*h**3+476*g*h+90*h**4+99*h**2+12))==0,'strict damping monotonicity')
check(s.simplify(P.subs({h:s.Rational(1,50),g:s.Rational(1,10)}))==-s.Rational(48852449,39062500),'strict positive-cumulant witness')
check(P.subs({h:s.Rational(21,250),g:s.Rational(11,100)})<0,'lower threshold bracket')
h1=s.Rational(17,200)
g1=s.Rational(11,100)
f=P.subs(h,h1)
f0=s.diff(P,g,2).subs({h:h1,g:0})
# Since P_gg(g)>=P_gg(0)>0 on g>=0, a global quadratic support bound gives
# min(P)>=P(g1)-P_g(g1)^2/(2P_gg(0)).
cert=s.factor(f.subs(g,g1)-s.diff(f,g).subs(g,g1)**2/(2*f0))
check(cert>0,'upper threshold bracket')
check(s.factor(P.subs(g,0))==3*h*(3*h**2+4)*(2*h**2+1),'positive at zero flip')
check(s.expand(P.subs(h,1)).coeff(g,1)>0,'positive P for h>=1')
# Independently replay stationary-generator identities at every degree.
for q in (s.Rational(1,50),s.Rational(1,10),s.Rational(1,2),s.Integer(1)):
 for r in (s.Rational(1,100),s.Rational(1,7),s.Rational(1,2),s.Integer(2)):
  for kk in (s.Rational(1,2),s.Integer(1),s.Integer(3)):
   subs={eta:q,gamma:r,k:kk}
   for d in range(1,5):
    for i in range(d+1):
     j=d-i;flag=d%2
     rhs=s.Integer(0)
     if i: rhs+=i*m[(i-1,j+1,flag)]
     if j:
      rhs+=j*m[(i,j-1,1-flag)]
      rhs-=j*eta*m[(i,j,flag)]
      rhs-=j*k*m[(i+1,j-1,flag)]
     if flag:rhs-=2*gamma*m[(i,j,flag)]
     check(s.cancel(rhs.subs(subs))==0,f'generator residual ({q},{r},{kk},{i},{j},{flag})')

if __name__=='__main__':
    import mpmath as mp
    mp.mp.dps=55
    fmp=s.lambdify((h,g),P,'mpmath')
    fgp=s.lambdify((h,g),s.diff(P,g),'mpmath')
    hc,gc=mp.findroot((fmp,fgp),('0.085','0.11'))
    print('Assertions passed:', assertion_count)
    print('Critical damping ratio h_c =',mp.nstr(hc,50))
    print('Critical flip ratio g_c =',mp.nstr(gc,50))
    print('Exact bracket: 21/250 < h_c < 17/200')
    print('Global upper bracket positivity certificate:',cert)
    print('Fourth cumulant expression verified exactly.')
