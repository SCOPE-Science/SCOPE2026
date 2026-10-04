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

The proof is analytic. The accompanying checker uses exact rational arithmetic
where square roots are avoided by cross-multiplying squared inequalities.

For random rational mass profiles and strictly increasing rational supports,
it verifies:

- the exact maximum probability weights \(w_i=P_i^n-P_{i-1}^n\);
- the score covariance identity for \(\mathbb E M_n-\mathbb E X\);
- the exact centered-threshold decomposition of every support;
- the lower bound against every cumulative-mass cut;
- the upper Cauchy--Schwarz bound;
- exact upper equality on the score-affine support;
- exact equality for all two-point profiles.

It also builds sequences of distinct supports whose nonselected gaps shrink
toward zero and checks that the squared normalized gap converges toward the
selected lower cut constant.

Finite replay is supplementary and is not used to infer the cone inequality
or interval-filling theorem.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK identity_checks=48000 decomposition_checks=16000 lower_checks=16000 upper_checks=16000 upper_equality_checks=16000 two_point_checks=152 boundary_checks=12000`.
