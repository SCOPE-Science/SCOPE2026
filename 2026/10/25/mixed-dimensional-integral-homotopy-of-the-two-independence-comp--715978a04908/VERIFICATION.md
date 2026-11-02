---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

PASS: Exact full 2^16 subset enumeration gives f=(16,120,464,964,960,440,80,10)=3054 nonempty faces, using selected-degree≤1 predicate. An independently implemented 16-pivot matching verified all 1517 pairs, 20 critical cells (one vertex, 17 three-cells, two four-cells), and all 13,568 face-incidence arrows topologically sorted with no cycle. Independent integral Morse reduction gave ∂4(4741)=e33285−e36869+e36870, ∂4(6181)=−e33285+e36869−e36870, a primitive pair of opposite degree vectors. An integer basis change among 17 S3 kills one by a degree-1 four-cell, and the second attaches nullhomotopically, yielding 16 S3 plus S4. Compared with actual certificate.json and source verifier; no extrapolation beyond Q4.

## originality

PASS

PASS best-of-knowledge: Full published Q4 ordinary independence Ind_1 result has only 742 nonempty faces and wedge^7 S3, not this higher-independence condition. Deshpande–Singh primary theorem covers certain complete multipartite, whiskered, cycle and tree graph families, not Q4; Sawant 2026 result is on trees, which Q4 is not. Resultary semantic search found different Q4 cut/Čech/neighborhood objects, no matching Ind_2(Q4) mixed-dimensional homotopy calculation. Risk of an uncatalogued finite computation remains.

## value

PASS

PASS: A naturally motivated higher-independence invariant of the smallest nontrivial 4D Boolean cube; an exact integral mixed-dimensional homotopy wedge is more informative than field Betti ranks. The presence of one S4 next to sixteen S3 is a specific structural datum useful in higher-independence graph-complex benchmarks without requiring an all-dimension theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
