# Independent mathematical audit

## correctness

PASS

For each fixed 0<alpha<1 and 0<c<=1 with independent sign reversals, eta_k=V_k-(1-2p_k)V_{k-1} are martingale differences with conditional variance 4p_k(1-p_k). Thus M_n=sum eta_k/(2p_k) has deterministic predictable bracket (1/c)sum_{k<=n}k^alpha-n, whose N^{-(1+alpha)} rescaling converges uniformly on compact times to t^{1+alpha}/[c(1+alpha)]. The maximal rescaled jump is O(N^{(alpha-1)/2}), verifying conditional Lindeberg. The identity M_j=X_j-V_j+V_0+R_j with R_j=sum_{k<=j}(k^alpha/(2c))(V_k-V_{k-1}) and monotone Abel summation gives |R_j|<=j^alpha/c pathwise; hence sup_{j<=NT}|X_j-M_j|<=2+(NT)^alpha/c=o(N^{(1+alpha)/2}). Functional martingale CLT plus uniform interpolation concludes weak convergence in C([0,T]), including c=1 and arbitrary independent V0. Covariance follows from time-changed Brownian motion. The proof is analytic for all real alpha in (0,1), not extrapolated from finite tests.

## originality

PASS

Best-of-knowledge novelty is the precise single-walk functional convergence under independent absolute-time flips p_k=c k^{-alpha} to Brownian clock t^{1+alpha}/[c(1+alpha)], not the originating superdiffusive MSD law, the Brownian time change as an abstract process, or the classical martingale functional CLT. Full-text comparisons of the exact origin and two plausible broader papers show no direct implication; bounded Resultary searches returned no matching theorem. Priority risks from broader inhomogeneous Markov-chain results remain.

## value

PASS

A path-space invariance principle for a natural, recently studied superdiffusive velocity-reversal model determines all macroscopic finite-dimensional laws, asymptotically independent nonstationary increments and the explicit transport clock, which are not implied by MSD scaling or correlation decay. The nonstandard martingale displacement identity resolves a motivated gap between anomalous second moments and Gaussian process-level behavior. The result is not claimed to extend to alpha=1, nonindependent reversals or a universal class, and its value does not depend on large theorem size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
