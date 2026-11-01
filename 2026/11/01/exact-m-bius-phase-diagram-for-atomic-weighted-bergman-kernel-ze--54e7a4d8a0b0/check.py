"""Independent finite diagnostics for a point-mass weighted Bergman kernel.

Only analytical arguments in the accompanying result establish the global theorem.
Run: python check.py
"""
import cmath
import math
import random

checks = 0

def check(cond, msg=''):
    global checks
    assert cond, msg
    checks += 1


def kernel(lam, mass, z):
    return cmath.exp(-lam * cmath.log(1-z)) - mass/(1+mass)


def entries(lam, mass):
    rho = (1+1/mass)**(1/lam)
    bound = lam / 6
    kmax = math.ceil(bound)-1
    return [(k, 1-rho*cmath.exp(2j*math.pi*k/lam))
            for k in range(-kmax, kmax+1)
            if abs(1-rho*cmath.exp(2j*math.pi*k/lam)) < 1-1e-12]


def predicted_count(lam, mass):
    rho = (1+1/mass)**(1/lam)
    if rho >= 2:
        return 0
    q = lam/(2*math.pi)*math.acos(rho/2)
    return 2*math.ceil(q)-1


def winding(lam, mass, radius=0.99, steps=65536):
    old = kernel(lam, mass, radius)
    angle = 0
    for j in range(1, steps+1):
        val = kernel(lam,mass,radius*cmath.exp(2j*math.pi*j/steps))
        delta=cmath.phase(val/old)
        angle += delta
        old=val
    return round(angle/(2*math.pi))


for lam in [1.5,2.0,2.6,4.5,6.0,6.1,7.5,11.0,12.0,12.5,18.1,21.6,30.5]:
    threshold=1/(2**lam-1)
    for mult in [0.4,0.77,1.23,3,30,1e4]:
        mass=threshold*mult
        roots=entries(lam,mass)
        check(len(roots)==predicted_count(lam,mass), ('count',lam,mass))
        check((len(roots)==0)==(mass<=threshold), ('first zero',lam,mass))
        for k,z in roots:
            check(abs(z)<1)
            check(abs(kernel(lam,mass,z))<3e-11, ('zero',lam,mass,k,z))
            check(abs(cmath.phase(1-z))<math.pi/2)
            if k==0:
                check(abs(z.imag)<1e-12 and z.real<0)
            else:
                check(lam>6)

for lam,mass in [(2,0.4),(2,1.0),(5,0.08),(8,1.5),(8,100),(12.8,1.0),(19,20),(30,10)]:
    check(winding(lam,mass)==predicted_count(lam,mass),('winding',lam,mass))

for lam in [2,6.01,7,9,13.5,21]:
    for k in range(0,math.ceil(lam/6)):
        cosine=math.cos(2*math.pi*k/lam)
        if cosine<=.5: continue
        hk=1/((2*cosine)**lam-1)
        rho=(1+1/hk)**(1/lam)
        z=1-rho*cmath.exp(2j*math.pi*k/lam)
        check(abs(abs(z)-1)<5e-12,('boundary',lam,k))
        for factor in [.93,1.07]:
            m=hk*factor
            newrho=(1+1/m)**(1/lam)
            newz=1-newrho*cmath.exp(2j*math.pi*k/lam)
            check((abs(newz)<1)==(factor>1),('cross',lam,k,factor))
        m=hk
        eps=1e-5*m
        def sqnorm(h):
            r=(1+1/h)**(1/lam)
            return abs(1-r*cmath.exp(2j*math.pi*k/lam))**2
        fd=(sqnorm(m+eps)-sqnorm(m-eps))/(2*eps)
        deriv=-4*cosine**2/(lam*m*(1+m))
        check(abs(fd/deriv-1)<1e-7,('derivative',lam,k))

for lam in [2.2,5.7,6.1,12.1,18.8,33.3,100,300.1]:
    expected=2*math.ceil(lam/6)-1
    check(predicted_count(lam,1e30)==expected,('saturation',lam))

# Check the closed kernel against finite monomial sums at noncritical interior points.
for lam in [1.2,2,3.7,5.2]:
    for z in [0,.2,-.4,.2+.2j,-.33+.45j]:
        mass=.5
        series=1/(1+mass)
        coeff=1.0
        for n in range(1,500):
            coeff*= (lam+n-1)/n
            series+=coeff*z**n
        check(abs(series-kernel(lam,mass,z))<1e-10,('series',lam,z))

# Check the automorphism normalization, including fractional powers.
rand=random.Random(7321)
for lam in [1.2,2.0,3.7,6.4,9.1,18.3]:
    for i in range(100):
        a=complex(rand.uniform(-.42,.42),rand.uniform(-.42,.42))
        z=complex(rand.uniform(-.6,.6),rand.uniform(-.6,.6))
        w=complex(rand.uniform(-.6,.6),rand.uniform(-.6,.6))
        check(max(abs(a),abs(z),abs(w))<1)
        phi=lambda q:(a-q)/(1-a.conjugate()*q)
        bare=lambda x,y:kernel(lam,1e99,x*y.conjugate())
        # Direct rank-one expression uses the unperturbed kernel exactly.
        K0=lambda x,y:cmath.exp(-lam*cmath.log(1-x*y.conjugate()))
        rhoK=K0(z,w)*K0(a,a)/(K0(z,a)*K0(a,w))
        target=cmath.exp(-lam*cmath.log(1-phi(z)*phi(w).conjugate()))
        check(abs(rhoK-target)<2e-10*max(1,abs(target)),('aut',lam,i))
        mu=.01 if i%2==0 else 2.
        h=mu/K0(a,a).real
        pert=K0(z,w)-h*K0(z,a)*K0(a,w)/(1+h*K0(a,a).real)
        pref=K0(z,a)*K0(a,w)/K0(a,a)
        norm=pref*(target-mu/(1+mu))
        check(abs(pert-norm)<2e-10*max(1,abs(pert),abs(norm)),('pert',lam,i))

# Every intrinsic scalar root is realized by genuine points of the disk.
for lam in [2.0,6.2,8.5,12.6,22.3]:
    mu=2
    a=.23+.19j
    phi=lambda q:(a-q)/(1-a.conjugate()*q)
    K0=lambda x,y:cmath.exp(-lam*cmath.log(1-x*y.conjugate()))
    mass=mu/K0(a,a).real
    for k,t in entries(lam,mu):
        v=(1+math.sqrt(abs(t)))/2
        z=phi(t/v)
        w=phi(v)
        check(abs(z)<1 and abs(w)<1)
        check(abs(phi(z)*phi(w).conjugate()-t)<1e-10)
        kh=K0(z,w)-mass*K0(z,a)*K0(a,w)/(1+mass*K0(a,a).real)
        check(abs(kh)<3e-7*max(1,abs(K0(z,w))),('realize',lam,k))

print(f'{checks} deterministic assertions passed')
