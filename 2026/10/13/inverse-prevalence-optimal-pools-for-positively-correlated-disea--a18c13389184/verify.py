"""Exact identities and sample-size checks for correlated two-stage testing.
Run with Python 3 standard library: python verify.py.
Finite checks complement, but do not replace, the analytical proof.
"""
from fractions import Fraction
from math import log, sqrt


def negative_prob(a, t, k):
    q = Fraction(1)
    for j in range(k):
        q *= (t-a+j)/(t+j)
    return q


def cost(a, t, k):
    return Fraction(1, k) + 1 - negative_prob(a, t, k)


def scaled_difference(a, t, k):
    return a*k*(k+1)*negative_prob(a,t,k)/(t+k)


def check():
    exact = 0
    tests = [
        (Fraction(1,20), Fraction(1)),
        (Fraction(1,10), Fraction(2)),
        (Fraction(3,10), Fraction(3,2)),
        (Fraction(1,4), Fraction(5,2)),
        (Fraction(2,3), Fraction(4)),
        (Fraction(9,10), Fraction(3,2)),
    ]
    for a,t in tests:
        assert 0 < a < min(t,1)
        for k in range(2,30):
            q = negative_prob(a,t,k)
            actual = cost(a,t,k+1)-cost(a,t,k)
            assert actual == (scaled_difference(a,t,k)-1)/(k*(k+1))
            assert scaled_difference(a,t,k+1)/scaled_difference(a,t,k) == Fraction((k+2)*(t-a+k),k*(t+k+1))
            assert scaled_difference(a,t,k+1)>scaled_difference(a,t,k)
            assert q==negative_prob(a,t,k)
            exact += 1
    # Fixed-concentration rare-prevalence optima, certified by exact
    # rational adjacent-cost signs, using only a single product pass.
    examples=[]
    for p in [Fraction(1,20), Fraction(1,100), Fraction(1,1000)]:
        t=Fraction(1); a=p
        q=Fraction(1)
        k=0
        previous_R=Fraction(0)
        while True:
            q *= (t-a+k)/(t+k)
            k+=1
            if k < 2: continue
            R=a*k*(k+1)*q/(t+k)
            if R>=1:
                assert previous_R<1 or k==2
                break
            previous_R=R
            assert k<3000
        assert k>2
        examples.append((round(float(p),6),k,round(float(a*k),6),round(float(Fraction(1,k)+1-q),9)))
    # In the IID case, the square-root scaling follows the exact cost formula.
    iid=[]
    for p in [Fraction(1,100),Fraction(1,10000)]:
        vals = [(Fraction(1,k)+1-(1-p)**k,k) for k in range(2,1000)]
        best,k=min(vals)
        iid.append((str(p),k,round(float(k)*sqrt(float(p)),6)))
    print('VERIFY_OK exact_adjacent_and_ratio_cases=%d correlated_examples=%s iid_examples=%s'%(exact,examples,iid))

if __name__=='__main__':
    check()
