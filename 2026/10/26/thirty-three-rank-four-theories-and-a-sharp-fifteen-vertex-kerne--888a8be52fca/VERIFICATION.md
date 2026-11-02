---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For positive part sizes in the independent-set five-cycle blow-up and pure uncolored adjacency language, the four-move EF game is invariant under size clipping at four: before the kth move each named part has fewer than four occupied clones, so Duplicator can preserve equality and adjacency using unused clones in corresponding parts. The exact recursive quantifier-rank type T_{r+1}=(atomic diagram, set of one-vertex extension T_r types) enumerates all possible moves up to permutations of unused clones. I independently coded this type recurrence (not the repository's verify_c5.py) and enumerated all 4^5=1024 clipped size vectors; recovered exactly 33 distinct rank-four empty-tuple types, class-minimum-size frequencies 5:1,6:1,7:3,8:4,9:7,10:7,11:6,12:2,13:1,15:1, and 3-clipping equivalence for every clipped vector. Combined with the analytic four-clipping, this is exhaustive for all positive sizes, not a finite extrapolation. The unique class needing 15 vertices is all sizes at least three. Reviewed actual RESULT.md, verify_c5.py and Git table presence; computed independent census. Does not apply to named parts, counting quantifiers, empty parts or rank >=5.

## originality

PASS

Exact 33-class FO rank-four classification and optimal 15-vertex representative bound are not contained in inspected extremal pentagon-count and inducibility literature; those use induced subgraphs or flag-algebra labeled types, not FO EF types. Brown–Hoshino treat bare paths and cycles, not independent clone substitutions. Standard EF extension recurrence and four-clipping alone are not claimed original; the nontrivial exhaustive reduced census and sharper three-clipping are assessed additions. A specialized unindexed finite model theory census could overlap.

## value

PASS

An exact elementary-equivalence classification of a widely studied natural graph family establishes a sharp finite kernel for all rank-four sentences without named parts. The further collapse from four to three clones is nontrivial and certifies a precise logical indistinguishability threshold, useful for finite-model descriptive complexity and algorithmic model checking.

The dated certificate retains the supplied scientific assessment, sources and limitations.
