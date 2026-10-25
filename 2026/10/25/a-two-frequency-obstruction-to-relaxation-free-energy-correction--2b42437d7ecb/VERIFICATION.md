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

Run the bundled standalone `verify.py` using `python3 verify.py`. No external modules, network connection, or numerical libraries are required. The program verifies, with exact rational arithmetic, the stage multiplier, the two squared-amplification quadratic polynomials, their strictly positive discriminants, the mixed quadratic discriminant identity valid for every real energy fraction, and the exact strictly positive completed-square constant. It additionally compares 54 directly evaluated four-dimensional real RK steps against the derived formula, using floating-point square roots as a supplementary check.

The expected final program output is `VERIFY_OK exact stage polynomial, two mode certificates, quadratic frontier identity, 54 direct 4D runs`.

The universal real-root iff classification follows from the polynomial proof in RESULT.md, not from enumeration or simulations. The checker is a finite independent implementation of key algebraic identities, not a substitute for the proof. Only the stated fixed-step, two-frequency, single-scalar correction is analyzed. Priority and broader-domain extension are not established by these calculations.
