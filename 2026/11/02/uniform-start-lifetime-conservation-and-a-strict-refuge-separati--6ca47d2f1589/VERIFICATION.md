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

# Reproducible checks and their limits

Run `python verify_refuges.py` with Python 3. No third-party libraries are required. The program uses exact rational Gaussian elimination and independently constructs the killed generator for each separation. It checks every admissible separation for cycle lengths from four through ten, two distinct positive rational migration/mortality pairs, and three positive rational Laplace arguments. In total, 138 exact rational resolvent comparisons passed. The program compares direct moments and transforms against the rank-two resolvent formula and checks the hyperbolic Green representation numerically against exact rational inverse entries; it also checks the exact six-site benchmark fractions.

The proof, not the finite program, supplies the statement for arbitrarily large cycles and arbitrary positive rates. It proves positive definiteness, the conservation identity and the strictly decreasing Green kernel analytically. A full external independent audit has not been performed. The code checks do not imply any general stochastic-dominance relation, any conclusion under asymmetric migration, or a claim about real metapopulation extinction.
