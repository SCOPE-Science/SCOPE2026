# Independent mathematical audit

## correctness

PASS

For sufficiently large N the given rates are probabilities. The one-site weight ratio G(k−1)/G(k)=g_N(k) balances each legal move against its reverse with the symmetric proposal, and P−D=K_N leaves the factor exp(−τD/N). Irreducibility follows by moving units from positive sites along paths to negative sites (intermediate sites receive before giving, so the ceiling is never breached), then connecting nonnegative configurations by surplus-to-deficit path transfers; legal reverse paths complete the argument. Given d>0 and j negative sites, choose their locations, a positive composition of d and a weak composition of K_N+d; this gives the three stated binomial factors. For d≥εN², expanding the two large binomial numerators as products of at most N terms gives a uniform O(1) error in the logarithm after replacing each factor by d or K_N+d, respectively. Stirling on the short factorials yields the stated entropy uniformly, with the endpoint conventions; the two missing degrees in the composition factors introduce only O(log N). For d=o(N²), monotonicity of sector counts bounds d≤εN² by the ε-sector and the tilt costs at most |τ|ε per vertex, while d=0 has entropy 1+log κ. Maximizing first over q gives q=√δ/(√(κ+δ)+√δ); the debt entropy has derivative 1/√(δ(κ+δ)), decreasing from infinity. Thus the unique cap or interior maximizer is exactly δ_τ, including equality at τ_c. A strict entropy gap against polynomially many sectors gives concentration, with feasible lattice sectors approaching the maximum even at the cap. Conditional hypergeometric signs converge to independent signs for fixed coordinates. The joint composition-tail ratio is a product of s−1 terms 1−Σ h_i/(M+j), j=1,…,s−1, and its log tends to −(sN/M)Σ x_i along convergent sector ratios; subtracting one handles positive compositions. This yields the two-sided exponential with the stated scales and mixture masses. Exchangeability and the two-coordinate limit make each bounded continuous empirical test variance vanish, and the debt and sign-fraction conclusions follow from concentration. The derivative formula gives the strict one-sided kink.

## originality

PASS

The finite stationary product structure and the equal-rate limit are known. The supported distinction is the stationary triangular-array crossover at fixed τ and wealth of order N²: a macroscopic debt ceiling becomes inactive at the explicit finite τ_c, with positive interior debt, a kink, and an explicit equilibrium family. The inspected fixed-rate limits and finite stationary formulas do not furnish this scale-dependent limit.

## value

PASS

When per-agent wealth is order N, a log rate bias of order 1/N competes with entropy at speed N. The constrained entropy switches from a cap optimizer to an interior optimizer, giving a sharp usable transition parameter, a nonzero interior debt and a measurable change of limiting stationary law. This explains what fixed-bias limits cannot resolve, with no extra graph-mixing assumption.

The dated certificate retains the supplied scientific assessment, sources and limitations.
