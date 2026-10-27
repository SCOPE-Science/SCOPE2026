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

# Reproducibility and limits

The claim is proved symbolically in `RESULT.md`, by the grade norm bound and exact parity-selective pure-tensor saturation. The standalone script `verify_mixed_fock.py` (requires NumPy) constructs every finite tensor matrix directly from creator and annihilator formulas and tests it against the scalar path matrix. It also tests the explicit extremal parity vectors, the entries of the two Jacobi blocks, all zero-weight boundaries, and the exact balanced path-cosine identity.

Run: `python verify_mixed_fock.py`.

The packaged program was executed successfully: 109 mixed-vector finite-Fock norm/chain checks, 40 degenerate or weighted path checks, and 80 balanced path/deficit checks. These are finite floating-point checks of algebraic formulas. They do not independently establish the quantifiers over arbitrary Hilbert spaces and cutoff orders; those rely on the proof. No external audit has been performed.
