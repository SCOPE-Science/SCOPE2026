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

# Reproducibility

Run `python3 verify_rank.py` in the directory containing this file (Python standard library only). The program checks: 1,000 deterministic-seed positive rational-size random allocation profiles satisfying the universal rank upper inequality; tournament instances for ranks 2–5 including height 11 at rank 2; Berge incidence-tree acyclicity via disjoint-set unions; and all assignment recipient pathways in six small tournament configurations, including 32,768 for rank 2 and height 4.

The program must print `ALL TESTS PASSED`. It uses exact `Fraction` arithmetic, not floating-point thresholds, and verifies that every terminal champion has received and been eligible for exactly the height number of jobs.

## Logical scope

These finite computations test the definitions and constructed examples. The theorem for every integer rank and arbitrary finite height is proved in RESULT.md by summing proportional-share contributions and an inductive component-merging argument. Finite testing is neither exhaustive for arbitrary rank nor a substitute for mathematical proof. Independent scientific audit has not been performed.
