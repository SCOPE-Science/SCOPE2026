import math
# verify constants: c=e^-6/4, point-mass lower bound vs exact binomial
from math import comb, exp, sqrt, log
def exact_fail(d):
    p=0.5+1/sqrt(d); s=0.0
    for j in range(0,d):  # P(Bin(2d-1,p)<=d-1)
        s+=comb(2*d-1,j)*(p**j)*((1-p)**(2*d-1-j))
    return s
def point_lb(d):
    return exp(-6)/(4*sqrt(d))
for d in [16,18,27,64,75,100,400,1000]:
    print(f"d={d} exactPfail={exact_fail(d):.6f} pointLB={point_lb(d):.6f} ratio={exact_fail(d)/point_lb(d):.1f}")
# check C(2d,d)>=4^d/(2 sqrt d)
for d in [1,2,5,16,27,100]:
    print(f"d={d} C={comb(2*d,d)} LB={4**d/(2*sqrt(d)):.1f} ok={comb(2*d,d)>=4**d/(2*sqrt(d))}")
# packing bound m/sqrt(d) -> inf
for n in [10**3,10**6,10**9,10**100]:
    ll=math.log(math.log(n)); d=int(ll**3); m=(n//4)**(d-1)
    print(f"n={n} d={d} log10(m)={(d-1)*math.log10(n/4):.2f} c*m/sqrt(d) huge -> {((d-1)*math.log(n/4)-0.5*math.log(d)):.2f} (log)")
