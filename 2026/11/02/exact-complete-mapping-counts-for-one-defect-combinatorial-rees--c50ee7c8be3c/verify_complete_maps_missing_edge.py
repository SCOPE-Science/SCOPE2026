"""Exact checks for complete mappings of nearly full Rees zero-matrix semigroups."""
from itertools import permutations
from math import factorial, comb
from fractions import Fraction


def claimed_count(m,n):
    numerator=factorial(n)**m*factorial(m)**n
    factor=sum(((-1)**t)*Fraction(comb(m,t)*factorial(n),factorial(n-t)*(m*n)**t) for t in range(min(m,n)+1))
    return numerator*factor


def exhaustive_count(m,n):
    cells=[(i,lam) for i in range(m) for lam in range(n)]
    count=0
    full=0
    for p in permutations(range(m*n)):
        images=set()
        for x,y in enumerate(p):
            i,lam=cells[x]; j,mu=cells[y]
            if lam==0 and j==0:
                break
            images.add((i,mu))
        else:
            if len(images)==m*n:
                count+=1
        images_full={(cells[x][0],cells[y][1]) for x,y in enumerate(p)}
        if len(images_full)==m*n:
            full+=1
    return count,full


def main():
    for m,n in [(2,2),(2,3),(3,2),(3,3)]:
        got,full=exhaustive_count(m,n)
        exp=claimed_count(m,n)
        base=factorial(n)**m*factorial(m)**n
        print('m,n',m,n,'count',got,'expected',exp,'unrestricted',full,'expected base',base)
        assert exp.denominator==1 and got==exp.numerator and full==base
    print('VERIFY_OK')

if __name__=='__main__':
    main()
