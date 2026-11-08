# A coherence-tilted arcsine law for a two-periodic quantum walk

## Finding

For a continuous-time quantum walk on the integer chain with alternating *positive* hopping amplitudes, a localized initial state has a symmetric arcsine ballistic law. A coherent preparation of **two neighbouring sites in one cell** has a different yet equally explicit limit. For arbitrary normalized amplitudes \(c,d\), put \(m=\min\{a,b\}\), \(w=\operatorname{Im}(\overline c d)\). Then

\[
\frac{X_t}{t}\ \Longrightarrow\ Y,\qquad
f_Y(y)=\frac{1-(w/a)y}{\pi\sqrt{4m^2-y^2}}\,\mathbf 1_{\{|y|<2m\}}.
\]

In particular the limiting distribution is symmetric **if and only if** \(w=0\). For each integer \(j\ge0\),

\[
\mathbb E[Y^{2j}]=\binom{2j}{j}m^{2j},\qquad
\mathbb E[Y^{2j+1}]=-\frac{w}{a}\binom{2j+2}{j+1}m^{2j+2}.
\]

The cumulative distribution on \([-2m,2m]\) is
\[
F_Y(y)=\frac12+\frac1\pi\arcsin\frac{y}{2m}+\frac{w}{\pi a}\sqrt{4m^2-y^2}.
\]
Hence \(\mathbb E Y=-2m^2w/a\) and \(\Pr(Y>0)=1/2-2mw/(\pi a)\). The largest directional imbalance \(|\Pr(Y>0)-\Pr(Y<0)|=2m/(\pi a)\) is attained at the two chirality-maximal states \((c,d)=(1,\pm i)/\sqrt2\). This is an explicit classification of the dependence of the full *ballistic velocity law* on two-site phase coherence, rather than merely a mean-displacement identity.

## Assumptions and scope

Let \(a,b>0\) be real, with dynamics for every \(n\in\mathbb Z\) and \(t\ge0\):

\[
\begin{aligned}
 i\partial_t\psi_t(2n)&=b\psi_t(2n-1)+a\psi_t(2n+1),\\
 i\partial_t\psi_t(2n+1)&=a\psi_t(2n)+b\psi_t(2n+2).
\end{aligned}
\]

The initial state has \(\psi_0(0)=c\), \(\psi_0(1)=d\), \(|c|^2+|d|^2=1\), and is zero otherwise. The normalized position observation is \(\Pr(X_t=x)=|\psi_t(x)|^2\). There is no dissipation, disorder, boundary, or time-dependent forcing. The claimed limit is weak convergence as real time \(t\to+\infty\); it is not a pointwise local central-limit statement.

## Proof

**1. Fibre spectral decomposition.** Introduce the cell Fourier transform \(\widehat\psi(k)=\sum_{n\in\mathbb Z}e^{-ikn}(\psi(2n),\psi(2n+1))^\top\), \(-\pi\le k<\pi\). Its Bloch Hamiltonian, positive band energy, and physical-site group velocity are

\[
H(k)=\begin{pmatrix}0&a+b e^{-ik}\\a+b e^{ik}&0\end{pmatrix},\quad
E(k)=\sqrt{a^2+b^2+2ab\cos k},\quad
v(k)=2E'(k)=-\frac{2ab\sin k}{E(k)}.
\]

For \(a\ne b\), the spectral projections onto the simple eigenvalues \(\pm E(k)\) are \(P_\pm(k)=(I\pm H(k)/E(k))/2\). The fibre initial vector \(\chi=(c,d)^\top\) is independent of \(k\). Direct multiplication gives

\[
\chi^\dagger\frac{H(k)}{E(k)}\chi
=\frac{2\operatorname{Re}(\overline c d)(a+b\cos k)+2wb\sin k}{E(k)}
=:s_{\mathrm{even}}(k)-\frac{w}{a}v(k),
\]

where \(s_{\mathrm{even}}\) is even and \(v\) is odd in \(k\).

**2. Justification of the ballistic weak limit.** For \(a\ne b\) the two Bloch bands are separated uniformly, so smooth differentiation of \(e^{-itH(k)}\chi=\sum_{\sigma=\pm1}e^{-i\sigma tE(k)}P_\sigma(k)\chi\) yields, for every nonnegative integer \(j\),

\[
\lim_{t\to\infty}\mathbb E[(X_t/t)^j]
=\int_{-\pi}^{\pi}\sum_{\sigma=\pm1}
 \langle\chi,P_\sigma(k)\chi\rangle
 [\sigma v(k)]^j\frac{dk}{2\pi}.
\]

Indeed the physical position operator in cell-Fourier space is \(2i\partial_k+\operatorname{diag}(0,1)\), and after dividing its \(j\)-th power by \(t^j\), only the \(j\) derivatives of the band phases survive. The bounded spectrum of group velocities, bounded second normalized moments, and moment determinacy for a compactly supported measure establish weak convergence. Equivalently, this step is an instance of the general periodic-graph ballistic limit theorem of Boutet de Monvel and Sabri (2022), whose general pushforward result is acknowledged explicitly below.

Therefore for every bounded continuous \(g\), the limiting expectation is

\[
\int_{-\pi}^{\pi}\Bigl[\frac{1+s(k)}2g(v(k))
+\frac{1-s(k)}2g(-v(k))\Bigr]\frac{dk}{2\pi}.
\]

