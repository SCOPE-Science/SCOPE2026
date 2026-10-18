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

The mathematical proof establishes the bijection between anti-Lyndon roots and inverse Lyndon words, the correspondence with maximal border lengths, and the exact random-prefix probability. It derives the asymptotic and expected-array formulas without relying on finite experiments.

Run `python3 check.py` to execute exhaustive binary checks up to length 12 and ternary checks up to length 8, including inverse Lyndon recognition from proper suffixes, enumeration by roots, complete maximal-border histograms, and direct array entries versus the exact expression. `verification_output.txt` records the executed output.

Finite computations do not establish infinitely many lengths. Random-array statements concern the uniform iid source; the conditional geometric-border statement uses a different, explicitly defined sampling procedure. Independent audit: not performed.
