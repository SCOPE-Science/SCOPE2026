# The smooth 3D Mahler-stability gap at distance 1.1 is false: smoothed-octahedron counterexample

## Context

The symmetric Mahler conjecture in R^3 (Iriyeh–Shibata 2020) gives minimum
volume product P(K) = |K||K^circ| >= 32/3 for origin-symmetric convex bodies,
attained at parallelepipeds (cubes). The admitted target asked for an explicit
quantitative stability cell: every origin-symmetric C^2 strictly convex
K in R^3 with multiplicative Banach–Mazur distance d_BM(K,P) >= 1.1 from the
parallelepiped class P satisfies P(K) >= 32/3 + 1e-3.
Nearest stability literature (Kim–Zvavitch unconditional, Boroczky–Hug
zonoid, Kim Hanner local minimality) gives only qualitative or
unspecified-constant small-eps moduli, no explicit (1.1, 1e-3) cell.

## Definitions

- d_BM(K,L) = inf{lam >= 1 : exists T in GL(3), K subset T(L) subset lam K};
  for class P, d_BM(K,P) = inf_{Pi in P} d_BM(K,Pi). For symmetric K,
  translated parallelepipeds reduce to centered ones (Lemma below).
- P(K) = |K||K^circ|, K^circ = {y : x.y <= 1 forall x in K}.
- B_1^3 = {x : |x|_1 <= 1} (octahedron / cross-polytope),
  B_inf^3 = [-1,1]^3 (cube).
- Witness: delta = 1e-6, f(x) = sum_{i=1}^3 sqrt(x_i^2+delta^2),
  K = {x : f(x) <= 1}, r = 1-3delta = 999997/10^6.

## Result

The target stability claim is FALSE. The body K above is origin-symmetric,
C^infinity (hence C^2) strictly convex, satisfies

  d_BM(K,P) >= (3/2)(1-3e-6) = 1.4999955 >= 1.1,

but

  |K||K^polar| <= (32/3)(1-3e-6)^{-3} < 32/3 + 1e-3,

with exact-integer certificates
3*999997 - 2200000 = 799991 > 0 and
32003*999997^3 - 32000*10^18 = 2711973864080135919 > 0
(excess <= ~9.6e-5). Strengthening: for every gamma > 0 there is a smooth
symmetric strictly convex K with d_BM(K,P) >= 1.4 and P(K) < 32/3 + gamma
(take delta < min(gamma/100, 1e-3)); no positive cube-only fixed-distance gap
exists. The octahedron, itself a minimizer with P = 32/3 far from cubes, is a
limit of smooth strictly convex bodies.

## Proof / evidence

1. Octahedron data: |B_1^3| = 4/3 (eight first-octant simplices of vol 1/6);
   (B_1^3)^circ = B_inf^3 (vol 8) since |x.y| <= |x|_1|y|_inf and e_i in B_1^3;
   hence P = 32/3.
2. Symmetrization lemma: if K symmetric and K subset Pi subset lam K with
   Pi = T(B_inf^3)+t, then Q = (Pi+(-Pi))/2 = T(B_inf^3) satisfies
   K subset Q subset lam K (same lam), using +-x in K and convexity. So only
   centered parallelepipeds matter.
3. Distance d_BM(B_1^3,P) >= 3/2: from B_1^3 subset T(B_inf^3) subset lam B_1^3,
   ||T^{-1}||_{1->inf} <= 1, ||T||_{inf->1} <= lam with
   ||T||_{inf->1} = max_{s in {+-1}^3}|Ts|_1,
   ||S||_{1->inf} = max_{i,j}|S_{ij}| (S = T^{-1}).
   Averaging identity (1/8)sum_s|r.s| = max(|r|_1/2,|r|_inf) (sign reduction +
   a>=b>=c case split) gives max_s|Ts|_1 >= (1/2)sum_{i,j}|T_{ij}|.
   Trace 3 = tr(ST) <= (max|S_{ik}|)(sum|T_{ki}|) yields product >= 3/2.
4. Smoothing: f is C^inf (delta > 0) with diagonal Hessian
   diag(delta^2/(x_i^2+delta^2)^{3/2}) > 0, hence strictly convex; even,
   coercive, f(0) < 1, so K is a symmetric convex body; sandwich
   |x|_1 <= f(x) <= |x|_1+3delta gives (1-3delta)B_1^3 subset K subset B_1^3;
   grad f != 0 on {f=1} gives C^inf boundary; strict convexity of f gives
   strictly convex body.
5. Transfer: rB_1^3 subset K subset B_1^3 and K subset Q subset lam K imply
   B_1^3 subset r^{-1}Q subset (lam/r)B_1^3, so lam >= (3/2)r >= 1.1
   (exact integers above). Polarity reversal
   K^circ subset r^{-1}(B_1^3)^circ gives P(K) <= (32/3)r^{-3} < 32/3+1e-3
   (exact integers above).

## Limitations

Disproves the exact stated (1.1, 1e-3) smooth-class cell and rules out any
positive cube-only fixed-distance gap. Does not decide the zonoid-only
fallback cell (gamma = 5e-4 on symmetric zonoids); the witness is not claimed
to be a zonoid. Uses only the elementary octahedron product, not the full
Iriyeh–Shibata theorem strength.

## Reproducibility

`output/artifacts/verify_counterexample.py` (stdlib only) checks: (A) averaging
identity on grid + 3000 random points (sanity replay of analytic proof);
(B) 3*999997 >= 2200000; (C) 32003*999997^3 > 32000*10^18 with margin
2711973864080135919; (D) sandwich on 20000 samples. Prints VERIFY_OK
(auditor-replayed).

## References

- Iriyeh–Shibata, Symmetric Mahler's conjecture in the 3-dimensional case,
  arXiv:1706.01749 / Duke Math. J. 2020 (minimum 32/3; context only).
- Kim–Zvavitch, Stability of the reverse Blaschke–Santalo inequality for
  unconditional bodies, arXiv:1302.5719 (nearest stability; no explicit cell).
- Kim, Minimal volume product near Hanner polytopes, arXiv:1212.2544.
- Fradelizi–Meyer–Zvavitch, Volume Product survey, arXiv:2301.06131.
- Chen–Li–Xi–Xu, Symmetric Mahler in 3D via admissible shadow systems,
  arXiv:2605.13795.
