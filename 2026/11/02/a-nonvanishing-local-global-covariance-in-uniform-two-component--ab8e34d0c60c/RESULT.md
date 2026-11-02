# A nonvanishing local–global covariance in uniform two-component Cayley forests

## Finding
For each integer \(n\ge2\), let \(F\) be uniform among the unrooted spanning forests with exactly two connected components of the complete graph \(K_n\). Fix a vertex \(b\). Write \(Q=|C_b|\) for the size of its component, \(S=n-Q\) for the other component's size, and \(D=\deg_F(b)\).

The complete joint law is obtained from
\[
\Pr(Q=q)=\frac{\binom{n-1}{q-1}\tau(q)\tau(n-q)}{A_n},\qquad
A_n=\frac{(n-1)(n+6)n^{n-4}}2,\qquad 1\le q\le n-1,
\]
where \(\tau(1)=1\) and \(\tau(k)=k^{k-2}\) for \(k\ge2\), and from the conditional distributions
\[
D\mid(Q=q)\ \stackrel{d}{=}\ \begin{cases}0,&q=1,\\
1+\operatorname{Bin}(q-2,1/q),&q\ge2.
\end{cases}
\]
These conditional degree distributions increase strictly in likelihood-ratio order as \(q\) increases; equivalently, the degree becomes strictly smaller in this order when the complementary component size increases. In particular, for every \(n\ge2\),
\[
\boxed{\operatorname{Cov}(D,S)=-\frac{2(n-2)}{n+6}.}
\]
The covariance is negative for all \(n\ge3\) and converges to \(-2\). Yet
\[
\boxed{\operatorname{Corr}(D,S)=-\sqrt{\frac2n}\,(1+o(1))}\qquad(n\to\infty).
\]
The correlation is undefined at \(n=2\), where both variables are deterministic.

## Assumptions and scope
Forests are **unrooted** and individually equally probable; no root is independently selected in either component. Labels are \(\{1,\ldots,n\}\), and \(b\) is any fixed label. A singleton component is a tree and its unique vertex has degree zero. The likelihood-ratio statement compares \(D\mid Q=q\) and \(D\mid Q=q+1\) for \(1\le q\le n-2\), with the usual extended likelihood-ratio convention for support boundaries.

## Proof
**1. Forest normalization and size law.** Let \(R(z)\) and \(T(z)\) be the exponential generating functions of rooted and unrooted labeled trees. Cayley's formula and the tree decomposition give \(R=ze^R\) and \(T=R-R^2/2\). The exponential generating function of forests with exactly two unrooted components is \(T^2/2\). Lagrange inversion gives, for \(n\ge4\),
\[
 n![z^n]R^j=\frac{j(n-1)!n^{n-j}}{(n-j)!},\quad
 A_n=n![z^n]\left(\frac{R^2}{2}-\frac{R^3}{2}+\frac{R^4}{8}\right)
 =\frac{(n-1)(n+6)n^{n-4}}2.
\]
Direct inspection gives the same formula for \(n=2,3\). To obtain \(Q=q\), choose the other \(q-1\) vertices in \(C_b\), then choose independent labeled trees on that set and its complement. This proves the displayed size law. Conditioned on its vertex set, \(C_b\) is a uniform Cayley tree. The Prüfer code contains the marked label with distribution \(\operatorname{Bin}(q-2,1/q)\); degree equals one plus this count, establishing the complete joint law.

**2. Strict likelihood-ratio ordering.** Put \(p_q(j)=\Pr(D-1=j\mid Q=q)\) for \(q\ge2\). For \(0\le j\le q-3\), binomial probability ratios satisfy
\[
 \frac{p_{q+1}(j+1)/p_q(j+1)}{p_{q+1}(j)/p_q(j)}
 =\frac{(q-1-j)(q-1)}{q(q-2-j)}
 =1+\frac{j+1}{q(q-2-j)}>1.
\]
The larger-\(q\) distribution also has strictly positive mass at its additional upper support point. Thus likelihood ratios increase strictly on the common support; the transition from \(q=1\) is strictly ordered because the degree jumps from zero to one. This implies strict stochastic monotonicity and hence negative association between \(D\) and every increasing nonconstant function of \(S\) on its support.

