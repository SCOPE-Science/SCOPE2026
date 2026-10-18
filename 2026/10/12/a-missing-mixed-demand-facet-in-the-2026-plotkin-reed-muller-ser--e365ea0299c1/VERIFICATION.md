---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The actual RESULT.md at blob fa95a2c4d1e64a1dd477084ec54ebf7f4b35a07b defines the unit-capacity flow region for columns (1,x) in F_2^(m+1). The unique column (1,0,...,0) receives dual weight 3, other 2^m-1 columns weight 1; any recovery set for the first object has odd size and weighted cost >=3, any recovery for other objects has positive even size and cost >=2. This proves 3 lambda_1+2sum_{i>=2}lambda_i <=2^m+2 for all m. The claimed 2026 enlarged outer region contains (a,b,0,...), a=(2^m+2)/3, b=(2^m-4)/6>0 for m>=3, but its dual cost excess is 2b. The 2020 exact theorem supplies achievability of the two-facet corrected region under k=m+1 coordinate relabel. Exact rational checks performed for m=3,4,5,8 confirm violations; they do not replace the infinite symbolic proof.

## originality

PASS

PASS for source-specific 2026 correction, not for the already published exact RM region: the 2020 complete theorem includes the allegedly omitted facet but cannot itself diagnose a specific future misstatement. Search results have not identified a prior public diagnosis of v1. Full 2026 v1/v2 text was inaccessible; this is a high-priority corroboration risk.

## value

PASS

Correcting the full simultaneous-demand region of a standard storage code removes an entire infeasible family, while preserving correct individual maxima. The independent weighted-capacity certificate localizes the error and has mathematical/operational motivation beyond cosmetic restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
