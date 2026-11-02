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

The recurrence and first-hitting formula are proved for all integers \(s\ge2\) and all real \(\delta\in(0,1)\) in `RESULT.md`. The standalone `verifier.py` independently reconstructs leaf-first updates using exact rational numbers and checks 82,953 eligible parameter pairs through denominator 80 and star size 30. It also exhausts all vertex update orders in 27 small rational parameter instances for the random-permutation deactivation formula.

These are finite reproducibility tests, not a replacement for universal algebraic arguments. The explicit random asynchronous absorption bound is certified by an event of positive probability in independent fixed-length chunks; no empirical stochastic tail estimate is used. No independent audit has been performed.

Reproduce with `python verifier.py` using Python 3 and its standard library.
