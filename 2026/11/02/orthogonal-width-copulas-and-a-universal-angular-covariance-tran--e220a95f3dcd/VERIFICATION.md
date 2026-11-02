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
# Reproducibility and verification

The exact proof appears in `RESULT.md`, and the standalone program is `verification/verify.py`. With Python 3 and `mpmath` installed, execute `python verification/verify.py` in the package root. It derives polygonal widths by vertex scalar products, compares them to the folded-cosine profile for each \(3\le n\le30\), numerically integrates the angular product at seven shifts per polygon, and tests five quantiles of the orthogonal enclosing-rectangle area distribution per polygon. A complete execution passed 11,564 individual geometric and numerical comparisons. The final high-precision checks evaluated opposite-angle Pearson correlations for seven effective side orders and verified the quartic limiting root.

The observations corroborate, but do not establish, the universal mathematical claims. The analytical steps requiring proof are central-symmetral geometry, the piecewise folded cosine integral, the strict sign of the derivative, the monotone area inversion, and the uniform Taylor estimate with variance of squared uniform coordinates. They are presented in `RESULT.md`.

Scientific limitations: only planar regular polygons with deterministic angular separation and uniform rotation; the limiting disk has undefined normalized width correlation. Literature priority has not been independently certified. No independent audit has been performed.
