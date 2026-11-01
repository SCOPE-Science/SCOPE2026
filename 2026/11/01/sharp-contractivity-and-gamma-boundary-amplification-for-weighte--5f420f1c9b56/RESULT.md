# Sharp contractivity and Gamma boundary amplification for weighted harmonic Poisson operators

## Finding

The circlewise Poisson extension associated with the standard weighted Laplacian exhibits a sharp change at weight zero, a one-dimensional discrete mode-selection law, and a universal high-frequency Gamma boundary layer. The Fourier coefficients used below are known; the claims concern their **sharp joint operator norm and maximizing frequencies**.

Fix \(\alpha>-1\), put \(\beta=\alpha+1\), and let \(0<r<1\). For the operator \(T_{\alpha,r}\) defined below, write \(\mathcal N_\alpha(r)=\|T_{\alpha,r}\|_{L^2(\mathbb T)\to L^2(\mathbb T)}\).

**(i) Sharp contraction criterion.** If \(-1<\alpha\le0\), then \(\mathcal N_\alpha(r)=1\) for every \(r\), and the only nonzero equality vectors are constants. If \(\alpha>0\), there is exactly one number \(r_c(\alpha)\in(0,1)\) satisfying
\[
(1-r_c^2)^{\alpha+1}=1-r_c.
\]
Then \(\mathcal N_\alpha(r)=1\) precisely when \(0<r\le r_c(\alpha)\); it is strictly larger than one when \(r>r_c(\alpha)\). At the threshold, constants and the first negative Fourier mode tie.

**(ii) Complete finite-radius mode selection.** For \(\alpha>0\), let \(N\) have the negative-binomial distribution
\[
\Pr(N=j)=(1-r^2)^\beta\frac{(\beta)_j}{j!}r^{2j}\quad(j=0,1,\ldots),
\]
and set \(S_k=\Pr(N\ge k)\). All negative-frequency moduli are \(m_k=r^{-k}S_k\) for \(k\ge1\), with \(m_0=1\). The ratios \(m_{k+1}/m_k\) decrease strictly in \(k\ge0\); consequently, at every radius the maximizing Fourier frequency is unique or consists of two consecutive nonpositive frequencies. The maximum is attained on exactly those Fourier modes where \(m_k\) is maximal, and any superposition of tied modes is also extremal. Explicitly, the first \(k\) with \(\Pr(N=k)/S_k\ge1-r\) is a maximum index; equality gives a tie between \(k\) and \(k+1\).

**(iii) Boundary limit and localization.** For \(\alpha>0\), define
\[
F_\alpha(t)=e^t\frac{\Gamma(\alpha+1,2t)}{\Gamma(\alpha+1)},\qquad t\ge0,
\]
where \(\Gamma(\beta,x)=\int_x^\infty u^{\beta-1}e^{-u}\,du\). There is a unique maximizer \(t_\alpha>0\), characterized by
\[
\frac{(2t_\alpha)^\alpha e^{-2t_\alpha}}{\Gamma(\alpha+1,2t_\alpha)}=\frac12.
\]
Writing \(\mathcal M_\alpha=F_\alpha(t_\alpha)>1\), one has
\[
\lim_{r\uparrow1}\mathcal N_\alpha(r)=\mathcal M_\alpha,
\qquad \lim_{r\uparrow1}k(r)(1-r)=t_\alpha
\]
for **every** choice \(k(r)\) of a maximizing negative-frequency index. In particular, the norm need not approach one even though every fixed Fourier multiplier approaches one.

**(iv) Explicit first positive weight.** When \(\alpha=1\), the negative multipliers simplify to \(m_k=r^k[1+k(1-r^2)]\). Defining
\[
\rho_j=\frac{\sqrt{1+4(j+1)^2}-1}{2(j+1)}\quad (j=0,1,2,\ldots),
\]
the maximizing index is zero below \(\rho_0=(\sqrt5-1)/2\), equals \(j+1\) for \(\rho_j<r<\rho_{j+1}\), and ties the indices \(j,j+1\) at \(\rho_j\). The boundary constants are \(t_1=1/2\) and \(\mathcal M_1=2/\sqrt e\).

## Assumptions and scope

