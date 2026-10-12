---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The symbolic proof in `RESULT.md` is unrestricted.

The attached checker independently evaluates the base-\(B\) digit sum and exhausts every prime pair
\[
p\le q<200
\]
and every base
\[
q<B\le pq.
\]
It compares the observed Smith bases with the divisor-cutoff formula
\[
B=1+\frac{pq-p-q}{a},
\qquad
a\mid pq-p-q,
\qquad
a\le\rho_-.
\]

For the even-prime branch it asserts that no admissible base occurs.

For every odd-prime pair in the exhaustive window except \((3,3)\), it verifies the canonical base
\[
B=(p-1)(q-1).
\]
It separately checks the \(p=3\) uniqueness law and the \(p=5\) two-base criterion for every prime
\[
q<5000.
\]

The finite replay does not establish the infinite statement. The infinite statement follows from the exact Smith equation, the factorization
\[
pq-p-q=a(B-1),
\]
and the quadratic digit-bound analysis.
