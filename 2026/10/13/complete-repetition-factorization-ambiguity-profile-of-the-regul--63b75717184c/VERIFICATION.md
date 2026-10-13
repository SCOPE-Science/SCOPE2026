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

Run `python3 verify.py` beside `catalog.json` and `certificate.json`.

The first engine reconstructs the regular paperfolding word from its four-letter \(2\)-uniform morphism. It verifies exact equality of every source factor set of lengths \(1\) through \(45\) at substitution levels \(9\) and \(10\). Because a target factor of length at most \(45\) depends on a source factor of length at most \(23\) and one alignment bit, this equality is an inductive stabilization certificate for the complete bounded factor language.

Every binary factor in the coded language is then tested directly for all periods up to half its length. Dynamic programming enumerates every cut composition whose blocks are repetitions.

A second engine generates \(65536\) bits from the independent odd-part formula and checks the same factor sets through length \(45\). The recomputed exact catalogue must match `catalog.json` record by record.

The published global theorem that any paperfolding factor admitting a repetition factorization has length at most \(45\) converts this bounded exact census into the complete infinite-word classification.

Independent audit has not been performed.
