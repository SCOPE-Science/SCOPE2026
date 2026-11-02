# Sharp second-passage-moment threshold for a run-and-tumble particle in a logarithmic trap

## Finding
Consider a one-dimensional persistent particle on the half-line, with its velocity direction reversed at Poisson rate \(\gamma>0\), deterministic velocity \(\dot X_t=-1/(1+X_t)+v\sigma_t\), and absorption on first reaching zero. Here \(0<v<1\), \(\sigma_t\in\{-1,+1\}\), and the initial direction has probability \(1/2\) for either sign. Let \(T_x\) be the absorption time from \(X_0=x>0\), and set \(a=v^{-1}-1\) and \(D=v^2/(2\gamma)\). Then:

1. For every \(0<x\le a\), \(T_x\) has a positive exponential moment, regardless of \(\gamma>0\).
2. For every \(x>a\), the second moment \(\mathbb E T_x^2\) is finite **if and only if** \(D<1/3\), equivalently \(\gamma>3v^2/2\). In particular, in the sharp intermediate range \(v^2/2<\gamma\le3v^2/2\), the mean absorption time is finite but its variance is infinite.
3. In the finite-second-moment regime, the full large-starting-distance law is
\[
\lim_{x\to\infty}\frac{\mathbb E T_x^2}{x^4}=\frac{1}{4(1-D)(1-3D)}.
\]
Thus the deterministic one-way region and the outer persistent region have different moment spectra despite belonging to the same potential landscape.

## Assumptions and scope
The sign process is an independent continuous-time symmetric two-state chain flipping at rate \(\gamma\) (not twice that rate). The force is the derivative of \(V(x)=\log(1+x)\) for \(x\ge0\). The parameter condition \(0<v<1\) makes \(a=v^{-1}-1>0\) the unique positive point where the plus-orientation velocity vanishes. Absorption occurs at the first actual zero crossing, not at a reset. The phase average is over the two equally probable initial orientations. All constants in the limits hold at fixed \(v,\gamma\), not uniformly at criticality.

## Proof
**1. Inner region.** For \(x\le a\), both instantaneous velocities are nonpositive, and in the negative state they are at most \(-2v\). The interval \([0,a]\) is forward invariant until absorption. There is a time \(t_0<\infty\) and a probability \(p_0>0\), uniformly over every position in this interval and either initial orientation, of obtaining a sufficiently long uninterrupted negative-orientation run to hit zero by time \(t_0\). From the plus state, first demand a flip in a fixed shorter interval; from the minus state, demand no flip. Applying the Markov property in time blocks yields \(\Pr(T_x>nt_0)\le(1-p_0)^n\), including \(x=a\). Hence all positive moments and some exponential moment are finite.

