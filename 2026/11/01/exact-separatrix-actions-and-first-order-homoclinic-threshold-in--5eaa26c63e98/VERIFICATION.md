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

Run `python verify_separatrix.py` with Python 3 and SymPy. The script recomputes the potential factorization, exact action quadratures, the two first-order Melnikov integral values, and the slope/width from algebraic quantities. Its exit code is nonzero if a symbolic equality fails.

The reproducible symbolic checks validate necessary identities in the proof; they do not independently establish the smoothness of stable/unstable manifolds or originality. Those deductions use the analytical argument and the literature comparison, respectively. The reported status is self-review only.
