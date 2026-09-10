# Explicit quadratic Mahler-product gap on a symmetric cube-to-Hanner shadow segment in R^4

## Context

Let P(K) = |K| |K°| be the (symmetric) Mahler volume product (Lebesgue
volumes, polarity about the origin). The symmetric Mahler conjecture
predicts P(K) >= 4^n/n! for centrally symmetric K in R^n; for n=4 the
conjectured minimum is 32/3 = 4^4/4!, attained on Hanner polytopes
(in particular the cube and the cross-polytope). The 4-dimensional
symmetric case is the first open dimension. Shadow systems are the
field-standard deformation method; Campi–Gronchi / Meyer–Reisner theory
gives only qualitative convexity of 1/P along them, and Kim's theorem
gives only existence-only local minimality near Hanner polytopes.

## Definitions

- Baseline P_min = 32/3. Constant c0 = 1/100.
- Fixed square S = [-1,1]^2 in span{e1,e2} (|S| = 4, |S°| = 2).
- Fiber B'_t in span{e3,e4} for t in [0,1]:
  B'_t = conv{(1,1-t),(-1,1-t),(1,t-1),(-1,t-1),(0,1),(0,-1)}
       = {(x,y) : |x| <= 1, t|x| + |y| <= 1}.
- Segment K_t = S × B'_t (Cartesian product in the e1e2|e3e4 splitting).
- K_0 = [-1,1]^4 (16 vertices (±1,±1,±1,±1)).
- K_1 = [-1,1]^2 × conv{(1,0),(-1,0),(0,1),(0,-1)} = B_∞^2 × B_1^2,
  a 4D Hanner polytope (l_∞/l_1 product), 16 vertices
  (±1,±1,±1,0),(±1,±1,0,±1).
- Shadow-system data (direction e4; all velocities parallel to e4;
  v(-x) = -v(x)): 16 moving trajectories from cube corners
  (a,b,c,d) ↦ (a,b,c,(1-t)d), velocity (0,0,0,-d); 8 static
  trajectories at (a,b,0,±1), velocity 0. Vertex census 16 → 24 → 16
  (fiber 4 → 6 → 4; the 8 static points are face-interior at t=0 and
  corner pairs merge at t=1).

## Result

For every t ∈ [0,1]:

  P(K_t) >= 32/3 + (1/100) t^2 (1-t)^2.

Both endpoints attain the baseline: P(K_0) = P(K_1) = 32/3.

## Proof / evidence

Exact analytic proof (all error terms exact, none unbounded):

1. Fiber area: |B'_t| = ∫_{-1}^{1}(2 - 2t|x|) dx = 4 - 2t, so
   |K_t| = |S||B'_t| = 4(4-2t) = 16 - 8t.
2. Polar fiber: (B'_t)° = {(u,v) : |v| <= 1, |u| + (1-t)|v| <= 1},
   of area 2 + 2t. The product polar is
   K_t° = conv(S° × {0}, {0} × (B'_t)°), and the product-polar
   identity |K_t°| = |S°||(B'_t)°|/C(4,2) = 2(2+2t)/6 = (2+2t)/3.
   Endpoint cross-checks: |K_0°| = 2/3 = 2^4/4! (B_1^4);
   |K_1°| = 4/3 (4·2/6).
3. Exact product: P(t) = 4(4-2t)(2+2t)/6 = (16/3)(2-t)(1+t)
   = 32/3 + (16/3)t(1-t).
4. Gap: P(t) - 32/3 - (1/100)t^2(1-t)^2
   = t(1-t)[16/3 - t(1-t)/100] >= 0 since t(1-t) <= 1/4 < 1600/3.
   Worst-case margin factor [(16/3)t(1-t)]/[(1/100)t^2(1-t)^2]
   = (1600/3)/(t(1-t)) >= 6400/3 ≈ 2133.

The computation was independently rechecked: exact shoelace on fiber
and polar hexagons confirms the area formulas, and the certificate
script replays endpoint volumes, the 16→24→16 census, the product
identity at 5 rational nodes, and the inequality at 11 rational nodes
(exact Fractions, stdlib only). Replay prints PASS.

## Limitations

- Proves only the one-segment envelope with loose c0 = 1/100; the true
  gap is linear (16/3)t(1-t), so c0 is not sharp (margin > 2000×).
- No full-target Banach–Mazur stability modulus is claimed.
- Does not establish Mahler minimality of 32/3 in R^4; the claim is a
  relative gap above 32/3, not minimality.
- Correction to admission narrative: K_t is in fact unconditional
  (product of unconditional factors); the segment's novelty is the
  explicit t-parameterized gap, not breaking unconditionality.

## Reproducibility

Run `python3 output/artifacts/fallback_certificate.py` (stdlib only,
exact Fractions). Expected output ends with
`FALLBACK CERTIFICATE REPLAY: PASS`.

## References

- J. Kim, Minimal volume product near Hanner polytopes,
  arXiv:1212.2544 (JFA 2014) — existence-only strict local minimality.
- J. Kim, A. Zvavitch, Stability of the reverse Blaschke–Santalo
  inequality for unconditional convex bodies, arXiv:1302.5719 —
  unconditional/near-unconditional stability only.
- M. Fradelizi, M. Meyer, A. Zvavitch, Volume Product,
  arXiv:2301.06131 — survey; Mahler open, shadow convexity qualitative.
- Hanner polytopes census (Klitzing) — 4D types and Mahler volume 32/3.
- Campi–Gronchi / Meyer–Reisner shadow-system convexity (via survey and
  HAL hal-00793779) — qualitative 1/P convexity only.
