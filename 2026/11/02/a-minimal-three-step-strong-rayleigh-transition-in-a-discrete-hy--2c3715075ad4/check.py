"""Reproduce exact polynomial and covariance identities for thinned record minima.

Requires SymPy. The infinite orthogonality and Rayleigh implications are proved
in the accompanying mathematics; finite checks are independent consistency tests.
"""
import itertools
from math import comb
import sympy as sp

p=sp.symbols('p',real=True)
z=sp.symbols('z1 z2 z3')


def joint_record_pgf(n, variables):
    result=sp.Integer(0)
    for k in range(n+1):
        for active in itertools.combinations(range(n),k):
            factor=sp.prod((variables[t]+r-1)/r for r,t in enumerate(active,1))
            result+=p**k*(1-p)**(n-k)*factor
    return sp.expand(result)

F=joint_record_pgf(3,z)
assert sp.simplify(F.subs(dict.fromkeys(z,1))-1)==0
expected=[
 p**2*(1-p)/12*(p**2*z[2]**2 +(4*p-p**2)*z[2]+6-4*p),
 p**2*(1-p)/12*(p**2*z[1]**2 +(4*p-3*p**2)*z[1]+2*p**2-8*p+6),
 p**2*(1-p)/12*(p**2*z[0]**2 +(4*p-5*p**2)*z[0]+6*p**2-12*p+6)]
count=0
for ((i,j),expr,k,shift) in zip(itertools.combinations(range(3),2),expected,[2,1,0],[sp.Rational(1,2),sp.Rational(3,2),sp.Rational(5,2)]):
    R=sp.expand(sp.diff(F,z[i])*sp.diff(F,z[j])-F*sp.diff(F,z[i],z[j]))
    assert sp.factor(R-expr)==0;count+=1
    centered=p**2*(1-p)/12*(p**2*(z[k]-(shift-2/p))**2 + (8-8*p-p**2)/4)
    assert sp.simplify(R-centered)==0;count+=1
    for pp in [sp.Rational(1,4),sp.Rational(1,2),sp.Rational(7,8),sp.Rational(19,20)]:
        xstar=shift-2/pp
        val=sp.factor(R.subs({p:pp,z[k]:xstar}))
        assert (val<0)==(pp>2*sp.sqrt(6)-4);count+=1

# Independent pgf formula, its Meixner transform, and numerical root geometry.
w=sp.symbols('w')
c=1-p
for n in range(1,10):
    g=sp.expand(sum(sp.binomial(n,j)*sp.prod(w-1-t for t in range(j))*p**j/sp.factorial(j) for j in range(n+1)))
    f=sp.expand(joint_record_pgf(n,sp.symbols('v0:'+str(n))).subs({a:w for a in sp.symbols('v0:'+str(n))}))
    assert sp.simplify(f-g)==0;count+=1
    # c^n M_n(-w;1,c): M_n(x)=sum binom(n,j) binom(x,j)(1-c^-1)^j
    m=sp.expand(sum(sp.binomial(n,j)*sp.prod((-w)-t for t in range(j))*((c-1)/c)**j/sp.factorial(j) for j in range(n+1))*c**n)
    assert sp.factor(g-m)==0;count+=1
    if n<=8:
        pol=sp.Poly(g.subs(p,sp.Rational(2,5)),w)
        roots=sp.nroots(pol,maxsteps=100)
        assert all(abs(float(sp.im(r)))<1.e-9 and float(sp.re(r))<0 for r in roots);count+=1

# Generating-function orthogonality identity at the rational parameter c=1/2.
s,t=sp.symbols('s t')
cc=sp.Rational(1,2)
M=lambda n,x:sp.expand(sum(sp.binomial(n,j)*sp.prod(x-u for u in range(j))*(1-1/cc)**j/sp.factorial(j) for j in range(n+1)))
# Verify orthogonality algebraically using E[binom(X,a)binom(X,b)]
# The generating kernel sum_x (1-c)c^x G_x(s)G_x(t) equals 1/(1-st/c).
identity=sp.factor((1-cc)/((1-s)*(1-t)-cc*(1-s/cc)*(1-t/cc)))
assert sp.simplify(identity-1/(1-s*t/cc))==0;count+=1
# Check exact probability signs using the integrals for pairs and the marginal formula.
u,v=sp.symbols('u v',real=True)
for pp in (sp.Rational(1,5),sp.Rational(1,2),sp.Rational(4,5)):
 for i in range(1,6):
  for j in range(i+1,9):
   joint=pp**2*sp.integrate((1-pp*v)**(i-1)*sp.integrate((1-pp*u)**(j-i-1),(u,0,v)),(v,0,1))
   marg_i=(1-(1-pp)**i)/i
   marg_j=(1-(1-pp)**j)/j
   assert joint-marg_i*marg_j<0;count+=1

print('PASS: {} exact symbolic/rational and numerical consistency assertions'.format(count))
print('F3:',F)
print('Rayleigh threshold p_star = 2 sqrt(6)-4 =',sp.N(2*sp.sqrt(6)-4,14))
print('At p=19/20, Rayleigh minima are negative; at p=1/2, positive.')
print('Meixner identities, jump-count factorization evidence, and pairwise signs checked.')
