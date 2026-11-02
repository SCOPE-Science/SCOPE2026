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

# Reproducibility and scope of checks

Run `python verify.py` using Python 3.10 or newer; no external packages or network connections are needed. The script constructs the coefficient profiles, builds actual parent-pointer rooted trees, checks the resulting distances and weight identities at exact rational viscosity values, verifies sign patterns through four polynomial families, and checks an explicit grid-avoidance polynomial. It also enumerates all 1,441 labeled acyclic parent-choice forests with at most five vertices, checking 55 level signatures and their strict-interior weighted voting breakpoints using rational Sturm sequences. The executable program was run successfully from its packaged path before delivery.

The theoretical implications for arbitrary degrees and arbitrary finite grids are proved in RESULT.md; the finite computation does not certify all infinite instances, publication priority, or unexamined decision rules. The endpoint and tie conventions are part of the proved assumptions. External independent validation has not been performed.
