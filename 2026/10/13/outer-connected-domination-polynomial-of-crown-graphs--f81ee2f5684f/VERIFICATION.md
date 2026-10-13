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

The proof is symbolic. For reproducibility, `verify.py` constructs \(\operatorname{Cr}_n\), tests domination directly, tests complement connectivity directly, and compares every accepted subset against the closed formula for each \(3\le n\le8\). It also checks the structural domination classifier, the three complement-disconnection types, the minimum-set claims, and the closed total count.

Running `python verify.py` produces:

`VERIFY_OK n_range=3..8 subset_checks=87360 structural_checks=174714 coefficient_checks=72 minimum_checks=6 max_order=16`

The computation does not certify the infinite theorem by extrapolation; the all-\(n\) justification is the case analysis in `RESULT.md`.
