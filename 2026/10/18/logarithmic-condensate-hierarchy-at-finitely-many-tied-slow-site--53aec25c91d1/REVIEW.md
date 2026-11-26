# Independent mathematical audit

## correctness

PASS

Rate times site weight at positive k equals the site weight at k-1. Incoming stationary flux on edge i→i+1 therefore equals the target configuration weight times the current departure rate at i+1, so the fluxes balance. Positive clockwise moves connect the fixed-particle state space. Multiplying weights by q^N yields a sum of L-m geometric variables tilted by W_m(N-b), and the conditional slow law is the product of reciprocal (k_i+1). The generating series for the latter is [-log(1-z)/z]^m. The Stirling coefficient divided by (s+m-1)! is the (m-1)-st elementary symmetric function of the reciprocals 1 through 1/(s+m-1); repeated-index terms in its comparison with the (m-1)-st harmonic power are lower order by summability of j^-2. This gives W_m(s)~m(log s)^(m-1)/s. On |b-(L-m)rho_c|<=L^(2/3) the tilt relative to its value at the central integer is uniformly 1+o(1); outside this window the geometric-sum Chernoff tail is exp(-c L^(1/3)), negligible even after polynomial reweighting. This proves the unchanged CLT and makes the atypical slow mass negligible even at the 1/log L scale. For each fixed winning index, restricting the other k_i+1 to s^t_i forces its residual mass to be s-o(s), and the subordinate harmonic sums, divided by log s, tend to t_i. The box probabilities tend to (1/m) times the product of those t_i, uniformly on the typical fluid window. Taking interior t_i to one gives uniqueness and uniform index; the uniform box limits factor jointly with the fluid Gaussian. For a selected macroscopic pair, restrict all other sites to at most delta*s and sum their harmonic weights. Writing R for their sum, the pair split is a uniform Riemann sum for s^-1 times the integral of [x(1-R/s-x)]^-1 on [epsilon,1-R/s-epsilon]. As delta tends to zero the integral tends uniformly to 2 log((1-epsilon)/epsilon). Any omitted term has a third macroscopic site: after fixing the other m-3 occupations, at most O(s^2) triple splits each have weight O(s^-3). The omitted or multiply counted terms thus have total weight O((log s)^(m-3)/s) for fixed thresholds. Multiplying by choose(m,2) and dividing by W_m(s) gives the stated coefficient; uniformity on typical s and the exponential fixed-fraction concentration justify averaging at the logarithmic scale. In particular the formally automatic event at s=0 is negligible. The supplied NumPy checker was inspected, not executed; the limits were proved analytically.

## originality

PASS

The finite stationary product weights, their single-site critical specialization, and the conditional slow partition law are not new: the last is exactly the classical conditional permutation law. The supported distinction is the joint fixed-m limit with independent Gaussian ordinary-site fluctuations, and the explicit sharp two-macroscopic-site coefficient in the tied-site regime. The relevant two-site formula gives a close lower-multiplicity analogue; neither it nor the inspected unconditioned or fixed-three-cycle results states or directly specializes to the complete asymptotics here.

## value

PASS

The marginal rate is a natural boundary for slow-site condensation. The theorem distinguishes one extensive condensate from several subextensive but widely populated independent log scales; basic uniqueness of the condensate does not quantify this distinction. It also identifies how often the uniqueness picture fails at a fixed macroscopic fraction, with an explicit threshold- and multiplicity-dependent coefficient, and separates these slow scales from Gaussian fluid noise. The value is in these joint and rare-event asymptotics, not in rediscovering the Stirling normalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
