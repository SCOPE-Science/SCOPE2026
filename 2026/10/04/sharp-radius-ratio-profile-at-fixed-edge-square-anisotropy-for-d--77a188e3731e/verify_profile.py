#!/usr/bin/env python3
import math, random

SEED = 210031
RNG = random.Random(SEED)
TOL = 2e-12
checks = 0
max_radius_formula_err = 0.0
max_profile_violation = 0.0
max_edge_q_err = 0.0
max_param_err = 0.0
max_endpoint_err = 0.0

def profile_bounds(q):
    root = math.sqrt(q)
    upper2 = (1.0 - 3.0*q + 2.0*q*root)/(9.0*(1.0-q))
    if q < 0.25:
        lower2 = (1.0 - 3.0*q - 2.0*q*root)/(9.0*(1.0-q))
    else:
        lower2 = 0.0
    return lower2, upper2

def cross(u,v):
    return (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])

def sub(u,v):
    return tuple(u[i]-v[i] for i in range(3))

def dot(u,v):
    return sum(u[i]*v[i] for i in range(3))

def norm(u):
    return math.sqrt(dot(u,u))

# Random coordinate disphenoids. Check geometric radius formula, edge anisotropy formula,
# and the claimed sharp interval pointwise.
for _ in range(20000):
    x = math.exp(RNG.uniform(-2.0, 2.0))
    y = math.exp(RNG.uniform(-2.0, 2.0))
    z = math.exp(RNG.uniform(-2.0, 2.0))
    aa, bb, cc = x*x, y*y, z*z
    S = aa+bb+cc
    P = aa*bb+bb*cc+cc*aa
    R = math.sqrt(S)
    r = x*y*z/math.sqrt(P)

    A=(x,y,z); B=(x,-y,-z); C=(-x,y,-z); D=(-x,-y,z)
    # r from 3V/surface area; all four faces congruent.
    det = dot(sub(B,A), cross(sub(C,A), sub(D,A)))
    V = abs(det)/6.0
    face_area = norm(cross(sub(B,A), sub(C,A)))/2.0
    r2 = 3.0*V/(4.0*face_area)
    max_radius_formula_err=max(max_radius_formula_err, abs(r-r2)/max(1.0,r))

    l2 = 4.0*(bb+cc)
    m2 = 4.0*(aa+cc)
    n2 = 4.0*(aa+bb)
    L = l2+m2+n2
    q_edges = 2.0*((l2-m2)**2+(m2-n2)**2+(n2-l2)**2)/(L*L)
    q_coords = ((aa-bb)**2+(bb-cc)**2+(cc-aa)**2)/(2.0*S*S)
    max_edge_q_err=max(max_edge_q_err, abs(q_edges-q_coords))
    q=q_edges
    lo,hi=profile_bounds(q)
    ratio2=(r/R)**2
    max_profile_violation=max(max_profile_violation, lo-ratio2, ratio2-hi, 0.0)
    checks += 5

# Exact trigonometric parametrization, sampled deterministically.
for _ in range(20000):
    s=RNG.random()*0.999999
    theta=RNG.uniform(-math.pi, math.pi)
    p=[(1.0+2.0*s*math.cos(theta+2.0*math.pi*k/3.0))/3.0 for k in range(3)]
    if min(p) <= 0:
        continue
    q=s*s
    Psum=p[0]*p[1]+p[1]*p[2]+p[2]*p[0]
    prod=p[0]*p[1]*p[2]
    ratio2=prod/Psum
    closed=(1.0-3.0*q+2.0*q*s*math.cos(3.0*theta))/(9.0*(1.0-q))
    max_param_err=max(max_param_err, abs(ratio2-closed))
    lo,hi=profile_bounds(q)
    max_profile_violation=max(max_profile_violation, lo-ratio2, ratio2-hi, 0.0)
    checks += 3

# Equality branches.
for j in range(1,10000):
    s=0.999*j/10000.0
    q=s*s
    pmax=((1+2*s)/3.0,(1-s)/3.0,(1-s)/3.0)
    Psum=pmax[0]*pmax[1]+pmax[1]*pmax[2]+pmax[2]*pmax[0]
    val=pmax[0]*pmax[1]*pmax[2]/Psum
    _,hi=profile_bounds(q)
    max_endpoint_err=max(max_endpoint_err,abs(val-hi))
    if s < 0.5:
        pmin=((1-2*s)/3.0,(1+s)/3.0,(1+s)/3.0)
        Psum=pmin[0]*pmin[1]+pmin[1]*pmin[2]+pmin[2]*pmin[0]
        val=pmin[0]*pmin[1]*pmin[2]/Psum
        lo,_=profile_bounds(q)
        max_endpoint_err=max(max_endpoint_err,abs(val-lo))
    checks += 2

assert max_radius_formula_err < TOL
assert max_edge_q_err < TOL
assert max_param_err < TOL
assert max_endpoint_err < TOL
assert max_profile_violation < TOL
print('VERIFY_OK')
print('seed',SEED)
print('checks',checks)
print('max_radius_formula_relative_error',format(max_radius_formula_err,'.3e'))
print('max_edge_anisotropy_error',format(max_edge_q_err,'.3e'))
print('max_parametrization_error',format(max_param_err,'.3e'))
print('max_endpoint_error',format(max_endpoint_err,'.3e'))
print('max_profile_violation',format(max_profile_violation,'.3e'))
