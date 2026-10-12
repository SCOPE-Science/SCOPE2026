import math
import random

def adam_gc_first(h, alpha=0.03, beta1=0.9, beta2=0.999, eps=1e-8):
    # Exact first source-form Adam-GC step from zero moments.
    m=[(1-beta1)*x for x in h]
    v=[(1-beta2)*x*x for x in h]
    mhat=[x/(1-beta1) for x in m]
    vhat=[x/(1-beta2) for x in v]
    return [-alpha*mh/(math.sqrt(vh)+eps) for mh,vh in zip(mhat,vhat)]

def mean(x):
    return sum(x)/len(x)

def center(x):
    m=mean(x)
    return [v-m for v in x]

random.seed(350078)

# Formula and bound over randomized centered gradients.
for d in range(2,65):
    for _ in range(300):
        h=center([random.uniform(-100,100) for _ in range(d)])
        if max(abs(x) for x in h)<1e-12:
            continue
        alpha=10**random.uniform(-3,-0.2)
        eps=10**random.uniform(-10,1)
        step=adam_gc_first(h,alpha=alpha,eps=eps)
        drift=mean(step)
        closed=-(alpha/d)*sum(x/(abs(x)+eps) for x in h)
        assert abs(drift-closed)<2e-12*max(1.0,abs(closed))
        if d==2:
            assert abs(drift)<2e-12
        else:
            assert abs(drift) < alpha*(d-2)/d + 2e-12

# Sharp family approaches the supremum.
for d in (3,4,8,16,64):
    alpha=0.07
    eps=1.0
    target=alpha*(d-2)/d
    prev=0.0
    for a in (1.0,10.0,1e2,1e4,1e8):
        h=[a]*(d-1)+[-(d-1)*a]
        drift=abs(mean(adam_gc_first(h,alpha=alpha,eps=eps)))
        assert drift >= prev-1e-14
        assert drift < target+1e-12
        prev=drift
    assert target-prev < 1e-7

# Final-delta centralization exactly restores zero mean, up to floating arithmetic.
for d in range(2,65):
    for _ in range(100):
        delta=[random.uniform(-10,10) for _ in range(d)]
        md=mean(delta)
        repaired=[x-md for x in delta]
        assert abs(sum(repaired))<1e-11*max(1.0,sum(abs(x) for x in delta))

# First-step formula does not depend on beta values after bias correction.
h=[2.0,-0.7,-1.3]
base=adam_gc_first(h,beta1=0.1,beta2=0.2,eps=1e-5)
for b1,b2 in ((0.5,0.8),(0.9,0.999),(0.99,0.9999)):
    cur=adam_gc_first(h,beta1=b1,beta2=b2,eps=1e-5)
    assert max(abs(a-b) for a,b in zip(base,cur))<1e-12

print("verification passed")
