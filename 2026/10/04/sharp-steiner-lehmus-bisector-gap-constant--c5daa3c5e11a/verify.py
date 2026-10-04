import math, random

def bisector_ratio(p,d):
    A=math.pi-2*p; B=p-d; C=p+d
    a=math.sin(A); b=math.sin(B); c=math.sin(C)
    y=2*a*c*math.cos(B/2)/(a+c)
    z=2*a*b*math.cos(C/2)/(a+b)
    return (y-z)/(c-b)

def reduced(p,d):
    g=math.cos(p); u=math.cos(d)
    return 2*(1-g)*math.sqrt((1+g)/(1+u))*(u+g+2*g*g)/(u-4*g**3+3*g)

def cubic(x): return x**3+4*x*x+x-10
lo,hi=0.0,2.0
for _ in range(120):
    m=(lo+hi)/2
    if cubic(m)<0: lo=m
    else: hi=m
q=(lo+hi)/2
f=lambda x: math.sqrt(x+2)*(x*x+x+2)/(2*(x+1)**2)
k=f(q)
assert abs(q-1.28427753730695)<2e-14
assert abs(k-0.856762017555545)<2e-14
rng=random.Random(20261001)
max_formula=0.0; min_margin=1e9
for _ in range(30000):
    p=rng.uniform(0.01,math.pi/2-0.01)
    d=rng.uniform(1e-7,p-1e-7)
    r1=bisector_ratio(p,d); r2=reduced(p,d)
    max_formula=max(max_formula,abs(r1-r2))
    min_margin=min(min_margin,r1-k)
    if r1 <= k-2e-10: raise AssertionError((p,d,r1,k))
p=math.acos(q/2)
vals=[reduced(p,10**(-j)) for j in range(2,8)]
assert abs(vals[-1]-k)<2e-10
print('VERIFY_OK')
print('q',format(q,'.15f'))
print('kappa',format(k,'.15f'))
print('max_formula_error',format(max_formula,'.3e'))
print('min_sample_margin',format(min_margin,'.3e'))
print('sharpness_last_error',format(abs(vals[-1]-k),'.3e'))
