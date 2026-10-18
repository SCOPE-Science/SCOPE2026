"""Standalone rational interval checks for Cantor-measure spectral profile."""
from fractions import Fraction as F
from math import factorial

def exp_minus(x):
    assert x >= 0
    scale=0
    while x > 1:
        x /= 2
        scale+=1
    low=sum(((-x)**j)/factorial(j) for j in range(26))
    up=sum(((-x)**j)/factorial(j) for j in range(25))
    return low**(2**scale), up**(2**scale)

def log_two():
    low=2*sum(F(1,(2*j+1)*3**(2*j+1)) for j in range(21))
    rem=F(2,43*3**43)*F(9,8)
    return low,low+rem

def log_three():
    low=2*sum(F(1,(2*j+1)*2**(2*j+1)) for j in range(21))
    rem=F(2,43*2**43)*F(4,3)
    return low,low+rem

def exp_plus(x):
    assert 0<=x<=2
    low=sum(x**j/F(factorial(j)) for j in range(31))
    t=x**31/F(factorial(31))
    return low,low+t/(1-x/32)

def positive_int(x):return F(x,1)

def mul(a,b):return a[0]*b[0],a[1]*b[1]
def add(a,b):return a[0]+b[0],a[1]+b[1]
def ratio(c,a):return c/a[1],c/a[0]

def k_bounds(y):
    y=F(y)
    Fp=(F(1),F(1)); Fl=(F(0),F(0))
    for j in range(1,19):
        c=F(2,3**j)
        r=exp_minus(c*y)
        Fp=mul(Fp,((1+r[0])/2,(1+r[1])/2))
        Fl=add(Fl,mul((c,c),ratio(F(1),(1+r[0],1+r[1])))) if False else Fl
        # c * exp(-x)/(1+exp(-x))
        Fl=add(Fl,(c*r[0]/(1+r[0]), c*r[1]/(1+r[1])))
    Fp=(Fp[0]*(1-y/F(3**18)),Fp[1])
    Fl=(Fl[0], Fl[1]+F(1,2*3**18))
    Pp=(F(1),F(1)); Pl=(F(0),F(0))
    for j in range(4):
        c=F(2*3**j)
        r=exp_minus(c*y)
        Pp=mul(Pp,(1+r[0],1+r[1]))
        Pl=add(Pl,(c*r[0]/(1+r[0]),c*r[1]/(1+r[1])))
    rtail=F(1,2**int(2*3**4*y))
    Pp=(Pp[0],Pp[1]*(1+4*rtail))
    Pl=(Pl[0],Pl[1]+4*3**4*rtail)
    if y==1: powfac=(F(1),F(1))
    elif y==2:
        l2=log_two()
        dl,du=F(6309297,10000000),F(6309298,10000000)
        l3=log_three()
        assert l2[0]/l3[1] > dl and l2[1]/l3[0] < du
        powfac=(exp_plus((1+dl)*l2[0])[0],exp_plus((1+du)*l2[1])[1])
    else: raise ValueError('only 1 or 2')
    return mul(powfac,mul(Fp,mul(Pp,add(Fl,Pl))))
if __name__=='__main__':
    one=k_bounds(1);two=k_bounds(2)
    for y,(a,b) in [(1,one),(2,two)]:
        print('K',y,'[',float(a),',',float(b),']')
        assert b-a<F(1,100000)
    assert one[0]>two[1]+F(1,1000)
    print('CERTIFIED separation >',float(one[0]-two[1]))
