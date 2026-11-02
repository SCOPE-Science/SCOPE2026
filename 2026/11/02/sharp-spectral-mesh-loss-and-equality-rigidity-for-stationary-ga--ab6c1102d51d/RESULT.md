# Sharp spectral mesh loss and equality rigidity for stationary Gaussian peak counts

## Finding
For a smooth stationary Gaussian time series, strict lattice peaks cannot be more frequent per unit length than continuous local maxima. The difference has a sharp second-order spectral coefficient, and below the Nyquist mesh equality occurs only for a single nonzero spectral frequency (with an optional zero-frequency component).

Let \(I_h\) be the intensity of strict lattice peaks at spacing \(h\), and \(J\) the continuous-peak intensity. Then
\[
0\le I_h\le J=\frac1{2\pi}\sqrt{\frac{m_4}{m_2}},\qquad
\frac{I_h}{J}=1-\frac{m_2m_6-m_4^2}{12m_2m_4}h^2+o(h^2).
\]
The coefficient is nonnegative, strictly positive exactly when the derivative-energy spectrum has more than one absolute frequency. If the spectral support lies in \([ -\Omega,\Omega ]\), equality \(I_h=J\) at any \(0<h\le\pi/\Omega\) occurs precisely when the support lies in \(\{0,\pm\omega_*\}\) for one positive frequency; otherwise the inequality is strict throughout this range.

## Assumptions and scope
Let \(X(t)\), \(t\in\mathbb R\), be centered, real, stationary and Gaussian with unit marginal variance and symmetric spectral probability measure \(\mu\), so \(r(t)=\mathbb E[X(0)X(t)]=\int\cos(\omega t)\,\mu(d\omega)\). Assume \(m_6=\int\omega^6\mu(d\omega)<\infty\) and \(m_2=\int\omega^2\mu(d\omega)>0\); these imply \(0<m_4<\infty\). For each \(h>0\), define \(p_h=\Pr\{X(0)>X(-h),\ X(0)>X(h)\}\) and \(I_h=p_h/h\), including the convention \(p_h=0\) if \(r(h)=1\), when lattice ties occur almost surely. Write \(J=(2\pi)^{-1}\sqrt{m_4/m_2}\). Finite \(m_6\) guarantees an almost surely twice continuously differentiable modification. At positive separation, \(p_h\) is independent of the site by stationarity. A spectral bandlimit is assumed only for the finite-mesh equality classification.

