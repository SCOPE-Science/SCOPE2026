---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Independently enumerated all 65,535 nonempty edge subsets of K_{4,4}, retaining precisely the 7,342 sets with all four row and all four column degrees at most two. The face vector is (16,120,528,1428,2304,2040,816,90). Independently replayed the stated 16-edge toggle order, obtaining 3,663 disjoint face-poset pairs, one critical vertex, fifteen critical 5-faces, and zero other critical faces. Oriented all 37,728 nonempty-face Hasse covers and completely topologically sorted the 7,342-node directed graph; it is acyclic. Forman discrete Morse therefore yields a CW complex with only one 0-cell and fifteen 5-cells. All attaching maps S^4->point are null, so the asserted integral wedge homotopy type follows. Boundary ranks and the saved certificate are corroborative, not substituted for this complete acyclicity certificate. No assertion about larger K_{n,n} or equivariant action.

## originality

PASS

This precise bounded-degree chessboard-with-multiplicities homotopy type is not implied by the located general Singh theorems: (m,n,r)=(4,4,2) meets neither m>r>=n nor r=n-1. Exact neighboring M_2(K_{3,4}) and M_2(K_{3,5}) homotopy facts do not extend by monotonicity to a change of graph. Reiner–Roberts supplies rational-homology information, not the complete integral wedge homotopy equivalence; Vega treats other graph families. Published finding searches under all principal aliases did not locate another claim of the exact K_{4,4} wedge type. Best-of-knowledge only; unpublished computations remain a risk.

## value

PASS

The first balanced complete-bipartite degree-two case outside Singh’s balanced r=n-1 sphere family has a natural topological invariant, and the computation upgrades potentially known rational homology to a complete integral homotopy type. The explicit finite acyclic certificate resolves a mathematically nontrivial canonical missing case, not an arbitrary numerical slice; no general n result is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
