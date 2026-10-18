# Universal reflected-Gumbel zero fringe from a faint out-of-band tone

## Finding
Let \(N_c(T)\) count, with complex analytic multiplicity, all zeros of the Gaussian-window short-time Fourier transform of a monochromatic signal plus stationary proper complex bandlimited Gaussian noise in the half-open vertical strip \(0\le t<T\), with no restriction on analysis frequency. The exact count law is
\[
\mathbb E N_c(T)=T\bigl(\max\{b,\theta\}-\min\{a,\theta\}\bigr),\qquad
\frac{N_c(T)}T\longrightarrow \max\{b,\theta\}-\min\{a,\theta\}
\quad\text{almost surely and in }L^1.
\]
Here \([a,b]\) is the closed convex hull of the essential spectral support and \(\theta\) is the frequency of a deterministic tone with any fixed nonzero amplitude \(c\). No regularity, connectedness or positivity away from zero is assumed for the compactly supported integrable power spectral density.

A faint tone outside the noise spectrum has a striking singular limit. For \(\theta>b\), put \(\delta=\theta-b>0\). There is a unique frequency \(w_c\) where the tone's local Gaussian STFT power equals the noise variance. As \(|c|\downarrow0\), this frequency escapes to \(+\infty\), with
\[
w_c\sim\frac{\log(1/|c|^2)}{4\pi\delta},
\qquad
\rho_c(w_c+s)\longrightarrow
4\pi\delta^2 e^{4\pi\delta s}\exp\!\bigl(-e^{4\pi\delta s}\bigr)
\]
locally uniformly for \(s\in\mathbb R\). The limit is the reflected-Gumbel density multiplied by \(\delta\), and its total mass equals \(\delta\). For \(\theta<a\), the same statement holds with \(\delta=a-\theta\), the opposite escape direction \(w_c\to-\infty\), and the outward coordinate \(w=w_c-s\).

## Assumptions and scope
Assume \(S:\mathbb R\to[0,\infty)\) is measurable, nonzero, in \(L^1(\mathbb R)\), and vanishes almost everywhere outside a bounded interval. Its essential support endpoints satisfy \(a<b\). Let \(B\) denote proper circular complex white-noise spectral measure with independent orthogonal increments and normalization \(\mathbb E|dB|^2=d\xi\). Define the stationary complex Gaussian process
\[
W_S(t)=\int_{\mathbb R}e^{2\pi i\xi t}\sqrt{S(\xi)}\,dB(\xi),
\quad f_c(t)=W_S(t)+ce^{2\pi i\theta t},
\quad c\in\mathbb C\setminus\{0\},\ \theta\in\mathbb R.
\]
The STFT convention is
\[
V_gf(t,w)=\int_{\mathbb R} f(u)e^{-\pi(u-t)^2}e^{-2\pi i w u}\,du,
\quad g(u)=e^{-\pi u^2}.
\]
The integral exists with the usual almost-sure smooth modification. Put
\[
M(w)=\int S(\xi)e^{-2\pi\xi^2+4\pi w\xi}\,d\xi,
\quad dP_w(\xi)=M(w)^{-1} S(\xi)e^{-2\pi\xi^2+4\pi w\xi}\,d\xi,
\]
\[
m(w)=\int\xi\,dP_w(\xi),\quad
v(w)=\int(\xi-m(w))^2\,dP_w(\xi),\quad
q_c(w)=\frac{|c|^2e^{-2\pi\theta^2+4\pi\theta w}}{M(w)}.
\]
The analytic-zero convention counts multiplicities. The first intensity \(\rho_c(w)\) is independent of \(t\) and is defined by \(\mathbb EN_c([0,T)\times I)=T\int_I\rho_c(w)\,dw\).

## Proof
**1. Analytic reduction.** Gaussian integration gives the exact identity
\[
V_g f_c(t,w)=e^{-\pi w^2-2\pi iwt}H_c(t-iw),
\quad H_c(z)=\int e^{-\pi\xi^2}e^{2\pi i\xi z}\sqrt{S(\xi)}\,dB(\xi)
+ce^{-\pi\theta^2}e^{2\pi i\theta z}.
\]
Compact spectral support permits a locally uniform holomorphic modification of the stochastic integral. The prefactor has no zeros, so spectrogram zeros are precisely the zeros of \(H_c\), with multiplicity and the sign-reversed imaginary coordinate \(z=t-iw\). The noise contribution at any fixed \(t-iw\) is proper complex normal with variance \(M(w)>0\).

