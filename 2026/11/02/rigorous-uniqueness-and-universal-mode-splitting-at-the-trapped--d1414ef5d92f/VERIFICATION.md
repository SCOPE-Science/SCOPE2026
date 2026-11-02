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

# Verification and reproducibility

The analytical argument in `RESULT.md` proves the infinite-parameter statement. `verify.py` is a standalone Python 3.10+ diagnostic using NumPy, SciPy and SymPy. Invoke `python verify.py`; 170 deterministic assertions pass. The symbolic Kummer crossing identity is verified algebraically; five persistence ratios have their hypergeometric phase roots computed independently; 260-node Gauss--Jacobi quadrature checks the critical curvature and fourth-derivative identity; and near-critical mode locations approach squared-distance ratio three. Finite experiments cannot establish uniqueness or the exact universal theorem, so these are independently proved in the text by variation-diminishing, implicit-function and heat-equation arguments.

The published integral equation for the phase boundary is prior literature. Exact source metadata and comparison appear in `RESULT.md` and `REVIEW.md`. No independent audit has been performed.
