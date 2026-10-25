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

By polar duality the facets of the real Lipschitz-free unit ball equal vertices of L_n={f(1)=0, |f(i)-f(j)|<=1 when |i-j|<=2}. At a dual vertex active tight edges must connect all n labels (active rank n-1), and a tight spanning tree enforces integer heights. Scanning from left to right, no tight connected component may be abandoned beyond the last two vertices. The six states (increment in {-1,0,1}, last-two joined flag c in {0,1}) completely encode future feasibility; the displayed 6x6 transition T and initial v, terminal w imply F_n=vT^(n-2)w. Exact row identity vT³=vT²+2vT+2v gives recurrence n>=5 and the GF. Independent brute force 2<=n<=11 tested all valid three-valued height increments and directly checked tight-graph connectivity: F=(2,6,12,28,64,144,328,744,1688,3832), matching recursion. Completeness is from boundary-component argument, not finite search.

## originality

PASS

Best-of-knowledge: targeted published finding search and primary-source theorem comparison did not identify a prior result implying the entire final claim; known components are explicitly credited, not counted as novel. All-dimensional exact facet count for the natural squared-path metric by a finite-state tight-graph classification and rational generating function. Unindexed-equivalent risk retained.

## value

PASS

The graph square P_n² has overlapping triangles, a natural first non-tree case for real finite Lipschitz-free spaces and symmetric edge polytopes. Counting all facets in every size by a small transfer automaton is a motivated infinite combinatorial classification, rather than a short finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
