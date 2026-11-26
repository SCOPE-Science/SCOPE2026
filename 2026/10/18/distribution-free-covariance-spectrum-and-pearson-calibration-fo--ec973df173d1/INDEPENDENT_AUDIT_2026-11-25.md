# Independent mathematical audit

## correctness

PASS

Let r_a=sqrt(p_a), P0 the projector on r tensor r, and let A have entries A_(ab,cd)=r_a delta_(bc) r_d. Directly counting zero and one lags gives W_L=L(I-P0)+(L-1)(A+A^T-2P0): longer lags do not overlap. A sends g tensor r to r tensor g and annihilates the sector with second tensor factor perpendicular to r; in particular A(r tensor r)=r tensor r. Thus constants vanish, the doubly perpendicular sector has eigenvalue L, and the two additive placements for every g perpendicular to r form a block with diagonal L and off-diagonal L-1. Its antisymmetric and symmetric eigenvalues are 1 and 2L-1, each q-1 times. Their dimensions and the (q-1)^2 interaction dimension exhaust the pair space. The unit mode is exactly a telescoping endpoint difference of pair scores. Positive D transfers the rank to the unweighted covariance by congruence; the condition number 2L-1 is for W_L, not in general for the raw covariance. At L=1 all positive eigenvalues coincide. Taking tr(W_L)/L gives q^2-1. The bounded centered 1-dependent vector satisfies a fixed-dimensional CLT, also in the degenerate directions by scalar projections. The limiting Pearson-normalized Gaussian has variances 0,0,1,2 in the four sectors. Taking its squared norm gives the stated sum of two independent chi-squares. The arguments require fixed strictly positive known p and fixed q for the limit, and do not assert a distribution-free Q_L law at finite L.

## originality

PASS

The supported distinction is the exact probability-invariant Pearson-weighted spectrum for arbitrary strictly positive p at finite L, notably the nonzero bounded endpoint sector; the exact trace and arbitrary-p calibration follow. The uniform asymptotic spectrum and uniform Pearson limit are already implied by a close indexed k-word collision theorem. Its product-score method also essentially contains the finite-L uniform calculation and suggests extending the basis argument to nonuniform p. Its stated covariance theorem is asymptotic and uniform; it is not a general positive-p finite weighted spectral theorem. The broad Markov generating-function result encodes the unweighted joint pair counts, but evaluating the p-weighted covariance and identifying its invariant sectors requires a separate computation. No novelty is assigned to pair-count moments in general or to the uniform limit in isolation.

## value

PASS

The ungrouped overlapping-pair statistic is a natural goodness-of-fit diagnostic. The exact bounded-variance endpoint sector versus two distinct bulk sectors explains why the ordinary multinomial calibration is wrong despite its correct mean. The effect persists for arbitrarily nonuniform positive category laws after Pearson weighting, with explicit finite spectral information in addition to an asymptotic correction. That is useful beyond the known uniform collision setting or a computation of pair-count moments alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
