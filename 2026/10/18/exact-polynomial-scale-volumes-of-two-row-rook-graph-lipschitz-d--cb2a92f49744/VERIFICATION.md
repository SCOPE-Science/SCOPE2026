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

# Verification of the exact volume formula

Run `python3 checker.py` with the standard Python library. It constructs the integer-point enumerator for the scaled unit-edge two-row rook Lipschitz polytope directly from the inequalities. One clique is anchored at its first vertex; the other clique is counted by the exact partition according to its minimum coordinate. For each dimension \(d=2n-1\), the finite difference of order \(d\) of the lattice-point counts at dilations \(0,1,\ldots,d\), divided by \(d!\), recovers the lattice-normalized ordinary anchored-coordinate volume. Total unimodularity of the incidence-difference inequalities guarantees an integral polytope and hence an Ehrhart polynomial.

Successful exact rational comparisons: \(n=2\) gave \(16/3\), \(n=3\) gave \(49/5\), \(n=4\) gave \(534/35\), and \(n=5\) gave \(5443/252\). The scale sets contained 4, 6, 8, and 10 lattice counts, respectively. The checker was run successfully against the actual packaged code before embedding. This is an independent computational route to four finite cases, not a proof of the theorem for arbitrary \(n\). The all-dimensional result relies on the analytic decomposition and integration in RESULT.md; its asymptotic relies on a separate Laplace estimate.
