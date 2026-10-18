"""Independent exhaustive obstruction to four rational total-ramification fibres."""
from collections import Counter
from group_orbits import ACTIONS, transform, total, fibre

def eval_deriv(c,t):
    if t==0:return c&1,(c>>1)&1
    if t==1:return c.bit_count()&1, ((c>>1)^(c>>3))&1
    return (c>>3)&1,(c>>2)&1

def has_rational_singularity(m):
    for a in range(3):
        for b in range(3):
            v,dy=eval_deriv(fibre(m,0,a),b)
            v2,dx=eval_deriv(fibre(m,1,b),a)
            assert v==v2
            if v==dx==dy==0:return True
    return False

bad=[];locgood=[]
for m in range(1,65536):
    if total(m,0)+total(m,1)>=4:
        bad.append(m)
        if not has_rational_singularity(m):locgood.append(m)
assert len(bad)==1128 and len(locgood)==18
assert len(bad)-len(locgood)==1110
orbit={transform(6854,g) for g in ACTIONS}
assert orbit==set(locgood) and len(orbit)==18
# The remaining orbit has a singular point over F4 at (alpha,alpha+1), alpha^2+alpha+1=0.
def mul(a,b):
    out=0
    while b:
        if b&1:out^=a
        b>>=1;a<<=1
        if a&4:a^=7
    return out
x=2;y=3
P=[1,x,mul(x,x),mul(mul(x,x),x)]
Q=[1,y,mul(y,y),mul(mul(y,y),y)]
F=Fx=Fy=0
for j in range(4):
    for i in range(4):
        if (6854>>(4*j+i))&1:
            F^=mul(P[i],Q[j])
            if i&1:Fx^=mul(P[i-1],Q[j])
            if j&1:Fy^=mul(P[i],Q[j-1])
assert (F,Fx,Fy)==(0,0,0)
print('sharp obstruction: 1128 masks have >=4 total fibres, 1110 rational singularities,')
print('other 18 = one orbit, representative 6854 singular over F4 at (alpha,alpha+1)')
