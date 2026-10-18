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

For source profile (x,y) on K_{n,n}, first-step equations solve to u=(λ n y+λ²x(n−y))/(n²−λ²(n−x)(n−y)), v with x/y swapped. If x>=y, u<=v and is bottleneck; for k<n the continuous centered benchmark B obeys B-u(d)=λ(1−λ)d(c−λd)/[2c(D0+λ²d²/4)], strictly positive for d>0. Thus even budget uniquely balanced; for odd k the derivative of the defect has sign of strictly decreasing Q(d), so u has no interior strict local max and a discrete maximizer is either near-balanced or one-shore. Exact endpoint subtraction has sign of F_{n,k}=2n−(k+1)λ−(2n+1−k)λ², giving one sharp threshold λ*. If n<=k<2n, every non-source support<=λ, equality exactly when S includes a full shore; full graph k=2n has support 1. Binomial counts match profiles. Independent exact rational enumeration of all profiles n=2..9 for four λ values (352 parameter instances), and explicit K4,4 λ=9/10, supports the analytic classification.

## originality

PASS

Allagan–Pereyra–Massey arXiv:2609.31535 (Sept 2026) defines the discounted hitting domination objective and proves submodularity/general optimization/special graph cases. The accessible abstract emphasizes complete graphs, stars and spiders; no balanced K_{n,n} complete phase diagram or odd-budget symmetry-breaking critical fidelity was located. Full source inaccessible despite both open-access attempts and authorized institutional retry (vpn_disconnected), so whole-document noncoverage is NOT asserted; this remains a concrete originality risk. Guo et al 2024 fixed-source group hitting probability ranking uses a different maximization objective. Best-of-knowledge originality PASS with stated risk.

## value

PASS

For a natural vertex-transitive but bipartition-sensitive graph family, the optimal min-over-starts discounted hitting potential exhibits a nontrivial parity-dependent phase transition and unique algebraic critical fidelity. The complete k,λ budget diagram and exact extremizer counts solve a motivated combinatorial optimization problem, not a routine recasting of generic submodular approximation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
