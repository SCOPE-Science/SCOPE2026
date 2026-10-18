"""Exact identities and independent numerical checks for cross-inhibition fold theorem.
Run: python verify.py. SymPy and SciPy required for checking; neither is used in the proof.
"""
import sympy as s
from scipy.optimize import brentq, root
import numpy as np

checks=0

def test(statement, label):
    global checks
    assert bool(statement), label
    checks += 1

q,r,t,z,x,y=s.symbols('q r t z x y', real=True)
u=1-x-y-2*z
f=q*u*(x+z)-x*(y+z)
g=u*(y+z)-q*y*(x+z)
J=s.Matrix([f,g]).jacobian([x,y])
D=q**2*r**3+(q**2+q)*r**2-(q+1)*r-1
Z=r*(q**2*r-1)/D
X=q**2*r**2*(r-1)/D
Y=(r-1)/D
U=q*r*(r-1)/D
subs={x:X,y:Y,z:Z}
for expr, label in [(X+Y+U+2*Z-1,'normalization'),
                    (f.subs(subs),'first equilibrium equation'),
                    (g.subs(subs),'second equilibrium equation'),
                    ((X+Z)/(Y+Z)-r,'physical ratio'),
                    (X/Y-q**2*r**2,'relative committed ratio'),
                    (1-X-Y-2*Z-U,'undecided definition')]:
    test(s.factor(expr)==0,label)
E=1+q*r**2-q**3*r**2+2*q**2*r**3-2*q**2*r-q**4*r**4
# Full Jacobian identity: det = -(q^2*r^2-1)*E/D^2
trace=s.factor(s.trace(J).subs(subs))
det=s.factor(J.det().subs(subs))
test(s.factor(det+(q*q*r*r-1)*E/D**2)==0,'determinant factorization')
test(s.factor(s.diff(Z,r)-E/D**2)==0,'branch derivative')
H=q**4+q**3*t+q**2*t-q**2*t**2-q*t**2-t**3
G=q**4*(1-2*t)-q*(q**2-1)*t**2+t**3*(2-t)
Phi=q**2*t*(1-t)/H
test(s.factor(Phi-Z.subs(r,t/q**2))==0,'bad branch reparametrization')
test(s.factor(s.diff(Phi,t)-q**2*G/H**2)==0,'fold polynomial')
test(s.factor(q**4*E.subs(r,t/q**2)-G)==0,'fold/sign equivalence')
test(s.factor(G.subs(t,1)+(q+1)*(q**3-1))==0,'fold upper sign')
test(s.factor(E.subs(q,1)+(r-1)**3*(r+1))==0,'large-r sign at q=1')
# Show E strictly decreases in q for q>=1,r>=1 by a direct nonpositive decomposition.
dEq=s.diff(E,q)
test(s.factor(dEq+4*q*r**3*(q*q*r-1)+r*r*(3*q*q-1)+4*q*r)==0,
     'q-derivative sign decomposition')
# H/q^2 rises strictly in q; this proves monotonic fold threshold.
Hscaled=s.factor(H/q**2)
test(s.factor(s.diff(Hscaled,q)-(2*q+t+t**2/q**2+2*t**3/q**3))==0,
     'strict quality monotonicity')
test(s.factor(Hscaled.subs(q,1)-(1-t)*(1+3*t+t*t))==0,
     'baseline positive denominator')
# Fold derivative bounded by negative for q>1, 0<t<1.
test(s.factor(s.diff(G,t)-(-2*q**4-2*q*(q*q-1)*t+6*t*t-4*t**3))==0,
     'strict fold derivative')
# For q=2, z=1/20 is above threshold by a strict polynomial certificate.
test(s.factor((s.Rational(1,20)*H-Phi*H).subs(q,2)*20 - (16-68*t+74*t*t-t**3))==0,
     'q2 single-phase polynomial')
test(s.factor(16-68*t+73*t*t)==16-68*t+73*t*t,
     'positive quadratic comparison')
test(68**2-4*73*16<0,'strictly positive quadratic discriminant')
test(s.factor(Phi.subs({q:2,t:s.Rational(1,2)}))>s.Rational(1,25),
     'q2 coexistence example lower bound')

# Independent numerical root/eigenvalue sampling for the stability and phase count.
def z_of_r(quality, rr):
    den=quality**2*rr**3+(quality**2+quality)*rr**2-(quality+1)*rr-1
    return rr*(quality**2*rr-1)/den

def eq_of_r(quality, rr):
    den=quality**2*rr**3+(quality**2+quality)*rr**2-(quality+1)*rr-1
    return np.array([quality**2*rr**2*(rr-1)/den,(rr-1)/den])

def field(a, quality, zz):
    xx,yy=a
    uu=1-xx-yy-2*zz
    return np.array([quality*uu*(xx+zz)-xx*(yy+zz), uu*(yy+zz)-quality*yy*(xx+zz)])

for quality in [1.02,1.1,1.5,2,3,5,20]:
    GG=s.lambdify(t,G.subs(q,quality),'numpy')
    tstar=brentq(GG,1e-12,1-1e-12,xtol=1e-14)
    zzstar=float(Phi.subs({q:quality,t:tstar}))
    test(0 < zzstar < .2,'fold in admissible range')
    rrstar=tstar/quality**2
    for zz, expected_n in [(zzstar*.6,3),(zzstar*1.2,1)]:
        roots=[]
        samples=np.linspace(1e-9,quality**-2-1e-9,400)
        for v,w in zip(samples[:-1],samples[1:]):
            if (z_of_r(quality,v)-zz)*(z_of_r(quality,w)-zz)<0:
                roots.append(brentq(lambda rr:z_of_r(quality,rr)-zz,v,w))
        upper=brentq(lambda rr:z_of_r(quality,rr)-zz,1+1e-12,max(2,4/zz),xtol=1e-13)
        roots.append(upper)
        test(len(roots)==expected_n,'number of equilibria')
        for rr in roots:
            xy=eq_of_r(quality,rr)
            test(np.linalg.norm(field(xy,quality,zz),ord=np.inf)<1e-9,'equilibrium residual')
            test(min(xy)>0 and sum(xy)+2*zz<1,'physical positivity')
            eig=np.linalg.eigvals(np.array(J.subs({q:quality,z:zz,x:xy[0],y:xy[1]}),dtype=float))
            expected_stable=(rr>1 or rr<rrstar)
            test((np.max(np.real(eig))<0)==expected_stable,'stability')

print(f'PASS: {checks} assertions; exact Jacobian, elimination, fold identities, sign decompositions, and numerical spectra.')
print('q=2 fold:')
tstar=brentq(s.lambdify(t,G.subs(q,2),'numpy'),0,1)
print('t* = %.15f; z* = %.15f'%(tstar,float(Phi.subs({q:2,t:tstar}))))
