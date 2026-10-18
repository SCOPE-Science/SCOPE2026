# Gaussian sharp constants for lazy positive weighted shifts

## Finding

Let \(0<\alpha<1\) and \(0<\delta<1\). On complex \(\ell^1(\mathbb N)\), define the positive backward weighted shift and its lazy average by
\[
 W_\alpha e_1=0,\qquad W_\alpha e_j=\left(\frac j{j-1}\right)^\alpha e_{j-1}\quad(j\ge2),\qquad T_{\alpha,\delta}=(1-\delta)I+\delta W_\alpha.
\]
Write \(\varphi(u)=(2\pi)^{-1/2}\exp(-u^2/2)\) and define the continuous Gaussian fractional integrals
\[
 A_\alpha(s)=\int_{-\infty}^{s}(s-u)^{-\alpha}\varphi(u)\,du,
 \qquad B_\alpha(s)=\int_{-\infty}^{s}(s-u)^{-\alpha}|u|\varphi(u)\,du.
\]
Both functions tend to zero as \(s\to\pm\infty\), so their respective maxima \(M_\alpha=\max_{s\in\mathbb R}A_\alpha(s)\) and \(N_\alpha=\max_{s\in\mathbb R}B_\alpha(s)\) are attained and strictly positive. The following are **sharp two-sided operator-norm asymptotics**:
\[
 \boxed{\lim_{n\to\infty}n^{-\alpha/2}\|T_{\alpha,\delta}^{n}\|=
 \left(\frac{\delta}{1-\delta}\right)^{\alpha/2}M_\alpha,}
\]
\[
 \boxed{\lim_{n\to\infty}n^{(1-\alpha)/2}\|T_{\alpha,\delta}^{n+1}-T_{\alpha,\delta}^{n}\|=
 \left(\frac{\delta}{1-\delta}\right)^{(\alpha+1)/2}N_\alpha.}
\]
Furthermore, \(T_{\alpha,\delta}\) is a positive absolutely Cesàro bounded operator with
\[
\sigma(T_{\alpha,\delta})=(1-\delta)+\delta\overline{\mathbb D},
\qquad \sigma(T_{\alpha,\delta})\cap\mathbb T=\{1\}.
\]
Thus \(\|T_{\alpha,\delta}^n\|\to\infty\), yet \(\|T_{\alpha,\delta}^{n+1}-T_{\alpha,\delta}^{n}\|\to0\). The exponents and both leading constants are exact for every fixed pair of parameters.

## Assumptions and scope

The scalar field is complex. Coordinates begin at \(j=1\); \(e_j\) are the standard unit vectors. Absolute Cesàro boundedness means that some finite \(K\) satisfies \(N^{-1}\sum_{m=0}^{N-1}\|T^m x\|_1\le K\|x\|_1\) for every integer \(N\ge1\) and every vector \(x\). All limits hold at fixed \(0<\alpha<1\), \(0<\delta<1\), with \(n\to\infty\); no uniformity at the endpoints in these parameters is asserted.

## Proof

**1. Exact column identities.** For \(0\le k<j\), telescoping gives \(W_\alpha^k e_j=(j/(j-k))^\alpha e_{j-k}\), and it vanishes for \(k\ge j\). Set \(p_{n,k}=\binom nk\delta^k(1-\delta)^{n-k}\) for \(0\le k\le n\), and zero otherwise; set \(p_{n,-1}=0\). The binomial formula and the \(\ell^1\) column-sum norm yield, without approximation,
\[
 \|T^n\|=\sup_{j\ge1}\sum_{k=0}^{\min(n,j-1)}p_{n,k}\left(\frac j{j-k}\right)^\alpha.\tag{1}
\]
The coefficient of the row \(j-k\) in \(\delta T^n(W_\alpha-I)e_j\) equals \(\delta(p_{n,k-1}-p_{n,k})(j/(j-k))^\alpha\) for \(0\le k<j\); here the convention \(p_{n,n+1}=0\) includes the last term. Hence
\[
 \|T^{n+1}-T^n\|=\delta\sup_{j\ge1}\sum_{k=0}^{\min(n+1,j-1)}|p_{n,k}-p_{n,k-1}|\left(\frac j{j-k}\right)^\alpha.\tag{2}
\]
These are exact infinite-dimensional norm formulas; cancellation is handled before taking the absolute column sums.

