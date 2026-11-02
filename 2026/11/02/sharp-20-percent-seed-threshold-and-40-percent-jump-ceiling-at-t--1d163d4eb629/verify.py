"""Exact rational checks for a sharp early-peak switch in the discrete SIR map."""
from fractions import Fraction as F
from random import Random

def step(s,i,z,b,g):
    n=b*s*i
    return s-n, i+n-g*i, z+g*i

def datum(u,r):
    a=1/(1+r)
    s=r/(1+r)
    beta=u/a
    gamma=u*(1-u)*r
    s1,i1,z1=step(s,a,F(0),beta,gamma)
    s2,i2,z2=step(s1,i1,z1,beta,gamma)
    return a,s,beta,gamma,(s1,i1,z1),(s2,i2,z2)

def check_switch(u,r):
    assert F(1,2)<u<1 and 0<r<(1-u)/u**3
    a,s,b,g,v1,v2=datum(u,r)
    assert 0<g<1 and a>F(1,5)
    assert b*v1[1]<1 and v1[1]>a and v1[1]==v2[1]
    assert v2[0]>0 and v2[0]<v1[0]
    jump=v1[0]-v2[0]
    assert jump==g*v1[1]
    assert jump==u*(1-u)*r*(1+u*u*r)/(1+r)
    assert jump<F(2,5)
    return jump

# Transparent explicit rational witness.
a,s,b,g,v1,v2=datum(F(8,15),F(3,2))
assert (a,s,b,g)==(F(2,5),F(3,5),F(4,3),F(28,75))
assert v1==(F(7,25),F(214,375),F(56,375))
assert check_switch(F(8,15),F(3,2))==F(5992,28125)
assert v2[0]==F(7,25)-F(5992,28125)
# Rational one-sided parameter choices; all iterates remain positive and peak at day 2 / day 1.
def check_side(beta,expected):
    ss,ii,zz=s,a,F(0)
    trajectory=[]
    for t in range(6):
        trajectory.append((ss,ii,zz))
        assert ss>0 and ii>0 and zz>=0 and ss+ii+zz==1
        assert beta*ii<1
        ss,ii,zz=step(ss,ii,zz,beta,g)
    peak=max(range(len(trajectory)),key=lambda t: trajectory[t][1])
    assert peak==expected, (peak,expected)
    return trajectory[peak]
for h in [F(1,100000),F(1,10000),F(1,1000)]:
    l=check_side(b-h,2)
    rr=check_side(b+h,1)
    assert 1-l[0] > 1-rr[0]

# Increasing gamma? gamma chosen at beta switch, physical example confirmed.
# Rational family approaching supremum 2/5; parameters r positive and strict.
last=F(0)
for k in (30,100,1000,10000):
    u=F(1,2)+F(1,k)
    r=(1-u)/u**3-F(1,k*k)
    j=check_switch(u,r)
    assert abs(j-F(2,5))<F(50,k)
    last=j
assert last>F(399,1000)

# Independent systematic small rational grid (exact inequalities) and threshold exclusion.
checked=0
for den in range(3,31):
    for num in range(den//2+1,den):
        u=F(num,den)
        rmax=(1-u)/u**3
        for k in (F(1,4),F(1,2),F(3,4),F(999,1000)):
            r=k*rmax
            j=check_switch(u,r)
            assert j < F(2,5)
            checked+=1
# Critical speed? Not relevant. Algebraic sharp upper envelope tested exactly.
print('PASS: example initial I=2/5, beta=4/3, gamma=28/75; peak jump = 5992/28125')
print('PASS: peak switches across +/- 1/1000, +/- 1/10000, +/- 1/100000')
print('PASS: exact rational grid:',checked,'comparisons; sharp limit family',last)
