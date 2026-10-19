"""Independent numerical checks of exact scalar formulas and large-step asymptotics.

Standard-library only. Finite calculations corroborate, not replace, the
uniform infinite-iteration proof in RESULT.md.
"""
import math
from fractions import Fraction

COUNT=0

def ck(ok, msg):
    global COUNT
    COUNT += 1
    if not ok:
        raise AssertionError(msg)

def norm_sq(v):
    return sum(z*z for z in v)

def field(x, c=1.0, curv=(1.0,), precond=(1.0,)):
    l=math.sqrt(c+sum(a*z*z for a,z in zip(curv,x))/2)
    return tuple(t*a*z/(2*l) for t,a,z in zip(precond,curv,x))

def trajectory(x0,eta,c=1.0,curv=(1.0,),precond=(1.0,),steps=60):
    x=tuple(x0)
    r=math.sqrt(c+sum(a*z*z for a,z in zip(curv,x0))/2)
    out=[(x,r)]
    for _ in range(steps):
        v=field(x,c,curv,precond)
        rnew=r/(1+2*eta*norm_sq(v))
        xnew=tuple(z-2*eta*rnew*w for z,w in zip(x,v))
        energy_residual = r*r-rnew*rnew-(r-rnew)**2-sum((zn-z)**2 for zn,z in zip(xnew,x))/eta
        ck(abs(energy_residual)<2e-12*max(1,r*r), 'energy identity')
        ck(rnew>=0 and rnew<=r, 'monotone auxiliary energy')
        out.append((xnew,rnew))
        x,r=xnew,rnew
    return out

def leading(x0,c,curv,precond):
    r0=math.sqrt(c+sum(a*z*z for a,z in zip(curv,x0))/2)
    v0=field(x0,c,curv,precond)
    n0=norm_sq(v0)
    star=tuple(z-r0*v/n0 for z,v in zip(x0,v0))
    vstar=field(star,c,curv,precond)
    ns=norm_sq(vstar)
    lead=tuple(r0/(2*n0)*(v/n0-vs/ns) for v,vs in zip(v0,vstar))
    return star,lead

# First-step rational identity: scalar c=1, x0=1.
for eta in [Fraction(16),Fraction(19),Fraction(100),Fraction(10_000)]:
    eta=float(eta)
    x1,r1=trajectory((1.0,),eta,steps=1)[-1]
    ck(abs(x1[0]-(3-2*eta)/(3+eta))<1e-12,'first-step location')
    ck(abs(r1-3*math.sqrt(1.5)/(eta+3))<1e-12,'first-step energy')

# Exact trapping bounds for the canonical strongly convex example.
for eta in [16,17,20,25,50,100,1000,10000,100000]:
    data=trajectory((1.0,),eta,steps=60)
    xs=[row[0][0] for row in data]
    ck(all(-2 < z < -1 for z in xs[1:]),f'trap failed {eta}')
    ck(all(xs[i]<=xs[i+1]+1e-13 for i in range(1,len(xs)-1)),'monotone after first step')
    xinf=xs[-1]
    ck(-2+9/(eta+3)-1e-12 <= xinf <= -2+18/(eta+3)+1e-12,'interval')
    ck(data[-1][1]<1e-10,'energy depletion')

C=9+9*math.sqrt(2)/2
for eta in [100,1000,10000,100000,1000000]:
    inf=trajectory((1.0,),eta,steps=60)[-1][0][0]
    ck(abs(eta*(inf+2)-C)<200/eta,'first order scalar asymptotic')

# Preconditioned, anisotropic two-dimensional quadratic.
curv=(1.,4.); precond=(1.,0.5); x0=(1.,1.); c=1.
star,a=leading(x0,c,curv,precond)
ck(all(abs(s-t)<1e-12 for s,t in zip(star,(-0.4,-1.8))),'vector jump')
for eta in [100,1000,10000,100000]:
    xinf=trajectory(x0,eta,c,curv,precond,steps=60)[-1][0]
    ck(max(abs(eta*(z-s)-l) for z,s,l in zip(xinf,star,a))<300/eta,'vector first-order')

# Exact rational telescope for constant field: jump map is the endpoint for all eta.
for eta in [Fraction(1,3),Fraction(2),Fraction(101,7)]:
    r=Fraction(3); x=(Fraction(1),Fraction(2)); v=(Fraction(1),Fraction(2))
    for _ in range(50):
        rn=r/(1+2*eta*5)
        xn=tuple(z-2*eta*rn*w for z,w in zip(x,v))
        ck(all(z0-z1 == (Fraction(3)-rn)*w/5 for z0,z1,w in zip((Fraction(1),Fraction(2)),xn,v)), 'constant-field telescoping')
        x,r=xn,rn
print(f'PASS {COUNT} deterministic scalar/vector/rational checks')
print(f'scalar asymptotic coefficient {C:.12f}')
print('large-step limit: x_infinity -> -2; energy -> 0; gradient -> -2')
