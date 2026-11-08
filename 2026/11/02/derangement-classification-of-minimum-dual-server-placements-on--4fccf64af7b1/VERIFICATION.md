---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

If a colour occurs in all rows or columns then elementary cover bounds force at least 2n-1 labels; at weight 2n-2 each colour misses at least one row/column. Missing-row/column intersections A×B, C×D force the opposite colour, with A∩C=B∩D=empty. If remaining U,V sizes are u,v, w>=ab+cd+2max(u,v)>=2n-2+|u-v|. Equality gives u=v, ab=a+b-1, cd=c+d-1 and thus the two orientations with bar dimensions (1,s-1,s-1,1) or its complementary orientation; remaining u red and u blue occupied cells form disjoint U-to-V perfect matchings. !u counts the second after choosing the first (u!), and s=2 orientations coincide. Independently computed M_n for n=2..6 as 4,18,320,8450,295272 and brute-checked n=2,3 placements; verified source C++ checker by reading it without treating reported VERIFY_OK as proof.

## originality

PASS

Best-of-knowledge originality survives the actual implication comparisons; cited antecedents cover the foundations or narrower/different objects but none of the accessible material establishes this exact completed statement. Uninspected plausible literature is explicitly treated as residual priority risk, not a proven absence.

## value

PASS

The natural exact minimizer classification and enumerator refine the previously known minimum two-colour domination number on a standard graph family, with a genuinely nontrivial derangement structure and meaningful all-n boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
