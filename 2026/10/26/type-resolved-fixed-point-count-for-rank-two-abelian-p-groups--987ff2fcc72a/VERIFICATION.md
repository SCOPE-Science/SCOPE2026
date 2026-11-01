---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Every endomorphism is uniquely determined by a,c,beta mod p and d mod p^b, with phi(x)=a x+p^(b-1)c y and phi(y)=beta x+d y; it is invertible iff a and d mod p are units. Pointwise fixing A[p] forces a=1,c=0,d=1 mod p. For delta=d-1 nonzero of valuation r in [1,b-1], the v-coordinate fixed kernel has p^r elements, all divisible by p; the fixed subgroup equals A[p] iff r=1. This contributes p(p-1)p^(b-2)=(p-1)p^(b-1). The delta=0, beta nonzero case contributes p-1 exactly at b=2, while beta=0 fixes too much. Cases exhaust all possibilities including p=2. Independent exhaustive enumeration checked p,b=(2,2),(2,3),(2,4),(3,2),(3,3),(5,2), with counts 3,4,8,8,18,24. The valuation proof establishes the universal result.

## originality

PASS

Prior theta(A,p^2) formulas count automorphisms with fixed-set cardinality p^2, not which subgroup is fixed. The already published Resultary separated-exponent rank-two paper gives theta counts, including a=1,b>=4 and known a=1,b=3, but not the canonical A[p] subgroup multiplicity; its formula cannot be reinterpreted as the same count. Senden classifies occurrence of possible fixed-point numbers, not exact subgroup multiplicities. The 1974 Camina–Collins titled study is plausible but full primary text inaccessible; authorized Oxford attempt returned vpn_disconnected. Qualified best-of-knowledge PASS, not a whole-paper noncoverage claim.

## value

PASS

A[p] is the unique canonical maximal elementary-p-torsion subgroup, so counting automorphisms with exactly that fixed subgroup is a natural refinement of the established theta(A,p^2) invariant. The exact all-prime, all-b formula with exceptional b=2 provides a type-sensitive statistic that cardinality-only tables do not determine. The proof is elementary and scope narrow; the substantive motivation is the fixed-subgroup-type distinction, not computational difficulty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
