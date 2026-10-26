"""High-precision tests of exponentially small thin-annulus bias."""
import mpmath as mp
mp.mp.dps=65

def eval_all(h,alpha,t):
    q2=mp.exp(-2*h)
    a2=mp.exp(-2*alpha*h)
    b2=mp.exp(-2*(1-alpha)*h)
    N=int(mp.ceil(105/(2*h*min(alpha,1-alpha))))+1
    K=mp.mpf('1');D=mp.mpf('0');DD=mp.mpf('0')
    for m in range(1,N+1):
        am=a2**m;bm=b2**m;z=q2**m
        x=t+(1-t)*z;y=1-t+t*z
        K+=am/x+bm/y
        D+=(1-z)*(bm/y**2-am/x**2)
        DD+=2*(1-z)**2*(am/x**3+bm/y**3)
    return K,D,DD

def solve(h0,a0):
    h=mp.mpf(str(h0));a=mp.mpf(str(a0))
    t=1-a
    for _ in range(10):
        K,D,DD=eval_all(h,a,t)
        dt=D/DD;t-=dt
        if abs(dt)<mp.mpf('1e-57'):break
    K,D,DD=eval_all(h,a,t)
    phase=mp.pi/h*mp.log((1-a)/a)+mp.pi*a
    leading= -4*mp.pi*mp.sin(mp.pi*a)/h*mp.exp(-mp.pi**2/h)*mp.cos(phase)
    C=(mp.pi/(2*h*mp.sin(mp.pi*a)))*(1-a)**(a-1)*a**(-a)
    Kcor=4*mp.sin(mp.pi*a)*mp.exp(-mp.pi**2/h)*mp.sin(phase)
    return float(t-(1-a)), float(leading),float((K/C)-1),float(Kcor)
if __name__=='__main__':
 for a in (.2,.35,.7):
  for h in (.6,.45,.3):
   actual,pred,kactual,kpred=solve(h,a)
   print(a,h,'mass bias',actual,'leading',pred,'rel err',((actual-pred)/pred if pred else 0),'kernel corr',kactual,'leading',kpred)
