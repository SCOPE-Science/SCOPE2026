from fractions import Fraction as Q

def mat(a, rho, r):
    D = r + rho - a
    assert D > 0
    return ((r/D, -Q(1)/D), (rho*r/D, (r-a)/D))

def mv(M, v):
    return (M[0][0]*v[0] + M[0][1]*v[1],
            M[1][0]*v[0] + M[1][1]*v[1])

def trdet(M):
    tr = M[0][0] + M[1][1]
    det = M[0][0]*M[1][1] - M[0][1]*M[1][0]
    return tr, det

def check_identities(a, rho, r):
    D = r + rho - a
    M = mat(a, rho, r)
    T, delta = trdet(M)
    assert T == (2*r-a)/D
    assert delta == r/D
    assert 1-delta == (rho-a)/D
    assert 1-T+delta == rho/D
    assert 1+T+delta == (4*r+rho-2*a)/D
    return M

# Exact optimal double root.
for a, rho in [(Q(4),Q(6)), (Q(3),Q(5)), (Q(2),Q(7))]:
    rstar = a*a/(4*rho)
    D = rstar + rho - a
    M = check_identities(a,rho,rstar)
    T,delta = trdet(M)
    assert T*T == 4*delta
    q = a/(2*rho-a)
    assert delta == q*q
    assert T == -2*q

# Strongly convex primal subproblem but unstable coupled dynamics:
# a=4, rho=3, r=2 gives D=1>0 and determinant 2>1.
M = check_identities(Q(4),Q(3),Q(2))
_,delta = trdet(M)
assert delta == 2

# Boundary rho=a: exact small two-cycle along the -1 eigenvector.
a=Q(4); rho=Q(4); r=Q(1)
M=check_identities(a,rho,r)
v=(Q(1,100), Q(1,50))
assert mv(M,v) == (-v[0],-v[1])
assert mv(M,mv(M,v)) == v

# Boundary 4r+rho=2a with rho>a: another exact -1 eigenmode.
a=Q(4); rho=Q(6); r=Q(1,2)
M=check_identities(a,rho,r)
v=(Q(1,100), Q(3,100))
assert mv(M,v) == (-v[0],-v[1])

# Interior stable example at the optimum has repeated eigenvalue -1/2.
a=Q(4); rho=Q(6); r=Q(2,3)
M=check_identities(a,rho,r)
T,delta=trdet(M)
assert T == -1 and delta == Q(1,4)

print("VERIFY_OK")
