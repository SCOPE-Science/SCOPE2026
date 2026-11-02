# Opposite global resetting optima for fresh and persistent uniform anchors on a Brownian circle

## Finding
Let a Brownian searcher with generator \(D\partial_{xx}\), \(D>0\), move on a circle of circumference \(2\ell\), \(\ell>0\), and be absorbed at one fixed point. Its initial position is uniform. Independently, an exponential clock of rate \(r>0\) triggers instantaneous positional resets. Compare:

- **Fresh-anchor protocol (A):** every reset location is a fresh independent uniform position on the circle.
- **Persistent-anchor protocol (Q):** the initially sampled position is an anchor that is retained throughout the search, and every reset returns to that same position.

Write \(T_{\mathrm A}(r)\) and \(T_{\mathrm Q}(r)\) for the respective unconditional mean absorption times, and \(z=\ell\sqrt{r/D}\). The exact identities are
\[
T_{\mathrm A}(r)=\frac{\ell^2}{D}\frac{z\coth z-1}{z^2},\qquad
T_{\mathrm Q}(r)=\frac{\ell^2}{D}\frac{\cosh z\,\arctan(\sinh z)/z-1}{z^2}.
\]
The unreset mean is \(T_0=\ell^2/(3D)\), and the strict global ordering
\[
\boxed{0<T_{\mathrm A}(r)<T_0<T_{\mathrm Q}(r)<\infty}\quad\text{for every }r>0
\]
holds. Moreover, \(T_{\mathrm A}\) decreases strictly with \(r\), with unattained infimum zero as \(r\to\infty\); the unique global minimizer of \(T_{\mathrm Q}\) over \(r\geq0\) is \(r=0\). The low-rate expansions (with \(z\downarrow0\)) are
\[
\frac{D T_{\mathrm A}}{\ell^2}=\frac13-\frac{z^2}{45}+\frac{2z^4}{945}+O(z^6),\qquad
\frac{D T_{\mathrm Q}}{\ell^2}=\frac13+\frac{z^4}{315}+O(z^6).
\]
In particular the linear-in-rate perturbation of the persistent-anchor population mean vanishes exactly. At high rate, \(z\to\infty\),
\[
T_{\mathrm A}\sim\frac{\ell^2}{Dz},\qquad
T_{\mathrm Q}\sim\frac{\pi\ell^2}{4D}\frac{e^z}{z^3},\qquad
\frac{T_{\mathrm Q}}{T_{\mathrm A}}\sim\frac{\pi}{4}\frac{e^z}{z^2}.
\]
There is also a distributional comparison. If \(\tau_{\mathrm A},\tau_{\mathrm Q}\) are the two first-passage times, then for every \(s>0\) and \(r>0\),
\[
\mathbb E[e^{-s\tau_{\mathrm Q}}]<\mathbb E[e^{-s\tau_{\mathrm A}}].
\]
This Laplace-transform ordering extends beyond circles to arbitrary reset-free motions when the fresh reset-site distribution is the same nondegenerate distribution from which a persistent anchor is sampled, provided the corresponding no-reset first-passage Laplace transform is not almost surely constant and absorption occurs almost surely under both protocols.

## Assumptions and scope
The Brownian generator is \(D\partial_{xx}\), not \((D/2)\partial_{xx}\). The circle has circumference \(2\ell\), the absorbing point is hit continuously, and the first uniform position is chosen once at time zero. In protocol A all subsequent reset sites are independent uniform draws; in protocol Q the single initial draw persists. Reset events are independent of Brownian noise and do not consume time. Expectations average both diffusive paths and the initially selected position. The formulas hold for every finite \(D,\ell,r>0\), with \(r=0\) understood as a limit. In the broader Laplace-order assertion, assume the reset-free hitting-time transform \(\phi_\lambda(x)=\mathbb E_x[e^{-\lambda\tau_0}]\) exists for each \(\lambda>0\) and lies in \((0,1]\) on the support of the sampling distribution, and the relevant means when discussed are finite.

