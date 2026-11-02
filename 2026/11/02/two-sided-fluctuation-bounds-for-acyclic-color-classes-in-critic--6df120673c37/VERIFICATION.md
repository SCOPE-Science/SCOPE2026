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

Run `python check.py` with a standard-library Python 3 interpreter in the same directory as this file. The command performs complete enumeration of \(s^{{s^2}}\) equally likely edge labelings for \(s=2\) and \(s=3\), counting directed cycles using depth-first search and the resulting missing-color counts. `check_output.txt` contains the resulting exact distribution, exact first two moments, pairwise covariance assertions, exact loop-occupancy lower bounds, and sample moment-generating inequalities. The executed checker completed successfully with its final `VERIFICATION_OK` line.

The two-neighbor digraph is the complete directed graph on \(s\) vertices, including self-loops; every ordered pair is a separate directed edge. For \(s=2\), the computed missing-count variance is \(15/64\) and the loop conditional lower bound is \(9/64\). For \(s=3\), the respective values are \(14396210/43046721\) and \(6396416/43046721\).

**Analytical checks.** The general statements rest on the explicit one-hot negative-association argument, independent-block closure, shared-monotonicity of the missing-color maps, exact conditioning on self-loop labels, and the published one-color asymptotic \(q_s\sim c_*s^{-1/3}\). The occupancy count's variance follows by two-bin joint vacancy probabilities. The almost-sure assertion follows from a summable Chernoff upper bound and Borel--Cantelli, without assumptions on coupling across sizes.

**Limits.** Exhaustive checking of two finite state sizes does not certify any statement quantified over all sizes. The numeric Airy constant is cited, not independently evaluated or rigorously enclosed by the checker. No exact variance asymptotic, central limit theorem, or independent expert review is asserted.