**2. First-moment baseline and exact second-moment equation.** For \(x>a\), denote the moments conditioned on the initial orientation by \(m_{j,\pm}(x)=\mathbb E_{x,\pm}T^j\) and their average by \(M_j=(m_{j,+}+m_{j,-})/2\). The backward generator acts as
\[
(\mathcal L h)_\pm=(f(x)\pm v)h_\pm'(x)+\gamma(h_\mp-h_\pm),\qquad f(x)=-\frac1{1+x}.
\]
Where the moments are finite, \(\mathcal L m_j=-j m_{j-1}\), with \(m_{0,\pm}=1\). Eliminate the directional difference directly from the two backward equations. With \(A=v^2-f^2\) and \(B=2f(\gamma-f')\), the averaged functions obey
\[
A M_1''+B M_1'=f'-2\gamma,
\]
\[
A M_2''+B M_2'=2(f'-2\gamma)M_1+4fM_1'+2.
\]
(The constant \(2\) in the last equation follows directly from the two-state generator and can be checked in the zero-propulsion deterministic limit.)

The mean-first-passage analysis for this specific logarithmic potential already establishes, for outer starting positions, that \(M_1<\infty\) exactly when \(D<1\), and when finite,
\[
M_1(x)=\frac{x^2/2+x}{1-D}+O(1),\qquad M_1'(x)=\frac{x}{1-D}+O(1)\quad(x\to\infty).
\]
The second derivative claim here uses the first-order equation for \(M_1'\), not formal differentiation of the \(O(1)\) remainder. Its directional difference is \(O(x)\), so each \(m_{1,\pm}(x)=O(x^2)\).

**3. Necessity of the threshold.** Suppose first \(1/3\le D<1\) and \(M_2(x_0)<\infty\) for some \(x_0>a\). The positive-rate switching and the two directed flows communicate throughout \((a,\infty)\). The strong Markov property therefore propagates finiteness of the second moment to all starting positions \(x>a\) and both signs. Under a common sign path, ordered initial positions stay ordered, so \(M_2\) is nondecreasing: \(M_2'(x)\ge0\). Define the positive integrating factor
\[
p(x)=\exp\left[\int_R^x\frac{B(u)}{A(u)}\,du\right],\quad R>a.
\]
As \(x\to\infty\), \(p(x)\sim Cx^{-b}\) with \(b=2\gamma/v^2=1/D\) and \(C>0\). The second moment equation is
\[
\bigl(pM_2'\bigr)'=\frac pA\left[2(f'-2\gamma)M_1+4fM_1'+2\right]
\sim -\frac{1}{D(1-D)}Cx^{2-b}.
\]
For \(b\le3\), its integral from any finite \(R\) to infinity diverges to \(-\infty\), making \(pM_2'\) eventually negative, a contradiction. If \(D\ge1\), the source's mean-time divergence already implies \(\mathbb E T_x^2=\infty\). Therefore finiteness requires \(D<1/3\), with the critical equality excluded.

**4. Sufficiency.** Suppose \(D<1/3\). Introduce the nonnegative-at-infinity quartic correctors
\[
W_\pm(x)=x^4\pm\frac{2v}{\gamma}x^3.
\]
Direct generator calculation gives, uniformly in the two signs,
\[
(\mathcal LW)_\pm=4(3D-1)x^2+O(x)\qquad(x\to\infty).
\]
Since \(3D-1<0\) and \(m_{1,\pm}=O(x^2)\), some multiple of these functions satisfies \(\mathcal LW\le-2m_1\) outside a compact set. Smoothly modify the functions on that compact set, then add a sufficiently large positive multiple of the exact mean-time vector \(m_1\), whose stopped-generator drift equals \(-1\), and an additive constant to make the resulting vector \(H\ge0\) globally. This gives \(\mathcal LH\le-2m_1\) on the whole pre-absorption state space. Localization and the stopped Dynkin inequality imply
\[
2\mathbb E\int_0^T m_{1,\sigma_t}(X_t)\,dt\le H(x,\sigma_0)<\infty.
\]
By the strong Markov property and Tonelli, the integral on the left equals \(\mathbb E T^2\). Thus both conditional second moments are finite; moreover the constructed bound gives \(M_2(x)=O(x^4)\) for large \(x\).

**5. Sharp asymptotic.** In the finite case \(b>3\), the same flux equation has eventually negative right-hand side, so \(pM_2'\) tends to a nonnegative limit \(\ell\). If \(\ell>0\), then \(M_2'(x)\gtrsim x^b\), contradicting \(M_2(x)=O(x^4)\) because \(b+1>4\). Consequently \(\ell=0\), and
\[
p(x)M_2'(x)=-\int_x^\infty\frac{p(y)}{A(y)}\left[2(f'(y)-2\gamma)M_1(y)+4f(y)M_1'(y)+2\right]dy.
\]
Using \(M_1(y)\sim y^2/[2(1-D)]\), \(p(y)\sim Cy^{-b}\) and \(A(y)\to v^2\) gives
\[
M_2'(x)\sim\frac{x^3}{(1-D)(1-3D)},\qquad M_2(x)\sim\frac{x^4}{4(1-D)(1-3D)}.
\]
The limit holds for the symmetric initial-direction average and, by the same directional-difference estimates, for either fixed starting orientation at leading order.

## Verification
The included `verify.py` checks the generator corrector identities, the exact flux exponent, and the leading-order moment coefficients symbolically in the parameters. It also checks the finite-speed-to-deterministic moment recursion boundary and positive rational parameter examples. These computations support, rather than replace, the integral divergence argument and stopped-generator proof. Run with `python verify.py` using SymPy.

## Relationship to prior work
Guéneau, Majumdar and Schehr derive the complete **first** mean-passage-time phase diagram for the same logarithmic potential, including the boundary \(\gamma=v^2/2\), and give formal higher-moment backward equations. They do not establish the **second**-moment existence boundary, the finite-mean/infinite-variance intermediate phase, or the exact outer \(x^4\) coefficient. The Brownian Bessel-like first-passage literature contains analogous diffusion thresholds, but replacing a two-state velocity process by its effective diffusivity is only a heuristic without the present nonlocal persistence and turning-point analysis. No uniqueness or exhaustive publication-priority claim is made.

## Limitations
The result assumes symmetric exponential flips, a deterministic nonthermal RTP, logarithmic potential with unit amplitude and \(0<v<1\). It classifies the second moment, not the full passage-time tail or arbitrary higher moments. The \(x\to\infty\) limit is at fixed parameters; no uniform critical-window asymptotic is claimed.

## References
- M. Guéneau, S. N. Majumdar and G. Schehr, *Run-and-tumble particle in one-dimensional potentials: mean first-passage time and applications*, arXiv:2409.16951v1 (first public September 25, 2024), Sections II and IV and Appendix B. https://arxiv.org/html/2409.16951v1
- M. Guéneau, S. N. Majumdar and G. Schehr, *Optimal mean first-passage time of a run-and-tumble particle in a class of one-dimensional confining potentials*, arXiv:2311.06923v1 (2023). https://arxiv.org/abs/2311.06923
- E. Martin, U. Behn and G. Germano, *First-passage and first-exit times of a Bessel-like stochastic process*, arXiv:1007.4588 (2010); a Brownian-logarithmic-potential comparison, not the same persistent process. https://arxiv.org/abs/1007.4588
