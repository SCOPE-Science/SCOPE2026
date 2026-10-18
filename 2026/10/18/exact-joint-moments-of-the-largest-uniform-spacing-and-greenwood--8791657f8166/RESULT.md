# Exact joint moments of the largest uniform spacing and Greenwood's statistic

## Finding
Let \(n\ge 2\), and let \((S_1,\ldots,S_n)\sim\operatorname{Dirichlet}(1,\ldots,1)\). Set
\[
M_n=\max_{1\le i\le n}S_i,\qquad G_n=\sum_{i=1}^n S_i^2.
\]
For \(0\le x\le1\), write \(u_k(x)=(1-kx)_+=\max\{1-kx,0\}\). The following **exact mixed tail-moment profile** holds:
\[
\mathbb E[G_n\mathbf1\{M_n>x\}]
=\sum_{k=1}^{n}(-1)^{k+1}\binom nk u_k(x)^{n-1}
\left[kx^2+\frac{2kx}{n}u_k(x)+\frac{2}{n+1}u_k(x)^2\right],
\tag{1}
\]
where terms with \(u_k(x)=0\) are zero. Simultaneously,
\[
\Pr(M_n>x)=\sum_{k=1}^{n}(-1)^{k+1}\binom nk u_k(x)^{n-1}.
\tag{2}
\]
Thus the complete conditional expectation \(\mathbb E[G_n\mid M_n\le x]\) is explicit for each \(1/n<x\le1\), as
\[
\frac{2/(n+1)-\mathbb E[G_n\mathbf1\{M_n>x\}]}{1-\Pr(M_n>x)}.
\tag{3}
\]
Writing \(H_n=\sum_{j=1}^n 1/j\) and \(H_n^{(2)}=\sum_{j=1}^n 1/j^2\), integration of (1) gives the exact, **strictly positive** covariance
\[
\boxed{\operatorname{Cov}(M_n,G_n)=\frac{H_n^2+H_n^{(2)}-2H_n}{n(n+1)(n+2)}>0.}
\tag{4}
\]
Its precise decay and the Pearson correlation satisfy
\[
\operatorname{Cov}(M_n,G_n)\sim\frac{(\log n)^2}{n^3},\qquad
\operatorname{Corr}(M_n,G_n)\sim\frac{\sqrt6}{2\pi}\frac{(\log n)^2}{\sqrt n}.
\tag{5}
\]
In particular the statistics are positively correlated for every fixed sample size yet asymptotically uncorrelated after standardization.

## Assumptions and scope
The spacings are **all** \(n\) gaps made by \(n-1\) independent uniform points on \([0,1]\), including the gaps from the endpoints; in many statistical references these would be the \(N+1\) spacings of \(N=n-1\) observations. Alternatively, the circular gaps between \(n\) independent uniform points, read from a randomly selected starting point, have the same exchangeable simplex law. The null distribution is continuous and the gaps sum exactly to one. No assertion is made under a nonuniform, fitted-parameter, dependent, or discretized null. At \(x=1/n\), the conditioning event \(M_n\le x\) has probability zero, so (3) requires the strict lower bound.

## Proof
**1. Subset exceedance and an affine simplex.** Fix a set \(J\subseteq\{1,\ldots,n\}\) of size \(k\ge1\). When \(kx<1\), the event \(E_J=\{S_j>x\text{ for every }j\in J\}\) has probability \((1-kx)^{n-1}\) because uniform simplex volume scales with the power \(n-1\). Conditional on this event, the shifted and normalized vector is again uniform on the simplex:
\[
S_i=x\mathbf1\{i\in J\}+(1-kx)T_i,
\qquad(T_1,\ldots,T_n)\sim\operatorname{Dirichlet}(1,\ldots,1).
\]
Here \(\mathbb ET_i=1/n\) and \(\mathbb E\sum_iT_i^2=2/(n+1)\). Consequently
\[
\mathbb E[G_n\mathbf1_{E_J}]
=(1-kx)^{n-1}\left[kx^2+\frac{2kx}{n}(1-kx)+\frac2{n+1}(1-kx)^2\right].
\]
For \(kx\ge1\) this expectation is zero; boundary equalities have probability zero. Inclusion-exclusion for the union \(\{M_n>x\}=\bigcup_i\{S_i>x\}\) establishes (1) and (2), including \(x=0\) by continuity. Subtracting from \(\mathbb EG_n\) and dividing by \(\Pr(M_n\le x)\) establishes (3).

