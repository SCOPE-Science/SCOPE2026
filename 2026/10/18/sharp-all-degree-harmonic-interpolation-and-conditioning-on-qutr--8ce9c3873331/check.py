#!/usr/bin/env python3
"""Exact rational reproducibility for qutrit MUB harmonic interpolation."""
from fractions import Fraction as F
import json

def legendre_values(x, max_n):
    p=[F(1),x]
    for n in range(1,max_n):
        p.append(((2*n+1)*x*p[n]-n*p[n-1])/(n+1))
    return p

def spectrum(q,ps):
    a=F((-1)**q,q+1)
    b=F(3,4)*(ps[q]-ps[q+1])/(q+1)
    # Within-basis contrasts, base constants with zero sum, global constants.
    lam=(1-a,1+2*a-3*b,1+2*a+9*b)
    return a,b,lam

# Exact Gaussian sums in Q(omega), with omega^2+omega+1=0.
def coeff(k):
    return ((1,0), (0,1), (-1,-1))[k % 3]
def magnitude_squared(z):
    x,y=z
    return x*x-x*y+y*y

def orthogonal_sum(a,b,c,d):
    x=y=0
    for t in range(3):
        u,v=coeff((c-a)*t*t+(d-b)*t)
        x+=u;y+=v
    return x,y

# Four bases, three orthonormal directions per basis, 12 lines total.
assert len([(a,b) for a in range(3) for b in range(3)])+3==12
geom_checks=0
for a in range(3):
    for b in range(3):
        for c in range(3):
            for d in range(3):
                norm=magnitude_squared(orthogonal_sum(a,b,c,d))
                want=9 if a==c and b==d else (0 if a==c else 3)
                assert norm==want,(a,b,c,d,norm,want)
                geom_checks+=1
# Standard basis is orthonormal; its overlaps with any chirp vector have squared modulus 1/3.
for t in range(3):
    for a in range(3):
        for b in range(3):
            assert magnitude_squared(coeff(a*t*t+b*t))==1
            geom_checks+=1

# Exact 12x12 orthogonal idempotents for four disjoint bases.
N=12
I=[[F(i==j) for j in range(N)] for i in range(N)]
T=[[F(i//3==j//3) for j in range(N)] for i in range(N)]
J=[[F(1) for j in range(N)] for i in range(N)]
Pw=[[I[i][j]-T[i][j]/3 for j in range(N)] for i in range(N)]
Pb=[[T[i][j]/3-J[i][j]/12 for j in range(N)] for i in range(N)]
Pc=[[J[i][j]/12 for j in range(N)] for i in range(N)]

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
def check_equals(A,B):
    assert all(A[i][j]==B[i][j] for i in range(N) for j in range(N))

for P in (Pw,Pb,Pc): check_equals(mm(P,P),P)
for A,B in ((Pw,Pb),(Pw,Pc),(Pb,Pc)):
    check_equals(mm(A,B),[[F(0)]*N for _ in range(N)])
check_equals([[Pw[i][j]+Pb[i][j]+Pc[i][j] for j in range(N)] for i in range(N)], I)
assert [sum(P[i][i] for i in range(N)) for P in (Pw,Pb,Pc)]==[8,3,1]

ps=legendre_values(F(-1,3),18)
results=[]
assert spectrum(0,ps)[2]==(F(0),F(0),F(12))
assert spectrum(1,ps)[2]==(F(3,2),F(0),F(0))
assert spectrum(2,ps)[2]==(F(2,3),F(20,9),F(0))
assert spectrum(5,ps)[2]==(F(7,6),F(70,81),F(2,27))
finite_max=(F(0),None)
min_overall=(F(100),None)
max_overall=(F(-1),None)
for q in range(3,17):
    a,b,e=spectrum(q,ps)
    assert min(e)>0,(q,e)
    assert 8*e[0]+3*e[1]+e[2]==12,(q,e)
    Kmat=[[I[i][j]+a*(T[i][j]-I[i][j])+b*(J[i][j]-T[i][j]) for j in range(N)] for i in range(N)]
    Emat=[[e[0]*Pw[i][j]+e[1]*Pb[i][j]+e[2]*Pc[i][j] for j in range(N)] for i in range(N)]
    check_equals(Kmat,Emat)
    if min(e)<min_overall[0]:min_overall=min(e),q
    if max(e)>max_overall[0]:max_overall=max(e),q
    assert min(e)>=F(2,27)
    assert max(e)<=F(28,15)
    K=max(e)/min(e)
    assert K <= F(63,4),(q,K)
    if K>finite_max[0]:finite_max=K,q
    results.append(dict(q=q,a=str(a),b=str(b),eigenvalues=[str(x) for x in e],condition_number=str(K)))
assert finite_max==(F(63,4),5),finite_max
assert min_overall==(F(2,27),5),min_overall
assert max_overall==(F(28,15),4),max_overall
# For q >=17: |P_n(-1/3)| <= 1 by Laplace's integral,
# |b_q| <= (3/2)/(q+1), |a_q| = 1/(q+1).
# Every eigenvalue lies in [1-31/(2(q+1)),1+31/(2(q+1))].
# At q=17 the worst resulting condition number is 67/5 < 63/4.
assert F(31,2*18)<1
assert (1+F(31,36))/(1-F(31,36)) == F(67,5)
assert F(67,5)<F(63,4)
assert 1-F(31,36)>F(2,27)
assert 1+F(31,36)<F(28,15)
report={
    'geometry_checks':geom_checks,
    'projector_spectrum_checks':14*12*12+7*12*12,
    'exact_low_degree_checks':3,
    'finite_degree_count':len(results),
    'low_degree_ranks': {'q0':1,'q1':8,'q2':11},
    'unrestricted_full_rank_from_degree':3,
    'worst_condition_number':'63/4',
    'global_lower_frame_constant':'2/27',
    'lower_equality_degree':5,
    'global_upper_frame_constant':'28/15',
    'upper_equality_degree':4,
    'unique_degree':5,
    'analytic_tail_begin':17,
    'uniform_upper_bound_on_tail':'67/5',
    'finite_table':results,
}
print(json.dumps(report,indent=2))
