"""Exact verification of isolated-chord/crossing covariance in uniform chord diagrams.
Python 3, standard library only. All checks use integer or rational arithmetic.
"""
from fractions import Fraction
from math import prod


def double_factorial_odd(j):
    assert j % 2 == 1 and j >= -1
    return prod(range(j, 0, -2))


def exact_formula(n):
    assert n >= 1
    denom = double_factorial_odd(2*n - 1)
    expected_isolates = Fraction(0)
    covariance = Fraction(0)
    expected_nonsimple = Fraction(0)
    nonsimple_covariance = Fraction(0)
    for r in range(n):
        p = Fraction(double_factorial_odd(2*r - 1)
                     * double_factorial_odd(2*n - 2*r - 3), denom)
        weight = n*p
        loss = Fraction(n-1 + r*(n-1-r), 3)
        expected_isolates += weight
        covariance -= weight*loss
        if 0 < r < n-1:
            expected_nonsimple += weight
            nonsimple_covariance -= weight*loss
    return expected_isolates, covariance, expected_nonsimple, nonsimple_covariance


def generate_matchings(points):
    if not points:
        yield ()
        return
    x = points[0]
    for j in range(1, len(points)):
        y = points[j]
        for rest in generate_matchings(points[1:j]+points[j+1:]):
            yield ((x,y),)+rest


def crossing(p,q):
    a,b = p
    c,d = q
    return (a<c<b<d) or (c<a<d<b)


def brute(n):
    N = 2*n
    total = 0
    sum_i = 0
    sum_s = 0
    sum_x = 0
    sum_ix = 0
    sum_sx = 0
    for matching in generate_matchings(tuple(range(N))):
        deg = [0]*n
        for i in range(n):
            for j in range(i+1,n):
                if crossing(matching[i],matching[j]):
                    deg[i]+=1
                    deg[j]+=1
        iso = sum(d==0 for d in deg)
        simple = sum(((b-a)==1 or (b-a)==N-1) for a,b in matching)
        x = sum(deg)//2
        total+=1
        sum_i+=iso
        sum_s+=simple
        sum_x+=x
        sum_ix+=iso*x
        sum_sx+=simple*x
    Ei=Fraction(sum_i,total)
    Es=Fraction(sum_s,total)
    Ex=Fraction(sum_x,total)
    cov_i = Fraction(sum_ix,total)-Ei*Ex
    cov_s = Fraction(sum_sx,total)-Es*Ex
    return total,Ei,Es,Ex,cov_i,cov_s


def main():
    total=0
    for n in range(1,8):
        count,Ei,Es,Ex,cov_i,cov_s=brute(n)
        Fi,Fc,Fn,Fnc=exact_formula(n)
        assert Ei==Fi,(n,'E isolates',Ei,Fi)
        assert cov_i==Fc,(n,'Cov',cov_i,Fc)
        assert Ex==Fraction(n*(n-1),6)
        assert Es==Fraction(2*n,2*n-1) if n>=2 else Es==1
        if n>=2:
            assert cov_s== -Fraction(2*n*(n-1),3*(2*n-1)),(n,'simple',cov_s)
        assert Ei-Es==Fn
        assert cov_i-cov_s==Fnc
        if n>=2:
            assert Fc<0
        total += count
        print(f'n={n}, matchings={count}, E_isolates={Ei}, Cov={cov_i}, non-simple Cov={Fnc}')
    print(f'ALL CHECKS PASSED ({total} exact matchings)')

if __name__=='__main__':
    main()
