from fractions import Fraction
from math import gcd

def ninf(v):
    return max(abs(v[0]),abs(v[1]))

def phi(x,y):
    xp=(x[0]+y[0],x[1]+y[1])
    xm=(x[0]-y[0],x[1]-y[1])
    a=ninf(xp); b=ninf(xm)
    u=(xp[0]/a,xp[1]/a)
    v=(xm[0]/b,xm[1]/b)
    return (a+b)*ninf((u[0]-v[0],u[1]-v[1]))/2, a, b

count=0
for q in range(1,81):
    for p in range(1,q+1):
        if gcd(p,q)!=1:
            continue
        r=Fraction(p,q)
        x=(Fraction(1), Fraction(1)-2*r)
        y=(Fraction(1), Fraction(1))
        assert ninf(x)==1 and ninf(y)==1
        val,a,b=phi(x,y)
        assert a==2 and b==2*r
        assert min(a,b)/max(a,b)==r
        target=2+r-r*r
        assert val==target
        assert target==Fraction(9,4)-(r-Fraction(1,2))**2
        count+=1

r=Fraction(1,2)
x=(Fraction(1),Fraction(0))
y=(Fraction(1),Fraction(1))
val,a,b=phi(x,y)
assert (a,b,val)==(2,1,Fraction(9,4))
assert ninf((3*y[0]-x[0],3*y[1]-x[1]))==3

print(f"VERIFY_OK rational_ratios={count} envelope=2+r-r^2 endpoint=9/4 equality_chords=2,1,3")
