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

# Verification of the exact rational projection certificate

The companion standalone \`CHECK.py\` runs on standard Python 3 without external packages. Execute \`python3 CHECK.py\` in this directory. The successful execution performed 2,919 exact-rational assertions and printed \`SHARP_NORM 845/659\`. It verified both biorthogonality conditions, idempotence and all five equal absolute row sums of the candidate projection, the signed involution's action on the two spanning vectors, and the exact coefficients of the universal three-class lower certificate. It also checked the block-extension projections at each integer dimension from 3 through 12.

The script's finite dimension range and coefficient samples are illustrative checks, not exhaustive tests or infinite proofs. For arbitrary dimension and all possible competing projections, the certified mathematical reasoning is the analytic direct-sum reduction and the explicit nonnegative rational lower certificate in RESULT.md. The calculation does not verify absence of equivalent prior literature or provide independent mathematical validation.
