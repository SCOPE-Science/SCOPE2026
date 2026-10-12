#!/usr/bin/env python3
import math

def dephasing_coeff(N,j):
    # vacuum has z=+1 at every site; one excitation at j has z=-1 only there.
    s=0.0
    for ell in range(N):
        zv=1
        zj=-1 if ell==j else 1
        s += 0.5*(zv*zj-1)
    return s

for N in range(1,13):
    for j in range(N):
        assert dephasing_coeff(N,j)==-1.0

for p_i in range(11):
    p=p_i/10.0
    for x in (0.01,0.1,0.5,1.0,2.0,5.0):
        c=math.exp(-x)
        det=-(c*c)/4.0
        assert det < 0.0
        lam=((1-p)-math.sqrt((1-p)*(1-p)+4*c*c))/4.0
        assert lam < 0.0
        # The least-negative case over p in [0,1] occurs at p=0.
        bound=(1-math.sqrt(1+4*c*c))/4.0
        assert lam <= bound + 1e-15

# If the coherence vanishes, the partial-transpose block is diagonal and PSD.
for p_i in range(11):
    p=p_i/10.0
    c=0.0
    det=0.0
    lam=((1-p)-math.sqrt((1-p)*(1-p)+4*c*c))/4.0
    assert abs(det)<1e-15 and abs(lam)<1e-15
print('VERIFY_OK')
