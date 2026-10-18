"""Exact endpoint and conjugacy checks for a geometric-series host-parasitoid map.

Run: python check.py
These checks corroborate rational identities in the analytical proof;
they do not replace the infinite-period exclusion argument.
"""
from fractions import Fraction as Q
from math import sqrt, log

def rational_steps(x,y):
    z=5*y*y/(x*(1+y))
    w=5*z*z/(y*(1+z))
    residual=5*z*(5-z)-y*(1+z)
    closure=z*(1+w)-5*w
    assert closure == -z*residual/(y*(1+z))
    return z,w,residual

cases=((Q(41,4),Q(41,6),Q(410,141),Q(49241,13254)),
       (Q(19),Q(19,2),Q(95,42),Q(-19,882)))
for x,y,z_target,r_target in cases:
    # Verify exact square-root branch Y=X sqrt(5/(1+X)).
    assert y>0 and y*y*(1+x)==5*x*x
    z,w,res=rational_steps(x,y)
    assert z==z_target and res==r_target and w>0
assert cases[0][3]>0>cases[1][3]

def R(x):
    y=x*sqrt(5/(1+x))
    z=5*y*y/(x*(1+y))
    w=5*z*z/(y*(1+z))
    return 5*z*(5-z)-y*(1+z), [x,y,z,w,w,z,y]

lo,hi=10.25,19.0
for _ in range(65):
    mid=(lo+hi)/2
    if R(mid)[0]>0:lo=mid
    else:hi=mid
rr,seq=R((lo+hi)/2)
assert abs(rr)<1e-11
for i in range(7):
    j=(i+1)%7
    k=(i+2)%7
    assert abs(seq[k]*seq[i] - 5*seq[j]*seq[j]/(1+seq[j]))<1e-9
ys=[seq[(i+1)%7]*(1+seq[i])/seq[i] for i in range(7)]
for i in range(7):
    j=(i+1)%7
    f1=ys[i]*seq[i]/(1+seq[i])
    f2=5*ys[i]/(1+seq[i])
    assert abs(f1-seq[j])<1e-10 and abs(f2-ys[j])<1e-10
assert seq[0]>10 and min(seq)>0 and max(seq)-min(seq)>1
print('VERIFY_OK: exact endpoint signs, cyclic closure, positive 7-cycle reconstruction')
