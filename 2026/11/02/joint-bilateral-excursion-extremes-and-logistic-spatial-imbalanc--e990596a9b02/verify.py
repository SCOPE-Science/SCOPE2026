import math

def hyp0f1(b,z):
    term=1.0;s=1.0
    for k in range(1,2000):
        term*=z/(k*(b+k-1));s+=term
        if abs(term) < 4e-16*abs(s):return s
    raise ArithmeticError('no convergence')

def eo(alpha,u,x):
    mu=1/(alpha+2)
    z=mu*mu*u*x**(1/mu)
    return hyp0f1(1-mu,z),x*hyp0f1(1+mu,z)

def H(alpha,u,a,b):
    ea,oa=eo(alpha,u,a);eb,ob=eo(alpha,u,b)
    return (oa+ob)/(ea*ob+eb*oa)

def G(alpha,u,a):
    mu=1/(alpha+2)
    e,o=eo(alpha,u,a)
    k=math.gamma(1-mu)/math.gamma(1+mu)*(mu*math.sqrt(u))**(2*mu)
    return 1/(e+k*o)

def gridH(alpha,u,a,b,h):
    N=round((a+b)/h)
    m=round(b/h)
    assert abs(N*h-a-b)<1e-8 and abs(m*h-b)<1e-8
    # indices interior i=1,...,N-1 at -b+i*h
    di=[];lo=[];up=[];rhs=[]
    def antider(x):return math.copysign(abs(x)**(alpha+1)/(alpha+1),x)
    for i in range(1,N):
        x=-b+i*h; mass=(antider(x+h/2)-antider(x-h/2))/h
        q=1/(h*h*mass)
        di.append(u+2*q);lo.append(-q if i>1 else 0);up.append(-q if i<N-1 else 0)
        rhs.append(q*((i==1)+(i==N-1)))
    for i in range(1,N-1):
        mlt=lo[i]/di[i-1]
        di[i]-=mlt*up[i-1];rhs[i]-=mlt*rhs[i-1]
    sol=[0]*(N-1);sol[-1]=rhs[-1]/di[-1]
    for i in range(N-3,-1,-1):sol[i]=(rhs[i]-up[i]*sol[i+1])/di[i]
    return sol[m-1]

if __name__=='__main__':
    checks=0
    for u in [0.1,0.7,2.5]:
      for a,b in [(0.4,0.7),(1.6,2.4),(2.1,3.7)]:
        k=math.sqrt(u)
        exact=(math.sinh(k*a)+math.sinh(k*b))/math.sinh(k*(a+b))
        got=H(0,u,a,b)
        assert abs(got-exact)<1e-12,(got,exact)
        checks+=1
    for alpha in [0,0.2,0.7,1.5,2]:
      for u in [0.25,1.3]:
        for a,b in [(0.5,1.2),(1.6,2.4),(3,4)]:
          F=H(alpha,u,a,b);ga=G(alpha,u,a);gb=G(alpha,u,b)
          q=ga+gb-F
          assert -1e-12<=q<=2*ga*gb+1e-12,(alpha,u,a,b,q,2*ga*gb)
          assert 0<F<1
          checks+=2
    for alpha in [0,0.5,1,2]:
      u=.7;a=1.6;b=2.4
      expected=H(alpha,u,a,b)
      errors=[abs(gridH(alpha,u,a,b,h)-expected) for h in [.4,.2,.1,.05]]
      print('alpha',alpha,'errors',errors)
      assert errors[-1]<1e-3,(alpha,errors)
      assert errors[-1]<errors[0]
      checks+=2
    for alpha in [0,0.5,1.5,3]:
      for u in [.3,1.1]:
        for a in [0.4,1,2.4]:
          # ODE y'' = u*x^alpha*y (independently of 0F1 expansion)
          h=1e-4
          e,o=eo(alpha,u,a)
          em,om=eo(alpha,u,a-h);ep,op=eo(alpha,u,a+h)
          assert abs((ep-2*e+em)/h**2-u*a**alpha*e)<4e-5*max(1,abs(e))
          assert abs((op-2*o+om)/h**2-u*a**alpha*o)<4e-5*max(1,abs(o))
          checks+=2
    for alpha in [0,0.5,1,2]:
        mu=1/(alpha+2);r=.8
        A_mu=2**mu*math.sqrt(math.pi/2)/math.gamma(1-mu)
        for T in [1e4,1e6,1e8]:
            ell=math.log(A_mu*r*T)
            aT=ell+(.5-mu)*math.log(ell)
            zeta=aT+.3
            level=(zeta/(2*mu*math.sqrt(r)))**(2*mu)
            intensity=r*T*G(alpha,r,level)
            assert abs(intensity-math.exp(-.3))<.15,(alpha,T,intensity)
            checks+=1
    for d in [-2,-.2,0,.7,4]:
        # difference of Gumbels is logistic, integral exp(-x)(1-exp(-exp(d)*x))
        # exact integration of exponential tilt
        c=math.exp(d)
        integrated=1-1/(1+c)
        logistic=1/(1+math.exp(-d))
        assert abs(integrated-logistic)<1e-14
        checks+=1
    print('PASS',checks,'checks')
