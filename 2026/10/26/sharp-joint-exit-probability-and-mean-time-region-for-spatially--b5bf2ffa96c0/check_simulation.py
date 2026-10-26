import math,random
L=1.7
v=1.4
K=2.2
rng=random.Random(1850744)

def hazard_factory(beta,amp=0.0):
    if beta==0.0:
        Z=1.0
    else:
        Z=math.expm1(beta)/beta
    def Q(t):
        return (t if beta==0 else math.expm1(beta*t)/beta)
    def H(x):
        t=x/L
        return K*(Q(t)/Z+amp*(t+math.sin(2*math.pi*t)/(2*math.pi) - t))
    # amp term normalised on cos independently; for beta !=0 keep 0
    assert abs(H(0))<1.e-12 and abs(H(L)-K)<1.e-12
    # ∫ x lambda(x) dx /v = K L mu_fraction
    mu=0.5 if beta==0 else ((beta-1)*math.exp(beta)+1)/(beta*math.expm1(beta))
    return H,mu

def simulate(H):
    T=[]; N=12000; hits=0
    for i in range(N):
        x=0.0; sign=1; t=0.0
        for event in range(100000):
            destination=L if sign==1 else 0.0
            h0=H(x); h1=H(destination)
            dh=abs(h1-h0)
            e=rng.expovariate(1)
            if e>=dh:
                t+=abs(destination-x)/v
                hits+=int(sign==1)
                T.append(t)
                break
            target=h0+sign*e
            lo,hi=(x,L) if sign==1 else (0.0,x)
            for j in range(43):
                mid=(lo+hi)/2
                if H(mid)<target:lo=mid
                else:hi=mid
            end=(lo+hi)/2
            t+=abs(end-x)/v
            x=end
            sign=-sign
        else:raise RuntimeError('event loop')
    return N,hits/N,sum(T)/N

for name,beta,amp in [('uniform',0,0),('rising',2.3,0),('falling',-2.3,0),('cos-modulated',0,0.3)]:
 H,mu=hazard_factory(beta,amp)
 n,p_obs,t_obs=simulate(H)
 p_exp=1/(1+K)
 tau_exp=(L/v)*(1+2*K*mu)/(1+K)
 print(f'{name:14} p predicted={p_exp:.7f} simulated={p_obs:.7f} time predicted={tau_exp:.7f} simulated={t_obs:.7f} rel_err={(t_obs/tau_exp-1)*100:.2f}%')
