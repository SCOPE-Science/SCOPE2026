from fractions import Fraction
from itertools import combinations

checks=0
for d in range(1,9):
    layers=list(range(d+1))
    for mask in range(1,1<<(d+1)):
        S=[s for s in layers if (mask>>s)&1]
        a,b=min(S),max(S)
        if 2*b<d:
            h=Fraction(b,1)
            contact={b}
        elif 2*a>d:
            h=Fraction(a,1)
            contact={a}
        else:
            h=Fraction(d,2)
            contact=set(S)
        t=h/Fraction(d,1)
        R2=h*(d-h)/d
        seen=set()
        for s in S:
            q=Fraction(s,1)*(1-t)**2+Fraction(d-s,1)*t*t
            assert q<=R2,(d,S,s,q,R2)
            if q==R2: seen.add(s)
        assert seen==contact,(d,S,seen,contact)
        # objective on the diagonal is the max of the endpoint quadratics;
        # compare with exact values at a grid around t* as corroboration.
        for j in range(-2*d,4*d+1):
            u=Fraction(j,2*d) if d else Fraction(0)
            val=max(Fraction(s,1)*(1-u)**2+Fraction(d-s,1)*u*u for s in S)
            assert val>=R2
        checks+=1
print(f'VERIFY_OK s-hypersimplex-MEB families={checks} d=1..8 exact=yes')
