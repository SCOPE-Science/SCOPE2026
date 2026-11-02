"""Standalone exact checks for the two-speed continuous-time coupon ballot theorem.

Uses the Python standard library only. Finite checks complement, and do not
replace, the analytical proof of the expansion and logarithmic susceptibility.
"""
from fractions import Fraction as Q
from functools import lru_cache
from math import comb, lgamma, exp, log


def catalan(n):
    return comb(2*n, n)//(n+1)


def harmonic(n):
    return sum((Q(1, k) for k in range(1, n+1)), Q(0))


def fast_count_formula(m, j):
    return catalan(m) + sum(catalan(r)*catalan(m-r)
        for r in range((j+1)//2, m))


def fast_count_exhaustive(m, j):
    count=0
    for word in range(1 << (2*m)):
        if word.bit_count()!=m: continue
        heights=[0]
        for k in range(2*m):
            heights.append(heights[-1]+(1 if (word>>k)&1 else -1))
        count += (min(heights[:j+1])>=0 and min(heights[j:])>=-1)
    return count


def kappa(m):
    h=harmonic(2*m)
    return sum((Q(catalan(r)*catalan(m-r),comb(2*m,m))
               *(h-harmonic(2*m-2*r-1))
               for r in range(m)), Q(0))


def slope(m, l):
    return Q(4*l,l+1)*kappa(m)


def grouped_probability(m,l,q):
    q=Q(q)
    assert q>0
    @lru_cache(None)
    def F(a,b,c,d):
        if a+c<b+d:return Q(0)
        if a==m and c==l:return Q(1)
        rates=[Q(m-a),Q(m-b),q*(l-c),q*(l-d)]
        total=sum(rates)
        acc=Q(0)
        for axis in range(4):
            if rates[axis]:
                state=[a,b,c,d]
                state[axis]+=1
                acc+=rates[axis]/total*F(*state)
        return acc
    return 2*F(0,0,0,0)


def labeled_probability(m,l,q):
    q=Q(q)
    rates=tuple([Q(1)]*m+[q]*l+[Q(1)]*m+[q]*l)
    d=m+l
    @lru_cache(None)
    def F(mask):
        a=(mask&((1<<d)-1)).bit_count()
        b=(mask>>d).bit_count()
        if a<b:return Q(0)
        if a==d:return Q(1)
        total=sum(rates[i] for i in range(2*d) if not (mask>>i)&1)
        return sum((rates[i]/total*F(mask|(1<<i))
                     for i in range(2*d) if not (mask>>i)&1), Q(0))
    return 2*F(0)


def kappa_float(m):
    log_choose=lgamma(2*m+1)-2*lgamma(m+1)
    def log_cat(t):
        return lgamma(2*t+1)-2*lgamma(t+1)-log(t+1)
    H=[0.0]*(2*m+1)
    for i in range(1,2*m+1):H[i]=H[i-1]+1/i
    return sum(exp(log_cat(r)+log_cat(m-r)-log_choose)
            *(H[2*m]-H[2*m-2*r-1]) for r in range(m))


def run():
    assertions=0
    def check(v):
        nonlocal assertions
        assert v
        assertions+=1
    for m in range(1,8):
        for j in range(2*m):
            check(fast_count_exhaustive(m,j)==fast_count_formula(m,j))
        check(fast_count_formula(m,0)==catalan(m+1))
        check(fast_count_formula(m,2*m-1)==catalan(m))
        check(kappa(m)>0)
    check(kappa(1)==Q(1,4))
    check(kappa(2)==Q(19,72))
    check(kappa(3)==Q(149,600))
    check(slope(2,1)==Q(19,36))
    for q in [Q(1,9),Q(1,3),Q(1),Q(3),Q(9)]:
        exact=Q(2*q**4+11*q**3+22*q**2+11*q+2,
                2*(q+1)**2*(q+2)*(2*q+1))
        check(grouped_probability(1,1,q)==exact)
    for m in range(1,4):
        for l in range(1,4):
            check(grouped_probability(m,l,Q(1))==Q(2,m+l+1))
            for q in [Q(1,3),Q(1,7)]:
                check(grouped_probability(m,l,q)==labeled_probability(m,l,q))
            for q in [Q(1,1000),Q(1,10000)]:
                val=grouped_probability(m,l,q)
                approx=Q(2,(m+1)*(l+1))+slope(m,l)*q
                check(abs(val-approx)<100*q*q)
    for m in [20,50,100,500,1000,5000]:
        R=m*kappa_float(m)/log(m)
        check(0.55 <R<1.1)
    print(f"PASS: {assertions} deterministic assertions")
    print("Catalan-convolution, rational-race, closed-form and first-order checks passed")
    print("Checks are finite; the infinite theorem is established in the written proof")

if __name__=='__main__':run()
