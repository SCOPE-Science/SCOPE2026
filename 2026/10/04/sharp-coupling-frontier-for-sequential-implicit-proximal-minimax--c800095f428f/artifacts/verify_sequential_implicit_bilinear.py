import cmath
import math

def matrix(t,k):
    d=(1+t)**2
    return (
        ((1+t-k*k*t*t)/d, -k*t/d),
        (k*t*(1+t)/d, (1+t)/d),
    )

def eigs(t,k):
    M=matrix(t,k)
    T=M[0][0]+M[1][1]
    D=M[0][0]*M[1][1]-M[0][1]*M[1][0]
    disc=cmath.sqrt(T*T-4*D)
    return (T+disc)/2,(T-disc)/2

def q(t,k):
    return max(abs(z) for z in eigs(t,k))

for k,t in [(0.5,0.2),(1.0,3.0),(2.0,0.4),(3.0,0.7),(5.0,0.2)]:
    M=matrix(t,k)
    T=M[0][0]+M[1][1]
    D=M[0][0]*M[1][1]-M[0][1]*M[1][0]
    assert abs(T-(2+2*t-k*k*t*t)/(1+t)**2) < 1e-13
    assert abs(D-1/(1+t)**2) < 1e-13
    j1=1-T+D
    j2=1+T+D
    j3=1-D
    assert abs(j1-(1+k*k)*t*t/(1+t)**2) < 1e-12
    assert abs(j2-(4+4*t+(1-k*k)*t*t)/(1+t)**2) < 1e-12
    assert abs(j3-t*(2+t)/(1+t)**2) < 1e-12

# All-step stable regime.
for k in [0.1,0.5,1.0]:
    for t in [1e-3,0.1,1,10,1e3]:
        assert q(t,k) < 1

# Strong-coupling finite boundary and flip.
for k in [1.1,2.0,3.0,8.0]:
    ts=2/(k-1)
    vals=eigs(ts,k)
    assert min(abs(z+1) for z in vals) < 2e-10
    assert q(0.999*ts,k) < 1
    assert q(1.001*ts,k) > 1

# Unique collision optimizer: check formula, neighborhood, and root coalescence.
for k in [0.1,0.5,1.0,1.1,2.0,5.0,20.0]:
    s=math.sqrt(1+k*k)
    ts=2/(s-1)
    qs=(s-1)/(s+1)
    roots=eigs(ts,k)
    assert abs(abs(roots[0])-qs) < 2e-8
    assert abs(abs(roots[1])-qs) < 2e-8
    assert q(0.9*ts,k) > qs
    assert q(1.1*ts,k) > qs
    if k>1:
        assert ts < 2/(k-1)

# On the complex branch q is exactly 1/(1+t).
for k in [0.5,1.0,2.0,5.0]:
    ts=2/(math.sqrt(1+k*k)-1)
    for frac in [0.1,0.3,0.7,0.99]:
        t=frac*ts
        assert abs(q(t,k)-1/(1+t)) < 2e-12

# Full simultaneous resolvent is unconditionally stable and strictly improves.
def qfull(t,k):
    return 1/math.sqrt((1+t)**2+(k*t)**2)

for k in [0.5,1.0,2.0,10.0]:
    vals=[qfull(t,k) for t in [0.01,0.1,1,10,100]]
    assert all(vals[i+1] < vals[i] for i in range(len(vals)-1))
    assert all(v < 1 for v in vals)

print("VERIFY_OK")
