#!/usr/bin/env python3
"""Standalone exact checks for random error-ball volumes in the radius-one
limited permutation channel. Requires Python 3.9+ standard library only.
"""
from fractions import Fraction
from itertools import product
from math import isclose, log, sqrt


def swap_masks(n):
    def gen(i, chosen):
        if i >= n - 1:
            yield tuple(chosen)
            return
        yield from gen(i + 1, chosen)
        chosen.append(i)
        yield from gen(i + 2, chosen)
        chosen.pop()
    return tuple(gen(0, []))


def brute_volume(word, masks):
    outputs = set()
    for indices in masks:
        arr = list(word)
        for i in indices:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        outputs.add(tuple(arr))
    return len(outputs)


def dp_volume(word):
    # Count matchings of positions with unequal adjacent symbols.
    a, b = 1, 0
    for i in range(len(word) - 1):
        a, b = a + b, a if word[i] != word[i + 1] else 0
    return a + b


def recurrence_moments(n, p):
    # Here the indexing is by the number of boundaries m = n - 1.
    f = [Fraction(1), 1+p]
    g = [Fraction(1), 1+3*p, 1+6*p+2*p*p]
    while len(f) < n:
        f.append(f[-1] + p*f[-2])
    while len(g) < n:
        g.append((1+p)*g[-1] + 2*p*g[-2] - p*p*g[-3])
    return f[n-1],g[n-1]


def independent_flags(n, q):
    p = Fraction(q-1, q)
    a = b = Fraction(0)
    # Uniform words induce iid inequality flags; each flag sequence
    # e has probability p^{sum e}(1-p)^{n-1-sum e}.
    for bits in product((0,1), repeat=n-1):
        zeros, ones = 1, 0
        for bit in bits:
            zeros, ones = zeros+ones, zeros if bit else 0
        v = zeros+ones
        weight = p**sum(bits)*(1-p)**(len(bits)-sum(bits))
        a += weight*v
        b += weight*v*v
    return a,b


def exact_checks():
    trials=0
    for q,max_n in ((2,11),(3,8),(4,7)):
        for n in range(1,max_n+1):
            masks=swap_masks(n)
            x1=x2=0
            for word in product(range(q),repeat=n):
                v=brute_volume(word,masks)
                assert v==dp_volume(word), (q,n,word,v,dp_volume(word))
                x1+=v
                x2+=v*v
                trials+=1
            brute=(Fraction(x1,q**n),Fraction(x2,q**n))
            by_rec=recurrence_moments(n,Fraction(q-1,q))
            by_flags=independent_flags(n,q)
            assert brute==by_rec==by_flags, (q,n,brute,by_rec,by_flags)
            if n==max_n:
                print('q=%s n=1..%s: direct balls = flag enumeration = rational-moment recurrence; final mean=%s second=%s' %(q,max_n,brute[0],brute[1]))
    print('EXACT_WORD_CASES=%d' % trials)


def moment_transfer_check():
    for q in (2,3,4,7,100):
        p=Fraction(q-1,q)
        # Matrix reduction with symmetric state pairs:
        # [00, 10=01, 11]. All vectors start at [1,1,1].
        a=b=c=Fraction(1)
        for n in range(1,80):
            _mean,_second=recurrence_moments(n,p)
            assert a==_second,(q,n)
            a,b,c=a+2*p*b+p*c,a+p*b,a
    print('TRANSFER_RECURRENCE_OK q=2,3,4,7,100 through n=79')


def variance_pressure_check():
    for q in (2,3,4,7,100):
        p=(q-1)/q
        alpha=(1+sqrt(1+4*p))/2
        def poly(x): return x**3-(1+p)*x*x-2*p*x+p*p
        lo=alpha*alpha
        hi=4.
        assert poly(lo)<0 and poly(hi)>0
        for _ in range(100):
            mid=(lo+hi)/2
            if poly(mid)>0:hi=mid
            else:lo=mid
        beta=(lo+hi)/2
        assert beta>alpha*alpha
        fib_a,fib_b=0,1
        gamma=0.
        vals=[]
        for k in range(5000 if q>=100 else 300):
            fib_a,fib_b=fib_b,fib_a+fib_b
            value=log(fib_b)  # After k+1 updates, fib_b = F_(k+2).
            prob=(1-p)**2*(p**k)
            gamma+=prob*value
            vals.append((k, value, prob))
        sigma=sum(prob*(value-gamma*(k+1))**2 for k,value,prob in vals)
        assert gamma>0 and sigma>0
        if q<=4:print('q=%d alpha=%.12f beta=%.12f ratio=%.12f gamma=%.12f sigma2=%.12f' % (q,alpha,beta,beta/(alpha*alpha),gamma,sigma))
    print('SPECTRAL_AND_RENEWAL_CONSTANTS_OK')

if __name__=='__main__':
    exact_checks()
    moment_transfer_check()
    variance_pressure_check()
    print('VERIFY_OK')
