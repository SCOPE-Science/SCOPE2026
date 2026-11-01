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

# Reproduction and proof boundaries
Run `python3 check_mycie.py` after extracting the embedded checker. It requires only the Python standard library and outputs `PASS 108 orbit graphs, 18 homology cases, 8 signed swap character checks` when all assertions succeed. It constructs the actual generalized Mycielskian from its edge relations and reconstructs orbit graphs, independently calculates selected reduced mod-two homology, and evaluates signed fixed-face sums under the involution. The general proof is the explicit averaging homotopy and all-parameter orbit classification in `RESULT.md`; a finite computation is not an infinite proof. The sources and potential novelty limitations are disclosed in `RESULT.md` and `REVIEW.md`. Independent audit was not performed.
