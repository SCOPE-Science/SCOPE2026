"""Reproduce exact quotient-norm identities for symmetric quadratic Walsh data.
Runs with the Python standard library; every finite check uses rational arithmetic.
"""
from fractions import Fraction
from itertools import product,combinations
from math import comb

def analysis(n):
    assert n>=2
    z=[Fraction((n-2*k)**2-n,2) for k in range(n+1)]
    masses=[Fraction(comb(n,k),2**n) for k in range(n+1)]
    order=sorted(range(n+1),key=lambda k:z[k]);cum=Fraction(0)
    median=None
    for k in order:
        cum+=masses[k]
        if cum>=Fraction(1,2):
            median=z[k];break
    mad=sum((p*abs(v-median) for v,p in zip(z,masses)),Fraction(0))
    variance=Fraction(n*(n-1),2)
    value=variance/mad
    below=sum((p for v,p in zip(z,masses) if v<median),Fraction(0))
    above=sum((p for v,p in zip(z,masses) if v>median),Fraction(0))
    tied=sum((p for v,p in zip(z,masses) if v==median),Fraction(0))
    t=(below-above)/tied
    assert -1<=t<=1
    def h_at(v):
        return value*(1 if v>median else (-1 if v<median else t))
    assert sum((masses[k]*h_at(z[k]) for k in range(n+1)),Fraction(0))==0
    assert sum((masses[k]*h_at(z[k])*z[k] for k in range(n+1)),Fraction(0))==variance
    assert max(abs(h_at(v)) for v in z)==value
    assert sum((masses[k]*abs(z[k]-median) for k in range(n+1)),Fraction(0))==mad
    return value,median,mad,h_at

def brute(n):
    value,median,mad,h=analysis(n)
    signs=list(product([-1,1],repeat=n))
    for inds in [()] + [(i,) for i in range(n)] + list(combinations(range(n),2)):
        coef=sum((h(Fraction(sum(s)**2-n,2))* __import__('math').prod(s[i] for i in inds) for s in signs),Fraction(0))/len(signs)
        assert coef==(1 if len(inds)==2 else 0),(n,inds,coef)
    z=[Fraction(sum(s)**2-n,2) for s in signs]
    dual=sum((v*(v-median) for v in z),Fraction(0))/len(z)/mad
    assert dual==value
    return value,median

def main():
    for n in range(2,13):
        v,m=brute(n);print(n,str(v),str(m))
    for n in range(13,251): analysis(n)
    print('PASS exact fractions: full low-Walsh checks n=2..12; shell formulas n=2..250')
if __name__=='__main__':main()
