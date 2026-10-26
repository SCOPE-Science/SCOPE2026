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
Execute `python3 verify_rook_dissociation.py` using Python 3.8+ with no third-party libraries. The script defines the rook graph by common-row/common-column adjacency, tests every subset for induced maximum degree at most one, and tests maximality by all one-vertex extensions. It independently constructs the component-count polynomial and checks every coefficient on 11 boards: 1,419,088 tested subsets in total. It additionally checks the proven extrema on 735 more board parameter pairs using exact-integer sums. The accompanying `verify_output.txt` records the observed coefficients and passing assertions. These finite computations corroborate but do not certify the infinite mathematical proof. No independent external audit has been performed.
