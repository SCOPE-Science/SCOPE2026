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

# Reproducible checks

Run `python verify.py` with any supported standard Python 3 interpreter. The script uses only the standard library, and its result from the saved package is in `verify_output.txt`. It independently constructs the four-state history chain, solves the stationary system, and solves the two hitting-time systems by exact rational Gaussian elimination before comparing with the theorem's formulas. It covers 625 grid quadruples and 400 seeded rational quadruples, including parameters on both sides of the relevant equalities. A deterministic run reports 1,025 passing parameter tuples.

These finite checks verify the formulas at the tested parameters and detect first-hit convention mismatches, but they are not exhaustive over real parameter space and do not certify historical novelty. The analytic proof in `RESULT.md` establishes the identities for every strictly positive parameter quadruple. No independent mathematical review or external certification has been conducted.