**2. Exact flux identity.** For a standard proper complex Gaussian \(Z\) of variance one, the circular mean identity for the logarithmic potential is
\[
\mathbb E\log|Z+\sqrt q|^2=\log q+E_1(q),\qquad
\frac{d}{dq}\mathbb E\log|Z+\sqrt q|^2=\frac{1-e^{-q}}q,
\]
for \(q>0\), where \(E_1(q)=\int_q^\infty e^{-u}du/u\). Its continuous limit at zero is \(-\gamma\). This follows by solving the radial Poisson equation for the Gaussian-convolved logarithmic potential and selecting the large-\(q\) asymptotic; it is also directly verified by radial Gaussian integration. Hence
\[
U_c(w):=\mathbb E\log|H_c(t-iw)|^2
=\log M(w)+\log q_c(w)+E_1(q_c(w)).
\]
Poincaré--Lelong and local integrability of the logarithm give the intensity \(\rho_c=(4\pi)^{-1}U_c''\). Differentiating the *positive finite* Laplace transform proves
\[
(\log M)'=4\pi m,\quad m'=4\pi v,\quad
q_c'=4\pi q_c(\theta-m).
\]
The derivative of \(U_c\), divided by \(4\pi\), is therefore the flux
\[
F_c(w)=e^{-q_c(w)}m(w)+(1-e^{-q_c(w)})\theta,
\quad \rho_c(w)=F_c'(w)
=4\pi e^{-q_c(w)}\left[v(w)+q_c(w)(\theta-m(w))^2\right].
\]
In particular \(\rho_c\ge0\) and \(F_c\) is nondecreasing.

**3. Boundary flux and exact mean.** For an integrable, compactly supported, nonzero density, exponential tilting concentrates \(P_w\) at \(b\) as \(w\to+\infty\) and at \(a\) as \(w\to-\infty\). Thus \(m(+\infty)=b\), \(m(-\infty)=a\), and the variances vanish at both ends. By the Laplace principle, \(\log M(w)=4\pi bw+o(w)\) at the positive end and \(4\pi aw+o(|w|)\) at the negative end. Comparing the deterministic exponential with these endpoint slopes shows
\[
F_c(+\infty)=\max(b,\theta),\qquad
F_c(-\infty)=\min(a,\theta).
\]
At an equality \(\theta=a\) or \(\theta=b\), either weighting in \(F_c\) tends to that same endpoint, so no exceptional case remains. Tonelli and the flux difference yield \(\mathbb E N_c(T)=T(F_c(+\infty)-F_c(-\infty))<\infty\). Thus any finite time strip contains only finitely many zeros, almost surely.

**4. Almost-sure law.** Let \(T_sW(t)=e^{-2\pi i\theta s}W(t+s)\). Proper complex Gaussian stationarity makes this flow measure preserving. Since \(S\in L^1\), the covariance \(\int S(\xi)e^{2\pi i(\xi-\theta)s}d\xi\) vanishes as \(|s|\to\infty\); hence the integer-time transformation \(T_1\) is strongly mixing (first for finite Gaussian vectors, then for the generated sigma field), and is ergodic. The STFT covariance of translation, plus the deterministic tone's phase, makes the zero count over successive unit time cells an integrable stationary ergodic sequence. Birkhoff's theorem proves \(N_c(n)/n\to \mathbb E N_c(1)\) almost surely for positive integers \(n\). Monotonicity of the counts extends the limit to real \(T\to\infty\). The normalized counts are nonnegative and have the common exact mean, so Scheffé's lemma gives \(L^1\) convergence as well.

