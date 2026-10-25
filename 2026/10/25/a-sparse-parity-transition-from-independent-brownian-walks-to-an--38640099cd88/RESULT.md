# A sparse-parity transition from independent Brownian walks to an arcsine-switching pair

## Finding
Fix \(\theta>0\). A family of independently randomized, inclusion-induced sign transformations with Bernoulli intensity \(p_n=2^{-\lceil\theta n\rceil-2}\) produces three distinct annealed functional scaling limits. For \(0<\theta<1/2\), the input and output converge to **independent** standard Brownian motions. For \(\theta>1/2\), they converge to the **same** standard Brownian motion. Exactly at \(\theta=1/2\), their limit is
\[
(B_t,Y_t),\qquad
Y_t=\int_0^t\mathbf1_{\{B_s>0\}}\,dB_s
     +\int_0^t\mathbf1_{\{B_s\le0\}}\,dW_s,
\]
where \(B,W\) are independent standard Brownian motions. At every \(t>0\),
\[
\frac{[B,Y]_t}{t}=\frac1t\int_0^t\mathbf1_{\{B_s>0\}}\,ds
\sim\operatorname{Beta}(1/2,1/2).
\]
Thus the critical pair has a nonconstant, arcsine-distributed realized cross-variation, although each coordinate is itself standard Brownian motion.

## Assumptions and scope
Let \(\xi_1,\xi_2,\ldots\) be independent symmetric variables in \(\{-1,+1\}\). For each integer \(n\ge1\) and each subset \(K\subseteq\{1,\ldots,n\}\), independently of all other coefficients and the input, draw \(\beta_{n,K}\) as Bernoulli with parameter
\[
p_n=2^{-\lceil\theta n\rceil-2}.
\]
Set \(S_n=\{i\le n:\xi_i=-1\}\), \(\zeta_0=1\), and for \(n\ge1\),
\[
\zeta_n=(-1)^{\sum_{K\subseteq S_n}\beta_{n,K}},
\qquad X_n=\sum_{j=1}^n\xi_j,\quad
Y_n=\sum_{j=1}^n\zeta_{j-1}\xi_j.
\]
The empty subset is included; all coefficient levels are separately resampled. The result concerns the **annealed** law jointly averaging input and coefficients; no quenched phase diagram is asserted. For any finite \(T>0\), linearly interpolate the two coordinates between integer steps and divide by \(\sqrt N\) at times \(\lfloor Nt\rfloor\). Convergence holds in \(C([0,T],\mathbb R^2)\).

## Proof
**1. Exact conditional parity mean and filtration.** Write \(V_n=|S_n|=(n-X_n)/2\). Conditional on \(\xi_1,\ldots,\xi_n\), precisely \(2^{V_n}\) independent Bernoulli coefficients occur in the exponent defining \(\zeta_n\). Therefore
\[
m_n:=\mathbb E(\zeta_n\mid\xi_1,\ldots,\xi_n)
=(1-2p_n)^{2^{V_n}}\in[0,1].
\]
At time \(n\), reveal the input through \(\xi_n\) and coefficient levels through \(n-1\), but reveal the next coefficient level jointly with \(\xi_{n+1}\). This makes \((X_n,Y_n)\) a bounded-increment martingale. The predictable covariance matrix of its increment at time \(n+1\) is
\[
\begin{pmatrix}1&m_n\\m_n&1\end{pmatrix}.
\]
In particular, every output increment is an independent fair sign (even conditional on the entire coefficient environment), because it is a predictable sign times the fresh fair input.

**2. Sharp asymptotic switch.** The positive quantity controlling \(m_n\) is
\[
2^{V_n}p_n=2^{(1/2-\theta)n-X_n/2+O(1)}.
\]
For \(\theta<1/2\), the law of large numbers gives \(2^{V_n}p_n\to\infty\) in probability and \(m_n\to0\) in \(L^1\), by \((1-2p_n)^r\le e^{-2p_nr}\). For \(\theta>1/2\), it gives \(2^{V_n}p_n\to0\) and \(m_n\to1\) in \(L^1\), by \(1-(1-2p_n)^r\le2p_nr\).

At \(\theta=1/2\), the same expressions give \(m_n\to\mathbf1_{\{X_n>0\}}\) in \(L^1\). Indeed, outside \(\{|X_n|\le n^{1/4}\}\), the preceding exponential bounds force the corresponding approximation uniformly, while \(\mathbb P(|X_n|\le n^{1/4})=O(n^{-1/4})\) by the binomial local bound. Since both quantities are in \([0,1]\), their Cesàro averaged absolute difference vanishes in \(L^1\). In each regime, the same statement holds uniformly for cumulative averages indexed by \(\lfloor Nt\rfloor\), \(0\le t\le T\).

