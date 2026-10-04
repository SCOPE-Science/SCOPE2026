from fractions import Fraction as Q
from math import sqrt, exp, isclose

def coeff(r,K,beta,gamma,a,b,c,k,alpha,d):
    q=(alpha-d)/a
    C0=r + K*k*beta*q*q*b*b
    C1=2*b*c*K*k*beta*q*q + b*K*beta*q + r*gamma-r*K
    C2=K*k*beta*q*q*c*c + c*K*beta*q-r*K*gamma
    return q,C0,C1,C2

def classify(C0,C1,C2):
    assert C0>0
    D=C1*C1-4*C0*C2
    if C2<0: return 1
    if C2==0: return 1 if C1<0 else 0
    if C1<0:
        if D>0: return 2
        if D==0: return 1
    return 0

def F(u,r,K,beta,gamma,b,c,k,q):
    return r*(1-u/K)*(u+gamma)-beta*q*(b*u+c)*(1+k*q*(b*u+c))

def P(u,C0,C1,C2):
    return C0*u*u+C1*u+C2

r,K,beta,gamma,a,b,c,k,alpha,d = Q(7,5),Q(11,3),Q(2,7),Q(5,4),Q(9,8),Q(3,10),Q(7,3),Q(1,20),Q(13,8),Q(1,2)
q,C0,C1,C2=coeff(r,K,beta,gamma,a,b,c,k,alpha,d)
for u in [Q(0),Q(1,7),Q(2,3),Q(5,2),Q(11,3)]:
    assert P(u,C0,C1,C2) == -K*F(u,r,K,beta,gamma,b,c,k,q)

r,K,beta,gamma,a,b,c,k,alpha,d=Q(1),Q(10),Q(1,5),Q(1),Q(1),Q(1,10),Q(5),Q(1,100),Q(3,2),Q(1,2)
q,C0,C1,C2=coeff(r,K,beta,gamma,a,b,c,k,alpha,d)
assert (q,C0,C1,C2)==(Q(1),Q(5001,5000),Q(-439,50),Q(1,2))
D=C1*C1-4*C0*C2
assert D==Q(9386,125) and classify(C0,C1,C2)==2
loglam=r/(1+k*q*c)-beta*q*c/gamma
assert loglam==Q(-1,21)
assert C2 == -K*gamma*(1+k*q*c)*loglam
rts=[(-float(C1)-sqrt(float(D)))/(2*float(C0)),(-float(C1)+sqrt(float(D)))/(2*float(C0))]
assert 0<rts[0]<rts[1]<float(K)
for u in rts:
    v=float(q)*(float(b)*u+float(c))
    e1=float(r)/(1+float(k)*v)*(1-u/float(K))-float(beta)*v/(u+float(gamma))
    e2=float(alpha)-float(a)*v/(float(b)*u+float(c))-float(d)
    assert abs(e1)<1e-12 and abs(e2)<1e-12
    assert isclose(u*exp(e1),u,rel_tol=0,abs_tol=1e-11)
    assert isclose(v*exp(e2),v,rel_tol=0,abs_tol=1e-11)

r=K=gamma=a=b=c=Q(1); beta=Q(2); k=Q(1,10); alpha=Q(3,2); d=Q(1,2)
q,C0,C1,C2=coeff(r,K,beta,gamma,a,b,c,k,alpha,d)
assert (C0,C1,C2)==(Q(6,5),Q(12,5),Q(6,5))
assert C1*C1-4*C0*C2==0 and classify(C0,C1,C2)==0
for u in [Q(0),Q(1),Q(7,3)]: assert P(u,C0,C1,C2)==Q(6,5)*(u+1)*(u+1)

assert classify(Q(1),Q(0),Q(-1))==1
assert classify(Q(1),Q(-2),Q(0))==1
assert classify(Q(1),Q(2),Q(0))==0
assert classify(Q(1),Q(-3),Q(2))==2
assert classify(Q(1),Q(-2),Q(1))==1
assert classify(Q(1),Q(-1),Q(1))==0
assert classify(Q(1),Q(3),Q(2))==0
print('VERIFY_OK')
