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
The exact checker independently reproduces the released search order and separately computes minimum lengths by increasing the number of summands from two through five. It verifies equality of returned and minimum lengths for every integer from 24 through 49, then verifies the first mismatch at 50. It also verifies the shorter four-term decomposition of 512550.

Limits: this certificate does not verify all repository CSV rows, does not test values above 50 for the first-mismatch assertion, and does not address the truth of the global at-most-five conjecture.
