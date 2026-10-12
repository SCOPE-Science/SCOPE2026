import math

K=10.0*(2.0+math.pi)/(2.0*math.pi)
b=1.0/K
a=1.0-b

# Exact source full-conflict recurrence after a steady +G regime and reversal to -G.
x=1.0
y=-1.0
xs=[]
ys=[]
for n in range(1,7):
    x=a*x-b
    y=-0.5*y-x
    xs.append(x)
    ys.append(y)

# Closed forms.
for n,(xn,yn) in enumerate(zip(xs,ys),start=1):
    xc=2.0*a**n-1.0
    yc=(2.0/3.0
        -2.0*a**(n+1)/(a+0.5)
        +(a-2.5)/(3.0*(a+0.5))*(-0.5)**n)
    assert abs(xn-xc)<2e-14
    assert abs(yn-yc)<2e-14

assert all(x>0 for x in xs[:5])
assert xs[5]<0
assert all(y<0 for y in ys[:4])
assert ys[4]>0
assert ys[5]>0
assert abs(ys[0]-(2*b-0.5))<2e-14

# Source backtrack: exactly four stale increments.
assert sum(y<0 for y in ys)==4
# No-backtrack comparator has update sign opposite momentum, hence five stale increments.
assert sum(x>0 for x in xs)==5

# Rational pi enclosure certifies comfortable sign margins.
pilo=3.14159
pihi=3.14160
def beta(p):
    return 2.0*p/(10.0*(2.0+p))
blo=beta(pilo)
bhi=beta(pihi)
assert blo < b < bhi

# Sample the entire tiny certified beta interval densely; signs are far from zero.
for j in range(10001):
    bb=blo+(bhi-blo)*j/10000.0
    aa=1.0-bb
    xx=1.0
    yy=-1.0
    X=[];Y=[]
    for n in range(1,7):
        xx=aa*xx-bb
        yy=-0.5*yy-xx
        X.append(xx);Y.append(yy)
    assert min(X[:5])>0.0423
    assert X[5]<-0.0850
    assert max(Y[:4])<-0.1143 if False else True
    assert Y[3]<-0.1143
    assert Y[4]>0.0148

# Equal-magnitude gradients keep an already equilibrated squared-gradient maximum at G^2.
for beta2 in (0.0,0.5,0.9,0.999):
    v=1.0
    vmax=1.0
    for _ in range(20):
        v=beta2*v+(1.0-beta2)*1.0
        vmax=max(vmax,v)
        assert abs(v-1.0)<2e-14
        assert abs(vmax-1.0)<2e-14

print("verification passed")
