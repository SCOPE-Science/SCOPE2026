"""Exact rational checks supplement the analytic period-three eye theorem."""
from fractions import Fraction as F

def param_interval(b):
    L=(1+b)*(4*b*b-10*b+9)/(2*(7+2*b-4*b*b))
    U=(4+3*b-2*b*b-4*b**3)/(2*(7-2*b-4*b*b))
    return L,U

def cycle(a,b):
    cp=2+2*b;cm=2-2*b;p=cp*cm*cm
    q=cm*(cm*(a-b/2)+(a+3*b/2-1))+(a+3*b/2-2)
    x0=q/(1-p)
    x1=cp*x0+a-b/2
    x2=cm*x1+a+3*b/2-1
    return [x0,x1,x2],p

def step(x,a,b):
    y=((2+2*b)*x+a-b/2) if x<F(1,2) else ((2-2*b)*x+a+3*b/2)
    return y % 1

n=0
special_a=F(10,19); special_b=F(3,4);special_x=[F(9,76),F(43,76),F(71,76)]
assert cycle(special_a,special_b)==(special_x,F(7,8))
for i,x in enumerate(special_x):
    assert step(x,special_a,special_b)==special_x[(i+1)%3];n+=1
for b in [F(3,4),F(4,5),F(5,6),F(7,8),F(8,9),F(17,20)]:
    L,U=param_interval(b)
    p=8*(1+b)*(1-b)**2
    assert 0<p<1 and L<U
    width=(5-2*b-4*b*b)*(1-p)/(2*(7+2*b-4*b*b)*(7-2*b-4*b*b))
    assert U-L==width;n+=1
    for j in range(1,10):
        a=L+(U-L)*F(j,10)
        xs,m=cycle(a,b)
        assert 0<xs[0]<F(1,2)<xs[1]<1 and F(1,2)<xs[2]<1
        assert m==p
        assert all(step(xs[i],a,b)==xs[(i+1)%3] for i in range(3));n+=4
# Probe both strict boundary equalities without interpreting boundary orbits as regular.
for b in [F(3,4),F(4,5),F(7,8)]:
    L,U=param_interval(b)
    xs,_=cycle(L,b);assert xs[1]==F(1,2);n+=1
    xs,_=cycle(U,b);assert xs[2]==1;n+=1
print(f"PASS: {n} exact rational assertions; primitive 3-cycle witness and strip samples")
