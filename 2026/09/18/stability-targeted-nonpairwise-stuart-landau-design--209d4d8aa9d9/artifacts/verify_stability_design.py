import sympy as sp

# Symbols and the unweighted all-to-all three-oscillator phase model of
# arXiv:2609.20632v1, Eq. (21), specialized to straight isochrones.
t1,t2,t3,rho,eps,a,eta=sp.symbols('t1 t2 t3 rho eps a eta', real=True)

def field(ti,tj,tk):
    f1=sp.sin(tj-ti+rho)+sp.sin(tk-ti+rho)
    Cijji=sp.sin(2*rho)+sp.sin(2*(tj-ti))
    Cijjk=sp.sin(tk-ti+2*rho)+sp.sin(2*tj-tk-ti)
    Cikki=sp.sin(2*rho)+sp.sin(2*(tk-ti))
    Cikkj=sp.sin(tj-ti+2*rho)+sp.sin(2*tk-tj-ti)
    Dijij=sp.sin(2*(tj-ti)+2*rho)
    Dijk=sp.sin(tj+tk-2*ti+2*rho)
    Dikik=sp.sin(2*(tk-ti)+2*rho)
    f2=(Cijji+Cijjk+Cikki+Cikkj-Dijij-2*Dijk-Dikik)/(4*a)
    fpn=(-sp.sin(2*tj-tk-ti)-sp.sin(2*tk-tj-ti)
         +sp.sin(tj+tk-2*ti+2*rho))
    return eps*f1+eps**2*f2+eta*fpn

F=sp.Matrix([field(t1,t2,t3),field(t2,t3,t1),field(t3,t1,t2)])
J=F.jacobian([t1,t2,t3])

# Synchrony: the two transverse eigenvalues are equal.
Js=sp.simplify(J.subs({t1:0,t2:0,t3:0}))
lam_sync=sp.simplify(Js[0,0]-Js[0,1])
expected_sync=-3*eps*sp.cos(rho)+(6*eta-sp.Rational(9,2)*eps**2/a)*sp.sin(rho)**2
assert sp.simplify(sp.trigsimp(lam_sync-expected_sync))==0

# Splay: the Jacobian is circulant.  The real part of either nontrivial
# conjugate eigenvalue is d-(p+q)/2 for first row (d,p,q).
Jp=sp.simplify(J.subs({t1:0,t2:2*sp.pi/3,t3:4*sp.pi/3}))
d,p,q=Jp[0,0],Jp[0,1],Jp[0,2]
re_splay=sp.simplify(sp.trigsimp(d-(p+q)/2))
im_splay=sp.simplify(sp.trigsimp(sp.sqrt(3)*(p-q)/2))
expected_re=(sp.Rational(3,2)*eps*sp.cos(rho)+6*eta*sp.sin(rho)**2
             +sp.Rational(9,8)*eps**2/a*sp.cos(2*rho))
expected_im=-sp.Rational(3,4)*eps*(2*a+3*eps*sp.cos(rho))*sp.sin(rho)/a
assert sp.simplify(sp.trigsimp(re_splay-expected_re))==0
assert sp.simplify(sp.trigsimp(im_splay-expected_im))==0

# Simultaneous marginality.  x=cos(rho); eliminate eta from the two real
# stability conditions.
x=sp.symbols('x', real=True)
Ls=-3*eps*x+(6*eta-sp.Rational(9,2)*eps**2/a)*(1-x**2)
Lp=sp.Rational(3,2)*eps*x+6*eta*(1-x**2)+sp.Rational(9,8)*eps**2/a*(2*x**2-1)
eta_sync=sp.solve(sp.Eq(Ls,0),eta)[0]
eliminated=sp.factor(Lp.subs(eta,eta_sync))
expected_elim=-sp.Rational(9,8)*eps*(-4*a*x+2*eps*x**2-3*eps)/a
assert sp.simplify(eliminated-expected_elim)==0

xstar=(a-sp.sqrt(a**2+sp.Rational(3,2)*eps**2))/eps
etastar=sp.simplify(eps*xstar/(2*(1-xstar**2))+sp.Rational(3,4)*eps**2/a)
assert sp.simplify((-4*a*x+2*eps*x**2-3*eps).subs(x,xstar))==0
assert sp.simplify(Ls.subs({x:xstar,eta:etastar}))==0
assert sp.simplify(Lp.subs({x:xstar,eta:etastar}))==0

r=sp.symbols('r', positive=True)
xs=(1-sp.sqrt(1+sp.Rational(3,2)*r**2))/r
etas=sp.simplify(r*xs/(2*(1-xs**2))+sp.Rational(3,4)*r**2)
print('lambda_sync =', expected_sync)
print('Re(lambda_splay) =', expected_re)
print('Im(lambda_splay) =', expected_im)
print('x_* =', xstar)
print('eta_* =', etastar)
print('x_* series (a=1, eps=r):', sp.series(xs,r,0,6))
print('eta_* series (a=1, eps=r):', sp.series(etas,r,0,6))
print('rho_* series (a=1, eps=r):', sp.series(sp.acos(xs),r,0,5))

for E in (sp.Rational(1,20),sp.Rational(1,10),sp.Rational(3,20)):
    xv=sp.N(xs.subs(r,E),16)
    ev=sp.N(etas.subs(r,E),16)
    rv=sp.N(sp.acos(xs.subs(r,E)),16)
    print(f'eps/a={float(E):.3f}: x*={xv}, eta*/a={ev}, rho*={rv}')
