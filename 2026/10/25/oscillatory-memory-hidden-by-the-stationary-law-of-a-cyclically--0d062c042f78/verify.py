import cmath,math
alpha=lambda nu:1.5*nu
beta=lambda nu:math.sqrt(3)*nu/2

def cov_closed(t,r,nu,D,a):
    lam=complex(1.5*nu,-math.sqrt(3)*nu/2)
    z=(cmath.exp(-lam*t)-math.exp(-r*t))/(r*r-lam*lam)
    return (a*a+4*D/r)*math.exp(-r*t)+a*a*r*r*z.real

def cov_numeric(t,r,nu,D,a,n=10000):
    # independent Simpson quadrature of original conditioning over last event time
    if t==0: return a*a+4*D/r
    dt=t/n
    z0=complex(1.5*nu,-math.sqrt(3)*nu/2)
    k=r/(r+z0)
    def f(s):return r*math.exp(-r*(t-s))*(k*cmath.exp(-z0*s)).real
    total=f(0)+f(t)
    for j in range(1,n):total+=(4 if j%2 else 2)*f(j*dt)
    return (a*a+4*D/r)*math.exp(-r*t)+a*a*total*dt/3

def rk4_cov(t,r,nu,D,a,steps=2000):
    w=complex(-.5,math.sqrt(3)/2)
    vs=[a*w**j for j in range(3)]
    k=r/(r+complex(1.5*nu,math.sqrt(3)*nu/2))
    initial_g=[k*v/3 for v in vs]
    initial_f=[(a*a+4*D/r)/3]*3
    state=initial_g+initial_f
    dt=t/steps
    def deriv(state):
        gg, ff=state[:3],state[3:]
        dg=[nu*(gg[(j-1)%3]-gg[j]) for j in range(3)]
        df=[nu*(ff[(j-1)%3]-ff[j])-r*ff[j]+r*(gg[j]*vs[j].conjugate()).real for j in range(3)]
        return dg+df
    def add(x,y,c):return [u+c*v for u,v in zip(x,y)]
    for _ in range(steps):
        k1=deriv(state);k2=deriv(add(state,k1,dt/2));k3=deriv(add(state,k2,dt/2));k4=deriv(add(state,k3,dt))
        state=[u+dt*(a+2*b+2*c+d)/6 for u,a,b,c,d in zip(state,k1,k2,k3,k4)]
    return sum(state[3:]).real

if __name__=='__main__':
    checks=0
    maxerr=0.0
    # Three independently implemented evaluations: resolvent, direct
    # Poisson-time quadrature, and Markov-generator moment evolution.
    for r in [0.2,0.6,1.2,1.5,1.8,2.7]:
      for nu in [0.4,1.,1.8]:
       for D in [0.001,0.1,1.5]:
        for t in [0.,0.2,0.8,2.,4.]:
         a=1.7
         c=cov_closed(t,r,nu,D,a)
         q=cov_numeric(t,r,nu,D,a,n=1000)
         f=rk4_cov(t,r,nu,D,a,steps=300)
         for x in [q,f]:
           assert abs(x-c) < 5e-8*(1+abs(c)), (r,nu,D,t,x,c)
           checks+=1
           maxerr=max(maxerr,abs(x-c))
    # Check the independent critical-line trigonometric envelope.
    nu=1.0; a=1.0; r=1.5*nu
    critical=(3*nu*a*a*(3*math.sqrt(13)-10))/104
    for D in [0.0,critical/2,critical,critical*2,0.2]:
      offset=10*a*a/13+4*D/r
      amplitude=3*a*a/math.sqrt(13)
      assert abs(offset-amplitude)<1e-12 if D==critical else ((offset<amplitude)==(D<critical))
      assert abs((offset-amplitude) - (4/r)*(D-critical))<2e-14
      checks+=2
    # Verify that the coefficient of slow r-mode is strictly positive
    # for representative r<3nu/2 and many Brownian strengths.
    for nu in [.25,1.,3.]:
      for ratio in [.05,.25,.75,1.49]:
       r=ratio*nu
       den=(r*r-1.5*nu*nu)**2+6.75*nu**4
       for D in [0.,.01,1.,7.]:
        slow=(1.5*nu*nu*(6*nu*nu-r*r))/den+4*D/(r*a*a)
        assert slow>0
        checks+=1
    # Check guaranteed late sign changes in the fast-reset regime.
    for r,nu,D in [(3.,1.,0.001),(2.5,1.,3.),(1.2,.4,1.)]:
      b=beta(nu)
      # For t sufficiently large the slower, complex mode dominates.
      times=[t/b for t in [70.,73.,76.,79.,82.,85.,88.,91.,94.,97.]]
      vals=[cov_closed(t,r,nu,D,1.)*math.exp(alpha(nu)*t) for t in times]
      assert any(v>1e-8 for v in vals) and any(v<-1e-8 for v in vals),vals
      checks+=1
    print('PASS',checks,'independent and boundary checks; max numerical error',maxerr)
