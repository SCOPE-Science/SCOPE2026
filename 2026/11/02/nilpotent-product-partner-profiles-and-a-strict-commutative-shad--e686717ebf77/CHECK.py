#!/usr/bin/env python3
"""Independent finite arithmetic tests for nilpotent-product partner profiles."""
from fractions import Fraction
from itertools import product
from collections import Counter


def full_matrix_2(q):
    E = list(product(range(q),repeat=4))
    def mul(x,y):
        a,b,c,d=x; e,f,g,h=y
        return ((a*e+b*g)%q,(a*f+b*h)%q,(c*e+d*g)%q,(c*f+d*h)%q)
    return E,mul,(0,0,0,0)


def upper_triangular_2(q,constant_diagonal=False):
    if constant_diagonal:
        E = list(product(range(q),repeat=2))
        def mul(x,y):
            a,b=x; c,d=y
            return ((a*c)%q,(a*d+b*c)%q)
        return E,mul,(0,0)
    E = list(product(range(q),repeat=3))
    def mul(x,y):
        a,b,c=x; d,e,f=y
        return ((a*d)%q,(a*e+b*f)%q,(c*f)%q)
    return E,mul,(0,0,0)


def field_four():
    E=list(range(4))
    def mul(a,b):
        x=0
        for i in range(2):
            if (b>>i)&1: x ^= a<<i
        if x&8: x ^= 0b1110 # x^3 = x(x+1)
        if x&4: x ^= 0b111 # x^2 = x+1
        return x
    return E,mul,0


def dual_numbers_four():
    F, mul4, z = field_four()
    E = list(product(F,repeat=2))
    def mul(x,y):
        a,b=x; c,d=y
        return (mul4(a,c),mul4(a,d)^mul4(b,c))
    return E,mul,(0,0)


def count_nilpotent_products(E,mul,z):
    nil=[]
    for x in E:
        cur=x
        for exponent in range(1,len(E)+1):
            if cur==z:
                nil.append(x); break
            cur=mul(cur,x)
    nil=set(nil)
    assert z in nil
    partners={x:sum(mul(x,y) in nil for y in E) for x in E}
    return Counter(Fraction(c,len(E)) for c in partners.values()),len(E),partners


def rank2(x,q):
    a,b,c,d=x
    if (a*d-b*c)%q: return 2
    if any(t%q for t in x): return 1
    return 0


def check_case(name,algebra, expected, predicted):
    E,mul,z=algebra
    freq,N,partners=count_nilpotent_products(E,mul,z)
    assert freq==Counter(expected),(name,freq,expected)
    assert all(Fraction(partners[x],N)==predicted(x) for x in E), name
    first=sum((val*count for val,count in freq.items()),Fraction(0))/N
    second=sum((val*val*count for val,count in freq.items()),Fraction(0))/N
    print(f'{name}: ring_order={N}; profile='+','.join(f'{p}:{freq[p]}' for p in sorted(freq,reverse=True))+
          f'; Pnil={first}; second_moment={second}; variance={second-first*first}')
    return first,second


def nilpotent_rank_counts(q,n):
    from math import prod
    return {r:prod((q**n-q**j)**2 for j in range(r))//prod((q**r-q**j) for j in range(r)) for r in range(n+1)}


def stoploss(freq,N,t):
    return sum((max(Fraction(0),p-t)*m for p,m in freq.items()),Fraction(0))/N


def main():
    fm2=full_matrix_2(2)
    fm3=full_matrix_2(3)
    for q,E in ((2,fm2),(3,fm3)):
        n=2
        counts=nilpotent_rank_counts(q,n)
        assert sum(counts.values())==q**(n*n)
        m,second=check_case(f'M2(F{q})',E,
            {Fraction(1,q**r):counts[r] for r in range(n+1)},
            lambda x,q=q:Fraction(1,q**rank2(x,q)))
        a=Fraction(1,q**n)
        assert m==2*a-a*a
        field_second=a+(1-a)*a*a
        assert second<field_second
        print(f'  commutative_shadow=F{q**n}; shadow_second={field_second}; strict_variance_gap={field_second-second}')
    check_case('F4',field_four(),{Fraction(1):1,Fraction(1,4):3},
               lambda x:Fraction(1 if x==0 else 1, 1 if x==0 else 4))
    check_case('F4[epsilon]/epsilon2',dual_numbers_four(),
               {Fraction(1):4,Fraction(1,4):12},
               lambda x:Fraction(1,4**int(x[0]!=0)))
    check_case('T2(F2)',upper_triangular_2(2),
               {Fraction(1):2,Fraction(1,2):4,Fraction(1,4):2},
               lambda x:Fraction(1,2**(int(x[0]!=0)+int(x[2]!=0))))
    check_case('dual_numbers(F2)',upper_triangular_2(2,True),
               {Fraction(1):2,Fraction(1,2):2},
               lambda x:Fraction(1,2**int(x[0]!=0)))
    # Test a noncommutative nonsemisimple ring with semisimple quotient F2 x F2.
    # Its profile equals that of the commutative quotient exactly.
    # Explicit stop-loss inequalities at all breakpoints for the simple M2(F2) block.
    matrix_freq, N, _ = count_nilpotent_products(*fm2)
    field_freq, Nfield, _ = count_nilpotent_products(*field_four())
    means=lambda freq,N:sum((p*m for p,m in freq.items()),Fraction(0))/N
    assert means(matrix_freq,N)==means(field_freq,Nfield)
    for t in sorted(set(matrix_freq)|set(field_freq)|{Fraction(0),Fraction(1)}):
        assert stoploss(matrix_freq,N,t)<=stoploss(field_freq,Nfield,t)
    assert stoploss(matrix_freq,N,Fraction(1,3))<stoploss(field_freq,Nfield,Fraction(1,3))
    print('convex_order_check=M2(F2) <=cx F4; strict at threshold 1/3')
    print('VERIFY_OK')


if __name__=='__main__':
    main()
