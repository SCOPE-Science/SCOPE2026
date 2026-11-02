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

Run `python3 verify.py` with Python 3.8 or later; only the standard library is required. The expected final line is:

`PASS: 816 checks; Fourier dimensions 5..250, modular Kalman dimensions 5..34, and collision orders 5..180`

The program checks all indicated finite dimensions. It uses a prime-modulus exact rank calculation for the control matrix and a floating-point tolerance only for spectral collision detection; neither finite output proves the theorem at unbounded sizes. The mathematical proof is the cyclotomic order classification and the PBH/Vandermonde argument in `RESULT.md`. No independent audit has been performed.
