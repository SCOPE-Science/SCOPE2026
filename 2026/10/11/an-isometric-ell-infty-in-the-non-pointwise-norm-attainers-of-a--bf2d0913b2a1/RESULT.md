# An isometric \(\ell_\infty\) in the non-pointwise-norm-attainers of a discrete metric family

## Finding
For every sequence \(\alpha=(\alpha_n)_{n\ge1}\) of real numbers satisfying
\[
0<\alpha_{n+1}\le\alpha_n\le\frac13,\qquad \lim_{n\to\infty}\alpha_n=0,
\]
let \(M_\alpha=\mathbb N\) have the distance
\[
d_\alpha(n,m)=2-\alpha_{\min\{n,m\}}-2\alpha_{\max\{n,m\}}\quad(n\ne m),\qquad d_\alpha(n,n)=0.
\]
Then the set consisting of zero and the real-valued Lipschitz functions on \(M_\alpha\) that **fail pointwise norm attainment** contains a closed linear subspace isometric to \(\ell_\infty\). More quantitatively, an explicit linear isometry \(T:\ell_\infty\to\operatorname{Lip}_0(M_\alpha)\) satisfies, for all \(a\in\ell_\infty\setminus\{0\}\) and all \(n\ge1\),
\[
\sup_{m\ne n}\frac{|T(a)(n)-T(a)(m)|}{d_\alpha(n,m)}\le
\left(1-\frac{\alpha_n}{2}\right)\|a\|_\infty
<\|T(a)\|_{\mathrm{Lip}}=\|a\|_\infty.
\]
In particular, the metric from Example 4.10 of Choi–Jung–Lee–Roldán (2023) corresponds to \(\alpha_n=3^{-n}\) and has the same conclusion.

## Assumptions and scope
All scalars are real. Let \(\operatorname{Lip}_0(M)\) denote Lipschitz functions vanishing at the distinguished point \(1\), with the usual Lipschitz seminorm as norm. A function \(f\) is *pointwise norm attaining* if at some \(n\in M\) the supremum of absolute slopes from \(n\) equals its global Lipschitz norm. Write \(\operatorname{PNA}(M)\) for these functions. The claimed subspace is closed because \(\ell_\infty\) is complete and the embedding is isometric. No assertion is made for arbitrary infinite metric spaces or about the complement of other norm-attainment classes.

The distance formula is indeed a metric: all off-diagonal distances lie in \([1,2)\), because \(2-3\alpha_1\ge1\). Consequently every triangle with three distinct vertices satisfies the triangle inequality, as the sum of its two legs is at least \(2\) while its third side is strictly less than \(2\).

## Proof
For each positive integer \(n\), uniquely express it as
\[
n=2^{k(n)-1}(2q(n)+1),\qquad k(n)\ge1,\quad q(n)\ge0,
\]
and put \(s_n=(-1)^{q(n)}\), \(r_n=1-2\alpha_n\). The inequalities imply \(r_n\ge1/3>0\). For an arbitrary bounded sequence \(a=(a_k)_{k\ge1}\), define
\[
F_a(n)=s_n r_n a_{k(n)},\qquad T(a)(n)=F_a(n)-F_a(1).
\]
This defines a linear map into the functions vanishing at \(1\). Let \(B=\|a\|_\infty\). For every two different indices \(n,m\), the triangle inequality for the real absolute value yields
\[
|F_a(n)-F_a(m)|\le B(r_n+r_m)
=B\bigl(d_\alpha(n,m)-\alpha_{\min\{n,m\}}\bigr)
\le B d_\alpha(n,m).
\]
Hence \(\|T(a)\|_{\mathrm{Lip}}\le B\).

