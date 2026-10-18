# Scientific review: exact covariance isometry for fair-tournament score histograms

## Correctness: PASS

For two distinct players, their scores are \((B_v+Z,B_w+1-Z)\) with independent \(B_v,B_w\sim\operatorname{Bin}(n-2,1/2)\) and a fair \(Z\); conditional independence makes the cross-player covariance exactly \(-\delta_f\delta_g/4\). The elementary binomial identity \(\operatorname{Cov}(f(R),R)=(n-1)\delta_f/4\) then turns the sum over ordered player pairs into the claimed residual covariance. Choosing indicator functions recovers every covariance-matrix entry. Binomial normalization gives two orthonormal null directions, so the Pearson-normalized matrix is exactly \(n\) times a rank-\(n-2\) orthogonal projector. Its trace, the variational variance identity and Krawtchouk orthogonality follow without approximation. The edge case \(n=2\) is a zero covariance matrix, as required.

The standalone checker verified 871 exact-rational identities, including enumeration of all 33,866 labeled fair-tournament configurations for \(2\le n\le6\) and independent Krawtchouk/variance checks through \(n=8\). These finite checks test the formulas; the proof provides the all-order argument. No unverified computation is required to establish the theorem.

## Originality: PASS on inspected evidence

Relevant full texts actually inspected were Aldous--Kolesnik's arXiv:1811.06662v1 on tournament mean-score feasibility, Kolesnik--Sanchez's arXiv:2009.09322v1 on score-vector zonotopes, and Claesson--Dukes--Franklín--Stefánsson's arXiv:2209.03925 on *counting* distinct score sequences. None of the inspected theorems states the full random-tournament **score-frequency covariance projector**, the all-function variance residual identity, or its exact Pearson mean. The random Erdős--Rényi degree-distribution paper arXiv:2303.05138 has shared **undirected** edges and does not imply the complementary orientation covariance. Exact preexisting score-sum constraints and Krawtchouk identities are acknowledged, not passed off as new.

Semantic published-finding corpus searches for score-frequency covariance, Pearson-standardized tournaments, binomial/Krawtchouk score modes and degree-histogram equivalents produced nearby records on graph histograms, tournament cycle counts and permutation comparisons, but no retrieved equivalent theorem. Published research claims were compared for mathematical implications: the directed independent-arc degree-pair spectrum and tournament cycle-score predictions address different covariance matrices. Title/parameter differences alone are not the reason for the comparison; the random experiment, random variables and resulting implications differ.

The 2026 Zegers master's thesis on random-tournament score-bin concentrations is a plausible *unresolved full-text comparison*: the repository abstract was read, but the complete thesis was not accessible. It may contain an implicit overlap. The abstract neither settles nor disproves the present projector theorem. Older joint-degree frequency results could also imply portions implicitly; independent historical-priority verification has not been done. The conclusion is best-knowledge originality rather than demonstrated uniqueness.

## Mathematical value: PASS

The complete score histogram is a canonical sufficient descriptive statistic in round-robin tournament analysis, but its bins have dependent counts even though individual player scores have binomial marginals. The theorem determines all covariance directions and the sharp variance of *every* additive score statistic at once. Its rank defect separates the two conservation laws from \(n-2\) equal-variance modes, yielding an exact Pearson expectation rather than an unsupported chi-square calibration. The contrast with independent-binomial sampling gives an interpretable second-order geometry and a reusable basis for statistical uncertainty computations. This is a structural classification, not a choice of arbitrary parameters or a routine marginal expectation.

## Limitations and closest scientific risks

The exact statement applies to independent **fair** tournament orientations. It does not imply distributional independence, a multivariate Gaussian limit, a valid chi-square significance test, or conclusions under heterogeneous Bradley--Terry models. The inaccessible 2026 thesis is the strongest identified possible prior overlap and should receive future independent priority assessment if full text becomes available. No claim of independent audit is made.

Self-review: passed. Independent audit: not yet performed.
