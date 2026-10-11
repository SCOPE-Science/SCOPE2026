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
# Reproducible verification

The `verify.py` source embedded with the finding independently recomputes the single-point area and boundary moments and reconstructs the fourth Euclidean moment of differences of two independent copies. The only required nonstandard dependency is declared in `requirements.txt`. Execute `python verify.py` and expect both markers `PARALLELOGRAM_FOURTH_CHORD_EXACT_OK` and `PARALLELOGRAM_ANGULAR_PHASE_EXACT_OK`.

The checker verifies exact algebraic identities for all symbolic generator lengths and dot products, both positive polynomial endpoint representations, the square value, the aspect-ratio degeneration limit, and the derivative factor giving the angular transition. The proof separately explains why the positive coefficient certificates cover all \(t\ge0\), why the boundary case \(c^2=1\) is used only in polynomial interpolation, and why the cubic has exactly one root above \(2\). A second script, `independent_check.py`, directly integrates the fourth power of the distance for all boundary-edge pairs and two independent interior points for the exact skew generators \(a=(3,0)\), \(b=(4/5,3/5)\); it reports `PARALLELOGRAM_INDEPENDENT_INTEGRAL_CHECK_OK`. This independent computation is a single rational spot-check, not a separate scientific audit or a universal proof. The sign and domain arguments are not inferred from finite samples.

No claim is made about higher moments, arbitrary planar convex bodies, or an independent mathematical audit. Literature priority remains subject to further primary-source inspection.