The unit circle has normalized angular measure \(d\theta/(2\pi)\). Every statement holds for all real \(\alpha>-1\) and radii \(r\in(0,1)\) in the indicated regimes, with no positivity or regularity restrictions on complex boundary input \(f\in L^2(\mathbb T)\). Let
\[
P_\alpha(z)=\frac{(1-|z|^2)^{\alpha+1}}{(1-z)(1-\bar z)^{\alpha+1}},\quad |z|<1,
\]
with its analytic branch normalized at zero. Define
\[
(T_{\alpha,r}f)(e^{i\theta})=\frac1{2\pi}\int_0^{2\pi}P_\alpha(re^{i(\theta-\phi)})f(e^{i\phi})\,d\phi.
\]
This is the complex, not the positive real, Poisson kernel of \(\partial_z[(1-|z|^2)^{-\alpha}\partial_{\bar z}]\). Our \(m_k\) denotes the multiplier at Fourier frequency \(-k\), rather than the multiplier at positive frequency \(k\).

## Proof

**1. Fourier diagonalization.** Expanding the two geometric-power factors in \(P_\alpha\) gives \(\widehat P_\alpha(n;r)=r^n\) for \(n\ge0\). For \(k\ge1\), the coefficient at \(-k\) equals
\[
\widehat P_\alpha(-k;r)
=r^k(1-r^2)^\beta\frac{(\beta)_k}{k!}
{}_2F_1(1,\beta+k;k+1;r^2)
=r^{-k}I_{r^2}(k,\beta).
\]
For completeness, the last identity follows by differentiating both sides in \(x=r^2\), using the incomplete beta integral, and matching the zero limit as \(r\downarrow0\); equivalently it is the standard negative-binomial tail identity \(I_x(k,\beta)=\sum_{j=k}^\infty (1-x)^\beta(\beta)_j x^j/j!\). In the displayed hypergeometric term the factor \((\beta)_k/k!\) has the initial radial power \(r^k\). Parseval then implies \(\mathcal N_\alpha(r)=\sup_{k\ge0}m_k\), since all positive multipliers are at most one.

**2. Nonpositive weights.** If \(0<\beta\le1\), the sum of an independent negative-binomial random variable of shape \(\beta\) and one of shape \(1-\beta\) has shape one, with success probability \(1-r^2\). Stochastic domination therefore yields \(S_k\le r^{2k}\) (shape-one geometric tail). Thus \(m_k\le r^k<1\) for \(k\ge1\), and nonconstant positive Fourier modes also have multipliers below one. Constants are the only norm-extremizers.

