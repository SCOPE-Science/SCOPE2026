#!/usr/bin/env python3
from fractions import Fraction

def ceil_frac(x):
    return (x.numerator + x.denominator - 1)//x.denominator

def var_es(losses, alpha):
    xs=sorted(Fraction(x) for x in losses)
    n=len(xs)
    k=ceil_frac(alpha*n)  # 1-based left quantile index
    var=xs[k-1]
    # Integral of left-continuous empirical quantile on [alpha,1].
    total=Fraction(0)
    for j,x in enumerate(xs, start=1):
        left=Fraction(j-1,n)
        right=Fraction(j,n)
        width=max(Fraction(0), right-max(left,alpha))
        total += width*x
    es=total/(1-alpha)
    return var,es

levels=[
    Fraction(1,2), Fraction(2,3), Fraction(3,4), Fraction(7,10),
    Fraction(9,10), Fraction(19,20), Fraction(39,40), Fraction(99,100),
    Fraction(5,8), Fraction(11,13)
]

checks=0
for alpha in levels:
    p=1-alpha
    nstar=ceil_frac(Fraction(2,1)/p)
    assert nstar >= 3
    # Below threshold, same-maximum order cannot reverse.
    for n in range(2,nstar):
        r=n*p
        # Formula has at most the top two empirical atoms in the ES tail.
        if r < 1:
            # VaR=ES=max.
            A=[0]*(n-1)+[7]
            B=[0]*(n-1)+[7]
            va,ea=var_es(A,alpha); vb,eb=var_es(B,alpha)
            assert va==ea==vb==eb==7
        else:
            assert r < 2
            # VaR is second-largest and ES is an increasing affine function
            # of that value when the maximum is held fixed.
            for x in range(0,5):
                for y in range(x,5):
                    A=[0]*(n-2)+[x,7]
                    B=[0]*(n-2)+[y,7]
                    va,ea=var_es(A,alpha); vb,eb=var_es(B,alpha)
                    assert va==x and vb==y
                    assert (ea-eb)*(va-vb) >= 0
                    checks += 1

    # At the threshold, equal mean and equal maximum witness.
    n=nstar
    r=n*p
    assert Fraction(2) <= r < Fraction(3)
    A=[0]*(n-3)+[1,3,4]
    B=[0]*(n-3)+[2,2,4]
    assert sum(A)==sum(B)==8
    assert max(A)==max(B)==4
    va,ea=var_es(A,alpha)
    vb,eb=var_es(B,alpha)
    assert va==1 and vb==2
    assert ea == (r+5)/r
    assert eb == (2*r+2)/r
    assert ea-eb == (3-r)/r > 0
    assert va < vb and ea > eb
    checks += 1

# Practical benchmarks.
for alpha,n in [(Fraction(19,20),40),(Fraction(39,40),80)]:
    assert ceil_frac(Fraction(2,1)/(1-alpha))==n
    A=[0]*(n-3)+[1,3,4]
    B=[0]*(n-3)+[2,2,4]
    va,ea=var_es(A,alpha); vb,eb=var_es(B,alpha)
    assert (va,ea,vb,eb)==(Fraction(1),Fraction(7,2),Fraction(2),Fraction(3))

print("VERIFY_OK")
print("confidence_levels_checked", [str(x) for x in levels])
print("finite_order_checks", checks)
print("95pct_threshold", 40, "VaR_ES_A", var_es([0]*37+[1,3,4],Fraction(19,20)),
      "VaR_ES_B", var_es([0]*37+[2,2,4],Fraction(19,20)))
print("97.5pct_threshold", 80, "VaR_ES_A", var_es([0]*77+[1,3,4],Fraction(39,40)),
      "VaR_ES_B", var_es([0]*77+[2,2,4],Fraction(39,40)))
