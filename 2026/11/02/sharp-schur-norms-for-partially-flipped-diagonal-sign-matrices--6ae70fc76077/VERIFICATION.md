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
The analytical argument provides both a spectral-sign lower witness and a matching positive-semidefinite Gram upper certificate. The checker `verify_schur.py` uses NumPy to verify the certificates' eigenvalues and the witness trace norms for integer \(1\le k\le100\), including the boundary between the two extremal regimes. Its recorded execution returned `PASS: 895 finite numerical assertions; checked k=1..100.`

Run `python verify_schur.py` in the directory containing this note. Calculations are finite supplementary checks only; the universal claims rely on the proof and are not inferred from enumeration or floating-point data. Complex-matrix validity follows from the operator-factorization inequality in the proof.
