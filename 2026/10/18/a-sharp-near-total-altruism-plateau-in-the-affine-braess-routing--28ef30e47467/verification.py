from fractions import Fraction as F

def evaluate(p,q,r,a,b,c,alpha):
    B=b-a-c
    L=(p+q)/2+r
    H=B-(p-q)/2
    K=(p-q)-B
    assert p>q>0 and p-q>B>(p-q)/2 and min(a,b,c,r)>0
    h=H/L
    assert 0<h<1
    z=min(h,1-alpha)
    Hx=z
    Ao=alpha/2
    Ho=(1-alpha-z)/2
    assert Ho>=0 and Ao>=0 and Hx>=0
    x=(1+z)/2; y=(1-z)/2
    LHouter=a+p*x+b+q*y
    LHcenter=2*(a+p*x)+c+r*z
    LAouter=a+2*p*x+b+2*q*y
    LAcenter=2*(a+2*p*x)+c+2*r*z
    assert LHcenter-LHouter==-H+L*z
    assert LAcenter-LAouter==K+2*L*z>0
    if Ho>0:assert LHcenter==LHouter
    if Hx>0:assert LHcenter<=LHouter
    if Ao>0:assert LAouter<LAcenter
    welfare=2*x*(a+p*x)+2*y*(b+q*y)+z*(c+r*z)
    base=a+b+(p+q)/2
    assert welfare==base+K*z+L*z*z
    return h,z,welfare,base

p,q,r,a,b,c=F(4),F(1),F(1),F(1,10),F(21,10),F(1,5)
for j in range(71):
    alpha=F(j,70)
    h,z,w,s0=evaluate(p,q,r,a,b,c,alpha)
    assert h==F(3,35) and s0==F(47,10)
    assert z==min(F(3,35),1-alpha)
    if alpha<=F(32,35):assert w-s0==F(9,70)
assert evaluate(p,q,r,a,b,c,F(1))[2]==F(47,10)
for n in range(2,41):
    p,q,r,a,c=F(2*n),F(1),F(1),F(1),F(1)
    b=F(n)+F(5,2)
    for alpha in (F(0),F(1,2),F(9,10),F(99,100),F(1)):
        h,z,w,s0=evaluate(p,q,r,a,b,c,alpha)
        assert h==F(2,2*n+3)
        if alpha<=1-h:assert w-s0==F(2*n-1,2*n+3)
print('VERIFY_OK: exact route inequalities, welfare, cutoff, and asymptotic rational family')
