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

# Reproducibility and finite checks

Run `python verify_crown_geodesic.py` and `python verify_crown_exhaustive.py` with Python 3 and no nonstandard dependencies. The first checks the displayed six- and ten-step local witnesses, all intermediate fixed-point restrictions and the relative cycle split/merge counts for \(k=2,\ldots,30\). The second directly enumerates perfect matchings and four-cycle flips for crown graphs with \(n\in\{3,4,5,6,9\}\), and performs exhaustive BFS from the distinguished source to target when \(n=3,6,9\). It confirms \(2\) isolated states for \(n=3\), \(265\) states at \(n=6\) and \(133496\) states at \(n=9\), with distances \(6\) and \(10\) at the latter two sizes.

The full infinite-range result is established by the cycle-merger lower bound and composition of fixed small legal templates; no finite experiment is treated as an infinite proof. No independent external audit or expert review is asserted.
