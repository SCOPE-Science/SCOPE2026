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

Run `python check_gap.py` with NumPy and SymPy installed; pinned minimum versions are given in `requirements.txt`. The script includes an independent symbolic determinant, four exact rational characteristic-polynomial factorizations, an exact order-three nilpotent test, 17 parameter regimes each sampled across 1001 dephasing angles, and determinant and trace checks. The actual run completed `PASS 17097 checks`. The analytical global optimum rests on the inequalities in RESULT.md, not exhaustive numerical sampling; near the third-order defective eigenvalue, ordinary floating-point eigensolvers lose several digits, and the script allows a small spectral tolerance.

The three nonzero Liouvillian eigenvalues are reproduced by the Bloch matrix; the remaining eigenvalue is the stationary identity mode. The test does not constitute a computational proof for the continuum of parameters or independent scientific certification.
