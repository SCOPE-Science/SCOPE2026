"""Self-contained exact-arithmetic verification of bipartite majority reversal identities."""
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb


def hyper_tail(r, s, a, b):
    t = a + b - 1
    return Fraction(sum(comb(r, k) * comb(s, t-k) for k in range(t+1) if k <= r and t-k <= s), comb(r+s, t)) if a==0 else Fraction(sum(comb(r, k) * comb(s, t-k) for k in range(a, t+1) if k <= r and t-k <= s), comb(r+s, t))


def first_flip_red_probability(m,n,x,y):
    assert m%2==1 and n%2==1
    if x>m//2 and y>n//2:return Fraction(1)
    if x<=m//2 and y<=n//2:return Fraction(0)
    if x>m//2:
        r=x;s=n-y;a=x-m//2;b=n//2+1-y
        return 1-hyper_tail(r,s,a,b)
    r=m-x;s=y;a=m//2+1-x;b=y-n//2
    return hyper_tail(r,s,a,b)


def recursive_probability(m,n,x,y):
    @lru_cache(None)
    def f(i,j):
        if i>m//2 and j>n//2:return Fraction(1)
        if i<=m//2 and j<=n//2:return Fraction(0)
        if j>n//2: lr=m-i; ni=i+1
        else: lr=i; ni=i-1
        if i>m//2: rr=n-j; nj=j+1
        else: rr=j; nj=j-1
        return Fraction(lr,lr+rr)*f(ni,j)+Fraction(rr,lr+rr)*f(i,nj)
    return f(x,y)


def inversion(m,n):
    total=Fraction(0)
    for x in range(m+1):
        for y in range(n+1):
            if 2*(x+y)==m+n:continue
            p=first_flip_red_probability(m,n,x,y)
            if 2*(x+y)>m+n:p=1-p
            total+=comb(m,x)*comb(n,y)*p
    return total/Fraction(2**(m+n))


def brute_prob(m,n):
    v=Fraction(0)
    for bits in product((0,1), repeat=m+n):
        x=sum(bits[:m]);y=sum(bits[m:]);z=x+y
        if 2*z==m+n: continue
        pr=recursive_probability(m,n,x,y)
        v+=1-pr if 2*z>m+n else pr
    return v/Fraction(2**(m+n))


def main():
    checks=0
    for m in (3,5,7,9):
        for n in (3,5,7,9):
            for x in range(m+1):
                for y in range(n+1):
                    p=first_flip_red_probability(m,n,x,y)
                    q=recursive_probability(m,n,x,y)
                    assert p==q, (m,n,x,y,p,q)
                    checks+=1
    examples={(3,3):Fraction(9,160),(3,5):Fraction(131,1792),(3,9):Fraction(233,2048)}
    for (m,n),want in examples.items():
        got=inversion(m,n)
        assert got==want,(m,n,got,want)
    for m,n in ((3,3),(3,5),(5,5)):
        assert inversion(m,n)==brute_prob(m,n)
    for m,n in ((3,3),(3,5),(3,9),(5,7),(7,21),(11,33)):
        print(f'K_{{{m},{n}}}: inversion={inversion(m,n)} approximately {float(inversion(m,n)):.10f}')
    print('PASS',checks,'conditional cases, 3 exhaustive binary-profile tests, 3 rational sample checks')

if __name__ == '__main__':main()
