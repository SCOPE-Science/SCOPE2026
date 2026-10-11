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

The independent-audit channel has not run. The same-model mathematical review used the exact proof in `RESULT.md` and the executable `verify.py` in this package.

To reproduce, run `python verify.py` with Python 3. The first checks use only the standard library and verify equality between the exact range-extrema volume formula and an independent conditional-extrema integral for all \(1\le p,q\le6\). An optional NumPy/SciPy check reconstructs the polytope as an intersection of halfspaces, enumerates vertices, and compares convex-hull volumes for seven small instances.

The checks passed as packaged: 36 exact-rational comparisons, strict imbalance comparisons for dimensions 4–12, and seven independent small convex-hull volume reconstructions. Finite evidence is corroborative only; it is not an all-parameter certificate. The all-parameter argument is a directly inspectable proof by integration and hyperbolic monotonicity, including boundary cases where a group has size one.
