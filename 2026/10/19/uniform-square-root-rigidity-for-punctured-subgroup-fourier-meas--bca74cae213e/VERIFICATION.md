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

`verify.py` uses only the Python standard library. Run `python verify.py` to reproduce Fourier coefficients, fixed-origin-mass profiles, the explicit optimizer and stability estimates on finite cyclic groups and finite-field prime planes. The program tests 32,000 seeded random admissible measures (4,000 in each of eight examples); it is not an exhaustive enumeration and not a substitute for the all-group proof. The proof uses finite character orthogonality, Parseval, and a two-point odd-characteristic perturbation. Neither an external audit nor any infinite computation is claimed.
