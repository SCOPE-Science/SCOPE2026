# Independent audit — 2026-09-29

**Record:** `2026/09/17/balanced-nonuniform-reset-coupon-rates--7b9ca5a2ebed`  
**Audited source tree:** `a1147222aa76bf12f1c591e701dfd7f9954d598c`  
**Repository:** `SCOPE-Science/SCOPE2026` at checked commit `253a0fe5d0217455660a277f9adb940030e567ad`  
**Overall independent-audit verdict:** **PASS**

## Correctness — PASS

The Poisson-race representation gives p_n=n c integral exp(n Phi_n(y))dy exactly.  The exponent is strictly concave with a unique saddle, and m<=x_i<=M supplies a common compact saddle interval, uniformly nondegenerate curvature, and the derivative bounds needed for the stated first-order Laplace expansion.  The equal-weight specialization agrees with the exact beta/gamma ratio.  Differentiating the z-dependent integral gives g_n'(s)/p_n=(n ybar_n-1/c)/s^2; substituting into the cited catastrophe parameter yields alpha_n=p_n(1+s-cn ybar_n)/(1-p_n), and Laplace concentration makes this -c n y_n p_n(1+O(n^{-1/2})).  Because y_n is uniformly bounded above and away from zero, the cited two-sided p+|alpha| result gives d_K=Theta(n p_n).  Weak convergence on the compact profile space gives the rate functional.  Finally, strict concavity of x->log(1-e^{-xy}) proves Schur-concavity, and its uniform negative second derivative on the compact x-y region gives the stated variance penalty.

## Originality — PASS

The located reset-coupon literature provides finite unequal-probability formulas, qualitative regenerative rare-success criteria, or the general p+|alpha| catastrophe theorem.  The recent Wang--Lu work explicitly leaves non-uniform coupon evaluation as a further direction.  No located source supplied the balanced-profile saddle functional together with the explicit alpha asymptotic, sharp coupon-specific Kolmogorov order, and quantitative heterogeneity penalty.  Classical Poissonization, Laplace method, and Schur-concavity ingredients are not claimed as novel.

## Scientific value — PASS

The record resolves a concrete recent non-uniform reset-coupon direction in a broad balanced regime, turns a high-dimensional probability vector into a one-dimensional saddle/profile functional, determines the exponential scale and prefactor of the success/mean quantities, and converts an abstract catastrophe bound into a sharp coupon-specific rate.  The heterogeneity penalty adds structural information beyond the limit law.

## Sources used in the independent comparison

- https://arxiv.org/abs/2609.16566 — Wang--Lu memoryless-catastrophe theorem giving the general two-sided p+|alpha| Kolmogorov scale and motivating non-uniform coupon evaluation.
- https://arxiv.org/abs/2605.14511 — Long regenerative formulation for reset coupon collectors; supplies the transform viewpoint and qualitative rare-success conditions.
- https://doi.org/10.3390/math12020239 — Jockovic--Todic reset coupon collector with unequal standard probabilities.
- https://doi.org/10.3934/math.2026800 — Li--Dai--Kim generalized expected-waiting-time formula for arbitrary standard coupon probabilities.

## Limitations and residual uncertainty

- The theorem fixes q in (0,1) and assumes balanced weights x_i/n with x_i uniformly bounded above and below.
- It does not cover moving-reset regimes, rare/Zipf-like coupons, or second-order saddle corrections.
- Priority is qualified because older generalized coupon/restart literature may contain equivalent pieces under different terminology, though no covering package was located.

This independent audit is scoped to correctness, originality, and scientific value.  Repository material was used as evidence only; no GitHub modification was made during the audit.
