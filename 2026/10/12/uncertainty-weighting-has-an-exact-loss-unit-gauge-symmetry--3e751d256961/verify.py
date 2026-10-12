import math
import random

def losses_and_grads(theta):
    x,y=theta
    L1=(x-1.2)**2 + 0.4*(y+0.3)**2 + 0.7
    G1=[2*(x-1.2), 0.8*(y+0.3)]
    L2=0.6*(x+0.5)**2 + (y-1.0)**2 + 1.1
    G2=[1.2*(x+0.5), 2*(y-1.0)]
    L3=0.3*(x-y)**2 + 0.9
    G3=[0.6*(x-y), -0.6*(x-y)]
    return [L1,L2,L3],[G1,G2,G3]

def objective_and_grad(theta,s,q=None):
    if q is None:
        q=[1.0,1.0,1.0]
    coeff=[0.5,1.0,0.5]
    L,G=losses_and_grads(theta)
    val=0.0
    gt=[0.0,0.0]
    gs=[]
    for a,si,qi,Li,Gi in zip(coeff,s,q,L,G):
        w=a*math.exp(-si)*qi
        val += w*Li + 0.5*si
        gt[0] += w*Gi[0]
        gt[1] += w*Gi[1]
        gs.append(-w*Li + 0.5)
    return val,gt,gs

random.seed(350077)

for _ in range(1000):
    theta=[random.uniform(-2,2),random.uniform(-2,2)]
    s=[random.uniform(-3,3) for _ in range(3)]
    q=[10**random.uniform(-2,2) for _ in range(3)]
    sp=[x+math.log(y) for x,y in zip(s,q)]
    v1,g1,u1=objective_and_grad(theta,s)
    v2,g2,u2=objective_and_grad(theta,sp,q)
    off=0.5*sum(math.log(x) for x in q)
    assert abs(v2-v1-off)<3e-12*max(1.0,abs(v1),abs(v2))
    assert max(abs(a-b) for a,b in zip(g1,g2))<3e-12
    assert max(abs(a-b) for a,b in zip(u1,u2))<3e-12

def adam_step(x,g,m,v,t,lr,b1=0.9,b2=0.999,eps=1e-8):
    xx=[]; mm=[]; vv=[]
    for xi,gi,mi,vi in zip(x,g,m,v):
        mi=b1*mi+(1-b1)*gi
        vi=b2*vi+(1-b2)*gi*gi
        mh=mi/(1-b1**t)
        vh=vi/(1-b2**t)
        xx.append(xi-lr*mh/(math.sqrt(vh)+eps))
        mm.append(mi); vv.append(vi)
    return xx,mm,vv

q=[7.0,0.13,3.2]
theta=[0.4,-0.8]
s=[0.2,-0.4,0.1]
theta2=theta[:]
s2=[x+math.log(y) for x,y in zip(s,q)]
mt=[0.0,0.0]; vt=[0.0,0.0]
ms=[0.0]*3; vs=[0.0]*3
mt2=mt[:]; vt2=vt[:]; ms2=ms[:]; vs2=vs[:]

for t in range(1,401):
    _,gt,gs=objective_and_grad(theta,s)
    _,gt2,gs2=objective_and_grad(theta2,s2,q)
    assert max(abs(a-b) for a,b in zip(gt,gt2))<5e-12
    assert max(abs(a-b) for a,b in zip(gs,gs2))<5e-12
    theta,mt,vt=adam_step(theta,gt,mt,vt,t,0.006)
    s,ms,vs=adam_step(s,gs,ms,vs,t,0.009)
    theta2,mt2,vt2=adam_step(theta2,gt2,mt2,vt2,t,0.006)
    s2,ms2,vs2=adam_step(s2,gs2,ms2,vs2,t,0.009)
    assert max(abs(a-b) for a,b in zip(theta,theta2))<5e-11
    assert max(abs((b-a)-math.log(qi)) for a,b,qi in zip(s,s2,q))<5e-11

theta=[0.4,-0.8]
s=[0.0,0.0,0.0]
_,g0,u0=objective_and_grad(theta,s)
_,gq,uq=objective_and_grad(theta,s,q)
assert max(abs(a-b) for a,b in zip(g0,gq))>1e-3
assert max(abs(a-b) for a,b in zip(u0,uq))>1e-3

for c in (0.1,0.7,2.0,11.0):
    s0=-0.3
    sigma=math.exp(0.5*s0)
    sp=s0+math.log(c*c)
    sigmap=math.exp(0.5*sp)
    assert abs(sigmap-c*sigma)<1e-12

print("verification passed")
