# A beta-profile law for growing-power harmonic Toeplitz semigroup defects

## Finding

Let \(\alpha>-1\), put \(a=\alpha+1>0\), and let \(T_f\) denote the Toeplitz compression of multiplication by \(f\) to the complex weighted harmonic Bergman space on the unit disk, as defined below. For every integer \(N\ge2\), define the **power-multiplicativity defect**
\[
D_N=T_{z^N}-(T_z)^N.
\]
Write
\[
h_j=\frac{\Gamma(j+1)\Gamma(a+1)}{\Gamma(j+a+1)},\qquad j\ge0.
\]
Then \(D_N\) is square-zero, has rank exactly \(N-1\), and has precisely the following positive singular values, counted with multiplicity:
\[
 d_{j,N}=\frac{h_N}{\sqrt{h_jh_{N-j}}}-\sqrt{h_jh_{N-j}}>0,
 \qquad 1\le j\le N-1.
\]
These numbers increase strictly as \(j\) moves from \(1\) to the center, are symmetric under \(j\mapsto N-j\), and attain their maximum at the central index or indices. In particular,
\[
 \|D_N\|=\frac{h_N}{\sqrt{h_{\lfloor N/2\rfloor}h_{\lceil N/2\rceil}}}
 -\sqrt{h_{\lfloor N/2\rfloor}h_{\lceil N/2\rceil}},
 \qquad \lim_{N\to\infty}\|D_N\|=2^{-a}.
\]

The complete **bulk singular-value law** is as follows. For every continuous real-valued function \(F\) on \([0,1]\),
\[
\lim_{N\to\infty}\frac1{N-1}\sum_{j=1}^{N-1}F(d_{j,N})
 =\int_0^1 F\bigl([t(1-t)]^{a/2}\bigr)\,dt.
\]
The probability measure on the right has density
\[
\rho_a(y)=\frac{4y^{2/a-1}}{a\sqrt{1-4y^{2/a}}},
\qquad 0<y<2^{-a},
\]
and vanishes outside the displayed interval. Consequently, for **every fixed real \(p>0\)**,
\[
 \boxed{\ \lim_{N\to\infty}N^{-1/p}\|D_N\|_{\mathcal S_p}
 =\mathrm B\left(1+\frac{ap}{2},1+\frac{ap}{2}\right)^{1/p}.\ }
\]
Here \(\mathcal S_p\) denotes the Schatten class or, for \(0<p<1\), its standard quasi-norm. Thus individually finite-rank, square-zero semigroup defects have an asymptotically nonzero operator norm and a nondegenerate limiting distribution of their \(N-1\) nonzero singular values.

As a quantile version, let \(s_1(D_N)\ge\dots\ge s_{N-1}(D_N)>0\) denote these values in decreasing order. If \(k_N/N\to u\in(0,1)\), then
\[
 s_{k_N}(D_N)\longrightarrow 2^{-a}(1-u^2)^{a/2}.
\]

## Assumptions and scope

Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) carry the probability measure
\[
 d\mu_\alpha(z)=\frac{\alpha+1}{\pi}(1-|z|^2)^\alpha\,dx\,dy.
\]
The Hilbert space \(h^2_\alpha(\mathbb D)\) is the closed subspace of \(L^2(\mu_\alpha)\) consisting of complex-valued harmonic functions. Its orthogonal projection is \(P_h\). For bounded measurable \(f\), set \(T_f=P_hM_f|_{h^2_\alpha}\). The symbols \(z^N\) are bounded, so no unbounded-operator or domain issue arises.

An orthonormal basis indexed by integers is
\[
 e_k(z)=\begin{cases}
 z^k/\sqrt{h_k}, & k\ge0,\\
 \overline z^{-k}/\sqrt{h_{-k}}, & k<0.
 \end{cases}
\]
For \(0<p<\infty\), \(\|D_N\|_{\mathcal S_p}=(\sum_{j\ge1}s_j(D_N)^p)^{1/p}\). The rank and singular values are algebraic/finite-dimensional for each fixed \(N\); all limits are for \(N\to\infty\) with \(\alpha\) and \(p\) fixed. No uniformity as \(\alpha\downarrow-1\) or \(p\) varies is claimed.

