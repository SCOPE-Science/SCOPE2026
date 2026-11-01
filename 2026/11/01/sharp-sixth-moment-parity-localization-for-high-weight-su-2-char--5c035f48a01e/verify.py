"""Deterministic checks for the sixth-moment parity law on SU(2)."""
from collections import defaultdict
from math import sqrt
import itertools


def tensor(x, y):
    out = defaultdict(int)
    for a, ca in x.items():
        for b, cb in y.items():
            for j in range(abs(a-b), a+b+1, 2):
                out[j] += ca*cb
    return dict(out)


def exact_sixth(coefficients, start):
    """Coefficients are integers or Gaussian integers; exact Haar integral."""
    u = {start+s: v for s,v in coefficients.items() if v}
    squared = tensor(u,u)
    cubed = tensor(squared,u)
    return sum(abs(v)**2 for v in cubed.values())


def predicted(c, even_count, odd_count):
    plus=sum(c.values())
    minus=sum(((-1)**s)*v for s,v in c.items())
    return (abs(plus)**6+abs(minus)**6)/4


def profile(e,o,x):
    return ((e*x+o*(1-x))**3+12*e*o*x*(1-x)*(e*x+o*(1-x)))/2


def optimizer(e,o):
    if not o: return 1.0
    if not e: return 0.0
    # e>=o; for e<o reflect.
    if e<o:return 1-optimizer(o,e)
    r=e/o
    if r>=5:return 1.0
    t=(10*r*(r-1)+sqrt((10*r*(r-1))**2+4*r*r*(5-r)*(5*r-1)))/(2*r*r*(5-r))
    return t/(1+t)


def test():
    checks=0
    # Singlet sixth moment derived by Clebsch-Gordan.
    for m in range(1,30):
        expected=(m+1)*(m*m+2*m+2)//2
        assert exact_sixth({0:1},m)==expected
        checks+=1
    # A stable family: exact moments approach endpoint limit / m^3.
    families = [({0:1,1:1},16.0),({0:1,2:1},32.0),({0:1,1:1j},4.0),({0:1,1:-1},16.0),({0:1,2:1,4:1},364.5),({0:1,1:1,2:-1},0.5),({0:1,1:1,2:1,3:1},1024.0)]
    # Check against exact formula only for adequate values to avoid numerical claims of rigorous asymptotic.
    for coeff,lim in families:
        assert abs(predicted(coeff,0,0)-lim)<1e-12
        checks+=1
        errors=[]
        for m in (16,32,64,128):
            moment=exact_sixth(coeff,m)
            errors.append(abs(moment/m**3-lim)/lim)
            checks+=1
        assert errors[0]>errors[1]>errors[2]>errors[3]
        assert errors[3]<0.1
        checks+=2
    # Check explicit derivative-root classification, grid never exceeds exact optimum.
    for e in range(1,13):
        for o in range(1,13):
            p=optimizer(e,o)
            assert 0<=p<=1
            best=profile(e,o,p)
            for j in range(101):
                assert best+1e-7>=profile(e,o,j/100)
                checks+=1
            if e>=5*o: assert p==1
            if o>=5*e: assert p==0
            if e<5*o and o<5*e: assert 0<p<1
            checks+=1
    return checks

if __name__=='__main__':
    print('Verified',test(),'deterministic assertions')
