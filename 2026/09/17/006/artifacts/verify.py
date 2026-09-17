from math import comb
from fractions import Fraction

# Exact certificate for the refined first-moment argument at p=571.
p = 571
w = 35
K = 19

# primality check
assert all(p % d for d in range(2, int(p**0.5) + 1))
assert w == int((2*p)**0.5) + (1 if int((2*p)**0.5)**2 == 2*p else 2)  # ceil(sqrt(2p))+1

# Exact hit probability for a trace of size K under a uniformly random w-subset marking.
q = Fraction(1,1) - Fraction(comb(p-K, w), comb(p, w))
q0 = Fraction(353, 500)
assert q < q0

# For t in [2p,4p], S(t)=A(t)-t(p+1)/(K+1), where
# A(t)=(p+1)^2 (t-p)^2/[t(t+p)] is the Cauchy-Schwarz lower bound
# on the number of lines containing at least two points.
# Its derivative is minimized at t=4p on this interval.
dmin = Fraction((p+1)**2, p) * Fraction(39,400) - Fraction(p+1, K+1)
assert dmin > 27

# Hence successive expected-size upper bounds contract by < 1/40.
ratio_bound = Fraction(p,2) * q0**27
assert ratio_bound < Fraction(1,40)

# At t=2p, S(2p) is larger than 21869.
S0 = Fraction((p+1)**2, 6) - Fraction(2*p*(p+1), K+1)
assert S0 == Fraction(328042,15)
assert S0 > 21869

# C(p^2,2p) <= (e p/2)^(2p), and e < 11/4.
# Therefore b_{2p} < (11p/8)^(2p) q0^21869.
first_num = pow(11*p, 2*p) * pow(q0.numerator, 21869)
first_den = pow(8, 2*p) * pow(q0.denominator, 21869)
assert first_num * 20 < first_den * 7  # first term < 7/20

# Geometric tail gives expected number < (7/20)/(1-1/40)=14/39<1.
expected_bound = Fraction(7,20) / (1-Fraction(1,40))
assert expected_bound == Fraction(14,39)
assert expected_bound < 1

lattice_size = p**3 + 2*p**2 + 2
assert lattice_size == 186_821_495

print('p =', p)
print('w =', w)
print('exact q =', float(q), '< 353/500 =', float(q0))
print('minimum derivative bound =', float(dmin), '> 27')
print('successive-term ratio bound =', float(ratio_bound), '< 1/40')
print('S(2p) =', float(S0), '> 21869')
print('expected-count upper bound < 14/39 =', float(expected_bound))
print('counterexample lattice size =', lattice_size)
