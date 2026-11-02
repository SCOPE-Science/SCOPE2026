# A quartic spectral-edge transition for Gaussian localization on two time bands

## Finding
Fix a band width \(w>0\) and separation parameter \(a>0\), put \(b=a+w\), and let \(E_{a,w}=[-b,-a]\cup[a,b]\). With the normalized Gaussian \(\phi(t)=\pi^{-1/4}e^{-t^2/2}\), the short-time Fourier transform \(V_\phi\) uses frequency normalization \((2\pi)^{-1/2}\). The localization operator \(L_{a,w}=V_\phi^*\mathbf1_{E_{a,w}\times\mathbb R}V_\phi\) on \(L^2(\mathbb R)\) has spectrum \([0,M_{a,w}]\), purely absolutely continuous and without eigenvalues, where
\[
M_{a,w}=\max_{t\in\mathbb R}m_{a,w}(t),\qquad
m_{a,w}(t)=\frac1{\sqrt\pi}\int_{E_{a,w}}e^{-(t-y)^2}\,dy.
\]
There is a unique critical \(a_c(w)>0\) satisfying
\[
2a_cw+w^2=\log\left(1+\frac{w}{a_c}\right).
\]
For \(a\le a_c(w)\), \(m_{a,w}\) has the unique global maximum at \(t=0\). For \(a>a_c(w)\), it has exactly two global maxima \(\pm t_*(a,w)\), where \(t_*>0\) is the unique positive solution of
\[
\frac{\sinh(2bt_*)}{\sinh(2at_*)}=e^{b^2-a^2}.
\]
At criticality, write \(b_c=a_c+w\), \(c=a_ce^{-a_c^2}=b_ce^{-b_c^2}\), \(\Delta=b_c^2-a_c^2\), and \(D=2c\Delta/(3\sqrt\pi)>0\). Then
\[
m_{a_c,w}(0)-m_{a_c,w}(t)=Dt^4+O(t^6),
\]
and, for the spectral superlevel length \(\mathcal N_{a,w}(s)=\left|\{t\in\mathbb R:m_{a,w}(t)>M_{a,w}-s\}\right|\),
\[
\mathcal N_{a_c,w}(s)\sim 2D^{-1/4}s^{1/4}\quad(s\downarrow0).
\]
Away from criticality, the exponent is \(1/2\): below the transition \(\mathcal N_{a,w}(s)\sim2A_0^{-1/2}s^{1/2}\), where \(A_0=-m''_{a,w}(0)/2>0\); above it \(\mathcal N_{a,w}(s)\sim4A_*^{-1/2}s^{1/2}\), where \(A_*=-m''_{a,w}(t_*)/2>0\). This is a genuine quartic spectral-edge merger, not just a change in the location of a Gaussian-convolution maximum.

