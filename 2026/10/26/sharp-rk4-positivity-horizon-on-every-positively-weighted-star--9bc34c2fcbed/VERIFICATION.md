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

# Reproducible verification

Install the dependency in `requirements.txt` and run `python verify.py` in this directory. Expected completion line:

`VERIFY_OK 6324 symbolic polynomial and exact rational graph identities, numerical sign spotchecks`

The program checks exact formulas for the graph Laplacian powers, all off-diagonal matrix entries for many positive rational weights, row sums, the normalized derivative-discriminant identity, and numerical sign changes before/after the unique positive threshold. The direct symbolic calculations for three indeterminate weights do not assume the claimed expressions as inputs. Finite sampling is not an exhaustive proof for arbitrary real weights or unbounded star size; the full argument uses the polynomial inequalities in `RESULT.md`. No independent external audit is claimed.
