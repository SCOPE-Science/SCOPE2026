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

Quantifier-rank recursion uses the SET of atomic third-vertex extensions of each ordered pair, then the set of these pair types at a chosen first vertex, then the realized first-vertex types. Vertex transitivity makes the last set a singleton. Equality cases are forced by the pair's atomic data, and the reflection interchanging the endpoints makes the two mixed extensions occur together. With L=2k+1, s=n−L, d≤floor(n/2), the two arcs give t=(L−d)_++(d−s)_+. For d<L this is L−min(d,s): the mixed count is min(d,s) for adjacent pairs and min(d,s)−1 otherwise; the neither count is s−min(d,s), and the common count is t−2 on adjacent pairs and t otherwise. For k≥2 adjacent pairs always have a common neighbor. Nonadjacent pairs with d<L have a common neighbor, and their mixed and neither counts change at s=1 and d=s respectively. When d≥L the bound d≤n/2 forces s≥d, giving t=0, mixed count L−1, and neither count s−L. These give all boundaries: s=0,1,2…k,k+1,k+2…2k,L,≥L+1, and direct substitution at k=1 gives the five ordinary-cycle rows. The resulting signatures are all distinct and minimizing n in each exact regime gives the listed representatives, with 11 first attained in class K. Independent bounded replay `python3 /workspace/audit-work/finite_checks.py` constructs pattern sets directly for 3≤n≤39 and gives the eleven expected minima. The infinite result relies on the symbolic inequalities, not the replay.

## originality

PASS

The already covered ordinary-cycle portion and the standard type recursion are not credited as new. The complete unrooted two-parameter classification for cycle powers and the sharp representative order are supported as distinct from the strongest inspected results, to the best of current evidence.

## value

PASS

This computes a natural logical invariant uniformly over two unbounded parameters, isolates the boundary and mixed-extension effects that cause class changes, and proves sharp representative order within the family. The complete exact classification can be used in place of separate three-round comparisons and is not just a bounded table of trial graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
