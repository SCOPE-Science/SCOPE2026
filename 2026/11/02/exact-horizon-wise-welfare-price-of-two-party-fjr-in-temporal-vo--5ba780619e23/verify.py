"""Exact integer-arithmetic checks of two-party party-list FJR+ price."""
from fractions import Fraction

def opt_brute(n,b,L):
    a=n-b
    floor_a=L*a//n
    floor_b=L*b//n
    options=[a*(L-w)+b*w for w in range(floor_b,L-floor_a+1)]
    assert options
    return max(options)

def rational_price(n,b,L):
    a=n-b
    return Fraction(a*L,a*L-(a-b)*(L*b//n))

def horizon_frontier(L):
    vals={j:Fraction(L*(L-j),L*L-2*L*j+2*j*j) for j in range(L//2+1)}
    return max(vals.values())

cases=allocations=0
for n in range(2,61):
    for L in range(1,51):
        vals=[]
        for b in range(1,n//2+1):
            a=n-b
            predicted=a*L-(a-b)*(L*b//n)
            observed=opt_brute(n,b,L)
            assert observed==predicted,(n,L,b,observed,predicted)
            vals.append(rational_price(n,b,L))
            cases+=1
            allocations+=L-(L*a//n)-(L*b//n)+1
        assert max(vals)<=horizon_frontier(L)

for L in range(1,91):
    H=horizon_frontier(L)
    bound_indices=list(range(L//2+1))
    # discrete search over the two integers nearest the unique continuous maximizer
    from math import sqrt,floor,ceil
    alpha=L*(1-1/sqrt(2))
    nearest={min(L//2,max(0,j)) for j in (floor(alpha),ceil(alpha))}
    assert max(Fraction(L*(L-j),L*L-2*L*j+2*j*j) for j in nearest)==H
    if L>=3:
        b=max(range(L//2+1),key=lambda j: Fraction(L*(L-j),L*L-2*L*j+2*j*j))
        assert rational_price(L,b,L)==H
assert horizon_frontier(3)==Fraction(6,5)
assert horizon_frontier(4)==Fraction(6,5)
assert horizon_frontier(5)==Fraction(20,17)
assert horizon_frontier(6)==Fraction(6,5)
assert horizon_frontier(7)==Fraction(35,29)
print(f'VERIFY_OK finite_profiles={cases} feasible_seat_counts={allocations} horizons=90 exact_examples=5')
