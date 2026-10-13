# Self-review

## Correctness
PASS. The proof starts from the classical product formula for symmetric determinantal degrees. A direct Legendre-floor argument shows that, for every prime \(p\mid n\), the corank
\[
p^{\nu_p(n)}
\]
is a \(p\)-unit degree whenever that corank is proper. This removes every candidate common prime outside the prime-power case; odd prime powers are then excluded by the rank-one quadratic Veronese degree.

For
\[
n=2^e,
\]
an exact adjacent-corank ratio gives
\[
\nu_2(A_{2m})
=
m(e-1)-2\sum_{u=0}^{m-1}s_2(u).
\]
A proved binary digit-sum inequality implies that all proper degrees have valuation at least \(e-1\), while corank two has valuation exactly \(e-1\). The bundled checker independently verifies the full gcd formula through \(n=120\) and the valuation identities for powers of two through \(n=256\). The finite checks are not used as proof of the infinite theorem.

## Originality
PASS. The inspected algebraic-geometry source studies the same symmetric rank loci, and the standard degree source gives the classical Harris--Tu product, but neither states an exact gcd theorem for the full rank tower. Targeted searches for gcd, common divisor, parity, prime divisibility, and prime-adic aliases found no equivalent result. The closest same-object result located concerns adjacent-rank curvature rather than whole-tower arithmetic.

Residual risk: the arithmetic consequence is short enough that it could occur in older weakly indexed representation-theoretic or enumerative literature.

## Value
PASS. Symmetric rank loci form the complete secant/rank stratification of the quadratic Veronese family. Their projective degrees are natural generic intersection counts, so the gcd is the exact universal modulus shared by all proper rank strata at fixed matrix size. The theorem completely classifies when such universal divisibility exists and gives its exact size.

Self-review: passed. Independent audit: not yet performed.
