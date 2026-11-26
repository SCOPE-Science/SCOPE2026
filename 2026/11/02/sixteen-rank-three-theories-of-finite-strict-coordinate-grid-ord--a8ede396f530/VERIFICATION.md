---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In a linear-order game with t moves left, gaps either match below 2^t−1 or both meet that threshold. Playing the two coordinate games simultaneously clips each side at seven and preserves selected-pair equality and both strict inequalities, hence their conjunction, including plays with a repeated coordinate or pair. Terminal diagrams with all three variables and the iterated sets of extensions encode exactly three-round equivalence, not counts of responses. The independent replay `python3 audit-evidence/strict_grids.py` checked all 28 clipped unordered grids and matched equality of types iff equality of the claimed keys. Only the clipped (7,7) grid has its type, so any member of that class has both sides at least seven. This proves the sharp 49-point bound; the replay does not itself prove the infinite reduction.

## originality

PASS

Credit only the exact rank-three partition in the strict-coordinate signature and the sharp lower bound on representative size; the coordinatewise upper bound and tensor-product method are existing consequences. The closest concrete table is in the reflexive product signature, not this one. Its unsourced reference to a previously reported strict classification is residual overlap risk, not independent evidence of a distinct covering record.

## value

PASS

The strict dominance order is a natural two-chain tensor product. Exact equivalence and least representatives at rank three resolve which size information is lost when the coordinate orders cannot be named. The table removes twelve of the 28 candidates left by composition and proves that the worst-case 49-point cap cannot be improved; neither is a routine restatement of the preceding bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
