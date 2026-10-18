"""Standalone exact-rational and arbitrary-precision checks for pooled stochastic seed-bank allocation."""
from math import comb
from fractions import Fraction as F
from decimal import Decimal, localcontext


def derivative_fraction(k, g, p, s, B):
    return sum((F(comb(k,j)) * p**j * (1-p)**(k-j)) *
               (B*F(j,k)-s)/(s*(1-g)+B*g*F(j,k))
               for j in range(k+1))


def derivative_decimal(k, g, p, s, B):
    return sum(Decimal(comb(k,j))*p**j*(1-p)**(k-j) *
               (B*Decimal(j)/k-s)/(s*(1-g)+B*g*Decimal(j)/k)
               for j in range(k+1))


def root_decimal(k,p,s,B):
    with localcontext() as ctx:
        ctx.prec=100
        lo=Decimal(0); hi=Decimal(1)-Decimal('1e-95')
        for _ in range(360):
            mid=(lo+hi)/2
            if derivative_decimal(k,mid,p,s,B)>0: lo=mid
            else: hi=mid
        return +(lo+hi)/2


def main():
    p=F(1,2); s=F(4,5); B=F(16,5)
    assert derivative_fraction(1,F(1,3),p,s,B)==0
    # k=2 critical numerator is 4(1-3g^2) divided by (1-g)(1+g)(1+3g).
    for g in [F(1,10), F(1,3), F(1,2), F(2,3), F(9,10)]:
        expected=(1-3*g*g)/((1-g)*(1+g)*(1+3*g))
        assert derivative_fraction(2,g,p,s,B)==expected
    trials=0
    for pp in [F(1,5),F(1,2),F(4,5)]:
        for ss in [F(2,5),F(3,5),F(4,5)]:
            for BB in [F(2),F(4),F(8)]:
                if BB*pp<=ss: continue
                for g in [F(1,10),F(1,3),F(2,3),F(9,10)]:
                    for k in range(1,12):
                        assert derivative_fraction(k+1,g,pp,ss,BB)>derivative_fraction(k,g,pp,ss,BB)
                        trials+=1
    with localcontext() as ctx:
        ctx.prec=100
        pd=Decimal('0.5'); sd=Decimal('0.8'); Bd=Decimal('3.2')
        previous=Decimal(0)
        for k in range(1,61):
            root=root_decimal(k,pd,sd,Bd)
            assert root>previous and root<1
            previous=root
        print('Rational derivative comparisons:',trials)
        for k in [1,2,4,8,16,32,60]:
            root=root_decimal(k,pd,sd,Bd)
            ratio=(1-root)/(Decimal('0.5')**k)
            print('k=',k,'optimal germination=',str(root)[:40], 'rescaled reserve=',str(ratio)[:22])
        assert abs((1-root_decimal(60,pd,sd,Bd))/Decimal('0.5')**60-2)<Decimal('0.1')
    print('All checks passed.')

if __name__=='__main__':main()
