# Exact positive dependence of multinomial roughness and Pearson chi-square

## Finding
For every integer \(N\ge 2\), every integer \(n\ge 2\), and every positive probability vector \(p=(p_1,\ldots,p_n)\), let \(X\sim\operatorname{Mult}(N,p)\), and put
\[
U_p(X)=\frac{1}{N(N-1)}\sum_{i=1}^n\frac{X_i(X_i-1)}{p_i}-1.
\]
Then \(\mathbb E U_p=0\), and for **every finite-valued convex** \(f:\mathbb R^n\to\mathbb R\),
\[
\operatorname{Cov}(f(X),U_p(X))\ge 0.
\]
If \(f\) is strictly convex, the covariance is strictly positive.

In the uniform case \(p_i=1/n\), Pearson's statistic is
\[
Q_{N,n}(X)=\sum_{i=1}^n\frac{(X_i-N/n)^2}{N/n}
              =(N-1)U_p(X)+(n-1).
\]
For any finite undirected graph on the labeled bins, with nonnegative edge weights \(w_{ij}\) and total weight \(W=\sum_{\{i,j\}}w_{ij}>0\), define its histogram roughness
\[
T_G(X)=\sum_{\{i,j\}}w_{ij}|X_i-X_j|.
\]
Let \(S_m\) be the sum of \(m\) independent increments with respective probabilities \(1/n,1-2/n,1/n\) at \(-1,0,+1\); in particular \(S_0=0\). The following **exact finite-sample** identity holds:
\[
\boxed{\operatorname{Cov}(T_G,Q_{N,n})
 =\frac{4(N-1)W}{n}\left(\frac{\Pr(S_{N-2}=0)}n+
 \left(1-\frac1n\right)\Pr(S_{N-2}=1)\right)>0.}
\]
The dependence on the graph is only through the sum of its edge weights. For the cyclic statistic \(T_\circ=\sum_{i=1}^n|X_i-X_{i+1}|\), \(X_{n+1}=X_1\), the edge \(\{1,2\}\) is counted twice when \(n=2\); this convention gives \(W=n\) for every \(n\ge2\). For each fixed \(n\ge 2\),
\[
\lim_{N\to\infty}\operatorname{Cov}\left(\frac{T_\circ}{\sqrt{Nn}},Q_{N,n}\right)=\frac2{\sqrt\pi}.
\]
For the linear adjacent-bin statistic \(T_{\mathrm{lin}}=\sum_{i=1}^{n-1}|X_i-X_{i+1}|\), the analogous limit is \(2(n-1)/(n\sqrt\pi)\).

## Assumptions and scope
The count total \(N\) and number of bins \(n\) are finite integers, at least two. The nonuniform result uses the **unbiased pair-collision statistic** \(U_p\), not ordinary nonuniform Pearson chi-square. In the uniform case these two variables are affine functions of one another as displayed. The graph may be disconnected; only nonnegative weights with \(W>0\) are required. The cyclic statistic includes the repeated edge at \(n=2\). The asymptotic limits hold with fixed \(n\) and \(N\to\infty\), not uniformly over growing \(n\).

## Proof
**1. An exact two-draw collision identity.** Realize the histogram as \(X=\sum_{a=1}^N e_{Y_a}\), with iid categorical \(Y_a\) of law \(p\), and write \(Z=\sum_{a=1}^{N-2}e_{Y_a}\). The factorial-moment identity, for every cell \(i\), is
\[
\mathbb E\big[(X_i)_2 f(X)\big]
 =N(N-1)p_i^2\mathbb E\big[f(Z+2e_i)\big],
\qquad (k)_2=k(k-1).
\]
Consequently \(\mathbb E U_p=0\). If \(I,J\) are two independent categorical indices of law \(p\), independent of \(Z\), then
\[
\begin{aligned}
\operatorname{Cov}(f(X),U_p(X))
 &=\mathbb E[f(Z+2e_I)]-\mathbb E[f(Z+e_I+e_J)]\\
 &=\mathbb E\left[\frac{f(Z+2e_I)+f(Z+2e_J)}2
                    -f(Z+e_I+e_J)\right].
\end{aligned}
\]
The summand is nonnegative by midpoint convexity because \(Z+e_I+e_J\) is the midpoint of \(Z+2e_I\) and \(Z+2e_J\). Under strict convexity, it is positive on \(I\ne J\), an event of positive probability for \(n\ge2\). This proves the first assertion, including both quantifiers and equality limitations.

