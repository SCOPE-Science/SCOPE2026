import math

r=math.sqrt(2.0)
a=r-1.0
b=2.0-r

def N(v):
    s,t=v
    return max(abs(s),abs(t),(abs(s)+abs(t))/r)

def d(lam):
    return max(1.0,a+lam/r,lam-a)

def mu_formula(p):
    A=(1.0+(2.0*a)**p)**(1.0/p)
    B=(1.0+(2.0*r)**p)**(1.0/p)/(1.0+r)
    return max(A,B)

# Exact geometric identities up to floating arithmetic.
assert abs((1.0-a)/r-a)<1e-14
assert abs(2.0*a-(2.0*r-2.0))<1e-14
assert abs((a+2.0)-(1.0+r))<1e-14

# Fixed equality pair for every sampled lambda.
x=(-a,1.0)
y=(1.0,0.0)
assert abs(N(x)-1.0)<1e-14
assert abs(N(y)-1.0)<1e-14
for k in range(2001):
    lam=8.0*k/2000.0
    assert abs(N((x[0]+lam*y[0],x[1]+lam*y[1]))-d(lam))<2e-12

# Facet endpoint family: x=(s,1), y=(+/-1,0).
for j in range(101):
    s=-a+2*a*j/100.0
    xx=(s,1.0)
    assert abs(N(xx)-1.0)<2e-14
    for eps in (-1.0,1.0):
        yy=(eps,0.0)
        for k in range(301):
            lam=6.0*k/300.0
            assert N((xx[0]+lam*yy[0],xx[1]))+2e-12>=d(lam)

# Interior support cone at x=(a,1): kernel directions lie between the
# horizontal and southeast-diagonal directions. Normalize y=(1,-q).
xx=(a,1.0)
for j in range(101):
    q=j/100.0
    raw=(1.0,-q)
    nr=N(raw)
    yy=(raw[0]/nr,raw[1]/nr)
    assert abs(N(yy)-1.0)<2e-14
    assert yy[0]+2e-14>=1.0/r
    for k in range(301):
        lam=6.0*k/300.0
        assert N((xx[0]+lam*yy[0],xx[1]+lam*yy[1]))+3e-12>=d(lam)

# Switch points.
L1=2.0*a
L2=2.0*r
assert abs(d(L1)-1.0)<2e-14
assert abs(d(L2)-(1.0+r))<2e-14

# Dense one-variable scan against the closed formula for representative p.
ps=[1.0,1.2,1.5,2.0,2.5,3.0,4.0,8.0,20.0]
for p in ps:
    target=mu_formula(p)
    # include both exact candidate points plus a dense compact scan; tail is decreasing.
    vals=[]
    for k in range(20001):
        lam=8.0*k/20000.0
        vals.append((1.0+lam**p)**(1.0/p)/d(lam))
    vals += [(1.0+L1**p)**(1.0/p)/d(L1),(1.0+L2**p)**(1.0/p)/d(L2)]
    assert max(vals)<=target+2e-8
    assert abs(max(vals)-target)<2e-8

print('VERIFY_OK d8_branches=3 lambdas=2001 support_grid=202 mu_p_exponents=9')
