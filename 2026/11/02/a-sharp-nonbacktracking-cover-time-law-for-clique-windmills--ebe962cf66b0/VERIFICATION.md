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

# Verification notes

Run `python3 verify_windmill.py` using Python 3's standard library. This solves exact absorbing-chain linear equations over rational numbers and compares independently derived single-petal avoidance probabilities with the claimed formulas for simple and nonbacktracking walks. It reports `PASS 114 exact rational checks` for petal sizes 2 through 7. The \(m=2\) tests are boundary checks only, not an assertion that the new asymptotic theorem is original at that size.

Run `python3 simulate_windmill.py` for a reproducible seeded finite-sample illustration on clique windmills with \(m=3,4\). It simulates the true nonbacktracking rule at the hub and at outer vertices. Asymptotic convergence is established in `RESULT.md` by conditional marked-set hazard bounds, factorial-moment convergence, renewal-time concentration and expectation estimates, not by finite simulation.

The completed mathematical review covers the stated hypotheses and limitations. External independent audit and independent computational verification are not represented as performed.
