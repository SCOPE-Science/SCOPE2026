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

From actual Git RESULT.md blob 3770ffeb, the distance formulas are exact on H_n: same-side distinct vertices distance 2, opposite-side distance 1 for i<=j and 3 otherwise. For W with p A-landmarks and q B-landmarks, omitted A/B vertices have 2-multiplicities p/q respectively and side-specific cumulative 1-counts. There are at most q+1 and p+1 such counts, proving |W|>=n-1. At equality, prefix/suffix inequalities force x1=0, y_n=0 and x_{k+1}+y_k=1 for all k<n. This gives exactly the 2^(n-1) shifted-pair choices; omitted cross-side vertices collide iff p=q, the odd-n balanced case. Independent exhaustive direct distance-multiset checker for n=2,3,4,5 yielded basis counts 2,2,8,10, exactly the formula. These checks are finite corroboration; the prefix argument proves all n>=2.

## originality

PASS

Statement-level best-of-knowledge comparison found no stronger prior theorem implying the complete final claim; source-specific exclusions and reading limits documented.

## value

PASS

Exact minimum and EVERY basis of a canonical nested-neighborhood graph, including the parity obstruction specific to discarding landmark identities. Researchers needing specific outer-multiset resolvers or basis counts can use the exact structural classification, not merely a numerical sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
