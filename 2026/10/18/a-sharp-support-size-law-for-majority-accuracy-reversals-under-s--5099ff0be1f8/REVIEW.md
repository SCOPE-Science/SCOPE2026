# Independent mathematical audit

## correctness

PASS

Reconstructed the conditional two-voter gain/loss probabilities: the sole flips occur at original r and r+1 successes, giving exactly binom(2r+1,r)(2p-1)[p(1-p)]^(r+1). Grouping equal lambda=p(1-p) and discarding zero combined coefficients gives an exponential polynomial with d distinct positive bases. Rolle induction after dividing by the smallest exponential yields at most d-1 real zeros, and each strict sampled reversal forces a different real zero; d=0 gives identically zero increments, d=1 gives no reversals. For every d>=2, Q_d(z)=z*prod_{j=0}^{d-2}(z-t^(2j+3)) with 0<t<1/2 has d nonzero alternating coefficients, and its roots separate z_r=t^(2r+2) for the first d values. Choosing p_i=(1+sgn(c_i)*sqrt(1-4t^(2i)))/2 and w_i proportional to |c_i|/sqrt(1-4t^(2i)) gives valid 0<p_i<1 and w_i>0 and realizes increments binom*Q_d(z_r)/W; the t->0 limit sends favorable state weight, favorable competence, and E[P] to 1. Conditional iid common-P covariance Var(P)>0 since the constructed states differ. The infinite claim follows from these symbolic proofs, not finite numerics.

## originality

PASS

Best-of-knowledge sharp attainable d-1 reversal theorem for finite de Finetti mixtures is not implied by materially inspected primary sources. The exact binomial step identity and exponential Chebyshev bound are acknowledged classical; the new supported implication is the sharp effective-support classification plus lawful positive-correlation, high-average-competence attaining construction. The full closest 2007 dependent-jury paper remains inaccessible and creates explicit qualified-priority risk.

## value

PASS

A sharp natural quantitative law for correlated Condorcet-style juries: the number of changes in the benefit of enlarging an odd jury by two is controlled by effective distinct latent variability scales, not marginal competence or pairwise correlation alone. The explicit construction proves arbitrarily many reversals remain possible even with a highly favorable average voter and positive association, resolving a motivated failure mode of naive independent-voter monotonicity. The exact d−1 boundary is useful for assessing heterogeneous-information election or aggregation models. This is not claimed for strategic voters, latent continuous distributions, or nonexchangeable dependence; classical exponential-zero theory is a proof component, not the value claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
