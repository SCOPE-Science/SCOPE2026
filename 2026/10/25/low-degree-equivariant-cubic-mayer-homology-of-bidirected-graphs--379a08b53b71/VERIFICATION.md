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

The proof is contained in `RESULT.md`. The standalone `verify_mayer.py` was run from this package with Python 3; it passed 26 graph/field combinations. It builds full nonregular word boundaries rather than applying path regularization, computes admissible-chain constraints and matrix ranks, and separately checks the rank of the **second** boundary out of degree two. The tests span paths, stars, even and odd chordless cycles, and the Petersen graph over primes seven and thirteen.

The finite computations do not establish an infinite-family theorem over the complex numbers; the uniform argument in `RESULT.md` provides that proof. Degrees at least four and independent scientific review remain unchecked.
