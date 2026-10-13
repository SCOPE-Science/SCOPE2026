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

# Reproduction

Execute `python3 verify.py` using the Python standard library. This program creates every matrix over the specified small fields, reduces generator redundancy by scalar shifts, computes the resulting inner derivation on every matrix unit, directly checks composition idempotence, calculates its rank by finite-field elimination, and compares the resulting multiplicity distribution to the closed formula.

The expected final line is `VERIFY_OK`, after six `PASS` lines for the cases \((n,q)=(2,2),(2,3),(2,4),(3,2),(3,3),(4,2)\). The last case yields exactly one rank-zero, 120 rank-six, and 336 rank-eight derivations. The \(q=4\) case uses a declared polynomial basis rather than treating its elements as integers modulo four. Exhaustiveness holds for the enumerated finite matrix spaces only. The theorem for every \(n\) and every prime power is established by the symbolic classification and group-orbit proof in `RESULT.md`, not inferred from the finite tests.

# Limits

The proof and program count \(\mathbb F_q\)-linear associative derivations only. No independent external validation or formal-system certification was performed. Potential equivalence to an older adjoint-operator classification is a residual literature risk.
