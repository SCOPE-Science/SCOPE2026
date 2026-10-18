"""Independent checks of the finite-support martingale Sinkhorn recurrence.

Requires only the Python standard library. Run: python VERIFY.py
"""
import math
import random


def recover_R(a, q):
    # Solve sqrt(R^2-a^2)/(2(1-R))=q by bisection.
    lo, hi = a, 1.0
    for _ in range(90):
        mid = (lo+hi)/2
        if math.sqrt(max(mid*mid-a*a,0))/(2*(1-mid)) < q:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2


def dual_full_step(a, target, weights):
    # Independent first-principles row moment projection and column normalization.
    # Weights are the three positive factors nu(y)*exp(-psi(y)).
    outcomes=(-1,0,1)
    halves=[]
    for x in (-a,a):
        lo,hi=-100.,100.
        for _ in range(95):
            h=(lo+hi)/2
            raw=[weights[j]*math.exp(-h*(outcomes[j]-x)) for j in range(3)]
            sm=sum(raw)
            m=sum(outcomes[j]*raw[j] for j in range(3))/sm
            if m<x: hi=h  # mean decreases in h
            else: lo=h
        h=(lo+hi)/2
        raw=[weights[j]*math.exp(-h*(outcomes[j]-x)) for j in range(3)]
        sm=sum(raw)
        halves.append([v/sm for v in raw])
    col=[(halves[0][j]+halves[1][j])/2 for j in range(3)]
    nu=[target/2,1-target,target/2]
    nxt=[weights[j]*nu[j]/col[j] for j in range(3)]
    return col,nxt,halves


def theory_step(a,target,q):
    R=recover_R(a,q)
    return q*target*(1-R)/((1-target)*R)


def KL_half(a,R,T):
    p=((R-a)/2,1-R,(R+a)/2)
    v=((T-a)/2,1-T,(T+a)/2)
    return sum(x*math.log(x/y) for x,y in zip(p,v))

rng=random.Random(20261016)
checks=0
for case in range(300):
    a=rng.uniform(.04,.88)
    T=rng.uniform(a+.0002,1-.0002)
    weights=[math.exp(rng.uniform(-4,4)) for _ in range(3)]
    q=math.sqrt(weights[0]*weights[2])/weights[1]
    col,nxt,halves=dual_full_step(a,T,weights)
    R=recover_R(a,q)
    assert abs(col[0]-R/2)<3e-12 and abs(col[1]-(1-R))<3e-12
    checks+=2
    for x,probs in zip((-a,a),halves):
        assert abs(probs[2]-probs[0]-x)<3e-12
        checks+=1
    newq=math.sqrt(nxt[0]*nxt[2])/nxt[1]
    qnext=theory_step(a,T,q)
    assert abs(newq/qnext-1)<1e-11
    checks+=1
    zstar=math.log(math.sqrt(T*T-a*a)/(2*(1-T)))
    z=math.log(q)
    if z<zstar:
        assert z<math.log(qnext)<zstar
    if z>zstar:
        assert zstar<math.log(qnext)<z
    checks+=1
    Rnow=R
    for k in range(45):
        q=theory_step(a,T,q)
        Rnew=recover_R(a,q)
        assert abs(Rnew-T)<=abs(Rnow-T)+1e-12
        Rnow=Rnew
        checks+=1

for a,T in ((.4,.6),(.2,.25),(.7,.9),(.31,.310001),(.01,.99)):
    zstar=math.log(math.sqrt(T*T-a*a)/(2*(1-T)))
    lam=a*a*(1-T)/(T*(T-a*a))
    for dz in (1e-3,1e-4,1e-5):
        z=zstar+dz
        f=math.log(theory_step(a,T,math.exp(z)))
        assert abs((f-zstar)/dz-lam) < .6*dz+2e-6
        checks+=1
    if T-a>1e-3:
        q=math.exp(zstar+.5)
        logs=[]
        for k in range(45):
            R=recover_R(a,q)
            logs.append(KL_half(a,R,T))
            q=theory_step(a,T,q)
            if abs(R-T)<1e-6:break
        ratios=[logs[i+1]/logs[i] for i in range(len(logs)-1) if logs[i]>1e-8 and logs[i+1]>1e-8]
        if len(ratios)>5:
            assert abs(ratios[-1]-lam*lam)<.03
            checks+=1

print('PASS',checks,'independent row/column normalization, recurrences, monotonicity, derivative and KL-rate checks')
