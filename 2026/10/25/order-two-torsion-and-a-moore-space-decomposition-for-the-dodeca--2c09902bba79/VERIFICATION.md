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

# Verification

Run `python3 verify_dodeca_perfect.py` using Python 3 and only its standard library. The included `VERIFIER_OUTPUT.txt` records the expected exact output; this is not a substitute for rerunning the source.

The program checks that the 20-vertex, 30-edge cubic graph has precisely 36 perfect matchings, enumerates all 30,503 nonempty faces, pairs 30,462 of them, and performs a complete directed acyclicity test over 163,650 cover incidences. The unmatched cells are one vertex, ten triangles and thirty tetrahedra. The signed Morse boundary from critical tetrahedra to critical triangles is reduced by integral recursion, with binary rank nine, one full 10-by-10 determinant two and a 9-by-9 determinant minus one. These suffice to establish the complete Smith invariant-factor list \(1,1,1,1,1,1,1,1,1,2\) and the homotopy classification of the resulting two/three-cell CW complex.

The combinatorial and arithmetic assertions are exhaustively checked for the specified finite graph only; the reported Morse attaching matrix concerns integral cellular degrees and does not imply any more general family statement. Independent scientific audit has not been performed.
