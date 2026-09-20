from math import gcd, isqrt
from fractions import Fraction


def divisors(n):
    out=[]
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            out.append(d)
            if d*d!=n:
                out.append(n//d)
    return sorted(out)


def unitary_divisors(n):
    return [d for d in divisors(n) if gcd(d,n//d)==1]


def sigma_eu_prime_power(p,a):
    return sum(p**d for d in unitary_divisors(a))


def is_prime(n):
    if n<2:
        return False
    if n%2==0:
        return n==2
    d=3
    while d*d<=n:
        if n%d==0:
            return False
        d+=2
    return True

# Direct bounded search supporting the theorem (the proof is general and does not
# depend on this cutoff).
sol=[]
for q in range(3,500,2):
    if not is_prime(q):
        continue
    for a in range(1,21):
        ua=sigma_eu_prime_power(2,a)
        for b in range(1,21):
            ub=sigma_eu_prime_power(q,b)
            if ua*ub == 2*(2**a)*(q**b):
                sol.append((a,q,b,(2**a)*(q**b)))

# Check the exact example and the elementary upper bound used to reduce a.
assert sigma_eu_prime_power(2,2)*sigma_eu_prime_power(3,2)==72
assert sol == [(2,3,2,36)]

bound_pass=[]
for a in range(2,41):
    m=a//2
    upper=Fraction(1,1)+sum(Fraction(2**d,2**a) for d in range(1,m+1))
    if upper > Fraction(4,3):
        bound_pass.append(a)
assert bound_pass == [2,4]

print('bounded_search_q_lt_500_a_b_le_20:', sol)
print('sigma_eu_star_36:', sigma_eu_prime_power(2,2)*sigma_eu_prime_power(3,2))
print('a_values_surviving_S_upper_gt_4/3_through_40:', bound_pass)
