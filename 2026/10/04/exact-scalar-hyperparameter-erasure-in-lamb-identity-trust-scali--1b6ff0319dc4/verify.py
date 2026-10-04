import math

def run(grad,x0,etas,b1,b2,eps):
    x=x0; m=0.0; v=0.0; out=[x]
    for t,eta in enumerate(etas,1):
        g=grad(x)
        m=b1*m+(1-b1)*g
        v=b2*v+(1-b2)*g*g
        mh=m/(1-b1**t) if b1 else m
        vh=v/(1-b2**t) if b2 else v
        r=mh/(math.sqrt(vh)+eps)
        assert r != 0.0
        x=x-eta*abs(x)*(1.0 if r>0 else -1.0)
        out.append(x)
    return out

etas=[0.2,0.1,0.35,0.05,0.4,0.15]
cases=[
    (lambda x:0.01*x,3.0),
    (lambda x:1000.0*x,-2.0),
    (lambda x:x+x**3,1.5),
    (lambda x:math.tanh(x),-1.25),
]
params=[(0.0,0.0,1e-3),(0.9,0.999,1e-8),(0.5,0.8,1.0),(0.99,0.9999,1e-12)]

for grad,x0 in cases:
    exp=[x0]; x=x0
    for eta in etas:
        x=(1-eta)*x; exp.append(x)
    for b1,b2,eps in params:
        got=run(grad,x0,etas,b1,b2,eps)
        for a,b in zip(got,exp):
            assert abs(a-b) <= 2e-12*max(1.0,abs(b))

lam=37.0
got=run(lambda x:lam*x,2.5,etas,0.9,0.999,1e-8)
for t,eta in enumerate(etas):
    f0=0.5*lam*got[t]**2
    f1=0.5*lam*got[t+1]**2
    assert abs(f1/f0-(1-eta)**2) < 2e-13

print("verification passed")
