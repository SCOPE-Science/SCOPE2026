# Scientific review

## Correctness — PASS

The all-edge strict convexity proof uses the positive-definite shifted Laplacian and the injective map from independent simple-graph conductances to off-diagonal Laplacian entries. The wheel Fourier eigenvalues then give the exact reduced objective. The sign of its budget-affine boundary derivative, together with strict convexity and divergence as the hub disconnects, establishes the global if-and-only-if threshold. The second spectral moment verifies the local onset coefficient. Uniform Riemann-sum derivative convergence and sign bracketing establish the infinite-size limit and critical window. The standalone program completed six exact symbolic assertions, 144 direct spectral and 144 scalar-identity comparisons, 2,160 unrestricted asymmetric feasible comparisons, 12 numerical constrained optimizer cases, and five critical-scaling tests. Numerical results are corroboration, not a substitute for proof.

## Originality — PASS, qualified

Ghosh–Boyd–Saberi explicitly give a wheel Fourier reduction and optimality equation for equal edge prices (2008, pp. 59–60); the present work does not claim either ingredient. Their general convex framework does not itself specify the exact two-price rim deletion threshold, quadratic onset coefficient, or \(1/n\) critical price scaling, which require the new priced-budget calculation and singular-limit analysis. A named 2008 paper on the Kirchhoff index of weighted wheels could not be fully inspected; bibliographic evidence only is insufficient to conclude it covers or does not cover optimization. Searches of pertinent published mathematical research records found wheel symmetric-edge-polytopes and other objectives, rather than an equivalent or stronger priced-total-resistance result. Publication priority is therefore qualified by residual specialized-coverage risk.

## Value — PASS

The wheel is a canonical redundant radial communication or electrical network. Whether it is worth buying any rim conductance at all, given a relative unit price, is a natural design decision not answered by the equal-cost result. The all-or-none threshold predicts a topology change; the exact small-premium quadratic cost improvement quantifies near-indifference, and the explicit critical window explains why every finite wheel can retain a rim at a price ratio where the large-wheel optimal ratio vanishes. All are model-intrinsic invariants and design rules, not arbitrary parameter slices.

## Closest literature and limits

- A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), Section 5.2, Eq. (38), pages 59–60: equal-cost wheel spectral reduction and uniqueness. https://stanford.edu/~boyd/papers/pdf/eff_res.pdf
- C. Li, Y. Yang, H. Zhang, *Kirchhoff index of weighted wheel graphs* (2008): close object, full paper not read; novelty risk retained. https://www.researchgate.net/publication/268625211_Kirchhoff_index_of_weighted_wheel_graphs_W_n_ab
- Exact statement applies only to independent edge conductances with two class-constant costs and the all-pairs resistance objective. No independent audit has taken place.

Self-review: passed. Independent audit: not yet performed.
