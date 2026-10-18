"""Exact finite checks for path maximal variation on unimodal data."""
from fractions import Fraction
from itertools import product


def is_unimodal(x):
    n = len(x)
    return any(all(x[i] <= x[i+1] for i in range(k)) and
               all(x[i] >= x[i+1] for i in range(k,n-1)) for k in range(n))


def maximal(x):
    n=len(x)
    y=[]
    for j in range(n):
        y.append(max(Fraction(sum(x[max(0,j-r):min(n,j+r+1)]),
                              min(n,j+r+1)-max(0,j-r)) for r in range(n)))
    return y


def variation(x):
    return sum(abs(x[j+1]-x[j]) for j in range(len(x)-1))


def check(x):
    n=len(x)
    y=maximal(x)
    top=max(x)
    p=x.index(top)
    assert all(y[j]<=y[j+1] for j in range(p))
    assert all(y[j]>=y[j+1] for j in range(p,n-1))
    assert y[p] == top
    var=variation(x)
    output=variation(y)
    assert output <= Fraction(n-1,n)*var
    a=top-x[0]
    b=top-x[-1]
    gap=Fraction(n-1,n)*var-output
    lower=a*(Fraction(1,p+1)-Fraction(1,n))+b*(Fraction(1,n-p)-Fraction(1,n))
    assert gap>=lower>=0
    if var:
        eq=gap==0
        endpoint_spike=(x[0]>x[1] and all(v==x[1] for v in x[1:])) or \
            (x[-1]>x[-2] and all(v==x[-2] for v in x[:-1]))
        assert eq == endpoint_spike, (n,x,eq,endpoint_spike)
    return var>0


def main():
    checked=0
    nonconstant=0
    for n in range(3,11):
        for tup in product(range(4),repeat=n):
            if not is_unimodal(tup):
                continue
            nonconstant += check(list(tup))
            checked += 1
    # Sample rational noninteger profiles and non-symmetric modes.
    profiles=[
        [Fraction(1,7),Fraction(2,5),Fraction(7,4),Fraction(11,6),Fraction(3,4),Fraction(1,4)],
        [Fraction(2,3),Fraction(3,4),Fraction(9,10),Fraction(1),Fraction(1),Fraction(2,7)],
        [Fraction(3,2),Fraction(5,4),Fraction(1,3),Fraction(0)],
        [Fraction(0),Fraction(3,5),Fraction(3,5),Fraction(5,4),Fraction(7,5),Fraction(1,2)],
    ]
    for x in profiles:
        assert is_unimodal(x)
        check(x)
    print(f'VERIFY_OK exact_unimodal_vectors={checked} nonconstant={nonconstant} rational_profiles={len(profiles)}')

if __name__=='__main__':
    main()
