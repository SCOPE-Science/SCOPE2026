"""Exact arithmetic and high precision checks for two-bit exchangeability transport.

This is a finite regression verifier; it is not a proof of the universal statements.
"""
from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec=65

def dec(x):
    return Decimal(x.numerator)/Decimal(x.denominator) if isinstance(x, Fraction) else Decimal(x)

def projection(a,c):
    a=dec(a); c=dec(c)
    sa=a.sqrt(); sc=c.sqrt()
    if sa+sc>=1: return Decimal(0),None
    q=min(max(Decimal(1)/2,sa),Decimal(1)-sc)
    return q*q+(1-q)*(1-q)-a-c,q

def distance(a,c,A,C):
    a=dec(a);c=dec(c);A=dec(A);C=dec(C)
    return (abs(a-A)+abs(c-C)+abs(a+c-A-C))/2

def trial(N,m):
    d=N*(N-1)
    return Fraction(m*(m-1),d),Fraction((N-m)*(N-m-1),d)

def product(q):
    q=dec(q)
    return q*q,(1-q)*(1-q)

def test():
    urns=0; phases=set(); tested_mixtures=0; parity_cases=0
    for N in range(2,51):
        values=[]
        for m in range(N+1):
            a,c=trial(N,m)
            t,q=projection(a,c)
            if q is not None:
                A,C=product(q)
                assert abs(distance(a,c,A,C)-t)<Decimal('1e-55')
                if dec(c)>=Decimal(1)/4: phases.add('left')
                elif dec(a)>=Decimal(1)/4:phases.add('right')
                else: phases.add('mid')
            values.append(t)
            urns+=1
        peak=max(values)
        if N%2==0:
            expected=Decimal(1)/(2*(N-1))
        else:
            expected=Decimal(1)+Decimal(1)/N-(Decimal(1)+Decimal(1)/N).sqrt()
        assert abs(peak-expected)<Decimal('1e-54'),(N,peak,expected)
        assert values[N//2]==peak and values[(N+1)//2]==peak
        for m in range(1,N//2+1):
            assert values[m]>=values[m-1]
        parity_cases+=1
    for ia in range(0,14):
        for ic in range(0,14):
            a=Fraction(ia,16); c=Fraction(ic,16)
            if a+c>1: continue
            opt,q=projection(a,c)
            if q is None: continue
            for jq in range(0,21):
                x=Fraction(jq,20)
                A,C=product(x)
                assert distance(a,c,A,C)+Decimal('1e-55')>=opt
                tested_mixtures+=1
            for jq in range(0,11,2):
                for jv in range(0,11,2):
                    x=Fraction(jq,10); y=Fraction(jv,10)
                    for num in (1,3,7,9):
                        w=Fraction(num,10)
                        A=w*x*x+(1-w)*y*y
                        C=w*(1-x)*(1-x)+(1-w)*(1-y)*(1-y)
                        assert distance(a,c,A,C)+Decimal('1e-55')>=opt
                        tested_mixtures+=1
    assert phases=={'left','mid','right'}
    print(f'VERIFY_OK urns={urns} cases={tested_mixtures} parity={parity_cases} phases=3')

if __name__=='__main__': test()
