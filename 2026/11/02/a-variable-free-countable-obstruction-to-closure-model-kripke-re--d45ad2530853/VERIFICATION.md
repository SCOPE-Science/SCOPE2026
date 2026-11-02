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

# Verification and limitations

The proof is symbolic: each natural-number world uses the specified finite Kripke row, and the exceptional generator uses the cofinite filter. The inductive calculation \(\Box^k\bot\) isolates the initial segment of length \(k\), so the derived \(\delta_j\) isolate every integer \(j\). The cofinite complements rule out every ordinary world from the common generator core; \(\neg\Box\chi_0\) rules out the exceptional world. This forces an empty core despite \(\bot\notin G(z)\), contradicting Kripke representability. Eventual constancy provides a Kripke realization separately for each finite family of modal observations.

The standalone `checker.py` implements symbolic finite prefixes plus an eventual-truth bit; it is not a formal infinite proof. Running `python3 checker.py` yielded `ALL_CHECKS_OK`, with 101 point-isolating formulas, 1000 random modal terms and 52 finite blocks checked. No external data or packages are required.

Interpretation is in the classical Boolean modal language with a constant false proposition and a box operator. Arbitrary propositional letters are permitted, but assigned false everywhere. The separating formulas use none of them. The theorem concerns same-carrier, same-valuation representations and does not address representations after adding worlds.
