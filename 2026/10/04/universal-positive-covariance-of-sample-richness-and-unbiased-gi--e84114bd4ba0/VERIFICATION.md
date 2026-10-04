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

The proof is analytic. The accompanying checker uses exact rational arithmetic.

For several rational categorical laws it exhaustively enumerates the complete iid sample space through sample size six, computes observed richness and the unbiased Gini--Simpson statistic, and verifies the exact covariance formula.

It then tests thousands of rational probability profiles and verifies
\[
B_n\le s_2A_n,
\]
the lower bound
\[
\operatorname{Cov}(K_n,\widehat G_n)
\ge
s_2(1-s_2)A_n,
\]
strict positivity, and the stated equality cases.

Finite replay is supplementary. The universal theorem is the direct collision-pair calculation and antitonic size-biased inequality in `RESULT.md`.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK enumeration_checks=19 formula_checks=24038 lower_bound_checks=24038 equality_checks=1037 strict_checks=11486`.
