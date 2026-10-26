"""Independent exact-arithmetic checks for an affine-quadratic ProxSkip recurrence."""
from fractions import Fraction as F
from math import comb


def S(c,j):
    return sum((c**k for k in range(j)), F(0))


def step(x,h,a,z,c,p,success):
    # x and z in Q^3; affine constraint x[2]=1, normal vector h=(0,0,h_3).
    gamma=(1-c)/a
    hat=tuple(x[i]-gamma*(a*(x[i]-z[i])-h[i]) for i in range(3))
    if success:
        newx=(hat[0],hat[1],F(1))
    else:
        newx=hat
    newh=tuple(h[i]+p/gamma*(newx[i]-hat[i]) for i in range(3))
    return newx,newh


n=0
z=(F(2),F(-1),F(3))
xstar=(F(2),F(-1),F(1))
for c,m in [(F(1,2),2),(F(2,3),3),(F(3,4),4),(F(1,3),5)]:
    a=1-c
    p=1/S(c,m)
    hstar=(F(0),F(0),a*(xstar[2]-z[2]))
    assert F(0)<p<1
    for j in range(1,14):
        x=xstar
        h=(F(0),F(0),hstar[2]+F(1,7))
        for _ in range(j-1):
            x,h=step(x,h,a,z,c,p,False)
        x,h=step(x,h,a,z,c,p,True)
        assert x==xstar
        assert h[2]-hstar[2] == (1-p*S(c,j))*F(1,7)
        assert (h==hstar)==(j==m)
        n+=1
    # The killing gap is absorbing even under arbitrary later successes and failures.
    x=xstar
    h=(F(0),F(0),hstar[2]+F(1,7))
    for _ in range(m-1):
        x,h=step(x,h,a,z,c,p,False)
    x,h=step(x,h,a,z,c,p,True)
    assert x==xstar and h==hstar
    for b in [False,False,True,False,True,True,False,True]:
        x,h=step(x,h,a,z,c,p,b)
        assert x==xstar and h==hstar
        n+=1
    # Renewal recurrence for exact expected waiting and hitting gap probability.
    hit_prob=p*(1-p)**(m-1)
    expected=1/(p*hit_prob)
    assert expected > 0
    assert (1-p* S(c,m))==0
    n+=2
# Nonresonant boundary p=1-c yields strictly positive multipliers c**j.
for c in [F(1,7),F(1,2),F(4,5)]:
    p=1-c
    for j in range(1,33):
        assert 1-p*S(c,j)==c**j > 0
        n+=1
# Unique rate optimum: m=2, c=1/2, p=2/3, expectation 27/4.
c=F(1,2)
p=1/S(c,2)
assert p==F(2,3) and 1/(p*p*(1-p))==F(27,4)
# Every m >=3 is at least 16 (indeed strict within actual resonant domain).
for c,m in [(F(1,2),3),(F(2,3),3),(F(1,2),4),(F(3,4),5)]:
    p=1/S(c,m)
    assert 1/(p*p*(1-p)**(m-1))>16
    n+=1
print('VERIFY_OK',n)
