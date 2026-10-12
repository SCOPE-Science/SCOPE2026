#!/usr/bin/env python3
import math

def logB_pair(delta,p):
    q=1.0/(1.0-p)
    return 2.0*math.log(delta)+(1.0-p)*math.lgamma(q+1.0)+(2.0-p)*math.log((1.0-p)/(delta-p))

def C_pair(delta):
    # d=2, b=delta^2
    return (delta**2)*((1.0-delta)**(2.0-delta))*math.gamma(1.0+1.0/(1.0-delta))**(1.0-delta)

delta=0.4
C=C_pair(delta)
ratios=[]
for eps in (1e-2,1e-3,1e-4,1e-5):
    p=delta-eps
    norm=math.exp(logB_pair(delta,p)+(2.0-delta)*math.log(eps))
    ratios.append(norm/C)
assert abs(ratios[-1]-1.0) < 3e-4, ratios
assert abs(ratios[-1]-1.0) < abs(ratios[0]-1.0)

# delta=1,d=2: B=Gamma(q+1)^(1/q), and (1-p)B -> 1/e.
boundary=[]
for eps in (1e-2,1e-3,1e-4,1e-5):
    q=1.0/eps
    logB=eps*math.lgamma(q+1.0)
    boundary.append(math.exp(math.log(eps)+logB+1.0)) # ratio to 1/e
assert abs(boundary[-1]-1.0) < 8e-5, boundary
assert abs(boundary[-1]-1.0) < abs(boundary[0]-1.0)

# r=1,d=1 exact source bound, normalized by the theorem's constant.
def logB_single(delta,p):
    return math.log(delta)+(1.0-p)*math.log((1.0-p)/(delta-p))
def C_single(delta):
    return delta*(1.0-delta)**(1.0-delta)
rs=[]
for eps in (1e-3,1e-5,1e-7):
    p=delta-eps
    val=math.exp(logB_single(delta,p)+(1.0-delta)*math.log(eps))/C_single(delta)
    rs.append(val)
assert abs(rs[-1]-1.0) < 5e-6, rs

print('VERIFY_OK subunit_ratio=%.10f boundary_ratio=%.10f single_ratio=%.10f' % (ratios[-1],boundary[-1],rs[-1]))
