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
The theorem is proved symbolically in `RESULT.md`. The finite program `verify.py` is a separate regression check of the formulas used in the proof.

Run:

`python3 verify.py`

Saved output:

`VERIFY_OK`

`limit=300000`

`composite_cases=274002`

`minimum_defect=290`

`unique_minimizer=4`

`squarefree_composite_minimum=2653`

`nonsquarefree_composite_minimum=290`

`branch_bound_violations=0`

The finite range does not prove an infinite statement. The infinite proof uses only the exact prime-factor identities, the bounds \(x\ge6\) on squarefree composites and \(x\ge2,y\ge1\) on nonsquarefree composites, and monotonicity of the explicit polynomial lower bound.
