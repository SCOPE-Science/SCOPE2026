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

# Verification

- Executed `python3 check_exact.py` from this package. The verifier uses Python standard-library `fractions.Fraction`, enumerates all four-party two-block residue quadruples with denominators 6, 12, and 18 and sum 2, and independently constructs basic feasible solutions of the full six-outcome marginal linear program.
- It checks all six exact nonnegative lottery weights, sum 1, four prescribed marginals, the predicted expected-inversion minimum, and the predicted probability-of-any-inversion minimum.
- Exact run: 1,398 rational quadruples; all checks passed. The strict example with residues (3/20, 17/20, 1/4, 3/4) also passed, minimum 1/10.
- The all-size two-block reflection law and measure-zero result are proved in `RESULT.md`; no numerical enumeration of continuous quota vectors is claimed.
- Verification does not provide independent scientific certification, priority confirmation or a general result for more than two blocks.
