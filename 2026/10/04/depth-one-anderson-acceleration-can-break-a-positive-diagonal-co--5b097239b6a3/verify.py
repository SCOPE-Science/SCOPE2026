from fractions import Fraction as F

def dot(a,b):
    return sum((x*y for x,y in zip(a,b)), F(0))

def add(a,b):
    return [x+y for x,y in zip(a,b)]

def sub(a,b):
    return [x-y for x,y in zip(a,b)]

def scale(c,a):
    return [c*x for x in a]

def g(e,x):
    return [(1-e)*x[0]+1, F(4,5)*x[1]+2*e]

def aa(e, last=6):
    x0=[F(0),F(0)]
    xs=[x0,g(e,x0)]
    denoms=[]
    coeffs=[]
    for k in range(1,last):
        fprev=sub(g(e,xs[k-1]),xs[k-1])
        fcur=sub(g(e,xs[k]),xs[k])
        d=sub(fcur,fprev)
        den=dot(d,d)
        assert den>0
        s=-dot(fprev,d)/den
        denoms.append(den)
        coeffs.append(s)
        gp=g(e,xs[k-1])
        gc=g(e,xs[k])
        xs.append(add(gp,scale(s,sub(gc,gp))))
    return xs, coeffs, denoms

# Exact rational witness.
e=F(1,200)
xs,coeffs,denoms=aa(e,6)
assert all(v>0 for x in xs[1:6] for v in x)
expected_second=F(-4801559852330482770906299820259,
                  349417867959904066964567555052100)
assert xs[6][1]==expected_second
assert xs[6][0]>0
assert xs[6][1]<F(-1,100)

# First accelerated coefficient formula.
assert coeffs[0] == (F(25)+20*e)/(29*e)

# Picard fixed point and positivity for the witness.
xstar=[F(1,e),10*e]
assert g(e,xstar)==xstar
xp=[F(0),F(0)]
for _ in range(20):
    xn=g(e,xp)
    assert xn[0]>xp[0] and xn[1]>xp[1]
    assert xn[0]>0 and xn[1]>0
    xp=xn

# Limiting scaled recurrence.
def f0(S):
    return [1-S[0], -S[1]/5]

def g0(S):
    return [S[0], F(4,5)*S[1]]

S1=[F(0),F(0)]
S2=[F(25,29),F(40,29)]
expected=[
    S1,
    S2,
    [F(625,689),F(800,689)],
    [F(105125,98149),F(28800,98149)],
    [F(14982925,14044109),F(3548160,14044109)],
    [F(2235098625,2165688769),F(-143897600,2165688769)],
]
Ss=[S1,S2]
limit_den=[]
for k in range(2,6):
    A=Ss[k-2]
    B=Ss[k-1]
    fa=f0(A)
    fb=f0(B)
    d=sub(fb,fa)
    den=dot(d,d)
    assert den>0
    limit_den.append(den)
    s=-dot(fa,d)/den
    ga=g0(A)
    gb=g0(B)
    Ss.append(add(ga,scale(s,sub(gb,ga))))
assert Ss==expected
assert all(S[0]>0 for S in Ss[1:])
assert all(S[1]>0 for S in Ss[1:5])
assert Ss[5][1]<0

# One-dimensional minimality.
for a,c in [(F(0),F(3)),(F(1,5),F(7,3)),(F(1,2),F(2)),(F(9,10),F(1,7))]:
    f0s=c
    f1s=a*c
    d=f1s-f0s
    assert d!=0
    s=-f0s*d/(d*d)
    assert s==F(1,1-a)
    x2=(1-s)*c+s*((1+a)*c)
    assert x2==c/(1-a)>0

print('VERIFY_OK')