Parity cancels the term containing \(s_{\mathrm{even}}\). Using \(v(-k)=-v(k)\) also turns the remaining odd term into the exact identity

\[
\mathbb E[g(Y)]=\int_{-\pi}^{\pi}
\left(1-\frac{w}{a}v(k)\right)g(v(k))\frac{dk}{2\pi}.
\]

**3. Explicit velocity pushforward.** Put \(M=\max\{a,b\}\), \(m=\min\{a,b\}\) and \(r=m/M\in(0,1)\). With \(\theta=\arg(e^{ik}+r)\) chosen continuously through a full circle,

\[
v(k)=-2m\sin\theta,\quad
k=\theta+\arcsin(r\sin\theta),\quad
\frac{dk}{d\theta}=1+\frac{r\cos\theta}{\sqrt{1-r^2\sin^2\theta}}.
\]

The extra Jacobian term is the derivative of \(\arcsin(r\sin\theta)\); its integral against *any continuous function of* \(\sin\theta\) over a full period is zero by a one-variable primitive. Consequently the uniform measure \(dk/(2\pi)\), pushed forward by \(v(k)\), is exactly the arcsine measure \(dy/(\pi\sqrt{4m^2-y^2})\) on \((-2m,2m)\), not merely a measure with matching low moments. Multiplication by \(1-(w/a)y\) proves the claimed density. Positivity follows from \(|w|\le|c||d|\le1/2\) and \(2m\le2a\).

**4. The gap-closing case.** When \(a=b\), one can instead use the usual one-site Fourier transform. Its scalar dispersion is \(2a\cos k\), velocity \(-2a\sin k\), and initial Fourier weight is \(|c+d e^{-ik}|^2=1+2\operatorname{Re}(\overline c d)\cos k+2w\sin k\). The cosine contribution integrates to zero against any function of the velocity, leaving exactly \(1-(w/a)v\) times the arcsine law. This separately covers the band crossing without making an invalid smooth-band argument at \(a=b\).

**5. Consequences.** Integrating the density yields the displayed CDF and moments, since \(\mathbb E_{\mathrm{arc}}[Y^{2j}]=\binom{2j}{j}m^{2j}\). The odd correction vanishes precisely for \(w=0\), proving the symmetry classification. The directional imbalance is maximized by \(|w|=1/2\), attained by equal-amplitude states with relative phases \(\pm\pi/2\).

## Verification

Run `python check.py` with NumPy in a clean folder containing the embedded checker. It evaluates Bloch spectral moment quadratures for nine normalized initial states and coupling pairs (including the gap-closing case), and separately evolves the wavefunction by finite Fourier transform at two positive times. The checker reports `PASS: 198 finite diagnostic assertions`; no finite grid, time, or diagnostic establishes the weak limit independently of the proof. The code's Bloch Hamiltonian and Fourier phases are documented and do not use the claimed density to generate wavefunctions.

## Relationship to prior work

Machida (first public version 13 April 2023, arXiv:2304.06464, Theorem 1) proves the symmetric arcsine law in the same alternating-hopping walk **with an initially localized single site**. This work changes the initial condition and obtains a genuinely asymmetric, exact continuous limiting density controlled by the imaginary coherence, together with a full moment and symmetry classification.

Boutet de Monvel and Sabri (2022, arXiv:2202.00940, Theorem 5.5) already prove **general weak convergence to band-velocity pushforward measures for arbitrary states on periodic graphs**. That general result covers the mechanism and gives an integral representation for the present case; the specific closed-form coherent two-site law, cancellation of the even Bloch component, dependence only on one coherence scalar, and exact extremal directional imbalance require an explicit evaluation not stated there. The result is not presented as a new general ballistic-convergence theorem.

Harter, Saxena and Joglekar (2018) analyze initial-state-dependent *mean displacement* in lossy and parity-time-symmetric dimer models. The present unitary, long-time **full probability law** is a different observable and dynamical model; a mean drift alone would not establish it.

## Limitations

Only two-site coherent initial states within one fixed cell, positive real alternating hoppings, and unitary evolution are covered. No local pointwise asymptotics, spatial boundaries, dissipative dynamics, arbitrary extended input waves, multidimensional arrays, or rates of weak convergence are claimed. The general pushforward principle is previously known, and the explicit formula could conceivably occur as an unindexed corollary elsewhere; an independent literature audit is not represented as having occurred. The finite numerical diagnostics cannot certify global mathematical novelty.

## References

1. T. Machida, *Limit distribution of a continuous-time quantum walk with a spatially 2-periodic Hamiltonian*, arXiv:2304.06464 (first posted 2023-04-13), https://arxiv.org/html/2304.06464v2 . In particular Theorem 1, Eq. (19) and its explicit localized initial condition.
2. A. Boutet de Monvel and M. Sabri, *Ballistic transport in periodic and random media*, arXiv:2202.00940 (2022), https://arxiv.org/html/2202.00940v1 . In particular Theorem 5.5, Eqs. (5.5)–(5.6), and the worked periodic examples.
3. A. K. Harter, A. Saxena and Y. N. Joglekar, *Fragile aspects of topological transition in lossy and parity-time symmetric quantum walks*, Scientific Reports 8, 12065 (2018), https://pmc.ncbi.nlm.nih.gov/articles/PMC6089968/ .
