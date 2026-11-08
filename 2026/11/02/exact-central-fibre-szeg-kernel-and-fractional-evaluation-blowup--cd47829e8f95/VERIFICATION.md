---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For canonical unweighted pentablock Hardy norm obtained by pushforward normalized T³ Haar measure under Ψ=(ξ(λ1-λ2)/2,λ1+λ2,λ1λ2), two independent phase symmetries orthogonalize pure a^k powers from all monomials involving s or p. Those latter monomials vanish at A(a)=(a,0,0), so the restricted evaluation kernel lies in the closed pure-power subspace (using bounded evaluations from the foundational source). Vandermonde gives ||a^k||²=4^(-k)binom(2k,k), hence K(t)=Σ4^k/binom(2k,k)t^k = _2F1(1,1;1/2;t). A beta-integral yields K(t)=(1-t)^(-1)+sqrt(t)arcsin(sqrt(t))/(1-t)^(3/2), holomorphic at t=0. Expansion in u=sqrt(1-t) gives K=(π/2)u^-3 -(π/4)u^-1 + 1/3 +O(u); sharp evaluation norm grows as sqrt(π/2)(1-r²)^(-3/4). The reproducing inequality is tight at kernel vectors. Independently checked exact coefficients k≤30, coefficient recurrence, and sample numerical evaluation.

## originality

PASS

Su–Tomar arXiv:2610.17729 develops precisely this canonical Hardy space, its torus normalization, orthogonal decomposition (Prop. 2.2), abstract kernel projector (Prop. 3.5), and averaged diagonal identity (Prop. 3.6). Its accessible full-text HTML Sections 2–3 were inspected: the exact central-fibre hypergeometric two-point kernel and sharp pointwise (1-|a|²)^(-3/4) evaluation constant are not explicitly given there. General reproducing kernel facts and Vandermonde are credited; the new claim evaluates a natural invariant beyond the abstract formula.

## value

PASS

The central fibre consists of nilpotent-matrix coordinates fixed by the domain's symmetry actions. An explicit two-point kernel and sharp fractional boundary exponent in a newly defined several-variable Hardy space are natural benchmarks for point evaluations, interpolation and comparisons with averaged Szegő estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
