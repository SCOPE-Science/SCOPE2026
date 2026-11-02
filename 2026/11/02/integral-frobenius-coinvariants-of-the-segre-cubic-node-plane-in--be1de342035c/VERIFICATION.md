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

# Verification and reproducibility

The accompanying `verify_segre_incidence.py` uses exact integer matrices and `sympy` to reconstruct all 10 node labels, 15 matching-plane labels, and their incidence. Python 3.10 or later and the pinned-minimum dependency in `requirements.txt` suffice.

The program checks the following mathematical statements: each plane has four incident nodes and each node lies on six planes; the integral Gram identity; mod-two rank five; a specified maximal minor of determinant 64; Smith and Hermite indices; the rank of the six-coordinate indicator map modulo two; full equivariance under all 720 permutations of six labels; and the Smith presentation of each Frobenius coinvariant group across all 11 cycle types. The observed terminal conclusion is `VERIFY_OK: all 11 Galois cycle types match the uniform formula`.

The theoretical proof establishes the uniform classification for every finite-field form from these matrix identities and an equivariant mod-two module isomorphism. The script does not independently establish the identification of the Segre cubic's geometric nodes and planes with their classical combinatorial labels; that geometric input comes from the cited literature. No generalizations to characteristics two or three, nor any identification with Picard/Brauer groups, are claimed.

The checks described here are reproducibility evidence and are not an independent scientific audit.