**3. Identification of the functional limits.** The input satisfies Donsker's invariance principle. The martingale brackets from Step 1 converge jointly with the scaled input. Away from criticality the limits are \(tI_2\) and \(t\left(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\right)\), respectively. The bounded-increment martingale functional central limit theorem therefore gives independent standard Brownian coordinates in the first case and coincident coordinates in the second.

At criticality, by Step 2 the cross bracket differs negligibly from \(N^{-1}\sum_{n<Nt}\mathbf1_{\{X_n>0\}}\). Donsker's theorem and the continuous-mapping theorem give convergence of this occupation sum to
\[
A_t=\int_0^t\mathbf1_{\{B_s>0\}}\,ds
\]
uniformly on compact time intervals, because Brownian zero sets have zero Lebesgue measure. Bounded martingale jumps imply tightness of the pairs. Every limit is a continuous local martingale whose first coordinate is \(B\), whose coordinate brackets equal \(t\), and whose cross bracket is \(A_t\). Such a law is uniquely identified by the displayed SDE: subtract \(\int\mathbf1_{\{B>0\}}\,dB\) from the second coordinate and represent the remaining continuous martingale, orthogonal to \(B\), with bracket \(\int\mathbf1_{\{B\le0\}}ds\), using an independent Brownian motion on an enlarged space. The representation also verifies existence. This establishes full convergence, not merely subsequential tightness.

**4. Arcsine occupation and non-Gaussian pairing.** Lévy's arcsine law gives \(A_t/t\sim\operatorname{Beta}(1/2,1/2)\) for each \(t>0\). The critical cross bracket is random and nondegenerate, in contrast to a two-dimensional Brownian motion with any fixed covariance parameter. Both coordinate brackets are still \(t\); the second coordinate is therefore a standard Brownian motion by Lévy's characterization.

## Verification
The standalone `verification.py` implements exact rational conditional-parity calculations for three coefficient intensities, verifies the binomial parity formula by an independent binomial expansion, and for small dimensions explicitly enumerates every coefficient configuration and input sign sequence. Running `python verification.py` yielded `PASS 122 exact-rational parity and model assertions`; the exact output is embedded as `verification_output.txt`. Further numerical diagnostics of the conditional mean at levels \(40,80,160,320\), performed using numerically stable `log1p`, showed convergence in all three regimes. The finite checks verify the exact discrete identities but **do not replace** the martingale and Brownian-limit proof.

## Relationship to prior work
Hamza and Tournier, *Are random random walks normal?* (first submitted 2026-10-01, arXiv:2610.01658v1), introduce the inclusion-induced independent coefficient scheme and establish Gaussian normality under coefficient parameters bounded away from zero and one. Their fully independent-uniform construction and one-factor bounds do not apply to the exponentially vanishing probabilities here. Their separate totally-unordered representation admits varying Bernoulli parameters but involves only one sampled coefficient per level, not the \(2^{V_n}\)-coefficient parity mechanism driving this theorem. Collevecchio, Hamza, Shi and Williams, *Limit theorems and ergodicity for general bootstrap random walks* (arXiv:2010.16000v2), supply the general martingale criterion and examples of non-Gaussian sign-based transforms; the sign-based limit itself is not claimed as a new type of stochastic integral. The new point is the **sharp exponential-sparsity threshold** and its **arcsine-switching critical law** within a natural random Boolean coefficient ensemble. Standard Donsker, martingale functional limit, and arcsine theorems are cited ingredients, not novel lemmas.

## Limitations
The theorem is annealed and is specific to independent subset coefficients with level-dependent common Bernoulli parameters of the stated exponential form. It does not establish quenched convergence, finite-sample convergence rates, or analogous critical limits under dependence across coefficient levels. The statement concerns weak functional limits only, not an independent proof of the classical Brownian arcsine law. Historical priority beyond the inspected sources remains subject to wider literature review.

## References
1. K. Hamza and L. Tournier, *Are random random walks normal?*, arXiv:2610.01658v1 (first public submission 2026-10-01), https://arxiv.org/html/2610.01658v1.
2. A. Collevecchio, K. Hamza, M. Shi and R. J. Williams, *Limit theorems and ergodicity for general bootstrap random walks*, arXiv:2010.16000v2, https://arxiv.org/html/2010.16000v2.
3. F. Aurzada, L. Döring and H. H. Pitters, *Occupation times and areas derived from random sampling*, arXiv:2406.09886 (2024); for an elementary proof of the classical arcsine occupation law.
4. Standard martingale functional central limit theorem, Donsker invariance principle, continuous-martingale representation and Lévy's characterization (classical tools).
