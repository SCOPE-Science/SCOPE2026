"""Exact finite checks for the rank-one two-component sampling comparison.
All tests use rational arithmetic; analytical quantifiers are established in RESULT.md.
Run with: python3 verify.py
"""
from fractions import Fraction as F
from itertools import product

def dot(x,y):return sum(a*b for a,b in zip(x,y))
def matmul(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def matvec(a,x):return tuple(dot(row,x) for row in a)
def sqnorm(x):return dot(x,x)
def scale(s,a):return tuple(tuple(s*t for t in row) for row in a)
def proj(u):return tuple(tuple(u[i]*u[j] for j in range(2)) for i in range(2))
def avg_risk(a,b,x,protocol):
    if protocol == 'RR': sequences=((a,b),(b,a))
    else: sequences=((a,a),(a,b),(b,a),(b,b))
    return sum(sqnorm(matvec(matmul(second,first),x)) for first,second in sequences)/len(sequences)

checks=0
for c,s in ((F(3,5),F(4,5)),(F(5,13),F(12,13)),(F(8,17),F(15,17))):
    u=(F(1),F(0)); v=(c,s)
    for a,b in product((F(1,8),F(1,4),F(1,2),F(3,4),F(7,8)),repeat=2):
        A=scale(a,proj(u)); B=scale(b,proj(v))
        for x in ((F(1),F(0)),(F(0),F(1)),(F(1),F(1)),(-s,c),(F(2,3),F(5,7))):
            ux=dot(u,x);vx=dot(v,x)
            rr=avg_risk(A,B,x,'RR'); wr=avg_risk(A,B,x,'iid')
            expect_rr=a*a*b*b*c*c*(ux*ux+vx*vx)/2
            expect_gap=((a**4-a*a*b*b*c*c)*ux*ux+(b**4-a*a*b*b*c*c)*vx*vx)/4
            assert rr==expect_rr and wr-rr==expect_gap
            assert wr*2>=rr
            checks+=3
        # Pointwise Loewner criterion and reversal probes
        boundary=(c<=min(a/b,b/a))
        gap_u=((a**4-a*a*b*b*c*c)*s*s)/4 # x=(-s,c) perpendicular v
        gap_v=((b**4-a*a*b*b*c*c)*s*s)/4 # x=(0,1) perpendicular u
        assert (gap_u>=0 and gap_v>=0)==boundary
        checks+=1
# Exact witness
c,s=F(3,5),F(4,5);a,b=F(1,4),F(3,4)
u=(F(1),F(0));v=(c,s);x=(-s,c)
A=scale(a,proj(u));B=scale(b,proj(v))
rr=avg_risk(A,B,x,'RR');wr=avg_risk(A,B,x,'iid')
assert rr==F(81,20000) and wr==F(53,20000)
assert rr/wr==F(81,53)
checks+=3
print(f'PASS: {checks} rational checks; example RR={rr}, iid={wr}, ratio={rr/wr}')
