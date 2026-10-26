# Interference fringes at the Gaussian–algebraic crossover of fractional quantum packets

## Finding
For a freely propagating one-dimensional Gaussian momentum packet with fractional dispersion \(H_\alpha=|P|^\alpha\), the limit \(\alpha\uparrow2\) has a sharp, logarithmically receding transition from its Gaussian core to a fractional algebraic wing. At every fixed propagation time \(t>0\), the transition exhibits persistent quantum interference rather than a simple monotone interpolation.

More precisely, set \(\varepsilon=2-\alpha\), \(L=\log(1/\varepsilon)\), and
\[
 C_t=\log\!\left(\frac{4(1+t^2)^{5/4}}{\sqrt\pi\,t}\right).
\]
For each bounded real \(s\), let \(y_\varepsilon(s)>3/2\) be the **larger** solution of
\[
 y_\varepsilon(s)-\frac32\log y_\varepsilon(s)=L+C_t+s,
 \qquad x_\varepsilon(s)=2\sqrt{(1+t^2)y_\varepsilon(s)}.
\]
This solution exists uniquely for all sufficiently small \(\varepsilon>0\), and
\[
 y_\varepsilon(s)=L+\frac32\log L+C_t+s+o(1).
\]
For every fixed \(t>0\) and \(S<\infty\), uniformly in \(|s|\le S\),
\[
 \boxed{\ \frac{\psi_{2-\varepsilon,t}(x_\varepsilon(s))}
 {\psi_{2,t}(x_\varepsilon(s))}
 =1+e^s\exp\!\left[i\left(\frac\pi2+\frac12\arctan t-t y_\varepsilon(s)\right)\right]
 +O_{t,S}(L^{-1}).\ }
\]
Consequently, if \(\theta_\varepsilon(s)=\pi/2+(\arctan t)/2-t y_\varepsilon(s)\),
\[
 \frac{|\psi_{2-\varepsilon,t}(x_\varepsilon(s))|^2}
 {|\psi_{2,t}(x_\varepsilon(s))|^2}
 =1+e^{2s}+2e^s\cos\theta_\varepsilon(s)+O_{t,S}(L^{-1}).
\]
The phase winds indefinitely when \(\varepsilon\downarrow0\). For each fixed \(s\in\mathbb R\), its intensity ratio has **exact** limit superior and inferior
\[
 \boxed{\ \limsup_{\varepsilon\downarrow0}\frac{|\psi_{2-\varepsilon,t}(x_\varepsilon(s))|^2}{|\psi_{2,t}(x_\varepsilon(s))|^2}=(1+e^s)^2,\quad
 \liminf_{\varepsilon\downarrow0}\frac{|\psi_{2-\varepsilon,t}(x_\varepsilon(s))|^2}{|\psi_{2,t}(x_\varepsilon(s))|^2}=(1-e^s)^2.\ }
\]
In particular, at \(s=0\), normalized intensities can approach either \(4\) or \(0\) along different sequences approaching the ordinary Schrödinger limit.

## Assumptions and scope
Use the unitary Fourier convention
\[\widehat f(p)=(2\pi)^{-1/2}\int_{\mathbb R}e^{-ipx}f(x)\,dx.\]
Let \(P=-i\partial_x\) on \(L^2(\mathbb R)\) and let \(H_\alpha=|P|^\alpha\) be defined by the spectral multiplier \(|p|^\alpha\). For \(1<\alpha\le2\), the normalized packet is
\[
 \widehat\psi_{\alpha,t}(p)=c\,e^{-p^2-it|p|^\alpha},
 \qquad c=(2/\pi)^{1/4},\qquad t>0.
\]
It has the **same** initial position-space Gaussian for every \(\alpha\); there is no potential, gain, or nonlinear interaction. At the classical order, with \(a=1+it\),
\[
 \psi_{2,t}(x)=\frac{c}{\sqrt{2a}}\exp\!\left(-\frac{x^2}{4a}\right).
\]
The square root has its principal branch. The theorem is for fixed \(t>0\) and compact \(s\)-intervals; no uniformity as \(t\to0\), \(t\to\infty\), or \(|s|\to\infty\) is asserted. Spatial evenness gives the corresponding result at negative positions.

