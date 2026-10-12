import math

c=1.0/(math.e-1.0)

def phi(s):
    t=math.exp((1.0-s)*math.log(s))
    return math.expm1(t)/(math.e-1.0)

def hazard_ratio(s):
    t=math.exp((1.0-s)*math.log(s))
    return (1.0-s-s*math.log(s))*(t*math.exp(t)/math.expm1(t))

ss=[1e-2,1e-4,1e-6,1e-8]
ratios=[phi(s)/s for s in ss]
hr=[hazard_ratio(s) for s in ss]
assert abs(ratios[-1]/c-1.0)<3e-7
assert abs(hr[-1]-1.0)<3e-7

# The second-order residual divided by s^2 tends to zero.
res=[]
for s in ss:
    approx=c*(s-s*s*math.log(s)+0.5*s*s)
    res.append((phi(s)-approx)/(s*s))
assert abs(res[-1])<5e-6

# Exact Pareto baseline S_G(x)=x^{-alpha}, x>=1.
def invert_phi(u):
    lo,hi=0.0,1.0
    for _ in range(160):
        mid=(lo+hi)/2
        if phi(mid)<u: lo=mid
        else: hi=mid
    return (lo+hi)/2

alpha=2.5
us=[1e-3,1e-5,1e-7]
qrat=[]
for u in us:
    s=invert_phi(u)
    qf=s**(-1.0/alpha)
    qg=u**(-1.0/alpha)
    qrat.append(qf/qg)
target=c**(1.0/alpha)
assert abs(qrat[-1]/target-1.0)<2e-5

print('VERIFY_OK')
print('tail_constant',format(c,'.15f'))
print('survival_ratio_last',format(ratios[-1],'.15f'))
print('hazard_ratio_last',format(hr[-1],'.15f'))
print('second_order_residual_over_s2_last',format(res[-1],'.15e'))
print('pareto_quantile_target',format(target,'.15f'))
print('pareto_quantile_ratio_last',format(qrat[-1],'.15f'))
