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

The analytic proof is primary.

`artifacts/verify.py` constructs \(W_{n,m}=K_1\vee nK_m\) directly. It tests the majority condition using open neighborhoods, independently checks the monochromatic-blade structural characterization, and compares the exact number of surjective colorings against the Stirling-number formula.

The exhaustive comparison covers
\[
1\le n\le4,\qquad 2\le m\le3
\]
for every color count in the claimed spectrum. Wider explicit constructions are checked for
\[
1\le n\le30,\qquad 2\le m\le10.
\]

Replay output:

`ALL CHECKS PASSED; parameter_cases=16; surjective_assignments_checked=1597912; construction_cases=2295; exhaustive_n=1..4,m=2..3`

These computations are finite corroboration only. The arbitrary-parameter theorem follows from the exact per-blade inequalities in `RESULT.md`.