## Proof
**1. Global non-overcount.** A strict discrete maximum at site \(ih\) has a maximizer of the continuous sample path in the open interval \(((i-1)h,(i+1)h)\), because both endpoint values are strictly lower. Two strict discrete maxima cannot occupy adjacent sites, so the open intervals assigned to different strict discrete maxima have disjoint interiors. Their continuous maxima are therefore distinct. For interior sites \(i=1,\ldots,N\), almost surely the count of strict discrete peaks is no larger than the count of continuous local maxima on \([0,(N+1)h]\). The standard one-dimensional Kac–Rice expectation for smooth stationary Gaussians is \(J\) per unit time: \(X'\) and \(X''\) are independent centered Gaussians with variances \(m_2,m_4\), and \(\mathbb E[(-X'')_+]/\sqrt{2\pi m_2}=\sqrt{m_4/m_2}/(2\pi)\). Taking expectations gives \(Np_h\le(N+1)hJ\); sending \(N\to\infty\) yields \(I_h\le J\) for every \(h>0\). The lower bound is immediate.

**2. Exact discrete identity and sixth-moment expansion.** When \(r(h)<1\), the bivariate normal orthant calculation for the two comparison differences gives the previously known exact identity
\[
 p_h=\frac1{2\pi}\arccos\!\left(\frac{2r(h)-1-r(2h)}{2[1-r(h)]}\right).
\]
Set \(V(h)=1-r(h)\), \(\Delta(h)=4V(h)-V(2h)\). The argument of arccos is \(1-\Delta(h)/(2V(h))\). Dominated convergence from finite \(m_6\) yields
\[
 V(h)=\frac{m_2h^2}{2}-\frac{m_4h^4}{24}+\frac{m_6h^6}{720}+o(h^6),\quad
 \Delta(h)=\frac{m_4h^4}{2}-\frac{m_6h^6}{12}+o(h^6).
\]
Combining these with \(\arccos(1-u)=\sqrt{2u}(1+u/12+O(u^2))\) proves
\[
 \frac{I_h}{J}=1-\frac{m_2m_6-m_4^2}{12m_2m_4}h^2+o(h^2).
\]
Indeed, under the probability measure \(\nu(d\omega)=\omega^2\mu(d\omega)/m_2\), the nonnegative numerator is \(m_2^2\operatorname{Var}_\nu(\omega^2)\). Equality in Cauchy–Schwarz is equivalent to \(\omega^2\) being constant \(\nu\)-almost surely, i.e., the spectral support away from zero consists of exactly one symmetric frequency pair.

**3. Rigidity below the highest frequency.** Suppose the spectral support is contained in \([-\Omega,\Omega]\). Fix \(0<h\le\pi/\Omega\). The positive weight
\[
 w_h(\omega)=\frac{1-\cos(h\omega)}{\omega^2}=\frac{h^2}{2}\left(\frac{\sin(h\omega/2)}{h\omega/2}\right)^2
\]
(strictly decreasing in \(|\omega|\) in the stated frequency range, with its continuous extension at zero) tilts \(\nu\) to another probability measure \(\nu_h\propto w_h\nu\). Algebra in the exact probability identity shows its arccos argument is \(\mathbb E_{\nu_h}\cos(h\omega)\). For \(s\in[0,\Omega^2]\), \(g(s)=\cos(h\sqrt s)\) is strictly convex and decreasing: for \(z=h\sqrt s\in(0,\pi]\),
\[
 g''(s)=\frac{h^4(\sin z-z\cos z)}{4z^3}>0,
\]
and the continuous limit at zero is also strictly positive. Antitone covariance gives \(\mathbb E_{\nu_h}\omega^2\le\mathbb E_\nu\omega^2=m_4/m_2\), while Jensen's inequality and the monotonicity of \(g\) imply
\[
 \mathbb E_{\nu_h}\cos(h\omega)\ge g(\mathbb E_{\nu_h}\omega^2)\ge\cos\!\left(h\sqrt{m_4/m_2}\right).
\]
Strict convexity gives strict inequality unless \(\omega^2\) is constant \(\nu\)-almost surely. As \(0\le h\sqrt{m_4/m_2}\le\pi\), decreasing arccos gives the asserted inequality and equality classification. For the classified spectra, the exact formula reduces to \(p_h=h\omega_*/(2\pi)\) for \(0<h\le\pi/\omega_*\); this also proves sharpness.

## Verification
Reproduce the finite algebra and numerical checks using the bundled standalone Python file \(\texttt{checks/check_gaussian_peak.py}\) with SymPy and mpmath. It reconstructs the sixth-moment coefficient symbolically, evaluates four covariance models at four spacings each, and tests the finite-mesh strict inequality on 96 independently seeded bandlimited mixtures. The packaged output records 128 passed numeric assertions; these are checks, not a substitute for the pathwise, Kac–Rice or Jensen proofs. Two instructive examples are the squared-exponential covariance, for which \((m_2,m_4,m_6)=(1,3,15)\) and the relative mesh-loss coefficient is \(1/6\), and an equal mixture of frequency-one and frequency-two harmonics, for which the coefficient is \(3/85\). To see that the mesh correction contains information beyond the Rice intensity, the squared-exponential covariance \(r(t)=e^{-t^2/2}\) and the monochromatic covariance \(r(t)=\cos(\sqrt3\,t)\) share the same intensity \(J=\sqrt3/(2\pi)\), but have distinct relative loss coefficients \(1/6\) and \(0\), respectively. No asymptotic error rate beyond little-\(o\) is proved.

## Relationship to prior work
Cheng and Ginos (2026), Corollary 2.4, already derive the exact stationary three-point peak probability, and Corollary 3.4 identifies the first-order infill limit \(J\). Those are inputs here, not new claims. The finite-mesh global undercount by pathwise injection, its precise equality classification for bandlimited spectra, and the sixth-moment signed sampling-loss formula are the claimed refinement. The 2007 discrete random-field paper by Taylor, Worsley and Gosselin studies discrete maxima and excursion approximations; Kratz (2006) surveys continuous Gaussian level crossings and Rice functionals. A direct second-order Taylor expansion of the published exact probability gives part of the result, which limits the independent novelty of that component; the combined nonasymptotic/equality/stability statement is the contribution assessed here.

## Limitations
No converse equality classification is claimed for unbounded spectra or for mesh spacings above \(\pi/\Omega\). The coefficient assumes a finite sixth spectral moment and does not cover rough processes. The result concerns expected numbers of strict peaks per unit length, not peak-height distributions, higher-dimensional random fields, or variance of peak counts. Historical-priority review beyond the inspected primary sources remains desirable, particularly for pre-existing continuous-versus-discrete extrema inequalities.

## References
- D. Cheng and J. Ginos, *Local Maxima of Discrete Gaussian Processes: Exact Distributions and Infill Limits* (2026), arXiv:2610.27687v1, https://arxiv.org/html/2610.27687v1 (sections 2.4, 3.4, 4.3).
- M.-F. Kratz, *Level crossings and other level functionals of stationary Gaussian processes* (2006), *Probability Surveys*, arXiv:math/0612577, https://arxiv.org/abs/math/0612577.
- J. E. Taylor, K. J. Worsley and F. Gosselin, *Maxima of discretely sampled random fields, with an application to “bubbles”* (2007), https://www.math.mcgill.ca/keith/bubbles/dlmstat.pdf.
- H. Cramér and M. R. Leadbetter, *Stationary and Related Stochastic Processes* (1967), Wiley (classical Kac–Rice theory).
