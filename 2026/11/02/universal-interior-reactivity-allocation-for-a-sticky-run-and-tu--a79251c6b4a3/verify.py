"""Reproduce finite checks for the sticky-wall allocation theorem (Python standard library)."""
import math

def mean(h,L,v,alpha,gamma,K,x,p):
    u=K*(1+h)/2; q=K*(1-h)/2; T=L/v
    den=alpha*T*u*q+gamma*(u+q)+u*q
    C=(alpha*T*T*u*q+2*gamma*T*u+T*u*q+u-q)/den
    # eliminate the apparently singular A at u=0 through the right boundary
    if u>1e-12:
        A=(1+(gamma+u/2)*C)/u
    else:
        # right wall: (gamma+q)*(s(T)+d(T)/2)=1+gamma*(s(T)-d(T)/2)
        # => q*s(T)+(gamma+q/2)*d(T)=1
        dT=C-2*T
        sT=(1-(gamma+q/2)*dT)/q
        A=sT-alpha*C*T+alpha*T*T
    a=x/v; z=2*p-1
    return A+alpha*C*a-alpha*a*a+z*(C/2-a)

def optimum(L,v,alpha,gamma,K,x,p):
    T=L/v; lam=alpha*T; eta=gamma*T; beta=K*T
    w=lam*(2*x/L-1)+(2*p-1); F=beta*(lam+1)
    B=2*(lam+1)*(F+4*eta); H=F+4*eta
    return -2*H*w/(B+math.sqrt(B*B-4*F*H*w*w))

def gold(L,v,alpha,gamma,K,x,p):
    lo=-1.; hi=1.; rat=(math.sqrt(5)-1)/2
    a=hi-rat*(hi-lo); b=lo+rat*(hi-lo)
    fa=mean(a,L,v,alpha,gamma,K,x,p); fb=mean(b,L,v,alpha,gamma,K,x,p)
    for i in range(115):
        if fa<fb:
            hi=b; b=a; fb=fa; a=hi-rat*(hi-lo);fa=mean(a,L,v,alpha,gamma,K,x,p)
        else:
            lo=a; a=b;fa=fb;b=lo+rat*(hi-lo);fb=mean(b,L,v,alpha,gamma,K,x,p)
    return (hi+lo)/2

n=0
for L in (0.6,2.):
 for v in (0.7,2.):
  for alpha in (0.2,2.):
   for gamma in (0.15,1.5):
    for K in (0.6,6.):
     for xfrac in (0.12,0.53,0.91):
      for p in (0.,0.35,1.):
       x=L*xfrac; par=(L,v,alpha,gamma,K,x,p)
       h=optimum(*par); assert -1<h<1
       g=gold(*par); assert abs(h-g)<3e-6,(par,h,g)
       f0=mean(h,*par); assert f0<=mean(-1,*par)+1e-8 and f0<=mean(1,*par)+1e-8
       step=min(1.e-5, (1-abs(h))/8)
       assert mean(h-step,*par)>f0-1e-8 and mean(h+step,*par)>f0-1e-8
       n+=1
print('PASS:',n,'parameter sets: strict interior, independent minimization and endpoint checks')
