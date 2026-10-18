"""Finite diagnostic checks for an exact affine-ReLU variation norm identity."""
import math
from itertools import product
from scipy.optimize import minimize_scalar

def formula(s,b):
    b=abs(b)
    return 2*math.hypot(s,b) if b<=s/math.sqrt(3) else b+math.sqrt(3)*s

def raw_cost(s,b,c):
    return abs(c)+2*math.hypot(s,b-c)

n=0
for s,b in product([0.,.01,.05,.2,.5,1,2,5,20],[0.,.02,.1,.4,.7,1,1.3,3,10,-.3,-5]):
    ans=formula(s,b)
    c=math.copysign(max(abs(b)-s/math.sqrt(3),0),b)
    assert abs(raw_cost(s,b,c)-ans)<1e-10*(1+ans)
    numeric=minimize_scalar(lambda x:raw_cost(s,b,x),bounds=(-max(abs(b),s,1)*4,max(abs(b),s,1)*4),method='bounded',options={'xatol':1e-11})
    assert numeric.fun >= ans-1e-8*(1+ans),(s,b,ans,numeric.fun)
    assert abs(numeric.fun-ans)<1e-6*(1+ans),(s,b,ans,numeric.fun)
    if s>0:
        t=-(b-c)/s
        q=math.hypot(1,t)
        for x in (-15,-4,-1,-.1,0,.1,.8,3,22):
            val=c+s*q*(max((x-t)/q,0)-max((t-x)/q,0))
            assert abs(val-(s*x+b))<1e-11*(1+abs(s*x+b))
            n+=1
print(f'PASS: {n} finite representation points, {9*11} scalar variational tests')
