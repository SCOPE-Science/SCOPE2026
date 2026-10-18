---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For 1/sqrt(15)<=a<alpha, s=sqrt(1+a^2), q=4as, u=sqrt(q-1), the explicitly displayed P=(0,u-a) satisfies the lower and upper horizontal Cassinian constraints and the two vertical ones: the latter are sqrt(q(q-4a(u-a)))<=q<4s. Every three-corner triple has product 8as=2q. For r=a/s>=1/4, the squared ratio for (A,C,P) equals (1+r-sqrt(r^2+4r-1))/(1-r^2), strictly above 1 iff (r-1)((r+1)^3-2)>0, i.e. r<2^(1/3)-1; squaring is sign-safe. The increasing a->r mapping yields the exact interval and witness equality at its upper endpoint. Independent SymPy polynomial check and exact a=69/260 (s=269/260,r=69/269) reproduce strict ratio 1.020645150198... . This proves only a particular triple lower bound, not the exact global three-diameter.

## originality

PASS

Source question 6.2 asks whether all Cassinian Reuleaux rectangles have constant 3-diameter; theorem 6.1 handles the square. The new result establishes a sharp explicit opposite-corner/diagonal-midpoint obstruction to the square corner-value certificate on an interval. No equivalent witness inequality was located in targeted semantic index and public searches. This is NOT a negative answer to constant 3-diameter itself, and the possibility of another previously unindexed witness remains a residual risk.

## value

PASS

A sharp explicit counter-obstruction to transferring the corner-controlled square 3-diameter proof to a naturally posed one-parameter rectangle family isolates a mathematically meaningful boundary in a live geometric question. The narrower comparison is useful even without resolving the global constant-3-diameter question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
