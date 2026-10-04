import math, random

def adamod_rates(raw,beta3):
    s=0.0; out=[]
    for eta in raw:
        s=beta3*s+(1-beta3)*eta
        out.append(min(eta,s))
    return out

random.seed(0)
for beta3 in (0.1,0.5,0.9,0.999,0.9999):
    for _ in range(100):
        raw=[10**random.uniform(-8,8) for _ in range(20)]
        out=adamod_rates(raw,beta3)
        for eta,hat in zip(raw,out):
            assert hat <= eta*(1+1e-14)
            assert hat+1e-18 >= (1-beta3)*eta*(1-1e-13)
        assert abs(out[0]-(1-beta3)*raw[0]) <= 1e-12*max(1,raw[0])

def first_step(x0,h,alpha,b1,b2,b3,eps):
    g=h*x0
    m=(1-b1)*g; v=(1-b2)*g*g
    mhat=m/(1-b1); vhat=v/(1-b2)
    eta=alpha/(math.sqrt(vhat)+eps)
    s=(1-b3)*eta
    hat=min(eta,s)
    return x0-hat*mhat,eta,hat

for b1 in (0,0.4,0.9,0.99):
  for b2 in (0,0.5,0.999):
    for b3 in (0.2,0.9,0.999):
      h=3.0; alpha=1e-3; eps=1e-6
      for x0 in (-1,-1e-3,-1e-7,1e-7,1e-3,1):
        x1,eta,hat=first_step(x0,h,alpha,b1,b2,b3,eps)
        expected=x0*(1-(1-b3)*alpha*h/(h*abs(x0)+eps))
        assert abs(x1-expected) < 1e-13*max(1,abs(expected))
        assert abs(hat-(1-b3)*eta) < 1e-13*max(1,eta)

for b3 in (0.2,0.9,0.999):
    alpha=0.01; eps=2e-4
    hcrit=2*eps/((1-b3)*alpha)
    for h in (0.1*hcrit,0.5*hcrit,hcrit):
      for x0 in (1e-12,1e-9,1e-6,1e-3,1):
        x1,_,_=first_step(x0,h,alpha,0.9,0.999,b3,eps)
        assert h*x1*x1/2 <= h*x0*x0/2 + 1e-24

b3=0.9; alpha=0.01; eps=1e-4; h=1.0
A=(1-b3)*alpha*h; r=(A/2-eps)/h
assert r>0
for x0 in (0.1*r,0.5*r,0.999*r):
    x1,_,_=first_step(x0,h,alpha,0.2,0.7,b3,eps)
    assert x1*x1>x0*x0
for x0 in (1.001*r,2*r,10*r):
    x1,_,_=first_step(x0,h,alpha,0.2,0.7,b3,eps)
    assert x1*x1<x0*x0

for b3,expected in ((0.999,9801.0),(0.9999,81.0)):
    x0=1e-16; h=1.0; alpha=1e-3; eps=1e-8
    x1,_,_=first_step(x0,h,alpha,0.9,0.999,b3,eps)
    ratio=(x1/x0)**2
    assert abs(ratio-expected)/expected < 3e-8

print('verification passed')
