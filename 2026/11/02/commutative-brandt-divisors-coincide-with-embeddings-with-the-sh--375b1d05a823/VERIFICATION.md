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

Run `python3 CHECK.py` using the standard library alone. The expected exact output is stored in `CHECK_OUTPUT.txt`; the last line is `VERIFY_OK`.

The first test enumerates all nonempty multiplication-closed subsets of the five-element aperiodic Brandt semigroup, constructs all set partitions, checks each semigroup congruence and quotient commutativity, and checks a structural predicate on every resulting commutative quotient. It finds 15 nonempty subsemigroups, 39 congruences and 32 commutative congruence quotients (with multiplicity across subsemigroups). It does not infer the infinite theorem by exhaustive testing.

The second test constructs Brandt embeddings for four different group-component configurations and annihilator sizes, then verifies injectivity and all products. The general proof in `RESULT.md`, specifically Steps 1–5, is required for the all-finite-semigroup assertion and the sharp lower bound. No exhaustive search over arbitrary finite structure groups is asserted.

All conclusions were reviewed for mathematical consistency; no independent audit or external formal certification has been performed.
