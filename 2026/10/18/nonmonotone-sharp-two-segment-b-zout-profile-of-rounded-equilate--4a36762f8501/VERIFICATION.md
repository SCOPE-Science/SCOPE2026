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

# Reproducibility and verification

The analytical result follows from the triangle width hexagon and two global inequalities, the fixed-radius nonnegative decomposition, equality classification, Steiner area, and a derivative polynomial with one positive root. The script `verify.py` is self-contained and uses only the Python standard library; execute `python3 verify.py` to reproduce numerical cross-checks. Successful execution prints `VERIFY_OK` and the independently computed root and maximum. Random and grid checks corroborate identities but do not certify all directions or radii; the continuum conclusion follows from the written proof. The independent audit status above is deliberately unperformed.
