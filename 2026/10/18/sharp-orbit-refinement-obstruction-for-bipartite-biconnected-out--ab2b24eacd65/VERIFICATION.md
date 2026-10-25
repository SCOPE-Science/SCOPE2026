---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

A biconnected simple outerplanar graph has a unique outer Hamiltonian cycle, reducing isomorphism to dihedral equivalence of noncrossing polygon diagonals; bipartiteness forces even order and opposite parity endpoints. Double-counting bounded-face boundary length gives c<=n/2−2 chords, so enumeration of all admissible noncrossing diagonal subsets for even n<=12 is exhaustive. A fresh independent exact enumeration gives (labelled dissections, dihedral classes, failures) (1,1,0),(4,2,0),(21,4,0),(126,13,0),(818,48,1) for n=4,6,8,10,12; the sole failure is chords (0,3),(6,9). Its equitable degree classes are sizes 4 and 8 versus three four-point dihedral automorphism orbits. For odd ell=2h+1, four degree-three hubs and h distance shells form an equitable partition; successive refinement distinguishes shells in exactly h strict rounds, and the chord-matching stabilizer has order four splitting each shell into two size-four orbits. Independently recomputed exact small n and ell=3..21 selected points, including automorphism counts. The infinite h theorem follows from shell and symmetry structure, not finite checks.

## originality

PASS

The older outerplanar graph-isomorphism count and abstract colour-refinement theory are prerequisites, not the exact first failure nor the unbounded orbit-colour deficit construction.

## value

PASS

Uniform counting colour refinement approximates automorphism orbit partitions, and the first failure within the natural bipartite 2-connected outerplanar family is a meaningful extremal boundary. The theorem proves uniqueness at 12 by a complete justified census and exposes an unbounded quantitative gap and exact refinement depth along a natural two-chord family. This structural witness is useful for testing symmetry-sensitive graph algorithms and is not an arbitrary enumeration of 48 graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
