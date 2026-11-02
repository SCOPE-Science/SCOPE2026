# Independent mathematical audit

## correctness

PASS

By marking two distinct block sizes in the Dyck-path/noncrossing bivariate generating function and applying Lagrange coefficients, the integer totals are A_a=binom(2n-a-1,n-a), M_ab=n binom(2n-a-b-2,n-a-b) for a+b<=n, otherwise zero, normalized by C_n. The ratio R(a+1,b)/R(a,b) is ((n-a-b)(2n-a-1))/((2n-a-b-2)(n-a)) and numerator minus denominator is n-b(n-1)-a<=0; symmetrically in b. The largest distinct-size ratio comes from {1,2}; substitution gives the sharp factor <1. n=2 and a+b>n handled directly, and equality uniqueness follows from strict steps unless the initial {1,2} pair. Direct independent Dyck enumerations n<=9 verified 240 exact mixed-moment signs/ratios including small boundaries. The all-n theorem is the coefficient identity plus monotonic ratio argument.

## originality

PASS

Kargin (2019) ALREADY explicitly computes the bivariate generating function and the exact two-size mixed moment, and proves the large-n negative covariance for each FIXED pair. Those ingredients are not novel. The assessed added theorem is STRICT negative covariance at every finite n for every pair, including growing sizes, together with the sharp normalized deficit and unique extremizer. Kargin Theorem 2.4 and proof pages 8–9 were read and do not state the finite universal maximum. An earlier use of the same exact formulas to derive the bound is possible and remains a priority risk.

## value

PASS

Finite negative dependence for all block size pairs cannot be deduced from a fixed-pair asymptotic with O(1) remainder. The exact optimal bound and unique pair {1,2} supply uniform finite-sample control of a natural random combinatorial block profile, with a precise mathematical boundary; no full negative association is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