## Proof

**1. Exact monomial action.** Let \(X=|z|^2\) under \(\mu_\alpha\). Its density is \(a(1-X)^{a-1}\) on \((0,1)\), and its moments are \(\mathbb E X^j=h_j\). Angular orthogonality shows that multiplication by \(z\), followed by projection, is a one-step bilateral weighted shift on the basis above. For \(j\ge1\), the coefficient from \(e_{-j}\) to \(e_{-j+1}\) is \(\sqrt{h_j/h_{j-1}}\), with \(h_0=1\); for \(k\ge0\), the coefficient from \(e_k\) to \(e_{k+1}\) is \(\sqrt{h_{k+1}/h_k}\). Consequently, the \(N\)-th power crosses the constant monomial once, and for \(1\le j<N\),
\[
 (T_z)^N e_{-j}=\sqrt{h_jh_{N-j}}\,e_{N-j}.
\]
Directly compressing multiplication by \(z^N\) instead gives
\[
 T_{z^N}e_{-j}=\frac{h_N}{\sqrt{h_jh_{N-j}}}\,e_{N-j}.
\]
For \(k\ge0\), both operators send \(e_k\) to \(\sqrt{h_{k+N}/h_k}\,e_{k+N}\). For \(j\ge N\), both send \(e_{-j}\) to \(\sqrt{h_j/h_{j-N}}\,e_{N-j}\), where \(j=N\) uses \(h_0=1\). The asserted formula for \(D_N\) follows, and its nonzero initial and final basis vectors are orthogonal within their respective families.

**2. Positivity, rank, and nilpotence.** For \(1\le j<N\), take independent copies \(X,Y\) of the nondegenerate random variable above. Then
\[
 2(h_N-h_jh_{N-j})
 =\mathbb E\bigl[(X^j-Y^j)(X^{N-j}-Y^{N-j})\bigr]>0.
\]
Thus all \(d_{j,N}\) are strictly positive. The map sends the \(N-1\) basis vectors \(e_{-1},\ldots,e_{-(N-1)}\) to distinct positive-index basis vectors and annihilates their targets, proving rank \(N-1\), square-zero, and the exact singular-value multiset.

**3. Location of the largest singular value.** The moment ratios are
\[
 \frac{h_{r+1}}{h_r}=\frac{r+1}{r+a+1},
\]
which increase strictly with \(r\), because \(a>0\). Hence the positive products \(h_jh_{N-j}\) decrease strictly toward the central index and then increase symmetrically. As \(x\mapsto h_N/\sqrt{x}-\sqrt{x}\) strictly decreases, the largest \(d_{j,N}\) occurs exactly at the center. It is simple for even \(N\) and has multiplicity two for odd \(N\).

**4. Limit distribution.** The gamma-ratio asymptotic gives
\[
 h_j=\Gamma(a+1)j^{-a}(1+O(j^{-1})),\qquad j\to\infty.
\]
Uniformly for \(j/N\) in any fixed compact subinterval of \((0,1)\), one obtains
\[
 d_{j,N}=[(j/N)(1-j/N)]^{a/2}+o(1).
\]
Indeed, the first term in \(d_{j,N}\) converges uniformly to this profile and its second term tends uniformly to zero. Every \(d_{j,N}\) lies in \((0,1)\), since it is positive and is bounded above by the corresponding matrix coefficient of the contraction \(T_{z^N}\). Given continuous \(F\), ignore the at most \(2\delta N+O(1)\) endpoints with \(j/N\notin[\delta,1-\delta]\), apply uniform convergence and a Riemann sum to the middle, and then let \(\delta\downarrow0\). This proves the asserted weak distribution law without any tacit uniform gamma asymptotic at the endpoints. The density follows by the two inverse branches of \(t(1-t)\).

