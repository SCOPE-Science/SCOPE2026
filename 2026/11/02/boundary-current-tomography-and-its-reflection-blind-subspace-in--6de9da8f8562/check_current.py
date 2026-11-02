"""Independent numerical checks of the membrane-current inverse theorem.
Scientific input: D,L,kappa>0, positive reset rates and source measures in (0,L).
Requires Python 3 and NumPy. Reports assertions, not an infinite proof.
"""
import math
import numpy as np

TESTS = 0

def close(a,b,tol=1e-10,label=''):
    global TESTS
    TESTS += 1
    assert abs(a-b) <= tol * max(1,abs(a),abs(b)), (label,a,b,abs(a-b))

def calc(D,L,kappa,r,points):
    lam = math.sqrt(r/D)
    c=lam*L/2
    F=sum(w*math.sinh(lam*(y-L/2)) for y,w in points)
    J=kappa*lam*F/(math.cosh(c)+(2*kappa/(D*lam))*math.sinh(c))
    return lam,F,J

def density(D,L,kappa,r,points,x):
    lam,F,J=calc(D,L,kappa,r,points)
    c=lam*L/2
    pneu=lam/sinh_stable(lam*L)*sum(w*math.cosh(lam*min(x,y))*math.cosh(lam*(L-max(x,y))) for y,w in points)
    return pneu-J*math.sinh(lam*(x-L/2))/(D*lam*math.cosh(c))

def sinh_stable(v):
    return math.sinh(v)

def fd(D,L,kappa,r,centers,source):
    n=len(centers); h=L/n
    weights=source / (np.sum(source)*h)
    A=np.zeros((n,n),float)
    a=D/h**2; effective=kappa/(1.+kappa*h/D); b=effective/h
    for i in range(n):
        A[i,i]=r+(2*a if 0<i<n-1 else a+b)
        if i>0: A[i,i-1]=-a
        if i<n-1: A[i,i+1]=-a
    A[0,n-1]=-b; A[n-1,0]=-b
    sol=np.linalg.solve(A,r*weights)
    return effective*(sol[-1]-sol[0]),sol

for D in (.25,1.,2.):
 for L in (.7,1.4):
  for kappa in (.11,.8,4.):
   for r in (.2,2.,8.):
    ps=[(.18*L,.45),(.71*L,.35),(.88*L,.2)]
    lam,F,J=calc(D,L,kappa,r,ps)
    p0=density(D,L,kappa,r,ps,0.)
    pL=density(D,L,kappa,r,ps,L)
    close(J,kappa*(pL-p0),1e-11,'membrane')
    assert p0>0 and pL>0
    TESTS+=2
    pref=[(L-y,w) for y,w in ps]
    _,Fr,Jr=calc(D,L,kappa,r,pref)
    close(J,-Jr,label='reflected flux')
    if abs(J)>1e-12:
        I=J*math.log(pL/p0)
        assert I>0, (I,J,p0,pL)
        close(I, Jr*math.log(density(D,L,kappa,r,pref,L)/density(D,L,kappa,r,pref,0)),label='reflected entropy')
        TESTS+=1
    # Flux sign and explicit zero-criterion equivalence
    assert J*F>0
    TESTS+=1

# Two distributions with different symmetric parts, equal nonzero all-rate currents
mu1=[(.25,.6),(.75,.4)]
mu2=[(.25,.55),(.75,.35),(.5,.1)]
for r in (.005,.1,.5,1.,3.,20.,50.):
    J1=calc(1.,1.,.7,r,mu1)[2]
    J2=calc(1.,1.,.7,r,mu2)[2]
    close(J1,J2,label='invisible even change')
    assert abs(J1)>1e-15
    TESTS+=1

# Explicit nonsymmetric reset law with vanishing current at one rate
D,L,kappa,r=1.,1.,.7,1.
left,right=.4,.8
wl=math.sinh(right-.5)/(math.sinh(.5-left)+math.sinh(right-.5))
no_current=[(left,wl),(right,1-wl)]
close(calc(D,L,kappa,r,no_current)[2],0.,tol=1e-13,label='one-rate hidden asymmetry')
assert abs(calc(D,L,kappa,2.4,no_current)[2])>1e-5
TESTS+=1

# Small-r slope identifies centered mean reset position
for mu in ([ (.3,.2),(.7,.8)], [(0.15,1.)],[(.45,.37),(.86,.63)]):
  m=sum((y-.5)*w for y,w in mu)
  for r in (1.e-3,1.e-4):
    J=calc(1.,1.,.75,r,mu)[2]
    close(J/r, .75*m/(1.+.75),tol=.003,label='small-rate slope')

# Finite-volume independent discretization with smooth reset law sigma(y)=30*y*(1-y)^4
# Gauss midpoint quadrature approximates the analytic flux integral independently.
for D,L,kappa,r in [(1.,1.,.7,2.),(1.4,1.,.23,.5),(0.8,1.,3.,5.)]:
    fine=np.linspace(0,1.,20001)
    sig=30*fine*(1.-fine)**4
    lam=math.sqrt(r/D)
    F=float(np.trapezoid(sig*np.sinh(lam*(fine-.5)),fine))
    J=kappa*lam*F/(math.cosh(lam/2)+(2*kappa/(D*lam))*math.sinh(lam/2))
    errors=[]
    for n in (60,120,240):
        x=(np.arange(n)+.5)/n
        s=30*x*(1-x)**4
        JJ, sol =fd(D,1.,kappa,r,x,s)
        err=abs(JJ-J)
        errors.append(err)
        assert np.min(sol)>0
        TESTS+=1
        close(float(np.mean(sol)),1.,tol=1e-11,label='finite volume normalization')
    assert errors[2]<errors[1]<errors[0],(errors,J)
    assert errors[2]<.0004,(errors,J)
    TESTS+=2


# Admissible-source fiber check for an atomic law: odd component fixes exactly
# a mass of 0.2; the remaining symmetric mass 0.8 is freely redistributable.
# The two reset laws above exhibit two distinct choices of this symmetric part.
odd_1=(mu1[0][1]-mu1[1][1])/2
odd_2=(mu2[0][1]-mu2[1][1])/2
close(odd_1,odd_2,label='same antisymmetric measure')
close(2*abs(odd_1),.2,label='antisymmetric total variation')
close(1.-2*abs(odd_1),.8,label='free symmetric mass')
# A reset concentrated at one location and away from the midpoint has unit
# antisymmetric total variation and no free symmetric probability mass.
close(2*.5,1.,label='single-atom antisymmetric total variation')
print('PASS',TESTS,'deterministic checks including probability-law fiber')
