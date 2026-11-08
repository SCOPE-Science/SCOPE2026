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

The source defines a distinct-descendant incidence matrix from 128 binary 7-words to 32 binary 5-words, avoiding multiplicity overcount from coincident deletion patterns. Every certificate row supplies a codebook C_L and dual weights y_v>=0,z_w>=0 satisfying sum_{v in D(w)} y_v+z_w>=1 for all 128 source words, yielding the weak-dual bound |C|<=L sum_v y_v+sum_w z_w. In an independent BigInt rational computation directly from frozen certificates.json blob 2ae3d..., all 6×128 inequalities and all nonnegativity checks passed; all listed codebooks are distinct of sizes 5,11,16,21,26,32 and each of 32 received words obeys the list limit. Objectives were exactly 256/45, 666/59, 452/27, 1160/53, 1430/53 and 2340/73; each is strictly below the next integer. Thus lower and upper bounds coincide; a complete FINITE certificate covers the entire stated domain (not any longer block length).

## originality

PASS

Best-knowledge PASS: exact natural finite-block list-size spectrum and explicit rational certificates, not the familiar LP incidence formulation. The directly relevant Kiah–Wei–Zeng preprint now has a November 1, 2026 v2 with a changed title and gives run-counting finite-length upper bounds and asymptotic coding rates, not the six-value n=7 exact classification in inspected material. Earlier n=6,L=2 published exact 7-word result is separate. Residual risk: an unindexed short-block capacity table.

## value

PASS

Maximizing block-code size at fixed length, deletions, and list size is a standard, naturally parameterized coding invariant. The exact six-entry profile identifies how decoding-list relaxation changes attainable cardinality, with complete independently checkable witnesses/covering certificates; useful as a small-block benchmark even without asymptotic rate improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
