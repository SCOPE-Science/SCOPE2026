from fractions import Fraction
from decimal import Decimal, getcontext
a,b,c=5,4,3
assert (a-b)*(a+b)**2 == 81 > 45 == a*c*c
wc2=Fraction(a*b*((a+b)**2-c*c),(a+b)**2)
delta=Fraction(b*b,1)-wc2
assert wc2==Fraction(160,9) and delta==Fraction(-16,9)
getcontext().prec=70
def D(x): return Decimal(str(x))
def dist(x1,y1,x2,y2): return ((x1-x2)**2+(y1-y2)**2).sqrt()
def bisq(u,v,d): return u*v*((u+v)**2-d*d)/(u+v)**2
def defect(e):
    e=D(e); x=e; y=D(4)-D(2)*e
    R1=dist(x,y,D(0),D(0)); R2=dist(x,y,D(3),D(0)); R3=dist(x,y,D(0),D(4))
    w1=bisq(R2,R3,D(5)).sqrt(); w2=bisq(R3,R1,D(4)).sqrt(); w3=bisq(R1,R2,D(3)).sqrt()
    return R1*R1+D(2)*R2*R3-(w1*w1+w2*w2+w3*w3+D(3)*(w2*w3+w3*w1+w1*w2))
for e in ('0.1','0.01','0.001','0.0001'): assert defect(e)<0
print('VERIFY_OK')
print('boundary_defect=',delta)
