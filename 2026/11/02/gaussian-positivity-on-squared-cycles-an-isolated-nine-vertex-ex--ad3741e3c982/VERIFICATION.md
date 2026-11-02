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

The standalone standard-library checker `check.py` was executed from this seven-file package's working directory. It separately constructed graph distances by BFS for all orders 3 through 128, checked each circulant Fourier sum against the stated formulas, classified positive and zero nonconstant modes, and verified the exact 9-vertex residue totals [4,4,4]. Its reported output was `CHECK_OK 732270 BFS, circulant Fourier, sign and nullity assertions n=3..128 n9_residue_totals= [4, 4, 4]`.

Numerical Fourier comparisons have finite floating-point tolerance and cannot certify all infinitely many dimensions. The nonnumerical derivation and sign classification in `RESULT.md` supply the proof for all orders. Literature screening remains bounded; independent validation has not been performed.
