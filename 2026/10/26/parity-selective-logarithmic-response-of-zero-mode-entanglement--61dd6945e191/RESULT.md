# Parity-selective logarithmic response of zero-mode entanglement to a weak conformal link

## Finding
Consider the half-chain von Neumann entropy shift caused by occupying versus averaging a delocalized zero mode in the conformal-defect free-fermion chain introduced by Capizzi and Eisler [1]. For its thermodynamic-limit half-chain quantities \(\delta S_{\mathrm e}\) and \(\delta S_{\mathrm o}\), distinguished by even and odd half-chain site parity, the transmission-amplitude limit \(\lambda\downarrow0\) obeys
\[
\delta S_{\mathrm e}(\lambda)=\log2-\frac{\lambda^2}{8}\left(1+2\log\frac{2}{\lambda}\right)+O\!\left(\lambda^4\log\frac1\lambda\right),
\]
\[
\delta S_{\mathrm o}(\lambda)=\frac{\lambda^2}{4}\left(\log2-\frac12\right)+O\!\left(\lambda^4\log\frac1\lambda\right).
\]
Consequently, the even sector loses entropy at the nonanalytic scale \(\lambda^2\log(1/\lambda)\) with coefficient \(1/4\); the odd sector gains entropy at the strictly positive quadratic scale with coefficient \((\log2-1/2)/4\). The odd logarithmic contribution cancels exactly between the continuum spectral density and the edge delta peak.

## Assumptions and scope
We use precisely the free-fermion conformal defect and the mixed-minus-pure ground-state entropy convention in [1, sections 4.1–4.2], including its order of limits: first the half-chain thermodynamic limit within a specified parity subsequence, then \(\lambda\downarrow0\). The defect lies at the half-chain cut. The parameter \(\lambda\in(0,1/2]\) is the amplitude of transmission, not its square. Set \(a=\sqrt{1-\lambda^2}\), \(\varepsilon_+=2\operatorname{arcosh}(1/\lambda)\), and define the single-particle entropy kernel
\[
s(\varepsilon)=\log(1+e^{-\varepsilon})+\frac{\varepsilon}{1+e^{\varepsilon}},\qquad\varepsilon\ge0.
\]
There is no assertion about finite-length errors uniformly in \(\lambda\), Rényi indices other than one, or defect configurations differing from [1].

## Proof
The exactly derived spectral-density formulas [1, equations (67)–(68)] give
\[
\delta S_{\mathrm e}=\log2+2\int_{\varepsilon_+}^{\infty}\!\delta\rho_+(\varepsilon)s(\varepsilon)\,d\varepsilon-\frac{s(\varepsilon_+)}2,
\quad
\delta S_{\mathrm o}=2\int_{\varepsilon_+}^{\infty}\!\delta\rho_-(\varepsilon)s(\varepsilon)\,d\varepsilon-\frac{s(\varepsilon_+)}2.
\]
Write \(v=\cosh y\), \(u=\sinh y\) and substitute \(\varepsilon=2\operatorname{arcosh}(v/\lambda)\), \(0\le y<\infty\). The Jacobian is \(2u/\sqrt{v^2-\lambda^2}\). Direct substitution into [1, equation (67)] yields the exact transformed spectral weights
\[
W_\pm(y,\lambda)=\delta\rho_\pm(\varepsilon(y))\frac{d\varepsilon}{dy}
=\frac{(1\mp a)(u^2\mp a)}{2\pi v(v^2-\lambda^2)}.
\]
The symbol convention is literal: \(W_+\) uses both upper signs, and \(W_-\) both lower signs. In particular, for every \(0<\lambda\le1/2\) and \(y\ge0\), with constants independent of \(y\) and \(\lambda\),
\[
W_+(y,\lambda)=O(\lambda^2/v),\qquad
W_-(y,\lambda)=\frac1{\pi v}+O(\lambda^2/v).
\]
These estimates follow from \(1-a=\lambda^2/(1+a)\), \(u^2=v^2-1\), \(v\ge1\), and \(v^2-\lambda^2\ge3v^2/4\). Uniformly on the same range,
\[
s(\varepsilon(y))=\frac{\lambda^2}{4v^2}\left[1+2\log\frac{2v}{\lambda}\right]
+O\!\left(\frac{\lambda^4}{v^4}\left[1+\log\frac{2v}{\lambda}\right]\right).
\]
Indeed, \(e^{-\varepsilon(y)}=[\lambda/(v+\sqrt{v^2-\lambda^2})]^2\), and expansion of the logarithm and Fermi occupation is uniform because \(e^{-\varepsilon(y)}\le(2-\sqrt3)^2\). At the edge \(v=1\) this gives
\[
\frac{s(\varepsilon_+)}2=\frac{\lambda^2}{8}\left[1+2\log\frac2\lambda\right]
+O\!\left(\lambda^4\log\frac1\lambda\right).
\]
The \(W_+\)-weighted entropy integral is \(O(\lambda^4\log(1/\lambda))\), since \(\int_0^\infty v^{-3}[1+\log v]dy<\infty\). This proves the even formula.

