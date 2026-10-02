---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-02.md",
      "INDEPENDENT_AUDIT_2026-10-02.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

Independent PARI 2.15.4 replay reconstructs all three BNF structures, verifies their cyclotomic field identities, the exact class-group orders, all six prime-class coordinates and orders, and all three trivial logarithmic class groups. K0/K1 bnfcertify both return 1; K2 remains expressly GRH-conditional. The replay also disproves the auxiliary capitulation sentence: a genuine nonprincipal base-field prime above 7 lifts to class 42 modulo 63, not zero. The old transcript tested an actual unit ideal, so its capitulation inference was invalid. That sentence is removed; the finite S-class vanishing claim is fully reproduced and unaffected.

## originality

PASS

The originally completed exact-object literature and catalogue checks are retained at their actual scope. They found no earlier exact three-layer S-class/decomposition-prime table. The corrected contribution is the finite-layer data only, not a capitulation result or an infinite-level Iwasawa claim.

## value

PASS

The independently reproduced finite S-class vanishing across three cyclotomic layers is a motivated diagnostic for fine Iwasawa questions. The auxiliary false capitulation statement is excluded and no infinite-level deduction is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
