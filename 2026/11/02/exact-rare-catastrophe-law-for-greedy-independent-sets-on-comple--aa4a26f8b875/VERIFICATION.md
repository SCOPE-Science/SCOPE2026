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

# Verification of the finite graph law

Run `python check_greedy_c4free.py` using Python 3.9 or later and no external packages. The checker constructs a direct stochastic recurrence on all currently eligible vertex subsets, independent of the conditional first-two-arrival proof, and compares every labeled output-set probability with the claimed exact formula. It includes the cases of deleted perfect matchings, regular missing cycles of different lengths and disconnected unions, and the seven-point projective-plane incidence graph. One eight-vertex case independently enumerates all `8!` permutations. A four-cycle-containing missing-edge graph serves as a negative-hypothesis control.

The checked execution printed `PASS 441 independent exact checks`; all claimed atom probabilities, means and variances matched rational arithmetic exactly. Computation is finite and is not an exhaustive proof over all possible graph orders. The proof itself is a support argument plus explicit conditional-priority computations, followed by a degree count and a projective-plane construction. The independent audit was not performed.
