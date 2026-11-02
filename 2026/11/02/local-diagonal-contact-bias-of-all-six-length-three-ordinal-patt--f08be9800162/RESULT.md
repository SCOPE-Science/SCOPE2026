# Local diagonal-contact bias of all six length-three ordinal patterns

## Finding

Let \(\pi\) be a uniformly sampled permutation of \([n]\), with \(n\ge3\). Define its fixed-point indicators \(F_j=\mathbf1\{\pi(j)=j\}\) and fixed-point count \(F=\sum_{j=1}^nF_j\). For \(1\le i\le n-2\) and \(\sigma\in S_3\), let \(A_{i,\sigma}\) be the event that the three consecutive entries \(\pi(i),\pi(i+1),\pi(i+2)\) have relative-order pattern \(\sigma\). Set \(Q_n=n(n-1)(n-2)\).

**Complete local covariance law.** If \(j\notin\{i,i+1,i+2\}\), then \(F_j\) and \(\mathbf1_{A_{i,\sigma}}\) are independent. Otherwise, put \(t=j-i+1\) and \(r=\sigma_t\) (the rank at the fixed position). Then

\[
\operatorname{Cov}(F_j,\mathbf1_{A_{i,\sigma}})
=\frac1n\left[\frac{\binom{j-1}{r-1}\binom{n-j}{3-r}}{(n-1)(n-2)}-\frac16\right].
\]

Consequently, for every stated \(n,i,\sigma\),

\[
\operatorname{Cov}(F,\mathbf1_{A_{i,\sigma}})
=\frac{b_\sigma(n,i)}{Q_n},
\]

where the following is the **entire six-pattern table**:

| Pattern \(\sigma\) | Numerator \(b_\sigma(n,i)\) |
|---|---|
| \(123\) | \(n-1\) |
| \(132\) | \(-3i+2n-3\) |
| \(213\) | \(3i-n\) |
| \(231\) | \(3i-2n+2\) |
| \(312\) | \(-3i+n-1\) |
| \(321\) | \(3-n\) |

In particular,

\[
\mathbb E[F\mid A_{i,\sigma}]
=1+\frac{6b_\sigma(n,i)}{Q_n}.
\]

For \(n\ge5\), every one of the four nonmonotone patterns has a covariance that changes strict sign between the leftmost and rightmost window, and each profile is affine in its position (so it has at most one zero). The \(123\) covariance is positive for all \(n\ge3\), whereas the \(321\) covariance is negative for \(n\ge4\) and is zero for \(n=3\).

There is an exact positional cancellation: at **every** feasible window,

\[
\operatorname{Cov}(F,\mathbf1_{A_{i,132}}+\mathbf1_{A_{i,231}})
=\operatorname{Cov}(F,\mathbf1_{A_{i,213}}+\mathbf1_{A_{i,312}})
=-\frac1{Q_n}.
\]

Thus the aggregate number of interior peaks, and likewise the aggregate number of interior valleys, has covariance \(-1/[n(n-1)]\) with \(F\). The position-resolved six-way law, rather than the aggregate peak covariance by itself, is the principal finding.

## Assumptions and scope

The only probability model is the uniform distribution on all \(n!\) one-line permutations of \([n]\), for integers \(n\ge3\). A relative-order pattern records the three within-window ranks, from smallest rank \(1\) to largest rank \(3\). The fixed-point count is in the *same permutation*, not an independently sampled permutation or its inverse. Every equality and sign claim is finite-sample, exact, and includes all indicated boundary cases.

## Proof

1. The uniform law gives \(\Pr(F_j=1)=1/n\), \(\Pr(A_{i,\sigma})=1/6\), and \(\mathbb E[F]=1\). Conditioned on \(\pi(j)=j\), the map on the other \(n-1\) positions is a uniform bijection onto the other \(n-1\) values. Thus for a window avoiding position \(j\), all six relative-order patterns remain equally likely: the claimed independence follows.

2. Suppose \(j\in\{i,i+1,i+2\}\), occupying position \(t=j-i+1\) and having prescribed rank \(r=\sigma_t\). Conditional on \(\pi(j)=j\), the two remaining window values are a uniformly ordered pair of distinct elements of \([n]\setminus\{j\}\), with \((n-1)(n-2)\) possibilities. The rank pattern requires choosing exactly \(r-1\) values below \(j\) and \(3-r\) values above \(j\). There are precisely \(\binom{j-1}{r-1}\binom{n-j}{3-r}\) possibilities: once the two values are chosen, their assignment to the two remaining positions is uniquely fixed by \(\sigma\). This proves the conditional probability formula, including zero-binomial boundary cases. Subtracting the product of marginals yields the local covariance law.

