"""Exact-rational checks for finite-bit fused Horner limit."""
from fractions import Fraction as F
from collections import deque
from random import Random

def exp2_floor(z):
    assert z > 0
    e = z.numerator.bit_length() - z.denominator.bit_length()
    power = F(2**e) if e >= 0 else F(1,2**(-e))
    if z < power:
        e -= 1
    elif z >= 2*power:
        e += 1
    return e

def gap(z, bits):
    e = exp2_floor(z)
    k = e-bits+1
    return F(2**k) if k >= 0 else F(1, 2**(-k))

def floor_binary(z,bits):
    d = gap(z,bits)
    return (z//d)*d

def ceil_binary(z,bits):
    low = floor_binary(z,bits)
    return low if low==z else low+gap(z,bits)

def transitions(z, x, p, r):
    exact = 1 + x*z
    low,high = floor_binary(exact,p),ceil_binary(exact,p)
    if high==low: return [(low,F(1))]
    small = floor_binary(exact,p+r)
    prob=(small-low)/(high-low)
    assert 0<=prob<=1,(z,x,p,r,low,high,small,prob)
    return [(value,weight) for value,weight in [(low,1-prob),(high,prob)] if weight>0]

def prediction(p,q,r):
    L=F(2**q); delta=F(2**(q-p))
    return L-(2**(q-r)-1)*delta if r<q else L

def graph_check(p,q,r):
    x=1-F(1,2**q)
    y=F(1)
    todo=deque([y]); reached={y}; trans={}; count=0
    while todo:
        z=todo.popleft()
        nxt=transitions(z,x,p,r)
        trans[z]=nxt
        assert z>=1 and z<=2**q
        assert all(t>=z and t<=2**q for t,pp in nxt if pp>0)
        for t,pp in nxt:
            if pp>0 and t not in reached:
                reached.add(t);todo.append(t)
        count+=1
        assert count<2**(p+2)
    absorbing={z for z,nxt in trans.items() if len(nxt)==1 and nxt[0][0]==z and nxt[0][1]==1}
    assert absorbing=={prediction(p,q,r)}, (p,q,r,absorbing,prediction(p,q,r))
    # The final predecessor is inevitable, and its waiting probability is exact.
    L=F(2**q)
    pred=prediction(p,q,r)-F(2**(q-p))
    assert pred in reached
    step=dict(trans[pred])
    assert step[pred+F(2**(q-p))] == (F(1,2**r) if r<q else F(1,L)), (p,q,r,step)
    assert step[pred]==1-step[pred+F(2**(q-p))]
    for z,nxt in trans.items():
        if z!=prediction(p,q,r):
            assert any(t>z and pp>0 for t,pp in nxt)
    return count

def run():
    checks=0;max_states=0
    for p in range(4,11):
      for q in range(2,p):
        for r in range(1,q+3):
            num=graph_check(p,q,r)
            checks+=1;max_states=max(max_states,num)
    # Verify the normalized threshold case with exact arithmetic for a large trap.
    p,q,r=8,7,1
    target=prediction(p,q,r)
    assert target==F(193,2), target
    assert target/F(128)==F(193,256)
    rng=Random(234781)
    z=F(1)
    steps=0
    while z!=target and steps<200000:
        nxt=transitions(z,1-F(1,2**q),p,r)
        u=rng.random();cdf=0.
        for v,pr in nxt:
            cdf+=float(pr)
            if u<=cdf:
                z=v;break
        steps+=1
    assert z==target
    print(f"PASS: {checks} distinct parameter triples; max {max_states} reachable states; sample absorption {steps} steps, terminal {target}")
if __name__=='__main__':run()
