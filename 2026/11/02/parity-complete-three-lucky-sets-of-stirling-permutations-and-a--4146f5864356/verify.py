"""Reproduce explicit Stirling-permutation lucky-position constructions.

Usage: python3 verify.py
No external packages are required.
"""
from math import comb


def double_labels(labels):
    return [x for y in labels for x in (y, y)]


def lucky_positions(w):
    occupied = set()
    lucky = []
    for i, x in enumerate(w, 1):
        p = x
        while p in occupied:
            p += 1
        if p == x:
            lucky.append(i)
        occupied.add(p)
    return tuple(lucky)


def validate_stirling(w):
    n = len(w) // 2
    assert len(w) == 2*n and sorted(w) == [x for i in range(1, n+1) for x in (i, i)]
    for x in range(1, n+1):
        a = w.index(x)
        b = len(w)-1-w[::-1].index(x)
        assert all(y > x for y in w[a+1:b]), (w, x)
    return True


def two_lucky_odd(m, i):
    t = (i-1)//2
    return double_labels(range(2,t+2)) + [1,1] + double_labels(range(t+2,m+1))


def two_lucky_even(m, i):
    a=i//2
    return (double_labels(range(1,a)) + [a,2*a,2*a] +
            double_labels(range(a+1,2*a)) +
            double_labels(range(2*a+1,m+1)) + [a])


def witness(n, i, j):
    assert n >= 3 and 2 <= i < j <= 2*n-1
    if i%2 and j%2:
        m=(j+1)//2
        base=two_lucky_odd(m-1,i)
        word=[v+1 for v in base]+[1,1]
    elif i%2 and not j%2:
        m=j//2+1
        t=(i-1)//2
        word=(double_labels(range(3,t+3)) + [1] +
              double_labels(range(t+3,m+1)) + [2,2,1])
    elif not i%2 and j%2:
        assert i < n
        a=i//2
        m=max(i+1,(j+1)//2)
        if m>i+1:
            base=two_lucky_even(m-1,i)
            word=[v+1 for v in base]+[1,1]
        elif j==i+1:
            word=(double_labels(range(1,a)) + [a,2*a,2*a+1,2*a+1,2*a,a]
                  +double_labels(range(a+1,2*a)))
        else:
            base=(double_labels(range(2,a+1)) + [a+1,2*a+1,2*a+1,a+1]
                  +double_labels(range(a+2,2*a+1)))
            gap=j-1
            assert gap>=i+2 and gap<=len(base) and (gap-i-2)%2==0
            word=base[:gap]+[1]+base[gap:]+[1]
    else:
        assert i%2==0 and j%2==0 and i+j<=2*n
        a,b=i//2,j//2
        m=a+b
        word=(double_labels(range(1,a)) + [a] +
              double_labels(range(2*a+1,m+1)) + [2*a,2*a,a] +
              double_labels(range(a+1,2*a)))
    word+=double_labels(range(len(word)//2+1,n+1))
    validate_stirling(word)
    actual=lucky_positions(word)
    assert actual==(1,i,j), (n,i,j,word,actual)
    return word


def eligible(n,i,j):
    if i%2 or j%2:
        return i%2==1 or i<n
    return i+j<=2*n  # sufficient only in the both-even sector


def exhaustive_lucky_sets(n):
    # Independent generator: recursively insert the next maximum adjacent pair.
    from itertools import combinations
    w=[1,1]
    seen=set()
    def rec(k):
        if k>n:
            luck=lucky_positions(w)
            if len(luck)==3:
                seen.add(luck)
            return
        for pos in range(len(w)+1):
            w[pos:pos]=[k,k]
            rec(k+1)
            del w[pos:pos+2]
    rec(2)
    return seen


def main():
    tested=0
    for n in range(3,61):
        for i in range(2,2*n):
            for j in range(i+1,2*n):
                if eligible(n,i,j):
                    witness(n,i,j)
                    tested+=1
    print('CONSTRUCTIVE_CHECK_OK',tested,'triples for orders 3..60')
    for n in range(3,9):
        obs=exhaustive_lucky_sets(n)
        sector={(1,i,j) for i in range(2,2*n) for j in range(i+1,2*n)
                if i%2 or j%2 if (i%2 or i<n)}
        observed_sector={s for s in obs if s[1]%2 or s[2]%2}
        assert observed_sector == sector,(n,len(sector),len(observed_sector),sector^observed_sector)
        suff={(1,i,j) for i in range(2,2*n) for j in range(i+1,2*n)
              if eligible(n,i,j)}
        assert suff <= obs
        h=(n-1)//2
        expected=(n-1)*(n-2)+h*n-h*(h+1)//2
        assert expected==len(sector)
        print('EXHAUSTIVE_OK',n,'three-lucky',len(obs),'parity-sector',len(sector),
              'both-even',len(obs-sector))
    print('VERIFY_OK')

if __name__=='__main__':
    main()
