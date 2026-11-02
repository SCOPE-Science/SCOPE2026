#!/usr/bin/env python3
"""Finite independent checks of a closed residue-gap formula (no external dependencies)."""
def expected(p, t):
    h=(p-1)//2
    E=h//2+1
    O=(h+1)//2
    qinv=pow(2,-1,p)
    b=t*(t-1)//2+(t*E)//p+(t*O)//p
    return [b + int(((j-1)*qinv)%p < (t*E)%p)
              + int(((j-1-t)*qinv)%p < (t*O)%p)
            for j in range(p)]

def check():
    cases=0
    for p in range(3,80,2):
        for t in range(1,35):
            a=p*t+1
            h=(p-1)//2
            upper=p*t*t-(h-1)*t-1
            actual=[0]*p
            for x in range(1,upper+1):
                k,y=divmod(p*x,a)
                if y>k:
                    actual[x%p]+=1
            want=expected(p,t)
            assert actual==want,(p,t,actual,want)
            assert max(actual)-min(actual)<=2
            assert sum(actual)==t*(p*t+1)//2
            if p>=5 and t==2:
                assert max(actual)-min(actual)==2
            cases+=1
    print('PASS:',cases,'exact histogram cases; sharpness witnesses checked')

if __name__=='__main__':
    check()