**5. Norms and quantiles.** The central formula combined with the same gamma ratios gives \(\|D_N\|\to(1/4)^{a/2}=2^{-a}\). Choosing \(F(y)=y^p\) in the weak law proves
\[
 \lim_{N\to\infty}\frac1N\sum_{j=1}^{N-1}d_{j,N}^p
 =\int_0^1[t(1-t)]^{ap/2}\,dt
 =\mathrm B(1+ap/2,1+ap/2).
\]
This yields the Schatten statement for every fixed \(p>0\). Strict center-directed monotonicity gives the quantile formula: the \(u\)-fraction of greatest singular values corresponds asymptotically to the centered interval \([(1-u)/2,(1+u)/2]\); its endpoint profile is \(2^{-a}(1-u^2)^{a/2}\).

## Verification

A standalone Python 3 program, `CHECK.py`, independently constructs the monomial Toeplitz-projection action from exact rational moments for integer \(a\in\{1,2,3,5\}\), computes powers by repeated one-step shifts, and compares every coefficient for \(2\le N\le21\) over the range of basis indices from \(-2N\) through \(2N\). It also checks exact strict positivity, reflection symmetry, central monotonicity, and degree-four explicit coefficients. Separate numerical gamma-function tests for \(a\in\{1,2,3\}\) and \(N=20000\) test the norm and Schatten-limit approximations. The program reports **68,619 passing finite assertions**. These computations cannot certify the all-parameter or infinite-rank asymptotic claims; those follow from the preceding analytical proof.

For the ordinary unweighted harmonic Bergman space \(\alpha=0\), the theorem gives the concrete limits
\[
 \lim_{N\to\infty}\|D_N\|=\frac12,\qquad
 \lim_{N\to\infty}\frac{\|D_N\|_{\mathcal S_1}}N=\frac\pi8,\qquad
 \lim_{N\to\infty}\frac{\|D_N\|_{\mathcal S_2}^2}N=\frac16.
\]

## Relationship to prior work

Huang, Wang and Zhao (2026) determine spectra and Weyl behavior of individual polynomial-symbol Toeplitz operators on the unweighted harmonic Bergman space. They do not establish a spectral law for the growing-power difference \(T_{z^N}-(T_z)^N\).

Dong and Zhou (2010) treat when products of two quasihomogeneous harmonic Bergman Toeplitz operators are Toeplitz; their Theorem 1.3 and preliminary monomial formulas concern fixed symbols. Dong and Zhou (2014) classify finite-rank two-factor generalized semicommutators and give canonical forms, including analytic monomials. Those results provide important background and may permit recovery of portions of the fixed-degree algebra; **the finite-rank phenomenon itself is not claimed as novel**. The present quantitative result addresses the complete singular spectrum of a growing number of factors, every power-weight \(\alpha>-1\), and the bulk limit and sharp \(\mathcal S_p\) growth for all \(p>0\). Choe, Koo and Lee (2008) also classify finite-rank/compact sums of Toeplitz products on the analytic Bergman space, a different compression space.

## Limitations

The statement concerns the monomial generator \(z\), fixed radial beta weight, and positive integer powers. The result is not a classification for general analytic symbols, nonradial weights, or joint limits of weight and power. A sharper finite-\(N\) error term and behavior in moving-parameter regimes are not established. An equivalent singular-law formulation may be implicit in older work on compressed bilateral weighted shifts; this remains a residual publication-priority risk. This is a mathematical proof subject to independent expert review; no independent audit or formal certification has been performed.

## References

1. M. Huang, J. Wang and X. Zhao, *The spectral structure of Toeplitz operators with polynomial symbols on the harmonic Bergman space*, arXiv:2610.09638v1 (first submitted October 7, 2026), https://arxiv.org/abs/2610.09638.
2. X.-T. Dong and Z.-H. Zhou, *Products of Toeplitz operators on the harmonic Bergman space*, Proceedings of the American Mathematical Society 138 (2010), 1765–1773, DOI:10.1090/S0002-9939-09-10204-6.
3. X.-T. Dong and Z.-H. Zhou, *Ranks of commutators and generalized semicommutators of quasihomogeneous Toeplitz operators*, arXiv:1411.0213 (first submitted November 2, 2014), https://arxiv.org/abs/1411.0213.
4. B. R. Choe, H. Koo and Y. J. Lee, *Sums of Toeplitz products with harmonic symbols*, Revista Matemática Iberoamericana 24 (2008), 43–70, DOI:10.4171/RMI/529.
