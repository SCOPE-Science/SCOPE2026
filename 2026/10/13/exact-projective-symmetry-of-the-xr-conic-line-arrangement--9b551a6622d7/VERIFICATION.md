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

Run `python3 verify.py` from the directory containing the packaged files.

The verifier uses only exact `fractions.Fraction` arithmetic. It reconstructs all projectivities preserving the six line components from projective four-point frames, verifies that the line skeleton has exactly \(24\) symmetries and the stated four triple-concurrency classes, filters those symmetries by exact transport of the six conic quadratic forms, checks that exactly \(6\) survive, verifies the \(S_3\) generator relations, and checks the component and added-line orbits.

A successful run prints `VERIFY_OK`, `line_stabilizer_order=24`, `arrangement_stabilizer_order=6`, and `group=S3`.

The computation proves only the projective stabilizer of the displayed arrangement and the symmetry consequences for the two source addition examples. It does not classify all possible lines that can be added while retaining freeness or plus-one generatedness.
