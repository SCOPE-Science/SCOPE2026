---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Writing T(e1)=(u,v), T(e2)=(w,z), orthogonality implies uw=vz=0 because det A != 0. If nonzero images of both basis vectors were proportional in rank one, their squares vanish and the surjectivity of the square span E^2=E forces T=0: impossible. Thus rank-one maps kill one basis vector. If e2 is killed, c=0 and x^2=x; the x=0 branch yields y=a/d and T^2=0, the x=1 branch is the quadratic d y^2-a y+b=0 with T^2=T. Symmetric for e1 killed; b=c=0 gives 6 maps. Over F_q, each triangular family has (q-1)^2(q-1) matrices; root incidences per family (q-1)^2(q-2); counting the diagonal case gives each rank-one type 2q(q-1)^2. Monomial invertible matrices contribute G+(q-1)^2(q-s+r), s=gcd(2,q-1), r=gcd(3,q-1); adding G zero maps plus singular maps yields 2G+(q-1)^2(5q-s+r). Independent brute equations over GF(2),GF(3),GF(4),GF(5) yielded respective (idempotent,nilpotent,automorphisms,total)=(4,4,8,22),(24,24,56,152),(72,72,234,558),(160,160,544,1344). Finite checks corroborate the exact arbitrary-field and all-prime-power algebraic derivation, not replace it.

## originality

PASS

Automorphism and isomorphism classifications were prior; the reviewed theorem singles out all noninvertible endomorphisms, their idempotent/nilpotent dichotomy, labeled incidence distributions and full pair census for every finite field. Closely read the 20-page 2022 isomorphism paper and Sriwongsa–Zou automorphism part. Neither claims the noninvertible fibers. A nonindexed classification of endomorphism semigroups remains a genuine priority risk.

## value

PASS

The noninvertible portion of a natural finite-dimensional algebra endomorphism monoid is structurally important, and the equality of global retraction/square-zero counts in every characteristic is a concrete nontrivial exact arithmetic invariant rather than a parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
