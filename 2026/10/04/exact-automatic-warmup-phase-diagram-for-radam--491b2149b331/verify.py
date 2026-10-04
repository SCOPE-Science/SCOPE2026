import math

def rho(t,b):
    return (1.0+b)/(1.0-b)-2.0*t*b**t/(1.0-b**t)

def P(t,b):
    return -3.0-b+sum((2*j-3)*b**j for j in range(2,t))

def F(t,b):
    return 5.0*b-3.0-b**t*((2*t-3)+(5-2*t)*b)

def root(t):
    lo,hi=0.6,1.0-1e-14
    for _ in range(140):
        mid=(lo+hi)/2
        if P(t,mid)>0:
            hi=mid
        else:
            lo=mid
    return (lo+hi)/2

def activation(b,limit=200000):
    for t in range(1,limit+1):
        if rho(t,b)>4.0:
            return t
    return math.inf

for b in (0.1,0.59,0.6001,0.61,0.65,0.7,0.8,0.9,0.99,0.999):
    prev=rho(1,b)
    for t in range(2,80):
        cur=rho(t,b)
        assert cur>prev-2e-12
        prev=cur

expected={
5:0.773303025730682,
6:0.690010172958752,
7:0.650907733825902,
8:0.630187730081184,
9:0.618416405229492,
10:0.611434178407706,
11:0.607176526646698,
}
roots={}
for t in range(5,25):
    bt=root(t)
    roots[t]=bt
    assert 0.6<bt<1.0
    for b in (0.61,0.65,0.72,0.83,0.95):
        assert abs(F(t,b)-(b-1.0)**2*P(t,b))<2e-10
for t,v in expected.items():
    assert abs(roots[t]-v)<2e-12
for t in range(5,24):
    assert roots[t+1]<roots[t]

assert activation(0.8)==5
assert activation(0.9)==5
assert activation(0.99)==5
assert activation(0.999)==5
assert activation(0.7)==6
assert activation(0.65)==8
assert activation(0.61)==11

for b in (0.1,0.5,0.6):
    assert (1+b)/(1-b)<=4.0+1e-14
    assert all(rho(t,b)<=4.0+1e-12 for t in range(1,200))

prev=1.0
for t in range(5,15):
    bt=roots[t]
    mid=(bt+prev)/2
    assert activation(mid)==t
    prev=bt

for t,tol in ((20,0.01),(30,0.001),(40,0.001),(50,0.001)):
    bt=root(t)
    delta=bt-0.6
    lead=(4.0/25.0)*t*(0.6**t)
    assert abs(delta/lead-1.0)<tol

print("verification passed")
