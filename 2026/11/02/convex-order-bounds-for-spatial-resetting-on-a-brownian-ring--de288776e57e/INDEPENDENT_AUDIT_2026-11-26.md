# Independent mathematical audit

## correctness

PASS

Cutting at the target gives the two-endpoint killed interval and the cosh hitting transform psi_q. If B is its average over the reset law at q=r+s, a cycle from a sampled position has discounted absorption contribution B and discounted reset contribution r(1-B)/(r+s). Solving the scalar restart equation and accounting for the fixed initial point gives (s psi_(r+s)(d_0)+r B)/(s+r B). Its derivative in B is strictly positive since d_0>0; the first-step mean is (1-psi_r(d_0))/(r B_r), strictly decreasing in B_r. In the cost coordinate u, expand cosh(sqrt(q/D) sqrt(L²/4-u)) in powers of L²/4-u. Every term of order at least two has nonnegative second derivative on the interval, and the quadratic term gives a positive lower bound on f_q'' even at the antipode. Distinct convex-ordered laws on a compact interval have different continuous stop-loss functions and thus strictly ordered expectations of this kernel. Jensen and the chord inequality give the two unique cost laws with the prescribed mean; the cost-distance map is strictly increasing up to L/2. Dividing the cosh series gives psi_q=1-q u/(2D)+q²u(L²+u)/(24D²)+O(q³), uniformly in distance. The common mean cancels the linear terms of the two averaged transforms, and the initial-point factor yields u_0 Var(U)/(48 D³) in the mean gap. The variance bound follows by averaging (U-u_a)(u_b-U)≥0. At high rate the lower distance contributes exp(-a sqrt(r/D)) with weight lambda, dominating the endpoint b even if b is antipodal, while d_m lies strictly below b. The common initial-point factor cancels in the mean ratio; both means diverge. The verification note and script were inspected, not executed: sampled inequalities, small-rate and high-rate checks and two approximate backward-equation comparisons support finite cases only.

## originality

PASS

The prior ring and random-position resetting formulas are credited. The supported distinct contribution is the strict simultaneous optimizer and convex-order comparison for Poisson ring resetting at fixed mean unreset exit cost, together with its weak- and high-rate laws. The inspected closest indexed results optimize related objectives but have different kernels or budget functionals. The assessment is not a priority claim for two-point extremizers in resetting generally.

## value

PASS

The budget has a direct physical meaning independent of the reset rate: the average free search cost from a reset. The result compares arbitrary admissible distributions, not a chosen finite family, and the same sharp pair governs every positive reset rate and Laplace argument. In particular it distinguishes a second-order weak-rate effect, whose coefficient has a sharp variance interpretation, from exponential separation at large rates. Those quantitative consequences make the specialization scientifically useful without asserting a general stochastic ordering.

The dated certificate retains the supplied scientific assessment, sources and limitations.
