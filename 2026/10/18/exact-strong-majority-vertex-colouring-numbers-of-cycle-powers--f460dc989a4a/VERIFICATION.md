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

# Reproduction and limits

Run `python3 verify_cycle_majority.py` with Python 3 and no third-party modules. The verifier constructs the cyclic neighbourhoods from their defining differences, tests each explicit two- and three-colour word, exhaustively enumerates binary words on all tested small noncomplete cycle powers, and compares the exact coprime count. It independently reproduces the exceptional local-junction window lists. The recorded execution returned all assertions successfully.

The infinite-domain claims are established mathematically in `RESULT.md`, by the cyclic shift factorization, the odd-period obstruction, the constructive sign words, and the explicit three-colour interval estimates. Finite enumeration alone does not prove an unrestricted assertion. The complete count of two-colourings outside the coprime subfamily, and every count of three-colourings, are outside the scope of the result. The earlier ordinary-cycle and quartic-circulant subcases are acknowledged.
