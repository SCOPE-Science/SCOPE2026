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

# Verification notes

Execute `python3 verification.py` with Python 3 and standard library only. The program enumerates all length-\(n\) words in the indicated bounded parameter ranges and uses the first letter together with exact directed bigram multiplicities as a complete \(2\)-abelian signature. It verifies that every distinct-letter run chain is singleton and that their counts equal \(q!\binom{n-1}{q-1}\), plus the published binary/ternary singleton formulas for applicable lengths.

Finite enumeration does **not** establish asymptotic bounds for arbitrary \(n\). The infinite proof instead uses the cited finite-type decomposition and no-outside-occurrence lemma. The verifier has no external inputs and no dependencies.
