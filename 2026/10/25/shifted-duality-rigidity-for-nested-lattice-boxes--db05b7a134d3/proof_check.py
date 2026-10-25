"""Exact finite checks for the stated relative Ehrhart box rigidity theorem.
The proof in RESULT.md covers all dimensions; these tests do not replace it.
"""
from fractions import Fraction
from itertools import product
from collections import Counter

def roots(a,b,sigma,interior=False):
    if not interior:
        return Counter(Fraction(y-1,x) for x,y in zip(a,b))
    return Counter(Fraction(y+1,x)-sigma for x,y in zip(a,b))

def formula(a,b,t,strict=False):
    ans=1
    for x,y in zip(a,b):
        factor=x*t-y+(-1 if strict else 1)
        if factor<0:
            raise ValueError('formula outside eventual range')
        ans*=factor
    return ans

def direct_count(a,b,t,strict=False):
    # Independently count integer translation vectors in the permitted box.
    ranges=[range(-1,x*t+2) for x in a]
    total=0
    for v in product(*ranges):
        if all((0<y and y+w<x*t) if strict else (0<=y and y+w<=x*t)
               for x,w,y in zip(a,b,v)):
            total+=1
    return total

def test():
    configurations=0
    identities=0
    raw_counts=0
    for d in range(1,5):
        for a in product(range(1,5), repeat=d):
            for b in product(*(range(x+1) for x in a)):
                configurations+=1
                s0=roots(a,b,0)
                classification=len(set(a))==1 and a[0] in (1,2)
                for sigma in (1,2,3):
                    actual=s0==roots(a,b,sigma,True)
                    expected=classification and sigma==2//a[0]
                    assert actual==expected,(a,b,sigma,actual,expected)
                    identities+=1
                if d<=3 and max(a)<=3:
                    t=3
                    for strict in (False,True):
                        assert direct_count(a,b,t,strict)==formula(a,b,t,strict)
                        raw_counts+=1
    a=(1,3,6);b=(1,4,5)
    assert roots(a,b,0)==roots(a,b,1,True)
    assert b[1]>a[1]
    assert formula(a,b,7)==formula(a,b,8,True)
    assert roots((1,2),(0,2),0)!=roots((1,2),(0,2),1,True)
    print(f'BOX_SHIFT_RIGIDITY_OK configurations={configurations} exact_identities={identities} independently_counted={raw_counts} nonnested_witness=PASS')

if __name__=='__main__':
    test()
