from fractions import Fraction
from math import sqrt


def gauge(r,s,p,q):
    d=1+r*s
    return (abs(Fraction(p)+s*Fraction(q))+abs(Fraction(q)-r*Fraction(p)))/d


def shortest(r,s,B=12):
    vals=[]
    best=None
    for p in range(-B,B+1):
        for q in range(-B,B+1):
            if p==0 and q==0:
                continue
            g=gauge(r,s,p,q)
            if best is None or g<best:
                best=g; vals=[(p,q)]
            elif g==best:
                vals.append((p,q))
    return best,set(vals)

for den in range(2,10):
    for ir in range(0,den):
        for js in range(0,den):
            r=Fraction(ir,den); s=Fraction(js,den)
            b,dirs=shortest(r,s)
            ge1=(1+r)/(1+r*s)
            ge2=(1+s)/(1+r*s)
            if r<s:
                assert b==ge1
                assert dirs=={(1,0),(-1,0)}
            elif s<r:
                assert b==ge2
                assert dirs=={(0,1),(0,-1)}
            else:
                assert b==ge1==ge2
                assert dirs=={(1,0),(-1,0),(0,1),(0,-1)}

# Exact canonical invariants and polar involution on rational samples.
for den in range(2,16):
    for num in range(1,den):
        x=Fraction(num,den)
        lam=(1+x)/(1+x*x)
        diam=2/lam
        assert diam==2*(1+x*x)/(1+x)
        area=2*(1+x*x)
        assert area>2 and area<4
        psi=(1-x)/(1+x)
        assert (1-psi)/(1+psi)==x
        Dpsi=2*(1+psi*psi)/(1+psi)
        assert Dpsi==diam

        # Polar vertices are A^{-1}(±1,±1), A=[[1,x],[x,-1]].
        c=(1+x)/(1+x*x)
        y=(x-1)/(x+1)
        polar={( (sx+x*sy)/(1+x*x), (x*sx-sy)/(1+x*x) )
               for sx in (Fraction(-1),Fraction(1))
               for sy in (Fraction(-1),Fraction(1))}
        qy={(c*Fraction(1),c*y),(-c*Fraction(1),-c*y),
            (c*y,-c*Fraction(1)),(-c*y,c*Fraction(1))}
        assert polar==qy

# The diameter profile has its unique continuous minimum at sqrt(2)-1.
x0=sqrt(2)-1
D0=2*(1+x0*x0)/(1+x0)
assert abs(D0-4*(sqrt(2)-1))<1e-14
for z in [0.001,0.05,0.2,0.4,0.7,0.95,0.999]:
    Dz=2*(1+z*z)/(1+z)
    assert Dz>=D0-1e-14

print('VERIFY_OK symmetric lattice quadrilateral classification profile')
