# Independent mathematical audit

## correctness

PASS

For the repaired claim, conditioning on the tree and marks through vertex j gives E[C_n|F_j]=M_n(p)C_j/M_j(p). The root-attachment indicator I_j is independent of earlier history, and E[I_j X_j]=p/(j-1). The local covariance splits into M_n times a telescoping reciprocal-product difference minus p/((j-1)(j-1+p)); summing proves the finite input identity, including p=0 and p=1. For lambda=(1-p)log n bounded, expansion of the log product has a uniform error bounded by a constant times (1-p)^2 times the convergent inverse-square sum, and the controlled tails of T_n(p) yield uniform convergence to zeta(2)-1. The global bound e^(-lambda(H_n-1)/log n)(log n/n+lambda) excludes both 0 and infinity as limits of rescaled maximizers, which exist by continuity. Compact-window convergence and the unique maximum of lambda exp(-lambda) then identify every maximizing sequence and the peak. In the frozen original the weighted subset lemma correctly uses log-concavity of elementary symmetric functions and conditions separately on the last-item indicator, allowing a nested full-vector coupling with shared alternative parents and marks. Its strict tail is also exactly 1-(1-p)^d. The rising factorial identity for the root cluster gives 2M_n(2p)-M_n(p)-M_n(p)^2 for variance, with positive leading coefficient for fixed p<1 by strict digamma increase, verifying the original decorrelation calculation.

## originality

PASS

The final claim is restricted to near-critical covariance as a function of the retention parameter and its global maximum and optimizer. The exact covariance formula, original-degree coupling and fixed-retention laws are not claimed as new. The strongest indexed predecessor supplies the same finite input but expressly gives only fixed-p asymptotics. Published critical-window cluster laws are for a marginal, not this smaller covariance response. The sharp covariance peak, constant, and localization of all maximizers survive the comparison.

## value

PASS

The repaired theorem determines where the joint response is strongest in a natural stochastic model: it vanishes at both deterministic retention endpoints and has a peak on a shrinking scale invisible to fixed-p asymptotics. The exact (zeta(2)-1)/e factor and localization of every maximizer distinguish the size and location of that effect, rather than reprinting a finite formula or optimizing a numerical grid.

The dated certificate retains the supplied scientific assessment, sources and limitations.
