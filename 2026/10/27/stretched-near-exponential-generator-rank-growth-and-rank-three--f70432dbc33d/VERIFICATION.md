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

# Verification of finite orbit data

Run `python3 checker.py` in the directory containing this file. The executable uses exact integers and the Euler-transform logarithmic derivative recurrence, without external packages. It checks partition factors, two-cycle factors, and the multiset transform to degree \(40\), including the rank-three and essential rank-two orbits and minimal generator counts. Representative comparisons include \(m(5)=35\), \(m(10)=2880\), \(m(20)=10998182\) and \(m(40)=30328785627967\).

The expected terminal marker is `VERIFY_OK formal Euler factors and rank3 dominance, n<= 40`. The finite table does **not** establish the asymptotic statements. The rigorous upper estimate uses absolute convergence, Euler-product inequalities and Cauchy's coefficient bound; the lower estimate uses an explicit pigeonhole family of unlabelled two-cycles, with exact equal-size padding. The distinction between labeled objects and conjugacy orbits is necessary. No independent audit or external certification has been performed.
