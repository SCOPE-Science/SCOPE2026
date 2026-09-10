# Flat-line transfer obstruction at p0=7/2 for the fold-degenerate cubic hyperbolic surface S_*

## Context
The elliptic/nondegenerate-hyperbolic restriction range p > 22/7 (Demeter–Wu for the
truncated hyperbolic paraboloid; Guo–Liu–Xi for strictly negative-curvature surfaces;
Wang–Wu elliptic analogue) raises the recognized transfer question: does it persist
under cubic perturbations that force Gaussian curvature to vanish? The nearest
perturbed-saddle breakthrough (Buschenhenke–Müller–Vargas: xy+y^3/3 and xy+h(y),
Hessian det −1, p > 10/3 upper bounds) is by construction non-vanishing curvature and
consistent with boundedness at p = 7/2, leaving the degenerate-fold case open.

## Definitions
- Phase: φ(ξ1,ξ2) = ξ1^2 − ξ2^2 + ξ1^3 on B^2(0,1/2).
- Surface: S_* = graph of φ.
- Extension: Ef(x) = ∫ e^{i(x1 ξ1 + x2 ξ2 + x3 φ(ξ))} f(ξ) dξ.
- Fold: Hess φ = diag(2+6ξ1, −2), det = −4(1+3ξ1); Gaussian curvature K = 0
  exactly and simply along ξ1 = −1/3 (d/dξ1 det = −12 ≠ 0), interior to the domain.
- Recentered coordinates u = ξ1+1/3, v = ξ2: φ = u^3 − u/3 + 2/27 − v^2;
  fold point ξ* = (−1/3, 0).

## Result (headline, exact)
At p0 = 7/2 and R = 2^24 = 16777216, the datum f = 1_Q on the rectangle
Q = {|u| ≤ d, |v| ≤ s}, d = 2^{−8} = R^{−1/3}, s = 2^{−12} = R^{−1/2}, satisfies:
- Q ⊂ B^2(0,1/2) (centre distance ≈ 0.337 < 1/2) and Q lies in the
  R^{−1/3}-neighbourhood of the fold line {ξ1 = −1/3};
- ‖f‖_2 = √(4ds) = 2^{−9} = 0.001953125;
- ‖Ef‖_{L^{7/2}(B_R)} / ‖f‖_2 ≥ 2.75599… ≥ 10^{−3} R^{1/24} (= 0.002).
The L^2-normalized datum g = f/‖f‖_2 gives the identical ratio.
The same family at R_k = 2^{6k} (k ≥ 4) gives ratio ≥ 0.463 R_k^{3/28}
≥ 10^{−3} R_k^{1/24}. Hence the elliptic range p > 22/7 does not transfer to S_*:
polynomial growth R^{3/28} at p0 = 7/2 is incompatible with any C R^ε bound.

## Proof / evidence
1. Shear y1 = x1−x3/3, y2 = x2, y3 = x3 (Jacobian 1) removes the −u/3 tilt;
   Ef(x) equals a unimodular factor times
   I(y) = ∫_{|u|≤d,|v|≤s} e^{i(y1 u + y2 v + y3 u^3 − y3 v^2)} du dv.
2. Coherence box T_y = {|y1| ≤ 0.1/d, |y2| ≤ 0.1/s, |y3| ≤ 0.1R}:
   each phase term ≤ 0.1, total ≤ 0.4 rad, so
   |I(y)| ≥ cos(0.4)·4ds = 3.51356886×10^{−6} =: Emin.
3. Physical box T_x = shear^{−1}(T_y): Vol = 8·0.1^3·d^{−1}s^{−1}R
   = 0.008 R^{11/6} = 140737488355.33; corner norm ≤ 0.1055R < R for all R ≥ 1,
   so T_x ⊂ B_R.
4. ‖Ef‖_{L^{7/2}(B_R)} ≥ Emin·Vol^{2/7} = 0.00538280; dividing by ‖f‖_2 = 2^{−9}
   gives 2.75599 ≥ 0.002. General exponent: ratio ≥ 2cos(0.4)(0.008)^{1/p} R^{11/(6p)−5/12};
   at p = 7/2 this is 0.4636 R^{3/28}.
5. Reproducibility: output/artifacts/verify_fold.py (symbolic geometry, constants,
   containment, ratios; VERIFY_OK); output/artifacts/verify_knapp_quad.py
   (direct quadrature at R = 256, min|I|/area 0.9935 ≥ cos 0.4; QUAD_CHECK PASS);
   output/artifacts/FALLBACK_CERTIFICATE.md (hand-replayable numbers).
   Quadrature is corroboration only; the analytic cos-bound chain is the proof.

## Sharpness context (lower-bound side only)
Over rectangle caps d = R^{−a}, s = R^{−b} the growth exponent is
e(a,b;p) = −(a+b)/2 + (a+b+min(min(3a,2b),1))/p, giving necessary condition
p ≥ 2+2·min(min(3a,2b),1)/(a+b) ≤ 22/5 with equality at a/b = 2/3 (this cap,
a = 1/3, b = 1/2). Thus 22/5 is the optimal rectangle-Knapp threshold
(2h+2 for Newton distance h = 6/5 of u^3−v^2). The conjectured TARGET p > 4
upper bound is therefore false on (4, 22/5).

## Limitations
Proves the obstruction (lower bound) only; no linear upper bound is claimed.
The full p > 4 TARGET upper half is refuted on (4, 22/5) by the same family.
The 22/5 optimality is a necessary-condition scan, not a proved upper bound.
Constants are absolute and explicit; no R^ε bookkeeping needed on this side.

## References
- Bourgain–Demeter, Decoupling for hypersurfaces with positive-definite second
  fundamental form (arXiv:1403.5335) and nonzero Gaussian curvature (arXiv:1409.1634).
- Buschenhenke–Müller–Vargas, perturbed hyperbolic paraboloid xy+y^3/3, p > 10/3
  (arXiv:1803.02711); xy+h(y) finite-type (arXiv:1902.05442); polynomial partitioning
  p > 3.25 analogue (arXiv:2003.01619).
- Demeter–Wu, hyperbolic paraboloid restriction p > 22/7 (arXiv:2505.09037).
- Guo–Liu–Xi, strictly negative-curvature p > 22/7 (arXiv:2606.16766).
- Ikromov–Müller, L^p–L^2 restriction / Newton-polyhedra height theory.