To show equality, fix \(k\ge1\). For \(j\ge0\), choose the indices \(n_j=2^{k-1}(4j+1)\), \(m_j=2^{k-1}(4j+3)\). Their \(k(\cdot)\) values both equal \(k\), while their signs \(s_{n_j}\) and \(s_{m_j}\) are opposite. Both indices tend to infinity with \(j\), so \(\alpha_{n_j},\alpha_{m_j}\to0\). Their slopes therefore obey
\[
\lim_{j\to\infty}
\frac{|F_a(n_j)-F_a(m_j)|}{d_\alpha(n_j,m_j)}
=|a_k|\lim_{j\to\infty}
\frac{r_{n_j}+r_{m_j}}{d_\alpha(n_j,m_j)}=|a_k|.
\]
This holds for every \(k\), so taking the supremum yields \(\|T(a)\|_{\mathrm{Lip}}\ge\sup_k|a_k|=B\). Together with the preceding bound, \(T\) is a linear isometry.

Finally, fix an arbitrary basepoint \(n\) and any distinct \(m\). Since \(\alpha\) is nonincreasing, \(\alpha_{\min\{n,m\}}\ge\alpha_n\). The same inequality gives
\[
\frac{|T(a)(n)-T(a)(m)|}{d_\alpha(n,m)}
\le B\left(1-\frac{\alpha_n}{d_\alpha(n,m)}\right)
\le B\left(1-\frac{\alpha_n}{2}\right).
\]
This bound is uniform over all \(m\ne n\). Because \(\alpha_n>0\) and \(B>0\) for nonzero \(a\), the local supremum is strictly smaller than the global norm \(B\). Hence no nonzero \(T(a)\) belongs to \(\operatorname{PNA}(M_\alpha)\), proving the theorem. \(\square\)

## Verification
A self-contained exact-arithmetic checker is provided as `VERIFY.py`. Run `python VERIFY.py`. It checks the metric inequalities, pairwise Lipschitz bounds, positive slack identities, and the strict local upper bounds for 192 finite rational instances (216,576 pairs and 9,216 local point tests); representative decay sequences are \(3^{-n}\), \((n+2)^{-1}\), and \((3n)^{-1}\). The count is a finite sanity check, not a substitute for the analytic proof over all dimensions or all positive sequences.

## Relationship to prior work
The definition of pointwise norm attainment comes from Choi, Jung, Lee and Roldán, arXiv:2312.00393v1, Definition 2.1. Their Example 4.10 explicitly identifies the special metric with \(\alpha_n=3^{-n}\) as lying outside several sufficient criteria for **positive** norm-attainment embeddings; that same paper proves an isometric \(c_0\) lies inside its strongly norm-attaining functions. The present result instead constructs an isometric \(\ell_\infty\) *in the complement* of pointwise norm attainment, on the original full metric space and on its entire monotone-decay family.

Choi, Jung, Lee and Roldán, arXiv:2404.07599v1, Theorem 2.2, prove a universal isometric \(\ell_\infty\) embedding avoiding norm attainment as a functional on the Lipschitz-free space; this does not imply avoidance of pointwise norm attainment, which is a different and strictly local criterion. Their Proposition 4.2 constructs non-pointwise-norm-attainers on real Banach-space domains; the present countable bounded, uniformly discrete metrics are not real Banach spaces. These comparisons are about logical implication of claims, not wording alone.

## Limitations
The result does not characterize all countable metric spaces for which the complement of pointwise norm attainment is spaceable. The strict local gap depends on \(n\) and is not uniform over all indices, so the proof does not claim any uniform global separation of the subspace from pointwise norm-attaining functions. While the cited primary sections and mathematical-database searches did not reveal stronger coverage, equivalent formulations in unindexed or subsequently published work remain possible. Verification of originality is distinct from verification of the explicit construction.

## References
1. G. Choi, M. Jung, H. J. Lee and Ó. Roldán, *Embeddings of infinite-dimensional spaces in the sets of norm-attaining Lipschitz functions*, arXiv:2312.00393v1 (first posted 2023-12-01), Definition 2.1, Example 4.10, Theorem 4.11. https://arxiv.org/html/2312.00393v1
2. G. Choi, M. Jung, H. J. Lee and Ó. Roldán, *Linear structures of norm-attaining Lipschitz functions and their complements*, arXiv:2404.07599v1 (first posted 2024-04-11), Theorem 2.2 and Proposition 4.2. https://arxiv.org/html/2404.07599v1
