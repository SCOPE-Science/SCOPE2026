# Independent mathematical audit

## correctness

PASS

The exact inequality is B^n<A^(n+1) for A=pi(n^2)>0 and B=A+d=pi((n+1)^2). For n>=1000, Brun-Titchmarsh controls the number of new primes d<=2(2n+1)/log(2n+1), and Rosser-Schoenfeld pi(n^2)>n^2/(2log n). From log n<n/100 derive A>50n>=50000 and log A>9; meanwhile n log(1+d/A)<nd/A<8+4/n<9. The interval width satisfies required x>=1, y>=2 and y<=x in this range. Independently generated exact sieve to 1,000,000 (pi=78498) and arbitrary-precision powers check all 997 integers 3<=n<=999, matching inspected verify.py. All indices are covered; finite tests do not prove the analytic tail.

## originality

PASS

Sun Conjecture 2.14(ii) in the full 2014 prime-problems source is literally the same sequence pi(n^2)^(1/n); inspected the conjecture page. We did not locate a subsequent full proof after targeted Sun/prime-root searches and Resultary semantic comparison. Related Sun Conjecture 2.7 fixes scale n while varying multiplicative k and does not imply this next-square inequality by either natural substitution. Classical prime-counting estimates are prior; the claimed contribution is their use to settle this exact conjectured all-n monotonicity.

## value

PASS

This resolves a specific published prime-counting monotonicity conjecture for every n>=3, with a rigorously closed analytic tail and finite prefix. It is a natural boundary on growth of prime counts between consecutive squares and not an arbitrary small data check. It does not imply Legendre or Firoozbakht conjectures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
