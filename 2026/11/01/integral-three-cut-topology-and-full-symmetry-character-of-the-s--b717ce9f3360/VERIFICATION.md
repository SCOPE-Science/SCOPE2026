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

Run `python3 verify.py certificate.json` in a directory containing these two files, with Python 3 standard library. Compare stdout with `verification_output.txt`. The checker directly reconstructs the Cayley graph and the rook comparator, exhaustively verifies both dual and cut faces, checks the integral boundary-square identities, replays every certificate unit pivot and proves the final residual matrices vanish. It enumerates all 192 full Shrikhande automorphisms and checks their signed traces against independent direct fixed-cut-face Lefschetz sums.

The certificate proves finite exact computations, not publication priority or independent validation. The integral homotopy conclusions additionally use the standard integral Alexander-duality, Hurewicz and Whitehead arguments recorded in RESULT.md. The rational orbit-space conclusion also uses finite-group transfer.
