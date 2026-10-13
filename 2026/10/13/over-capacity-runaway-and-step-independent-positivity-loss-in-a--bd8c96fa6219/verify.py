#!/usr/bin/env python3
"""Exact-rational spot checks for Gao's ecological map; theorem is proved analytically."""
from fractions import Fraction as Q
from decimal import Decimal, getcontext
from math import ceil, log

def F(u,v,r,b,k1,a,K,c,d,e,f,h):
    return (u*(1+h*(r-b-r*k1*u-a*v)),
            v*(1+h*c*(K-v)/(K+d*v)*(e*u-f)))

r,b,k1,a,K,c,d,e,f,h=Q(3,2),Q(1,2),Q(1,2),Q(1,2),Q(3),Q(1),Q(1),Q(1),Q(1),Q(1,4)
u0,v0=Q(1,2),Q(4)
A=r-b
assert all(q>0 for q in (r,b,k1,a,K,c,d,e,f,h))
assert 0<a<1 and 0<b<1 and 0<h*a<1 and 0<h*b<1
assert 0<u0<f/e and v0>max(K,A/a)
u1,v1=F(u0,v0,r,b,k1,a,K,c,d,e,f,h)
assert u1 == Q(21,64) and v1==Q(57,14)
eta=f-e*u0
q=1+h*c*eta*(v0-K)/(K+d*v0)
assert q==Q(57,56)
T=max(v0,(A+1/h)/a)
assert T==Q(10)
bound=1+ceil(log(float(T/v0))/log(float(q)))
assert bound < 150
# Illustrative numerical replay; not an infinite proof.
getcontext().prec=65
u,v=(Decimal(u0.numerator)/Decimal(u0.denominator),Decimal(v0.numerator)/Decimal(v0.denominator))
D=lambda z: Decimal(z.numerator)/Decimal(z.denominator)
rd,bd,k1d,ad,Kd,cd,dd,ed,fd,hd=map(D,(r,b,k1,a,K,c,d,e,f,h))
exit_index=None
for i in range(bound+1):
    assert u>0 and v>Kd and u<fd/ed
    un=u*(1+hd*(rd-bd-rd*k1d*u-ad*v))
    vn=v*(1+hd*cd*(Kd-v)/(Kd+dd*v)*(ed*u-fd))
    if un<=0:
        exit_index=i+1
        assert vn>v
        break
    assert un<u and vn>v
    u,v=un,vn
assert exit_index is not None and exit_index<=bound
# Exact derivative identity: g'(v)=K(1+d)/(K+dv)^2>0,
# and exact logarithmic-rate deficit identity, by cross multiplication.
v=Q(5)
g=(v-K)/(K+d*v)
assert Q(1,d)-g == K*(1+d)/(d*(K+d*v))
assert (Q(1,d)-(v+Q(1,999999)-K)/(K+d*(v+Q(1,999999)))) < (Q(1,d)-g)
print('VERIFY_OK')
print('r,b,k1,a,K,c,d,e,f,h =', tuple(str(x) for x in (r,b,k1,a,K,c,d,e,f,h)))
print('initial (u,v) =',str(u0),str(v0),'first =',str(u1),str(v1))
print('geometric q =',q,'rigorous max exit iterate <=',bound,'observed exit iterate =',exit_index)
