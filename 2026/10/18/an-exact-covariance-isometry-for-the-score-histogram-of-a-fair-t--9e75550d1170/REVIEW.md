# Independent mathematical audit

## correctness

PASS

For K=n-1 >=1, every ordered distinct pair of players has (S_v,S_w) = (B_v+Z,B_w+1-Z) in distribution with independent Bin(K-1,1/2) variables and a single independent fair Bernoulli Z. For arbitrary finite-support f,g, conditional independence gives -delta_f delta_g/4 off-diagonal covariance; the individual diagonal is Cov(f(R),g(R)) for R~Bin(K,1/2). A direct Bernoulli-summand expansion gives Cov(f(R),R)=K delta_f/4, so summing the n diagonal and n(n-1) ordered off-diagonal contributions yields the stated n-times residual covariance after projecting f and g off 1,R. For indicator test functions the exact histogram formula is Sigma=n(P-pp^T)-nK dd^T/4, d_j=2(2j-K)p_j/K. Therefore P^{-1/2}Sigma P^{-1/2}=n(I-uu^T-ww^T), u=sqrt(p), w=(2j-K)sqrt(p)/sqrt(K), with orthonormal u,w. Rank and eigenvalues are exactly 0 twice and n with multiplicity n-2 (including n=2 zero covariance). Trace gives EX_n=n-2, residual projection gives the sharp minimum over affine functions and equality cases, and the binomial generating function E[(1-z)^R(1+z)^{K-R}(1-y)^R(1+y)^{K-R}]=(1+zy)^K establishes orthogonal Krawtchouk modes of degrees >=2. I independently reconstructed the formulas, inspected the exact verify.py code, exhaustively recomputed all 33,866 labeled orientations of K_2 through K_6 and their full covariance matrices, and rationally checked the projector identity, constraints, Pearson trace and all Krawtchouk cross-covariances for each n=2..10. My first independent checker had a Krawtchouk-index coding typo that produced a failure at n=3; after correcting comb(K-j,r-t), every check passed. This debugging is not scientific contradiction. The universal statement is proved analytically, not by finite enumeration.

## originality

PASS

Best-of-knowledge original exact all-n covariance-isometry finding after direct comparison of four mathematical reformulations, stronger coverage, exact score tables and prior-result implications. A full relevant geometric primary article gives feasible score/mean-score zonotopes, not orientation-weighted second moments; other accessible source statements and Resultary hits do not imply the projector. Crucially, the 2026 Zegers thesis explicitly develops score-bin concentration/CLT and could contain this finite-n covariance identity; only its full abstract was read, the complete text could not be obtained, and overlap remains a named priority risk. Inaccessibility alone does not force FAIL, but it is not proof of novelty. This verdict does not claim exhaustive historical priority or independent publisher certification.

## value

PASS

The full score histogram is a natural statistic of uniformly oriented complete tournaments, with non-independent counts despite binomial one-player marginals. Classifying its entire Pearson-standardized covariance as exactly n times a rank-(n-2) projector isolates both deterministic conservation laws and proves an equal-variance structure for every higher-order Krawtchouk score contrast. The all-functions residual-variance identity and exact finite-sample Pearson mean n-2 provide sharp reusable second-moment tools for comparing tournament scores and assessing naive independence benchmarks. This is a natural, parameter-uniform structural classification rather than a contrived numeric slice, a mere n=small experiment, or the known fact that the total number of wins is fixed. Its significance is bounded to second moments; no goodness-of-fit calibration is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
