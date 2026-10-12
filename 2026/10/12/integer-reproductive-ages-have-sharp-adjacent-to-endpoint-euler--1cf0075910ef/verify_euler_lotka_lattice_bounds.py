#!/usr/bin/env python3
from fractions import Fraction
from itertools import product

Z_VALUES=[Fraction(1,2),Fraction(2,3),Fraction(3,2),Fraction(2,1)]

def powq(z,j):
    return z**j

def expectation(counts,L,z):
    M=sum(counts)
    return sum(Fraction(c,M)*powq(z,L+i) for i,c in enumerate(counts))

def mean_age(counts,L):
    M=sum(counts)
    return sum(Fraction(c,M)*(L+i) for i,c in enumerate(counts))

def adjacent_expectation(mu,z):
    k=mu.numerator//mu.denominator
    if mu.denominator==1:
        return powq(z,k)
    theta=mu-k
    return (1-theta)*powq(z,k)+theta*powq(z,k+1)

def endpoint_expectation(mu,L,U,z):
    qL=Fraction(U,1)-mu
    qL/=U-L
    qU=mu-Fraction(L,1)
    qU/=U-L
    return qL*powq(z,L)+qU*powq(z,U)

checked=0
strict_checked=0
for L in range(1,5):
    for U in range(L+1,8):
        m=U-L+1
        for M in range(1,9):
            # all rational distributions with denominator M
            for counts in product(range(M+1), repeat=m):
                if sum(counts)!=M:
                    continue
                mu=mean_age(counts,L)
                for z in Z_VALUES:
                    e=expectation(counts,L,z)
                    lo=adjacent_expectation(mu,z)
                    hi=endpoint_expectation(mu,L,U,z)
                    assert lo <= e <= hi, (L,U,M,counts,mu,z,lo,e,hi)
                    checked += 1
                # Strictness at nontrivial z for non-extremizers is spot-checked
                z=Fraction(2,1)
                e=expectation(counts,L,z)
                lo=adjacent_expectation(mu,z)
                hi=endpoint_expectation(mu,L,U,z)
                k=mu.numerator//mu.denominator
                theta=mu-k
                adj=[0]*m
                if mu.denominator==1:
                    adj[k-L]=M
                    is_adj = counts==tuple(adj)
                else:
                    # exact adj representation may not have denominator M; only compare if representable
                    is_adj=False
                    if (1-theta)*M == int((1-theta)*M) and theta*M == int(theta*M):
                        adj[k-L]=int((1-theta)*M); adj[k+1-L]=int(theta*M)
                        is_adj=counts==tuple(adj)
                if not is_adj and e==lo:
                    raise AssertionError(('unexpected lower equality',L,U,M,counts,mu))
                qL=(Fraction(U,1)-mu)/Fraction(U-L,1)
                qU=(mu-Fraction(L,1))/Fraction(U-L,1)
                is_end=False
                if qL*M==int(qL*M) and qU*M==int(qU*M):
                    end=[0]*m; end[0]=int(qL*M); end[-1]=int(qU*M)
                    is_end=counts==tuple(end)
                if not is_end and e==hi:
                    raise AssertionError(('unexpected upper equality',L,U,M,counts,mu))
                strict_checked += 1

# Worked demographic example: R0=2, ages 1..4, mean 5/2.
# Adjacent schedule: half reproduction at ages 2,3 => lambda^3-lambda-1=0.
# Endpoint schedule: half at ages 1,4 => lambda^4-lambda^3-1=0.
def p_adj(x): return x**3-x-1
def p_end(x): return x**4-x**3-1
la_lo=Fraction(13247,10000); la_hi=Fraction(13248,10000)
le_lo=Fraction(13802,10000); le_hi=Fraction(13803,10000)
assert p_adj(la_lo)<0<p_adj(la_hi)
assert p_end(le_lo)<0<p_end(le_hi)
assert la_hi < le_lo

# Convex-order direction translated to Euler-Lotka roots: for z != 1,
# adjacent <= arbitrary <= endpoints in E[z^A]. The Euler-Lotka function
# is monotone in z, so roots in z reverse this order and roots lambda=1/z
# restore it: lambda_adj <= lambda_any <= lambda_end.
print('VERIFY_OK')
print('exact_distribution_checks', checked)
print('strictness_checks', strict_checked)
print('z_values', [str(z) for z in Z_VALUES])
print('example_lambda_adj_bracket', float(la_lo), float(la_hi))
print('example_lambda_end_bracket', float(le_lo), float(le_hi))
