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

Run `python3 unicyclic_rank_check.py` from the extracted package directory. It requires Python 3 standard library only. The program independently constructs all matchings to compute the predicted combinatorial polynomial, then enumerates finite-field matrix entries and computes ranks by Gaussian elimination, using an explicit finite-field multiplication for \(\mathbb F_4\). It exhaustively verifies six specified unicyclic graphs over fields with 2, 3 and 4 elements (18 configurations), and verifies \(\sum_j[z^j]R_G(q,z)=q^{|E|}\) each time. The final expected marker is `UNICYCLIC_SKEW_RANK_CORRECTION_OK 18`.

The source-independent mathematical proof is in RESULT.md. Enumerations over three small fields are not a proof over arbitrary finite fields or arbitrary unicyclic graphs. The character-degree consequence follows the classical odd-characteristic class-two orbit method; it was checked arithmetically for a cycle with a two-edge pendant path in characteristic three. No independent mathematical audit has been performed.
