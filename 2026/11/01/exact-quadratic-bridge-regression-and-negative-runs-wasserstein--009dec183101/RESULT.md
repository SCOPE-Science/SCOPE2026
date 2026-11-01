# Exact quadratic bridge regression and negative runs–Wasserstein dependence

## Finding

Let \(m\ge2\), put \(N=2m\), and choose uniformly a binary word \((X_1,\ldots,X_N)\) containing exactly \(m\) ones and \(m\) zeros. Define its run count and signed bridge by
\[
R=1+\sum_{i=1}^{N-1}\mathbf 1\{X_i\ne X_{i+1}\},
\qquad
S_k=\sum_{i=1}^{k}(2X_i-1),\quad 1\le k<N.
\]
For every index \(k\) and every attainable value \(s\) of \(S_k\), the **exact conditional regression** is
\[
\boxed{\mathbb E[R\mid S_k=s]
=\frac{N+3}{2}-\frac{(N-1)s^2}{2k(N-k)}.}\tag{1}
\]
Thus for any nonnegative deterministic weights \(w_k\) and finite, nondecreasing functions \(g_k:[0,\infty)\to\mathbb R\),
\[
\boxed{\operatorname{Cov}\!\left(R,\sum_{k=1}^{N-1}w_k g_k(|S_k|)\right)\le0.}\tag{2}
\]
Equality in (2) holds exactly when every positively weighted internal \(g_k\), \(2\le k\le N-2\), is constant on the attainable support of \(|S_k|\). In particular, positive weight at one internal index with nonconstant \(g_k\) makes the inequality strict. The exact local quadratic covariance is
\[
\boxed{\operatorname{Cov}(R,S_k^2)
=-\frac{N(k-1)(N-k-1)}{(N-3)(N-1)}.}\tag{3}
\]
This is strictly negative at every internal index and zero at the two boundary indices.

For the classical two-sample null, take independent samples of size \(m\ge2\) from the **same atomless distribution on \(\mathbb R\)** with finite first moment. Order their pooled observations as \(Z_{(1)}<\cdots<Z_{(N)}\) and label their sources by \(X_i\). Let \(\widehat F\) and \(\widehat G\) be the two empirical probability measures' CDFs. Then
\[
W_1(\widehat F,\widehat G)
=\frac1m\sum_{k=1}^{N-1}(Z_{(k+1)}-Z_{(k)})|S_k|,
\]
and, in fact,
\[
\boxed{\operatorname{Cov}\bigl(R,W_1(\widehat F,\widehat G)
\mid Z_{(1)},\ldots,Z_{(N)}\bigr)<0\quad\text{a.s.},}\tag{4}
\]
so the unconditional covariance is also **strictly negative**.

## Assumptions and scope

The finite-word model is a uniform permutation of fixed binary counts \((m,m)\), with no independence assumption on the label positions. A run is one maximal contiguous block of equal labels; \(S_k\) is a simple bridge with \(S_N=0\). Attainable \(s\) has the appropriate parity and satisfies \(|s|\le\min(k,N-k)\). Every function \(g_k\) is finite on this finite set of attainable absolute imbalances; outside it the function's values do not matter. Nondecreasing includes constants.

In the two-sample formulation, the underlying common real law must be atomless (to avoid ties) and have finite first absolute moment (for integrable \(W_1\)). Sampling and label assignments are independent under this null. Strict negativity requires \(m\ge2\); at \(m=1\) the run count is constant and the covariance vanishes.

## Proof

First derive the conditional mean for an arbitrary word containing \(a\ge1\) ones and \(b\ge1\) zeros, with \(N=a+b\). Fix \(1\le k<N\), and condition on the first \(k\) positions containing \(c\) ones. Conditional on this count, the length-\(k\) prefix and length-\((N-k)\) suffix are independent uniform fixed-count words. Their expected numbers of *internal transitions* are respectively
\[
\frac{2c(k-c)}k
\quad\text{and}\quad
\frac{2(a-c)(b-k+c)}{N-k}.
\]
The probability that the prefix's last label differs from the suffix's first label is
\[
\frac{c(b-k+c)+(k-c)(a-c)}{k(N-k)}.
\]
Adding the initial run gives the exact general formula
\[
\begin{aligned}
\mathbb E[R\mid\sum_{i\le k}X_i=c]
={}&1+\frac{2c(k-c)}k
+\frac{2(a-c)(b-k+c)}{N-k}\\
&+\frac{c(b-k+c)+(k-c)(a-c)}{k(N-k)}.
\end{aligned}\tag{5}
\]
This also applies when a conditional subword has length one, since then its internal contribution is zero. Substitute \(a=b=N/2\) and \(s=2c-k\); algebraically simplifying (5) proves (1). Directly counting one transition gives \(\mathbb E R=1+2m^2/N=(N+2)/2\).

