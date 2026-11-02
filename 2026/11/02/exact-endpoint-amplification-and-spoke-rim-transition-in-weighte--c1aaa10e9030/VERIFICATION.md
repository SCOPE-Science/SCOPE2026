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

# Reproducibility and checked limits
Run `python3 verify.py` beside `RESULT.md` and this file. Only Python standard-library modules are used. The program exactly constructs weighted grounded Laplacians over rational numbers, inverts them, assembles symmetric edge-gradient projections, and checks all spoke and rim absolute row sums against the theorem for 78 parameter profiles. It verifies projection symmetry, trace, selected idempotence, and sample unweighted wheel norms. The recorded result is `VERIFY_OK exact_weighted_profiles=78 graph_sizes=3..15`, followed by an unweighted sample.

The Green recurrence, monotonicity, all-real-parameter crossover uniqueness, and both iterated limits are analytically proved in `RESULT.md`; checking finitely many matrices is not a proof of the infinite families. No independent external scientific audit has been performed.
