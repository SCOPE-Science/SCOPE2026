---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For m,n>=3 the only distance-3 vertex from a root in A is its matched deleted-edge partner in B; all other opposite-side vertices are distance 1, same-side vertices distance 2. Every last move to a permanently occupied root originates as a 1-,2-, or (once) 3-packet. An A-origin cup not at the root requires a distinct B-origin cup in its final packet, except one 3-packet may carry two A-origin cups, giving m-1 <= n+1_{i<=t}; symmetrically for B. The sharp construction uses a 3-stack at a deleted partner (built from two other A singleton neighbors), then Hall matching of each remaining A cup to a distinct B cup; n-1>=2 handles the small boundary. For unmatched root, direct Hall matching suffices. Checking unmatched opposite-side singleton moves and all distances verifies the construction and indicator total S(m,n,t). Independent analysis of m=5,n=3,t=1 yields only its large-side matched endpoint and all three small-side roots, as stated. The packaged exhaustive small instances support but do not prove the infinite characterization.

## originality

PASS

The target-resolved characterization for K_{m,n} minus an arbitrary matching, with the exceptional eccentricity-3 endpoints and explicit all-target counts, is not supplied by the predecessor complete-multipartite result or Hamiltonicity criterion.

## value

PASS

This gives a natural complete parametric graph-family classification and a sharp boundary effect: deleting even one edge creates an additional stackable eccentricity-three root without making the whole bipartite graph stackable. Such explicit target profiles address a cited eccentricity-three gap, not an arbitrary small graph recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
