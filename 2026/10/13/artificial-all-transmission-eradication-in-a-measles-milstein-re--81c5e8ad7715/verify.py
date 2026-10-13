"""Exact checks for the source model's numerical extinction discrepancy.

Only Python standard library required: python verify.py
"""
from fractions import Fraction as F

L=F(5); beta=F(20); mu=F(1); psi=F(1); wv=F(1)
phi=F(1); gamma=F(1); phi1=F(1); kappa=F(1); w=F(1)
a=mu+phi; d=mu+gamma+phi1; A=mu+kappa+wv; B=mu+w
state=(F(15,11),F(15,11),F(5,11),F(5,11),F(5,22),F(15,22))
S,E,I,V1,V2,R=state
N=sum(state); J=beta*S*I/N
assert N==F(50,11) and J==F(30,11)
original=(L+wv*V1-J-(psi+mu)*S,
          J-a*E,
          phi*E-d*I,
          psi*S-A*V1,
          kappa*V1-B*V2,
          gamma*I+w*V2-mu*R)
assert original==(F(0),)*6, original
printed=original[:2]+(original[2]-J,)+original[3:]
assert printed[2]==-F(30,11)
q=mu*A/(mu*A+psi*(mu+kappa))
assert q==F(3,5)
DFE=(F(3),F(0),F(0),F(1),F(1,2),F(1,2))
assert sum(DFE)==L/mu
Sd,Ed,Id,V1d,V2d,Rd=DFE
assert L+wv*V1d-(psi+mu)*Sd==0
assert psi*Sd-A*V1d==0
assert kappa*V1d-B*V2d==0
assert w*V2d-mu*Rd==0
trace_true=-(a+d); det_true=a*d-phi*beta*q
trace_print=-(a+d+beta*q); det_print=a*(d+beta*q)-phi*beta*q
assert (trace_true,det_true)==(F(-5),F(-6))
assert (trace_print,det_print)==(F(-17),F(18))
assert F(1)**2-trace_true*F(1)+det_true==0
assert F(-6)**2-trace_true*F(-6)+det_true==0
assert (beta*q*phi)/(a*d)==F(2)
assert (beta*q*phi)/(a*(d+beta*q))==F(2,5)
h=F(1,40)
M=max(beta+psi+mu,a,d+beta,A,B,mu)
assert h<=1/M
assert F(1)-mu*h==F(39,40)
# One-step exact algebra at an interior, non-equilibrium state.
S,E,I,V1,V2,R=(F(4),F(2,5),F(1,6),F(1,2),F(1,3),F(1,4))
N=S+E+I+V1+V2+R
inc=beta*S*I/N
En=E+h*(inc-a*E)
In=I+h*(phi*E-d*I-inc)
assert En+In==E+I-h*(mu*E+d*I)
assert En>=0 and In>=0 and En+In<=(F(1)-mu*h)*(E+I)
# Independently evaluate all printed Euler coordinates and positivity.
vec=(S+h*(L+wv*V1-inc-(psi+mu)*S),En,In,
     V1+h*(psi*S-A*V1),V2+h*(kappa*V1-B*V2),
     R+h*(gamma*I+w*V2-mu*R))
assert min(vec)>=0 and sum(vec)>0
# The original drift and printed drift disagree by a nonvanishing amount.
assert (In-I)/h-(phi*E-d*I)==-inc and inc>0
print('VERIFY_OK')
