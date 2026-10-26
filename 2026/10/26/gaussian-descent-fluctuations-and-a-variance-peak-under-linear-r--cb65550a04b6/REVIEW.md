# Scientific review

## Correctness (C): PASS
The rank-insertion construction gives mutually independent relative ranks and an exact one-dependent sequence of descent indicators. The adjacent joint probability has a finite summation proof; subtracting the known marginals yields the explicit negative adjacent covariance. Because separated indicators are independent, the finite variance is a sum of Bernoulli variances and neighboring covariances. Uniform Riemann-sum convergence holds with \(\lambda>0\), and the displayed antiderivative verifies the limiting variance. Blocking with one-index gaps yields independent block sums; omitted gaps have negligible variance and Lindeberg holds because blocks are of size \(o(\sqrt n)\). The derivative test proves a unique positive maximizer. The packaged checker independently corroborates finite identities with exact arithmetic. Risks: the result does not cover the singular regimes \(\lambda=0\) or \(\lambda=\infty\); no finite experiment is substituted for the asymptotic proof.

## Originality (O): PASS, conditional on historical-priority review
The earliest motivating source here is Bouvel–Nicaud–Pivoteau, arXiv:2409.01692v1, publicly available September 3, 2024. Its Sections 3.2 and 4.1 contain the ingredients and marginal formula; Section 4.2 treats the linear-bias **mean**, whereas Section 4.3 explicitly restricts descent CLTs to **fixed** bias. The 2016 predecessor, arXiv:1605.02905v1, was inspected in its primary 12-page text; its relevant results are first moments, not the growing-parameter variance/CLT. Féray's fixed-parameter Ewens asymptotics and generic 1-dependent CLTs do not themselves state the explicit linear-record-bias coefficient. Searches against published mathematical records and primary literature found no equivalent quantitative assertion, but a broader theorem or uninspected longer Féray text could imply it; this residual risk is not a novelty proof by absence.

## Value (V): PASS
The record-biased model was motivated by analysis of nearly sorted inputs, and the published linear-bias regime previously yielded expected descents and a deterministic permutation limit without a second-order descent fluctuation law. The new theorem supplies the asymptotic uncertainty scale and exact variance for every fixed linear bias, while identifying a nonmonotone response and a unique sharp peak. This is a structural complement to published first-order results, not a parameter substitution or merely a numerical coefficient.

## Scope and limitations
Only \(\theta_n/n\to\lambda\in(0,\infty)\) is covered. Centering uses the exact, previously known mean. The independent-insertion law is prior literature. The finite checker corroborates, but cannot prove, the central limit theorem. Historical priority and independent mathematical review remain open.

Self-review: passed. Independent audit: not yet performed.
