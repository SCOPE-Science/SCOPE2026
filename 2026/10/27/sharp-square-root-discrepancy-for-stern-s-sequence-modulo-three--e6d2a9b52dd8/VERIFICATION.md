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

Run `python3 verify.py` in a standard Python 3 environment. This program derives all eight states from the update maps, evaluates the exact characteristic polynomial using integer Newton identities, verifies the squarefree annihilator matrix identity, and directly enumerates Stern terms below \(2^{17}\). For each covered dyadic level it verifies the stated recurrence and the equality of state counts in three classes. It also independently checks all \(131072\) initial-prefix counts against a loose square-root bound.

A matrix computation on eight states is an exact finite identity because the matrix contains *all* possible residue states. The derivation from its spectrum to arbitrary unbounded prefixes and the nonvanishing lower limsup is in the mathematical proof, not inferred from computational sampling. The finite-prefix checks test the implementation but are not substitutes for those arguments. No external independent audit has been carried out.
