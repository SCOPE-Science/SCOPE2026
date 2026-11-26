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

Any two vertices in a layer share a neighbor, and all vertices have degree four, so the graph is connected with a unique bipartition up to swap. Common-neighbor counts recover the rook graph within a layer, and opposite-layer neighbor sets distinguish all nine cells. The 72 rook symmetries lift simultaneously to both layers; the layer flip commutes with them. Proposition 25 supplies reduced homology concentrated in degree 3 with dimension 14. An independent exact calculation (not execution of the supplied checker) enumerated all nonempty bitmasks on the lexicographic 18 triples, discarding masks containing any pair differing in all three coordinates. The face counts by degree were 18,117,348,504,378,192,72,18,2. For each of 144 permutations (independent coordinate permutations, optional coordinate swap, optional layer flip), keep setwise-fixed faces, give each orientation sign by inversion parity on the image list, and subtract their degree-alternating signed sum from 1. Traces at identity, layer flip, coordinate swap and their product were 14,4,-4,-2. Taking the character inner products on the no-swap subgroup confirmed exactly the seven multiplicity-one constituents, and diagonal component exchange traces -1,-2,-1 force minus flips, with the remaining pairs exchanged. Thus the only no-swap invariant line is killed by the swap. For quotient homology, pass to barycentric subdivision so simplex stabilizers fix their simplices pointwise; rational coinvariants compute quotient chains, are exact, and identify with invariants by averaging. The conclusion is about the topological quotient over Q, not its integral homology.

## originality

PASS

The accepted distinction is the combined full automorphism action on H3, notably the separate diagonal exchange signs and the loss of the invariant line in the full quotient. The homotopy type, layer involution trace and dimensions are not distinct contributions. The broader separately permuted coordinate result, even taken without an assumption about historical priority, does not determine the exchange extensions.

## value

PASS

This is the first symmetric case of this three-factor family in which the two non-bipartition coordinates are equal and interchangeable. The full action distinguishes two natural orbit spaces that the known nonequivariant rank and separate-coordinate invariants cannot distinguish: the one invariant class survives without exchange and disappears with it. The explicit full module makes that distinction reusable beyond the quotient Betti number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
