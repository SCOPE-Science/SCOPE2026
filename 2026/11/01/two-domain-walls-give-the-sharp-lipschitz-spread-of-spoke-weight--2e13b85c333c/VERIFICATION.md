---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Translate hub potential to zero, giving compact P_t={|x_i|≤t, |x_i−x_{i+1}|≤1}. The variance Hessian is positive definite, forcing maxima at vertices. For t≤1/2 all rim constraints vanish and balanced ±t signs optimize. For 1/2<t<1 tight components must touch ±t and then propagate integer differences, forcing only four levels ±t,±(1−t). A one-extreme-sign competitor has exact pairwise variance and is strictly worse by the displayed positive polynomial. With both extremes at least two bridge sites are compulsory; for even n the variance penalty per bridge plus mean square is minimized by exactly two opposite bridges. For odd n integral sign-parity bounds prohibit >=3 bridge sites and give residual mean |3t−2|. The t=1 limiting/polytopal argument and derivative identities cover boundaries. Independently exhausted all feasible FOUR-LEVEL candidate rim vectors n=4..7 at five rational t values, matching 20 exact rational optimum values; infinite real-parameter result depends on analytic four-level and exclusion proofs.

## originality

PASS

Best-of-knowledge independent search and theorem-level comparison. Spread is a known variance functional under Lipschitz constraints, but the weighted wheel's noninteger bridge levels and t-continuous metric make the existing unweighted integer extreme-point theorem inadequate; same invariant is not same theorem. A general upper bound for graph spread cannot yield the sharp equality branch, two-wall rigidity, or derivative discontinuity for these explicitly weighted wheels without additional polytope analysis. Direct comparison of assumptions shows earlier results allow general graphs but are bounds; they do not imply exact noninteger weighted-wheel optimizers. Novelty is specifically the interpolation and classification, not the spread definition. An unsuccessful search alone is not evidence of priority. Actual primary material read and remaining limits below.

## value

PASS

Exactly solves a natural metric-measure spread optimization on the simplest hub-plus-cycle graph as the metric shifts from hub-mediated to rim-geodesic. Two domain walls and a sharp first-derivative transition are structural, not a known unweighted graph table or arbitrary numerical slice, with complete parity-dependent optimizer classification for infinitely many rim lengths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
