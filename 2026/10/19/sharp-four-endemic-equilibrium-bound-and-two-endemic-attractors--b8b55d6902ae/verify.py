"""Exact-arithmetic witness for a purely triadic two-class SIS model.
Run: python verify.py (Python 3 standard library only).
"""
from fractions import Fraction as F

def poly(z, a=10**8, b=100, p=F(1,1000)):
    return a*b*z**4-a*b*z**3+(a+b)*z*z-(p*a+(1-p)*b)*z+1

def fix(z, a=10**8, b=100, p=F(1,1000)):
    return p*(a*z*z/(1+a*z*z))+(1-p)*(b*z*z/(1+b*z*z))-z

def check():
    xs=[F(0),F(1,50000),F(1,500),F(1,50),F(1)]
    signs=[1,-1,1,-1,1]
    for x,s in zip(xs,signs):
        assert poly(x)*s>0,(x,poly(x))
    # Check the polynomial clearing-denominator identity exactly.
    for x in [F(0),F(1,100000),F(1,1000),F(1,100),F(1,2),F(1)]:
        assert fix(x)*(1+10**8*x*x)*(1+100*x*x)==-x*poly(x)
    brackets=[]
    for lo,hi in zip(xs,xs[1:]):
        sl=1 if poly(lo)>0 else -1
        for _ in range(80):
            mid=(lo+hi)/2
            sm=1 if poly(mid)>0 else -1
            if sm==sl: lo=mid
            else: hi=mid
        assert poly(lo)*poly(hi)<0 and 0<=lo<hi<=1
        brackets.append((float(lo),float(hi)))
    print('PASS: 5 exact sign witnesses, 6 polynomial identities, 4 disjoint 80-step rational root brackets')
    for i,(lo,hi) in enumerate(brackets,1):
        print('root',i,'in',(lo,hi))

if __name__=='__main__':check()