**5. Universal spectral escape.** Suppose \(\theta>b\) and set \(\delta=\theta-b\). Since \(m(w)\le b<\theta\), the function \(q_c(w)\) increases strictly from zero to infinity. Thus there exists exactly one \(w_c\) with \(q_c(w_c)=1\). As \(|c|\downarrow0\), \(w_c\to+\infty\). The endpoint Laplace asymptotic used above and the balance equation give
\[
w_c\sim\frac{\log(1/|c|^2)}{4\pi\delta}.
\]
For bounded \(s\), integrate the exact identity \((\log q_c)'=4\pi(\theta-m)\) between \(w_c\) and \(w_c+s\). Since \(m(w)\to b\) uniformly on translated bounded intervals and \(v(w)\to0\), it follows locally uniformly that \(q_c(w_c+s)\to e^{4\pi\delta s}\), and the displayed reflected-Gumbel density limit follows from the exact formula for \(\rho_c\). Its integral is \(\delta\), by substitution \(u=e^{4\pi\delta s}\). More precisely, the flux at \(w_c+s\) tends to \(b+\delta(1-e^{-e^{4\pi\delta s}})\), identifying the mass of the escaping fringe. Frequency reflection reduces the case \(\theta<a\) to this one. At each fixed \(w\), \(q_c(w)\to0\) and \(\rho_c(w)\to4\pi v(w)\), whose integral is \(b-a\). The failure of convergence of total masses records genuine escape to unbounded frequency rather than missing finite-frequency zeros.

## Verification
The accompanying standalone `verify.py` uses 640-point Gauss--Legendre quadrature for two distinct compactly supported PSDs (constant and vanishing quadratically at the endpoints), out-of-band tones of both signs, and four decreasing tone amplitudes. It verifies the flux derivative, the Laplacian of the Gaussian logarithmic potential, and quantitative convergence toward the limiting reflected-Gumbel density. It completes 68 supplementary comparisons when run with Python, NumPy and SciPy. These finite tests do not establish any infinite-frequency or almost-sure assertion; those follow from the analytic arguments above.

## Relationship to prior work
Escudero, Koliander and Romero, *Zeros of the Spectrogram of Colored Noise* (arXiv:2609.18689, originally posted 2026-09-16), prove the general noncentral colored-noise first-intensity formula (Theorem 1.1). That formula covers the finite-frequency first intensity as a special case; **neither the general first-intensity formula nor its proof is claimed here as new**. Their separate Theorem 1.2 studies slowly varying power spectra under a strictly positive lower bound, unlike the compact-frequency-support regime here. The present result concerns the spectral-endpoint global flux, an all-frequency almost-sure law for a fixed deterministic tone, and the universal singular weak-tone boundary layer with its reflected-Gumbel profile. Feldheim, *Zeroes of Gaussian Analytic Functions with Translation-Invariant Distribution* (arXiv:1105.3929), establishes limiting zero measures for stationary centered Gaussian analytic functions, including the continuous-spectrum case: that prior result covers the centered-noise limiting law, which is not claimed as new. It does not directly give the noncentral weak-tone density fringe with fixed non-Gaussian mean. The zero intensity for spectrograms in Gaussian noise and phase-sensitive zero statistics are developed in the additional cited papers.

## Limitations
The noise spectrum must be nonzero, absolutely continuous and compactly supported; the theorem makes no claim for general unbounded PSDs or singular spectral measures. The out-of-band reflected-Gumbel limit is a first-intensity statement, not convergence of random zero point processes to a Gumbel point process. Its mass describes zeros per unit time, not a normalized probability density unless divided by \(\delta\). It is a singular limit at fixed noise PSD and vanishing nonzero tone amplitude, and does not assert the count law for a deterministic tone alone. The analysis is independently unvalidated, and any hidden equivalent spectral-edge theorem in unindexed literature remains a priority risk.

## References
1. L. A. Escudero, G. Koliander and J. L. Romero, *Zeros of the Spectrogram of Colored Noise*, arXiv:2609.18689 (first public version 2026-09-16). https://arxiv.org/pdf/2609.18689
2. N. Feldheim, *Zeroes of Gaussian Analytic Functions with Translation-Invariant Distribution*, arXiv:1105.3929 (2011). https://arxiv.org/html/1105.3929v3
3. N. Feldheim, A. Haimi, G. Koliander and J. L. Romero, *Hyperuniformity and non-hyperuniformity of zeros of Gaussian Weyl-Heisenberg Functions*, arXiv:2406.20003 (2024). https://arxiv.org/abs/2406.20003
4. R. Bardenet, J. Flamant and P. Chainais, *On the zeros of the spectrogram of white noise*, arXiv:1708.00082 (2017). https://arxiv.org/abs/1708.00082
