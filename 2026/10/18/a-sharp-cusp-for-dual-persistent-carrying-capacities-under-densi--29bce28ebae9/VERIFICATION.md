---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

PASS: The positive diagonal fixed-point equation for T(x)=a x/(1+x)[u+v x²/(H+x²)] is cubic P(x)=x³-Lx²+Hx-HK with K=au-1>0, L=a(u+v)-1>K, H=h²>0. P(-y)<0, so all real roots are positive. Its discriminant H[-4H²+QH-4L³K], Q=L²+18LK-27K², has Q²-64L³K=(L-9K)³(L-K); this proves exactly L>9K and H_-<H<H_+ for three positive roots, folds at endpoints, and triple cusp L=9K,H=27K². T strictly increases, and T(r)-r sign together with derivative formula gives outer diagonal multipliers in (0,1), middle >1; planar eigenvalues T'(r) and (2p-1)T'(r) yield outer sinks, middle instability. Rational a=10,u=17/110,v=6/11,H=11,p=3/5 has T=x(17+7x²)/((1+x)(11+x²)) and T-x=-x(x-1)(x-2)(x-3)/((1+x)(11+x²)). Independently exact SymPy calculation verified discriminant factor, derivative (7x^4+120x^3+214x²+187)/((1+x)^2(11+x²)^2), and positivity coefficients [176,726,215,12,62,6,3] of (3-T') numerator. Thus 0<T'<3 and global difference contracts by factor 3/5, excluding asymmetric full-system fixed points at the example. Exact multipliers 17/11,11/12,47/45,37/40 give origin unstable, outer sinks, middle hyperbolic saddle. Implicit function theorem gives their persistence under small admissible C^1 perturbations. Global all-parameter absence of asymmetric equilibria is not claimed.

## originality

PASS

PASS best of knowledge: McGrane-Corrigan, Mason and de Andrade Moral 2024 introduce broad nonlinear lossy dispersal patch models and numerical persistence/extinction behavior; their cited Example 5 exhibits extinction-vs-positive coexistence, not this explicit identical-monotone Beverton–Holt/Hill survival two-positive-sink cusp and full-system synchronization certificate. Generic scalar cubic discriminants and Allee-like hysteresis are classical; novelty limited to the sharp parameter law plus the rational two-patch model with two stable positive densities despite uniquely stable isolated BH recruitment.

## value

PASS

PASS: The result exhibits two distinct *positive* carrying capacities while each isolated Beverton–Holt recruitment map has only one positive attracting density, a motivated counterexample in lossy dispersal modeling. The sharp two-parameter cusp, complete exact rational witness, transverse contraction excluding hidden asymmetric fixed points and hyperbolic robustness provide reusable mathematical bifurcation information beyond a generic polynomial sign computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
