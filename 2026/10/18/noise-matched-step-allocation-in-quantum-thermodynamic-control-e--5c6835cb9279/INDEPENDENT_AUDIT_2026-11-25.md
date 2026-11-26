# Independent mathematical audit

## correctness

PASS

Completing the square gives the claimed integral lower bound since g(x)√φ(x)·ẋ integrates to its endpoint primitive for absolutely continuous x. For equality, strict positivity forces ẋ=N√φ(x) a.e. Composing with F(y)=∫_a^y du/√φ(u) yields F(x(t))=Nt; the inverse gives an admissible unique solution with N=F(b). When φ=s² the schedule is uniform in the parameter. For the metric-speed schedule, with L_g=∫√g, the deterministic coefficient is L_g² and the noise coefficient is s²∫g^(3/2)/L_g; optimizing the positive real count gives the stated excess, strict by Cauchy–Schwarz unless g is constant. The Gibbs metric is β times the variance of σ_z/2, hence β sech²(βu/2)/4. Integrating gives the tanh expression; after z=βu/2 the powers of β cancel in the ratio and the sech integrals (π, 2, π/2 for powers 1, 2, 3) give π/(2√2). On the integer grids, compactness for each N and E_s≥(min g)Ns²/2 reduce attainment to finitely many counts for each s. The rounded uniform grid gives sG+O(s²), G=∫g. Every minimizer then has ∑d_i²=O(s) and N=O(s^−1). The identity E_s=s∑g(x_i)d_i+(1/2)∑g(x_i)(d_i−s)² and Lipschitz quadrature error at most ||g′||∞∑d_i²/2 give the matching lower bound and a uniform squared-error penalty of order s². Cauchy–Schwarz yields the stated O(√s) error for Ns. The squared-error estimate is aggregate, not a pointwise d_i/s→1 claim.

## originality

PASS

The closest quantum source derives the quadratic objective and optimizes count along a prescribed geodesic, not simultaneously over scalar speed and count. Classical stochastic control already exhibits a related velocity/noise balance, and deterministic discrete control already gives equal increments in a special fixed-count model. The supported distinction is the full joint scalar optimum, its strict benchmark gap including the qubit limit, and the all-global-minimizers result for a variable metric in the noisy integer objective. The use of square completion or Cauchy–Schwarz is not itself new.

## value

PASS

The theorem changes the recommended control schedule within a previously specified physical response model: even with a rapidly varying metric, a uniform ramp is optimal under constant increment variance, and a metric-speed ramp can have a quantified 11.07% higher leading cost. The integer theorem adds more than rounding a formal duration, by controlling the cost and aggregate mismatch of every global optimizing grid. This is a motivated and useful comparison for the quadratic model rather than a new physical-noise expansion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
