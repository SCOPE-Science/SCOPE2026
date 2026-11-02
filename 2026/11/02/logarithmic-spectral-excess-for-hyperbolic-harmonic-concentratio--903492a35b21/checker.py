"""Exact rational checks for four-ball radial concentration formulas.

Run with: python3 checker.py
Dependencies: Python 3 standard library only.
These finite checks are diagnostic; the proof is analytical.
"""
from fractions import Fraction
from math import gamma, log

checks = 0

def assert_close(a, b, rel):
    global checks
    checks += 1
    assert abs(a-b) <= rel * max(1,abs(b)), (a,b,rel)

def poly_mul(a,b):
    out=[Fraction(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j] += x*y
    return out

def moment(m,s,T,harmonic):
    assert type(m)==int and m>=0 and type(s)==int and s>=0
    assert 0<=T<=1
    base=[Fraction(1)]
    for _ in range(s): base=poly_mul(base,[Fraction(1),Fraction(-1)])
    if harmonic:
        h=[1+Fraction(m,2), -Fraction(m,2)]
        base=poly_mul(base,poly_mul(h,h))
    return sum(a*T**(m+2+j)/Fraction(m+2+j) for j,a in enumerate(base))

def beta_int(m,s,T):
    # Exact incomplete beta for integer shape parameters: integral of
    # t^(m+1)*(1-t)^s on [0,T].
    return moment(m,s,T,False)

def hyperbolic_beta_decomposition(m,s,T):
    return (beta_int(m,s,T) + m*beta_int(m,s+1,T)
            + Fraction(m*m,4)*beta_int(m,s+2,T))

def evalue(m,s,T,harmonic=True):
    return moment(m,s,T,harmonic)/moment(m,s,Fraction(1),harmonic)

def logfrac(q):
    return log(q.numerator)-log(q.denominator)

def count_above(s,T,epsilon,harmonic):
    m=0
    total=0
    while True:
        x=evalue(m,s,T,harmonic)
        if x<=epsilon: return total,m
        total+=(m+1)**2
        m+=1
        assert m<5000

for s in range(4):
    for T in (Fraction(1,4),Fraction(1,2),Fraction(3,4)):
        prev=Fraction(1)
        for m in range(90):
            h=evalue(m,s,T)
            e=evalue(m,s,T,False)
            checks+=1;assert 0<h<prev, ('ordering',s,T,m)
            checks+=1;assert 0<e<1
            checks+=1;assert moment(m,s,T,True)==hyperbolic_beta_decomposition(m,s,T)
            checks+=1;assert evalue(m,s,Fraction(1))==1
            prev=h
        # Check the power-two hyperbolic enhancement without assuming
        # a finite experiment establishes its limit.
        for m in (100,250,500):
            h=evalue(m,s,T)
            e=evalue(m,s,T,False)
            ratio=float(h/e) * (s+2)*(s+5)/(m*m*float(1-T)**2)
            checks+=1;assert abs(ratio-1)<0.8, ('enhancement',s,T,m,ratio)

for s in range(4):
    T=Fraction(1,2)
    C=float(T)**2*(1-float(T))**(s+2)/(gamma(s+1)*(s+2)*(s+5))
    for m in (250,500,1000):
        h=evalue(m,s,T)
        logref=log(C)+(s+2)*log(m)+m*log(float(T))
        actual=logfrac(h)
        checks+=1;assert abs(actual-logref)<0.7, ('precise-asymptotic',s,m,actual-logref)

for s in range(3):
    T=Fraction(1,2)
    c=log(2)
    for K in (100,200,400):
        L=K*c
        h,mh=count_above(s,T,Fraction(1,2**K),True)
        e,me=count_above(s,T,Fraction(1,2**K),False)
        lead=L**3/(3*c**3)
        sec=(s+2)*L**2*log(L)/c**3
        difference=2*L**2*log(L)/c**3
        # Check only remainder scale, not an invented finite exact identity.
        checks+=1;assert abs(h-lead-sec) < 25*L**2
        checks+=1;assert abs((h-e)-difference) < 30*L**2
        checks+=1;assert mh>=me
print('PASS:',checks,'exact rational and finite asymptotic checks')