3. Covariance is additive, so only the three positions in the window contribute to \(\operatorname{Cov}(F,\mathbf1_{A_{i,\sigma}})\). Substitute \(j=i,i+1,i+2\), with the corresponding ranks \(\sigma_1,\sigma_2,\sigma_3\), into the preceding expression. Expanding \(\binom{x}{2}=x(x-1)/2\) in the six cases and collecting terms yields the displayed table over the common denominator \(Q_n\). It also shows the row sum is zero, as must hold because exactly one of the six patterns occurs at each window. Since \(\Pr(A_{i,\sigma})=1/6\), the conditional-mean identity follows from \(\mathbb E[F]=1\).

4. In the four nonmonotone rows, the numerators have nonzero slope \(\pm3\). At positions \(i=1\) and \(i=n-2\), respectively, their numerator pairs are \((2n-6,3-n)\) for \(132\), \((3-n,2n-6)\) for \(213\), \((5-2n,n-4)\) for \(231\), and \((n-4,5-2n)\) for \(312\). These are strictly of opposite signs for \(n\ge5\). The signs of the monotone rows are immediate. The identities \(b_{132}+b_{231}=-1\) and \(b_{213}+b_{312}=-1\) prove the peak and valley cancellation formulas. Summing over all \(n-2\) windows proves their aggregate covariances.

## Verification

The accompanying standalone \(\texttt{verify.py}\) uses only the Python standard library. It checks the full position-specific formula algebraically by exact integer and rational arithmetic for all \(3\le n\le50\) and each feasible window and rank pattern; it also checks the peak/valley cancellation and partition-of-patterns identities. Independently, it enumerates **every** permutation for \(3\le n\le8\), checking the complete fixed-point count covariance and every site-by-site covariance, including the exact remote independence implication at the level of two-event probabilities. It passes **32,802 exact assertions** when run with \(\texttt{python verify.py}\). These finite tests are independent corroboration; the proof above establishes the all-size theorem.

## Relationship to prior work

The fixed-point-set viewpoint and permutation coupling in Diaconis–Evans–Graham (2013) concern increasing successions and fixed points, not six local ordinal-pattern covariances. Elizalde (2015) surveys the classical length-three consecutive patterns and their peak and valley interpretations. Fulman–Kim–Lee (2019) analyze peaks in fixed conjugacy classes. Gessel–Zhuang (2020), especially Section 6.1 and Theorem 6.1, gives broad generating functions for joint **aggregate** peak, descent, and fixed-point counts, and consequently subsumes aggregate moment deductions. Those statistics do not distinguish the two types of a local peak \(132\) and \(231\), which have the same local ascent/descent pattern yet different fixed-point interactions. The present complete **position-specific six-way covariance matrix** is not established by those inspected statements.

The published result *Boundary localization of fixed-point–descent dependence in a uniform permutation* provides a nearest small-window analogue for two-entry comparisons; it does not contain the new three-entry peak/valley separation or the affine sign-transition profiles. Historical implicit coverage beyond the inspected sources remains a risk; no claim of absolute priority is made.

## Limitations

The law concerns uniform permutations, first mixed moments, and windows of length exactly three. It does not imply independence between the total fixed-point and peak counts, specify their complete joint law, or establish a hypothesis-testing power gain. The aggregate peak covariance can be extracted from stronger classical global generating functions, so it is not claimed as a separate original theorem. The novelty comparison is conditional on the sources inspected; unlocated earlier equivalent local results could affect priority. Independent scientific audit has not been performed.

## References

- P. Diaconis, S. N. Evans, R. Graham, *Unseparated pairs and fixed points in random permutations*, arXiv:1308.5459, first submitted 2013-08-25. https://arxiv.org/abs/1308.5459
- S. Elizalde, *A survey of consecutive patterns in permutations*, arXiv:1504.07265, first submitted 2015-04-27. https://arxiv.org/abs/1504.07265
- J. Fulman, G. B. Kim, S. Lee, *Central limit theorem for peaks of a random permutation in a fixed conjugacy class*, arXiv:1902.00978, first submitted 2019-02-03. https://arxiv.org/abs/1902.00978
- I. M. Gessel, Y. Zhuang, *Plethystic formulas for permutation enumeration*, arXiv:2001.00654, first submitted 2020-01-02, Section 6.1. https://arxiv.org/abs/2001.00654
- C. Reutenauer, *Number of Permutations with Given Descent Set and Cycle Structure*, Séminaire Lotharingien de Combinatoire B21h (1989), https://www.mat.univie.ac.at/~slc/s/s21reut.html
