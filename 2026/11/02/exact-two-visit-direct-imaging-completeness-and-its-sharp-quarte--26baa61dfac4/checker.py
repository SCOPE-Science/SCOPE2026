#!/usr/bin/env python3
"""Numerical cross-checks of the ideal two-visit projected-separation theorem.

Run: python3 checker.py
Standard library only. The analytic proof in RESULT.md establishes the theorem;
these finite checks do not establish a continuum of parameter cases.
"""
import math
import random

PI=math.pi
assertions=0

def check(condition, context):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(context)

def lens(s, tau):
    h=math.sqrt(1-tau*tau)
    alpha=math.asin(tau)
    if s<=0.0:
        return 2*PI*(1-h)
    if s>=2*alpha-1e-12:
        return 0.0
    b=math.acos(max(-1., min(1.,h*math.tan(s/2)/tau)))
    g=math.acos(max(-1., min(1.,(math.cos(s)-h*h)/(tau*tau))))
    return 2*PI-4*h*b-2*g

def completion(tau, phase):
    d=math.acos(abs(math.cos(phase)))
    return 1-(lens(d,tau)+lens(PI-d,tau))/(2*PI)

def best(tau):
    h=math.sqrt(1-tau*tau)
    if tau<=2**-.5:
        return 1.0
    return 1+4*h/PI*math.acos(h/tau)-2/PI*math.acos(h*h/(tau*tau))

def lens_slope(s,tau):
    h=math.sqrt(1-tau*tau)
    if s>=2*math.asin(tau):return 0.0
    return -2*math.sqrt(max(0.,1-h*h/math.cos(s/2)**2))

# Independent geometric quadrature: integrate directly over isotropic
# viewing directions, rather than the derived cap-overlap formula.
def direct_grid(tau, phase, nz=420, nphi=800):
    h=math.sqrt(1-tau*tau)
    c,s=math.cos(phase),math.sin(phase)
    detections=0
    for j in range(nz):
        z=-1+2*(j+.5)/nz
        r=math.sqrt(max(0.,1-z*z))
        for k in range(nphi):
            x=r*math.cos(2*PI*(k+.5)/nphi)
            if abs(z)<=h or abs(c*z+s*x)<=h:
                detections+=1
    return detections/(nz*nphi)

for tau in [0.05,0.17,0.4,0.6,0.7071067811865476,0.72,0.8,0.9,0.98]:
    h=math.sqrt(1-tau*tau)
    check(abs(completion(tau,0)-h)<2e-14,'coincident visits')
    check(abs(completion(tau,PI/2)-best(tau))<2e-13,'closed form maximum')
    prev=-1.0
    for j in range(201):
        d=j*PI/400
        cur=completion(tau,d)
        check(-1e-12<=cur<=1+1e-12,'probability range')
        check(cur>=prev-1e-12,'phase monotonicity')
        check(cur<=best(tau)+1e-12,'maximality')
        check(abs(cur-completion(tau,PI-d))<1e-12,'antipodal phase symmetry')
        prev=cur
    for j in range(1,35):
        s=j*(2*math.asin(tau))/36
        step=min(1e-5,s/4,(2*math.asin(tau)-s)/4)
        derivative=(lens(s+step,tau)-lens(s-step,tau))/(2*step)
        check(abs(derivative-lens_slope(s,tau))<2e-6,'lens derivative')
    if tau<2**-.5-1e-10:
        check(abs(completion(tau,2*math.asin(tau))-1)<2e-12,'guaranteed phase edge')
        check(abs(completion(tau,PI/2)-1)<2e-12,'guarantee plateau')

for tau,d in [(0.25,0.2),(0.65,0.5),(0.8,0.4),(0.8,PI/2),(0.92,0.9),(0.97,PI/2)]:
    analytic=completion(tau,d)
    direct=direct_grid(tau,d)
    check(abs(direct-analytic)<0.0045,'independent spherical grid quadrature')

# Directly test the orientation-wise optimal lower envelope on a dense
# azimuthal grid for edge-on viewing; analytic proof is in the manuscript.
for d in [0.15,0.33,0.7,1.1,PI/2]:
    expected=math.sin(d/2)
    samples=[max(abs(math.sin(x)),abs(math.sin(x+d)))
             for x in [j*PI/100000 for j in range(100000)]]
    check(min(samples)>=expected-2e-5,'minimax lower bound')
    check(min(samples)<=expected+2e-5,'minimax attained')

print(f'PASS: {assertions} finite assertions; independent spherical grid integration included.')
print('Example tau=4/5: single=',math.sqrt(1-0.8**2),
      'two=',best(.8),'first-visit conditional second detection=',
      (best(.8)-math.sqrt(1-.8**2))/(1-math.sqrt(1-.8**2)))
