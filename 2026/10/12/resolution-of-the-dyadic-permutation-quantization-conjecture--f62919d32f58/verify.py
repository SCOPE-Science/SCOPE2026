from fractions import Fraction
from itertools import permutations

def pair_cost(x,y):
    return x*y/(x+y)

checks=0
boundary_equalities=0
for k in range(2,9):
    vals=[Fraction(1,2**j) for j in range(1,k)]
    for perm in permutations(vals):
        w={j+1:perm[j] for j in range(k-1)}
        for j in range(k,k+20):
            w[j]=Fraction(1,2**j)
        for n in range(k+2,k+7):
            U=Fraction(8,3*2**n)
            c_pair=pair_cost(Fraction(1,2**(n-1)),Fraction(1,2**n))
            tail_mass=Fraction(1,2**n)
            assert c_pair + 2*tail_mass == U
            for r in range(1,n-2):
                d=pair_cost(w[r],w[r+1])
                assert d>=U
                checks+=1
                if d==U: boundary_equalities+=1
for k in range(3,30):
    assert Fraction(1,2**(k-1)+2**(k-2))==Fraction(4,3*2**k)
    assert pair_cost(Fraction(1,2**(k-1)),Fraction(1,2**k))==Fraction(2,3*2**k)
print(f"checked_adjacent_pair_inequalities={checks}")
print(f"boundary_equalities={boundary_equalities}")
print("VERIFY_OK")
