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

# Reproducible checks

Run `python3 forest_type_check.py` with a standard Python 3 interpreter. The checker independently constructs all \((n+1)\)-element comparison matrices for assignments of a new point as below, above or incomparable with each named parameter, and counts those satisfying transitivity. It compares that count to the subtree formula for all recursive-parent encodings through six vertices. The checker also evaluates each of three explicit families for sizes one through eight.

The recorded run passed 874 forest configurations plus 24 closed-form example cases. These are finite checks and are not a substitute for the proof for arbitrary \(n\). Every computation is deterministic, no third-party dependencies are required, and no external verification has been claimed.