## Proof
**1. Order expansion.** Write \(F_\beta(p)=e^{-p^2-it|p|^\beta}\) and \(U_\beta=(2\pi)^{-1/2}\int e^{ipx}F_\beta(p)\,dp\); then \(\psi_{\beta,t}=cU_\beta\). Differentiating with respect to \(\beta\) and Taylor expanding at \(\beta=2\) gives
\[
 U_{2-\varepsilon}(x)=U_2(x)+\varepsilon G_t(x)+R_\varepsilon(x),
 \quad G_t(x)=\frac{it}{\sqrt{2\pi}}\int_{\mathbb R}e^{ipx}|p|^2\log|p|\,e^{-ap^2}\,dp.
\]
The integrand at \(p=0\) is defined by continuity. Taylor's second-derivative integrand is
\[
 \partial_\beta^2 F_\beta(p)
 =F_\beta(p)\big[(-it)^2|p|^{2\beta}-it|p|^\beta\big](\log|p|)^2.
\]

**2. The leading algebraic coefficient.** With a smooth cutoff equal to one near zero, the standard cosine-power Fourier identity, analytically continued near \(\lambda=2\), is
\[
 \mathcal F^{-1}(|p|^\lambda)(x)
 =-\sqrt{2/\pi}\,\Gamma(\lambda+1)\sin(\pi\lambda/2)\,|x|^{-\lambda-1},\qquad x\ne0.
\]
Differentiating at \(\lambda=2\) yields \(\mathcal F^{-1}(|p|^2\log|p|)(x)=\sqrt{2\pi}\,|x|^{-3}\). Near zero, \(e^{-ap^2}=1+O_t(p^2)\); the additional \(|p|^4\log|p|\) term transforms as \(O_t(|x|^{-5})\), and the smooth cutoff-away-from-zero contribution decreases faster than any power. Therefore
\[
 G_t(x)=it\sqrt{2\pi}\,x^{-3}+O_t(x^{-5})\qquad(x\to+\infty).
\]

**3. A uniform Taylor remainder.** For \(\beta\in[2-\varepsilon,2]\), \(0<|p|<1\), and integers \(0\le j\le5\), direct differentiation of the preceding formula gives
\[
 |\partial_p^j\partial_\beta^2 F_\beta(p)|
 \le C_{t,j}|p|^{\beta-j}(1+|\log|p||)^2.
\]
The derivatives decrease rapidly for \(|p|\ge1\), uniformly in \(\beta\) in this interval. Split the inverse Fourier integral at \(|p|=1/x\), and decompose the region \(1/x\le|p|\le1\) into dyadic annuli. The lowest interval is bounded directly. On each larger annulus integrate by parts five times; the derivative estimate gives an absolutely summable geometric series, because \(5>\beta+1\). The result, uniformly for \(x\ge2\), is
\[
 |\mathcal F^{-1}(\partial_\beta^2F_\beta)(x)|
 \le C_t x^{-\beta-1}(1+\log x)^2.
\]
Taylor's integral remainder hence satisfies
\[
 |R_\varepsilon(x)|\le C_t\varepsilon^2x^{-3+\varepsilon}(1+\log x)^2.
\]
In particular, whenever \(x\asymp\sqrt L\), the preceding steps combine to give
\[
 U_{2-\varepsilon}(x)=U_2(x)+it\sqrt{2\pi}\,\varepsilon x^{-3}
 \left[1+O_t\big(x^{-2}+\varepsilon x^\varepsilon(1+\log x)^2\big)\right].
\]
The bracket error is \(O_t(L^{-1})\) because \(\varepsilon(\log L)^2=o(L^{-1})\).

**4. Exact amplitude matching and phase.** As \(a=1+it\), one has \(1/a=(1-it)/(1+t^2)\), so at \(x=2\sqrt{(1+t^2)y}\),
\[
 \frac{it\sqrt{2\pi}\,\varepsilon x^{-3}}{U_2(x)}
 =\frac{\sqrt\pi\,t}{4(1+t^2)^{5/4}}\,\varepsilon e^y y^{-3/2}
 \exp\!\left[i\left(\frac\pi2+\frac12\arctan t-ty\right)\right].
\]
The defining equation \(y-\tfrac32\log y=L+C_t+s\) makes its positive prefactor **exactly** \(e^s\), not merely asymptotic. As \(y\sim L\), step 3 now gives the stated complex-amplitude estimate, uniform on compact \(s\)-sets. Taking its modulus squared gives the intensity formula.

