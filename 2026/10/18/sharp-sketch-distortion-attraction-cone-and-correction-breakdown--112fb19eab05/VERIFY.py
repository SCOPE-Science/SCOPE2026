from fractions import Fraction as F
from random import Random
import math

def calc(a,b,c,t,l1=F(2),l2=F(7)):
    u=(F(1),t)
    H=((a,c),(c,b)); det=a*b-c*c; q=a+2*c*t+b*t*t
    theta=(l1*(a+c*t)+l2*t*(c+b*t))/q
    r=((l1-theta),(l2-theta)*t)
    v=(-(c+b*t),a+c*t)
    # H v = det (-t,1) exactly
    hv=(-det*t,det)
    # coefficient in projected H inner product
    denom=hv[0]*(l1-theta)*v[0]+hv[1]*(l2-theta)*v[1]
    numerator=hv[0]*r[0]+hv[1]*r[1]
    if denom==0:return theta,None,None
    alpha=-numerator/denom
    unew=(u[0]+alpha*v[0],u[1]+alpha*v[1])
    assert unew[0]!=0
    predicted=-t*t*(c+b*t)/(a+c*t)
    assert unew[1]/unew[0]==predicted
    assert denom==(l2-l1)*det*(a-b*t*t),('bad denom',denom)
    assert numerator==(l2-l1)*det*t
    return theta, unew[1]/unew[0],alpha

rng=Random(118431)
checks=0
for _ in range(5000):
    a=F(rng.randint(6,30),15)
    b=F(rng.randint(6,30),15)
    c=F(rng.randint(-4,4),15)
    if a*b<=c*c:continue
    t=F(rng.randint(-9,9),15)
    if a-b*t*t==0 or a+c*t==0:continue
    calc(a,b,c,t);checks+=1
assert calc(F(2,5),F(8,5),F(0),F(1,2))[1] is None
for t in (F(-1,4),F(1,4)):
    assert abs(calc(F(2,5),F(8,5),F(0),t)[1])<abs(t)
for t in (F(-3,4),F(3,4)):
    assert abs(calc(F(2,5),F(8,5),F(0),t)[1])>abs(t)
assert calc(F(16,25),F(34,25),F(12,25),F(1,100000))[1] !=0
assert F(12,16)==F(3,4)

# robust norm envelope for random E with E norm < epsilon=3/5; exact bound by squaring q, and t<1/2.
for _ in range(20000):
    p=F(rng.randint(-15,15),50)
    q=F(rng.randint(-15,15),50)
    if p*p+q*q>F(9,25):continue
    a=1+p;b=1-p;c=q
    t=F(rng.randint(-49,49),100)
    if t==0:continue
    th,tn,alpha=calc(a,b,c,t)
    assert tn is not None
    T=abs(t)
    envelope=T*T*(T+F(3,4))/(1-F(3,4)*T)
    assert abs(tn)<=envelope, ('envelope fail',a,b,c,t,tn,envelope)
    assert abs(tn)<T
    checks+=1

# max offdiagonal coefficient equality
assert F(12,25)/F(16,25)==F(3,4)
# finite high-precision projective iterates for diagonal extremal metric
for t in [F(1,4),F(49,100),F(3,4),F(1,1)]:
    x=t
    for _ in range(3):
        x=-F(4)*x*x*x
    if abs(t)<F(1,2):assert abs(x)<abs(t)
    else:assert abs(x)>abs(t)
print('ALL',checks,'EXACT CHECKS PASS')
