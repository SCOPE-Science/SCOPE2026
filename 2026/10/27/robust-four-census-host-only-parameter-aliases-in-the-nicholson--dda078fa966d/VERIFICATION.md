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

Run `python3 verify_alias.py` using Python 3 standard library. The program checks both exact-parameter trajectories through the fourth and fifth host counts; the analytically derived fifth-census ratio; root residuals and derivative identities at reproduction multipliers 2 and 4; and 500 reproducible small perturbations of the host ratios that each retain two distinct positive parameter reconstructions. The script prints PASS only after all assertions succeed.

The decisive infinite-family evidence is analytical, not the finite script: exact recurrence substitution proves the shared first four host counts; the nonzero derivative at each compatibility root plus the implicit function theorem proves the open set. Numerical root-finding is not used to infer uniqueness of all compatible roots or any result about longer data sequences.