**2. One-edge exact covariance.** Put \(q=1/n\) and take an edge \(\{i,j\}\). The difference \(Z_i-Z_j\) has the law of \(S_{N-2}\). For a given integer \(s\), let \(\delta(s)\) be the expected value of \(|s+2\mathbf1_{I=i}-2\mathbf1_{I=j}|-|s+\mathbf1_{I=i}+\mathbf1_{J=i}-\mathbf1_{I=j}-\mathbf1_{J=j}|\). Elementary evaluation using the probabilities \(q,1-2q,q\) gives
\[
\delta(0)=4q^2,\qquad
\delta(1)=\delta(-1)=2q(1-q),\qquad
\delta(s)=0\quad (|s|\ge2).
\]
Since \(S_{N-2}\) is symmetric,
\[
\operatorname{Cov}(|X_i-X_j|,U_p(X))
 =4q^2\Pr(S_{N-2}=0)+4q(1-q)\Pr(S_{N-2}=1).
\]
For uniform \(p\), expanding the definitions gives \(Q_{N,n}=(N-1)U_p+n-1\). Multiply the last identity by \(N-1\), sum over the graph edges, and factor the total weight \(W\). The resulting formula is strictly positive: for \(n\ge3\), zero is reachable by an all-zero path, while for \(n=2\) at least one of zero or one is reachable according to parity, and both coefficients are positive.

**3. Fixed-bin asymptotics.** For \(n\ge3\), the increments of \(S_m\) are aperiodic of lattice span one, centered, and have variance \(2/n\). The lattice local central limit theorem yields, for each fixed \(k\in\{0,1\}\),
\[
\Pr(S_m=k)\sim\sqrt{\frac{n}{4\pi m}}.
\]
For \(n=2\) the walk is periodic: at each parity, exactly one of \(0,1\) can occur, its accessible-site probability is asymptotic to \(\sqrt{2/(\pi m)}\) (a central-binomial estimate); the weighted bracket in the finite formula is still asymptotic to \(1/\sqrt{2\pi m}=\sqrt{n/(4\pi m)}\). Thus for every fixed \(n\ge2\),
\[
\operatorname{Cov}(T_G,Q_{N,n})\sim
\frac{2W}{\sqrt{\pi n}}\sqrt{N}.
\]
Taking \(W=n\) for the cycle or \(W=n-1\) for the path and dividing by \(\sqrt{Nn}\) gives the stated limiting covariances. The proof, not finite enumeration, establishes all infinitely many sizes.

## Verification
The standalone script `verify_covariance.py` uses only Python's standard library and exact rational arithmetic. It exhaustively enumerates all multinomial histograms for the one-edge identity over \(2\le n\le6\), \(2\le N\le7\), checks the general collision-covariance identity at 54 parameter/function cases including a nonuniform law, and checks three graph-weight families at five sizes each. Assertions compare independently computed expectation/covariance sums against the identities. To reproduce, run `python verify_covariance.py`. All checks pass. These finite tests support but cannot replace the proof or the local central limit theorem.

## Relationship to prior work
Banić and Elezović's October 9, 2026 study of multinomial discrete total variation gives its **one-statistic expectation** under the uniform null, including a cyclic mean asymptotic. Its introduction explicitly contrasts the order-sensitive total-variation statistic with order-insensitive Pearson chi-square and describes later planned work on total-variation variance and marginal distributions. The present result concerns a different quantity: the **joint cross-covariance** between total variation and Pearson chi-square, for every finite sample size and every weighted graph of bin comparisons; it also identifies a general convex-functional pair-collision mechanism.

Banić and Elezović's earlier Comb Test compares marginal testing power and computes the discrete-total-variation null distribution. Bax and Ouimet treat normal approximation and confidence intervals using Pearson chi-square. Those questions differ from an exact graph-independent mixed moment. A universally valid mean formula or marginal distribution for either statistic alone does not determine their covariance, because it does not specify their joint law. The convex-collision representation here supplies that joint information.

## Limitations
No joint distribution or testing-power improvement is established, and positive covariance does not imply positive quadrant dependence. The affine Pearson relation is confined to a uniform null; the nonuniform claim is about the specified unbiased collision statistic \(U_p\). The asymptotic statement holds with fixed \(n\). Prior-work comparison is based on searchable records and the complete accessible text of the motivating paper; the full texts of some related sources were inaccessible, leaving a residual possibility of a stronger earlier result under an alternative formulation. No independent mathematical audit has been performed.

## References
1. N. Banić and N. Elezović, *Discrete total variation under the multinomial, Part 1: expectation under the uniform null*, arXiv:2610.13366v1 (posted 2026-10-09), https://arxiv.org/html/2610.13366v1.
2. N. Banić and N. Elezović, *Comb Test: Histogram Uniformity Testing Based on Discrete Total Variation*, arXiv:2606.01465 (2026), https://arxiv.org/abs/2606.01465.
3. E. Bax and F. Ouimet, *Non-asymptotic approximations for Pearson's chi-square statistic and its application to confidence intervals for strictly convex functions of the probability weights of discrete distributions*, arXiv:2309.01882 (2023), https://arxiv.org/abs/2309.01882.
4. N. Banić and N. Elezović, *TVOR: Finding Discrete Total Variation Outliers among Histograms*, arXiv:2012.11574 (2020), https://arxiv.org/abs/2012.11574.

