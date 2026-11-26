---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

In the direct product a diagonal pair leaves at most the two cross-corners unobserved. An observed vertex in a third row and one of the pair's columns sees only the missing corner in the other column, so both corners can be forced. A set meeting two rows and columns contains a diagonal pair: a pair in different rows either already works or shares a column, and a vertex in another column forms a diagonal pair with at least one of them. Two or more vertices in a single row initially observe every vertex outside that row; if u vertices of the row remain, each outside vertex sees u or u-1 of them. Thus u>=3 stalls and u<=2 succeeds. The column case is symmetric. A singleton leaves a cross of unobserved vertices; its observed neighbors each see m+n-4 of them and no force is possible. Subtracting the empty set, singletons and disjoint row/column failures gives the coefficient formula; diagonal pairs and the applicable length-four fibers give the two-sensor count. The top degree is mn and the last deficit is max(m,n)-3, also for 4x4, yielding the unordered factors. Independent sequential-forcing replay matched all 2,162,688 subsets on 4x4, 4x5 and 5x4; checked all fiber placements plus sampled subsets on 5x6 and 8x6.

## originality

PASS

The strongest indexed overlap gives the exact same structure and polynomial on a larger parameter range and implies factor recovery on the reviewed range. It is indexed after the frozen record, not evidence of antecedent coverage. The inspected earlier primary literature gives known power-domination polynomial machinery, zero-forcing equivalences or scalar parameters, not this complete-family enumerator. The originality judgment credits the earlier-indexed classification and enumerator only on the supported evidence, not factor recovery as an independent advance over a source already giving the same polynomial.

## value

PASS

The exact placement classification sharpens minimum sensor number to describe all successful placements and the precise obstructions at every cardinality. Its polynomial distinguishes factor pairs of equal vertex count, while the coefficient deficits expose where all placements become successful. The structural classification is the main value; factor recovery is a useful consequence, not a separate difficult theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
