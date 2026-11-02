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

# Verification and boundaries

Run `python3 check_tree_choice.py` with a standard Python 3 interpreter; no network or third-party package is needed. The recorded execution produced `PASS 3481 exact and analytic consistency assertions`. Full-tree Bellman checks explicitly enumerate every ordered offered-neighbor tuple for small complete trees, use rational numbers, and verify both the normalization of offer probabilities and the resulting radial value equation. Additional rational recurrences check exact first two moments and the gambler's-ruin success probabilities at bounded sizes. The general-integer threshold follows from coprimality, rather than an enumeration.

The CLT and exponential law hold for fixed integer branching and fixed integer offers with height tending to infinity. The accompanying exact tests are finite checks only: the proof supplies the unbounded-time coupling, Lyapunov argument, and renewal-Laplace expansion. The limiting Gaussian variance is strictly positive and the outward rare-event mean is positive. There is no independent audit or external certification of mathematical correctness or historical novelty.
