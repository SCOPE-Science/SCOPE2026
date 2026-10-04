from fractions import Fraction as F
from math import isqrt

def weights(m):
    D=(2*m+1)*(4*m*m+4*m-3)
    A=3*m*m+3*m-1
    return [F(3*(A-5*j*j),D) for j in range(-m,m+1)]

def defect(m):
    ws=weights(m)
    return -sum((w for w in ws if w<0),F(0))

def closed_defect(m):
    A=3*m*m+3*m-1
    k=isqrt(A//5) if A%5==0 else isqrt(A//5)
    # Correct floor(sqrt(A/5)) exactly.
    while 5*(k+1)*(k+1)<=A: k+=1
    while 5*k*k>A: k-=1
    D=(2*m+1)*(4*m*m+4*m-3)
    num=(m-k)*(10*k*k+10*k*m+15*k-8*m*m-3*m+11)
    return F(num,D),k

for m in range(1,60):
    ws=weights(m)
    js=list(range(-m,m+1))
    assert sum(ws,F(0))==1
    assert sum((w*j for w,j in zip(ws,js)),F(0))==0
    assert sum((w*j*j for w,j in zip(ws,js)),F(0))==0
    v,k=closed_defect(m)
    assert v==defect(m)
    A=3*m*m+3*m-1
    for j,w in zip(js,ws):
        assert (w<0)==(5*j*j>A)

assert weights(2)==[F(-3,35),F(12,35),F(17,35),F(12,35),F(-3,35)]
assert weights(3)==[F(-2,21),F(3,21),F(6,21),F(7,21),F(6,21),F(3,21),F(-2,21)]
assert defect(1)==0
assert defect(2)==F(6,35)
assert defect(3)==F(4,21)
for m in range(4,28):
    assert defect(m)<F(4,21)

# Exact constants and algebra used in the uniform m>=28 bound.
m=28
D=(2*m+1)*(4*m*m+4*m-3)
assert D==184965
assert (m+1)**3==24389
assert F((m+1)**3,D)==F(24389,184965)
assert 3*m*m+3*m-1==2435
assert F(2435,5)==487
assert F(75261,3409)**2-F(487,1)==F(4654274,11621281)
assert F(4654274,11621281)>0

# Check the displayed monotonicity identities for a broad exact range.
for m in range(1,200):
    a2=F(3*m*m+3*m-1,5*(m+1)*(m+1))
    a2n=F(3*(m+1)*(m+1)+3*(m+1)-1,5*(m+2)*(m+2))
    assert a2n-a2==F(3*m*m+11*m+9,5*(m+1)*(m+1)*(m+2)*(m+2))
    Fm=F((m+1)**3,(2*m+1)*(4*m*m+4*m-3))
    mn=m+1
    Fnext=F((mn+1)**3,(2*mn+1)*(4*mn*mn+4*mn-3))
    rhs=-F(3*m*m+13*m+13,(2*m-1)*(2*m+1)*(2*m+3)*(2*m+5))
    assert Fnext-Fm==rhs

# Strictly positive seven-point witness, M=1.
ws=weights(3)
y=[F(1),F(2,25),F(2,25),F(2,25),F(2,25),F(2,25),F(1)]
assert all(v>0 for v in y)
out=sum((w*v for w,v in zip(ws,y)),F(0))
assert out==F(-2,21)

print('VERIFY_OK')
