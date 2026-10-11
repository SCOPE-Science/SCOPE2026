#!/usr/bin/env python3
from fractions import Fraction

def facet_data(n,k,l):
    N=n+1
    t=k+l
    W=Fraction(k*(k+2*l+1),2)
    Q=Fraction((k-1)*k*(2*k-1),6)+(l+1)*k*k
    P=Q-W*W/N
    mu=Fraction(3**N,N)
    kappa=Fraction(3**(t+1)-3**(l+1),2)+Fraction(3**k-3*k,3**n-n-1)
    X=mu*W-kappa
    H2=Fraction(N,n)*P
    singleton2=(mu-3)**2*Fraction(N,n)
    distance2=X*X/P
    delta=X*X-(mu-3)**2*H2
    return distance2,singleton2,delta

expected={
    (3,2):Fraction(45),
    (4,2):Fraction(1191,2),
    (4,3):Fraction(1683,2),
    (5,4):Fraction(53901,5),
    (6,5):Fraction(118818),
}
for (N,t),want in expected.items():
    n=N-1
    vals=[]
    for k in range(1,t+1):
        l=t-k
        vals.append(facet_data(n,k,l)[2])
    assert min(vals)==want,(N,t,min(vals),want)
    assert all(v>0 for v in vals)

checks=0
for n in range(2,61):
    equality=[]
    for k in range(1,n+1):
        for l in range(0,n-k+1):
            d2,r2,delta=facet_data(n,k,l)
            assert d2>=r2,(n,k,l,d2,r2)
            if d2==r2:
                equality.append((k,l))
            checks+=1
    assert equality==[(1,0)],(n,equality)

print(f"VERIFY_OK simple-permutoassociahedron-inradius facet_checks={checks} n=2..60 exact=yes")
