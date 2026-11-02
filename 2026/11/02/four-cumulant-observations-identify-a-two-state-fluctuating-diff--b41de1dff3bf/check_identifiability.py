"""Independent ODE checks for a two-state switching-diffusivity observation law.

Run: python3 check_identifiability.py
No third-party dependencies. Proof of global injectivity is in RESULT.md.
"""
import math
import random


def f(z):
    # Cancellation-safe for tiny z.
    if abs(z)<0.001:
        return sum(((-z)**j)/math.factorial(j+2) for j in range(9))
    return (z+math.expm1(-z))/(z*z)


def g(z):
    if abs(z)<0.001:
        return sum(((-z)**j)*(j+1)/math.factorial(j+3) for j in range(9))
    return (z-2+(z+2)*math.exp(-z))/(z**3)


def analytic(dm,dp,alpha,beta,t):
    lam=alpha+beta
    p=alpha/lam
    delta=dp-dm
    mu=dm+p*delta
    w=p*(1-p)*delta**2
    c=p*(1-p)*(1-2*p)*delta**3
    return 2*mu*t,24*w*t*t*f(lam*t),720*c*t**3*g(lam*t)


def integrate_moments(dm,dp,alpha,beta,t,steps=1900):
    lam=alpha+beta
    p=alpha/lam
    y=[1-p,p]+[0.0]*6
    dt=t/steps
    def rhs(y):
        out=[0.0]*8
        for n in range(4):
            i=2*n
            out[i]=-alpha*y[i]+beta*y[i+1]
            out[i+1]=alpha*y[i]-beta*y[i+1]
            if n:
                out[i]+=n*dm*y[i-2]
                out[i+1]+=n*dp*y[i-1]
        return out
    for _ in range(steps):
        k1=rhs(y)
        k2=rhs([v+dt*a/2 for v,a in zip(y,k1)])
        k3=rhs([v+dt*a/2 for v,a in zip(y,k2)])
        k4=rhs([v+dt*a for v,a in zip(y,k3)])
        y=[v+dt*(a+2*b+2*c+d)/6 for v,a,b,c,d in zip(y,k1,k2,k3,k4)]
    m1=y[2]+y[3]; m2=y[4]+y[5]; m3=y[6]+y[7]
    var=m2-m1*m1
    third=m3-3*m1*m2+2*m1**3
    return 2*m1,12*var,120*third


def invert(k2a,k4a,k4b,k6a,ta,tb):
    assert 0<ta<tb and k4a>0 and k4b>0
    ratio=(k4a/ta**2)/(k4b/tb**2)
    if not 1<ratio<tb/ta:
        raise ValueError('inconsistent noiseless data')
    lo=0.0; hi=1.0
    while f(hi*ta)/f(hi*tb)<ratio: hi*=2
    for _ in range(100):
        mid=(lo+hi)*0.5
        if f(mid*ta)/f(mid*tb)<ratio:lo=mid
        else:hi=mid
    lam=(lo+hi)*0.5
    w=k4a/(24*ta**2*f(lam*ta))
    c=k6a/(720*ta**3*g(lam*ta))
    mu=k2a/(2*ta)
    delta=math.sqrt((c/w)**2+4*w)
    p=(1-c/(w*delta))/2
    return mu-p*delta,mu+(1-p)*delta,lam*p,lam*(1-p)


def check():
    # All comparisons use a Markov-generator moment hierarchy rather than
    # the conditional three-time correlation proof from the theorem.
    random.seed(410026)
    checks=0
    for _ in range(75):
        dm=random.uniform(.15,2.0)
        dp=dm+random.uniform(.25,3.0)
        alpha=random.uniform(.3,3.0)
        beta=random.uniform(.3,3.0)
        t=random.uniform(.16,2.2)
        exact=analytic(dm,dp,alpha,beta,t)
        ode=integrate_moments(dm,dp,alpha,beta,t)
        for a,b in zip(exact,ode):
            assert abs(a-b)<=5e-7*max(1.0,abs(a),abs(b)),(a,b,dm,dp,alpha,beta,t)
            checks+=1
        t1=random.uniform(.2,.85)
        t2=t1+random.uniform(.5,2.5)
        k2,k4a,k6=analytic(dm,dp,alpha,beta,t1)
        k4b=analytic(dm,dp,alpha,beta,t2)[1]
        recon=invert(k2,k4a,k4b,k6,t1,t2)
        for original,rec in zip((dm,dp,alpha,beta),recon):
            assert abs(original-rec)<1e-6*max(1.,original), (original,rec)
            checks+=1
    # A one-parameter family of physically admissible models with
    # identical second/fourth cumulants for all times but different sixth.
    mu=2.0; w=.4; lam=1.7
    family=[]
    for p in (.15,.3,.48,.6):
        delta=math.sqrt(w/(p*(1-p)))
        dm=mu-p*delta
        dp=dm+delta
        alpha,beta=lam*p,lam*(1-p)
        assert dm>0
        family.append((dm,dp,alpha,beta))
    for x in family[1:]:
        for t in (.3,1.1,2.7):
            base=analytic(*family[0],t)
            test=analytic(*x,t)
            assert abs(base[0]-test[0])<1e-12
            assert abs(base[1]-test[1])<1e-12
            assert abs(base[2]-test[2])>1e-3
            checks+=3
    # Monotonicity of the elasticity of f and the finite-time ratio.
    for i in range(1,251):
        z=i/80
        # 2*cosh(z) - z^2 - 2 positive for z>0.
        assert 2*(math.cosh(z)-1)>z*z
        checks+=1
    print('PASS:',checks,'independent numerical assertions')
    print('Example:', 'model',family[0], 'four observations',
          (analytic(*family[0],.5)[0],analytic(*family[0],.5)[1],
           analytic(*family[0],1.25)[1],analytic(*family[0],.5)[2]))

if __name__=='__main__':check()
