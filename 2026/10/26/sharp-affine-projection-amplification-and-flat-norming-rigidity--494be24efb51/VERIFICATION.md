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

The exact \(\ell_p\)-volume coordinate variance is calculated from gamma functions and tested against the Euclidean identity \(s_{d,2}^2=1/(d+2)\) for eight dimensions. The accompanying `check.py` samples normalized uniform \(\ell_p\)-ball points using independent gamma magnitudes, symmetric signs, and an exponential radial variable. It evaluates the actual affine kernel at flat, single-coordinate, and half-supported evaluation points for \(p\in\{3,4,6\}\) and dimensions \(24,96,288\), then compares the normalized norms to the predicted Gaussian law.

The script is intended as a finite stochastic diagnostic with stated tolerances, not an independent proof, exhaustive computation, or certification of the infinite theorem. The analytic proof in `RESULT.md` supplies all essential limiting steps, including moment normalization, weighted CLT, uniform small-profile bound, and rigidity. The paper identified by DOI:10.1007/BF01163879 could not be inspected in full; other previously unknown equivalent formulations may exist. Independent scientific audit has not been performed.
