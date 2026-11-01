---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

For each n>=2 the geometric K-fixed points of the matching complex are exactly convex combinations with equal barycentric coefficients on K-edge orbits; the explicit barycenters of the individually admissible orbit-matchings triangulate that locus PL. A vertical-edge orbit contains both vertically adjacent edges in a column, so is forbidden. Horizontal orbits split into nonconflicting outer-row and central-row families. Column reversal yields q=n/2 or q=(n-3)/2 permitted orbits per family for even or odd n, and within each family precisely consecutive orbit indices conflict. Hence the full fixed orbit complex is Ind(P_q disjoint union P_q); q=0 at n=3 gives the empty realization, whereas n=2 gives a simplex. The elementary two-contractible-piece cover gives Ind(P_q) ~= suspension Ind(P_(q-3)), with initial q=1,2,3 cases. Joining two path complexes supplies the claimed integral sphere dimensions or contractibility, with the first sphere occurring q>=2 and arbitrarily high dimensions. An independent reconstruction of all reflection-edge orbits and conflicts agrees for n=2..24. These bounded tests do not prove all widths or integral topology.

## originality

PASS

Existing same-graph work gives ambient nonequivariant connectivity, row/column individual Lefschetz numbers, and the half-turn plus whole-quotient Euler characteristic; these scalar invariants do not determine the common K-fixed-space PL model or homotopy. The two reflected horizontal families in prior orbit counts are known; the extra simultaneous column action and conflict-path reconstruction are the claimed structural refinement. Best of knowledge with close-prior-work and access caveats.

## value

PASS

The actual common fixed-point space of two commuting involutions is a natural equivariant-topology invariant, stronger than a Lefschetz scalar. A canonical PL identification for every grid width yields full integral homotopy, an empty exceptional case, and an unbounded sequence of genuine fixed spheres despite highly connected ambient matching complexes. This is an interpretable structural family result, not a re-tabulation of alternating traces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
