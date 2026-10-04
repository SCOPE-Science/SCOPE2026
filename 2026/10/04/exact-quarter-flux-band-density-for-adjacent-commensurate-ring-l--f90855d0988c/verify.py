from fractions import Fraction
import math


def exact_probability_by_roots(m):
    r=2*m+1
    pts={Fraction(0),Fraction(2)}
    for n in (m,m+1):
        for j in range(1,2*n):
            pts.add(Fraction(j,n))
    for j in range(2*r):
        pts.add(Fraction(2*j+1,2*r))
    pts=sorted(pts)
    good=Fraction(0)
    for a,b in zip(pts,pts[1:]):
        mid=(a+b)/2
        x=float(mid)*math.pi
        f=-math.cos(r*x)*math.sin(m*x)*math.sin((m+1)*x)
        if f>1e-12:
            good += b-a
        elif f < -1e-12:
            pass
        else:
            raise AssertionError((m,a,b,mid,f))
    return good/Fraction(2)


def formula(m):
    r=2*m+1
    s=m if m%2 else m+1
    return Fraction(3,4)-Fraction(1,4*r*s)


def mismatch_formula(m):
    r=2*m+1
    z=[]
    for i in range(1,m+1):
        z.append(Fraction(i,m+1))
        if i<m:
            z.append(Fraction(i,m))
    assert len(z)==2*m-1 and all(z[i]<z[i+1] for i in range(len(z)-1))
    c=[Fraction(2*j+1,2*r) for j in range(2*m+1)]
    M=c[0]+(Fraction(1)-c[-1])
    for j,zz in enumerate(z, start=1):
        assert c[j-1] < zz < c[j+1]
        M += abs(zz-c[j])
    return Fraction(1)-M

for m in range(1,201):
    a=exact_probability_by_roots(m)
    b=mismatch_formula(m)
    c=formula(m)
    assert a==b==c,(m,a,b,c)

# Independent dense midpoint check against the transformed band condition for representative m.
for m in (1,2,3,4,7,12,25):
    r=2*m+1
    N=200000
    good=0
    for j in range(N):
        x=2*math.pi*(j+0.5)/N
        f=-math.cos(r*x)*math.sin(m*x)*math.sin((m+1)*x)
        good += (f>=0)
    est=good/N
    target=float(formula(m))
    assert abs(est-target) < 2e-4,(m,est,target)

# Check the exact symmetric-chain value from source formula (37) at quarter flux.
A=0.25
symmetric=1-math.acos(math.cos(2*math.pi*A))/math.pi
assert abs(symmetric-0.5)<1e-15

print('VERIFY_OK')
