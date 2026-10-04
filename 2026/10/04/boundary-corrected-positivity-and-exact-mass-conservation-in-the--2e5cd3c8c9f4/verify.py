from fractions import Fraction as F

def step(S,E,I,R,D,beta,eps,gamma,mu,h):
    N=S+E+I+R
    assert N>0
    Sn=S/(1+h*beta*I/N)
    En=(E+h*beta*Sn*I/N)/(1+h*eps)
    In=(I+h*eps*En)/(1+h*(gamma+mu))
    Rn=R+h*gamma*In
    Dn=D+h*mu*In
    return Sn,En,In,Rn,Dn

cases=[
    (F(9),F(2),F(1),F(3),F(4),F(3,5),F(1,4),F(1,7),F(1,11),F(5,3)),
    (F(1),F(0),F(1),F(0),F(0),F(4),F(3),F(2),F(1),F(10)),
    (F(7),F(5),F(0),F(2),F(3),F(2),F(1,2),F(1,3),F(1,5),F(9,2)),
]
for c in cases:
    old=c[:5]
    new=step(*c)
    assert all(x>=0 for x in new)
    assert sum(new,F(0))==sum(old,F(0))
    assert new[4]>=old[4]

# Exact boundary counterexample to strict positivity.
N=F(13)
old=(N,F(0),F(0),F(0),F(0))
new=step(*old,F(5,2),F(4,3),F(2,7),F(3,8),F(11,4))
assert new==old
assert not all(x>0 for x in new)
print('VERIFY_OK')