**2. Binomial local-limit lemma, including its singular kernel.** Put \(\mu_n=n\delta\), \(\sigma_n=\sqrt{n\delta(1-\delta)}\), and \(u_{n,k}=(k-\mu_n)/\sigma_n\). For fixed \(\delta\), Stirling's formula in the central zone and the exact binomial ratio
\[
\frac{p_{n,k-1}}{p_{n,k}}=\frac{k(1-\delta)}{(n-k+1)\delta}
\]
show, uniformly for \(u_{n,k}\) in compact sets,
\[
 \sigma_n p_{n,k}\longrightarrow\varphi(u_{n,k}),\qquad
 \sigma_n^2|p_{n,k}-p_{n,k-1}|\longrightarrow |u_{n,k}|\varphi(u_{n,k}).\tag{3}
\]
The notation means that the difference between the two sides tends uniformly to zero in each bounded \(u\)-window. For a fixed \(\delta\) there are \(C,c>0\), independent of large \(n\) and indices \(k\in\{0,\dots,n+1\}\), such that
\[
 \sigma_np_{n,k}\le C e^{-c u_{n,k}^2},\qquad
 \sigma_n^2|p_{n,k}-p_{n,k-1}|\le C(1+|u_{n,k}|)^2e^{-c u_{n,k}^2}.\tag{4}
\]
Indeed, the central ratio above is \(O((1+|u_{n,k}|)/\sigma_n)\) when \(|k-n\delta|\le\varepsilon n\); outside that zone, Chernoff bounds for the binomial point probabilities are exponentially small in \(n\), absorbing all polynomial factors and yielding (4) after decreasing \(c\). The boundary terms at \(k=0,n+1\) obey the same exponential bound.

For either choice \(g(u)=\varphi(u)\) or \(g(u)=|u|\varphi(u)\), (3)–(4) imply the following singular Riemann-sum statement: if integers \(j_n\) satisfy \((j_n-\mu_n)/\sigma_n\to s\in\mathbb R\), then
\[
\frac1{\sigma_n}\sum_{k<j_n}(s_n-u_{n,k})^{-\alpha}a_{n,k}\longrightarrow
 \int_{-\infty}^s(s-u)^{-\alpha}g(u)\,du,\qquad s_n=\frac{j_n-\mu_n}{\sigma_n},\tag{5}
\]
where \(a_{n,k}=\sigma_np_{n,k}\) in the first case and \(a_{n,k}=\sigma_n^2|p_{n,k}-p_{n,k-1}|\) in the second. For a full proof of the singular cutoff, split the sum at \(j_n-k\le\varepsilon\sigma_n\), the compact region \(\varepsilon\sigma_n<j_n-k\) with bounded \(|u_{n,k}|\), and Gaussian tails. The first part is at most \(C\sigma_n^{\alpha-1}\sum_{h\le\varepsilon\sigma_n}h^{-\alpha}\le C_\alpha\varepsilon^{1-\alpha}\), uniformly in \(n,j_n\); the compact part is an ordinary uniform-mesh Riemann sum, and (4) controls the tails. Send \(n\to\infty\), then \(\varepsilon\downarrow0\). The integrability threshold \(\alpha<1\) is used precisely here.

For maximizing over **all** columns, we also need localization rather than only pointwise convergence. The Gaussian envelope (4) and the same cutoff show that, for \(j\in[\mu_n/2,2\mu_n]\) and \(s_n=(j-\mu_n)/\sigma_n\), each normalized sum in (5) tends uniformly to zero along sequences with \(|s_n|\to\infty\). To verify this, for \(s_n\to+\infty\) split at \(|u_{n,k}|\le s_n/2\), on which the denominator is at least \(s_n/2\), and its complement, controlled by \(e^{-c s_n^2/4}\) times a uniformly bounded singular lattice sum. For \(s_n\to-\infty\), every contributing \(u_{n,k}<s_n\) lies in that Gaussian tail, and the same fractional-sum estimate applies. Thus there is no mass escaping to large normalized \(|s_n|\).

**3. Sharp constants and global supremum.** For \(j_n=\mu_n+s\sigma_n+o(\sigma_n)\), rewrite (1) using (5):
\[
 n^{-\alpha/2}\sum_{k<j_n}p_{n,k}\left(\frac{j_n}{j_n-k}\right)^\alpha
 \longrightarrow\left(\frac\delta{1-\delta}\right)^{\alpha/2}A_\alpha(s).\tag{6}
\]
Similarly, (2) and (5) give
\[
 n^{(1-\alpha)/2}\delta\sum_{k<j_n}|p_{n,k}-p_{n,k-1}|\left(\frac{j_n}{j_n-k}\right)^\alpha
 \longrightarrow\left(\frac\delta{1-\delta}\right)^{(\alpha+1)/2}B_\alpha(s).\tag{7}
\]
The prefactors follow from \(j_n/n\to\delta\) and \(\sigma_n/\sqrt n\to\sqrt{\delta(1-\delta)}\).

It remains to justify replacing a chosen \(j_n\) by the supremum. If \(j\le\mu_n/2\), every contributing \(k<j\) lies a fixed fraction below the binomial mean, while \((j/(j-k))^\alpha\le(n+2)^\alpha\). Both column sums, with the scalings in (6)–(7), vanish exponentially. If \(j\ge2\mu_n\), the terms \(k\le3\mu_n/2\) have \(j/(j-k)\le4\), giving bounded first columns and second columns at most \(O(\sigma_n^{-1})\), because \(\sum_k|p_{n,k}-p_{n,k-1}|=2\max_k p_{n,k}=O(\sigma_n^{-1})\); the remaining binomial tails are exponentially small even with the bound \((j/(j-k))^\alpha\le(n+2)^\alpha\). Hence neither outer region contributes after the normalizations. For \(j\in[\mu_n/2,2\mu_n]\), the previous localization argument eliminates \(|s_n|\to\infty\). Subsequence compactness of \(s_n\) and (6)–(7) give the upper bounds \(M_\alpha,N_\alpha\); choosing \(j_n\) nearest \(\mu_n+s_*\sigma_n\) at any maximizer \(s_*\) gives the matching lower bounds. Dominated convergence proves continuity of \(A_\alpha,B_\alpha\); the Gaussian tails and fractional kernel imply their decay at both ends, completing their maximum claims.

