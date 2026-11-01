"""Reproduce exact rational arithmetic for the five-coordinate projection witness.

This finite calculation checks the displayed certificate. The universal
lower bound remains the algebraic inequality proved in RESULT.md.
"""
from fractions import Fraction as F

Q = lambda a,b=1: F(a,b)
u = (Q(1), Q(4,5), Q(1,4), Q(-1,4), Q(-4,5))
v = (Q(0), Q(3,5), Q(1), Q(1), Q(3,5))
f = (Q(520,659), Q(105,1318), Q(110,659), Q(-110,659), Q(-105,1318))
g = (Q(0), Q(70,659), Q(575,1318), Q(575,1318), Q(70,659))
T = Q(845,659)
checks = 0

def check(condition, detail):
    global checks
    assert condition, detail
    checks += 1

def inner(a, b):
    return sum((x*y for x,y in zip(a,b)), Q(0))

check(inner(f,u)==1, 'f(u)')
check(inner(f,v)==0, 'f(v)')
check(inner(g,u)==0, 'g(u)')
check(inner(g,v)==1, 'g(v)')

P = [[u[i]*f[j]+v[i]*g[j] for j in range(5)] for i in range(5)]
for i,row in enumerate(P):
    check(sum(map(abs,row),Q(0)) == T, f'row {i+1} norm')
for basis in (u,v):
    for i in range(5):
        check(sum((P[i][j]*basis[j] for j in range(5)),Q(0))==basis[i], 'range/reproduction')
for i in range(5):
    for j in range(5):
        check(sum((P[i][k]*P[k][j] for k in range(5)),Q(0))==P[i][j], 'idempotence')

# Symmetry R(x1,x2,x3,x4,x5) = (-x1,x5,x4,x3,x2).
R = [[Q(0) for j in range(5)] for i in range(5)]
for i,j,sgn in ((0,0,-1),(1,4,1),(2,3,1),(3,2,1),(4,1,1)):
    R[i][j]=Q(sgn)
for z,sign in ((u,-1),(v,1)):
    for i in range(5):
        check(sum((R[i][j]*z[j] for j in range(5)),Q(0))==sign*z[i], 'reflection eigenvectors')

# The universal lower-bound certificate is a convex combination of the
# three independent row-class estimates in the proof.
theta = Q(286,315)
wA,wB,wC = Q(104,659),Q(315,659),Q(240,659)
check(wA+wB+wC==1,'weights')
check(0 < theta < 1,'theta')
for name,coefficient,target in (
    ('a',wA+Q(4,5)*wB+Q(1,4)*wC,Q(416,659)),
    ('b',Q(2)*wA+Q(8,5)*theta*wB,Q(416,659)*Q(8,5)),
    ('c',Q(2)*wA,Q(416,659)*Q(1,2)),
    ('d',Q(6,5)*(1-theta)*wB+Q(2)*wC,Q(429,659)*Q(6,5)),
    ('e',Q(6,5)*wB+Q(2)*wC,Q(429,659)*Q(2)),
):
    check(coefficient==target,'dual coefficient '+name)
check(Q(416,659)+Q(429,659)==T,'dual objective')

# Test a variety of rational symmetrized projections against the analytical
# lower bound; this checks finite samples only, not universal optimality.
for denominator in (2,3,5,7,11):
    for ai in range(-2*denominator,2*denominator+1):
        a=Q(ai,denominator)
        b=Q(0)
        c=2*(1-a)
        d=Q(0)
        e=Q(1,2)
        A=abs(a)+2*abs(b)+2*abs(c)
        B=(4*abs(a)+2*max(4*abs(b),3*abs(d))+2*max(4*abs(c),3*abs(e)))/5
        C=abs(a)/4+2*max(abs(b)/4,abs(d))+2*max(abs(c)/4,abs(e))
        check(max(A,B,C)>=T,'finite sample lower bound')

# Block extensions to n-dimensional W_n in R^(2n), n>=3.
for n in range(3,13):
    N=2*n
    B=[[Q(0) for j in range(N)] for i in range(N)]
    for i in range(5):
        B[i][:5]=P[i][:]
    B[5][5]=Q(1)
    for j in range(n-3):
        i=6+2*j
        B[i][i]=B[i][i+1]=B[i+1][i]=B[i+1][i+1]=Q(1,2)
    for i in range(N):
        check(sum(map(abs,B[i]),Q(0)) <= T,'block row bound')
    # Verify idempotence using sparse block structure.
    for i in range(N):
        for j in range(N):
            check(sum((B[i][k]*B[k][j] for k in range(N)),Q(0)) == B[i][j],'block idempotence')
    check(max(sum(map(abs,B[i]),Q(0)) for i in range(N)) == T,'block exact norm')

print('EXACT_RATIONAL_CHECKS_PASSED', checks)
print('SHARP_NORM',str(T),'FLOAT',float(T))
