# A parity-sensitive cross-covariance law for unseparated pairs and fixed points

## Finding

Let \(\pi\) be a uniformly random permutation of \(\{1,\ldots,n\}\). For \(1\le i<n\) and \(1\le j\le n\), respectively, define the **succession** and **fixed-point** indicators
\[
A_i=\mathbf 1\{\pi(i+1)=\pi(i)+1\},\qquad F_j=\mathbf 1\{\pi(j)=j\}.
\]
For every integer \(n\ge3\), their entire position-indexed cross-covariance matrix is
\[
\boxed{
\operatorname{Cov}(A_i,F_j)=
\begin{cases}
\dfrac{1}{n^2(n-1)}, & j\in\{1,n,i,i+1\},\\[5pt]
-\dfrac{2}{n^2(n-1)(n-2)}, & j\notin\{1,n,i,i+1\}.
\end{cases}}
\]
In particular, **none** of its entries vanishes: endpoint fixed points and incident fixed points have positive covariance with a succession, while all other interior fixed points have negative covariance.

Let \(M_n\) denote this \((n-1)\)-by-\(n\) matrix. Its rank has the exact parity law
\[
\boxed{\operatorname{rank}M_n=
\begin{cases}
n-1,&n\text{ even},\\
n-2,&n\text{ odd}.
\end{cases}}
\]
For odd \(n\), the alternating succession contrast
\[
Z_n=\sum_{i=1}^{n-1}(-1)^{i-1}A_i
\]
is therefore uncorrelated with **each** individual fixed-point indicator \(F_j\). For even \(n\), there is no nonzero real linear combination of the \(A_i\) with that property. Independently of parity, \(F_1-F_n\) is uncorrelated with every \(A_i\).

Writing \(S_n=\sum_{i=1}^{n-1}A_i\) and \(N_n=\sum_{j=1}^nF_j\), one also has, for \(n\ge3\),
\[
\operatorname{Cov}(S_n,F_1)=\operatorname{Cov}(S_n,F_n)=\frac1{n^2},
\]
\[
\operatorname{Cov}(S_n,F_j)=\frac{2}{n^2(n-1)(n-2)}\quad(2\le j\le n-1),
\qquad
\boxed{\operatorname{Cov}(S_n,N_n)=\frac2{n(n-1)}}.
\]
The two endpoint fixed points consequently carry asymptotically all of this positive aggregate covariance, although the cross-covariance matrix has negative bulk entries.

At the exceptional size \(n=2\), both entries of \(M_2\) equal \(1/4\), its rank is one, and \(\operatorname{Cov}(S_2,N_2)=1/2\).

## Assumptions and scope

The permutation is exactly uniform on the symmetric group, with no conditioning or asymptotic approximation. A succession requires a **positive difference of one** between adjacent images, not just an ascent and not the different condition \(\pi(i)=i+1\). The fixed-point statistic is defined using the *same* permutation. All indices and edge cases are included above. Covariance and rank are over \(\mathbb R\). No claim is made that a vanishing covariance gives independence.

## Proof

For any eligible \(i,j\), elementary symmetry gives \(\mathbb E A_i=\mathbb E F_j=1/n\). We compute \(\mathbb P(A_i=1,F_j=1)\).

**Incident case.** When \(j=i\), the conjunction requires \(\pi(i)=i\) and \(\pi(i+1)=i+1\). When \(j=i+1\), it requires exactly the same two fixed points. Either event has probability \(1/[n(n-1)]\). Subtracting the product of the marginal means gives \(1/[n^2(n-1)]\).

**Nonincident case.** Suppose \(j\notin\{i,i+1\}\). Conditional on \(F_j=1\), the images at positions \(i,i+1\) are a uniformly sampled ordered pair of *distinct* values from \(\{1,\ldots,n\}\setminus\{j\}\). Among the \((n-1)(n-2)\) possible ordered pairs, exactly \(n-1-c_j\) have the form \((a,a+1)\), where \(c_j=1\) if \(j\in\{1,n\}\) and \(c_j=2\) otherwise. Thus
\[
\mathbb P(A_i=1,F_j=1)
=\frac{n-1-c_j}{n(n-1)(n-2)}.
\]
Subtracting \(1/n^2\) and simplifying gives the positive endpoint entry when \(c_j=1\), and the negative interior entry when \(c_j=2\). This proves every displayed covariance entry.

