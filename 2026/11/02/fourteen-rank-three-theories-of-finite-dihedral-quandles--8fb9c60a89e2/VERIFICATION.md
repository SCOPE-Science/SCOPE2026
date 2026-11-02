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

# Reproducibility and limits

Run `python3 verify.py` with Python's standard library from this directory. The actual recorded output appears in `verification_output.txt` and ends with `VERIFY_OK`.

The verifier directly enumerates all thirty equality/ternary atoms and recursively constructs complete three-round types for each of the fourteen proposed representatives. It separately constructs compressed nine-bit atomic types, checks exact agreement, verifies `type_certificate.json` against recomputation, and checks symbolic pair-key profiles for moduli 9 through 500. The program checks that the fourteen representative signatures are pairwise distinct and each tested stable modulus obeys the stated greatest-common-divisor classification.

The universal statement for all moduli depends on the explicit candidate-residue and overlap proof given in `RESULT.md`: the finite regression tests alone would not prove it. No external or independent mathematical audit is claimed. A published equivalent theorem could exist beyond the sources inspected.
