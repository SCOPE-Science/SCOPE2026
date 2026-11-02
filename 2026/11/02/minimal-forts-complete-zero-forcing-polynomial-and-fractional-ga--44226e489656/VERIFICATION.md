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

Execute `python3 verify.py` using Python 3.9 or newer, with no external dependencies.

The script constructs every edge from the graph definition and exhaustively checks inclusion-minimal forts (direct fort tests over all vertex subsets), standard zero-forcing closures (all initial subsets), formula counts for each size from three through eight, the fort packing maximum by subset dynamic programming through size seven, and vertex incidence/capacity identities of the fractional LP certificate through size eight. The recorded successful execution ended with `VERIFY_OK`.

The finite checks do not imply the statements for arbitrarily large orders; those follow from the proof and the explicit primal-dual argument. This is a reproducible self-review, not an independent mathematical audit.
