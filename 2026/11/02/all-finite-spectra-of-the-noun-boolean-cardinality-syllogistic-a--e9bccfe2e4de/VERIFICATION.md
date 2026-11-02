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

# Verification of the mathematical result

The elementary unrestricted proof has four steps: disjoint union preserves every sentence; least representatives modulo the smallest positive spectrum member finitely generate an arbitrary nonempty additive set; pairwise-disjoint and covering inclusion axioms plus two opposite non-strict cardinality inequalities force equinumerous blocks; the two contradictory inclusions realize the empty spectrum on the nonempty-domain convention.

Run `python checker.py` using only Python 3 standard library. Actual completed output: `ALL_CHECKS_OK 23 412071`. The checker compares full assignments of each point to a unique partition block against independently computed multinomial coefficients and positive semigroup membership for generator sets \((2,3)\), \((3,4)\), \((4,7)\), and \((1)\). It also checks specified gaps in the semigroup \(\langle4,7\rangle\). The checker is bounded finite evidence; it is **not** an infinite proof.

The statement's priority is assessed only against identified published material; an equivalent earlier theorem in a broader comparative-cardinality context remains a possibility. No independent audit has been performed.
