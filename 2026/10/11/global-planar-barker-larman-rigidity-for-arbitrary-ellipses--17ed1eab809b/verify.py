#!/usr/bin/env python3
import math

def det2(Q):
    return Q[0][0]*Q[1][1]-Q[0][1]*Q[1][0]

def inv2(Q):
    d=det2(Q)
    return [[Q[1][1]/d,-Q[0][1]/d],[-Q[1][0]/d,Q[0][0]/d]]

def dot(a,b):
    return a[0]*b[0]+a[1]*b[1]

def mv(Q,x):
    return [Q[0][0]*x[0]+Q[0][1]*x[1],
            Q[1][0]*x[0]+Q[1][1]*x[1]]

def chord_formula(c,Q,r,u):
    q=dot(u,mv(Q,u))
    s=r-dot(u,c)
    D=det2(Q)
    rad=D*(q-s*s)/(q*q)
    assert rad>0
    return 2*math.sqrt(rad)

def chord_direct(c,Q,r,u):
    v=[-u[1],u[0]]
    A=inv2(Q)
    x0=[r*u[0]-c[0],r*u[1]-c[1]]
    av=dot(v,mv(A,v))
    bv=2*dot(v,mv(A,x0))
    cv=dot(x0,mv(A,x0))-1
    disc=bv*bv-4*av*cv
    assert disc>0
    return math.sqrt(disc)/av

cases=[
    ([0.20,-0.10], [[4.0,0.6],[0.6,2.5]], 0.30),
    ([-0.15,0.25], [[3.0,-0.4],[-0.4,2.0]], 0.25),
    ([0.0,0.0], [[2.7,0.5],[0.5,1.8]], 0.20),
]
angles=[0.0,0.17,0.61,1.1,2.0,3.4,5.2]
for c,Q,r in cases:
    for th in angles:
        u=[math.cos(th),math.sin(th)]
        a=chord_formula(c,Q,r,u)
        b=chord_direct(c,Q,r,u)
        assert abs(a-b)<2e-12,(c,Q,r,th,a,b)

# Exact antipodal odd-part identity, checked numerically on deterministic data.
for c,Q,r in cases[:2]:
    D=det2(Q)
    for th in angles:
        u=[math.cos(th),math.sin(th)]
        um=[-u[0],-u[1]]
        Lp=chord_formula(c,Q,r,u)
        Lm=chord_formula(c,Q,r,um)
        q=dot(u,mv(Q,u))
        lhs=(Lp*Lp-Lm*Lm)/(16*r)
        rhs=D*dot(c,u)/(q*q)
        assert abs(lhs-rhs)<3e-12,(lhs,rhs)

# The proportional-shape scaling step in the proof:
# if Q2=k Q1 and the center agrees, equality of full data forces k=1.
c=[0.18,-0.07]
Q=[[3.2,0.3],[0.3,1.9]]
r=0.22
for k in (0.7,1.0,1.4):
    Qk=[[k*Q[0][0],k*Q[0][1]],[k*Q[1][0],k*Q[1][1]]]
    diffs=[]
    for th in angles:
        u=[math.cos(th),math.sin(th)]
        diffs.append(abs(chord_formula(c,Q,r,u)-chord_formula(c,Qk,r,u)))
    if k==1.0:
        assert max(diffs)<1e-14
    else:
        assert max(diffs)>1e-3

print("VERIFY_OK")
print("direct_affine_chord_formula = passed")
print("antipodal_odd_identity = passed")
print("proportional_shape_scale_test = passed")
