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

# Verification record

Execute the included standalone standard-library checker with `python3 check.py`; it prints `CHECK_OK` on success. Its `fractions.Fraction` computations reconstruct the two half-step and one whole-step backward-Euler matrices for the positive-definite diagonal generator, all entries of the blended matrix, and the strictly positive exact rational value of \(\|He_1\|_2^2-1\). It also tests the rank-one extremizer's closed-form eigenvalue and examples around the sharp threshold. The output was obtained from that file, not an unrelated earlier program.

The analytical argument independently establishes the operator inequality in all finite dimensions and the sharpness witness. Numerical floating-point comparisons only corroborate finite sample identities. No machine-checked proof or independent audit has been performed. The one-step norm excess does **not** prove divergent iterates; the given common-generator example has spectral radius below one by the displayed positive-definite similarity transform.
