---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The two-stage walk factors exactly as Q=AB with A(g,x)=1_(gx=x)/f(g), B(x,h)=1_(hx=x)/|H|. The companion point process K=BA is invariant under point stabilizer H; double transitivity forces common off-diagonal (1−a)/(n−1), hence K=Π+λ(I−Π). Burnside’s lemma for the H-action on X gives E_H f=2, and Jensen yields a≥1/2>1/n; identity fixes all n points, so a<1 and 0<λ<1. The formula Q^t=A K^(t−1)B gives π=f/|G| and exact affine interpolation for every t≥1. A one-step row Q(g,.) is a convex mixture of μ_x=Uniform(G_x), with TV(μ_x,π)=1−2/n from exact support comparison; a singleton fixer makes it exact. For S_n the inverse fixed-point count expectation yields truncated exponential; for affine group the stabilizer is identity plus q−2 single-fix nontrivial dilations. Independent Fraction arithmetic checked 497 exact Q²(g,h) comparisons in S_3, S_4 and AGL(1,5), and sharp maxima, corroborating the all-group proof.

## originality

PASS

Feng (2025/26) already establishes general dual-Burnside Q=AB, π, spectral transport, mixing inequalities and conjugacy lumping. These ingredients are explicitly credited, and one-step conjugacy-class stationarity is already a corollary. The inspected complete lawful primary paper did not state the all-doubly-transitive two-eigenvalue reduction with exact TV prefactor for every positive time, its singleton-fixer sharpness, nor the quantified S_n versus AGL(1,q) asymptotic contrast. The result is an elementary special-case derivation, with genuine risk that general spectral machinery or a group-specific prior table implicitly dominates it.

## value

PASS

Exact finite-time worst-start total-variation, not just a mixing bound, is a motivated invariant for sampling in a widely natural class of permutation actions. Symmetric and affine families share immediate class-level stationarity but have qualitatively different full-group relaxation scales, making the sharp asymptotic comparison informative. No unjustified performance or universal cutoff claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
