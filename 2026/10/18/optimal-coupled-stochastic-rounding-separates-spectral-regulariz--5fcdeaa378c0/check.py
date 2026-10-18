"""Independent exact-arithmetic checks for coupled unbiased two-point rounding.

Usage: python check.py. Requires only the Python standard library.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt
from random import Random


def endpoints(p, q):
    return max(F(0), p + q - 1), min(p, q)


def states(low1, step1, low2, step2, p, q, t):
    return [((low1, low2), 1-p-q+t),
            ((low1, low2+step2), q-t),
            ((low1+step1, low2), p-t),
            ((low1+step1, low2+step2), t)]


def moment(states_):
    A = sum((pr*x*x for (x,y),pr in states_), F(0))
    B = sum((pr*y*y for (x,y),pr in states_), F(0))
    C = sum((pr*x*y for (x,y),pr in states_), F(0))
    return A,B,C


def mineig(m):
    a,b,c=map(float,m)
    return (a+b-sqrt((a-b)**2+4*c*c))/2


checks = 0
for low1,low2 in product((F(1),F(3,2),F(2)),repeat=2):
    for step1,step2 in product((F(1,4),F(1,2)),repeat=2):
        for p,q in product((F(1,4), F(1,3), F(1,2), F(2,3),F(3,4)),repeat=2):
            a,b=endpoints(p,q)
            u=low1+step1*p; v=low2+step2*q
            target=p*q-u*v/(step1*step2)
            tstar=max(a,min(b,target))
            # Fréchet endpoints + independence + optimum + sampled interior couplings
            ts=sorted(set([a,b,p*q,tstar]+[a+(b-a)*F(k,12) for k in range(13)]))
            baseline=moment(states(low1,step1,low2,step2,p,q,p*q))
            optimal=moment(states(low1,step1,low2,step2,p,q,tstar))
            x=mineig(optimal)
            for t in ts:
                z=moment(states(low1,step1,low2,step2,p,q,t))
                assert z[0]==u*u+step1*step1*p*(1-p)
                assert z[1]==v*v+step2*step2*q*(1-q)
                assert z[2]==u*v+step1*step2*(t-p*q)
                assert mineig(z)<=x+1e-10
                # Exact PSD test: 2G(independent)-G(coupled) must be PSD.
                da=2*baseline[0]-z[0]
                db=2*baseline[1]-z[1]
                dc=2*baseline[2]-z[2]
                assert da>=0 and db>=0 and da*db>=dc*dc
                checks+=5

# The midpoint symmetric case has three distinct positive-coordinate rays.
lo,hi=F(1),F(3,2)
h=hi-lo
x=(lo+hi)/2
for t in (F(0), F(1,6), F(1,4), F(1,2)):
    st=states(lo,h,lo,h,F(1,2),F(1,2),t)
    a,b,c=moment(st)
    assert a==x*x+h*h/4 and b==a
    assert c==x*x+h*h*(t-F(1,4))
    # For all t in [0, 1/2] the smaller eigenvalue is the antisymmetric one.
    assert min(a+c,a-c)==h*h*(F(1,2)-t)
    checks+=3
    for n in range(2,7):
        # Exact finite enumeration, including zero-probability state labels.
        probability=F(0)
        for seq in product(range(4),repeat=n):
            prob=F(1)
            rows=[]
            for k in seq:
                v,pr=st[k]; prob*=pr; rows.append(v)
            if not prob: continue
            pivot=rows[0]
            if all(pivot[0]*v[1]==pivot[1]*v[0] for v in rows[1:]):
                probability+=prob
        formula=(2*t)**n+2*(F(1,2)-t)**n
        assert probability==formula,(n,t,probability,formula)
        checks+=1

for n in range(2,17):
    # Strictly convex probability objective has its unique minimum at t=1/6.
    rankbest=F(3)**(1-n)
    assert rankbest < F(2)**(1-n)
    assert rankbest <= F(1,2)**n+2*F(1,4)**n
    checks+=2

# Verify sharp bound attained in the symmetric case.
assert mineig(moment(states(lo,h,lo,h,F(1,2),F(1,2),F(0))))==2*mineig(moment(states(lo,h,lo,h,F(1,2),F(1,2),F(1,4))))
checks+=1

# Empirical population Gram for n rows under the two key couplings.
rng=Random(384901)
for t in (F(0),F(1,6),F(1,4)):
    st=states(lo,h,lo,h,F(1,2),F(1,2),t)
    vals=[(row, float(pr)) for row,pr in st if pr]
    A=B=C=F(0); n=30000
    for _ in range(n):
        z=rng.random(); cum=0.
        for (p1,p2),pr in vals:
            cum+=pr
            if z<cum: break
        A+=p1*p1; B+=p2*p2; C+=p1*p2
    empirical=mineig((A/n,B/n,C/n))
    theory=mineig(moment(st))
    assert abs(empirical-theory)<0.015, (t, empirical, theory)
    checks+=1

print('PASS: %d independently implemented moment, coupling, rank and simulation checks.'%checks)
print('symmetric minimum squared singular value per row: antithetic',h*h/F(2),'rank-optimal',h*h/F(3),'independent',h*h/F(4))
print('rank-deficiency at 4 rows: antithetic',F(1,8),'rank-optimal',F(1,27),'independent',F(1,16)+2*F(1,256))
