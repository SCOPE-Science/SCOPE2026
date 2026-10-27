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
# Verification scope
The inverse branches and derivatives are exact symbolic identities; all \(s\)-limits are on bounded intervals. The critical infinite-dimensional part is a standard uniform full-branch BV Lasota--Yorke estimate (fixed branches, common expansion and BV reciprocal-slope bounds), followed by BV compactness and the disjoint-cylinder variation inequality. No numerical samples can validate that infinite step independently.

# Reproduction
Run `python verify.py` with Python 3 standard library. The script tests structural inverse-branch and profile recursions on samples, and reports passing checks; it does not certify the uniform BV theorem or novelty. The independent audit remains not performed.