**3. Exact covariance.** Let \(\kappa=n^{n-2}\) denote the number of spanning trees of \(K_n\). Removing one edge of a tree yields a two-component forest; conversely, a two-component forest with component sizes \(Q,S\) admits exactly \(QS\) joining edges. A still simpler count: for each vertex \(v\ne b\), the number of forests in which \(v\) lies in the component away from \(b\) equals the number of spanning trees containing the edge \(bv\). Edge transitivity and Cayley's formula show this count to be \(2n^{n-3}\). Hence
\[
 \mathbb E S=\frac{(n-1)2n^{n-3}}{A_n}=\frac{4n}{n+6}.
\]
For every deterministic two-component forest, \(\sum_{v=1}^n|C_v|^{-1}=2\); vertex exchangeability therefore gives \(\mathbb E(1/Q)=2/n\). Moreover, the Prüfer law implies \(\mathbb E(D\mid Q)=2-2/Q\), valid even for \(q=1\). Thus
\[
 \operatorname{Cov}(D,S)=\operatorname{Cov}(2-2/Q,n-Q)
 =-2\left(\mathbb E Q\,\mathbb E\frac1Q-1\right)
 =-\frac{2(n-2)}{n+6}.
\]

**4. Variance and decorrelation.** The established two-component-forest inclusion identity (Kassel–Kenyon–Wu, Theorem 3) states that distinct vertices \(u,v\ne b\) both belong to the floating component with probability \(\kappa G_{uv}/A_n\), where \(G\) is the Dirichlet Green matrix. For \(K_n\), \(G=(I+J)/n\) on the \(n-1\) unmarked vertices. Thus \(\Pr(u,v\in\Sigma)=n^{n-3}/A_n\) and
\[
 \mathbb E S(S-1)=\frac{2n(n-2)}{n+6},\qquad
 \operatorname{Var}(S)=\frac{2n^2(n-2)}{(n+6)^2}\sim2n.
\]
The conditional binomial moments give
\[
 \mathbb E D=2-\frac4n,\qquad
 \mathbb E[D(D-1)]=3-\frac{18}n+6\mathbb E(Q^{-2}).
\]
Since \(0\le \mathbb E(Q^{-2})\le\mathbb E(Q^{-1})=2/n\), it follows that \(\operatorname{Var}(D)\to1\). Combining these variances with the exact covariance proves the correlation limit.

## Verification
The bundled `verify.py` independently enumerates every choice of \(n-2\) edges of \(K_n\), rejects cyclic choices, measures \((Q,D)\), and compares exact rational frequencies with the displayed joint distribution for \(2\le n\le8\). It additionally checks both component-size moments, the covariance, and the strict probability-ratio inequalities. The enumerated forest totals are \(1,3,15,110,1080,13377,200704\), respectively; all 240 assertions pass. The infinite-size statements are proved analytically and are not inferred from these finite checks.

## Relationship to prior work
Kassel, Kenyon, and Wu (first public arXiv version, 22 March 2012) study **unrooted** random two-component spanning forests of general finite graphs and establish floating-component one- and two-vertex inclusion formulas. Their Theorem 3 supplies the existing size-second-moment input used above; their result does not directly state the joint marked-degree/component-size law, its strict likelihood-ratio ordering, or the nonvanishing degree–size covariance. Cayley's and Prüfer's classical tree formulas supply the conditional degree law. Myrvold's work counts multi-component forests, but its inspected abstract does not give the marked-degree dependence claim. D'Achille, Enriquez, and Melotti (2026) give local-shape distributions for **massive rooted-forest weights** proportional to the product of component sizes, not the unweighted two-component model. See the limitations regarding possible indirect implications.

## Limitations
The proof concerns complete graphs and exactly two **unrooted** forest components; the conclusion is not asserted for arbitrary host graphs, arbitrary component counts, or the rooted massive-spanning-forest ensemble. The explicit variance of the complementary size is an application of the prior two-point inclusion theorem, not a claim of novelty. Neither likelihood-ratio ordering nor covariance implies independence. Historical priority remains uncertain because broader exact tree-shape enumerations might yield the stated joint law after additional conditioning and reweighting. Independent audit has not been performed.

## References
1. A. Kassel, R. Kenyon, W. Wu, *Random two-component spanning forests*, arXiv:1203.4858, first posted 2012-03-22; later *Ann. Inst. H. Poincaré Probab. Statist.* 51 (2015), 1457–1464. https://arxiv.org/abs/1203.4858
2. W. Myrvold, *Counting k-component forests of a graph*, *Networks* 22 (1992), 647–652. https://doi.org/10.1002/net.3230220704
3. M. D'Achille, N. Enriquez, P. Melotti, *Massive Spanning Forests on the Complete Graph: Exact Distribution and Local Limit*, *Random Structures & Algorithms* (2026). https://doi.org/10.1002/rsa.70048
4. A. Cayley, *A theorem on trees*, *Quart. J. Math.* 23 (1889), 376–378; classical Prüfer correspondence for labeled trees.
