# Independent mathematical audit

## correctness

PASS

Algorithm 1 and Eq. (7) use one shared Gaussian prefix matrix and the fixed inverse r/a, where a is the squared norm of the first r entries of the design column. The strict upper hypothesis on m_j avoids the source's exact-gradient switch. The coefficient of the standardized head response Z in x_t is a^(−1/2)P_t(1/a); the leading coefficient of P_t is the product of −μr c_j/m_j, with c_j the squared norms of the extra rows, each positive almost surely. The rest is polynomial in 1/a of degree at most t. All coefficients have finite positive moments and are independent of a; finite-sum bounds give integrability when E[a^(−p(t+1/2))] is finite. For an independent lower-bound argument, condition on all design-column Gaussians. Then x_t is centered normal, and the disjoint head and extra response coordinates imply variance at least P_t(1/a)^2/a. For each fixed extra design block with nonzero leading coefficient, the conditional p-th absolute moment therefore bounds a positive multiple of a^(−p(t+1/2)) on a sufficiently small interval. Integration against the chi-square density proves divergence for r≤p(2t+1), logarithmic at equality, also for t=0. All finite iterates exist for a>0. For one step the conditional variance is (1−qc/a)^2/a+q²c/a², c~χ²_k independent of a. Substituting E[c]=k, E[c²]=k(k+2) and the three inverse chi-square moments gives the stated formula exactly. Independent replay `python3 /workspace/checks/frozen_replay.py 1` passed 81 exact rational response-weight updates, including the leading-power scaling and one-step variance. The replay is not the integrability proof.

## originality

PASS

The inspected sources supply the algorithm, underlying inverse-moment facts, or distinct cutoffs for one-shot sketches and iterative Hessian sketching. They do not give or imply the sharp all-real-p threshold for source-initialized nested Gaussian IDS on this instance or its nonasymptotic one-step mean-square formula. The novelty claim is limited to that combination and scope, not inverse-chi-square tails or moment thresholds in general.

## value

PASS

The simplest full-rank least-squares example already separates almost-sure existence from unconditional risk for the published algorithm. The width budget to obtain a given moment rises exactly with the iteration count, and no strictly oversized non-full finite gradient prefix changes that budget. For example r=5 can give finite initialization mean square and infinite one-step mean square. This is a sharp warning about which error summaries exist, not merely a different constant in a convergence rate or an isolated bad random seed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
