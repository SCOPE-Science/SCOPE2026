"""Independent algebraic/numerical checks of the two-tumbling-rate stationary profiles.

Uses only the Python standard library. Finite checks are not a substitute for proof.
Run: python verify.py
"""
import math

N = 0

def close(a, b, atol=5e-9, rtol=5e-9):
    global N
    assert math.isfinite(a) and math.isfinite(b), (a,b)
    assert abs(a-b) <= atol + rtol*max(abs(a),abs(b)), (a,b,abs(a-b))
    N += 1

def truth(condition):
    global N
    assert condition
    N+=1

def pars(M, r, ag, al, v0, rm):
    cg=math.sqrt(r*(r+ag))/v0
    cl=math.sqrt(r*(r+al))/v0
    beta=cl/cg
    mu=M*cg/2
    assert mu>1 and rm>4
    A=beta*mu
    u=math.log((A+math.sqrt(1+beta*beta*(mu*mu-1)))/(1+beta))
    b=u/(rm*cl)
    eg=math.sqrt(r/(r+ag))
    el=math.sqrt(r/(r+al))
    yb=rm/2*(1-math.sqrt(1-4/rm))
    return locals()

def liquid(p, x):
    z=p['u']-p['rm']*p['cl']*x
    rho=p['rm']*(math.cosh(z)+p['beta']*math.sinh(z))
    sig=p['rm']*p['el']*(math.sinh(z)+p['beta']*math.cosh(z))
    drho=-p['rm']**2*p['cl']*(math.sinh(z)+p['beta']*math.cosh(z))
    dsig=-p['rm']**2*p['cl']*p['el']*(math.cosh(z)+p['beta']*math.sinh(z))
    return rho,sig,drho,dsig

def gas(p, h):
    # Solve log(rho/yb) - 2(rho-yb)/rm = -cg*h monotonically in log rho.
    yb=p['yb']; rm=p['rm']; rhs=-p['cg']*h
    l=-1000.0; z=0.0
    for _ in range(95):
        mid=(l+z)*0.5
        val=mid-2*yb*(math.exp(mid)-1)/rm
        if val<rhs:l=mid
        else:z=mid
    rho=yb*math.exp((l+z)*0.5)
    sig=p['eg']*rho
    drho=-p['cg']*rho/(1-2*rho/rm)
    dsig=p['eg']*drho
    return rho,sig,drho,dsig

def simpson(f,a,b,n=2000):
    h=(b-a)/n
    return (f(a)+f(b)+4*sum(f(a+(2*i+1)*h) for i in range(n//2))
            +2*sum(f(a+2*i*h) for i in range(1,n//2)))*h/3

for M,r,ag,v0,rm in [(10.,.7,1.2,1.3,7.),(17.,1.5,.5,.8,10.),(5.,.9,.8,1.2,6.)]:
    cg=math.sqrt(r*(r+ag))/v0
    M=max(M,3/cg)
    Bs=[]
    for al in [.15,.6,ag,5.,35.]:
        p=pars(M,r,ag,al,v0,rm)
        Bs.append(p['b'])
        u=p['u'];beta=p['beta'];mu=p['mu']
        close(math.sinh(u)+beta*math.cosh(u),beta*mu)
        close(liquid(p,p['b'])[0],rm)
        close(p['yb']*(1-p['yb']/rm),1)
        rho,sig,*_=liquid(p,p['b'])
        close(v0*sig/rm, v0*p['eg'])
        close(p['rm']*p['el']*beta,p['rm']*p['eg'])
        close(liquid(p,0)[1]*v0/rm,r*M/2)
        close(2*(math.sinh(u)+beta*(math.cosh(u)-1))/p['cl'],M-2/p['cg'])
        for f in [.0,.17,.51,.93,1.]:
            x=f*p['b']
            rho,sig,dr,ds=liquid(p,x)
            truth(0<=sig<=rho)
            close((v0/rm)*ds,-r*rho)
            close((v0/rm)*dr,-(r+al)*sig)
        for h in [0.,.2/p['cg'],.8/p['cg'],2./p['cg']]:
            rho,sig,dr,ds=gas(p,h)
            truth(0<sig<rho<rm/2)
            close(v0*p['eg']*(1-2*rho/rm)*dr,-r*rho)
            close(v0*(1-2*rho/rm)*dr,-(r+ag)*sig)
        # Integration of gas half-mass; 50 decay lengths bound truncation error.
        gi=simpson(lambda h:gas(p,h)[0],0,45/p['cg'])
        close(gi,1/p['cg'],atol=2e-6,rtol=2e-6)
    # first rates below ag are ordered, with possible repetition if ag matches an entry
    sorted_pairs=sorted(zip([.15,.6,ag,5.,35.],Bs))
    for (_,left),(_,right) in zip(sorted_pairs,sorted_pairs[1:]):
        truth(left>right)
    # homogeneous-tumbling formula
    p=pars(M,r,ag,ag,v0,rm)
    close(p['b'],math.log(p['mu'])/(rm*cg))
    for al in [1e3,1e5,1e7]:
        p=pars(M,r,ag,al,v0,rm)
        u0=math.acosh(p['mu'])
        close(p['u'],u0,atol=2/math.sqrt(al),rtol=0)
        close(p['b']*rm*p['cl'],u0,atol=2/math.sqrt(al),rtol=0)
        close(liquid(p,0)[0]/(rm*p['beta']),math.sinh(u0),atol=2/math.sqrt(al),rtol=0)
        for q in [.2,.6,.9]:
            y=q*u0
            if y<p['u']:
                close(liquid(p,y/(rm*p['cl']))[0]/(rm*p['beta']),math.sinh(u0-y),atol=2/math.sqrt(al),rtol=0)
print(f'PASS {N} independent finite checks; all three parameter families and singular limits. No infinite proof claimed.')
