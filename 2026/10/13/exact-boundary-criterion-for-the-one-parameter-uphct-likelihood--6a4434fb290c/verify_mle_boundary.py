import math

def logL_gamma(gamma, xs, Rs, sstar, Rstar):
    nu=len(xs)
    K=sum(Rs)+Rstar
    return (nu*math.log(gamma+1)+(nu+K)*math.log(gamma)
            -Rstar*math.log(gamma+sstar)
            -sum((2+r)*math.log(gamma+x) for x,r in zip(xs,Rs)))

def logL_delta(delta, xs, Rs, sstar, Rstar):
    nu=len(xs)
    return (nu*math.log1p(delta)-Rstar*math.log1p(delta*sstar)
            -sum((2+r)*math.log1p(delta*x) for x,r in zip(xs,Rs)))

def D(delta, xs, Rs, sstar, Rstar):
    nu=len(xs)
    return (nu/(1+delta)-Rstar*sstar/(1+delta*sstar)
            -sum((2+r)*x/(1+delta*x) for x,r in zip(xs,Rs)))

def threshold(xs, Rs, sstar, Rstar):
    return Rstar*sstar+sum((2+r)*x for x,r in zip(xs,Rs))

# Parameterization identity differs only by no parameter-dependent term.
xs=[0.22,0.41,0.63]; Rs=[1,0,2]; s=.75; Rstar=2
for g in [0.1,0.5,2,10,100]:
    d=1/g
    assert abs(logL_gamma(g,xs,Rs,s,Rstar)-logL_delta(d,xs,Rs,s,Rstar)) < 1e-11

# Complete-data boundary example: mean 0.7, so no finite MLE.
xs=[0.6,0.7,0.8]; Rs=[0,0,0]; s=.8; Rstar=0
assert threshold(xs,Rs,s,Rstar) > len(xs)
for d in [0,0.01,0.1,1,10,100]:
    assert D(d,xs,Rs,s,Rstar) < 0
assert logL_gamma(1e6,xs,Rs,s,Rstar) > logL_gamma(100,xs,Rs,s,Rstar) > logL_gamma(1,xs,Rs,s,Rstar)

# Complete-data interior example: mean 0.2, so finite maximizer exists.
xs2=[0.1,0.2,0.3]; Rs2=[0,0,0]
assert threshold(xs2,Rs2,s,0) < len(xs2)
assert D(0,xs2,Rs2,s,0) > 0
assert D(100,xs2,Rs2,s,0) < 0
# Simple grid locates an interior maximizer with likelihood above the uniform boundary.
best=None
for k in range(1,200000):
    d=10**(-4+8*k/199999)
    v=logL_delta(d,xs2,Rs2,s,0)
    if best is None or v>best[1]: best=(d,v)
assert best[0] > 1e-4 and best[0] < 1e4
assert best[1] > logL_delta(0,xs2,Rs2,s,0)

# Censored boundary example.
xc=[0.3,0.4]; Rc=[1,2]; sc=.6; Rsc=3
Tc=threshold(xc,Rc,sc,Rsc)
assert abs(Tc-4.3)<1e-14 and Tc>len(xc)
for d in [0,0.01,0.1,1,10,100]:
    assert D(d,xc,Rc,sc,Rsc) < 0

# Positive-probability complete-data boundary subset.
gamma=2.0; n=4
p_half=gamma/(2*gamma+1)
assert abs(p_half-0.4)<1e-15
assert p_half**n > 0

print('VERIFY_OK')
print('boundary_complete_T',threshold([0.6,0.7,0.8],[0,0,0],.8,0))
print('interior_complete_T',threshold(xs2,Rs2,.8,0))
print('interior_delta_max_grid',best[0])
print('censored_boundary_T',Tc)
print('boundary_subset_probability_gamma2_n4',p_half**n)
