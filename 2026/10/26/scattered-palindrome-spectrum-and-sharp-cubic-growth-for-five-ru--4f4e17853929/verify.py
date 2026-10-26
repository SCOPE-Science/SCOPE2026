#!/usr/bin/env python3
"""Independent finite checks for five-run scattered palindrome spectra.

Counts distinct subsequence strings by an ordinary set-recursion, completely
independent of the run-pattern argument used in the mathematical proof.
"""
from collections import Counter
from itertools import product, combinations


def spectrum_by_subsequence_sets(word):
    strings = {""}
    for symbol in word:
        strings |= {s + symbol for s in strings}
    return Counter(len(s) for s in strings if s and s == s[::-1])


def spectrum_by_formula(a, b, c, d, e):
    result = Counter()
    A = min(a, c + e)
    B = min(e, a + c)
    E = min(a, e)
    t = min(b, d)
    for i in range(1, a + c + e + 1):
        result[i] += 1
    for i in range(1, b + d + 1):
        result[i] += 1
    # 0-1-0, with a unique allocation of each pair of run lengths.
    for i in range(1, E + 1):
        for j in range(1, b + d + 1):
            result[2*i+j] += 1
    for i in range(E+1, A+1):
        for j in range(1, b+1):
            result[2*i+j] += 1
    for i in range(E+1, B+1):
        for j in range(1, d+1):
            result[2*i+j] += 1
    # 1-0-1.
    for i in range(1, t+1):
        for j in range(1, c+1):
            result[2*i+j] += 1
    # 0-1-0-1-0.
    for i in range(1, E+1):
        for j in range(1, t+1):
            for k in range(1, c+1):
                result[2*i+2*j+k] += 1
    return result


def total_formula(a,b,c,d,e):
    n=a+b+c+d+e
    return n+b*min(a,c+e)+d*min(e,a+c)+(min(a,e)+1)*c*min(b,d)


def run_checks():
    tests = 0
    for params in product(range(1,5), repeat=5):
        a,b,c,d,e = params
        w='0'*a+'1'*b+'0'*c+'1'*d+'0'*e
        actual=spectrum_by_subsequence_sets(w)
        expected=spectrum_by_formula(*params)
        if actual != expected:
            raise AssertionError(('spectrum',params,actual,expected))
        if sum(actual.values()) != total_formula(*params):
            raise AssertionError(('total',params,actual,total_formula(*params)))
        tests+=1
    extrema=[]
    for n in range(5,31):
        maximum=-1
        all_max=[]
        symmetric_max=-1
        for i,j,k,l in combinations(range(1,n),4):
            params=(i,j-i,k-j,l-k,n-l)
            val=total_formula(*params)
            if val>maximum:
                maximum=val;all_max=[params]
            elif val==maximum:
                all_max.append(params)
            if params[0]==params[4] and params[1]==params[3]:
                symmetric_max=max(symmetric_max,val)
        if maximum!=symmetric_max:
            raise AssertionError(('symmetric_n',n,maximum,symmetric_max,all_max))
        extrema.append((n,maximum,len(all_max)))
    # An external check of the asymptotic coefficient at multiples of six.
    for k in (2,3,5,10,25,50,100):
        a=b=d=e=k;c=2*k;n=6*k
        val=total_formula(a,b,c,d,e)
        expected=n**3//108+n**2//9+n
        assert val==expected, (k,val,expected)
    print('VERIFY_OK 1024 complete independent subsequence spectra, exact integer maxima n=5..30, symmetric witnesses, scaled constructions')
    print('EXTREMA',extrema)

if __name__=='__main__':
    run_checks()