**3. Unimodality for positive weights.** Assume \(\beta>1\). If \(p_j=\Pr(N=j)\), then
\[
\frac{p_{j+1}}{p_j}=r^2\frac{j+\beta}{j+1}
\]
is strictly decreasing in \(j\). Consequently the ratios \(S_k/p_k=\sum_{\ell\ge0}\prod_{i=0}^{\ell-1}(p_{k+i+1}/p_{k+i})\) decrease strictly: every nonconstant summand strictly decreases, while the constant summand equals one. Therefore the discrete hazards \(p_k/S_k\) increase strictly. Since
\[
\frac{m_{k+1}}{m_k}=\frac{1-p_k/S_k}{r},
\]
these ratios strictly decrease. They tend to \(r<1\) as \(k\to\infty\): the mass ratios tend to \(r^2\), implying \(S_{k+1}/S_k\to r^2\). The first hazard crossing thus locates the unique or adjacent-tie global maximizers. The first ratio exceeds one exactly when
\[
\frac{1-(1-r^2)^\beta}{r}>1
\quad\Longleftrightarrow\quad
(1-r^2)^\beta<1-r.
\]
Write its log sign as \(G(r)=\alpha\log(1-r)+(\alpha+1)\log(1+r)\). Then \(G(0)=0\), \(G'(r)=[1-(2\alpha+1)r]/(1-r^2)\), and \(G(r)\to-\infty\) as \(r\uparrow1\). Hence \(G\) has exactly one zero in \((0,1)\); the signs on the two sides give the stated sharp threshold.

**4. Gamma scaling and no escaping maxima.** Suppose \(r\uparrow1\) and \(k\to\infty\) with \(k(1-r)\to t\in(0,\infty)\). Put \(y=k(1-r^2)\) and change variables \(u=k(1-v)\) in the incomplete beta tail. This yields
\[
I_{r^2}(k,\beta)=\frac{\Gamma(k+\beta)}{\Gamma(k)\Gamma(\beta)k^\beta}
\int_y^k(1-u/k)^{k-1}u^{\beta-1}\,du.
\]
The prefactor tends to \(1/\Gamma(\beta)\), while \(y\to2t\) and the integrand tends to \(e^{-u}u^{\beta-1}\) and is dominated by an exponentially decreasing multiple. As \(r^{-k}\to e^t\), it follows that \(m_k\to F_\alpha(t)\). If \(k\) stays bounded or \(k(1-r)\to0\), the limit is one. If \(k(1-r)\to\infty\), it is zero: for sufficiently large \(k\), \(r^2>9/10\), and \(k\ge20\), the integrand is bounded by \(e^{-19u/20}u^{\beta-1}\); meanwhile \(r^{-k}\le\exp[y/(2r^2)]\le\exp(5y/9)\), and \(\int_y^\infty e^{-19u/20}u^{\beta-1}du\) decays faster than \(\exp(-5y/9)\). These bounds exclude both ends as maximizer limits after a positive interior comparison is found.

**5. Uniqueness of boundary maximizer.** The Gamma survival hazard
\[
h_\beta(x)=\frac{x^{\beta-1}e^{-x}}{\Gamma(\beta,x)}
\quad\text{satisfies}\quad
h_\beta(x)^{-1}=\int_0^\infty e^{-u}(1+u/x)^{\beta-1}\,du.
\]
For \(\beta>1\), its reciprocal strictly decreases from infinity to one, so \(h_\beta\) increases strictly from zero to one. The sign of \(\frac{d}{dt}\log F_\alpha(t)=1-2h_\beta(2t)\) changes exactly once, proving the unique positive maximizer and \(F_\alpha(t_\alpha)>F_\alpha(0)=1\). Compactness of rescaled maximizing indices from Step 4 then proves both boundary limits.

**6. The explicit unit-weight staircase.** At \(\beta=2\), the negative-binomial tail identity reduces to \(m_k=r^k[1+k(1-r^2)]\). Consecutive modes tie exactly when \(r[1+(k+1)(1-r^2)]=1+k(1-r^2)\), or equivalently \((k+1)r^2+r-(k+1)=0\), yielding \(\rho_k\). These radii are strictly increasing. The strict ratio ordering from Step 3 supplies all between-transition claims. Finally \(F_1(t)=e^{-t}(1+2t)\), maximized at \(t=1/2\).

## Verification

The accompanying standalone Python checker evaluates the exact incomplete-beta multipliers against the elementary unit-weight formula, all modal thresholds through twenty transitions, contractivity samples on both sides of the weight-zero transition, strict discrete mode-ratio ordering, the Gamma hazard maximum, and high-frequency scaling. It requires SciPy and passes 3,131 finite numerical assertions on the displayed test sets. Its arithmetic is corroborative; the all-parameter claims are established by Steps 1–6 rather than by finite numerical evidence.

## Relationship to prior work

Olofsson and Wittsten (2013) introduced the standard weighted Laplacian Poisson kernel and derived its Fourier expansions. These known coefficients are inputs, not new discoveries. Olofsson (2020) uses weighted Poisson representations to analyze Lipschitz regularity. Li, Ma and Wang (2023) prove weighted-harmonic Schwarz and Schwarz–Pick bounds, primarily pointwise and derivative inequalities. Their inspected results do not determine the sharp full-circle \(L^2\) norm as a function of radius, its negative-frequency selection law, the weight-dependent contractivity radius, or the Gamma boundary localization. No claim of exhaustive historical priority is made.

## Limitations

The statements concern circlewise \(L^2\) multipliers for this complex kernel, not pointwise \(L^\infty\) bounds, positive real Poisson kernels, general spatial domains, or \(L^p\) norms with \(p\ne2\). The boundary scaling assumes a fixed positive weight \(\alpha\); it is not uniform as \(\alpha\downarrow0\). The positive-weight spectral norms are achieved by frequency vectors at each fixed radius, but the limiting Gamma scaling does not provide a quantitative convergence rate. Earlier equivalent norm statements in uninspected historical literature cannot be categorically ruled out. Independent mathematical validation has not been performed.

## References

1. M. Li, X.-S. Ma, and L.-M. Wang, *Schwarz Lemma and Schwarz-Pick Lemma for solutions of the α-harmonic equation*, arXiv:2311.10310, first public 2023-11-17, https://arxiv.org/html/2311.10310v1 . Primary MSC2020 31A05.
2. A. Olofsson and J. Wittsten, *Poisson integrals for standard weighted Laplacians in the unit disc*, J. Math. Soc. Japan **65** (2013), 447–486, https://doi.org/10.2969/jmsj/06520447 .
3. A. Olofsson, *Lipschitz continuity for weighted harmonic functions in the unit disc*, Complex Variables and Elliptic Equations (2020), https://doi.org/10.1080/17476933.2019.1669572 .
