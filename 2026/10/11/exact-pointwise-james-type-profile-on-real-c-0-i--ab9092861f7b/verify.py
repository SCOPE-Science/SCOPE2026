import math
from fractions import Fraction
from itertools import product

def norm_inf(v):
    return max(abs(float(z)) for z in v)

def mean_t(a,b,t):
    a=float(a); b=float(b)
    if t == '-inf':
        return min(a,b)
    if t == 0:
        return math.sqrt(a*b)
    t=float(t)
    if t < 0 and (a == 0.0 or b == 0.0):
        return 0.0
    return ((a**t+b**t)/2.0)**(1.0/t)

def s2(x):
    vals=sorted((abs(float(z)) for z in x), reverse=True)
    return vals[1]

vals=[Fraction(-1),Fraction(-1,2),Fraction(0),Fraction(1,2),Fraction(1)]
xs=[]
for v in product(vals, repeat=4):
    if max(abs(z) for z in v)==1:
        xs.append(v)
ys=xs
params=['-inf',-4,-1,0,Fraction(1,2),1,2,5]
checks=0
for x in xs:
    s=s2(x)
    target={str(t):mean_t(2,1+s,t) for t in params}
    for y in ys[::17]:
        a=norm_inf(tuple(x[i]+y[i] for i in range(4)))
        b=norm_inf(tuple(x[i]-y[i] for i in range(4)))
        for t in params:
            assert mean_t(a,b,t) <= target[str(t)] + 2e-12
            checks += 1

witness_checks=0
for x in xs:
    absvals=[abs(z) for z in x]
    k=absvals.index(Fraction(1))
    others=[(absvals[j],j) for j in range(4) if j!=k]
    s,l=max(others)
    y=[Fraction(0) for _ in range(4)]
    y[k]=Fraction(1) if x[k]>0 else Fraction(-1)
    if s>0:
        y[l]=Fraction(-1) if x[l]>0 else Fraction(1)
    else:
        y[l]=Fraction(1)
    a=max(abs(x[i]+y[i]) for i in range(4))
    b=max(abs(x[i]-y[i]) for i in range(4))
    assert sorted([a,b])==sorted([Fraction(2),Fraction(1)+s])
    for t in params:
        assert abs(mean_t(a,b,t)-mean_t(2,1+s,t)) < 2e-12
        witness_checks += 1

print(f'VERIFY_OK grid_x={len(xs)} upper_checks={checks} witness_checks={witness_checks} params={len(params)}')
