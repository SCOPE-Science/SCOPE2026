from fractions import Fraction as Q

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def scale(c,a): return (c*a[0],c*a[1])
def dot(a,b): return a[0]*b[0]+a[1]*b[1]
def norm2(a): return dot(a,a)

u=(Q(0),Q(-1))

def step(x,eta):
    h=add(x,scale(eta,u))
    s=norm2(h)
    assert s>1
    g=(s-1)/2
    lam=(dot(h,u)+g)/s
    assert 0<lam<1
    w=add(u,scale(-lam,h))
    assert g+dot(h,w)==0
    xp=add(x,scale(eta,w))
    assert xp==scale(1-eta*lam,h)
    return h,xp

for eta in [Q(1,10),Q(1,4),Q(1,2),Q(3,4)]:
    x=(Q(1),Q(0))
    rho=1-eta*eta*(4-eta)*(2-eta)/(4*(1+eta)*(1+eta))
    prev=None
    for _ in range(7):
        h,xp=step(x,eta)
        assert norm2(h)>1
        assert norm2(xp)<1
        d=norm2(add(h,scale(-1,u)))
        if prev is not None:
            assert d<=rho*prev
        hn=add(xp,scale(eta,u))
        s=norm2(h)
        lhs=norm2(hn)-1
        rhs=(eta*eta*d*(2*(s+1)-d)+4*(1-eta)*s*(s-1))/(4*s)
        assert lhs==rhs and lhs>0
        prev=d
        x=xp
print("VERIFY_OK")
