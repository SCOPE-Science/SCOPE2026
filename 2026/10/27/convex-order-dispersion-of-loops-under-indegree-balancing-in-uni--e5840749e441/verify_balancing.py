"""Independent rational checks for fixed-point count under degree balancing.

No third-party dependencies. Usage: python research33_split_verifier.py
"""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial


def partitions_of_integer(n, smallest=1):
    if n == 0:
        yield ()
    else:
        for first in range(smallest, n + 1):
            for tail in partitions_of_integer(n-first, first):
                yield (first,) + tail


def elem_sym(groups, maximum):
    out = [0] * (maximum + 1)
    out[0] = 1
    for v in groups:
        for j in range(maximum, 0, -1):
            out[j] += v * out[j-1]
    return out


def falling(n, r):
    z = 1
    for j in range(r):
        z *= n-j
    return z


def pgf_coefficients(groups, n):
    # Coefficients of E[z^F] via factorial moments and the change z=1+t.
    e = elem_sym(groups, n)
    ans = []
    for f in range(n+1):
        ans.append(sum(((-1)**(r-f))*comb(r,f)*Fraction(e[r], falling(n,r))
                       for r in range(f,n+1)))
    return ans


def sample_by_injections(groups,n):
    # Directly enumerates distinct target injections into nonempty fiber blocks.
    # Does not use the elementary-symmetric-polynomial expression.
    result=[0]*(n+1)
    p=0; blocks=[]
    for d in groups:
        blocks.append(set(range(p,p+d)))
        p+=d
    for targets in permutations(range(n),len(groups)):
        fixed=sum(targets[j] in blocks[j] for j in range(len(groups)))
        result[fixed]+=1
    den=falling(n,len(groups))
    return [Fraction(x,den) for x in result]


def auxiliary_pgf(others,n):
    return pgf_coefficients(others,n-2)


def balancing_identity(old_left,old_right,new_left,new_right,others,n):
    a=pgf_coefficients((old_left,old_right)+others,n)
    b=pgf_coefficients((new_left,new_right)+others,n)
    q=auxiliary_pgf(others,n)
    scale=Fraction(new_left*new_right-old_left*old_right,n*(n-1))
    for f in range(n+1):
        target=scale*((q[f] if f<len(q) else 0)
                      -2*(q[f-1] if 0<=f-1<len(q) else 0)
                      +(q[f-2] if 0<=f-2<len(q) else 0))
        assert b[f]-a[f]==target,(n,old_left,old_right,new_left,new_right,others,f)
    # Convex-order call-function inequalities at every integer threshold.
    for threshold in range(n):
        comparison=sum(Fraction(f-threshold)*(b[f]-a[f]) for f in range(threshold+1,n+1))
        assert comparison>=0,(n,old_left,old_right,new_left,new_right,others,threshold)
    assert sum(Fraction(f)*(b[f]-a[f]) for f in range(n+1))==0
    assert sum(Fraction(f*f)*(b[f]-a[f]) for f in range(n+1))==2*scale
    return n+3


def main():
    validations=0
    for n in range(2,9):
        for profile in partitions_of_integer(n):
            formula=pgf_coefficients(profile,n)
            assert formula==sample_by_injections(profile,n),(n,profile)
            assert sum(formula)==1
            assert sum(Fraction(f)*formula[f] for f in range(n+1))==1
            validations+=3
            expanded=profile+(0,)*(n-len(profile))
            for i in range(n):
                for j in range(n):
                    if i!=j and expanded[i]>=expanded[j]+2:
                        others=tuple(expanded[t] for t in range(n) if t not in (i,j) and expanded[t])
                        validations+=balancing_identity(expanded[i],expanded[j],expanded[i]-1,expanded[j]+1,others,n)
        print(f'n={n}: exact enumeration, pmfs, all degree-balancing transfers and call inequalities verified')
    print(f'PASS exact assertion count {validations}')

if __name__=='__main__':main()
