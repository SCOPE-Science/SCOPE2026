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

Run `python3 verify/verify_wheel_metric.py` and `python3 verify/verify_wheel_complement_count.py` with Python 3; both use only the standard library. The first enumerates wheel spanning trees for rim sizes 3–10 and checks eccentricity, radius, diameter, and peripheral counts; for rim sizes 3–5 it explicitly generates all one-edge exchanges and breadth-first-searches all shortest paths. The second directly enumerates every two-coloring of rim edges and spokes for sizes 3–8, checks both colors are spanning trees, and compares this with the two alternating-boundary constructions; for rim sizes 9–14 it verifies all constructed completions.

Representative results: for \(m=6\) the wheel has 320 spanning trees, radius 4, diameter 6, and 124 peripheral spanning trees. For \(m=10\) the corresponding values are 15125, 7, 10, and 2044. The direct exhaustive check returns `ALL_WHEEL_TREE_METRIC_CHECKS_PASS`; the complementary-tree checker returns `ALL_WHEEL_COMPLEMENT_CHECKS_PASS`.

The mathematical proof separately covers every integer \(m\ge3\). Finite enumerations are consistency checks rather than a substitute for the unbounded arguments. No independent scholarly audit has been performed.
