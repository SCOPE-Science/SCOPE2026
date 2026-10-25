# A unique concentration-driven singleton–doubleton covariance reversal in symmetric Dirichlet–multinomial sampling

## Finding
Let \(n\geq4\) be an integer and \(K\geq K_0(n):=2+\binom{n-1}{2}\) an integer. Draw a random categorical probability vector from the symmetric \(K\)-component Dirichlet law with common positive shape \(a\), and draw \(n\) independent observations conditional on this vector. If \(M_1\) and \(M_2\) are the numbers of categories observed exactly once and twice, respectively, there is a **unique** \(a_c(n,K)>0\) such that
\[
\operatorname{Cov}_a(M_1,M_2)\begin{cases}>0,&0<a<a_c(n,K),\\=0,&a=a_c(n,K),\\<0,&a>a_c(n,K).\end{cases}
\]
Thus the finite-alphabet sampling model has a single dependence reversal as reinforcement is weakened. The cutoff \(K_0(n)\) is exact for a **strictly positive limiting sign ratio** as \(a\downarrow0\), because \(R(\infty)>1\) holds exactly when \(K\ge K_0(n)\). At the boundary \(K=K_0(n)-1\), this ratio tends to one, so its limiting value alone does not decide the eventual covariance sign. No global claim is made for smaller alphabets.

An explicit implicit equation uniquely specifying \(a_c\) is \(R(a_c)=1\), where
\[
R(a)=\frac{(K-1)(n-2)}{Kn}\,
\frac{(Ka)_n((K-2)a)_{n-3}}{((K-1)a)_{n-1}((K-1)a)_{n-2}},
\]
and \((z)_j=z(z+1)\cdots(z+j-1)\) denotes the rising factorial, with \((z)_0=1\). Here \(R(a)\) is strictly decreasing for \(a>0\) under the stated alphabet condition.

## Assumptions and scope
Only positive real \(a\), integers \(n\ge4\), and integer alphabets \(K\ge2+\binom{n-1}{2}\) are covered by the global uniqueness theorem. There are exactly \(K\) possible categories. Conditional sample draws are independent but unconditionally exchangeable, and the common Dirichlet shape \(a\) is **per category**, so the total concentration is \(Ka\). There is no Poisson–Dirichlet infinite-alleles limit in the claim. The covariance is not normalized to a correlation.

## Proof
**1. Exact factorial moments and sign reduction.** Fix one category. The marginal and bivariate counts have beta-binomial and Dirichlet-multinomial laws. Therefore the probabilities \(p_1=\Pr(X_1=1)\), \(p_2=\Pr(X_1=2)\), and \(p_{12}=\Pr(X_1=1,X_2=2)\), for distinct labeled categories 1 and 2, are
\[
\begin{aligned}
p_1&=n\frac{(a)_1((K-1)a)_{n-1}}{(Ka)_n},\\
p_2&=\binom n2\frac{(a)_2((K-1)a)_{n-2}}{(Ka)_n},\\
p_{12}&=\frac{n!}{2(n-3)!}\frac{(a)_1(a)_2((K-2)a)_{n-3}}{(Ka)_n}.
\end{aligned}
\]
The same category cannot have counts one and two simultaneously, hence
\[
\operatorname{Cov}(M_1,M_2)=K(K-1)p_{12}-K^2p_1p_2
=K^2p_1p_2\bigl(R(a)-1\bigr).
\]
The prefactor is positive for the claimed domain. Cancelling factors yields the displayed formula for \(R\).

**2. Strong- and weak-reinforcement endpoints.** Put \(t=1/a\) and \(k=K\). At \(t=0\), interpreted as \(a\to\infty\),
\[
R(0)=\frac{n-2}{n}\left(\frac{k}{k-1}\right)^2
\left(1-\frac1{(k-1)^2}\right)^{n-3}.
\]
Writing \(z=(k-1)^{-2}\), Bernoulli's inequality gives \((1-z)^{n-3}\le[1+(n-3)z]^{-1}\). Consequently,
\[
R(0)\le\frac{(n-2)k^2}{n((k-1)^2+n-3)}<1.
\]
The last strict inequality follows from
\[
n((k-1)^2+n-3)-(n-2)k^2
=2(k-n/2)^2+\frac{n(n-4)}2>0,
\]
using \(n\ge4\) and \(k\ge K_0(n)\ge5\). Conversely, at \(t\to\infty\) (\(a\downarrow0\)), rising-factorial first-order asymptotics give
\[
R(\infty)=\frac{(k-2)(n-1)(n-2)}{(k-1)n(n-3)}.
\]
It exceeds one precisely when \(k>1+\binom{n-1}{2}\). At equality, it is one; below equality, it is smaller than one. This proves sharpness of the strict endpoint ratio criterion; in the equality case the next term, not just this limit, would be required to decide the finite-shape sign.

