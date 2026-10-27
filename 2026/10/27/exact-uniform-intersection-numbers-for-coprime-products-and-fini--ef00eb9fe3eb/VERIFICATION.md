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

Run `python verify_uniform_intersection.py` using Python 3.10 or later, with no third-party dependencies. The script enumerates complete maximal-subgroup families for sixteen elementary-abelian Sylow profiles, recomputing their intersections rather than using the predicted uniform invariant. It also independently constructs the subgroup lattice of \(S_3\times C_5\) and compares the group and factor invariants. On successful completion it prints `COUNTEREXAMPLE_OK`, `NONABELIAN_COPRIME_OK`, and ends with `VERIFY_OK`.

The enumeration concerns finite displayed examples only. It does not prove the arbitrary-dimension hyperplane count or the unrestricted coprime-product claim; those follow by the arguments in `RESULT.md`. It does not independently certify originality or replace an external mathematical audit.
