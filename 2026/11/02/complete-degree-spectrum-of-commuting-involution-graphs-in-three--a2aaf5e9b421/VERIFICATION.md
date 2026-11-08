---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For q even and s,t>=2, in the (s,t,1)-block unipotent radical a matrix u(X,y,z)=1+N has order dividing 2 exactly when Xy=0. Two such matrices commute iff Xy_prime=X_prime y; central z,z_prime never affect these relations. For y=0 and rank(X)=a, simultaneous Xy_prime=0 and X_prime y_prime=0 gives q^(st)+(q^(t-a)-1)q^(s(t-1)) compatible (X_prime,y_prime); for nonzero y, split y_prime into its q line multiples and q^t-q outside, yielding q*q^(s(t-1))+(q^t-q)*q^(s(t-2)). Multiply by q^s central choices, remove identity and self loop to get displayed degrees. Counting ordered (y,y_prime) by span ranks 0,1,2 gives exact commuting pair C, and E=(C-3I+2)/2. Independent GF(2),s=t=2 full adjacency counted 111 vertices, 3225 edges, degree multiset {110:3,78:36,62:24,38:48}. All-parameter formulas follow linear algebra, not a sample.

## originality

PASS

The induced commuting-involution graph degree distribution differs from a unipotent radical’s conjugacy-class count, graph diameter, or the total group centralizer order. The relevant primary sources provide these broader but logically different invariants; no complete multiset for all s,t,q was found. Historical originality is qualified against other possible parabolic centralizer literature.

## value

PASS

This is an exact all-parameter degree multiset and edge formula for a natural family of finite nilpotent matrix groups. It reveals rank stratification and uniform nonregularity, a finer invariant than class counts and immediately applicable in group-associated graph theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
