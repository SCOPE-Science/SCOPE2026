"""Exact independent verifiers for three-one binary-shift digit-sum density."""
from collections import defaultdict
from functools import lru_cache
from fractions import Fraction

EXPECTED = (
    (Fraction(43,64), Fraction(19,32), Fraction(41,64), Fraction(21,32)),
    (Fraction(19,32), Fraction(5,8), Fraction(5,8), Fraction(41,64)),
    (Fraction(41,64), Fraction(5,8), Fraction(5,8), Fraction(41,64)),
    (Fraction(21,32), Fraction(41,64), Fraction(41,64), Fraction(21,32)),
)

def shift(a,b):
    assert a>=1 and b>=1
    return 1 + (1<<a) + (1<<(a+b))

def digit_carry_probability(t):
    """Count all n bit-strings with at most three outgoing carries.

    Beyond highest 1 digit of t, three 0 columns exhaust the carry budget.
    Integer states are exact counts; denominator 2**(bitlen(t)+3).
    """
    assert t>0 and t.bit_count()==3
    L=t.bit_length()+3
    states={(0,0):1}
    for i in range(L):
        bit=(t>>i)&1
        nxt=defaultdict(int)
        for (carry,k), multiplicity in states.items():
            for x in (0,1):
                outgoing=int(x+bit+carry>=2)
                if k+outgoing<=3:
                    nxt[(outgoing,k+outgoing)] += multiplicity
        states=dict(nxt)
    assert all(carry==0 for carry,k in states)
    return Fraction(sum(states.values()), 1<<L)

@lru_cache(None)
def stop_distribution(t):
    """Cheng's finite deconvolution P_t, independently of carry counting."""
    assert t>=1
    if t==1:
        return {0:Fraction(1)}
    if t%2==0:
        return stop_distribution(t//2)
    u=t//2
    out=defaultdict(Fraction)
    for j,p in stop_distribution(u).items():
        out[j+1] += p/2
    for j,p in stop_distribution(u+1).items():
        out[j-1] += p/2
    assert sum(out.values())==1
    return dict(out)

def convolution_probability(t):
    result=Fraction(0)
    for v,p in stop_distribution(t).items():
        if v>=-1:
            result += p*(1-Fraction(1, 2**(v+2)))
    return result

def brute_density(t):
    """Directly enumerate one complete finite carry-determining residue period."""
    L=t.bit_length()+3
    return Fraction(sum((n+t).bit_count()>=n.bit_count() for n in range(1<<L)),1<<L)

def run():
    cells=0
    for a in range(1,5):
        for b in range(1,5):
            t=shift(a,b)
            expected=EXPECTED[a-1][b-1]
            assert digit_carry_probability(t)==expected, (a,b,'carry')
            assert convolution_probability(t)==expected, (a,b,'deconvolution')
            assert brute_density(t)==expected, (a,b,'brute')
            cells+=1
    stress=0
    vals=set()
    for a in range(1,17):
        for b in range(1,17):
            t=shift(a,b)
            expected=EXPECTED[min(a,4)-1][min(b,4)-1]
            assert digit_carry_probability(t)==expected,(a,b,'carry')
            assert convolution_probability(t)==expected,(a,b,'deconvolution')
            vals.add(expected)
            stress+=1
    assert vals==set(sum((list(x) for x in EXPECTED),[]))
    print('CANONICAL_CELLS_OK:',cells)
    print('INDEPENDENT_METHODS: carry-count, deconvolution, direct-residue enumeration')
    print('GAP_STRESS_PAIRS_OK:',stress)
    print('ATTAINED_VALUES:',','.join(map(str,sorted(vals))))
    print('MINIMUM:',min(vals),'BIAS:',min(vals)-Fraction(1,2))
    print('MINIMIZING_GAPS_CANONICAL:', [(a+1,b+1) for a,row in enumerate(EXPECTED) for b,v in enumerate(row) if v==min(vals)])
    print('RESULT: ALL_EXACT_CHECKS_PASS')

if __name__=='__main__':
    run()
