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

# Computational verification

Run `python3 verify_halfturn.py` using Python 3.8 or later; no external libraries or downloaded datasets are required. Exact integer arithmetic checks an explicit eight-state polynomial identity \(T^8-T^7+2T^6+T^4=0\), as well as the first eight coefficients of each parity-specific series. Because the identity annihilates all later coefficients of the claimed denominator, this is a finite exact verification of the matrix-generating-function step rather than extrapolation from numerical examples.

The script additionally derives the graph involution from the original three-row hexagonal-strip edges, tests fifteen quotient orbit graphs against a separately constructed canonical graph, enumerates invariant faces directly for five strip lengths, and verifies 239 transfer terms. These corroborate the combinatorial reduction; their bounded ranges do not prove the unrestricted graph model, whose proof is written in RESULT.md.

The expected complete stdout is stored in `verification_output.txt`. The exact script shipped with the result produced that output. No independence, external validation, or formal proof certification is claimed.
