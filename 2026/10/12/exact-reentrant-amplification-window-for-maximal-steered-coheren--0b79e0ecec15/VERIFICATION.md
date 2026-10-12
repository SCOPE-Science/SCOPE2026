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

The full argument is analytic. It uses exact density-matrix eigenvalues, the two-qubit positive-partial-transpose characterization of separability, the exact qubit Bloch-vector identity for single-outcome maximal steered coherence, and discriminant factorization of the remaining quadratic.

For reproducibility, run `python verify.py` with Python 3. The self-contained verifier constructs four physical, separable parameter triples, applies the two Kraus matrices explicitly and calculates conditional qubit states for the two analytically optimizing projective effects at eight damping strengths each. These 32 directly reconstructed coherence values agree with both closed squared-singular-value branches within numerical tolerance. Python `fractions.Fraction` reproduces the exact rational sample and squared-coherence and discriminant identities.

Expected terminal output: `VERIFY_OK exact_fraction_witness=passed direct_kraus_steering_cases=32 boundary=passed`.

These finite computations do not prove any universally quantified equality, positivity over a continuum, or literature novelty; those propositions are supported by the algebra in `RESULT.md` and the source comparison in `REVIEW.md`. Independent validation is not performed.
