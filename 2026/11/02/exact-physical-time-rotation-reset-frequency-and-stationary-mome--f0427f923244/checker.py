import math, random

def f(x,s,lam,beta):
    alpha=beta-lam
    xx=lam*x+alpha*s
    y=s+xx-x
    return (xx, y if abs(y)<=1 else 0.)

def from_w(W,lam,beta):
    mu=-lam/(1-lam)
    q=1/(1-lam)
    nu=beta+mu
    L=math.log(nu/mu)
    th=math.log(nu/q)/L
    ell=2-th
    sig=1 if W<ell else -1
    w=W if W<ell else W-ell
    if w<1:
        z=w; t=mu*math.exp(L*z)
        return (sig*t,0.)
    z=w-1; t=mu*math.exp(L*z)
    return (lam*sig*t,(lam-1)*sig*t)

random.seed(314159)
for lam,beta in [(-.5,2),(-.8,1.5),(-.3,3),(-.75,5)]:
    assert -lam*(beta+1)>1
    mu=-lam/(1-lam);q=1/(1-lam);nu=beta+mu
    L=math.log(nu/mu);theta=math.log(nu/q)/L; ell=2-theta
    for _ in range(20000):
        W=random.random()*2*ell
        x,s=from_w(W,lam,beta)
        xx,ss=f(x,s,lam,beta)
        xxx,sss=from_w((W+1)%(2*ell),lam,beta)
        assert abs(xx-xxx)<2e-12 and abs(ss-sss)<2e-12, (lam,beta,W,x,s,xx,ss,xxx,sss)
    # Haar second-moment tests by quadrature midpoint on circle
    n=80000
    sx2=ss2=sxs=on=0.
    for k in range(n):
        x,s=from_w((k+.5)/n*2*ell,lam,beta)
        sx2+=x*x/n;ss2+=s*s/n;sxs+=x*s/n;on+=(s==0)/n
    theo_x=(nu*nu-mu*mu+lam*lam*(q*q-mu*mu))/(2*(L+math.log(q/mu)))
    theo_s=(lam-1)**2*(q*q-mu*mu)/(2*(L+math.log(q/mu)))
    theo_xs=lam*(lam-1)*(q*q-mu*mu)/(2*(L+math.log(q/mu)))
    assert abs(sx2-theo_x)<5e-4 and abs(ss2-theo_s)<5e-4 and abs(sxs-theo_xs)<5e-4 and abs(on-1/ell)<5e-4
    print('PASS',lam,beta,'theta',round(theta,9),'positive',round(theo_x,7),round(theo_s,7))
print('PASS: 80000 branch-conjugacy comparisons and four quadrature cross-checks')
