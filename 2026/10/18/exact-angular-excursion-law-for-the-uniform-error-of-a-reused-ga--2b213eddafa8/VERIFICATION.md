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

Run `python verify_rotation.py` with dependencies in `requirements.txt`. Expected output is embedded verbatim in `verification_output.txt`.

The program reconstructs actual rank-one projections of \(A_\varepsilon(t)\) from a Gaussian vector, compares their spectral norm residuals against the closed formula, checks the formula for the continuous supremum against finite angular grids, computes mean errors through two independent one-dimensional integrations, and compares exact angular-tail probabilities against 150,000-point deterministic angular grids. It also checks the small-eigenvalue logarithmic mean expansion and the exact pointwise squared-error identity.

All six check classes passed in a run on the supplied standalone script. The dense grids, quadratures, and finite test cases do not certify any result for all angles or all positive \(\varepsilon\); the infinite and continuum statements rest on the proof in `RESULT.md`. The Gaussian direction is mathematically uniform modulo \(\pi\) because the two probe coordinates are independent standard normals. The residual calculation and projective circle measure, not simulation output, establish the sharp tail probabilities. No independent audit or external certification has been performed.
