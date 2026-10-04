from fractions import Fraction as F

def domega(I,w,c,k):
    return 2*w*I/(k+I)-c

def derivatives(Sp,Sn,I,bp,bn,w,c,k):
    d=domega(I,w,c,k)
    dSp=-bp*I*Sp+d*Sp*Sn
    dSn=-bn*I*Sn-d*Sp*Sn
    return dSp,dSn

def p_dot_quotient(Sp,Sn,I,bp,bn,w,c,k):
    S=Sp+Sn
    dSp,dSn=derivatives(Sp,Sn,I,bp,bn,w,c,k)
    dS=dSp+dSn
    return (dSp*S-Sp*dS)/(S*S)

def p_dot_closed(Sp,Sn,I,bp,bn,w,c,k):
    S=Sp+Sn
    p=Sp/S
    return p*(1-p)*((bn-bp)*I+S*domega(I,w,c,k))

cases=[
    (F(1,20),F(1,20),F(1,250),F(3,40),F(3,20),F(1,10),F(1,100),F(1,10)),
    (F(2,7),F(3,11),F(1,23),F(1,9),F(2,7),F(3,10),F(1,50),F(2,9)),
    (F(5,19),F(7,31),F(3,101),F(2,15),F(1,4),F(4,13),F(1,40),F(1,8)),
]
for cse in cases:
    assert p_dot_quotient(*cse)==p_dot_closed(*cse)

# Exact default-parameter witness from the paper.
Sp=F(1,20); Sn=F(1,20); I=F(1,250)
bp=F(3,40); bn=F(3,20); w=F(1,10); c=F(1,100); k=F(1,10)
S=Sp+Sn; p=Sp/S
d=domega(I,w,c,k)
icross=c*k/(2*w-c)
assert icross==F(1,190)
assert I<icross
assert d==F(-3,1300) and d<0
pd=p_dot_closed(Sp,Sn,I,bp,bn,w,c,k)
assert pd==F(9,520000) and pd>0

# Threshold polynomial. Its unique positive root lies between 0 and I_cross
# because all derivative coefficients are positive on I>=0.
delta=bn-bp
A=delta*k+S*(2*w-c)
def poly(x):
    return delta*x*x+A*x-S*c*k
assert poly(F(0))<0
assert poly(icross)>0
assert poly(I)==F(9,1250000)>0
assert delta>0 and A>0

# Integrated log-odds selection term uses R'=gamma I; this sample checks
# only the coefficient identity used in the proof.
gamma=F(1,10)
assert delta/gamma==F(3,4)
print('VERIFY_OK')
