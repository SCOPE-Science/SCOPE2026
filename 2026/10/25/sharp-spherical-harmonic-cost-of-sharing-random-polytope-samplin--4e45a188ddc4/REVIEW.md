# Scientific review of sharp spherical-harmonic sampling compromise

## Correctness — PASS

The normalizations are anchored to the established random boundary polytope formula: \(\mathcal I_j=\int w_j\rho^{1-\beta}\,dS\), \(w_j=\kappa^{1/(d-1)}H_{d-j}\), and \(\beta=(d+1)/(d-1)\). Strict Hölder optimization gives \(p_j\), and the radial-graph Weingarten first variation gives \(u_j=-(d-j+1)(g-\overline g)/(d+1)\). The two-endpoint average functional provides an exact lower bound. The geometric-mean sampler attains that lower bound through second order simultaneously for all intermediate indices. The spectral estimate follows from the exact Laplace–Beltrami eigenvalues, with sharp equality at degree two.

Direct numerical evaluation on a strictly convex three-dimensional zonal quadrupole independently brackets the minimax cost and reproduces the claimed \(1/5\) coefficient. Its finite quadrature is corroboration only, not the proof. The theorem is local and about limiting separately normalized coefficients, not finite-sample optimization.

## Originality — PASS, with risks

Hoehner's 2026 primary text was inspected at Theorem 3.1, Lemma 3.3, and Theorem 3.4, providing the curvature error formula, the unique individual optimal densities, and qualitative simultaneous-optimality rigidity. It does not compute the sharp near-sphere quadratic worst-risk coefficient or the all-index spherical-harmonic spectrum. The endpoint average-risk lower bound used in this finding is proved directly from Hölder's inequality. The public ellipse minimax research record was read through its main theorem and proof: it treats two objectives in dimension two, giving the known planar coefficient \(3/8\), which is explicitly excluded as a novelty claim. The public Hellinger-gap paper was read: it compares two optimal probability distributions, not worst normalized intrinsic-volume loss. Böröczky–Fodor–Hug (2011) was inspected at its exact Reitzner asymptotic formula, and Besau–Hoehner–Kur (2019) at its abstract. Actual semantic and keyword searches did not identify an equivalent all-dimension near-ball spectral minimax theorem; such negative searches do not prove priority. Full inspection of every historical paper was not possible, leaving literature-priority uncertainty.

## Value — PASS

The geometric problem is an explicit quantitative version of the recent rigidity theorem: how much relative approximation quality must be lost when one vertex sampler serves several intrinsic volumes? The answer identifies the *sharp* second-order price for every index set, shows only its extreme indices matter at leading order, gives the full intrinsic spectrum, and determines exactly which geometric infinitesimal deformations are invisible. The sharp degree-two coefficient supplies a reusable calibration benchmark in stochastic convex geometry rather than an arbitrary numerical slice.

## Limits

The perturbation must be fixed and sufficiently smooth; no global nonlinear bound or finite-sample sampler optimality is asserted. Published special cases and competing metrics are acknowledged without recasting them as new. Residual unseen-source overlap is possible.

Self-review: passed. Independent audit: not yet performed.
