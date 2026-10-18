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

## Reproducible checks

Run `python verify.py` using Python 3 and its standard library. The program reconstructs residuals independently from the finite Heyting adjunction, tests the adjunction for every triple, and enumerates materializers for all parameter pairs \(1\le n,k\le5\). It checks the proposed complete membership classifications, their size distribution, the nonzero order isomorphism, and the exact material-implication failure count against exhaustive enumeration.

Observed result: `VERIFY_OK exhaustive_parameter_pairs=25 evaluated_input_pairs=8955`.

The 25 cases are finite diagnostic checks, not a proof for unbounded parameters. The separate general argument in RESULT.md proves the formulas and asymptotics. Literature uniqueness and priority have not been independently validated.
