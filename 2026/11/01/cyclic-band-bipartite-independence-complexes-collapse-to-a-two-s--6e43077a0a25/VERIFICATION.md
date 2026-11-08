---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Taking complements turns the bipartite independence complex into a clique complex with two full pure vertex cliques and mixed edges a_i b_(i+q), q=0..t-1. Adding a layer s>=3 creates new edge e=(a_i,b_(i+s-1)); n>=2s-1 prevents wraparound and its common-neighbor link is exactly two cliques A_1..A_(s-1) and B_0..B_(s-2) with cross-adjacency r<=q, independent of previously inserted same-layer edges. Each A_r (r>=2) is dominated by A_1, and after removing them each B_q (q<=s-3) is dominated by B_(s-2); link collapses via codimension-one pairs to an edge and then to a vertex. Lifting link pairs by union with e removes only new faces; each is a genuine free codimension-one face, so the enlarged whole complex collapses to its pre-insertion complex. Ferrers link has (s+1)2^(s-2) faces including empty, yielding (s+1)2^(s-3) pairs per new edge; summing n times over s=3..t gives n(t2^(t-2)-2), with t=2 an empty sum. Exact pure-simplex and mixed-annulus face counting gives 2^(n+1)-1+nt2^(t-1). For t=2, the mixed strip is an annulus capped along both boundary cycles by the full a and b simplices, hence homotopy S2. Replayed the inspected full package checker from its Git-SHA-verified bytes: for all n=3..11 in the specified range it reconstructs actual complete face sets and verifies every free-face pair and final remainder. This is finite support only; the Ferrers link argument proves all stable parameters.

## originality

PASS

A bounded comparison of precise mathematical statements and implications finds no identified earlier theorem covering the full new claim; known special cases and foundational tools are acknowledged; inaccessible source scopes and possible hidden prior art are explicitly residual risks.

## value

PASS

Deleting consecutive matchings from a complete bipartite graph is a natural structured graph operation. A uniform explicit strong simplicial collapse onto a fixed two-sphere homotopy type throughout a two-parameter stable range, together with exact pair and face counts, is stronger and more useful than an Euler-characteristic observation or a random small-parameter census. It gives a direct constructive topological simplification of a family whose complexes grow exponentially.

The dated certificate retains the supplied scientific assessment, sources and limitations.
