---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Identify the universal flag triangulation with the equilateral triangular tiling with increments (1,0),(0,1),(1,1), and deck lattice L={(a,b):a+3b=0 mod 13}; the quotient has precisely 13 vertices,39 edges,26 triangles, no 4-cliques, so the tiling is the genuine universal cover of a torus. Graph displacement length is ell(a,b)=max(|a|,|b|,|a-b|), from coordinate lower bounds and explicit shortest step decomposition. Exact enumeration of all L displacements ell<=4 gives only +/- (4,3), +/-(3,-1), +/-(1,4), no nontrivial shorter. Their geodesic words have 3 edges of one type and 1 other, giving 13 unoriented cycles per class. All 39 remaining 4-cycles bound elementary two-triangle rhombi indexed by graph edges. Exact separate enumeration confirmed total 78 four-cycles and histogram 39 trivial plus 13 each of 3 directions. Multiplication by 3 lifts as (a,b)->(-b,a-b), translation acts trivially on deck displacements, and -3 acts on basis A=(4,3),B=(3,-1) by [[0,-1],[1,1]]; group transitivity follows. Counting covers only 4-cycles and unit combinatorial metric, not smooth/longer loops.

## originality

PASS

Published T_{13,1,3} and its Paley torus affine symmetries are already known; the counted integral essential 4-cycle carriers and explicit action on their primitive homology classes were not found in the actually inspected primary comparisons. Resultary's nearby one-direction T_{n,1,3} theorem explicitly assumes n>=17, hence does not cover n=13. This is a bounded best-of-knowledge scientific judgment: an unsuccessful search cannot prove absolute priority.

## value

PASS

A canonical smallest flag cyclic torus and Paley graph has a complete shortest nontrivial homology carrier census, including multiplicities and symmetry action; it distinguishes null rhombi from essential directions in a natural minimal triangulation and provides exact systolic benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
