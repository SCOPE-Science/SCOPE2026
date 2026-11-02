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

# Verification and reproducibility

The independently replayable script `verify_directed_ring.py` uses exact rational arithmetic for the finite covariance recurrences and leader-placement enumeration; its optional numerical integration uses SciPy. Run it with a standard Python interpreter and SciPy installed.

Observed output: `PASS {'lyapunov_blocks': 33, 'leader_sets': 6105, 'optimum_sets': 1365, 'critical_checks': 16}`.

The exact test checks the Lyapunov equation entry by entry for gains \(1/3\), \(3/5\), and \(1\) and lengths zero through ten. It enumerates all leader subsets for rings of sizes two through ten, compares their exact variance totals against the balanced formula, and verifies that all and only balanced subsets are minimizers, including their count. It also checks strict discrete convexity through length 101, the critical closed form, and 16 finite-size numerical convergence comparisons using sizes 500, 2000, and 8000.

These computations do not certify an infinite statement. The proof in `RESULT.md` establishes the nilpotent matrix integral, strict convexity, optimizer count and the two limiting regimes without relying on sampling or a numerical solver. Small numerical checks use ordinary floating-point and are not interval certificates. Self-review only; no independent external review or certification was performed.
