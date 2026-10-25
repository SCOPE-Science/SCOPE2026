# Independent mathematical audit

## correctness

PASS

For uniform recursive-tree attachment, conditional updates T_(n+1)=T_n+1+D_K, L_(n+1)=L_n+1-I(K leaf), and A_(n+1)=A_n+1+D_K-I D_K yield ET_n=n(H_n-1), EL_n=n/2, EA_n=nH_n/2-n/4. The conditional covariance plus total covariance reduces to c_(n+1)=c_n-1/4 with c_2=0, so Cov(T_n,L_n)=-(n-2)/4 for all n>=2. W_n=(T_n-ET_n)/n has orthogonal increments (D_K-T_n/n)/(n+1) and square-summable increments, proving its nondegenerate L2 and a.s. limit. L_n has Eulerian 1+descents law; bounded 1-dependent descents give N(0,1) at sqrt(n/12). Crucially, at fixed m the number of surviving leaves labeled >m is independent of the parent-history F_m, while the <=m contribution is bounded by m. Approximate any bounded F_infinity statistic by its F_m conditional expectation and pass m then n to show mixing; replacing W by W_n gives joint independence. Independently enumerated all parent choices n=2..8 matched the exact rational covariance. Finite checks are not the mixing proof.

## originality

PASS

Best-of-knowledge originality: explicit cross-statistic theorem not established by the inspected primary statements; compare four mathematical implications below. No guarantee of absolute historical priority.

## value

PASS

A joint theorem for the natural tree shape statistic (number of leaves) and global search-cost statistic (total depth), whose fluctuations occur on incompatible sqrt(n) and n scales. The strong mixing conclusion against the ENTIRE fixed growth history is not a routine consequence of vanishing Pearson correlation; it explains why a non-Gaussian path-cost martingale limit decouples from Gaussian leaf noise while finite trees remain negatively dependent. The exact -1/4-per-vertex covariance is additionally useful for small-sample calibration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
