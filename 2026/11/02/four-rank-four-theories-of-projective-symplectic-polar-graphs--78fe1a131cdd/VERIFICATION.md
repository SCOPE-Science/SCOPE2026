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
The accompanying `verify_polar.py` uses only the Python standard library and evaluates atomic-extension profiles for projective symplectic graphs in eight finite parameter cases. The output `verify_output.txt` records every tested graph order and the 28 pairwise decisions.

The supplementary `separator_check.py`, which imports `verify_polar.py`, directly tests both distinguishing rank-four properties on five small models; `separator_output.txt` records successful results. The executable checks verify the finite cases only. The uniform algebraic argument in `RESULT.md`, including the surjectivity and exceptional missing-fiber analysis, is required for the infinite statement. No external or independent mathematical validation was performed.
