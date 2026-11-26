---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Reconstructed the specified triangle expansion of the Petersen graph and enumerated all nonempty matchings. The face vector is (18,117,335,408,165,8). The 517 toggle pairs give an acyclic orientation of all 3,744 cover incidences on 1,051 faces. The Morse model has one 0-cell and sixteen 3-cells; each 3-cell attaches to the point, proving the ordinary wedge equivalence and free rank-16 third homology. For the flag support bound, minimize the vertex set of an induced subcomplex with nonzero reduced H_d. Deleting any vertex then kills H_d; link–deletion Mayer–Vietoris forces nonzero reduced H_(d−1) in its link. Induction from the disconnected d=0 case gives at least 2d neighbors, and the flag cone criterion forces a nonneighbor. At equality every vertex has exactly one nonneighbor, so the complement is a perfect matching. Applying this with d=3 reduces the census to all eight-edge selections whose intersection graph is four disjoint edges. The exact replay found 63, checked the signed boundary of each 16-term cycle, and checked that integral elimination vanishes on all 165 four-simplex boundaries. The specified sixteen cycle columns have determinant −1, making the induced map H_3 → ℤ^16 surjective and hence an isomorphism; all 63 coordinate vectors have gcd 1. The twelve graph automorphisms form S_3×C_2 with the stated central involution. Their support orbits have sizes (6,12,12,3,12,12,6); the involution fixes three supports and exchanges thirty pairs, including each of the eight basis pairs. Orienting the partners by the involution makes the integral action a sum of eight transpositions. In each block the sum and difference generate an index-two sublattice, giving quotient (ℤ/2)^8. Signed Lefschetz traces independently give 16 on the identity, −2 on the two elements of order three, and zero on the other nine, implying the stated rational decomposition and one-dimensional invariant space.

## originality

PASS

The strongest located overlap is the later Resultary record for the identical ordered graph: it gives the same wedge and rational character. The distinctive contribution of the frozen finding is the complete minimum induced support census and the construction of an integral basis chosen from those supports and exchanged in pairs by the central involution. The same-object comparison and the applicable scope of the inspected broader literature do not cover that contribution. This is a best-of-knowledge assessment, not a priority certification.

## value

PASS

The Tietze graph is a natural triangle expansion of the Petersen graph. Classifying every induced support in the least possible size gives explicit primitive geometric representatives, rather than just an abstract free group. The basis shows that the shortest carriers already generate integrally and can be organized into actual involution pairs. The eigensublattice quotient is usable information about integral symmetry that cannot be recovered from the ranks and rational character alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
