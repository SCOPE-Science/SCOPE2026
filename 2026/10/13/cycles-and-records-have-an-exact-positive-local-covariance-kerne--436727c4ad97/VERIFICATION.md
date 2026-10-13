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

The proof is analytic. The accompanying checker exhaustively enumerates every permutation in
\[
S_n,
\qquad
2\le n\le9.
\]

For each permutation it recomputes the cycle count by orbit traversal and recomputes every upper-record indicator directly from the one-line word. All expectations are accumulated with exact integer counts and compared using rational arithmetic.

For every admissible \(n\) and \(j\), the checker verifies
\[
\Pr(R_{n,j}=1)=\frac1j
\]
and
\[
\operatorname{Cov}(C_n,R_{n,j})
=
\frac{j-1}{n j\binom{n-1}{j-1}}.
\]

It separately verifies the total covariance obtained by summing the local terms and the exact variance identity
\[
\operatorname{Var}(C_n)
=
\operatorname{Var}(R_n)
=
H_n-H_n^{(2)}.
\]

The exhaustive replay is supplementary. The universal proof is the insertion recurrence in `RESULT.md`.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK permutations_checked=409112 probability_checks=44 local_covariance_checks=44 positivity_checks=36 total_covariance_checks=8 variance_checks=16`.
