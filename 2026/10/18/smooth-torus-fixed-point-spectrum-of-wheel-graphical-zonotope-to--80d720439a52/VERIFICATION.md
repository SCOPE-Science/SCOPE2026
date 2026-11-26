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

A maximal chamber corresponds to an acyclic orientation, and each cover edge gives a facet: its endpoints can be tied while keeping all other inequalities strict, by contracting the cover in the DAG. The undirected cover graph remains connected because deleted edges are replaced by paths. With m facets the cover graph is a tree, and its edge roots form an integral basis of the specified root lattice (e.g. eliminate leaves); with more facets the cone is not regular. For mixed spokes, every crossing rim edge is forced from the incoming group to the outgoing group and becomes transitive through the hub. Internal run edges are covers since no directed detour can leave and reenter their group. Only incoming-run sinks and outgoing-run sources give hub covers. The cover count is m−2r plus the number of these extrema, so regularity is exactly one extremum per run. A length-ℓ path supplies ℓ choices, and marking one of r starts of an incoming run accounts for m/r. The two uniform-spoke strata each have 2m directed Hamiltonian-path shortcuts; no other uniform-spoke chamber can have only m covers. The two factors of 1−R(z)^2 give the stated Lucas and cosine terms. Independently, the two-letter transfer matrix with diagonal 2 and off-diagonal 1 counts 3^m+1 rim assignments for all spoke words, before the four uniform-spoke directed rim cycles are excluded. Thus the denominator is 3^m−3, including m=3, and the leading exponential rate follows. Scope is fixed points and arbitrary algebraically closed base field. The finite reachability checker was inspected, not executed, and is not used for the proof.

## originality

PASS

The supported distinct contribution is the explicit wheel enumeration with the incoming-spoke refinement, not the tree-poset criterion or the all-orientation total. A distinct later-dated indexed wheel result gives exactly the smooth total and uses the same underlying run-weight method; this is equivalent coverage of the total formula, not a separate corroboration of priority. The compared result does not give the incoming-spoke distribution.

## value

PASS

The family is natural and nonsimple from m=4 onward. Counting lattice-regular chambers is not a consequence of the global nonsimplicity flag or an ordinary face count. The precise incoming-spoke distribution retains the hub's order relation to rim vertices, yielding a motivated refinement, while its sum quantifies exponential rarity. This does not claim to describe nonfixed smooth or singular orbits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
