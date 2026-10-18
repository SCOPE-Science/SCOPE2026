# Two-extreme universality for record–consecutive-pattern covariance

## Finding
Fix a consecutive relative-order pattern \(\sigma\) of length \(k\). In an otherwise uniform random permutation, the covariance between the number of left-to-right records and the indicator that \(\sigma\) occurs in a given window has an exact, dimension-free formula. Far from the start of the permutation its sign depends **only on whether the second largest or the largest pattern entry comes first**, with an exact universal inverse-square coefficient:
\[
\lim_{j\to\infty}j^2\operatorname{Cov}(R_n,I_{j,\sigma})=
\frac{k(k-1)}{2k!}\bigl(2\mathbf1\{\operatorname{pos}_\sigma(k-1)<\operatorname{pos}_\sigma(k)\}-1\bigr),
\qquad n\ge j+k-1.
\]
The covariance does not depend on the ambient length \(n\) once the window fits.

## Assumptions and scope
All integers \(k\ge2\), \(j\ge1\), and \(n\ge j+k-1\) are allowed, and \(\sigma\in S_k\) is fixed. Sample a uniform random permutation \(\Pi\in S_n\). Define the strict upper-record count
\[R_n=\sum_{i=1}^{n}\mathbf1\{\Pi_i>\Pi_h\text{ for all }h<i\}.\]
Define \(I_{j,\sigma}\) as the indicator that the relative ranks of \(\Pi_j,\ldots,\Pi_{j+k-1}\) are precisely \(\sigma_1,\ldots,\sigma_k\). Write \(\operatorname{Rec}(\sigma)\) for the set of prefix-record positions in the pattern (the first position always qualifies), and define
\[Q_s(j,k)=\prod_{h=s}^{k}\frac{h}{j+h-1}\qquad(1\le s\le k).\]

## Proof
Represent the permutation as relative ranks of independent continuous uniform observations \(U_1,\ldots,U_n\). Their order has exactly the uniform permutation distribution. The record indicator at index \(i\) has expectation \(1/i\); the window pattern occurs with probability \(1/k!\).

For indices \(i<j\), the record event depends only on previous observations, and the relative order of the disjoint window is independent of it. For \(i\ge j+k\), condition on all observations before index \(i\). The rank of the new observation among the first \(i\) is uniform independently of every relative-order event involving the first \(i-1\), so the record event is independent of the pattern. Therefore only indices within the window contribute to covariance.

Conditional on the window having relative order \(\sigma\), its \(k\) order statistics have their usual uniform-order-statistic distribution and are independent of the window's rank permutation and the preceding \(j-1\) observations. At position \(j+r-1\), being a record is impossible unless \(r\in\operatorname{Rec}(\sigma)\). If that position has window rank \(s=\sigma_r\), it is a record precisely when the previous \(j-1\) observations all lie below the \(s\)-th of those \(k\) order statistics. The latter order statistic is \(\operatorname{Beta}(s,k+1-s)\), whose \((j-1)\)-st moment equals
\[
\mathbb E U_{(s)}^{j-1}=
\frac{(s)_{j-1}}{(k+1)_{j-1}}=
\frac{k!}{(s-1)!}\frac{(j+s-2)!}{(j+k-1)!}=Q_s(j,k).
\]
Subtracting the unconditional record expectations over precisely the window yields the exact covariance
\[
\boxed{\operatorname{Cov}(R_n,I_{j,\sigma})=
\frac1{k!}\left[\sum_{r\in\operatorname{Rec}(\sigma)}Q_{\sigma_r}(j,k)-\sum_{h=0}^{k-1}\frac1{j+h}\right].}
\]

For fixed \(k\), only ranks \(k\) and \(k-1\) contribute terms of order at least \(j^{-2}\):
\[Q_k(j,k)=\frac{k}{j+k-1}=\frac{k}{j}-\frac{k(k-1)}{j^2}+O_k(j^{-3}),\]
\[Q_{k-1}(j,k)=\frac{k(k-1)}{(j+k-2)(j+k-1)}=\frac{k(k-1)}{j^2}+O_k(j^{-3}),\]
while every \(Q_s(j,k)\) with \(s\le k-2\) is \(O_k(j^{-3})\). The rank \(k\) always contributes, whereas rank \(k-1\) contributes if and only if it appears before rank \(k\). Finally,
\[\sum_{h=0}^{k-1}\frac1{j+h}=\frac{k}{j}-\frac{k(k-1)}{2j^2}+O_k(j^{-3}).\]
Combining proves the claimed two-extreme sign law and its universal coefficient, uniformly in ambient \(n\ge j+k-1\).

For the illustrative consecutive pattern \(\sigma=132\), substitution gives
\[\operatorname{Cov}(R_n,I_{j,132})=-\frac{3j-4}{6j(j+1)(j+2)},\]
which is positive at \(j=1\) and negative for all integers \(j\ge2\).

## Verification
The standalone `verify.py` executes exact-rational comparisons between the formula and independently enumerated permutations through order six, multiple general-pattern large-index consistency checks, and the exact sign-switch example. It prints the check count on success. These finite checks corroborate but do not replace the proof for arbitrary pattern length and window position. Run using `python3 verify.py`; no nonstandard packages are required.

## Relationship to prior work
The probabilistic study of fixed-pattern statistics is well established: Janson, Nakamura and Zeilberger treat moments of classical (not necessarily consecutive) pattern occurrences; Janson (2014) studies 132-avoiding permutations; Elizalde surveys the structure and counting of consecutive pattern occurrences. Those sources motivate the natural observables and their asymptotics. The present assertion instead couples the *global* record count of an **unrestricted** uniform permutation to a *position-specific consecutive-pattern indicator*, producing an exact covariance and a two-largest-entry universality law. General results for pattern-count marginals or aggregate bivariate laws do not automatically determine this positional covariance. Existing record/descents dependence results may imply particular length-two instances but do not directly imply the fixed-arbitrary-length two-extreme law.

## Limitations
The statement concerns covariance, not stochastic independence or monotone likelihood ratio. The limit keeps the pattern length fixed while moving the window farther from the beginning; it is not uniform if \(k\) grows with \(j\). Finite small-position signs need not equal the eventual sign. The formula is an exact mathematical deduction; the assertion that its general two-extreme classification is absent from all earlier literature is subject to independent scholarly confirmation.

## References
1. S. Janson, *Patterns in random permutations avoiding the pattern 132*, 2014 preprint (first posted January 22, 2014), arXiv:1401.5679, https://arxiv.org/abs/1401.5679 (primary 60C05).
2. S. Elizalde, *A survey of consecutive patterns in permutations*, 2015 preprint, arXiv:1504.07265, https://arxiv.org/abs/1504.07265.
3. S. Janson, B. Nakamura, D. Zeilberger, *On the asymptotic statistics of the number of occurrences of multiple permutation patterns*, 2013 preprint, arXiv:1312.3955, https://arxiv.org/abs/1312.3955.
