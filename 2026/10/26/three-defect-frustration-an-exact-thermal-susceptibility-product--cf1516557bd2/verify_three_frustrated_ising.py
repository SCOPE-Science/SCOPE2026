"""Exact checks of the three-defect Ising ring susceptibility product law.
Run with Python 3.9+; standard library only.
"""
from fractions import Fraction
from itertools import product


def full_enumeration(n, a, b, c, t):
    assert a+b+c == n and min(a,b,c)>=1 and 0<t<1
    neg = {a-1, a+b-1, n-1}
    Z=Fraction(0); mom=Fraction(0)
    for s in product((-1,1), repeat=n):
        w=Fraction(1)
        for i in range(n):
            w *= 1 + ( -t if i in neg else t ) * s[i]*s[(i+1)%n]
        Z += w
        mom += w*sum(s)**2
    return mom/(n*Z)


def B(n,t):
    return Fraction(1) + Fraction(2,n*(1-t**n))*sum((n-2*d)*t**d for d in range(1,n))


def formula(n,a,b,c,t):
    return B(n,t)-8*t*(1-t**a)*(1-t**b)*(1-t**c)/(n*(1-t)**2*(1-t**n))


def ground_formula(n,a,b,c):
    return Fraction(n*n+2,3*n)-Fraction(8*a*b*c,n*n)


def ground_exact(n,a,b,c):
    neg={a-1,a+b-1,n-1}
    energies=[]
    for s in product((-1,1),repeat=n):
        en = -sum((-1 if i in neg else 1)*s[i]*s[(i+1)%n] for i in range(n))
        energies.append((en, sum(s)**2))
    mn=min(x[0] for x in energies)
    ls=[m for e,m in energies if e==mn]
    assert len(ls)==2*n, (n,a,b,c,len(ls))
    return Fraction(sum(ls),len(ls)*n)


def main():
    count=0; ground=0; placements=0
    for n in range(3,10):
        vals={}
        for a in range(1,n-1):
            for b in range(1,n-a):
                c=n-a-b
                for t in (Fraction(1,5),Fraction(1,2),Fraction(4,5)):
                    actual=full_enumeration(n,a,b,c,t)
                    theorem=formula(n,a,b,c,t)
                    assert actual==theorem, (n,a,b,c,t,actual,theorem)
                    count+=1
                x=ground_exact(n,a,b,c)
                assert x==ground_formula(n,a,b,c), (n,a,b,c,x)
                ground+=1
                vals[a,b,c]=formula(n,a,b,c,Fraction(2,5))
        mx=max(vals.values()); mn=min(vals.values())
        expected_max={g for g in vals if sorted(g)==[1,1,n-2]}
        expected_min={g for g in vals if max(g)-min(g)<=1}
        assert {g for g,v in vals.items() if v==mx}==expected_max
        assert {g for g,v in vals.items() if v==mn}==expected_min
        placements+=1
    print(f'PASS: {count} independent exact rational full-spin tests, {ground} zero-temperature enumeration tests, {placements} exact extremizer enumerations.')

if __name__=='__main__':main()
