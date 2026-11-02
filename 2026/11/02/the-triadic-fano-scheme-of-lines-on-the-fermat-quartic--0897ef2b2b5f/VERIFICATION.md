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

Run `python3 verify_fermat_quartic_fano.py` using Python 3 standard library only; the expected final line is `FERMAT_QUARTIC_MIXED_CHAR_48_64_FROBENIUS_8_28_AND_MOD9_PASS`.

The program enumerates exactly 7462 row-reduced two-dimensional subspaces of \(\mathbb F_9^4\), verifies that 112 satisfy the Hermitian conditions, partitions these into 48 pairing and 64 additional lines, and enumerates the full 1536-element monomial group orbit. It verifies exactly eight Frobenius-fixed additional lines and zero Frobenius-fixed pairing lines, and computes the rank-four Hilbert tangent matrix at every one of the 112 special lines. The exact polynomial identity at the additional representative line and the coefficient modulo nine are checked using integer arithmetic; the proof explains why no first-order deformation can cancel this coefficient.

The complete relative-scheme classification is proved in RESULT.md using a smooth-quartic normal-bundle argument, properness/quasifiniteness, Hensel lifting, and Nakayama. Finite tests alone do not prove completeness over an algebraic closure or over all Artin thickenings. Historical priority is subject to the sources and residual risks documented in AUDIT.json. No independent external validation has been performed.
