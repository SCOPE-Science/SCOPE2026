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

# Reproduction and limitations

The accompanying `verify.py` is a standalone Python 3 script depending on NumPy. Run `python verify.py`. The saved script was executed from its actual path and returned:

`VERIFY_OK: 2183 deterministic assertions, including rank enumeration and numerical samples.`

Checks cover the exact Euclidean ray-angle geometry independently of the final formula, derivative and centroid curvature by finite differences, uniform distinguished-rank enumeration, consistency of the fixed-dimensional mean, Gaussian hyperplane simulations, and diagnostics for both limiting regimes. Random checks use a fixed seed; they are nonexhaustive and approximate. The exact rank enumeration has a finite parameter range. Universal correctness requires the analytic proof in `RESULT.md`, particularly the Gaussian local empirical-CDF equicontinuity and the distinction between \(t<1\) and \(t=1\). Historical novelty and scientific value are assessed separately in `REVIEW.md` and `AUDIT.json`. Independent scientific audit has not been performed.
