#!/usr/bin/env python3
"""Independent interpolation census using SymPy gcd/factorization."""
from itertools import product
from collections import Counter
from sympy import symbols, Poly
P=5;x=symbols('x')

def interpolate(values):
    # Interpolate the unique degree <=4 polynomial through (0..4, v_i).
    r=Poly(0,x,modulus=P)
    for i,value in enumerate(values):
        b=Poly(1,x,modulus=P);d=1
        for j in range(P):
            if i==j:continue
            b*=Poly(x-j,x,modulus=P)
            d=d*(i-j)%P
        r+=b.mul_ground((value*pow(d,-1,P))%P)
    return r

cnt=Counter();smooth=[];vetted=[]
for vals in product((1,4),repeat=5):
    base=interpolate(vals)
    for top in (1,4):
        for free in range(5):
            f=base+Poly((x**5-x)*(top*x+free),x,modulus=P)
            coeff=tuple(int(f.nth(i))%5 for i in range(7))
            assert int(f.nth(6))%5==top
            assert tuple(int(f.eval(i))%5 for i in range(5))==vals
            if f.gcd(f.diff()).degree():
                cnt['singular']+=1;continue
            factors=f.factor_list()[1]
            partition=tuple(sorted(c.degree() for c,m in factors for _ in range(m)))
            cnt[partition]+=1
            smooth.append(coeff)
            vetted.append((coeff,partition))
assert len(smooth)==240 and cnt['singular']==80
assert {k:cnt[k] for k in ((2,4),(3,3),(6,))}=={(2,4):120,(3,3):40,(6,):80}
print('interpolated',len(smooth)+cnt['singular'],'smooth',len(smooth),'singular',cnt['singular'])
print('branch_partition_counts',[(str(k),v) for k,v in sorted(cnt.items(),key=lambda p:str(p[0])) if k!='singular'])
