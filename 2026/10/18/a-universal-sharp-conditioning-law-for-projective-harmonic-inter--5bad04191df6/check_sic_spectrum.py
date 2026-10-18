#!/usr/bin/env python3
"""Reproduce exact Jacobi/Legendre calculations and numerical SIC geometry.
This verifies finite rational arithmetic; all-degree steps use the analytic
Legendre integral bound established in the accompanying proof.
"""
from fractions import Fraction as F
import cmath, json, math
from pathlib import Path

X = F(-1, 2)

def legendre_at_x(count, x=X):
    p = [F(1), x]
    for n in range(1, count):
        p.append(((2*n+1)*x*p[n]-n*p[n-1])/(n+1))
    return p

p = legendre_at_x(40)
a = [(p[q]-p[q+1])*F(2, 3*(q+1)) for q in range(40)]
assert a[0] == 1
assert a[1] == a[2] == -F(1,8)
assert a[3] == F(31,256)
assert max(a[q] for q in range(3,20)) == F(31,256)
assert min(a[q] for q in range(3,20)) == -F(47,1024)
assert [q for q in range(3,20) if a[q]==F(31,256)]==[3]
assert F(4,63) < F(31,473) < F(31,256)

conditions=[]
for q in range(3,20):
    alpha,beta = F(1)-a[q], F(1)+8*a[q]
    assert alpha>0 and beta>0
    cond=max(alpha,beta)/min(alpha,beta)
    assert cond <= F(56,25)
    if cond == F(56,25): assert q==3
    conditions.append((q,str(a[q]),str(cond)))

# Confirm SIC geometry for distinct members of the continuous qutrit family.
w=cmath.exp(2j*math.pi/3)
def rotate(v):return (v[2],v[0],v[1])
def make_sic(angle):
    seed=(0j,1/math.sqrt(2),-cmath.exp(2j*angle)/math.sqrt(2))
    points=[]
    for t in range(3):
        z=tuple(seed[j]*w**(t*j) for j in range(3))
        for s in range(3):
            points.append(z)
            z=rotate(z)
    return points
for angle in [0.,math.pi/20,math.pi/6]:
    current=make_sic(angle)
    assert len(current)==9
    for i in range(9):
        for j in range(9):
            overlap=abs(sum(current[i][k].conjugate()*current[j][k] for k in range(3)))**2
            assert abs(overlap - (1 if i==j else .25)) < 1e-12
vs=make_sic(math.pi/20)

# Independent real-valued recurrence at each observed projective angle.
def legendre_numeric(n,x):
    if n==0:return 1.
    b,c=1.,x
    for k in range(1,n): b,c=c,((2*k+1)*x*c-k*b)/(k+1)
    return c
for q in range(0,12):
    h=(q+1)**3
    for i in range(9):
        for j in range(9):
            t=2*abs(sum(vs[i][k].conjugate()*vs[j][k] for k in range(3)))**2-1
            if abs(t-1)<1e-10: val=h
            else:
                val=h*(legendre_numeric(q,t)-legendre_numeric(q+1,t))/((1-t)*(q+1))
            expected=h*(1 if i==j else float(a[q]))
            assert abs(val-expected)<2e-6

certificate={
 'exact_a_q_q0_to_19': {str(q):str(a[q]) for q in range(20)},
 'Gram_condition_number_q3_to_19':{str(q):str(max(F(1)-a[q],F(1)+8*a[q])/min(F(1)-a[q],F(1)+8*a[q])) for q in range(3,20)},
 'analytic_tail': {'q_min':20,'bound':'abs(a_q) <= 4/(3(q+1)) <= 4/63 < 31/473',
                   'argument':'Legendre integral implies abs(P_n(x))<=1 for -1<=x<=1.'},
 'sharp_claim':'max for q>=3 of spectral condition number of Gram = 56/25, unique at q=3',
 'q0_rank':1,'q1_q2_rank':8,'all_q_at_least_3_rank':9,
 'sample_normalization':'sphere probability measure; dim H_(q,q)(C^3)=(q+1)^3',
 'numerical_independent_geometry':'Three distinct nine-point WH SIC configurations checked at pairwise squared overlap 1/4; a non-Hesse member used for Jacobi kernel comparison',
}
Path(__file__).with_name('spectrum_certificate.json').write_text(json.dumps(certificate,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf8')
print('PASS: Jacobi values 0-19, sharp global Gram conditioning and nine-point SIC geometry')
print('Unique sharp q: 3; Gram conditioning:',F(56,25))
print('Exact-degree rows:',len(conditions),' kernel entries:',9*9*12,' SIC inner-product checks:',3*9*9)
