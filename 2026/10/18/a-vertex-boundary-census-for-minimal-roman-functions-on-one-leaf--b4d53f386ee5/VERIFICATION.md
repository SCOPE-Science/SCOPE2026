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

# Reproducibility and boundaries

Execute `python3 verify.py` using only the Python standard library. The test constructs all 75 labeled base graphs with at most four vertices, checking 425,907 three-label assignments on their coronas by direct Roman feasibility and direct pointwise lowering. It separately checks 597,780 assignments on sunlets with cycle lengths three through six, and 349,504 cyclic words up to length nine. The calculated coefficients are compared to the structural gap expansion and exact cubic recurrence. Exact-integer identities for total counts and the minimum-weight multiplicities are checked through order 24.

The recorded output is in `verification_output.txt`; a successful fresh run ends in `VERIFICATION_OK`. The infinite parameter claims and arbitrary-base identity rely on the written proofs; finite checks do not establish universality or bibliographic originality. Independent validation has not been performed.