**2. Integration gives an exact mixed moment.** Since \(M_n\in[0,1]\), Tonelli's theorem yields
\[
\mathbb E[M_nG_n]=\int_0^1\mathbb E[G_n\mathbf1\{M_n>x\}]\,dx.
\]
For each subset size \(k\), substituting \(t=kx\) and evaluating beta integrals gives
\[
\begin{aligned}
\int_0^{1/k}kx^2(1-kx)^{n-1}\,dx&=\frac{2}{k^2n(n+1)(n+2)},\\
\int_0^{1/k}\frac{2kx}{n}(1-kx)^n\,dx&=\frac{2}{kn(n+1)(n+2)},\\
\int_0^{1/k}\frac2{n+1}(1-kx)^{n+1}\,dx&=\frac{2}{k(n+1)(n+2)}.
\end{aligned}
\]
The last two terms combine to \(2/[kn(n+2)]\). The two elementary alternating-binomial identities
\[
\sum_{k=1}^n\frac{(-1)^{k+1}}k\binom nk=H_n,\qquad
\sum_{k=1}^n\frac{(-1)^{k+1}}{k^2}\binom nk=\frac{H_n^2+H_n^{(2)}}2
\]
therefore yield
\[
\mathbb E[M_nG_n]=\frac{H_n^2+H_n^{(2)}}{n(n+1)(n+2)}+\frac{2H_n}{n(n+2)}.
\tag{6}
\]
Both identities follow, respectively, by integrating \((1-(1-t)^n)/t\) and multiplying the resulting harmonic identity by \(1/t\) under a second integral, or by the recurrence in \(n\). Integrating (2) gives \(\mathbb EM_n=H_n/n\), while the Dirichlet second-moment identity gives \(\mathbb EG_n=2/(n+1)\). Subtraction in (6) proves (4).

**3. Positivity and correlation.** Put \(A_n=H_n^2+H_n^{(2)}-2H_n\). Direct substitution gives \(A_1=0\) and
\[
A_{n+1}-A_n=\frac{2(H_{n+1}-1)}{n+1}>0\quad(n\ge1),
\]
so (4) is strictly positive for \(n\ge2\). A second tail integration of (2) gives
\[
\mathbb E[M_n^2]=\frac{H_n^2+H_n^{(2)}}{n(n+1)},\qquad
\operatorname{Var}(M_n)=\frac{nH_n^{(2)}-H_n^2}{n^2(n+1)}.
\]
The Dirichlet fourth moments \(\mathbb E S_i^4=24/[n(n+1)(n+2)(n+3)]\) and \(\mathbb E S_i^2S_j^2=4/[n(n+1)(n+2)(n+3)]\) for distinct indices give
\[
\operatorname{Var}(G_n)=\frac{4(n-1)}{(n+1)^2(n+2)(n+3)}.
\]
Consequently, for all \(n\ge2\),
\[
\operatorname{Corr}(M_n,G_n)=
\frac{A_n\sqrt{(n+1)(n+3)}}{2\sqrt{(n+2)(n-1)(nH_n^{(2)}-H_n^2)}}.
\tag{7}
\]
Finally \(H_n=\log n+\gamma+o(1)\) and \(H_n^{(2)}\to\pi^2/6\). Substituting into (4) and (7) proves (5).

## Verification
The included `verify.py` uses exact rational arithmetic to check the binomial-harmonic sums, integrated mixed moments, signs, variance bounds, and tail-profile boundary and range conditions for all \(2\le n\le39\). Two independent hand-integration benchmarks are recorded: for \(n=2\), direct integration against a uniform point gives \(\mathbb E[M_nG_n]=25/48\) and covariance \(1/48\); for \(n=3\), partitioning the two-dimensional simplex by its largest coordinate gives \(\mathbb E[M_nG_n]=349/1080\) and covariance \(19/1080\). Additional seeded Monte Carlo comparisons used independent normalized exponential variables for \(n=2,3,5,9,25\) and agreed within simulation fluctuations. Neither finite checks nor Monte Carlo establishes the infinite family; the affine-simplex proof above does.

## Relationship to prior work
Eller and Shtembari (arXiv:2111.02252, first posted November 3, 2021) explicitly list the Greenwood sum-of-squared-spacings test and compare it with other spacing tests. Shtembari and Caldwell (arXiv:2008.02048, first posted August 5, 2020) give exact distributions for the largest spacing and sums of ordered spacings; that includes the **marginal** maximum-spacing law, not this quadratic mixed tail moment. Shtembari and Caldwell (arXiv:2303.09520, first posted March 16, 2023) discuss maximum-gap and summed-gap methods for unknown-background limit setting, but their reviewed analysis does not provide a joint Greenwood–maximum-spacing moment. These sources motivate how the two statistics may be used jointly and supply the separate known ingredients; no new marginal maximum distribution or Greenwood definition is claimed.

## Limitations
The theorem concerns only the uniform-simplex null and the first mixed moment profile \(\mathbb E[G_n\mathbf1\{M_n>x\}]\), not the full bivariate distribution or the power of a combined test under alternatives. The Pearson correlation tending to zero does not establish independence, nor does it prove a joint central limit theorem. The exact formulas may be obtained by specializing older general Dirichlet moment or ordered-spacing identities not identified in the inspected literature; historical priority has not been independently verified. The alternating sums are exact but may exhibit numerical cancellation for large \(n\) unless evaluated with stable methods.

## References
- P. Eller and L. Shtembari, *A goodness-of-fit test based on a recursive product of spacings*, arXiv:2111.02252 (v1 November 3, 2021), https://arxiv.org/abs/2111.02252.
- L. Shtembari and A. Caldwell, *On the sum of ordered spacings*, arXiv:2008.02048 (v1 August 5, 2020), https://arxiv.org/abs/2008.02048.
- L. Shtembari and A. Caldwell, *Limit setting using spacings in the presence of unknown backgrounds*, arXiv:2303.09520 (v1 March 16, 2023), https://arxiv.org/abs/2303.09520.
