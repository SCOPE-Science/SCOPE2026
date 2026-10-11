import math
import random

def lq2(v,q):
    if math.isinf(q):
        return max(abs(v[0]),abs(v[1]))
    return (abs(v[0])**q+abs(v[1])**q)**(1.0/q)

random.seed(230082)
fiber_checks=0
for q in [2.0,2.25,3.0,4.0,8.0,20.0]:
    for _ in range(2000):
        z=[random.uniform(-1,1),random.uniform(-1,1)]
        n=lq2(z,q)
        if n<1e-12:
            continue
        z=[z[0]/n,z[1]/n]
        u=[z[1],-z[0]]
        assert abs(lq2(u,q)-1.0)<1e-11
        A=lq2([z[0]+u[0],z[1]+u[1]],q)
        B=lq2([z[0]-u[0],z[1]-u[1]],q)
        assert A+1e-11 >= 2.0**(1.0/q)
        assert B+1e-11 >= 2.0**(1.0/q)
        fiber_checks+=1

envelope_checks=0
for q in [2.0,2.5,3.0,4.0,8.0,20.0]:
    for p in [1.0,1.25,1.5,2.0,3.0,5.0,10.0,30.0]:
        target=max(2.0,2.0**(p/q))
        for k in range(1001):
            a=k/1000.0
            H=(1.0+a**q)**(p/q)+1.0-a**p
            assert H <= target+2e-10*max(1.0,target)
            envelope_checks+=1

# Infinity-fiber endpoint.
for p in [1.0,1.5,2.0,4.0,10.0]:
    for k in range(1001):
        a=k/1000.0
        H=2.0-a**p
        assert H<=2.0+1e-12
        envelope_checks+=1

print(
    "VERIFY_OK "
    f"fiber_checks={fiber_checks} envelope_checks={envelope_checks} "
    "phase=p_equals_q formula=2^(1/min(p,q))"
)