## Proof
**1. Free hitting transform.** Folding the circle at the point antipodal to the target turns the search into reflected Brownian motion on \([0,\ell]\) absorbed at zero. The folded distance \(x\) of a uniform initial position is uniform on \([0,\ell]\). The no-reset Laplace transform solves
\[
D\phi_\lambda''=\lambda\phi_\lambda,\quad \phi_\lambda(0)=1,\quad \phi_\lambda'(\ell)=0,
\]
so, with \(k=\sqrt{\lambda/D}\),
\[
\phi_\lambda(x)=\frac{\cosh(k(\ell-x))}{\cosh(k\ell)}.
\]
The unreset mean solves \(D m''=-1\), \(m(0)=0\), \(m'(\ell)=0\); thus \(m(x)=x(2\ell-x)/(2D)\) and its uniform average is \(T_0=\ell^2/(3D)\).

**2. Two distinct renewal averages.** For fixed reset anchor \(x\), the renewal identity gives
\[
\mathbb E_x\tau^{(x)}_r=\frac{1-\phi_r(x)}{r\phi_r(x)}.
\]
If the reset site is independently redrawn from distribution \(\rho\) at every event and the initial state also has distribution \(\rho\), renewal instead gives
\[
T_{\mathrm A}=\frac{1-\Phi_r}{r\Phi_r},\qquad\Phi_r=\int\phi_r(x)\rho(dx).
\]
For the persistent anchor, the correct average is *outside* the reciprocal:
\[
T_{\mathrm Q}=\frac1r\left(\int\frac{\rho(dx)}{\phi_r(x)}-1\right).
\]
For uniform folded \(x\), direct integration gives \(\Phi_r=\tanh z/z\). In the second integral, substitute \(u=\sqrt{r/D}(\ell-x)\), and use \(\int_0^z\operatorname{sech}u\,du=\arctan(\sinh z)\). These evaluations yield both displayed closed forms.

**3. Strict global signs.** The Mittag-Leffler partial-fraction identity
\[
\frac{z\coth z-1}{z^2}=2\sum_{n=1}^\infty\frac1{z^2+\pi^2n^2}
\]
shows that \(T_{\mathrm A}\) strictly decreases with \(r\), and at zero the sum equals \(1/3\). It decreases to zero as \(r\to\infty\). For the other protocol, write \(B(z)=\arctan(\sinh z)=\int_0^z\operatorname{sech}u\,du\) and \(H(z)=\cosh z B(z)-z-z^3/3\). Since
\[
H'(z)=\sinh z\,B(z)-z^2
=\left(\int_0^z\cosh u\,du\right)\left(\int_0^z\operatorname{sech}u\,du\right)-z^2>0
\]
for every \(z>0\) by strict Cauchy–Schwarz, and \(H(0)=0\), we have \(H(z)>0\). Consequently
\[
T_{\mathrm Q}(r)-T_0=\frac{\ell^2}{D}\frac{H(z)}{z^3}>0.
\]
This is a global, not perturbative, result. It does not assert monotonicity of \(T_{\mathrm Q}(r)\).

**4. Endpoint asymptotics.** Taylor expansion of the analytic expressions at zero gives the displayed coefficients. At infinity, \(\coth z\to1\), \(\arctan(\sinh z)\to\pi/2\), and \(\cosh z\sim e^z/2\), establishing the two leading asymptotics and their ratio.

**5. Laplace-transform ordering.** In any resetting model under the stated broader hypotheses, conditionally on anchor \(x\), the Laplace transform of the first-passage time under fixed-anchor resetting is
\[
F_{\mathrm Q}(s\mid x)=\frac{(s+r)\phi_{s+r}(x)}{s+r\phi_{s+r}(x)}.
\]
For independently resampled reset sites and matching initial distribution, the corresponding expression is
\[
F_{\mathrm A}(s)=\frac{(s+r)\Phi_{s+r}}{s+r\Phi_{s+r}}.
\]
For \(s,r>0\), the map \(u\mapsto(s+r)u/(s+ru)\) is strictly concave on \((0,1]\), since its second derivative is \(-2sr(s+r)/(s+ru)^3\). Jensen's inequality gives \(\mathbb E_\rho F_{\mathrm Q}(s\mid x)<F_{\mathrm A}(s)\) when \(\phi_{s+r}(x)\) is nonconstant \(\rho\)-almost surely. On the circle this nonconstancy holds for every \(s,r>0\).

## Verification
The accompanying standalone `verify.py` implements an independently discretized reflected/absorbed boundary-value problem, independently integrates the resulting free hitting transforms, and compares both resulting MFPTs against the closed forms. It also checks finite sets of points for strict inequalities, the small- and large-rate asymptotics, and the Cauchy–Schwarz inequality. Running `python verify.py` with a standard Python installation passed 94 deterministic numerical assertions. These finite tests are corroborative only: the all-parameter inequalities, asymptotics and Laplace-transform statement follow from the preceding analytic proof, not from numerical sampling.

## Relationship to prior work
The renewal construction, one-site MFPT on a circle and fresh-site mixture formulas are established in Julián-Salgado, Castro-Villarreal, Dagdug and Boyer (2026). Méndez, Flaquer-Galmés and Campos (2024) discuss independently drawn reset positions and the mean-first-passage averaging formula for that model on the line. Pal and Prasad (2019) study resetting to a fixed start in an absorbing interval. The present claim is **not** novelty of these renewal formulas, the elementary free-circle hitting transform, or fresh resetting itself. It is the sharply opposite **global optimization classification for matched uniform initial/reset ensembles distinguished solely by whether an anchor persists**, the exact cancellation of the persistent protocol's first-order rate response, the exponential-versus-algebraic high-rate separation, and the paired Laplace-transform ordering. The source renewal equations can be specialized to motivate and derive parts of the conclusion; independent priority assessment must determine whether the combined global classification is already implicit elsewhere.

## Limitations
The circle model relies on exactly uniform positional sampling, an ideal absorbing point, finite diffusivity, and instantaneous resetting. The strict middle comparison with the unreset mean is not claimed for arbitrary geometries or nonuniform anchor distributions. Laplace-transform ordering is weaker than pathwise or first-order stochastic dominance and is not claimed to imply either. No finite-rate optimum of the persistent protocol is asserted, and no monotonicity claim about its value away from the global minimum is made. The result has not undergone independent mathematical or publication-priority audit.

## References
1. P. Julián-Salgado, P. Castro-Villarreal, L. Dagdug, D. Boyer (2026), *Mirror transitions in diffusion with stochastic resetting confined on a ring*, arXiv:2605.08414v1, https://arxiv.org/html/2605.08414v1 (first public May 8, 2026).
2. V. Méndez, R. Flaquer-Galmés, D. Campos (2024), *First-passage time of a Brownian searcher with stochastic resetting to random positions*, arXiv:2401.01125v1, https://arxiv.org/html/2401.01125v1 (first public January 2, 2024).
3. A. Pal and V. V. Prasad (2019), *First passage under stochastic resetting in an interval*, *Physical Review E* 99, 032123, https://arxiv.org/abs/1812.03009 (first public December 7, 2018).
