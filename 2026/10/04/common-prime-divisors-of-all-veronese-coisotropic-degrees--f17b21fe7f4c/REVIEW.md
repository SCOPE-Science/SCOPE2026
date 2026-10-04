# Same-model review

## Correctness
PASS. The polar vector is independently derivable from the standard smooth polar-class formula. Reindexing it as
\[
a_k=\binom Nk e^{k-1}(e-1)^{N-k},
\qquad
N=n+1,
\]
reduces the gcd theorem to a prime-wise minimum valuation. If \(p\nmid e\), the endpoint \(a_N=e^{N-1}\) excludes \(p\). If \(p\mid e\), then
\[
\nu_p(a_k)=\nu_p\binom Nk+(k-1)\nu_p(e),
\]
and
\[
\nu_p\binom Nk\ge\nu_p(N)-\nu_p(k).
\]
Because
\[
\nu_p(k)\le k-1\le(k-1)\nu_p(e),
\]
every term has valuation at least \(\nu_p(N)\), while \(k=1\) attains equality. This proves the claimed gcd exactly.

The bundled checker independently recomputes the polar vector from the Chern-class sum and verifies the gcd and ED-degree identities in finite ranges; those computations are regression evidence only.

## Originality
PASS. The inspected archival source identifies coisotropic degrees with polar degrees, and later sources provide explicit Segre--Veronese and quadratic-Veronese polar formulas. None of the inspected material states the gcd of the full Veronese polar vector, the common-prime iff criterion, or the exact shared \(p\)-adic exponent. Targeted semantic searches using gcd, common-divisor, common-prime, coisotropic, and polar-degree formulations found no covering statement.

Residual risk: the consequence is short once the explicit polar formula is known, so an unindexed historical source may contain it.

## Value
PASS. The result gives a natural arithmetic invariant of the complete system of generic tangency degrees attached to a Veronese variety. It determines exactly when the polar vector is primitive and exactly which primes divide every coisotropic degree, uniformly in dimension and embedding degree.

Same-model review: passed. Independent audit: not yet performed.
