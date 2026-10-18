---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Write V=F_q^n and Z=Λ²V of dimension N=n(n−1)/2. A subalgebra projecting to W≤V with dim W=k<n is uniquely specified by T=S∩Z containing Λ²W and a linear lift W→Z/T; choosing T and lift yields F_k(q)=Σ_{j=0}^{N−C(k,2)}[N−C(k,2) choose j]_q q^{k(N−C(k,2)−j)}. Proper subalgebras cannot project onto V because brackets of a full V basis span Z. Two subalgebras Lie-generate L iff quotient projection subspaces W+U=V; intersection dimension k+ℓ−n and complements count [k choose k+ℓ−n]_q q^{(n−k)(n−ℓ)}, yielding every D_k. Nested W_k<W_(k+1) strictly increase neighbor sets by a complement of W_(k+1), so 0<D1<...<D_(n−1). Degree classes count n, and least positive degree D1=q^{n−1}F_(n−1)(q) strictly increases in q (Gaussian polys have nonnegative coefficients); this reconstructs n and q. Every field, including characteristic 2, is covered. Independent exact Gaussian formula evaluation reproduced n3 q2 histogram 0:15,116:357,378:203; n3 q3 histogram 0:27,1062:2392,3072:1534; n4 q2 additional. The full theorem is proved by counting subspaces, not those small checks.

## originality

PASS

The known general Frattini-quotient graph blow-up, especially Towers–Zuleta–Gutierrez arXiv:2608.16575 Theorem 6.1, substantially subsumes the abstract adjacency reduction and must receive credit. The distinct proposed all-rank free-exterior-square fiber factors F_k, full degree multiset, and intrinsic q/n reconstruction were not found in the actual published-record query or accessible abstracts. However, the highly relevant August 2026 primary full text was not accessible via arXiv/OA routes, and the authorized institutional route returned VPN disconnected; snippets cannot certify NOT_COVERING. This is best-of-knowledge PASS with **material overlap risk** not an absolute priority claim. Absence of full text alone does not mathematically refute the explicit formulas nor automatically fail O.

## value

PASS

The graph invariant is an exact all-rank finite-field classification for a natural and unbounded nilpotent Lie family, including substantial rank-3 graph of 575 vertices over F2. Recovering free rank and field size from an unlabelled graph degree multiset is a natural inverse problem not contained in a generic quotient-adjacency statement; the explicit counting formulas can be reused without graph enumeration. This is materially more than a small table or parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
