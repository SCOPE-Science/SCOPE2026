import math


def psi(q, s):
    a = math.log1p(-q) - q*s
    b = math.log(q) + (1-q)*s
    m = max(a,b)
    return m + math.log(math.exp(a-m)+math.exp(b-m))


def objective(loglam, ps, rs, alpha):
    lam = math.exp(loglam)
    total = math.log(2/alpha)
    for p,r in zip(ps,rs):
        q=min(p,1-p)
        d=r/(p*(1-p))
        total += psi(q,lam*d)
    return total/(len(ps)*lam)


def golden_min(f, lo=-12.0, hi=12.0, it=180):
    g=(math.sqrt(5)-1)/2
    x1=hi-g*(hi-lo); x2=lo+g*(hi-lo)
    f1=f(x1); f2=f(x2)
    for _ in range(it):
        if f1>f2:
            lo=x1; x1=x2; f1=f2; x2=lo+g*(hi-lo); f2=f(x2)
        else:
            hi=x2; x2=x1; f2=f1; x1=hi-g*(hi-lo); f1=f(x1)
    x=(lo+hi)/2
    return math.exp(x), f(x)


def hoeffding_width(ps, rs, alpha):
    L=math.log(2/alpha)
    # Common interval case has r=(b-a)/2 and coefficient radius r/[p(1-p)].
    return math.sqrt(L/2*sum((r/(p*(1-p)))**2 for p,r in zip(ps,rs)))/len(ps)


def bernstein_width(ps, rs, alpha):
    L=math.log(2/alpha)
    V=sum(r*r/(p*(1-p)) for p,r in zip(ps,rs))
    R=max(r/min(p,1-p) for p,r in zip(ps,rs))
    return (R*L/3+math.sqrt(2*V*L+(R*L/3)**2))/len(ps)


def orientation_check():
    grid_p=[0.01,0.1,0.4,0.5,0.6,0.9,0.99]
    grid_s=[0.1,1.0,3.0]
    for p in grid_p:
        q=min(p,1-p)
        for s in grid_s:
            mp=(1-p)*math.exp(-p*s)+p*math.exp((1-p)*s)
            mm=(1-p)*math.exp(p*s)+p*math.exp(-(1-p)*s)
            best=max(mp,mm)
            mq=(1-q)*math.exp(-q*s)+q*math.exp((1-q)*s)
            if abs(best-mq)>1e-12:
                raise AssertionError((p,s,best,mq))


def main():
    orientation_check()
    n=500; alpha=0.05; r=0.5
    print('p  Hoeffding  ExactChernoff  Bernstein')
    for p in [0.5,0.2,0.05,0.01]:
        ps=[p]*n; rs=[r]*n
        _,exact=golden_min(lambda x: objective(x,ps,rs,alpha))
        print(f'{p:.2f} {hoeffding_width(ps,rs,alpha):.9f} {exact:.9f} {bernstein_width(ps,rs,alpha):.9f}')

if __name__=='__main__':
    main()
