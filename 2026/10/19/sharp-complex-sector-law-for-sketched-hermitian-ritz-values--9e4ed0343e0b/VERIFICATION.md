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

# Reproduction of the sharp sector law

The theorem is proved analytically in `RESULT.md`. The accompanying `verify.py` is a self-contained standard-library corroboration of two exact constructions and multiple finite sampled examples. Run `python3 verify.py` alongside these documents.

The exact fraction checks reconstruct \(u^*T_0u=24/25\), the real and imaginary parts of \(u^*T_0A_0u\), the quotient \((5+\sqrt2 i)/3\), and the Gram perturbation norm \(1/5\). The explicit real sketches attain a zero eigenvalue at distortion \(3/5\) and a negative one at \(3/4\) for spectral ratio \(9\).

The random tests cover seven positive spectral ratios, five fractions of the sharp admissible embedding range, and 250 complex Hermitian sketch perturbations per combination, for 8,750 total instances. All perturbations are parametrized to ensure the required operator-norm condition exactly by construction (up to floating-point evaluation); each generated Ritz quotient is compared against the analytical sector in floating-point arithmetic.

Expected output:

`VERIFY_OK exact_fraction_identities=6 sharp_complex_equality=1 sharp_threshold_witnesses=2 random_complex_embedding_cases=8750`

Boundaries and limitations: these numerical checks are finite and do not prove the universal statement; the proof supplies that. The verifier does not enumerate all Hermitian matrices or sketches, certify floating-point implementations of eigensolvers, or establish independent validation. The theorem's equality sketch is positive definite and may be square or extended to a genuinely dimension-reducing two-by-three sketch.
