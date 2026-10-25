#!/usr/bin/env python3
"""Independent finite checks for the sharp run-refined 010 subsequence theorem.

Run: python3 verify.py
The theorem is proved symbolically in RESULT.md; finite checking is diagnostic.
"""
from itertools import combinations


def count_010(word):
    zeros = pairs01 = count = 0
    for symbol in word:
        if symbol == '0':
            count += pairs01
            zeros += 1
        else:
            pairs01 += zeros
    return count


def run_count(word):
    return 1 + sum(word[i] != word[i-1] for i in range(1, len(word)))


def deficit(a, t):
    if t == 0:
        return 0
    s = t // 2
    if t % 2:
        return s * (s+1) * (2*s+1) // 3
    if a % 2 == 0:
        return s * (2*s*s+1) // 3
    return 2*s * (s*s-1) // 3


def number_of_cut_choices(a, t, extra):
    assert t >= 1 and 0 <= extra and t <= a-1
    if a % 2 == 0:
        return 1 if t % 2 else 2
    if t == 1:
        return 2
    return (1 if t % 2 == 0 else 2) * (extra+1)


def formula(a, b, runs):
    assert a >= 1 and b >= 1 and runs >= 2
    peak = a*a//4
    if runs % 2 == 0:
        r = runs//2
        if a < r or b < r:
            return None
        if r == 1:
            return (0, 2)
        t = r-1
        return ((b-1)*peak - deficit(a,t),
                2*number_of_cut_choices(a,t,b-r))
    r = runs//2
    if a >= r+1 and b >= r:
        return (b*peak-deficit(a,r),
                number_of_cut_choices(a,r,b-r))
    if a == r and b >= r+1:
        if r == 1:
            return (0, b-1)
        t = r-1
        return ((b-2)*peak-deficit(a,t),
                number_of_cut_choices(a,t,b-r-1))
    return None


def slow_peak(a, t):
    if t == 0:
        return 0
    best = -1
    for js in combinations(range(1,a),t):
        value = sum(j*(a-j) for j in js)
        if value > best:
            best = value
    return t*(a*a//4)-best


def full_check(max_length=18):
    all_cases = 0
    for n in range(2,max_length+1):
        best, multiplicity = {}, {}
        for a in range(1,n):
            b=n-a
            for locations in combinations(range(n),a):
                chars=['1']*n
                for p in locations:
                    chars[p]='0'
                word=''.join(chars)
                key=(a,b,run_count(word))
                score=count_010(word)
                if key not in best or score>best[key]:
                    best[key]=score
                    multiplicity[key]=1
                elif score==best[key]:
                    multiplicity[key]+=1
        for key in best:
            expected=formula(*key)
            assert expected == (best[key],multiplicity[key]), (
                key,expected,best[key],multiplicity[key])
            all_cases+=1
    return all_cases


def independent_deficit_check(max_a=22):
    cases=0
    for a in range(2,max_a+1):
        for t in range(1,min(a,8)):
            assert deficit(a,t)==slow_peak(a,t),(a,t)
            cases+=1
    return cases


if __name__=='__main__':
    a=independent_deficit_check()
    b=full_check()
    print('CENTER_DEFICIT_CHECKS',a)
    print('FULL_COMPOSITION_RUN_AND_EXTREMIZER_CASES',b)
    print('VERIFY_OK')
