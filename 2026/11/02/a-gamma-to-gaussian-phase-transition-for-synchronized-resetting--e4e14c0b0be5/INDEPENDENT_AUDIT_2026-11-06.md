# Independent mathematical audit

## correctness

PASS

The finite-N identity p_N=E exp[-a(log N)^2/Y_(N)] follows from Y_i=t0/tau_i ~ Gamma(1/2,1) and a single shared exponential clock. Uniform exponential moments of the centered Gamma maximum below a=1 give Gamma(1-a)(pi log N)^(-a/2) N^(-a). At and above a=1, the exactly normalized tilted density exp[-y-aL^2/y]/sqrt(pi y) has center sqrt(a)L and CLT variance sqrt(a)L/2; the transition factor crosses at y=L+O(log L), proving 1/2 at a=1, N^(1-2sqrt(a)) for a>1 and Phi(z/sqrt(2)) in a_N=1+z/sqrt(L). Renewal Laplace transform then gives r_N p_N T_N=>Exp(1) and exact E T_N=(1-p_N)/(r_N p_N). Independently integrated both exact finite-N formulas at (N,a)=(2,.5),(4,1),(12,2) and found agreement. Checked restrictions N>=2, fixed positive a, d,D>0, and fixed-z crossover; no a=0 or uniform-z conclusion.

## originality

PASS

The common-clock finite-N renewal formula is prior work, not the claimed novelty. Inspecting Biroli–Majumdar–Schehr 2023 protocol B and its appendix shows finite-number optimization and formulae, not the N-dependent r_N~(log N)^2 three-regime Gamma/Gaussian threshold. General frequent-resetting results can entail the exponential renewal factor, but do not determine the joint-population success-probability edge. Resultary analogous coupon reset records concern discrete coupon collections, not Brownian earliest absorption. Qualified best-of-knowledge originality for the complete phase/crossover claim.

## value

PASS

The explicit critical line a=1 and nondegenerate Gaussian crossover separate two different mechanisms for fastest search under a single reset clock, giving precise success probabilities and mean-search growth for a natural controlled stochastic population, beyond the known finite-N renewal formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
