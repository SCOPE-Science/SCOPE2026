#!/usr/bin/env python3
import math
import cmath

def step(state,theta):
    c=math.cos(theta); s=math.sin(theta)
    out={}
    for (coin,x),amp in state.items():
        if coin==0:
            a0=c*amp; a1=s*amp
        else:
            a0=s*amp; a1=-c*amp
        out[(0,x-1)]=out.get((0,x-1),0j)+a0
        out[(1,x+1)]=out.get((1,x+1),0j)+a1
    return out

def probs(theta,n):
    st={(0,0):1/math.sqrt(2),(1,0):1j/math.sqrt(2)}
    for _ in range(n): st=step(st,theta)
    p={}
    for (coin,x),amp in st.items(): p[x]=p.get(x,0.0)+abs(amp)**2
    return p

def entropy(p):
    return -sum(v*math.log(v,2) for v in p.values() if v>0)

def formula2(theta):
    c=math.cos(theta); s=math.sin(theta)
    return {-2:c*c/2,0:s*s,2:c*c/2}

def formula3(theta):
    c=math.cos(theta)
    return {-3:c**4/2,-1:(1-c**4)/2,1:(1-c**4)/2,3:c**4/2}

def maxdiff(a,b):
    ks=set(a)|set(b)
    return max(abs(a.get(k,0)-b.get(k,0)) for k in ks)

def main():
    comparisons=0
    for j in range(101):
        th=(math.pi/2)*j/100
        assert maxdiff(probs(th,2),formula2(th))<2e-13
        assert maxdiff(probs(th,3),formula3(th))<3e-13
        comparisons+=2

    th2=math.asin(1/math.sqrt(3))
    th3=math.acos(2**(-0.25))
    p2=probs(th2,2); p3=probs(th3,3)
    assert max(abs(v-1/3) for v in p2.values())<2e-13
    assert max(abs(v-1/4) for v in p3.values())<2e-13
    h2=entropy(p2); h3=entropy(p3)
    assert abs(h2-math.log(3,2))<2e-13
    assert abs(h3-2.0)<2e-13

    had=math.pi/4
    hh2=entropy(probs(had,2)); hh3=entropy(probs(had,3))
    assert abs(hh2-1.5)<2e-13
    assert abs(hh3-(3-0.75*math.log(3,2)))<2e-13
    assert h2>hh2 and h3>hh3

    # One-step entropy is exactly one across the parameter range.
    for j in range(101):
        th=(math.pi/2)*j/100
        assert abs(entropy(probs(th,1))-1.0)<2e-13

    # Supplementary dense-grid localization.
    N=200000
    best2=(-1,None); best3=(-1,None)
    for j in range(N+1):
        th=(math.pi/2)*j/N
        e2=entropy(formula2(th)); e3=entropy(formula3(th))
        if e2>best2[0]: best2=(e2,th)
        if e3>best3[0]: best3=(e3,th)
    step_size=(math.pi/2)/N
    assert abs(best2[1]-th2)<=step_size
    assert abs(best3[1]-th3)<=step_size

    print('VERIFY_OK')
    print('formula_comparisons =',comparisons)
    print('theta2_star =',format(th2,'.15f'))
    print('H2_star =',format(h2,'.15f'))
    print('H2_Hadamard =',format(hh2,'.15f'))
    print('theta3_star =',format(th3,'.15f'))
    print('H3_star =',format(h3,'.15f'))
    print('H3_Hadamard =',format(hh3,'.15f'))
    print('grid_points =',N+1)

if __name__=='__main__':
    main()
