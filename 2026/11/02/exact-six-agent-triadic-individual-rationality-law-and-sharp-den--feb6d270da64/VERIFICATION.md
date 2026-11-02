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

# Mathematical verification

Run `python3 artifacts/verify.py` from the package root; no third-party Python libraries are needed. The program enumerates the full 15-edge Boolean cube, all ten unordered triple partitions, and a second reachability-based connectedness predicate. It verifies the complete coefficient table `artifacts/multiplicity_coefficients.csv`, the layer binomial totals, exact feasibility and multiplicity counts, the 8-edge isolation criterion, and both 7-edge exceptional isomorphism orbits. The two orbit sizes are 15 and 90. The checker outputs six `PASS` lines on success.

A separate graph-atlas enumeration of all 156 six-vertex unlabeled graphs weighted by their automorphism orbit sizes reproduced all 16 feasibility coefficients. This corroborates the finite count but does not constitute an independent expert audit.

The analytical proof in `RESULT.md` establishes the 8-edge cutoff without relying on computation. The exact finite distribution is certified by exhaustive coverage of the specified finite sample space, not by Monte Carlo. The formulas do not claim any probability distribution under asymmetric or dependent edges, nor do they assert Nash or core stability.
