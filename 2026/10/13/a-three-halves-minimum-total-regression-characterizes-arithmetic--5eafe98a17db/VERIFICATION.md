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

The proof is analytic. The accompanying checker supplies an exact finite replay.

It enumerates every strictly increasing integer population formed by choosing \(N\) points from
\[
\{0,\ldots,9\},
\qquad
3\le N\le9,
\]
and then enumerates every unordered sample pair.

For each population, it reconstructs
\[
\mathbb E[S\mid M=z_k]
\]
from the pair census using exact rational arithmetic. It verifies that
\[
\mathbb E[S\mid M]-\frac32M
\]
is constant if and only if all adjacent population spacings are equal.

For every arithmetic population in the census, the checker also verifies the dual maximum regression, the exact covariance identity
\[
\operatorname{Cov}(M,S)=\frac32\operatorname{Var}(M),
\]
and the exact squared correlation
\[
\operatorname{Corr}(M,S)^2=\frac34.
\]

The census is supplementary. The proof for arbitrary \(N\) is the tail-mean recurrence in `RESULT.md`.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK populations=967 pair_rows=11430 regression_checks=4043 rigidity_checks=967 max_checks=194 covariance_checks=54 correlation_checks=108`.
