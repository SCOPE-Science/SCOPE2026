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

Run `python verify.py` from this directory after installing the versions of dependencies specified by `requirements.txt`. Only Python standard-library `fractions` and `sympy` are used. The program confirms the algebraic risk derivative and endpoint identities, and it compares independent finite exact path enumeration against moment recurrences for 450 cases. The 101-point numerical grids for six curvature values are supplementary checks, not exhaustive proofs or existence certificates. The sign analysis and affine contraction in `RESULT.md` independently establish the infinite-step assertions.

# Verification limits

No simulation is claimed to certify the uniqueness or sharp threshold. No external independent mathematical audit or computational certification has been performed. The published-paper comparisons are limited to the identified materially inspected sections and available searchable records; broader unindexed priority remains possible.
