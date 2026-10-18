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

For L=X⊕Y⊕Kz (dim 2m+1) with central z and [ei,fj]=δij z, [fi,ej]=λδij z, λ∈K×, λ²≠1, the bracket is 2-step nilpotent and non-Lie (1+λ≠0). Every subalgebra either contains z, hence is π^{-1}(W), giving t*Σ_k Gaussian[2m,k]_q t^k, or misses z and is a unique linear graph f:W→K. Graph closure implies two ordered bracket equations A+λC=0, C+λA=0; det1−λ² nonzero forces x⋅y'=x'⋅y=0 for all pairs, precisely projections U=pr_X(W), T=pr_Y(W) perpendicular. For a=dim U, b=dim T≤m−a there are Gaussian[m,a]Gaussian[m−a,b] options. A subdirect W≤U⊕T of dimension a+b−d is determined by codimension-d kernels I,J and an isomorphism U/I≅T/J; Gaussian[a,d]Gaussian[b,d]|GL_d| choices; each W admits q^{a+b−d} graphs f. Summing gives exact stated full polynomial independent of admissible λ over ALL characteristics. Independent explicit RREF enumeration of closed subspaces over F4 (λ=2, x²+x+1) gave m=1 coefficients 1,9,5,1 and m=2 1,101,197,357,85,1 (total 742), matching formula. Excludes λ=±1; finite tests not universal proof.

## originality

PASS

Mancini–La Rosa classify two-step nilpotent Leibniz algebras through bilinear forms (full paper read), not counts of embedded subalgebras; their main setting assumes char≠2 while present valid q can have even characteristic. Siciliano–Towers study modularity/semimodularity of subalgebra lattices and extraspecial algebras (full arXiv paper read), not rank-wise cardinalities over finite fields. Lie Heisenberg subalgebra-count findings involve alternating λ=−1, explicitly outside generic case. Elementary subdirect-product Gaussian counts are well known, but applying them to the constrained generic non-Lie algebra produces a new complete dimension polynomial. Unindexed subalgebra zeta-type formulas might overlap.

## value

PASS

An exact dimension generating polynomial across all m and every admissible q is a natural invariant of an infinite family of nilpotent non-Lie Leibniz algebras, distinguishes central-ideal and noncentral isotropic graph subalgebras, and yields nontrivial characteristic-2 instances. This is more than a known Lie Heisenberg table or arbitrary finite sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
