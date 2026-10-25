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

Run `python verify.py` with NumPy and SciPy installed. The program independently checks the twelve-vertex projected-diameter formula against all 66 vertex pairs, enumerates the fifteen axis inner products and twenty triple Gram matrices, checks the exact pair-overlap primitive by adaptive quadrature, and compares three probabilities with 1,200,000 seeded Haar samples. It also checks the analytic quartic endpoint expansion numerically. These tests executed successfully. Neither simulation nor finitely many numerical comparisons constitutes a proof of a continuous-orientation statement; the full proof is in `RESULT.md`.

The exact formula is certified analytically only for \(0\le t\le\sqrt{(1-2/\sqrt5)/3}\). A complete lower-diameter branch, all other solids, and independent mathematical validation remain outside scope.