For the odd formula, the leading \(W_-\) term yields
\[
2\int_0^\infty W_-s(\varepsilon(y))\,dy
=\frac{\lambda^2}{2\pi}\int_0^\infty\!\operatorname{sech}^3y\left[1+2\log\frac2\lambda+2\log\cosh y\right]dy
+O\!\left(\lambda^4\log\frac1\lambda\right).
\]
Differentiate \(I(p)=\int_0^\infty\operatorname{sech}^p y\,dy=\sqrt\pi\,\Gamma(p/2)/[2\Gamma((p+1)/2)]\) at \(p=3\) to obtain
\[
\int_0^\infty\operatorname{sech}^3y\,dy=\frac\pi4,\qquad
\int_0^\infty\operatorname{sech}^3y\log\cosh y\,dy=\frac\pi4\left(\log2-\frac12\right).
\]
Hence the odd continuum term equals \(\lambda^2[1+2\log(2/\lambda)]/8+\lambda^2(\log2-1/2)/4+O(\lambda^4\log(1/\lambda))\). Subtracting the identical leading edge contribution cancels the entire logarithm and proves the odd formula. Since \(\log2>1/2\), its quadratic coefficient is positive.

## Verification
All limits and error bounds above are uniform in the integration variable after the substitution. Direct high-precision quadrature of [1, equation (68)] using the transformed densities gives the ratios \(\delta S_{\mathrm o}(\lambda)/\lambda^2\) equal to approximately \(0.04898846805642\), \(0.04848848216615\), \(0.04832474858112\), and \(0.04829736469669\) for \(\lambda=0.1,0.05,0.02,0.01\), converging to \((\log2-1/2)/4=0.04828679513999\). The corresponding deviations of the even exact integral from its displayed asymptotic prediction are approximately \(-2.80630\times10^{-5}\), \(-2.15336\times10^{-6}\), \(-6.88088\times10^{-8}\), and \(-4.94969\times10^{-9}\). These are sanity checks only; the uniform estimates constitute the proof. The accompanying code reproduces the numerical checks with arbitrary-precision quadrature.

## Relationship to prior work
Capizzi and Eisler [1] established the exact spectral-density formulas (67)–(68), the endpoints \(\delta S_{\mathrm e}(0)=\log2\) and \(\delta S_{\mathrm o}(0)=0\), and parity-sensitive curves; their treatment does not state the weak-link rates, the even logarithmic coefficient, or the cancellation of logarithms in the odd sector. The result here is a new endpoint asymptotic consequence of their exact formulas, not an independent derivation of the spectral densities. Earlier zero-mode/defect entropy work [2–3] treats distinct geometry and homogeneous or Ising-defect effects, and does not provide these two weak-transmission coefficients.

## Limitations
This is a theorem about the particular exactly solved thermodynamic zero-mode entropy shifts, not arbitrary conformal defects. The half-chain thermodynamic limit is taken before the weak-transmission limit. The remainder is asymptotic, not a global error bound with an explicit optimal constant. No assertion is made about the uniformity of finite-size convergence as the defect is disconnected, nor about experimental realization. Independent validation has not been performed.

## References
[1] L. Capizzi and V. Eisler, "Zero-mode entanglement across a conformal defect," *J. Stat. Mech.* (2023) 053109, equations (54), (66)–(68), arXiv:2303.10425, https://arxiv.org/abs/2303.10425 (first public version 2023-03-18).
[2] D. Rogerson, F. Pollmann and A. Roy, "Entanglement entropy and negativity in the Ising model with defects," arXiv:2204.03601, https://arxiv.org/abs/2204.03601.
[3] A. R. Its et al. and subsequent zero-mode continuum analyses cited in [1, section 1]; contextual, not used in the proof.
