from fractions import Fraction
from math import comb

def density(t):
    h=t.bit_count(); assert t>0
    D={(0,0):Fraction(1)}
    for j in range(t.bit_length()):
        digit=(t>>j)&1; E={}
        for (carry,used),prob in D.items():
            for bit in (0,1):
                newcarry=(bit+digit+carry)//2
                v=used+newcarry
                if v<=h:E[(newcarry,v)]=E.get((newcarry,v),Fraction(0))+prob/2
        D=E
    return sum(p if carry==0 else p*(1-Fraction(1,2**(h-used+1))) for (carry,used),p in D.items())

for h in range(1,7):
    expect=Fraction(1,2)+Fraction(comb(2*h,h),2*4**h)
    for gap in (h+1,h+2,2*h+3):
        t=sum(1 << (i*gap) for i in range(h))
        got=density(t)
        assert got==expect,(h,gap,got,expect)
    if h>=2:
        t=sum(1 << (i*h) for i in range(h))
        print('h',h,'expected',expect,'at gap h',density(t),'expected?',density(t)==expect)
    print('OK',h,expect)
print('VERIFY_OK isolated_carries=PASS weights=1..6, three_distances_each')
