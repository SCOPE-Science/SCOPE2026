---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the finite mathematical certificate

Run `python3 desargues_checker.py morse_certificate.json` with the two supplied files in the same directory. The checker uses only the Python 3 standard library and returns `DESARGUES_ALL_SCALES_MORSE_AND_240_CHARACTERS_OK` on success.

The checker regenerates the graph from subset incidence, all graph distances, all 260 scale-two and 3,200 scale-three nonempty simplices, and verifies that the matching certificates partition these face posets into pairs plus the stated critical cells. Every matched pair must consist of adjacent dimensions, every face is used exactly once, and the reversed-matched Hasse diagram is exhaustively tested for directed cycles. These checks are proofs for the finite mathematical objects, because every possible face and edge of the directed Hasse diagram is considered.

Exact signed Lefschetz contributions of each fixed simplex are calculated for all 240 natural graph automorphisms and compared against the explicit irreducible-character formulas in RESULT.md. The cross-polytope determinant computation supplies scale four; the graph-cycle count supplies scale one. The resulting homotopy type controls integral torsion, and distinct homology degrees across scales control persistence maps.

The certificate does not establish equivariant homotopy equivalences, infinite-family generalizations, or publication priority. Independent audit: not performed.
