#!/usr/bin/env python3
from fractions import Fraction as F

def conv(a,b):
    out=[F(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out

def lc(seq):
    return all(seq[k]*seq[k] >= seq[k-1]*seq[k+1] for k in range(1,len(seq)-1))

def check_three_point(p,f0,f1,f2):
    q=1-p
    A=q+p*f0
    B=p*f1
    C=p*f2
    h=[A,B,C]
    g=conv(h,h)
    crit=(3*B*B >= 2*A*C)
    assert g == [A*A,2*A*B,B*B+2*A*C,2*B*C,C*C]
    d1=g[1]*g[1]-g[0]*g[2]
    d2=g[2]*g[2]-g[1]*g[3]
    d3=g[3]*g[3]-g[2]*g[4]
    assert d1 == A*A*(3*B*B-2*A*C)
    assert d2 == B**4+4*A*A*C*C
    assert d3 == C*C*(3*B*B-2*A*C)
    assert lc(g)==crit
    # Xia--Lv condition for n=2 is equivalent after multiplying by A*p>0.
    # 3*(p/A)*f1^2 >= 2*f2  <=> 3*p^2*f1^2 >= 2*A*p*f2.
    assert crit == (3*p*f1*f1 >= 2*A*f2)

cases=0
for den in range(3,16):
    for a in range(0,den):
        for b in range(1,den-a+1):
            c=den-a-b
            if c<0: continue
            f0,f1,f2=F(a,den),F(b,den),F(c,den)
            if f0+f1+f2 != 1: continue
            for pd in range(2,13):
                for pn in range(1,pd):
                    check_three_point(F(pn,pd),f0,f1,f2)
                    cases+=1

# Reproduce the published support-{0,1,2,3} counterexample.
p=F(20,23); q=1-p
f=[F(1,20),F(1,5),F(3,10),F(9,20)]
h=[q+p*f[0]]+[p*x for x in f[1:]]
g=conv(h,h)
delta=p/(p*f[0]+q)
assert 3*delta*f[1]*f[1] == 2*f[2]
assert not lc(g)
assert g[4]*g[4] < g[3]*g[5]

print(f"VERIFY_OK three_point_cases={cases} support4_counterexample=exact")
