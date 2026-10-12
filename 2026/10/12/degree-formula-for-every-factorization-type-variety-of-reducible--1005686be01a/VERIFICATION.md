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
The checker enumerates every partition of \(d\) for
\[
2\le d\le10
\]
and every
\[
3\le m\le7.
\]

For each partition it computes
\[
N_i=\binom{m+d_i-1}{m-1}-1,
\qquad
D=\sum_iN_i,
\]
the top intersection coefficient
\[
\frac{D!}{\prod_iN_i!},
\]
and the generic symmetry degree
\[
\prod_e\mu_e!.
\]
It verifies that the quotient is integral.

It separately verifies the specialization to completely decomposable forms, the closed formula for the top-dimensional component \((d-1,1)\), and the values
\[
3,\ 10,\ 21,\ 220
\]
for the listed small cases.

Finite checks do not prove the all-parameter theorem. The proof is the projection-formula and unique-factorization argument in `RESULT.md`.
