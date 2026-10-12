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

The recurrence and joint-probability identities are proved for every \(0<a<b\), \(0<p<1\), \(0\leq t\leq\min(p,1-p)\), and \(\eta>0\) in `RESULT.md`. The standalone `verify.py` was executed from this package's actual path using Python 3 and completed 2,467 exact-rational checks. It checked all four atoms of the joint distribution, endpoint optimality on both sides of the crossover, exact strict stability classification, the constant derivative sign for the stability frontier, and the rational witness. Finite tests are illustrative and do not constitute an exhaustive proof of the real-parameter theorem. The proof's exact matrix identity and symbolic parameter differentiation establish the universal assertions. Independent audit has not been performed.
