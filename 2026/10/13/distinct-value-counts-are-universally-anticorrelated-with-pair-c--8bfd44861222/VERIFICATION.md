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

The theorem is proved analytically in `RESULT.md`. The accompanying checker supplies independent finite replay.

For several nonuniform rational probability vectors and sample sizes, the checker enumerates every iid sample word. Each word is weighted by its exact rational probability. It computes
\[
K_n,
\qquad
C_n,
\qquad
\mathbb E K_n,
\qquad
\mathbb E C_n,
\qquad
\mathbb E[K_nC_n]
\]
directly and verifies the exact covariance formula.

The checker separately verifies the weighted rearrangement quantities used in the sign proof and confirms strict negativity for every nondegenerate test profile.

For uniform laws it verifies
\[
\operatorname{Cov}(K_n,C_n)
=
-\frac{\binom n2}{m}
\left(1-\frac1m\right)^{n-1}
\]
and
\[
\operatorname{Var}(C_n)
=
\binom n2
\frac1m
\left(1-\frac1m\right).
\]

High-precision diagnostics evaluate the exact uniform covariance and occupied-count variance in birthday-scale sequences and confirm correlation approaching \(-1\).

These computations do not replace the all-parameter proof.

Independent audit has not been performed.

Deterministic replay result: `VERIFY_OK exhaustive_checks=25 weighted_sign_checks=25 uniform_checks=112 asymptotic_checks=9 enumerated_words=7882`.
