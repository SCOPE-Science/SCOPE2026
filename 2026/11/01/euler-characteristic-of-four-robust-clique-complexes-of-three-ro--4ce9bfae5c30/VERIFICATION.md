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

# Verification record
The Python standard-library transfer program reconstructs the full 54-state, 260-transition automaton and verifies the exact integer identity \(A(A-I)^4\mathbf1=0\) coordinate-by-coordinate; the fourth-difference consequence applies to every integer width. It checks the four initial signed face counts and separately propagates signed counts for widths 1–30.

A second program uses an independent recursive maximum-independent-set oracle over all \(2^{3n}\) selected vertex subsets at widths 2–6. The signed sums are 0, 4, 20, 56, and 120 in increasing width, matching the theorem. These finite direct checks do not replace the all-width matrix identity.

Only Euler characteristics are certified here; homotopy-type conjectures and integral homology remain unproved. Independent audit has not been performed.
