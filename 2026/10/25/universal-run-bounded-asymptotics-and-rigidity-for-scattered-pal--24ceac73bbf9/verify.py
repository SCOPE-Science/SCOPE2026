"""Independent finite checks for run-bounded scattered-palindrome formulas.

No third-party dependencies. Run: python3 verify.py
"""
from itertools import product
from math import prod


def runs(word):
    if not word:
        return []
    out = [[word[0], 1]]
    for letter in word[1:]:
        if letter == out[-1][0]:
            out[-1][1] += 1
        else:
            out.append([letter, 1])
    return out


def all_distinct_palindromic_subsequences(word):
    # Enumerate distinct subsequence STRINGS rather than embeddings.
    subs = {""}
    for symbol in word:
        subs |= {prefix + symbol for prefix in subs}
    return {s for s in subs if s and s == s[::-1]}


def leading_full_run_count(word, k):
    r = runs(word)
    if len(r) != 2*k + 1:
        return 0
    if [a for a, _ in r] != [a for a, _ in r[::-1]]:
        return 0
    return r[k][1] * prod(min(r[i][1], r[2*k-i][1]) for i in range(k))


def target_run_count(p):
    return len(runs(p))


def five_run_formula(a,b,c,d,e):
    n = a+b+c+d+e
    A = min(a,c+e); B = min(a+c,e); C = min(a,e)
    h = min(b,d)
    triple0 = C*(b+d) + (A-C)*b + (B-C)*d - (min(A,B)-C)*h
    triple1 = h*c
    quintuple0 = C*h*c
    return n + triple0 + triple1 + quintuple0


def run_tests():
    checked = 0
    for alphabet, max_n in [("01", 13), ("012", 9)]:
        Q = len(alphabet)
        for n in range(1, max_n+1):
            for word_tuple in product(alphabet, repeat=n):
                word = "".join(word_tuple)
                r = runs(word)
                if len(r) > 7:
                    continue
                pal = all_distinct_palindromic_subsequences(word)
                for k in (1,2,3):
                    if len(r) > 2*k + 1:
                        continue
                    leading = leading_full_run_count(word,k)
                    actual_full = sum(target_run_count(p)==2*k+1 for p in pal)
                    assert leading == actual_full, (Q,word,k,leading,actual_full)
                    rest = len(pal)-leading
                    upper = sum(Q*(Q-1)**j*n**(j+1) for j in range(k))
                    assert 0 <= rest <= upper, (Q,word,k,rest,upper)
                    coarse_global = n**(k+1)/(2**k*(k+1)**(k+1)) + upper
                    assert len(pal) <= coarse_global+1e-8, (Q,word,k)
                    checked += 1
                if Q==2 and len(r)==5 and r[0][0]=='0':
                    assert len(pal)==five_run_formula(*[b for a,b in r]), (word,len(pal),r)
    # Check the exact three-run extremal for lengths at which the bound is attained.
    for n in range(4,36):
        best = 0
        for a in range(1,n-1):
            for b in range(1,n-a):
                c=n-a-b
                best=max(best,n+min(a,c)*b)
        assert best==n+(n*n)//8, (n,best)
    print('VERIFY_OK', checked, 'run-cap/leading-count checks; exact 5-run and 3-run spot checks')


if __name__ == '__main__':
    run_tests()
