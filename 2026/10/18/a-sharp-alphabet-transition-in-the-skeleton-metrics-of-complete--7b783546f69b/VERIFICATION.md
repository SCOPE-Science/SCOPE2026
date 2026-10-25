---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

With arc-incidence (not projected) coordinates, the union support of two paths decomposes into r maximal mismatch runs and exposes exactly 2^r recombinations; for r=1 it is an edge, while for r>=2 swapping one branch yields x+y=u+v, so no edge. Unique intervals give degree. Sum_{interval} tensor_{i in interval}(J_{n_i}-I_{n_i}) produces each spectrum eigenvalue via constant/orthogonal factors; multiplicities and Kirchhoff tree count follow, including unique zero by single-coordinate adjacency. Binary padded transition count changes by at most 2 per interval toggle, and each run is removable in one step; the even-boundary map identifies classical halved cube. For q>=3 a third symbol at each coordinate gives x-z-y in two steps; disjoint mismatch positions 1 and 3 witness exact diameter 2, k<=2 complete.

## originality

PASS

Rispoli 1992 (as attributed verbatim in Blanchard–De Loera–Louveaux 2020/21 Section 3) already establishes the unique-cycle path-polytope adjacency principle. Classical halved cube metrics/spectrum are known once the binary identification is made. Those components are credited. The specific full arbitrary-layer tensor Laplacian signature, spanning-tree product and sharp uniform q=2 to q>=3 diameter-2 collapse do not follow from a general Hirsch bound or from the different consecutive-layer hypersimplex spectra.

## value

PASS

This is a complete natural family of network-flow polytope skeletons: exact all-layer spectral/tree complexity, plus an unbounded-vs-two metric transition for exponentially many path vertices. The quantitative classification goes beyond quoting generic path adjacency or existing halved-cube formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
