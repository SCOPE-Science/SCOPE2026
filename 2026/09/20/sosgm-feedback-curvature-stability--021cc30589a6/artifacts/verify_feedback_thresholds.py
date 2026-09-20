import math
import random
from math import comb


def moments(xs, ps):
    mu = sum(p*x for x,p in zip(xs,ps))
    m2 = sum(p*x*x for x,p in zip(xs,ps))
    hm = sum(p/x for x,p in zip(xs,ps))
    return mu, m2, hm


def q(p, mu, m2):
    return 1.0 - 2.0*mu*p + m2*p*p


def targets(xs, ps):
    mu,m2,hm = moments(xs,ps)
    return mu/m2, 1.0/mu, hm


def random_law(kappa, n=7):
    xs = [1.0 + (kappa-1.0)*random.random() for _ in range(n)]
    ws = [random.expovariate(1.0) for _ in range(n)]
    s = sum(ws)
    ps = [w/s for w in ws]
    return xs, ps


def ratio_uniform_max(kappa):
    return (kappa-1.0)**2/(4.0*kappa)


def hyper_uniform_max(kappa):
    return (kappa-math.sqrt(kappa)+1.0)**2/kappa


def endpoint_hyper_ratio(kappa, p_hi):
    xs=[1.0,kappa]
    ps=[1.0-p_hi,p_hi]
    mu,m2,hm=moments(xs,ps)
    return hm*m2/mu


def p_hyp_batch(kappa,b):
    return sum(comb(b,j)/(2.0**b)/(1.0+(kappa-1.0)*j/b) for j in range(b+1))


random.seed(1729)
print('sharp thresholds')
ratio_kappa = 3.0 + 2.0*math.sqrt(2.0)
s = ((1.0+math.sqrt(2.0)) + math.sqrt(2.0*math.sqrt(2.0)-1.0))/2.0
hyper_kappa = s*s
print(f'ratio_uniform_kappa = {ratio_kappa:.15f}')
print(f'hyper_uniform_kappa = {hyper_kappa:.15f}')

print('\nequal two-point law, kappa=4')
kappa=4.0
xs=[1.0,kappa]
ps=[0.5,0.5]
mu,m2,hm=moments(xs,ps)
pms,pr,ph=targets(xs,ps)
print(f'p_ms = {pms:.15f}')
print(f'p_ratio = {pr:.15f}')
print(f'p_hyper = {ph:.15f}')
print(f'Q_ms = {q(pms,mu,m2):.15f}')
print(f'Q_ratio = {q(pr,mu,m2):.15f}')
print(f'Q_hyper = {q(ph,mu,m2):.15f}')
qnull=0.5*(1.0-ph)**2 + 0.5*1.0
print(f'Q_hyper_with_null = {qnull:.15f}')

print('\nendpoint extremizers')
for kappa in (2.0,4.0,8.0):
    p_ratio_hi=1.0/(kappa+1.0)
    xs=[1.0,kappa]
    ps=[1.0-p_ratio_hi,p_ratio_hi]
    mu,m2,hm=moments(xs,ps)
    qr=q(1.0/mu,mu,m2)
    p_hyper_hi=1.0/(math.sqrt(kappa)+1.0)
    hs=endpoint_hyper_ratio(kappa,p_hyper_hi)
    print(f'kappa={kappa:g} ratio_ext={qr:.15f} ratio_formula={ratio_uniform_max(kappa):.15f} hyper_S_ext={hs:.15f} hyper_formula={hyper_uniform_max(kappa):.15f}')

print('\nrandom support checks')
max_ratio_violation=-1e100
max_hyper_violation=-1e100
max_order_violation=-1e100
for kappa in (1.5,2.0,3.0,4.0,6.0,10.0):
    for _ in range(3000):
        xs,ps=random_law(kappa)
        mu,m2,hm=moments(xs,ps)
        pms,pr,ph=mu/m2,1.0/mu,hm
        max_order_violation=max(max_order_violation,pms-pr,pr-ph)
        max_ratio_violation=max(max_ratio_violation,q(pr,mu,m2)-ratio_uniform_max(kappa))
        max_hyper_violation=max(max_hyper_violation,hm*m2/mu-hyper_uniform_max(kappa))
print(f'max_order_violation = {max_order_violation:.3e}')
print(f'max_ratio_bound_violation = {max_ratio_violation:.3e}')
print(f'max_hyper_bound_violation = {max_hyper_violation:.3e}')

print('\nbatch-size example for iid equal two-point sample curvatures')
for kappa in (10.0,100.0,1000.0):
    first=None
    for b in range(1,31):
        phb=p_hyp_batch(kappa,b)
        mu=(1.0+kappa)/2.0
        m2=mu*mu+(kappa-1.0)**2/(4.0*b)
        qb=q(phb,mu,m2)
        if qb < 1.0:
            first=(b,phb,qb)
            break
    necessary=math.log2((1.0+kappa)/4.0)
    print(f'kappa={kappa:g} first_stable_b={first[0]} p_hyper_b={first[1]:.15f} Q={first[2]:.15f} necessary_b_gt={necessary:.15f}')
