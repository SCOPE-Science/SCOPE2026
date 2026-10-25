"""Independent finite checks for minimal unique contiguous factors of binary five-run words.

Run with Python 3: python verify.py
No external dependencies.
"""
from collections import Counter
from itertools import product
from math import comb


def word(runs):
    return ''.join(str(i & 1) * runs[i] for i in range(5))


def independent_mus(s):
    """Literal factor-frequency enumeration; does not use the stated classification."""
    frequencies = Counter(s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1))
    return {t for t, occurrences in frequencies.items()
            if occurrences == 1
            and frequencies[t[1:]] >= 2
            and frequencies[t[:-1]] >= 2}


def predicted(runs):
    a,b,c,d,e = runs
    k = min(b,d)
    out = {
        '0'*max(a,c,e),
        '1'*max(b,d),
        '0'*(min(a,c)+1)+'1',
        '0'+'1'*(k+1),
        '1'*(k+1)+'0',
        '1'+'0'*(min(c,e)+1),
        '0'+'1'*k+'0',
    }
    if c<min(a,e):out.add('1'+'0'*c+'1')
    return out


def separated(runs):
    a,b,c,d,e=runs
    return min(abs(a-c),abs(a-e),abs(c-e),abs(b-d))>=2


def check():
    full=0
    for runs in product(range(1,8),repeat=5):
        if not separated(runs):continue
        a=independent_mus(word(runs))
        b=predicted(runs)
        assert a == b, (runs,a,b)
        assert len(a)==7+(runs[2]<min(runs[0],runs[4]))
        full+=1
    # Exact histogram over all compositions; no use of the classification.
    totals=[]
    for n in (15,20,25):
        hist=Counter()
        for a in range(1,n-3):
            for b in range(1,n-a-2):
                for c in range(1,n-a-b-1):
                    for d in range(1,n-a-b-c):
                        e=n-a-b-c-d
                        hist[len(independent_mus(word((a,b,c,d,e))))]+=1
        assert sum(hist.values())==comb(n-1,4)
        totals.append((n,sorted(hist.items())))
    # Independently count separated compositions by direct nested loops and
    # compare to coefficients of 12*z^13/((1-z^3)(1-z^2)^2(1-z)^2).
    # Each weight assignment in the generating denominator is enumerated separately.
    for n in range(13,33):
        seven = eight = 0
        for a in range(1,n-3):
            for b in range(1,n-a-2):
                for c in range(1,n-a-b-1):
                    for d in range(1,n-a-b-c):
                        e=n-a-b-c-d
                        runs=(a,b,c,d,e)
                        if separated(runs):
                            if c<min(a,e): eight+=1
                            else:seven+=1
        # denominator choices 1/(1-z^3), 1/(1-z^2)^2, 1/(1-z)^2
        den = 0
        target=n-13
        for j in range(target//3+1):
            for k in range((target-3*j)//2+1):
                remainder=target-3*j-2*k
                den+=(k+1)*(remainder+1)
        assert (seven,eight)==(8*den,4*den), (n,seven,eight,den)
    print('VERIFY_OK independent_complete_sets=',full,
          'unrestricted_composition_histograms=',totals)

if __name__ == '__main__':check()
