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

# Reproducibility and proof boundary

The mathematical proof is contained in `RESULT.md`. The independent computational cross-check is `checker.py`, requiring Python 3 and NumPy. Execute `python checker.py` from the extracted finding directory. It checks exact survival/mass identities; transforms against direct finite sums; the sharp two-step bounds; and the independent reset-age distribution evolution against the predicted co-rotating spectral limit at multiple phases. The exact example yields \(p=1/2\), amplitude \(1/(1+2\log 2)\), and successive-state trace-norm limit \(2/(1+2\log 2)\).

All experiments are finite; no enumeration or numerical convergence estimate is substituted for the analytic coupling, Fourier and spectral arguments. The result has undergone self-review only; no independent audit has been performed.
