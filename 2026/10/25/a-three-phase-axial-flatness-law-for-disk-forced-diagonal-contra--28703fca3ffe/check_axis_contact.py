"""Finite checks for diagonal-disk support formulas."""
import math
from fractions import Fraction

def support(a,b,s,depth):
    x=ydef=0.0
    for k in range(depth):
        u=s*(a/b)**k
        hyp=math.hypot(1.0,u)
        x+=s*(a*a/b)**k/hyp
        # Stable evaluation of 1-1/sqrt(1+u²)
        ydef+=b**k*u*u/(hyp*(hyp+1.0))
    return x,ydef

def main():
    assertions=0
    for a,b in ((Fraction(1,2),Fraction(1,6)), (Fraction(1,2),Fraction(1,4)), (Fraction(1,2),Fraction(1,3))):
        assert 0<b<a<1;assertions+=1
    a=0.5;b=1/6
    q=math.log(b)/math.log(a)
    assert 2<q<3;assertions+=1
    ratios=[]
    for m in (6,10,14,18,22):
        x,d=support(a,b,3.0**(-m),m+60)
        ratio=d/x**q
        assert 0.001<ratio<1
        ratios.append(ratio);assertions+=1
    print('power exponent:',q,'normalized deficits:',ratios)
    a=.5;b=.25
    critical=[]
    for m in (24,32,40,48,64):
        x,d=support(a,b,2.0**(-m),m+65)
        z=d*math.log(1/x)/(x*x)
        critical.append(z)
        assert abs(z-math.log(2)/2)<0.12
        assertions+=1
    print('critical ratios:',critical,'limit:',math.log(2)/2)
    assert abs(critical[-1]-math.log(2)/2)<abs(critical[0]-math.log(2)/2);assertions+=1
    a=.5;b=1/3
    curv=[]
    for m in (8,14,22,28):
        x,d=support(a,b,2.0**(-m),m*2+40)
        z=d/(x*x)
        curv.append(z)
        assert abs(z-0.125)<.02;assertions+=1
    print('positive curvature ratios:',curv,'limit:',.125)
    for a,b in [(Fraction(1,2), Fraction(1,6)),(Fraction(2,3),Fraction(1,5)),(Fraction(3,4),Fraction(1,3))]:
        if b>=a*a: continue
        lam=a*a/b
        c0=math.sqrt(float(2*lam/(lam-1)))+float(a/(1-a))
        assert lam>1 and c0>1;assertions+=1
    print('PASS',assertions,'finite support and parameter checks')
if __name__=='__main__':main()
