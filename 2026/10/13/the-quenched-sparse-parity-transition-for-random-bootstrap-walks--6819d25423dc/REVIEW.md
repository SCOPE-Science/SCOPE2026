# Independent mathematical audit

## correctness

PASS

Fix the full input path first: level k uses exactly 2^{N_k} independent Bernoulli bits, so a_k=E(ζ_k|ξ)=(1−2r_k)^{2^{N_k}}, and the centered parities are independent across levels conditional on that path. The summable Hoeffding bound and then Fubini give a quenched almost-sure Cesàro error tending to zero for almost every environment, for each fixed α. On the sign strong-law event λ_k=2r_k2^{N_k} changes exponentially at α=1/2. Below it, a_k≤e^(−λ_k) tends to zero and the normalized bracket tends to zero uniformly by the partial-sum lemma; the conditional covariance matrix has diagonals 1 and off-diagonal ζ_{j−1}, and the scaled jumps are bounded by √(2/n), giving the martingale functional CLT. For α=0 the mean is identically zero at k≥1. Above the threshold Σr_k2^{N_k}<∞ along almost every input path, so conditional union bounds, Borel–Cantelli, and Fubini give finitely many negative parities; Y−X becomes constant, not necessarily zero. At criticality λ_k=2^{k/2−floor(k/2)}2^(−X_k/2). Bernoulli and exponential bounds make the mean uniformly close to 1 on X_k≥M and to 0 on X_k≤−M as M grows. A fixed strip has O_M(√m) expected visits by the local binomial bound, hence zero limiting visit fraction almost surely by dyadic Markov/Borel–Cantelli and monotonicity. Taking the countable intersection over M then gives the stated uniform occupation-time approximation. In the proof's index shift, compare with the centered partial sum through m−1 and add the single initial term 1/n; for a comparison at the same m the literal endpoint bound is 3/n rather than 1/n. Either gives the claimed uniform limit. Donsker and Brownian zeros of Lebesgue measure zero give joint convergence of (rescaled X, Q_n); the time-one positive occupation has Beta(1/2,1/2), with the stated mean and variance. For a direct necessity check, on each partition block [a,b] the product of walk increments minus Σ_{j=a+1}^b ζ_{j−1} is the martingale sum with coefficients (X_{j−1}−X_a)ζ_{j−1}+(Y_{j−1}−Y_a), multiplying ξ_j. Summing over m equal time blocks, isometry bounds the squared error after division by n by 2(1/m+1/n). A hypothetical Brownian pair would force its block product sums, as m grows, to its deterministic covariance, contradicting the arcsine bracket limit. Countably many integer horizons suffice. The supplied checker was inspected, not executed; finite parity checks cannot establish these limiting claims.

## originality

PASS

Verified coverage is partial: the α=0 endpoint is already uniformly elliptic, the predictable covariance criterion is classical in bootstrap walks, and the arcsine law is classical. The distinct supported claim is a quenched transition in the full inclusion-induced model with these exponentially decaying coefficient probabilities, including the critical reduction of its random parities to positive occupation time. The closest checked techniques and results do not provide that transition or reduction.

## value

PASS

The model tests a natural limit of elliptic bootstrap-walk results: the exponentially small activation probability competes with an exponentially large random number of included bits. The full threshold rather than an arbitrary parameter slice is identified, and the critical behavior shows that two diffusive marginals can share a genuinely random macroscopic bracket. This adds a distinct mechanism, not a new proof of the arcsine law alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
