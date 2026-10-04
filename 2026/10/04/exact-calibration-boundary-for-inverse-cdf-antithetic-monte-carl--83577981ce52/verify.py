from fractions import Fraction
from math import factorial

def beta_mix(B,c):
    comb=Fraction(factorial(B),factorial(c)*factorial(B-c))
    beta=Fraction(factorial(c)*factorial(B-c),factorial(B+1))
    return comb*beta

def masses(B):
    d={j:Fraction(1,2*(B+1)) for j in range(1,B+1)}
    d[B+1]=Fraction(1,B+1)
    d.update({j:Fraction(1,2*(B+1)) for j in range(B+2,2*B+2)})
    return d

for B in range(1,201):
    assert all(beta_mix(B,c)==Fraction(1,B+1) for c in range(B+1))
    m=masses(B); assert sum(m.values(),Fraction())==1
    cdf=Fraction(); first=None; best=(Fraction(-1),None)
    for j in range(1,2*B+2):
        cdf += m[j]
        exp=Fraction(j,2*(B+1)) if j<=B else Fraction(j+1,2*(B+1))
        assert cdf==exp
        exc=cdf-Fraction(j,2*B+1)
        if j<=B: assert exc<0
        elif j<=2*B:
            assert exc>0
            if first is None: first=j
        else: assert exc==0
        if exc>best[0]: best=(exc,j)
    assert first==B+1 and best[1]==B+1
    assert best[0]==Fraction(B,2*(B+1)*(2*B+1))
assert masses(1)=={1:Fraction(1,4),2:Fraction(1,2),3:Fraction(1,4)}
print("VERIFY_OK")
