#!/usr/bin/env python3
import math

SQRT2 = math.sqrt(2.0)
SQRT2PI = math.sqrt(2.0 * math.pi)

def sf(x):
    return 0.5 * math.erfc(x / SQRT2)

def phi(x):
    return math.exp(-0.5 * x * x) / SQRT2PI

def hazard(x):
    return phi(x) / sf(x)

def bisect_root(target, lo=-12.0, hi=12.0, it=120):
    for _ in range(it):
        mid=(lo+hi)/2.0
        if hazard(mid) < target:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2.0

def boundary(alpha, delta, rho):
    s=delta*math.sqrt(1.0-rho)
    x=bisect_root(s)
    t=sf(x)
    w=(math.log(1.0/(alpha*t)) + 0.5*delta*delta - s*x)/(delta*math.sqrt(rho))
    return s,x,t,w,sf(w)

def g_of_x(alpha,delta,rho,x):
    s=delta*math.sqrt(1.0-rho)
    return (math.log(1.0/(alpha*sf(x))) + 0.5*delta*delta - s*x)/(delta*math.sqrt(rho))

def q_over_t(alpha,delta,rho,w,t):
    s=delta*math.sqrt(1.0-rho)
    m=delta*math.sqrt(rho)*w - 0.5*delta*delta
    z=(math.log(1.0/(alpha*t))-m)/s
    return sf(z)/t

def grid_sup_ratio(alpha,delta,rho,w):
    best=0.0
    best_t=None
    # log grid near zero plus linear grid
    for j in range(1,20001):
        t=j/20000.0
        r=q_over_t(alpha,delta,rho,w,t)
        if r>best:
            best,best_t=r,t
    return best,best_t

def main():
    alpha,delta,rho=0.05,3.0,0.5
    s,x,t,w,p=boundary(alpha,delta,rho)
    assert abs(hazard(x)-s) < 1e-12
    # Unique minimum: derivative h(x)-s changes sign.
    assert hazard(x-1e-4) < s < hazard(x+1e-4)
    # Direct grid comparison around the analytic minimizer.
    vals=[g_of_x(alpha,delta,rho,-5.0+10.0*j/200000.0) for j in range(200001)]
    gmin=min(vals)
    assert abs(gmin-w) < 2e-9
    # At first contact, conditional tail fraction equals the step-up fraction.
    assert abs(q_over_t(alpha,delta,rho,w,t)-1.0) < 2e-12
    low,_=grid_sup_ratio(alpha,delta,rho,w-0.05)
    high,_=grid_sup_ratio(alpha,delta,rho,w+0.05)
    assert low < 1.0 and high > 1.0
    # Stable benchmark values.
    assert abs(t-0.043388293511075544) < 2e-14
    assert abs(w-3.29993272728449) < 2e-13
    assert abs(p-0.00048354003713771214) < 2e-15
    print('VERIFY_OK')
    print(f's={s:.15g}')
    print(f'x_star={x:.15g}')
    print(f't_star={t:.15g}')
    print(f'w_star={w:.15g}')
    print(f'limit_fdr={p:.15g}')
    print(f'sup_ratio_below={low:.12g}')
    print(f'sup_ratio_above={high:.12g}')

if __name__ == '__main__':
    main()
