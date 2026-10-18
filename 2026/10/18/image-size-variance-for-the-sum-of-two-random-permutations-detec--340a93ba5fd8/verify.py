"""Exact finite-group checks for the variance of the image size of two random permutations.

Run with Python >=3.9. No external packages or randomness required.
"""
from itertools import permutations, product
from collections import Counter
from fractions import Fraction
from math import factorial, comb, lcm


def group(factors):
    pts=list(product(*(range(q) for q in factors)))
    pos={pt:i for i,pt in enumerate(pts)}
    add=[[pos[tuple((a+b)%q for a,b,q in zip(x,y,factors))]
          for y in pts] for x in pts]
    order=[lcm(*(q//__import__('math').gcd(q,a) for q,a in zip(factors,x)))
           for x in pts]
    return add,order


def convolve(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out


def cycle_rook_poly(m):
    return [1]+[2*m*comb(2*m-k,k)//(2*m-k) for k in range(1,m+1)]


def forbidden_pair_probability(n,m):
    assert n % m == 0 and m >= 2
    q=[1]
    for _ in range(n//m): q=convolve(q,cycle_rook_poly(m))
    return Fraction(sum((-1)**k*co*factorial(n-k)
                        for k,co in enumerate(q)),factorial(n))


def formula(factors):
    add,ords=group(factors)
    n=len(add)
    p0=Fraction(sum((-1)**k*Fraction(1,factorial(k))
                    for k in range(n+1)))
    em=n*(1-p0)
    var=n*p0-n*n*p0*p0 + n*sum(
        (forbidden_pair_probability(n,m) for m in ords[1:]),Fraction(0))
    return em,var,p0,ords


def exhaustive(factors):
    add,ords=group(factors)
    n=len(add)
    hist=Counter()
    zero_counts=[0]*n
    both_counts=[0]*n
    total=0
    for pi in permutations(range(n)):
        outputs={add[i][pi[i]] for i in range(n)}
        hist[len(outputs)]+=1
        absent=[u not in outputs for u in range(n)]
        for u in range(n):
            zero_counts[u]+=absent[u]
            both_counts[u]+=absent[0] and absent[u]
        total+=1
    assert total == factorial(n)
    em=sum(Fraction(k*v,total) for k,v in hist.items())
    var=sum(Fraction((k*k)*v,total) for k,v in hist.items())-em*em
    exp,var_formula,p0,ords=formula(factors)
    assert em==exp,(factors,em,exp)
    assert var==var_formula,(factors,var,var_formula)
    assert all(Fraction(c,total)==p0 for c in zero_counts)
    for u in range(1,n):
        assert Fraction(both_counts[u],total)==forbidden_pair_probability(n,ords[u]),(factors,u)
    print(f'{factors}: n={n}, image histogram={dict(sorted(hist.items()))}, '
          f'mean={em}, variance={var}, pair checks={n-1}')
    return 2+n+n-1


def brute_cycle_matchings(n,m):
    # The cyclic two-factor board with rows i and columns (-i) and (mshift-i),
    # represented here by rows i, columns i and i+1 (mod m) in each of n/m blocks.
    adj=[(i//m*m+i%m, i//m*m+(i%m+1)%m) for i in range(n)]
    out=Counter()
    def go(i,used,k):
        if i==n:
            out[k]+=1
            return
        go(i+1,used,k)
        for c in adj[i]:
            if not (used >> c)&1:
                go(i+1,used|(1<<c),k+1)
    go(0,0,0)
    q=[1]
    for _ in range(n//m):q=convolve(q,cycle_rook_poly(m))
    assert [out[k] for k in range(n+1)]==q,(n,m,out,q)
    return n+1


def main():
    checks=0
    for n in [2,3,4,6,8]:
        for m in range(2,n+1):
            if n%m==0:
                checks+=brute_cycle_matchings(n,m)
    for factors in [(2,),(3,),(4,),(2,2),(5,),(6,),(2,3),(7,),(8,),(4,2),(2,2,2)]:
        checks+=exhaustive(factors)
    assert formula((4,))[:2]==(Fraction(5,2),Fraction(7,12))
    assert formula((2,2))[:2]==(Fraction(5,2),Fraction(5,4))
    checks+=2
    print(f'PASS: {checks} grouped exact identities; zero Monte Carlo estimation.')

if __name__=='__main__':main()
