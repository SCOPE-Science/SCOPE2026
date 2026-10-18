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

The source `check_unary.py` constructs complete four-tuple truth tables for the positive and full unary modal term algebras of every labeled two-world Kripke frame. It independently checks the semantic monotonicity filter, the precise three failing relation masks, and the positive-simulation countermodel for representatives \(7\) and \(15\). It additionally covers both one-world relations.

The source `check_unary_independent.py` uses an eight-bit representation and a separate saturation procedure. It computes all sixteen instances and reproduces every positive, full, and monotone operation count. Both programs terminated successfully and printed their PASS marker when run with Python 3.

Completeness is guaranteed by the proof that there are exactly \(256\) possible unary truth tables on the four valuations and that the closure operators realize precisely the two formula grammars. Enumerating formula strings to a fixed depth would not supply that guarantee; the supplied computation instead reaches fixed points.

For the two obstructing isomorphism types, an additional noncomputational proof uses a directed positive simulation and the explicit formula \(\Diamond p\wedge(\Box p\vee\neg p)\). The simulation has three related pairs and satisfies the atomic, forth, and back clauses. The result does not extend to additional propositional variables or larger world sets. Reproducible computation is not an independent audit.
