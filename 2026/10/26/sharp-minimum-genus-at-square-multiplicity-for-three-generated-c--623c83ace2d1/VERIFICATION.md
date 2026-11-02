---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For a three-generated CI gluing S=<qa,qb,p>, gcd(a,b)=gcd(p,q)=1, q>=2, a<b, p nonminimal in <a,b>, the Frobenius number is q(ab-a-b)+(q-1)p and the multiplicity is min(qa,p). Because ab-a-b>=a^2-a-1, if qa=m=s^2 then p>=m+1 gives F>=m(a+q-2)-1>=2m(s-1)-1 by AM–GM, equality only a=q=s,b=s+1,p=m+1. If p=m<qa, q>s^2/a implies a strict improvement over the same target; for a=s integer q>=s+1 yields strict inequality. The candidate p=s^2+1=(s-1)s+(s+1) is legal and achieves F=2s^2(s-1)-1; CI symmetry gives g=(F+1)/2. Independent finite gluing search confirmed uniqueness for s=2..6; those tests are not the universal proof.

## originality

PASS

Best-of-knowledge original for the restricted final claim after direct implication-based comparison; primary overlap, unavailable full text and mathematical reduction risks are explicitly documented, not treated as absence-proof.

## value

PASS

This closes an explicit infinite fixed-embedding-dimension slice of the minimum-genus problem for complete intersections, including uniqueness, and distinguishes it from generic semigroup genera and mere realizability. It is not a renaming of a two-generator formula: the gluing parameters require optimized global inequalities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
