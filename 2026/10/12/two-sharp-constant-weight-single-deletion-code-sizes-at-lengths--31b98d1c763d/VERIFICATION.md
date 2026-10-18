---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Binary code words have length n, weight exactly three, and pairwise disjoint sets of distinct length-(n-1) one-symbol deletion outputs. Verified n14 witness 32 supports and n15 witness 37 supports from actual Git witnesses.json by independently generating full binary strings and all single-coordinate deletion outputs; no pair intersects (174 distinct outputs at n14; 205 at n15). For every of C(14,3)=364 and C(15,3)=455 possible input words, independently tested a weighted shadow certificate u_m: each weight-two output gets weight 1 plus 1 for adjacent ones, with an additional unit on (13,14) if m=14; each contiguous weight-three output starting odd at 1,3,5,7,9,11 gets weight 1; all others 0. The sum across distinct outputs is >=3 for every candidate; total shadow weights 96 at m13 and 111 at m14. Disjoint deletion balls imply 3|C|<=96/111 and bounds 32/37. This is a finite *complete* proof for these lengths, not extrapolation to other n. The original verifier source and witnesses were inspected, not trusted solely via its VERIFY_OK string.

## originality

PASS

The 2023 Hagiwara–Nation draft Theorem 11/Table 3 gives matching upper bounds but only 31 and 35 lower bounds at n14/15 and explicitly leaves these rows unresolved. This package supplies the missing size-32/37 lower witnesses plus an independent weighted packing proof. Semantic database hits for ternary deletion codes at much shorter lengths do not cover constant weight 3 binary cases. No later covering codebook was found, with residual unindexed-construction risk.

## value

PASS

Closes two explicitly unsolved natural entries in a published coding-theory bounds table, with reproducible concrete extremal codebooks and an independently checkable dual-weight certificate. Exact finite optimum is scientifically valuable even absent a general n formula or all-maximizers classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
