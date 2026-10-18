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

The standard-library verifier `verify_frame_bounds.py` executes exact rational checks for 27 integer sizes \(2\le m\le28\), a boundary eigenvector, and five interior rational phases per size. It checks 1,091 instances, including full tridiagonal LDL pivot positivity and independently evaluated Walnut overlap sums. Execute `python3 verify_frame_bounds.py` from a directory containing this file and the standalone program; the expected output is supplied as `verify_frame_bounds_output.txt`. The mathematical generality for unbounded integer \(m\) comes from the displayed algebraic quadratic-form proof, not the finite checks.

No independent audit or external formal proof certificate is represented here.
