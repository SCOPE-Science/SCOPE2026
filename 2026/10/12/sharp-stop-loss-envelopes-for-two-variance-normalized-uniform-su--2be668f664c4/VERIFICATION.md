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

# Verification of the sharp stop-loss envelopes

The proof in `RESULT.md` is the mathematical basis of the universal formulas: exact convolution, complete partition into central, outer and zero-risk chambers, strictly signed first derivatives, positive second derivative, and exact optimizer admissibility thresholds. Boundary cases \(d=0\), \(d=1\), \(d=\sqrt2\), and strikes \(1/(2\sqrt2)\), \(1/\sqrt5\), \(1/\sqrt3\) are accounted for.

Run `python3 verify_stoploss.py` using Python's standard library. The checks independently calculate positive-part expectations by deterministic integration of convolution densities, verify rational instances against the closed formula, test the chamber derivatives against finite differences, compare global optimizations across strikes with the piecewise formulas, and confirm continuity at all phase boundaries. Numerical tests are not an exhaustive search or an infinite proof. The entire classification requires the analytic inequalities given in `RESULT.md`.

The scientific comparison includes the 2023 uniform-tail paper, the 2003 and 2011 slab papers, and the 2026 general cube-moment method. The older two original slab papers could not be fully inspected; no independent priority audit has been performed.
