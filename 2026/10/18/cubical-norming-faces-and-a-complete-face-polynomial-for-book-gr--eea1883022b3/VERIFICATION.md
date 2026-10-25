---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For book graph B_m=K_2 join independent m leaves, f(u)=0 identifies dual Q_m with |b|<=1, |x_i|<=1, |x_i-b|<=1. Exposing functional s b+sum a_i x_i, positive/negative total leaf coefficients P,N and k zero entries yield exact piecewise maximized support sum|a_i|+b(s-N) on 0<=b<=1 and sum|a_i|+b(s+P) on -1<=b<=0. For a!=0 the five mutually exhaustive regimes s>N, s=N, -P<s<N, s=-P, s<-P give three singleton-hub k-cubes and two interval-hub (k+1)-cubes. Case a=0 gives two m-cubical hub facets and for s=0 whole ball only. Distinct zero/sign patterns exhaust all proper exposed faces (every polytope face exposed), counted by 3sum_(k<m)binom(m,k)2^(m-k)t^k+2t sum_(k<m)binom(m,k)2^(m-k)t^k+2t^m+t^(m+1)=(3+2t)(2+t)^m-t^m(1+t). Polarity yields primal vertex figures combinatorial m-crosspolytopes and degree 2m. Independently enumerated closure intersections of 2+4m inequalities and affine dimensions for m=2,3,4, obtaining [12,20,10,1],[24,52,42,14,1],[48,128,136,72,18,1], exactly predicted. Source verify_book_faces.py inspected, not blindly run; finite ranks corroborate only.

## originality

PASS

Symmetric edge/polyhedral Lipschitz identification and general face-subgraph criteria are known; counts of facets alone and exact ellipsoid of same graph are not new. The genuine assertion is cubical type of every nonempty proper dual face and full polynomial for all m, plus complete Banach norming-face interpretation. Inspected relevant graph families and Resultary ellipsoid show no actual stated full f-vector, but methods may make specialization straightforward; priority risk preserved.

## value

PASS

The entire face lattice by dimension of the natural edge-sharing triangle graph family, and norming-functional geometry of its Lipschitz-free space, are canonical exact structural invariants useful to graph polytopes, Banach norming sets and face enumeration. The full cubical classification adds information far beyond previously available facet totals and is not an arbitrary small-instance calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
