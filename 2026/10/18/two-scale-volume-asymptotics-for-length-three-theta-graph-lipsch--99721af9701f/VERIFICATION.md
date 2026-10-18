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

# Reproducibility

The proof in `RESULT.md` is self-contained. The exact comparison below uses a different route from the displayed integral: counting integer anchored potentials on the graph for every integer dilation, then extracting the Ehrhart leading coefficient using finite differences. This is valid because an oriented vertex-edge incidence matrix with one base vertex removed is totally unimodular; its signed inequality duplicates preserve this property, so all vertices of the unit graph-Lipschitz ball are integral.

Run `python3 artifacts/verify.py` after extracting the complete file set while keeping relative paths. Python's standard library alone suffices. The executable reconstructs the arm counts by direct integer enumeration, multiplies them across independent arms only after conditioning on the common hub, evaluates the finite difference, and compares against the explicit rational integral.

Observed output included `PASS: 7 Ehrhart volumes; 19 exact strict log-convexity checks; 20 upper-ratio checks`. Dimensions checked were \(3,5,7,9,11,13,15\), with exact volumes \(8,88/5,1536/35,12128/105,72320/231,865152/1001,1727488/715\). These finite computations test normalization and algebra, while the analytic derivation establishes all integer \(m\ge3\) and the asymptotic limits.

No independent external mathematical audit was performed. A search for equivalent formulations in primary literature and mathematical research records is necessarily nonexhaustive.
