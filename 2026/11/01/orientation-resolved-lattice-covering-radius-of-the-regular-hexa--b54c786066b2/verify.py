#!/usr/bin/env python3
"""Deterministic numerical diagnostics for the regular-hexagon covering profile.
The universal assertion is proved analytically in RESULT.md; these checks are not a proof.
Python standard library only.
"""
import math

SQ3 = math.sqrt(3.0)
STAR = math.atan((4.0-SQ3)/13.0)

def gauged(x, y):
    return max(abs(x)+abs(y)/SQ3, 2.0*abs(y)/SQ3)

def norm(x, y, t):
    c, s = math.cos(t), math.sin(t)
    return gauged(c*x+s*y,-s*x+c*y)

def radius_A(t):
    c, s = math.cos(t), math.sin(t)
    return ((SQ3+1)*c+(1-SQ3)*s)/(2*SQ3)

def radius_B(t):
    c, s = math.cos(t), math.sin(t)
    return ((SQ3+2)*c+s)/(3*SQ3)

def witness(t, branch):
    c, s = math.cos(t), math.sin(t)
    u = (c+s/SQ3)/2
    v = (c-SQ3*s)/2 if branch=='A' else ((4-SQ3)*c-s)/6
    return (c*u-s*v, s*u+c*v)

def close(a,b,tol=1e-11):
    assert abs(a-b)<=tol, (a,b)

checks=0
close(math.tan(STAR),(4-SQ3)/13); checks+=1
close(radius_A(STAR),radius_B(STAR)); checks+=1
close(radius_A(STAR)**2,(11+6*SQ3)/39); checks+=1
close(radius_A(0),1/(3-SQ3)); checks+=1
for i in range(2001):
    t=(math.pi/12)*i/2000
    a,b=radius_A(t),radius_B(t)
    r=max(a,b)
    branch='A' if t<=STAR else 'B'
    x,y=witness(t,branch)
    assert -1e-12<=x<=.5+1e-12 and -1e-12<=y<=.5+1e-12
    distances=[norm(x-j,y-k,t) for j,k in [(0,0),(1,0),(0,1),(1,1)]]
    for d in distances[:3]: close(d,r)
    assert distances[3]>=r-1e-12
    for j in range(-2,4):
        for k in range(-2,4):
            if j in (0,1) and k in (0,1): continue
            assert norm(x-j,y-k,t)>=1-1e-12
    checks+=1

for i in range(31):
    t=(math.pi/12)*i/30
    r=max(radius_A(t),radius_B(t))
    # All the sampled points in a fundamental square are covered by one of
    # its four corners (the full assertion follows from the triangle lemma).
    for j in range(61):
        x=j/60
        for k in range(61):
            y=k/60
            d=min(norm(x-a,y-b,t) for a,b in ((0,0),(1,0),(0,1),(1,1)))
            assert d<=r+1e-11, (i,j,k,d,r)
            checks+=1

# Exact minimizer is checked algebraically in RESULT.md; numerical scan is
# a consistency test for strict branch monotonicity and the cusp.
for i in range(1,1001):
    t=STAR*i/1001
    assert radius_A(t)>radius_A(STAR)
    t=STAR+(math.pi/12-STAR)*i/1001
    assert radius_B(t)>radius_B(STAR)
    checks+=2
print(f'PASS: {checks} deterministic covering-profile diagnostics')
