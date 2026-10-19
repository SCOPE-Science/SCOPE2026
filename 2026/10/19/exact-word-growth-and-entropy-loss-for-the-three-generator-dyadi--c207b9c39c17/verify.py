#!/usr/bin/env python3
"""Independent finite checks for the binary-token affine semigroup 0, 1, 01."""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, log, isclose, sqrt

TOKENS=('0','1','01')
WEIGHTS=(Fraction(2,9),Fraction(1,3),Fraction(4,9))

def occurrences(word):
    return sum(word[i:i+2]=='01' for i in range(len(word)-1))

def formula_counts(N):
    vals=[1]
    for n in range(1,N+1):
        val=sum(1 for length in range(n,2*n+1)
                for bits in product('01',repeat=length)
                if occurrences(''.join(bits))>=length-n)
        vals.append(val)
    return vals

def rational_series(N):
    # P(z)A(z)=(1-z)^2, P(z)=(1-2z)(1-3z+z^2)
    divisor=[1,-5,7,-2]
    numer=[1,-2,1]
    out=[]
    for n in range(N+1):
        out.append((numer[n] if n<len(numer) else 0)
                  -sum(divisor[k]*out[n-k]
                       for k in range(1,min(n,3)+1)))
    return out

def verify():
    checks=0
    seq=rational_series(9)
    assert seq==[1,3,9,26,73,201,546,1469,3925,10434]
    assert seq[:7]==formula_counts(6)
    checks+=7
    for n in range(0,10):
        word_weight=defaultdict(Fraction)
        class_counts=defaultdict(int)
        group_by_word=defaultdict(list)
        for choice in product(range(3),repeat=n):
            word=''.join(TOKENS[i] for i in choice)
            prob=Fraction(1)
            for i in choice:
                prob*=WEIGHTS[i]
            word_weight[word]+=prob
            class_counts[word]+=1
            group_by_word[word].append(choice)
        assert len(word_weight)==seq[n]
        assert sum(word_weight.values())==1
        checks+=2
        entropy_tokens=n*(-sum(float(w)*log(float(w)) for w in WEIGHTS))
        ambiguity_expect=0.0
        H_out=-sum(float(p)*log(float(p)) for p in word_weight.values())
        for word,p in word_weight.items():
            j=len(word)-n
            number=comb(occurrences(word),j)
            assert class_counts[word]==number,(n,word,number,class_counts[word])
            ambiguity_expect+=float(p)*log(number)
            checks+=1
            # if probabilities are equal across parses conditioned on output,
            # each n-token parsing is a choice of identical counts of tokens.
            p0=next((WEIGHTS[0]**choice.count(0)*WEIGHTS[1]**choice.count(1)*WEIGHTS[2]**choice.count(2)) for choice in group_by_word[word])
            assert all(WEIGHTS[0]**choice.count(0)*WEIGHTS[1]**choice.count(1)*WEIGHTS[2]**choice.count(2)==p0 for choice in group_by_word[word])
            checks+=1
        assert isclose(H_out,entropy_tokens-ambiguity_expect,abs_tol=1e-10)
        checks+=1
    # Cross-check conditional parsing entropy for two further rational laws.
    for weights in ((Fraction(1,3),Fraction(1,3),Fraction(1,3)),
                    (Fraction(1,2),Fraction(1,4),Fraction(1,4))):
        for n in range(0,7):
            masses=defaultdict(Fraction)
            for choice in product(range(3),repeat=n):
                p=Fraction(1)
                for i in choice:
                    p*=weights[i]
                masses[''.join(TOKENS[i] for i in choice)]+=p
            hout=-sum(float(p)*log(float(p)) for p in masses.values())
            htoken=-sum(float(p)*log(float(p)) for p in weights)
            missing=sum(float(p)*log(comb(occurrences(w),len(w)-n))
                        for w,p in masses.items())
            assert isclose(hout,n*htoken-missing,abs_tol=1e-11)
            checks+=1
    a,b,c=map(float,WEIGHTS)
    C=a*b+c
    hsource=-sum(x*log(x) for x in (a,b,c))
    p=c/C
    hloss=-C*(p*log(p)+(1-p)*log(1-p))
    hrw=hsource-hloss
    Hgap=-b*log(b)-C/(1-a)*log(C)-C*a/(1-a)**2*log(a)
    assert isclose(hrw,(1-a)*Hgap,abs_tol=1e-13)
    assert 0 < hrw < (1+c)*log(2)
    a=b=c=1/3
    C=a*b+c
    h=-3*a*log(a)-C*(-(c/C)*log(c/C)-(a*b/C)*log(a*b/C))
    assert isclose(h/((1+c)*log(2)),log(3)/log(2)-2/3,abs_tol=1e-13)
    # Published source-coding example: e^{-R}=sqrt(2)-1 and p(01)=e^{-2R}.
    a=b=sqrt(2)-1
    c=a*a
    C=a*b+c
    q=c/C
    hsource=-sum(t*log(t) for t in (a,b,c))
    hactual=hsource+C*(q*log(q)+(1-q)*log(1-q))
    assert isclose(hsource/(1+c),0.881373587019543,abs_tol=1e-12)
    assert isclose(hactual/(1+c),0.6783554781938712,abs_tol=1e-12)
    assert hactual/(1+c)<log(2)<hsource/(1+c)
    checks+=3
    print('VERIFY_OK: n=0..9 exhaustive output/map equality; polynomial coefficient check;')
    print('    exact parsing multiplicity and conditional equiprobability;')
    print('    finite-n entropy identity at three rational laws; renewal entropy identity;')
    print('    equal-weight dimension and published codeweight example;')
    print('    checks =',checks)

if __name__=='__main__':
    verify()