**Rank and parity.** Multiply \(M_n\) by \(n^2(n-1)(n-2)\) to obtain an integer matrix \(B\). Its first and last columns consist entirely of \(n-2\). For an interior column \(j\in\{2,\ldots,n-1\}\), the entries in rows \(j-1,j\) are \(n-2\) and the other entries are \(-2\).

Let \(a=(a_1,\ldots,a_{n-1})\in\mathbb R^{n-1}\) satisfy \(a^\mathsf TB=0\), and write \(s=\sum_i a_i\). The first column forces \(s=0\). For each interior column \(j\),
\[
0=\sum_i a_iB_{ij}=n(a_{j-1}+a_j)-2s,
\]
so \(a_j=-a_{j-1}\) for every \(2\le j\le n-1\). Therefore \(a_i=(-1)^{i-1}a_1\). This alternating vector has zero sum precisely when \(n-1\) is even, i.e. \(n\) is odd. The left kernel consequently has dimension one for odd \(n\) and zero for even \(n\); rank-nullity establishes the rank formula and the alternating covariance cancellation. Identical boundary columns also prove the assertion about \(F_1-F_n\).

**Aggregate formulas.** For \(j=1,n\), each of the \(n-1\) rows contributes \(1/[n^2(n-1)]\), yielding \(1/n^2\). For interior \(j\), exactly two rows contribute positively and the other \(n-3\) negatively, so
\[
\operatorname{Cov}(S_n,F_j)
=\frac{2}{n^2(n-1)}-
\frac{2(n-3)}{n^2(n-1)(n-2)}
=\frac{2}{n^2(n-1)(n-2)}.
\]
Summing over all fixed-point indices proves \(\operatorname{Cov}(S_n,N_n)=2/[n(n-1)]\). For \(n=2\), direct inspection of the identity and transposition proves the stated exception.

## Verification

The accompanying self-contained \(\texttt{verify.py}\) independently enumerates every permutation at sizes \(n=2,\ldots,8\), reconstructing each indexed covariance from integer joint-event counts and checking the rank and aggregate identities exactly with rational arithmetic. It separately constructs the scaled integer matrix and verifies its parity-sensitive rank for \(n=3,\ldots,40\). To reproduce, run \(\texttt{python3 verify.py}\) with Python 3; it requires no third-party packages. These finite computations corroborate but do not replace the general proof above.

## Relationship to prior work

Diaconis, Evans, and Graham proved that the random set of succession **positions** in \(\{1,\ldots,n-1\}\) is equal **in distribution** to the set of fixed points restricted to those labels. Their result determines the two marginal random-set laws, not the joint cross-covariance of these two sets when formed from the *same* permutation. The present matrix and its rank change concern precisely that same-permutation dependence.

Chen and Fu subsequently refined succession/fixed-point equidistribution using grammatical bijections and investigated joint distributions involving excedances or jumps. These equidistribution and aggregate-statistic identities likewise do not assert the position-indexed cross-covariance or its odd/even rank dichotomy. Related work on adjacencies jointly with descents studies different paired observables.

## Limitations

The claim is for exactly uniform permutations. Its covariance identities are second-order statements, not full joint-distribution formulas or independence results. The asymptotic observation about endpoint dominance follows from the displayed exact sums, not a distributional limit theorem. A more general existing refined enumeration could imply the matrix after differentiation; that priority risk remains despite the literature comparisons. No independent scientific audit has been performed.

## References

1. P. Diaconis, S. N. Evans, R. Graham, *Unseparated pairs and fixed points in random permutations*, Berkeley Statistics Technical Report 822 (August 2013), https://statistics.berkeley.edu/tech-reports/822 ; arXiv:1308.5459 (August 2013), https://arxiv.org/abs/1308.5459 .
2. W. Y. C. Chen and A. M. Fu, *A Grammar of Dumont and a Theorem of Diaconis-Evans-Graham*, arXiv:2402.02743 (2024), https://arxiv.org/abs/2402.02743 .
3. A. Burstein, *On the joint distribution of adjacencies, descents and some Mahonian statistics*, Discrete Mathematics & Theoretical Computer Science (2010), https://dmtcs.episciences.org/2846 .
