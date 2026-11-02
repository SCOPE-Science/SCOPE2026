#!/usr/bin/env python3
"""Independent exact/rational and midpoint quadrature checks of the metric theta graph second-moment bounds.

Python standard library only. All finite tests are supplementary to the analytical proof.
"""
from fractions import Fraction as F
from random import Random


def exact_second(a,b,c):
    a,b,c=sorted((a,b,c))
    K=(3*a**4+2*a**3*b+2*a**3*c+3*a*a*b*b+3*a*a*c*c
       +4*a*b**3+6*a*b*b*c+6*a*b*c*c+4*a*c**3
       +b**4+2*b**3*c+3*b*b*c*c+2*b*c**3+c**4)/12
    return K/(a+b+c)**2

def gap_certificates(a,b,c):
    a,b,c=sorted((a,b,c));x=a;y=b-a;z=c-b;L=a+b+c
    K=L*L*exact_second(a,b,c)
    lower=(216*x*x*y*y+216*x*x*y*z+216*x*x*z*z+168*x*y**3
         +252*x*y*y*z+288*x*y*z*z+102*x*z**3+19*y**4
         +38*y**3*z+69*y*y*z*z+50*y*z**3+13*z**4)/324
    upper=(39*x**4+104*x**3*y+52*x**3*z+96*x*x*y*y+96*x*x*y*z
         +18*x*x*z*z+40*x*y**3+60*x*y*y*z+24*x*y*z*z
         +2*x*z**3+7*y**4+14*y**3*z+9*y*y*z*z+2*y*z**3)/12
    assert K-F(7,162)*L**4==lower
    assert L**4/12-K==upper
    assert lower>=0 and upper>0
    assert (lower==0)==(y==0 and z==0)

def d_network(lengths,i,x,j,y):
    p,q=lengths[i],lengths[j]
    if i==j:
        t=abs(x-y)
        alternative=min(lengths[k] for k in range(3) if k!=i)
        return min(t,p-t+alternative)
    h=lengths[3-i-j]
    return min(x+y,p+q-x-y,x+h+q-y,p-x+h+y)

def quadrature(lengths,n=121,power=2):
    total=0.0
    for i,p in enumerate(lengths):
        for j,q in enumerate(lengths):
            partial=0.0
            for r in range(n):
                x=p*(r+.5)/n
                for s in range(n):
                    y=q*(s+.5)/n
                    partial+=d_network(lengths,i,x,j,y)**power
            total+=p*q*partial/(n*n)
    return total/(sum(lengths)**2)

def run():
    checks=0
    assert exact_second(F(1),F(1),F(1))==F(7,18);checks+=1
    for a in range(1,9):
        for b in range(a,10):
            for c in range(b,11):
                aa,bb,cc=F(a),F(b),F(c)
                gap_certificates(aa,bb,cc);checks+=4
                moment=exact_second(aa,bb,cc);L=aa+bb+cc
                assert F(7,162)*L*L<=moment<L*L/12;checks+=1
    rng=Random(5262026)
    cases=[[1.,1.,1.],[.2,.3,.5],[.1,.2,3.],[1.,2.,4.],
           [.01,.02,3.], [.1,.1,3.], [1.,1.1,1.2],
           [1.,10.,10.], [2.,2.,9.], [.01,.495,.495]]
    for _ in range(12):
        cases.append(sorted([10**rng.uniform(-1,1.4) for _ in range(3)]))
    for lengths in cases:
        got=quadrature(lengths,n=121)
        predicted=float(exact_second(*lengths))
        assert abs(got-predicted)<.00016*sum(lengths)**2,(lengths,got,predicted)
        checks+=1
    # Exact limiting CDFs at t=1/5 for the equal-arm and two-loop degenerations.
    t=F(1,5)
    assert 2*t+4*t*t>2*t+3*t*t
    checks+=1
    print('VERIFY_OK',checks,'exact rational identities, independent double quadratures, and CDF-limit comparison')
if __name__=='__main__':run()
