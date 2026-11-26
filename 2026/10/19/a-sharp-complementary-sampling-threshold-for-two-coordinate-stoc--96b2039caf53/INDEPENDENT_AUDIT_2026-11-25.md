# Independent mathematical audit

## correctness

PASS

For A_i=2P_iJ each one-step matrix is I−ηA_j+η²A_jA_i. A_i²=0, while the two complementary products are −4 times their respective corrector-coordinate projections. The two same-coordinate Gram matrices average to (1+2η²)I; the complementary average is (1−2η²+8η⁴)I. Weighting by the balanced pair probabilities and conditioning on the current iterate gives the exact factor q_r and its kth power. q_r−1=2η²(1−2r+4rη²); at zero step or the positive endpoint the error moment is constant, not converging to the saddle for a nonzero start. Mean iteration uses the averaged matrix (1−2rη²)I−ηJ, whose squared norm factor is (1−2rη²)²+η². At r=1/2 this tends to zero under iteration precisely for 0<η<1 despite second-moment growth for every η>0. Marginal oracle unbiasedness is for fixed inputs; no conditional unbiasedness at the random predictor is assumed for coupled pairs. The supplied check was inspected but not run. /workspace/branches/61ea2ef6-f9c3-4247-b7c9-d90de9e9e5b0/replay_frozen_coordinate_gram.py is a separate 1,760-case exact-rational replay with boundary checks; continuum validity comes from the symbolic Gram identities.

## originality

PASS

The closest inspected coupling frontier concerns multiplying a full skew field by a scalar slope. Its nonzero oracle matrices have rank two and its transition matrices lie in the commuting algebra span{I,J}; neither describes the rank-one nilpotent coordinate factors or their noncommuting products. Prior divergence for independent stochastic extragradient is not the novelty. The supported distinction is the exact necessary-and-sufficient pairing window and simultaneous mean/second-moment separation for the two-stage single-coordinate oracle.

## value

PASS

This is a complete stability classification of a minimal nontrivial one-coordinate-per-call model, with identical call marginals but qualitatively different second-moment behavior depending on pairing. The mean/moment split shows why a first-moment analysis misses instability. The practical interpretation is limited to this bilinear test problem and does not claim a general optimizer guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
