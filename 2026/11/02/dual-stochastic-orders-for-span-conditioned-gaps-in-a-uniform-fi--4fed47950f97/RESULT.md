# Dual stochastic orders for span-conditioned gaps in a uniform finite sample

## Finding

Let \(N\ge 2\), \(2\le k\le N\), and choose a \(k\)-element subset uniformly from \(\{1,\ldots,N\}\). Write its ordered elements as \(X_1<\cdots<X_k\), its range as \(R=X_k-X_1\), and the \(m=k-1\) positive internal gaps as \(G_i=X_{i+1}-X_i\). The conditional law of \(G=(G_1,\ldots,G_m)\), given \(R=r\), is uniform among the positive integer vectors summing to \(r\), for every \(m\le r\le N-1\).

**Two simultaneous conditional orders.** There exists one coupling \(G^{(r)}\) of all these conditional gap laws such that, almost surely, for each admissible successive span,
\[
G^{(r+1)}\ge G^{(r)}\quad\text{coordinatewise},\qquad
\mathbb E\left[\left.\frac{G^{(r+1)}}{r+1}\,\right|G^{(r)}\right]=\frac{G^{(r)}}r.
\]
Consequently, if \(C_t=\#\{i:G_i\le t\}\), \(t=1,2,\ldots\), then every coordinatewise nondecreasing function of the short-gap count vector has a conditional mean that is nonincreasing in \(r\). Conversely, for every convex function \(\Phi\) on the probability simplex, \(\mathbb E[\Phi(G/R)\mid R=r]\) is nondecreasing in \(r\). Thus, for every nondecreasing real-valued \(f\), every coordinatewise nondecreasing \(\Psi\) on finitely many short-gap counts, and every convex \(\Phi\),
\[
\operatorname{Cov}\bigl(f(R),\Psi(C_{t_1},\ldots,C_{t_s})\bigr)\le0,\qquad
\operatorname{Cov}\bigl(f(R),\Phi(G/R)\bigr)\ge0.
\]
All variables are bounded because the sample space is finite. If \(N>k\), \(1\le t\le N-k\), and \(f\) is strictly increasing, then \(\operatorname{Cov}(f(R),C_t)<0\). If \(N>k\ge3\), \(f\) is strictly increasing, and \(\Phi\) is strictly convex, then \(\operatorname{Cov}(f(R),\Phi(G/R))>0\).

**Exact natural statistics.** Let \(A=\#\{i:G_i=1\}\), the number of adjacent selected pairs, and let \(Q=\sum_{i=1}^m(G_i/R)^2\), the quadratic concentration of normalized internal gaps. Then
\[
\boxed{\operatorname{Cov}(R,A)=-\frac{2(k-1)(N-k)}{N(k+1)}}.
\]
For every permissible \(r\),
\[
\boxed{\mathbb E[Q\mid R=r]=\frac{2r-(k-2)}{kr}},\qquad
\operatorname{Cov}(R,Q)=\frac{k-2}{k}\left(\mathbb E[R]\,\mathbb E[R^{-1}]-1\right).
\]
The last quantity is strictly positive when \(N>k\ge3\), and is zero in degenerate cases. The pair of signs distinguishes absolute clustering from *relative* gap inequality as the sample span increases.

## Assumptions and scope

The sampled positions are distinct, uniformly sampled without replacement from the consecutive integer grid \(\{1,\ldots,N\}\). The sample size \(k\) is fixed, and the gap coordinates retain their order. All statements hold at finite \(N\); the parameter \(r\) runs over every integer from \(k-1\) to \(N-1\), inclusive. Conditional probabilities are supported at every such \(r\). The normalized vector lies in the \((k-2)\)-dimensional simplex. The convention \(k=2\) makes \(Q\equiv1\). When \(k=N\), the range is deterministic.

## Proof

**1. Conditional uniformity.** Fix \(r\) and a positive gap composition \(g_1+\cdots+g_m=r\). Every choice of the left endpoint \(x\in\{1,\ldots,N-r\}\) gives exactly one sample with these internal gaps. Consequently, there are precisely \(N-r\) samples for this gap vector. Because there are \(\binom{r-1}{m-1}\) compositions and \(\binom Nk\) total samples,
\[
\Pr(R=r)=\frac{(N-r)\binom{r-1}{m-1}}{\binom Nk},\qquad
\Pr(G=g\mid R=r)=\binom{r-1}{m-1}^{-1}.
\]

**2. A single coupled Pólya growth process.** Start with the deterministic vector \(G^{(m)}=(1,\ldots,1)\). If \(\sum_iG_i^{(r)}=r\), choose coordinate \(i\) with probability \(G_i^{(r)}/r\), and add one unit to that coordinate. A uniform positive-composition law at span \(r\) is transformed into the uniform law at \(r+1\): for any target composition \(h\), its total inbound probability is
\[
\frac{\sum_i(h_i-1)}{r\binom{r-1}{m-1}}
=\frac{r+1-m}{r\binom{r-1}{m-1}}
=\binom r{m-1}^{-1}.
\]
The initial law is uniform, so induction gives every required conditional law. Each coordinate only increases. Moreover, for every coordinate,
\[
\mathbb E\left[\left.\frac{G_i^{(r+1)}}{r+1}\,\right|G^{(r)}\right]
=\frac{G_i^{(r)}+G_i^{(r)}/r}{r+1}
=\frac{G_i^{(r)}}r.
\]
Thus the normalized vector is a martingale. Jensen's inequality proves convex-order growth; a short-gap count cannot increase under this coupling. If \(m\ge2\), every growth step has at least two distinct possible next vectors of positive probability, so strict Jensen applies to strictly convex \(\Phi\).

**3. Regression and strict covariance signs.** Since \(R\) is scalar and \(\mathbb E[\Psi(C)\mid R]\) is nonincreasing, the independent-copy identity
\[
2\operatorname{Cov}(f(R),Y)
=\mathbb E\bigl[(f(R)-f(R'))(\mathbb E[Y\mid R]-\mathbb E[Y\mid R'])\bigr]
\]
(with \(R'\) an independent copy of \(R\)) gives the negative sign. Replace \(Y\) by \(\Phi(G/R)\) for the positive sign. For \(1\le t\le N-k\), the expectation of \(C_t\) is \(m\) at \(r=m\), but is smaller at \(r=N-1\): a positive composition can then have a coordinate \(N-k+1>t\). Hence its regression is not constant and the strict negative covariance follows. Strict positive covariance follows from strict Jensen and the nontrivial range support when \(N>k\ge3\).

**4. Exact adjacent-pair covariance.** Add the boundary spacings \(Y_0=X_1\) and \(Y_k=N+1-X_k\) to \(Y_i=G_i\) for \(1\le i<k\). The resulting positive composition of \(N+1\) into \(k+1\) parts is uniform. For any internal gap \(Y_i\), symmetry gives
\[
\Pr(Y_i=1)=\frac{k}{N},\quad
\mathbb E[R]=\frac{(k-1)(N+1)}{k+1},\quad
\mathbb E[R\mid Y_i=1]=N+1-\frac{2N}{k}.
\]
The last identity follows because, conditioned on \(Y_i=1\), the other \(k\) positive parts uniformly sum to \(N\). Summing \(\mathbf1_{Y_i=1}\) over \(i=1,\ldots,k-1\) yields \(\mathbb E[A]=k(k-1)/N\), and substituting into \(\operatorname{Cov}(R,A)=\mathbb E[RA]-\mathbb E[R]\mathbb E[A]\) gives the displayed formula.

**5. Quadratic concentration.** Under the coupling, \(r-m\) additions follow the standard symmetric unit-initialized Pólya urn. Let \(S_r=\sum_i(G_i^{(r)})^2\). The increment rule yields \(\mathbb E[S_{r+1}\mid G^{(r)}]=(1+2/r)S_r+1\), with \(S_m=m\). Solving this first-order recurrence gives
\[
\mathbb E\left[\left.\sum_iG_i^2\,\right|R=r\right]
=\frac{r(2r-m+1)}{m+1}.
\]
Divide by \(r^2\), put \(m=k-1\), and apply the total covariance identity. Strict positivity for nonconstant \(R\) follows from strict Cauchy–Schwarz: \(\mathbb E[R]\mathbb E[R^{-1}]>1\).

## Verification

A standalone standard-library Python checker, `verify.py`, exhaustively enumerates every subset with \(2\le N\le11\) and \(2\le k\le N\). It independently compares the exact span law, uniform conditional composition law, threshold means, the adjacent-pair covariance, the normalized quadratic conditional mean, the positive covariance identity and its strict boundary cases. It also enumerates every one-step Pólya transition through those sizes and checks the normalized-quadratic and short-gap mean orderings. The observed result was `exact_checks_passed: 6527`. These finite checks are not the proof of any unbounded assertion; the preceding arguments cover all \(N,k\).

## Relationship to prior work

Kochar and Korwar (2001), Section 4, already establish the joint law, exchangeability, multivariate increasing-failure-rate property, and pairwise reverse regularity for spacings of a simple random sample without replacement. These are essential prior laws, not newly claimed. Their inspected Theorems 4.1–4.4 do not assert the conditional-on-span Pólya coupling or the paired unnormalized-coordinate and normalized-convex stochastic orders. The present result uses the classical composition law and standard urn martingale algebra to obtain that additional exact conditional dependence statement. The urn framework itself is classical and was extensively studied by Flajolet, Gabarró and Pekari (2005; preprint public July 7, 2004). Çalık (2005) treats moments of the sample range for a discrete uniform population, not its signed dependence with internal-gap statistics.

## Limitations

The uniform consecutive-grid and fixed-size assumptions are essential to the simple composition representation; no claim is made for unequal inclusion weights, duplicated observations, irregularly spaced population values, or continuous samples. The multivariate convex-order assertion is for **normalized internal gaps** and should not be confused with coordinatewise stochastic ordering of the normalized vector. The finite-population covariance formulas are exact, but no general asymptotic central limit theorem is asserted. Existing general urn representations or unpublished specializations may have an equivalent conclusion; independent historical-priority assessment is outstanding.

## References

- S. C. Kochar and R. Korwar, *On Random Sampling Without Replacement from a Finite Population*, Annals of the Institute of Statistical Mathematics **53** (2001), 631–646, especially Section 4. DOI: https://doi.org/10.1023/A:1014693702392. Lawful full text: https://www.ism.ac.jp/editsec/aism/pdf/053_3_0631.pdf.
- P. Flajolet, J. Gabarró and H. Pekari, *Analytic urns*, Annals of Probability **33** (2005), 1200–1233. First public arXiv version July 7, 2004: https://arxiv.org/abs/math/0407098.
- S. Çalık, *On the Variances of Distribution of the Sample Range of Order Statistics from a Discrete Uniform Distribution*, Journal of Mathematics and Statistics **1** (2005), 180–183. Published September 30, 2005. DOI: https://doi.org/10.3844/jmssp.2005.180.183.
