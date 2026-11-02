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

The standalone `verify.py` uses exact integers and fractions to enumerate all 152 permutations of memory lengths for periods two through five. It checks the finite necessary-and-sufficient criterion justified by the stabilized-image lemma, compares the full successful sets against the two stated cyclic-rotation families, and separately checks companion-matrix block evolution for every pattern.

Executed result:

`VERIFY_OK permutations=152 counts=2,3,4,10 noncyclic_first=5 multiplier=24 matrix_checked=yes`

The theorem for unbounded indices follows from the matrix proof and the recurrence induction, not from finite forward sampling alone. The program does not certify priority or replace independent mathematical audit.
