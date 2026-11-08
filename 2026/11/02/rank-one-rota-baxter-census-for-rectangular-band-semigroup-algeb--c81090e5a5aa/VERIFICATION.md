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

The semigroup rule (i,j)(h,l)=(i,l) gives ab=rho(a)gamma(b)^T. For nonzero rank-one R=a⊗f, RB identity forces a²=λa and fL_a=μf, fR_a=νf, μ+ν=λ. If λ=0, μ=ν=0; a²=0 iff row or column marginal vanishes. The row/column marginal map has fibers of dimension (m-1)(n-1); disjoint possibilities (u=v=0), (u=0,v!=0), (v=0,u!=0) yield the three terms divided by q-1. When λ!=0, a=α^{-1}uv^T with α=τ(a)!=0; the scaled left/right operators are commuting projections with ranks n,m and one-dimensional intersection. Their (1,0) and (0,1) dual eigenspaces have dimensions n-1,m-1 and yield q^{m+n-2}(q^{n-1}+q^{m-1}-2). Distinct pair representations divide by q-1; all characteristics and m=1/n=1 boundaries work. Independent finite sums agree with B_{1,2}(3)=8, B_{2,2}(2)=35, B_{2,2}(3)=164, B_{2,3}(2)=429. The algebraic classification, not finite cases, supports arbitrary q.

## originality

PASS

General rank-one tensor reduction and semigroup-algebra Rota–Baxter coefficient equations are classical. The literature inspected classifies order-two/three semigroups, quasi-idempotent multiplier constructions, and direct sums of fields, not the full explicit all-m,n rectangular-band rank-one weight-zero count with its square-zero/quasi-idempotent split.

## value

PASS

Rectangular bands form a canonical unbounded two-parameter semigroup family, whose nonunital algebra differs from matrices or products of fields. The complete low-rank RB operator census is a natural exact invariant, including nontrivial square-zero annihilator and characteristic dependence in simple arithmetic; it is a directly reusable base case for broader operator classifications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
