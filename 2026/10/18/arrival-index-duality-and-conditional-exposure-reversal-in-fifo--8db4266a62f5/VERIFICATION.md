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

# Verification of the FIFO arrival-index and conditional-exposure theorem

**Proof checks:** The rank equivalence for every index and rank reduces each side to the same condition \(D_{i-k}>A_i+\ell\). Stationarity shifts rank tails. Past/future iid interarrival and mark independence supplies conditional factorization given the tagged sojourn. The unit-service workload staircase is checked separately at the idle atom, away from the integer-null set, and at either side of the contact threshold. The Poisson thinning formula and stationary workload generator establish both risks and the exact marginal. The strict late-time comparison follows from \(-\log(1-p)>\lambda p\); the queue's workload has full positive support beyond its atom.

**Standalone reproduction:** Execute `python3 verify.py` in the same directory (Python 3 and NumPy). The included program passed 1,180,980 exact finite FIFO rank assertions, 40 parameterized conditional-risk inequalities, and a fixed-seed Poisson-queue simulation consistency check. A representative calculation gave analytic common marginal 0.3668051156 and empirical earlier/later risks 0.3666085016 and 0.3666077983. Monte Carlo error is not a defect in an exact identity.

**Limitations:** Finite checks and simulations cannot certify universally quantified claims. The proof is analytic; any novelty assessment compares accessible primary literature and is not an independent priority certification. The conditional-independence and conditional-risk claims require the assumptions specified in RESULT.md, and no exact union-risk or unique sign-crossing claim is made.
