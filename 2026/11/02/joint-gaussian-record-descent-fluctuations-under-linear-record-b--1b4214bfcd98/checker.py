#!/usr/bin/env python3
"""Exact checks of record/adjacent-descent identities for record-tilted permutations."""
from itertools import permutations
from fractions import Fraction
from math import log

def formula(n, theta):
    p=[Fraction(i*(2*theta+i-1),2*(theta+i-1)*(theta+i)) for i in range(1,n)]
    j=[Fraction(i*(i+1)*(3*theta+i-1),6*(theta+i-1)*(theta+i)*(theta+i+1)) for i in range(1,n-1)]
    r=[theta/(theta+i-1) for i in range(1,n+1)]
    er=sum(r)
    ed=sum(p)
    vr=sum(z*(1-z) for z in r)
    vd=sum(z*(1-z) for z in p)+2*sum(j[k]-p[k]*p[k+1] for k in range(len(j)))
    crd=-theta*n*(n-1)/(2*(theta+n-1)**2)
    return p,j,er,ed,vr,vd,crd

def exact_enumeration(n,theta):
    z=Fraction(0)
    eR=eD=eRR=eDD=eRD=Fraction(0)
    dp=[Fraction(0) for _ in range(n-1)]
    joint=[Fraction(0) for _ in range(n-2)]
    for perm in permutations(range(1,n+1)):
        mx=0; R=0
        for x in perm:
            if x>mx:mx=x;R+=1
        d=[int(perm[i]>perm[i+1]) for i in range(n-1)]
        D=sum(d)
        w=theta**R
        z+=w;eR+=w*R;eD+=w*D;eRR+=w*R**2;eDD+=w*D**2;eRD+=w*R*D
        for i,v in enumerate(d):dp[i]+=w*v
        for i in range(n-2):joint[i]+=w*d[i]*d[i+1]
    return [x/z for x in dp],[x/z for x in joint],eR/z,eD/z,eRR/z-(eR/z)**2,eDD/z-(eD/z)**2,eRD/z-(eR/z)*(eD/z)

def asymp(lam):
    r=lam*log(1+1/lam)-lam/(lam+1)
    v=(6*lam**2+4*lam+1)/(12*(lam+1)**3)
    c=-lam/(2*(lam+1)**2)
    return r,v,c

def main():
    tests=0;perms=0
    for n in range(2,8):
        for theta in (Fraction(1,2),Fraction(1),Fraction(3,2),Fraction(3)):
            expected=formula(n,theta)
            actual=exact_enumeration(n,theta)
            for label, a,b in zip(('p','joint','ER','ED','VarR','VarD','CovRD'),expected,actual):
                if isinstance(a,list):
                    assert a==b,(n,theta,label,a,b)
                    tests+=len(a)
                else:
                    assert a==b,(n,theta,label,a,b)
                    tests+=1
            assert expected[3]==Fraction(n*(n-1),2*(theta+n-1))
            tests+=1
            from math import factorial
            perms+=factorial(n)
    for lam in (Fraction(1,2),Fraction(1),Fraction(2)):
        lr,lv,lc=asymp(float(lam))
        assert lr*lv-lc*lc>0
        tests+=1
        for n in (300,1000,3000):
            _,_,_,_,vr,vd,c=formula(n,lam*n)
            for val,target in ((float(vr)/n,lr),(float(vd)/n,lv),(float(c)/n,lc)):
                assert abs(val-target)<0.01,(lam,n,val,target)
                tests+=1
    print(f'PASS: {tests} exact identities and asymptotic probes; {perms} enumerated weighted permutations')

if __name__=='__main__': main()
