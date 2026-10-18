"""Exact finite checks of bounded-support recovery from divisor counts.
Run with python3 CHECKER.py; requires only the Python standard library.
This checks examples and exact reconstruction; it is not an infinite proof.
"""
from itertools import combinations_with_replacement
from math import comb, prod
from fractions import Fraction


def divisor_counts(a, r):
    return [prod(comb(k+x-1,x) for x in a) for k in range(1,r+2)]


def c_counts(d):
    return [sum((-1)**(j-t)*comb(j,t)* (d[t-1] if t else 0)
                for t in range(j+1)) for j in range(1,len(d)+1)]


def multiply(P, Q):
    R=[Fraction(0)]*(len(P)+len(Q)-1)
    for i,x in enumerate(P):
        for j,y in enumerate(Q): R[i+j]+=x*y
    return R


def polynomial_from_values(vals, r):
    # Reconstruct H(T)=T**r+sum_{j=0}^{r-1} b_j T**j.
    # Newton interpolation of H(T)-T**r at nodes 1,...,r.
    v=[Fraction(vals[i]-(i+1)**r) for i in range(r)]
    coeff=[]
    for j in range(r):
        coeff.append(v[0])
        v=[(v[i+1]-v[i])/Fraction(j+1) for i in range(len(v)-1)]
    poly=[Fraction(0)]
    basis=[Fraction(1)]
    for j in range(r):
        term=[coeff[j]*x for x in basis]
        poly += [Fraction(0)]*(len(term)-len(poly))
        for k,x in enumerate(term): poly[k]+=x
        basis=multiply(basis,[Fraction(-j-1),Fraction(1)])
    poly += [Fraction(0)]*(r+1-len(poly))
    poly[r]+=1
    return poly


def quotient_linear(poly, a):
    q=[Fraction(0)]*(len(poly)-1)
    q[-1]=poly[-1]
    for j in range(len(q)-2,-1,-1): q[j]=poly[j+1]-a*q[j+1]
    return q,poly[0]-a*q[0]


def recover_from_c(c, r):
    d=[1]
    for k in range(2,r+2):
        d.append(sum(comb(k,j)*c[j-1] for j in range(1,k+1)))
    assert all(x>0 for x in d)
    hvals=[Fraction(t**r*d[t],d[t-1]) for t in range(1,r+1)]
    assert all(x.denominator==1 for x in hvals)
    poly=polynomial_from_values(hvals,r)
    result=[]
    for a in range(1,max(2,max(int(x) for x in hvals))+1):
        while len(poly)>1:
            q, rem=quotient_linear(poly,a)
            if rem: break
            poly=q
            result.append(a)
        if len(poly)==1: break
    assert poly==[1],(c,r,poly)
    assert len(result)==r
    return tuple(sorted(result))

cases=0
for r,maximum in [(1,150),(2,100),(3,42),(4,20),(5,13)]:
    seen={}
    for a in combinations_with_replacement(range(1,maximum+1),r):
        d=divisor_counts(a,r)
        c=c_counts(d)
        assert c[0]==1
        recovered=recover_from_c(c,r)
        assert recovered==a,(r,a,recovered)
        fingerprint=tuple(c[1:])
        assert fingerprint not in seen or seen[fingerprint]==a
        seen[fingerprint]=a
        cases+=1

# Exact witnesses that one fewer count fails in prime-support sizes 2 and 3.
for left,right,r in [((1,5),(2,3),2),((1,6,8),(2,2,13),3),
                     ((3,7,11,74),(4,4,17,63),4)]:
    dl=divisor_counts(left,r)
    dr=divisor_counts(right,r)
    assert dl[:r]==dr[:r] and dl[r]!=dr[r]
    assert c_counts(dl)[:r]==c_counts(dr)[:r]
print('PASS:',cases,'exact exponent tuples recovered; three sharpness witnesses.')
