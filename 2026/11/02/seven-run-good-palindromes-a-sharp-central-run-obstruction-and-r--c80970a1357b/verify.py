"""Finite independent checks of a classification of seven-run binary palindromes."""
from itertools import product


def word(a,b,c,d):
    return '0'*a + '1'*b + '0'*c + '1'*d + '0'*c + '1'*b + '0'*a


def antisquare_free_except_order_one(w):
    for k in range(2,len(w)//2+1):
        for i in range(len(w)-2*k+1):
            if all(w[i+j] != w[i+k+j] for j in range(k)):
                return False
    return True


def criterion(a,b,c,d):
    return ((a==c==1 and b>=3 and d!=2)
            or (b==d==1 and c>=3)
            or (b==c==1 and d>2*a))


def theory(n):
    total=0
    for a in range(1,n):
        for b in range(1,n):
            for c in range(1,n):
                d=n-2*a-2*b-2*c
                if d>=1 and criterion(a,b,c,d):total+=2
    return total


def directly(n):
    acc=0
    for h in product('01',repeat=(n+1)//2):
        left=''.join(h)
        w=left+left[:n//2][::-1]
        runs=1+sum(w[i]!=w[i-1] for i in range(1,len(w)))
        if runs==7 and antisquare_free_except_order_one(w):acc+=1
    return acc


def from_series(n):
    # Twice the sum of disjoint family contributions.
    a=sum(1 for b in range(3,n) for d in ([1]+list(range(3,n))) if 2*b+d+4==n)
    b=sum(1 for aa in range(1,n) for c in range(3,n) if 2*aa+2*c+3==n)
    c=sum(1 for aa in range(1,n) for d in range(2*aa+1,n) if 2*aa+d+4==n)
    return 2*(a+b+c)

cases=0
for a,b,c,d in product(range(1,10),repeat=4):
    cases+=1
    assert antisquare_free_except_order_one(word(a,b,c,d))==criterion(a,b,c,d), (a,b,c,d)
for n in range(1,27):
    assert directly(n)==theory(n)==from_series(n), (n,directly(n),theory(n),from_series(n))
for n in range(1,61):
    assert theory(n)==from_series(n),n
print('VERIFY_OK quadruples=%d full_palindrome_lengths=26 coefficient_lengths=60' % cases)
print('LENGTH_COUNTS',[(n,theory(n)) for n in range(9,22)])
