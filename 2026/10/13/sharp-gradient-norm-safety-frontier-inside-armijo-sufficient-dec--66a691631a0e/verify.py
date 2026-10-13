from fractions import Fraction as F

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

def matvec(A,x):
    return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]

# Exact rational witness: sigma=1/4, kappa=4, first trial alpha=1.
sigma=F(1,4)
kappa=F(4)
A=[[F(15,16),F(0)],[F(0),F(15,4)]]
x=[F(32,15),F(4,15)]
g=matvec(A,x)
assert g == [F(2),F(1)]
alpha=F(1)
xp=[x[i]-alpha*g[i] for i in range(2)]
gp=matvec(A,xp)
assert gp == [F(1,8),F(-11,4)]

def f(v):
    Av=matvec(A,v)
    return dot(v,Av)/2

assert f(x)==F(34,15)
assert f(xp)==F(61,60)
assert f(xp)-f(x) == -sigma*dot(g,g)
ratio_sq=dot(gp,gp)/dot(g,g)
assert ratio_sq==F(97,64)
assert ratio_sq>1

# The Rayleigh quotient hits the Armijo endpoint.
q=dot(g,matvec(A,g))/dot(g,g)
assert q==F(3,2)
assert alpha*q==2*(1-sigma)

# Exact formula and safety equivalence on rational parameter pairs.
pairs=[
    (F(1,4),F(2)),
    (F(1,4),F(3)),
    (F(1,4),F(4)),
    (F(4,9),F(5)),
    (F(9,25),F(4)),
]
for s,k in pairs:
    Kmax=(k+1)**2/(4*k)
    endpoint=4*s-3 + (1-s)**2*(k+1)**2/k
    threshold=(k-1)**2/(k+1)**2
    assert (endpoint <= 1) == (s >= threshold)
    T=2*(1-s)
    assert endpoint == 1-2*T+Kmax*T*T

# General first-trial construction for rational square kappa.
for s,k,s0 in [(F(1,4),F(4),F(1)),
               (F(1,9),F(9),F(1,2)),
               (F(4,9),F(9),F(3,5))]:
    root_k=F(int(k.numerator**0.5), int(k.denominator**0.5))
    assert root_k*root_k==k
    gamma=(1-s)*(k+1)/(k*s0)
    AA=[[gamma,F(0)],[F(0),gamma*k]]
    gg=[root_k,F(1)]
    qq=dot(gg,matvec(AA,gg))/dot(gg,gg)
    assert s0*qq==2*(1-s)

print("VERIFY_OK")
print("witness_squared_gradient_ratio", ratio_sq)
