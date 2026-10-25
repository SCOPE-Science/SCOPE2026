"""Standalone integer verification of sparse-word palindromic subsequence theorem.

This checks examples and finite parameter ranges; the all-parameter proof is mathematical.
No third-party dependencies are needed.
"""
from itertools import combinations


def gap_word(a,b,c,d):
    return '0'*a+'1'+'0'*b+'1'+'0'*c+'1'+'0'*d


def formula(a,b,c,d):
    assert min(a,b,c,d) >= 0
    m = a+b+c+d
    h = max(min(a,b+c+d), min(a+b,c+d), min(a+b+c,d))
    x = min(a,d)
    two = (x+1)*(b+c+1)
    if a <= d:
        two += min(b,d-a)*(c+1)
    else:
        two += min(c,a-d)*(b+1)
    three = (x+1)*(min(b,c)+1)
    return m+2+h+two+three


def is_subseq(pat, word):
    it = iter(word)
    return all(any(ch == p for ch in it) for p in pat)


def by_palindrome_generation(word):
    m = word.count('0')
    palindromes = {''}
    for i in range(m+1):
        palindromes.add('0'*i)
        pat='0'*i+'1'+'0'*i
        if is_subseq(pat,word):palindromes.add(pat)
        for j in range(m+1):
            pat='0'*i+'1'+'0'*j+'1'+'0'*i
            if is_subseq(pat,word):palindromes.add(pat)
            pat='0'*i+'1'+'0'*j+'1'+'0'*j+'1'+'0'*i
            if is_subseq(pat,word):palindromes.add(pat)
    return len(palindromes)


def dynamic_program(word):
    n=len(word)
    dp=[[0]*n for _ in range(n)]
    for i in range(n):dp[i][i]=1
    for span in range(2,n+1):
        for i in range(n-span+1):
            j=i+span-1
            middle=dp[i+1][j-1] if span>2 else 0
            if word[i]!=word[j]:
                dp[i][j]=dp[i+1][j]+dp[i][j-1]-middle
            else:
                lo=i+1; hi=j-1
                while lo<j and word[lo]!=word[i]:lo+=1
                while hi>i and word[hi]!=word[i]:hi-=1
                if lo>hi:dp[i][j]=2*middle+2
                elif lo==hi:dp[i][j]=2*middle+1
                else:dp[i][j]=2*middle-(dp[lo+1][hi-1] if lo+1<=hi-1 else 0)
    return dp[0][n-1]+1 if n else 1


def compositions4(total):
    for a in range(total+1):
        for b in range(total-a+1):
            for c in range(total-a-b+1):
                yield a,b,c,total-a-b-c


def pal_source_max(s):
    a=s//2; b=s-a
    return 3*a*b+5*a+6*b+4


def run_tests():
    brute = dp = palindrome_tests=0
    for m in range(0,13):
        for gaps in compositions4(m):
            word=gap_word(*gaps)
            target=formula(*gaps)
            assert by_palindrome_generation(word)==target,(gaps,'generation')
            brute+=1
    for m in range(0,19):
        for gaps in compositions4(m):
            target=formula(*gaps)
            assert dynamic_program(gap_word(*gaps))==target,(gaps,'dynamic')
            dp+=1
    for s in range(0,101):
        scores=[formula(a,b,b,a) for a in range(s+1) for b in [s-a]]
        assert max(scores)==pal_source_max(s)
        assert scores.index(max(scores))==s//2
        palindrome_tests+=1
    print('VERIFIED palindromic-pattern enumeration',brute,'gap quadruples, total zeros <=12')
    print('VERIFIED independent interval DP',dp,'gap quadruples, total zeros <=18')
    print('VERIFIED symmetric-family optimality',palindrome_tests,'zero-half sums, 0..100')

if __name__ == '__main__':
    run_tests()
