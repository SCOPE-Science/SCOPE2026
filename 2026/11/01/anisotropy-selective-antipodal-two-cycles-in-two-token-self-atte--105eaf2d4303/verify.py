"""Exact and numerical checks for an antipodal two-token attention cycle.

Run with standard Python 3: python verify.py
Scientific checks are diagnostic and do not replace the analytic all-parameter proof.
"""
from fractions import Fraction as Q
from math import exp, log, sqrt

# The example has tanh(alpha) = 1/2, alpha = log(3)/2.
t = Q(1, 2)
p = (1 + t)/2
eta = Q(1, 2)
strengths = (Q(8),Q(2),Q(1))
R = eta*strengths[0]*t-Q(1)
assert (t,p,R)==(Q(1,2),Q(3,4),Q(1))
results=[]
for s in strengths[1:]:
    diagonal=(Q(1)-eta*s*p)/R
    offdiagonal=-eta*s*(Q(1)-p)/R
    common=diagonal+offdiagonal
    difference=diagonal-offdiagonal
    assert common==(Q(1)-eta*s)/R
    assert difference==(Q(1)-eta*s*t)/R
    results.extend((common*common,difference*difference))
assert sorted(results)==sorted((Q(0),Q(1,4),Q(1,4),Q(9,16)))
assert Q(2)/(t*(strengths[0]+strengths[-1]))==Q(4,9)
assert strengths[1]/strengths[0]<t

# Directly evaluate the full unmasked two-token spherical update.
alpha=log(3)/2
Vdiag=(-8.0,-2.0,-1.0)
step=0.5
unit=(1.0,0.0,0.0)
minus=(-1.0,0.0,0.0)

def normalized(v):
    n=sqrt(sum(q*q for q in v))
    assert n>1e-10
    return tuple(q/n for q in v)

def advance(pair):
    def dot(x,y): return sum(a*b for a,b in zip(x,y))
    out=[]
    for i in range(2):
        z=[alpha*dot(pair[i],pair[j]) for j in range(2)]
        z=[v-max(z) for v in z]
        w=[exp(v) for v in z]
        w=[v/sum(w) for v in w]
        m=[sum(w[j]*pair[j][k] for j in range(2)) for k in range(3)]
        out.append(normalized(tuple(pair[i][k]+step*Vdiag[k]*m[k] for k in range(3))))
    return tuple(out)

pair=(unit,minus)
image=advance(pair)
assert image==(minus,unit)
assert advance(image)==pair

# Central-difference derivatives on the product of spheres.  The tangent
# coordinates correspond to the non-principal spectral directions.
def jac(pair,h=1e-6):
    M=[[0.0]*4 for _ in range(4)]
    for col in range(4):
        state=col//2
        coord=col%2+1
        pp=[list(x) for x in pair]
        pm=[list(x) for x in pair]
        pp[state][coord]+=h
        pm[state][coord]-=h
        pp=tuple(normalized(tuple(x)) for x in pp)
        pm=tuple(normalized(tuple(x)) for x in pm)
        yp=advance(pp)
        ym=advance(pm)
        fp=(yp[0][1],yp[0][2],yp[1][1],yp[1][2])
        fm=(ym[0][1],ym[0][2],ym[1][1],ym[1][2])
        for row in range(4):
            M[row][col]=(fp[row]-fm[row])/(2*h)
    return M

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]

J=jac(pair)
Jnext=jac(image)
for k,s in enumerate(strengths[1:]):
    for i in (k,k+2):
        assert abs(J[i][i]-float((Q(1)-eta*s*p)/R))<1e-8
    assert abs(J[k][k+2]-float(-eta*s*(1-p)/R))<1e-8
    assert abs(J[k+2][k]-float(-eta*s*(1-p)/R))<1e-8
for i in range(4):
    for j in range(4):
        assert abs(J[i][j]-Jnext[i][j])<1e-8
assert max(abs(mm(Jnext,J)[i][j]) for i in range(4) for j in range(4))<1.0

# An independent exact rational grid tests the sharp iff inequalities.
count=0
for t0 in (Q(1,10),Q(1,4),Q(1,2),Q(3,4),Q(19,20)):
    for r1 in (Q(1,100),Q(1,10),Q(1,5),Q(2,5),Q(4,5),Q(19,20)):
        for r2 in (Q(1,100),Q(1,10),Q(3,10),Q(3,5),Q(17,20)):
            for b in (1/t0+Q(1,1000),1/t0+Q(2,5),2/t0,5/t0,20/t0):
                den=b*t0-1
                eigs=[(1-b*r)/den for r in (r1,r2)]+[(1-b*r*t0)/den for r in (r1,r2)]
                observed=all(abs(x)<1 for x in eigs)
                expected=(max(r1,r2)<t0 and b>2/(t0*(1+min(r1,r2))))
                assert observed==expected,(t0,r1,r2,b)
                count+=1
assert count==750
print('PASS: exact antipodal orbit, rational full Floquet spectrum, direct four-dimensional derivatives, 750 exact-parameter iff checks')
