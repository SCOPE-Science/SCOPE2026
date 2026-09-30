# Independent audit — 2026-09-30

## Disposition: PASSED

### Correctness
PASS. Starting from the Lee–Wang parametrization and the standard shrinker rescaling, I independently recovered the diagonal metric and the stated strictly negative Gaussian curvature. The substitution `t=tanh μ` makes the total-curvature integral exact and gives `-4π√(pq)`. The exact radial coordinate cuts a centered ball to `|μ|≤a`; integrating the area form gives the filed radical/arcosh formula. Differentiation yields the single maximum equation `ds a sinh(2a)=2pq` and the single cone-density crossing. The large-radius logarithmic term is also correct.

For `(p,q)=(2,1)`, the Möbius quotient halves area and total curvature. Solving `3a sinh(2a)=4` reproduces `a*=0.7000655576`, `R*=1.6512789741`, and peak ratio `1.8448061591`. The metric bound under the deck map `(θ,r)↦(θ+π,-r)` gives the rigid systole `2π`.

### Originality
PASS, qualified. Lee–Wang supply the family and conical asymptotics, and Braxton–Lee–Zhu supply recent F-stability. Searches of the accessible current literature did not locate the exact total-curvature package, centered ball-area overshoot/crossing law, logarithmic excess, or Möbius systole. These are direct but nontrivial global consequences of the explicit metric, so the claim is limited to those invariants.

### Scientific value
PASS. The formulas sharpen qualitative asymptotic-cone information into an exact global area profile and provide intrinsic invariants for a newly important stable higher-codimension shrinker.

### Evidence
- Lee–Wang, arXiv:0707.0239; open full text inspected.
- Braxton–Lee–Zhu, arXiv:2609.19648.
- Castro–Lerma, arXiv:0906.3117.

### Limitations
General `(p,q)` area counts immersion multiplicity; no nonlinear stability claim is made. A forthcoming same-surface thesis was unavailable and remains an originality caveat.
