"""Direct checks for logarithmic races of positional palindromes.

Finite tests check the exact digit-prefix counting identity independently
of its analytical use. They are not a substitute for the infinite proof.
"""
from math import gcd, log
from fractions import Fraction
from itertools import permutations


def digits(n, base):
    assert n >= 1 and base >= 2
    out=[]
    while n:
        out.append(n % base)
        n//=base
    return out


def palindrome_count_brute(n, b):
    return sum(digits(j,b)==digits(j,b)[::-1] for j in range(1,n+1))


def palindrome_count_prefix(n,b):
    if n<1:return 0
    k=0
    z=n
    while z>=b:
        z//=b
        k+=1
    m=(k+1)//2
    H=b**m
    p=n//H
    # Build the palindrome belonging to the prefix p.
    # The first k+1 digits determine the mirror convention.
    prefix=[]
    z=p
    while z:
        prefix.append(z%b)
        z//=b
    leading=prefix[::-1]
    if (k+1)%2:
        mirrored=leading+leading[-2::-1]
    else:
        mirrored=leading+leading[::-1]
    palindrome=0
    for dig in mirrored:
        palindrome=palindrome*b+dig
    eps=int(palindrome<=n)
    return H+p+eps-2,eps,H,p


def rational_order_probability(ranges, permutation):
    """Exact ordered-volume integration, via polynomial integration.

    Integrate independent uniform T_i on [0,L_i] with integer L_i.
    Piecewise polynomial DP on breakpoints of the L_i, using fraction
    coefficients (ascending degree). This is a separate finite identity.
    """
    L=[ranges[i] for i in permutation]
    knots=sorted(set([0,*L]))
    poly=[Fraction(1)]
    # More straightforward exact iterate integrals by rational polynomial
    # over segments on [0,max L], clipping each upper endpoint.
    # f_0(t) = 1, f_j(t) = 1_{t<=L_j} integral_0^t f_{j-1}(s) ds.
    segments=[(knots[k],knots[k+1]) for k in range(len(knots)-1)]
    old=[[Fraction(1)] if a<L[0] else [Fraction(0)] for a,b in segments]
    for cap in L[1:]:
        new=[]
        running=Fraction(0)
        for idx,(a,b) in enumerate(segments):
            q=old[idx]
            anti=[Fraction(0)]+[v/Fraction(i+1) for i,v in enumerate(q)]
            evalp=lambda z:sum((coef*(z**i) for i,coef in enumerate(anti)),Fraction(0))
            if a>=cap:
                new.append([Fraction(0)])
            else:
                # on segment, cumulative + integral from a to t
                out=anti[:]
                out[0]+=running-evalp(a)
                new.append(out)
            running+=evalp(b)-evalp(a)
        old=new
    total=Fraction(0)
    for (a,b),q in zip(segments,old):
        anti=[Fraction(0)]+[v/Fraction(i+1) for i,v in enumerate(q)]
        total+=sum(coef*(b**i-a**i) for i,coef in enumerate(anti))
    prod=1
    for x in L:prod*=x
    return total/prod


def run():
    comparisons=0
    for base in (2,3,4,5,6,7,8,10,12):
        count=0
        for n in range(1,5001):
            if digits(n,base)==digits(n,base)[::-1]:count+=1
            exact,eps,H,p=palindrome_count_prefix(n,base)
            assert exact==count, (base,n,exact,count)
            assert eps in (0,1)
            assert -2 <= exact - (H+n//H) <= -1
            assert abs(count-(H+n/H))<=3.001
            comparisons+=1
    for L in ((1,2),(2,3),(2,4,6),(1,3,4),(2,3,5,9)):
        probs=[rational_order_probability(L,p) for p in permutations(range(len(L)))]
        assert sum(probs)==1,(L,probs,sum(probs))
        assert all(q>0 for q in probs),(L,probs)
        comparisons+=len(probs)
    # Pair ordering probability for U(0,a) and U(0,b).
    for a in range(1,8):
        for b in range(1,8):
            if a==b: continue
            expected=Fraction(a,2*b) if a<b else Fraction(1)-Fraction(b,2*a)
            value=rational_order_probability((a,b),(1,0))
            # event T_1 > T_2 is T_2 < T_1
            assert value==expected,(a,b,value,expected)
            comparisons+=1
    print('CERTIFICATE_PASS exact_count_and_volume_comparisons',comparisons)
    print('example_two_three_log_density',log(2)/(2*log(3)))
    print('three_base_order_probabilities_for_uniform_scales_1_3_4',
          [(p,str(rational_order_probability((1,3,4),p))) for p in permutations(range(3))])

if __name__=='__main__':run()
