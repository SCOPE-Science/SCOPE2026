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
# Reproducibility and verification

The included `verify.py` can be run with Python 3 and the two pinned packages in `requirements.txt`. The executed version produced `PASS 329 deterministic checks` followed by independent high-precision approximations of the fold, first-order switch and asymptotic coefficients. Checks include symbolic consistency of the telegraph backward equations, symbolic stationary-objective differentiation, high-precision stationary roots, exact equation residuals, objective comparisons on both sides of the switch, and large-distance numerical scaling.

The underlying proof is the analytical argument in `RESULT.md`. Testing finitely many parameters is not a proof of the uniqueness assertions; those follow from strict monotonicity of \(H\) and the envelope comparison. Numerical threshold digits are not represented as certified interval arithmetic; the exact definitions are the unique roots established in the proof.

The first-public-source date is documented as July 18, 2026 in the open-access journal record. The result is restricted to fixed-total-rate Bernoulli decisions and deterministic favorable-direction resets. Comparison with relevant literature does not establish independent priority, and independent auditing was not performed.