**4. Positivity, Cesàro boundedness, spectrum and dynamical consequences.** Positivity of \(T\) is immediate. For every \(j,N\ge1\), the column sum of \(\sum_{m=0}^{N-1}T^m\) is
\[
 \sum_{m=0}^{N-1}\sum_{k<j}p_{m,k}\left(\frac j{j-k}\right)^\alpha
 \le\frac1\delta\sum_{k=0}^{\min(j-1,N-1)}\left(\frac j{j-k}\right)^\alpha
 \le\frac N{\delta(1-\alpha)}.\tag{8}
\]
The first inequality uses the exact negative-binomial renewal identity \(\sum_{m=k}^\infty p_{m,k}=1/\delta\); the second uses the integral bound \(\sum_{h=1}^j h^{-\alpha}\le j^{1-\alpha}/(1-\alpha)\) when \(j\le N\), while for \(j\ge N\) the summands decrease as functions of \(j\) and their maximal sum occurs at \(j=N\). Positivity and \(|T^m x|\le T^m|x|\) therefore give \(N^{-1}\sum_{m<N}\|T^m x\|_1\le[\delta(1-\alpha)]^{-1}\|x\|_1\), proving absolute Cesàro boundedness.

We have \(\|W_\alpha^k\|=(k+1)^\alpha\), so its spectral radius is \(1\). For each \(|z|<1\), the vector with coordinates \(z^{j-1}/j^\alpha\) belongs to \(\ell^1\) and is an eigenvector of \(W_\alpha\) with eigenvalue \(z\). Thus \(\sigma(W_\alpha)=\overline{\mathbb D}\), and the affine spectral mapping theorem gives the asserted disk. Its only contact with \(\mathbb T\) is at \(1\). Since the constants \(M_\alpha,N_\alpha\) are finite and positive, the power growth and difference decay follow immediately from the sharp limits.

## Verification

The identities (1)–(2) are exact finite-column expressions. Their asymptotic leading constants follow from the binomial local central limit theorem, the explicitly justified fractional-kernel cutoff, and a separate global-column localization argument. The optional standalone code `check.py` reproduces selected finite truncations and numerical Gaussian integrals; it is a diagnostic, not an infinite-dimensional or novelty certificate. Reproduction requires Python 3 with NumPy and SciPy.

## Relationship to prior work

Abbar–Arnold–Coine (2026, arXiv:2609.24601, first posted September 21) establish a general classification of absolute Cesàro boundedness for weighted backward shifts and sharp power-growth phenomena, but do not analyze the binomially smoothed weighted shift's two exact asymptotic norm constants. Arnold (2026, arXiv:2610.00271, first posted September 24), Example 3.2, presents the polynomial positive shift in a general self-improvement setting, and Section 7 establishes an abstract lazy-averaging preservation lemma before constructing **nonpositive** counterexamples to a Katznelson–Tzafriri extension. The present result neither claims the original weighted shift nor the lazy-preservation observation as new; it adds a simultaneous exact Gaussian asymptotic for both \(\|T^n\|\) and \(\|T^{n+1}-T^n\|\). The positive-operator question posed there for \(L^p\), \(1<p<\infty\), remains open as far as this argument is concerned: the theorem here is specifically on \(\ell^1\). Cohen–Cuny–Eisner–Lin (2020) give general growth bounds without the present sharp constants.

## Limitations

The theorem concerns this explicitly weighted lazy-shift family and does not establish operator-norm decay for all positive absolutely Cesàro bounded operators. The behavior at \(\alpha=0,1\) or \(\delta=0,1\) is not covered, and the two maxima are defined by convergent one-dimensional integrals rather than claimed elementary closed forms. Independently unindexed prior work could in principle contain equivalent asymptotic formulas; no exhaustive priority assertion is made. Numerical convergence is especially slow when \(\alpha\) approaches \(1\), because of the integrable singularity in the Gaussian convolution.

## References

1. A. Abbar, L. Arnold, C. Coine, *On Absolutely Cesàro bounded operators*, arXiv:2609.24601v1 (first public September 21, 2026), https://arxiv.org/html/2609.24601v1 , especially Section 3.
2. L. Arnold, *Self-improvement for absolutely Cesàro bounded operators*, arXiv:2610.00271v1 (first public September 24, 2026), https://arxiv.org/html/2610.00271v1 , especially Example 3.2, Section 7 and Question 8.2.
3. G. Cohen, C. Cuny, T. Eisner, M. Lin, *Resolvent conditions and growth of powers of operators*, Journal of Mathematical Analysis and Applications 487 (2020), article 124035, https://doi.org/10.1016/j.jmaa.2020.124035 .
