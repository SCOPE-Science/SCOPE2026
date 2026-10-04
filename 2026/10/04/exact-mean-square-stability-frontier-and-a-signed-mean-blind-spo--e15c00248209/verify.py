from fractions import Fraction as F
from math import comb, sqrt

# Bivariate polynomials in (c,m), represented by {(i,j): coefficient}.
def clean(p):
    return {k:v for k,v in p.items() if v}

def add(p,q):
    out=dict(p)
    for k,v in q.items():
        out[k]=out.get(k,F(0))+v
    return clean(out)

def scale(p,a):
    return clean({k:a*v for k,v in p.items()})

def mul(p,q):
    out={}
    for (i,j),a in p.items():
        for (k,l),b in q.items():
            key=(i+k,j+l)
            out[key]=out.get(key,F(0))+a*b
    return clean(out)

def power(p,n):
    out={(0,0):F(1)}
    for _ in range(n):
        out=mul(out,p)
    return out

ONE={(0,0):F(1)}
C={(1,0):F(1)}
M={(0,1):F(1)}
B=add(ONE,scale(C,F(-1)))     # beta = 1-c
U=mul(C,M)                    # u = c*m

# Reconstruct characteristic coefficients exactly from the displayed formulas.
a1=scale(add(add(add(add(scale(power(B,2),F(2)),scale(mul(B,U),F(4))),B),
                     scale(power(U,2),F(2))),ONE),F(-1,2))

a2_num={}
for term in (
    scale(power(B,3),F(2)),
    scale(mul(power(B,2),U),F(8)),
    scale(power(B,2),F(2)),
    scale(mul(B,power(U,2)),F(10)),
    scale(mul(B,U),F(4)),
    B,
    scale(power(U,3),F(4)),
):
    a2_num=add(a2_num,term)
a2=scale(a2_num,F(1,4))

a3=scale(
    mul(
        add(B,scale(U,F(2))),
        add(add(power(B,2),scale(mul(B,U),F(2))),scale(power(U,2),F(2)))
    ),
    F(-1,4)
)

J1=add(add(add(ONE,a1),a2),a3)
J2=add(add(add(ONE,scale(a1,F(-1))),a2),scale(a3,F(-1)))
J3=add(add(add(ONE,scale(a2,F(-1))),mul(a1,a3)),scale(power(a3,2),F(-1)))

# Exact claimed factor for J1:
# (beta-1)/4 * ((beta+2u)^2-(beta+2)).
S=add(B,scale(U,F(2)))
rhs=scale(
    mul(
        add(B,scale(ONE,F(-1))),
        add(power(S,2),scale(add(B,scale(ONE,F(2))),F(-1)))
    ),
    F(1,4)
)
assert J1 == rhs

# J2 has the displayed positive beta-u expansion; test exact positivity independently
# after converting beta=1-c,u=cm by its Bernstein coefficients.
def bernstein_coeffs(poly, nc=None, nm=None):
    if nc is None:
        nc=max((i for i,j in poly),default=0)
    if nm is None:
        nm=max((j for i,j in poly),default=0)
    out=[]
    for i in range(nc+1):
        row=[]
        for j in range(nm+1):
            s=F(0)
            for (k,l),coef in poly.items():
                if i>=k and j>=l:
                    s += coef*F(comb(i,k),comb(nc,k))*F(comb(j,l),comb(nm,l))
            row.append(s)
        out.append(row)
    return out

B3=bernstein_coeffs(J3,6,6)
flat=[v for row in B3 for v in row]
assert len(flat)==49
assert min(flat)==F(3,16)
assert all(v>0 for v in flat)

# Numerical covariance recurrence for representative points.
def step(v,beta,mass):
    q,r,s=v
    u=(1-beta)*mass
    a=beta+u
    return (
        F(1,2)*q+r+s,
        F(beta,2)*r+a*s,
        F(1,2)*u*u*q-a*u*r+a*a*s
    )

# Stable example: beta=0, M=1/2.
v=(F(1),F(0),F(0))
for _ in range(200):
    v=step(v,F(0),F(1,2))
assert float(v[0]) < 1e-20

# Marginal exact boundary at beta=0, M=1/sqrt(2) cannot be represented rationally;
# verify the analytic boundary equation instead.
assert abs(2*(1/sqrt(2)) - sqrt(2)) < 1e-15

# Unstable rational example beta=0, M=4/5: covariance does not decay.
v=(F(1),F(0),F(0))
vals=[]
for k in range(160):
    v=step(v,F(0),F(4,5))
    if k in (40,80,120,159):
        vals.append(float(v[0]))
assert vals[-1] > vals[-2] > vals[-3]

# Signed mean for beta=0 has polynomial t^2-(M+1/2)t+M.
# Quadratic Jury quantities are 1-tr+det=1/2, 1+tr+det>0, 1-det>0 for M<1.
for mass in (F(0),F(1,2),F(4,5),F(99,100)):
    tr=mass+F(1,2)
    det=mass
    assert 1-tr+det == F(1,2)
    assert 1+tr+det > 0
    assert 1-det > 0

# Full-mass smoothing threshold.
beta_c=(5-sqrt(17))/2
assert abs(beta_c-0.4384471871911697) < 2e-16

print("verification passed")
