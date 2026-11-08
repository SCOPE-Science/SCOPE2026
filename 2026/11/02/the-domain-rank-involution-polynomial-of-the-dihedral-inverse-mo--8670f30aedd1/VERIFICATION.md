---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For n≥3 an involutive partial dihedral restriction g|A must preserve A and satisfy g²|A=id. A rotation other than identity/half-turn has no nonempty fixed points of its square, so all nonidentity cases extend reflections or the even-n half-turn. A global involution with f fixed vertices and t transpositions contributes (1+z)^f(1+z²)^t invariant subsets; subtract partial identities. Distinct reflections never coincide on a nonidentity restriction; on even n=2h the half-turn agrees with a reflection only on one of h antipodal swapped two-point domains, giving correction −h z² and no higher collisions. This derives both odd/even formulas and first coefficients 1,n,n(n−1). At z=1, the nonidempotent count is O(n 2^(n/2)) versus 2^n identities; mixture bound yields total-variation distance O(n 2^(−n/2)) from Binomial(n,1/2). Independent deduplicated partial-map enumeration for n=3..9 reproduced involution totals 14,31,62,125,226,439,782 and every polynomial coefficient; the uniform proof is group-orbit classification, not finite induction.

## originality

PASS

Qualified PASS for the complete parity-dependent involution domain-rank polynomial and asymptotic binomial law. The monoid identification, cardinality/presentation and even antipodal rank-two nonunique extension lemma are already explicit in Fernandes–Paulista and credited.

## value

PASS

Self-inverse elements and their domain-rank distribution are natural invariants of an inverse semigroup. The exact even-cycle antipodal overlap and exponentially dominant partial identities clarify structural combinatorics and give a natural asymptotic distribution beyond established monoid cardinality/generator ranks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
