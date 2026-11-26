# Independent mathematical audit

## correctness

PASS

An (n-1)-row real Gaussian matrix has full row rank almost surely; orthogonal invariance makes its kernel a uniform unoriented line. For a spherical unit representative u, the last squared coordinate is T=Z_n^2/(Z_1^2+...+Z_n^2), the ratio of independent chi-square components with degrees 1 and n-1 in numerator and complement. Pulling the line back by diagonal A and normalizing gives the residual ratio 1/[T+kappa^(-2)(1-T)]. For kappa>1 this decreases in T, so exact residual selection replaces T by W=max_j T_j and F_W=F_n^K. The residuals increase pointwise in kappa to 1/W. The density near zero is asymptotic to (K/2)(2/B_n)^K t^(K/2-1); the integral of t^(-q) against it is finite exactly when K>2q, with logarithmic divergence at equality. Monotone convergence handles the supremum; domination by W^(-q) also proves uniform integrability when the bound holds. For the first two means put e=kappa^(-2) and split at fixed small delta, with bounded contribution from [delta,1]. For K=1 the rescaling t=e*z and the leading beta density give e^(-1/2)B_n^(-1) times the integral of z^(-1/2)/(1+z), which is pi. For K=2 the density tends to 4/B_n^2 and the integrated leading kernel is log(1/e)+O_delta(1), yielding 8/B_n^2 times log kappa. The kernel slope 1-e is uniformly bounded away from zero near the limit and goes to 1; splitting lets the density errors tend to zero, also when n=2 and the other endpoint density is unbounded. For n=3 the square root of T is uniform, giving an integral with weight K u^(K-1), hence K/(K-2) in the limit and the three displayed finite-kappa arctan/log formulas by integration of u^(K-1)/(1+(kappa^2-1)u^2). The off-axis to axial norm ratio is kappa^(-1) times the corresponding ratio for u, so the angle converges under the common-sketch coupling, and does not control these scaled residual moments. For tall A, right singular coordinates and Gaussian multiplication by the thin left isometry give the same independent standard sketches. The uploaded verification and script were inspected, not executed; their finite checks and Monte Carlo are supporting evidence only.

## originality

PASS

Credit is for the selected best-of-independent-one-row-short ensemble, in particular the sharp replication threshold and its finite-contrast rates and constants, not for single-trial spherical invariance, beta/order-statistic facts, or a new range-finder error model. The nearest early primary result covers an equivalent single trial via the codimension-one Gaussian range finder, including its limiting Gaussian representation and a single-trial obstruction. The exact later one-spike law is another direct single-trial overlap. Neither inspected result gives a best-of-independent selection theorem: varying the number of columns or rows in one sketch is not that operation. Following the actual reductions distinguishes the comparatively narrow new result from classical ingredients and known single-sketch effects.

## value

PASS

The replication threshold is a concrete boundary for a plausible exact-arithmetic sketch rule: in the same spectrum and fixed dimension, two repetitions can still have a divergent expected relative squared residual even as every candidate approaches the correct direction, while three guarantee a uniform bound. The distinct rare-event rates and exact dimension-three quality floor quantify that issue, not just convergence of angle. This is not a claim of superiority over a single larger sketch, arbitrary spectra, or reduced wall-clock time.

The dated certificate retains the supplied scientific assessment, sources and limitations.
