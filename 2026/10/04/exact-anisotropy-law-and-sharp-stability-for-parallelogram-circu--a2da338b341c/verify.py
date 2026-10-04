#!/usr/bin/env python3
import math, random

rng = random.Random(20261001)
worst_inc = 0.0
worst_area = 0.0
worst_cosh = 0.0
worst_defect = 0.0
min_stability = float("inf")
count = 0

def det2(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def inv2(A):
    d=det2(A)
    return [[A[1][1]/d,-A[0][1]/d],[-A[1][0]/d,A[0][0]/d]]

def transpose(A):
    return [[A[0][0],A[1][0]],[A[0][1],A[1][1]]]

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def mv(A,x):
    return [A[0][0]*x[0]+A[0][1]*x[1], A[1][0]*x[0]+A[1][1]*x[1]]

def dot(x,y): return x[0]*y[0]+x[1]*y[1]

def quad(H,x): return dot(x,mv(H,x))

def col(A,j): return [A[0][j],A[1][j]]

for _ in range(12000):
    while True:
        P=[[rng.uniform(-3,3),rng.uniform(-3,3)],[rng.uniform(-3,3),rng.uniform(-3,3)]]
        if abs(det2(P))>0.25: break
    c=rng.uniform(-0.985,0.985)
    K=[[1.0,c],[c,1.0]]
    Pinv=inv2(P)
    H=mm(transpose(Pinv),mm(K,Pinv))
    p,q=col(P,0),col(P,1)
    for v in (p,[-p[0],-p[1]],q,[-q[0],-q[1]]):
        worst_inc=max(worst_inc,abs(quad(H,v)-1.0))
    area_q=2.0*abs(det2(P))
    area_e=math.pi/math.sqrt(det2(H))
    ratio=area_e/area_q
    target=math.pi/(2.0*math.sqrt(1.0-c*c))
    worst_area=max(worst_area,abs(ratio-target))
    delta=math.atanh(abs(c))
    target2=(math.pi/2.0)*math.cosh(delta)
    worst_cosh=max(worst_cosh,abs(ratio-target2))
    defect=ratio-math.pi/2.0
    exact=math.pi*math.sinh(delta/2.0)**2
    worst_defect=max(worst_defect,abs(defect-exact))
    min_stability=min(min_stability,defect-(math.pi/4.0)*delta*delta)
    # additional affine change L; recompute and test incidence/area ratio
    while True:
        L=[[rng.uniform(-2,2),rng.uniform(-2,2)],[rng.uniform(-2,2),rng.uniform(-2,2)]]
        if abs(det2(L))>0.2: break
    Linv=inv2(L)
    H2=mm(transpose(Linv),mm(H,Linv))
    P2=mm(L,P)
    p2,q2=col(P2,0),col(P2,1)
    for v in (p2,q2):
        worst_inc=max(worst_inc,abs(quad(H2,v)-1.0))
    area_q2=2.0*abs(det2(P2))
    area_e2=math.pi/math.sqrt(det2(H2))
    worst_area=max(worst_area,abs(area_e2/area_q2-target))
    count += 1

# Near-minimizer sequence confirms optimal quadratic coefficient.
ratios=[]
for d in (1e-2,5e-3,2e-3,1e-3):
    defect=(math.pi/2.0)*(math.cosh(d)-1.0)
    ratios.append(defect/(d*d))
limit_err=abs(ratios[-1]-math.pi/4.0)

assert worst_inc < 1e-7, worst_inc
assert worst_area < 1e-7, worst_area
assert worst_cosh < 1e-7, worst_cosh
assert worst_defect < 1e-7, worst_defect
assert min_stability > -1e-10, min_stability
assert limit_err < 1e-6, (limit_err, ratios)
print("VERIFY_OK")
print("cases", count)
print("worst_vertex_incidence", f"{worst_inc:.3e}")
print("worst_area_formula", f"{worst_area:.3e}")
print("worst_cosh_formula", f"{worst_cosh:.3e}")
print("worst_defect_identity", f"{worst_defect:.3e}")
print("minimum_stability_margin", f"{min_stability:.3e}")
print("near_zero_quadratic_ratio", [f"{x:.12f}" for x in ratios])
