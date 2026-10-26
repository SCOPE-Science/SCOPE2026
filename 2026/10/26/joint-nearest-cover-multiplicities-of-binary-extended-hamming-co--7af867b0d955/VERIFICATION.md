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

# Reproducible verification

Run `python3 check_joint.py` with Python 3 and no third-party dependencies. The program uses exact integer arithmetic, generates every correction up to the proved maximum joint support, computes its syndrome directly from the explicit parity-check columns, and groups results by the actual minimum weight and number of minimizers. It then checks both rank/parity classification and the exact counts against the formulas.

The checked pairs are \((m,t)=(2,1),(2,2),(2,3),(3,1),(3,2),(3,3),(4,1),(4,2)\), covering \(4096\) syndromes in the largest syndrome space tested. The \((3,3)\) test enumerates \(188{,}707\) weight-bounded correction patterns. The output file `verification_output.txt` is the recorded stdout from replaying this exact program, ending in `EXACT_JOINT_LEADERS_VERIFY_OK`.

These computations are finite checks. The all-parameter assertion follows from the affine-basis proof in `RESULT.md`, not by extrapolation from tests. Independent mathematical or priority validation has not been performed.