For a fixed \(k\), write \(Y=|S_k|\). By (1) and the tower property,
\[
\operatorname{Cov}(R,g(Y))
=-\frac{N-1}{2k(N-k)}\operatorname{Cov}(Y^2,g(Y)).\tag{6}
\]
If \(Y'\) is an independent copy of \(Y\), then
\[
2\operatorname{Cov}(Y^2,g(Y))
=\mathbb E[(Y^2-{Y'}^2)(g(Y)-g(Y'))]\ge0.
\]
Each product is nonnegative by monotonicity. It has strictly positive expectation precisely when \(g\) is not constant on the support of \(Y\). For \(2\le k\le N-2\), this support has at least two distinct values; for \(k=1,N-1\), \(|S_k|=1\) identically. Summing (6) with nonnegative \(w_k\) proves (2) and its equality characterization.

For (3), the balanced fixed-count signs \(\varepsilon_i=2X_i-1\) satisfy
\[
\mathbb E[\varepsilon_i\varepsilon_j]=-\frac1{N-1}\quad(i\ne j),
\qquad
\mathbb E[\varepsilon_i\varepsilon_j\varepsilon_l\varepsilon_h]
=\frac3{(N-1)(N-3)}
\]
for four distinct indices, by sampling without replacement from \(m\) plus signs and \(m\) minus signs. Expanding \(S_k^2\) and \(S_k^4\), grouping terms by index multiplicity, gives
\[
\mathbb E S_k^2=\frac{k(N-k)}{N-1},
\qquad
\mathbb E S_k^4
=\frac{k(N-k)\{3k(N-k)-2N\}}{(N-1)(N-3)}.
\]
Consequently,
\[
\operatorname{Var}(S_k^2)
=\frac{2Nk(N-k)(k-1)(N-k-1)}{(N-3)(N-1)^2}.
\]
Using \(g(Y)=Y^2=S_k^2\) in (6) yields (3). These identities hold for all \(N=2m\ge4\) and \(1\le k<N\), including boundary zero-variance cases.

For (4), conditional on pooled ordered observations, every choice of \(m\) source labels among the \(N\) positions is equally likely. In one dimension the first Wasserstein distance between probability measures with finite first moments equals the area between their CDFs. Across the gap \((Z_{(k)},Z_{(k+1)})\), the CDF difference is exactly \(S_k/m\), proving the displayed weighted-bridge representation. All pooled gaps are positive almost surely; at least one internal index exists for \(N\ge4\). Apply the strict part of (2) with \(g_k(y)=y\) and \(w_k=(Z_{(k+1)}-Z_{(k)})/m\). Finally \(\mathbb E[R\mid Z_{(1)},\ldots,Z_{(N)}]=(N+2)/2\) is constant, so the law of total covariance reduces the unconditional covariance to the expectation of the strictly negative conditional covariance. Integrability follows from the finite first moment.

## Verification

The included standard-library-only Python program `verify_runs_bridge.py` enumerates every uniform fixed-composition word for each \(1\le a,b\le7\), directly checks (5) at every feasible prefix count, and tests the balanced identity (1). It separately tests the sign theorem for \(g(y)=y,y^2,y^4\), evaluates the exact quadratic covariance (3), and computes strict negative covariance with a deterministic increasing pooled sample's empirical Wasserstein statistic. Exact `Fraction` arithmetic avoids numerical tolerances. A successful local execution returned **1,587 exact assertions**, **144,392 conditional-enumeration word instances**, and **49 fixed-composition profiles**. This finite verification supports but does not replace the algebraic proof for arbitrary \(m\).

## Relationship to prior work

Wald and Wolfowitz established the classical fixed-composition two-sample run statistic. Smeeton and Cox (2003), inspected in full, discuss random shuffling and the total run-count distribution rather than the joint prefix-imbalance regression. Friedman and Rafsky (1978) discuss Wald–Wolfowitz and Smirnov statistics and their multivariate generalizations; the inspected sections do not yield (1)–(4). Ramdas, García Trillos and Cuturi (2015) develop Wasserstein two-sample tests and compare them to classical CDF-based statistics; the inspected full text does not give a joint runs–Wasserstein sign law. A separately published local-transition analysis gives the adjacent/disjoint covariances of individual run transitions, which are not the conditional law (1) nor the universal monotone weighted-bridge inequality (2).

An earlier result about covariance between run count and a particular quadratic empirical-CDF discrepancy supplies one *special weighted-quadratic instance*; (1)–(4) are substantially broader, covering every nondecreasing function of each bridge magnitude, all positive gap weights and all atomless null parent distributions for \(W_1\). Algebraic implications, rather than title similarity, determine this distinction.

## Limitations

The covariance and regression statements are for balanced binary labels. No analogous universal sign is claimed for unequal sample sizes, for a maximum rather than an additive discrepancy, or for nonlinear functions coupling several different \(|S_k|\) coordinates. The result is a covariance sign, **not** a stochastic-order theorem for the full conditional runs distribution, independence claim, or simultaneous-test error-rate guarantee. It requires continuous common null laws and a finite first moment to interpret ordinary one-Wasserstein covariance. Classical runs monographs and all historical variants were not exhaustively accessible; independent historical-priority confirmation remains outstanding.

## References

1. A. Wald and J. Wolfowitz, “On a Test Whether Two Samples are from the Same Population,” *Annals of Mathematical Statistics* **11** (1940), 147–162, DOI: 10.1214/aoms/1177731909.
2. N. Smeeton and N. J. Cox, “Do-it-yourself shuffling and the number of runs under randomness,” *Stata Journal* **3** (2003), 270–277, DOI: 10.1177/1536867X0300300304.
3. J. Friedman and L. Rafsky, “Multivariate Generalizations of Wald-Wolfowitz and Smirnov Two-Sample Tests,” SLAC-PUB-2116 (1978), https://www.slac.stanford.edu/pubs/slacpubs/2000/slac-pub-2116.pdf.
4. A. Ramdas, N. García Trillos, and M. Cuturi, “On Wasserstein Two Sample Testing and Related Families of Nonparametric Tests,” arXiv:1509.02237v1, first public version 2015-09-08, https://arxiv.org/abs/1509.02237.
5. “Exact dependence phases of fixed-composition run transitions,” published-finding corpus record `2026/10/4/SCOPE-exact-dependence-phases-of-fixed-composition-run-transitions--c6b28ad6d93d` (see its original published RESULT.md).