**5. Sharp envelopes.** At fixed \(s\), \(y_\varepsilon(s)\) is continuous and tends to \(+\infty\) as \(\varepsilon\downarrow0\). Thus the phase \(\pi/2+\tfrac12\arctan t-ty_\varepsilon(s)\) crosses infinitely many even and odd multiples of \(\pi\) for every \(t>0\). Along these two families of parameters the cosine tends respectively to \(+1\) and \(-1\). The uniform vanishing remainder proves the stated exact limsup and liminf; the elementary inequality \(-1\le\cos\theta\le1\) excludes wider envelopes.

## Verification
The accompanying standalone script `verify.py` evaluates the Fourier integral directly using high-precision quadrature rather than assuming the claimed asymptotics. It verifies the classical Gaussian integral, evenness, the first variation in fractional order, shrinking errors at the implicitly centered Gaussian–wing crossover for two propagation times, and an independent fixed-order algebraic-tail coefficient. It reports 38 successful finite assertions under `mpmath` 1.3.0. These are consistency checks only; the unbounded-parameter limits are proved by the preceding analytic argument.

## Relationship to prior work
Antar, Bakırtaş and Horikis (2026) establish by numerical propagation that fractional nonlinear Schrödinger similaritons acquire algebraic tails of order \(|x|^{-1-\alpha}\), with suppressed wings as \(\alpha\to2\). They also show beam splitting in the free linear control problem. The present theorem restricts to a **different exactly defined free, fixed-Gaussian-input problem** and determines the previously unspecified joint order/spatial limit, including the \(\tfrac32\log\log(1/\varepsilon)\) scale correction, its exact constant, coherent phase, and sharp interference envelopes. It does not claim the nonlinear similariton result.

Solaimani (2025) numerically studies Gaussian collision packets under fractional Schrödinger evolution with delta potentials; the exactly free, fractional-order boundary layer here is a baseline distinct from its scattering model. Zhang et al. (2016) analyze Gaussian-beam propagation particularly at the \(\alpha=1\) dispersion endpoint, not the present \(\alpha\uparrow2\) moving tail. Bednorz, Łochowski and Martynek (2018) bound Gaussian-versus-Pareto tail transition regions for real-valued stable probability laws; those bounds do not give this time-dependent **complex-amplitude** interference profile and do not concern a fixed Gaussian initial momentum amplitude. No priority claim beyond the inspected literature and indexed records is made.

## Limitations
The theorem is a one-dimensional free linear propagation statement for an even Gaussian spectral envelope, for fixed strictly positive time. It does not prove an analogous asymptotic law for nonlinear optical similaritons, potentials or scatterers, or uniform behavior when time approaches zero. The result concerns the ratio of probabilities at moving positions; the absolute probabilities in that remote region still tend to zero. Earlier general complex Fourier asymptotic theory could potentially subsume parts of the proof, even if the particular phase and centering are not explicitly tabulated. No independent audit has been performed.

## References
1. N. Antar, İ. Bakırtaş, T. P. Horikis, *Similaritons and tail formation in the fractional non-linear Schrödinger equation*, Journal of Nonlinear Waves **2** (2026), e20, first online 2026-10-14, DOI: 10.1017/jnw.2026.10049.
2. M. Solaimani, *Wave packet splitter and rectificator based on the Dirac delta potentials in a fractional medium*, Scientific Reports **15** (2025), 5489, DOI: 10.1038/s41598-025-87001-y.
3. Y. Zhang et al., *Diffraction-free beams in fractional Schrödinger equation*, Scientific Reports **6** (2016), 23645, DOI: 10.1038/srep23645.
4. W. M. Bednorz, R. M. Łochowski, R. Martynek, *On tails of symmetric and totally asymmetric \(\alpha\)-stable distributions*, arXiv:1802.00612 (2018).