For a fixed width, as \(\epsilon=a-a_c\downarrow0\) from above, set \(q'_c=cw(2+1/(a_cb_c))\). Then
\[
t_*(a,w)=\left(\frac{3q'_c}{2c\Delta}\right)^{1/2}\epsilon^{1/2}+O(\epsilon^{3/2}),
\]
\[
M_{a,w}-m_{a,w}(0)=\frac{3(q'_c)^2}{2\sqrt\pi\,c\Delta}\epsilon^2+O(\epsilon^3).
\]
These expansions quantify the square-root splitting of the optimal observation locations and its quadratic improvement in the localization norm.

## Assumptions and scope
All statements are for \(w>0\), \(a>0\), \(b=a+w\), with a frequency-unrestricted phase-space mask \(E_{a,w}\times\mathbb R\). The Gaussian and short-time Fourier transform are normalized by
\[
\phi(t)=\pi^{-1/4}e^{-t^2/2},\qquad
V_\phi f(x,\xi)=\frac1{\sqrt{2\pi}}\int_{\mathbb R}f(t)\overline{\phi(t-x)}e^{-i\xi t}\,dt.
\]
The operator is bounded and positive but not compact. The reported superlevel length is Lebesgue measure in the original time variable \(t\); it is not a discrete eigenvalue-counting function. \(M_{a,w}\) is a spectral supremum but is not an attained Rayleigh quotient for any nonzero \(L^2\) function.

## Proof
**Exact reduction.** By Plancherel in the frequency variable and Tonelli for nonnegative integrands,
\[
\int_{\mathbb R}|V_\phi f(x,\xi)|^2\,d\xi
=\int_{\mathbb R}|f(t)|^2|\phi(t-x)|^2\,dt.
\]
Polarization gives \(\langle L_{a,w}f,g\rangle=\int m_{a,w}(t)f(t)\overline{g(t)}\,dt\), so \(L_{a,w}\) is multiplication by \(m_{a,w}\). In terms of the error function,
\[
m_{a,w}(t)=\frac12\big[\operatorname{erf}(b-t)-\operatorname{erf}(a-t)+\operatorname{erf}(b+t)-\operatorname{erf}(a+t)\big].
\]
The function is even, strictly positive and real analytic, tending to zero at both infinities.

**Exactly one modal transition.** Direct differentiation yields
\[
m'_{a,w}(t)=\frac{2e^{-t^2}}{\sqrt\pi}
\big[e^{-a^2}\sinh(2at)-e^{-b^2}\sinh(2bt)\big].
\]
For \(t>0\) the ratio \(R(t)=\sinh(2bt)/\sinh(2at)\) is strictly increasing, because the derivative of \(\log R\) is \([2bt\coth(2bt)-2at\coth(2at)]/t>0\); here \(x\coth x\) increases strictly for \(x>0\), as \(\sinh x\cosh x>x\). Also \(R(0+)=b/a\) and \(R(+\infty)=+\infty\). Consequently \(m'\) is negative for all \(t>0\) if \(e^{b^2-a^2}\le b/a\), whereas if \(e^{b^2-a^2}>b/a\) it is first positive and then negative with precisely one simple zero \(t_*>0\). Evenness proves the global classification. The threshold equation is \(2aw+w^2=\log(1+w/a)\); its left side minus right side has derivative \(2w+w/(a(a+w))>0\), with limits \(-\infty\) and \(+\infty\), proving existence and uniqueness for every \(w>0\).

**Quartic spectral edge.** Put \(q(a)=ae^{-a^2}-be^{-b^2}\). Taylor expansion of the exact derivative gives
\[
m'_{a,w}(t)=\frac{4q(a)}{\sqrt\pi}t+
\frac{1}{\sqrt\pi}\left[\frac83(a^3e^{-a^2}-b^3e^{-b^2})-4q(a)\right]t^3+O(t^5).
\]
At \(a=a_c\), \(q(a_c)=0\) and \(a_c^3e^{-a_c^2}-b_c^3e^{-b_c^2}=-c\Delta\), so integration gives the asserted \(m(0)-m(t)=Dt^4+O(t^6)\), with \(D=2c\Delta/(3\sqrt\pi)\). If \(s>0\) is small, the critical superlevel set consists of exactly one interval centered at zero and of half-length \((s/D)^{1/4}(1+O(s^{1/2}))\), giving \(\mathcal N(s)=2D^{-1/4}s^{1/4}(1+O(s^{1/2}))\). Outside criticality, all global maxima are nondegenerate by strict monotonicity of \(R\) at its positive root and by \(q(a)<0\) on the centered branch; the ordinary quadratic Taylor theorem gives the two stated \(s^{1/2}\) laws.

**Unfolding coefficients.** Keeping \(w\) fixed, differentiate \(q(a)\) with \(b=a+w\); at criticality \(q'_c=cw(2+1/(a_cb_c))>0\). In the variable \(z=t^2\), the stationarity equation divided by \(t\) extends real analytically near \((z,a)=(0,a_c)\) and has a nonzero \(z\) derivative \(-8c\Delta/(3\sqrt\pi)\). The implicit-function theorem yields
\[
z=\frac{3q'_c}{2c\Delta}(a-a_c)+O((a-a_c)^2),
\]
which implies the square-root law. Substituting into the Taylor expansion \(m(t)-m(0)=(2q(a)/\sqrt\pi)t^2-(2c\Delta/(3\sqrt\pi))t^4+O((a-a_c)t^4+t^6)\) gives the stated quadratic gain.

**Spectral assertions.** Since \(m\) is continuous and tends to zero, its essential range is \([0,M]\), the spectrum of its multiplication operator. For each real \(\lambda\), the level set \(\{t:m(t)=\lambda\}\) has Lebesgue measure zero because \(m\) is a nonconstant real-analytic function; hence there are no eigenvalues. The finitely many intervals of strict monotonicity allow a change of variables on each branch, showing that every scalar spectral measure is absolutely continuous with respect to Lebesgue measure on \([0,M]\). No singular-continuous spectrum occurs.

## Verification
The included standalone `check.py` uses only the Python standard library. Run `python check.py`. It checks exact root and derivative identities, positivity on both sides of the transition, the error-function normalization against quadrature, the square-root location law, the quadratic norm gain and the quartic edge constant. In one reference example \(w=1\), the critical separation is \(a_c=0.27170231920910426\ldots\), the quartic coefficient is \(D=0.14650295975805103\ldots\), and the critical spectral-edge length coefficient is \(2D^{-1/4}=3.2327222769\ldots\). Numerical checks do not replace the proof for arbitrary positive parameters or the spectral-type assertion.

## Relationship to prior work
The Gaussian-window short-time Fourier transform and localization-operator framework are standard. Nicola–Tilli (2022) prove optimal localization norm estimates for symbols in finite phase-space \(L^p\) classes; the present two infinite frequency-unrestricted bands do not meet those hypotheses. Knutsen (2020) treats radial finite/Cantor sets, with a different Hermite diagonalization. Cordero–Gröchenig (2003) establish general mapping and Schatten properties; those do not by themselves specify a two-band norm bifurcation. Gaussian smoothing and mode transitions are classical in statistics, but two-point Gaussian-mixture criteria do not directly give the above uniform-band spectral-edge constants. The new focused assertion here is the complete exact two-band multiplier mode/spectral-edge transition with sharp critical and unfolding coefficients, not the STFT reduction or general Gaussian smoothing machinery.

## Limitations
The mask is infinite in the frequency direction, so this is a continuous-spectrum result, not a compact time-frequency localization eigenvalue theorem. The bands must have equal widths and be mirror symmetric; arbitrary multiband or unequal-weight masks are not classified. Near-critical expansions are for fixed \(w\) only. The originality comparison is provisional and not an exhaustive priority certification; a specialized earlier Gaussian-smoothing formula could imply the mode criterion. No independent audit or external certification is claimed.

## References
1. F. Nicola and P. Tilli, *The norm of time-frequency and wavelet localization operators*, arXiv:2207.08624, first submitted 18 July 2022, https://arxiv.org/html/2207.08624v2 .
2. H. Knutsen, *Daubechies’ Time–Frequency Localization Operator on Cantor Type Sets I*, J. Fourier Anal. Appl. **26** (2020), article 47, https://doi.org/10.1007/s00041-020-09751-9 .
3. E. Cordero and K. Gröchenig, *Time–frequency analysis of localization operators*, J. Funct. Anal. **205** (2003), 107–131, https://doi.org/10.1016/S0022-1236(03)00166-6 .
4. P. Hall, M. C. Minnotte and C. Zhang, *Bump hunting with non-Gaussian kernels*, arXiv:math/0503676 (2005), https://arxiv.org/abs/math/0503676 .