**3. Strict monotonicity of the ratio.** Cancel positive factors in the expression for \(R(1/t)\). With \(n\ge4\), it is a positive constant times
\[
\left[\prod_{j=1}^{n-4}\left(1-\frac1{(k-1+jt)^2}\right)\right]
B(t),\qquad
B(t)=\frac{(k+(n-3)t)(k+(n-2)t)(k+(n-1)t)}{(k-1+(n-3)t)^2(k-1+(n-2)t)}.
\]
The product is interpreted as one when \(n=4\); every factor present is strictly increasing for \(t\ge0\). It remains to establish \(B'(t)>0\).

The logarithmic derivative \(B'/B\) has a strictly positive denominator
\[
D(t)=(k+(n-3)t)(k+(n-2)t)(k+(n-1)t)
(k-1+(n-3)t)(k-1+(n-2)t)
\]
and numerator \(c_0+c_1t+c_2t^2+c_3t^3\), where
\[
\begin{aligned}
c_0&=k^2(k-1)(2k-3n+6),\\
c_1&=k\{(6n-14)k^2+(-9n^2+33n-26)k+6n^2-24n+22\},\\
c_2&=(n-2)\{(6n-16)k^2+(-9n^2+36n-29)k+3n^2-12n+9\},\\
c_3&=(n-3)(n-2)\{2k(n-2)-3n^2+10n-7\}.
\end{aligned}
\]
Each coefficient is positive at and above \(k=K_0(n)\). Here is an explicit all-integer verification rather than a finite test: set \(v=n-4\ge0\) and \(k_0=(v^2+5v+10)/2\). At \(k=k_0\) the braces in \(c_0\) and \(c_3\) are respectively \(v^2+2v+4\) and \(v^3+4v^2+6v+5\), and both increase in \(k\). Denote by \(Q_1(k),Q_2(k)\) the two bracketed quadratics multiplying \(k\) and \(n-2\) in \(c_1,c_2\), respectively. Direct expansion yields
\[
\begin{aligned}
2Q_1(k_0)&=3v^5+26v^4+101v^3+214v^2+268v+164,\\
Q_1'(k_0)&=6v^3+31v^2+71v+62,\\
2Q_2(k_0)&=3v^5+25v^4+94v^3+187v^2+219v+128,\\
Q_2'(k_0)&=(2v+3)(3v^2+10v+17).
\end{aligned}
\]
All displayed polynomials are strictly positive for \(v\ge0\), and \(Q_1'',Q_2''>0\) since \(n\ge4\). Therefore every \(c_i>0\), proving \(B'>0\). Hence \(R(1/t)\) is strictly increasing in \(t\ge0\), or equivalently \(R(a)\) strictly decreases in \(a>0\). Combined with the strict endpoint inequalities, the intermediate value theorem gives one and only one crossing, with the claimed signs.

## Verification
The standalone `verify.py` reproduces factorial-moment probabilities and covariance by **independently enumerating all integer count vectors** under exact rational Dirichlet-multinomial masses in several small cases; it checks the exact ratio formula and both sides of the crossing. It also checks the logarithmic-derivative polynomial coefficients by exact rational evaluation for a set of small dimensions and positive \(t\). Those finite checks support transcription accuracy but are **not** substitutes for the preceding symbolic proof, which holds for all claimed integers and real shapes.

## Relationship to prior work
Dirichlet-multinomial count modeling and its concentration parameter are well established; Mao and Ma's 2020 open preprint explicitly states the conditional multinomial / Dirichlet construction in its section 2.1, equation (2.1). Grantham et al. (2017) study dependence and sparsity in microbiome count data, motivating the interaction of rare and double-observation categories. Zhu (2021) studies the law of observed distinct types under exchangeability; it does not itself derive this two-frequency-class dependence phase diagram. The present contribution is **not** the multinomial/Dirichlet compound mass function or the covariance reduction, but the all-shape single-crossing theorem and its sharp large-alphabet sufficient cutoff. Other results about richness-versus-frequency covariances and infinite-type Poisson–Dirichlet partition counts concern different covariance pairs or probability laws, so their statements do not directly imply the finite-symmetric-Dirichlet reversal.

## Limitations
The theorem does not assert the complete phase diagram for \(K<K_0(n)\). No sample-wide inference guarantee, estimator, or direct empirical microbiome inference is established. The implicit critical shape does not have a claimed elementary closed form. Priority is subject to unindexed or not-materially-inspected work on two-frequency Dirichlet–multinomial occupancies; a literature search cannot certify absolute novelty. Independent validation has not been performed.

## References
- N. S. Grantham, B. J. Reich, E. T. Borer and K. Gross (2017), *MIMIX: a Bayesian Mixed-Effects Model for Microbiome Data from Designed Experiments*, arXiv:1703.07747, first posted 22 March 2017, https://arxiv.org/abs/1703.07747 .
- J. Mao and L. Ma (2020), *Dirichlet-tree multinomial mixtures for clustering microbiome compositions*, arXiv:2008.00400, first posted 2 August 2020, https://arxiv.org/abs/2008.00400 .
- T. Zhu (2021), *The distribution of the number of distinct values in a finite exchangeable sequence*, arXiv:2103.07518, first posted 12 March 2021, https://arxiv.org/abs/2103.07518 .
