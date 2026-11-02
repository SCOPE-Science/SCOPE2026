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

The exact finite certificate is `verify_carousel.py`, with its unedited output in `verification_output.txt`. Run `python3 verify_carousel.py` using only Python's standard library. It compares full nested atomic-type structures rather than hashing signatures, and it exhaustively processes every vertex extension, including repeated vertices. It compares all 21 pairs of distinct odd tournament orders from 3 through 15 and checks rank-three exceptions. On orders 3, 5, 7, and 9, a second computation without cyclic normalization agrees exactly with the optimized calculation.

The program's checks on six larger finite orders provide tests, not a proof of the infinite tail. The latter follows from the algebraic antipodal-gap argument, whose critical parity and threshold cases are written out in RESULT.md. No finite extrapolation or external theorem-prover claim is used. The full sentence signatures for all finite orders are not printed, but can be reconstructed deterministically from the included source. The claimed theorem has not undergone independent scientific validation.
