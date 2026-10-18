# The fourth-moment transition for cubic-chirped Gaussian ambiguity functions

## Finding

Let the unit-energy signal be
\[
f_\lambda(t)=2^{1/4}\exp(-\pi t^2+i\lambda t^3),\qquad t,\lambda\in\mathbb R,
\]
and use the symmetric self-ambiguity convention
\[
A_\lambda(\tau,\nu)=\int_{\mathbb R} f_\lambda(t+\tau/2)
\overline{f_\lambda(t-\tau/2)}e^{-2\pi i\nu t}\,dt.
\]
Put \(c=3|\lambda|/(2\pi)\) and, for every fixed real \(p>0\), define the ambiguity moment
\[
M_p(c)=\int_{\mathbb R^2}|A_\lambda(\tau,\nu)|^p\,d\tau\,d\nu.
\]
**Theorem.** The ambiguity function is nonzero at *every* real delay–Doppler point, including for all nonzero cubic phases. Its moments are finite and obey the complete exact law
\[
M_p(c)=\sqrt{\frac2p}\int_{\mathbb R}e^{-p\pi\tau^2/2}
(1+c^2\tau^2)^{(2-p)/4}\,d\tau,\qquad M_p(0)=\frac2p.
\]
For \(c>0\), with \(U\) the standard Tricomi confluent hypergeometric function,
\[
M_p(c)=\frac{\sqrt{2\pi/p}}c
U\left(\frac12,2-\frac p4,\frac{p\pi}{2c^2}\right).
\]
For each fixed \(p>2\), \(M_p(c)\) is strictly decreasing in \(c>0\); for \(0<p<2\) it is strictly increasing; \(M_2(c)=1\) exactly. Thus the zero-free non-Gaussian ambiguity functions move strictly away from the sharp Gaussian \(p\)-moment endpoint for \(p>2\) without acquiring any zeros.

The **strong-chirp moment transition occurs at exactly \(p=4\)**, with all constants explicit. For each fixed \(0<p<4\),
\[
M_p(c)\sim K_p c^{1-p/2},\qquad
K_p=\sqrt{\frac2p}\left(\frac{p\pi}{2}\right)^{p/4-1}
\Gamma\left(1-\frac p4\right).
\]
For \(p=4\), with \(K_0\) the modified Bessel function of the second kind,
\[
M_4(c)=\frac{e^{\pi/c^2}K_0(\pi/c^2)}{\sqrt2\,c}
=\frac{2\log c+\log(2/\pi)-\gamma}{\sqrt2\,c}
+O\left(\frac{\log c}{c^3}\right),
\]
where \(\gamma\) is Euler's constant. For each fixed \(p>4\),
\[
M_p(c)\sim\frac{D_p}{c},\qquad
D_p=\sqrt{\frac{2\pi}{p}}\,
\frac{\Gamma(p/4-1)}{\Gamma(p/4-1/2)}.
\]
All asymptotics are as \(c\to+\infty\). In particular \(M_p(c)\to0\) for every \(p>2\), but \(M_2(c)=1\) and \(A_\lambda(0,0)=1\) for all \(c\).

## Assumptions and scope

The phase parameter \(\lambda\) is any real number. The moment exponent \(p>0\) is fixed while \(c\to\infty\); none of the displayed asymptotics is asserted uniformly when \(p\) approaches \(4\) with \(c\). All integrals are ordinary Lebesgue integrals; \(f_\lambda\) is a Schwartz function and has unit squared \(L^2\)-norm. The Doppler-frequency Fourier kernel is \(e^{-2\pi i\nu t}\), so no implicit \(2\pi\) conversion is permitted. The statement concerns self-ambiguity, not arbitrary cross-ambiguity pairs or time-limited cubic chirps.

## Proof

**1. Exact Fourier–Gaussian reduction and global zero-freeness.** The elementary cubic identity
\[
(t+\tau/2)^3-(t-\tau/2)^3=3\tau t^2+\frac{\tau^3}{4}
\]
and the Gaussian identity
\[
(t+\tau/2)^2+(t-\tau/2)^2=2t^2+\frac{\tau^2}{2}
\]
reduce the defining integral to a Gaussian integral with coefficient \(2\pi-i3\lambda\tau\), whose real part is \(2\pi>0\). With the signed parameter \(d=3\lambda/(2\pi)\), the standard principal square-root branch, continuous from \(\tau=0\), gives
\[
A_\lambda(\tau,\nu)=
\frac{e^{-\pi\tau^2/2+i\lambda\tau^3/4}}{\sqrt{1-id\tau}}
\exp\!\left[-\frac{\pi\nu^2}{2(1-id\tau)}\right].
\]
Neither the denominator nor any exponential factor vanishes for real \(\tau,\nu\). Thus there are no real ambiguity zeros, whether \(\lambda\) vanishes or not. Taking moduli removes the sign of \(d\) and yields
\[
|A_\lambda(\tau,\nu)|=
 e^{-\pi\tau^2/2}(1+c^2\tau^2)^{-1/4}
\exp\!\left[-\frac{\pi\nu^2}{2(1+c^2\tau^2)}\right].
\]

**2. Moment identity and special functions.** Raise this positive expression to the power \(p\) and integrate first in \(\nu\). Tonelli's theorem applies for every \(p>0\), and
\[
\int_{\mathbb R}e^{-p\pi\nu^2/[2(1+c^2\tau^2)]}\,d\nu
=\sqrt{\frac{2(1+c^2\tau^2)}p}.
\]
This gives the exact one-dimensional integral in the theorem. Its Gaussian tail proves finiteness for every fixed \(p>0\) and finite \(c\). At \(c=0\) both Gaussians integrate to \(M_p(0)=2/p\). For \(c>0\), the substitution \(u=c\tau\), followed by \(s=u^2\), gives
\[
M_p(c)=\frac{\sqrt{2/p}}c
\int_0^\infty e^{-p\pi s/(2c^2)}
 s^{-1/2}(1+s)^{(2-p)/4}\,ds.
\]
The integral representation
\[
U(a,b,z)=\frac1{\Gamma(a)}\int_0^\infty e^{-zs}s^{a-1}(1+s)^{b-a-1}\,ds,
\quad a,z>0,
\]
then proves the stated Tricomi formula. In the special case \(p=4\), substitute \(u=\sinh v\) in the even integral to obtain
\[
\int_{\mathbb R}\frac{e^{-2\pi u^2/c^2}}{\sqrt{1+u^2}}\,du
=e^{\pi/c^2}K_0(\pi/c^2),
\]
which establishes the exact Bessel expression. The familiar small-argument expansion
\(K_0(z)=-\log(z/2)-\gamma+O(z^2|\log z|)\) proves its stated expansion after multiplication by \(e^z\). The error is \(O(c^{-3}\log c)\).

**3. Monotonicity and normalization.** For \(\tau\ne0\), the factor \((1+c^2\tau^2)^{(2-p)/4}\) strictly decreases with \(c>0\) for \(p>2\), strictly increases for \(p<2\), and is identically one for \(p=2\). The Gaussian weight is strictly positive, so integration preserves strict inequalities. At \(p=2\), \(M_2(c)=\int_{\mathbb R}e^{-\pi\tau^2}\,d\tau=1\), in accordance with Moyal's identity. Separately, direct normalization gives
\(\|f_\lambda\|_2^2=\sqrt2\int_{\mathbb R}e^{-2\pi t^2}\,dt=1\).

**4. Strong-chirp regimes.** Write \(b=(2-p)/4\). For \(0<p<4\), divide the moment formula by \(c^{1-p/2}=c^{2b}\) to get an integrand with factor \((c^{-2}+\tau^2)^b\). Pointwise away from zero it converges to \(|\tau|^{2b}\). If \(b\ge0\), for \(c\ge1\) it is dominated by \((1+\tau^2)^b\); if \(-1/2<b<0\), it is dominated by \(|\tau|^{2b}\). Both dominate after multiplication by the same Gaussian weight and are integrable. Dominated convergence therefore gives
\[
\lim_{c\to\infty}c^{p/2-1}M_p(c)
=\sqrt{\frac2p}\int_{\mathbb R}
 e^{-p\pi\tau^2/2}|\tau|^{1-p/2}\,d\tau.
\]
The Gamma integral evaluates the right-hand side to \(K_p\). For \(p>4\), put \(u=c\tau\), so
\[
cM_p(c)=\sqrt{\frac2p}\int_{\mathbb R}
 e^{-p\pi u^2/(2c^2)}(1+u^2)^{(2-p)/4}\,du.
\]
The remaining weight is integrable exactly when \(p>4\), providing a dominating function and a limit. With \(u=\tan\theta\) or the beta integral, its integral equals
\(\sqrt\pi\,\Gamma(p/4-1)/\Gamma(p/4-1/2)\), proving \(D_p\). At the boundary \(p=4\), neither dominated-convergence argument has an integrable limit: the limiting integrand has a \(1/|u|\) tail. The exact Bessel identity from step 2 gives the logarithmic law, completing all three cases.

## Verification

The companion independent quadrature checker evaluates four samples of the original complex ambiguity integral and compares them to the closed form at 48-decimal precision. It also compares the moment integral against the Tricomi representation for seven exponents and three chirp strengths, verifies the Bessel identity and Moyal normalization, and prints finite-strength asymptotic ratios. These checks passed. They are finite numerical consistency tests, not substitutes for the above all-real-parameter proof. Run with Python and `mpmath`: `python check_moments.py`.

## Relationship to prior work

Lieb's classical \(L^p\) ambiguity-function bounds, reproduced explicitly in Jung's 2006 analysis of weighted ambiguity norms, imply the universal sharp endpoint \(M_p\le2/p\) when \(p>2\), with equality only for Gaussian waveforms. They do not determine the *parameter-dependent* moments of cubic-phase Gaussians or the \(p=4\) logarithmic strong-chirp transition. Jaming's 2006 result concerns moment-based zero-free neighborhoods for general signals, not global zero-freeness of this explicit non-Gaussian family. Wang, Wang and Li's 2013 cubic-chirp signal model is connected to nonlinear phase modulation but concerns parameter estimation and image formation, not ambiguity moments. The exact elementary Fourier–Gaussian reduction is used here as a proof component, not presented as novel by itself.

## Limitations

The proposed originality is the complete fixed-exponent moment law and its three-regime strong-chirp asymptotics (including the logarithmic critical exponent), taken as a single theorem; neither the Gaussian integral nor the general ambiguity-function definitions are claimed as novel. The result does not treat non-Gaussian amplitude envelopes, higher-degree phases, finite observation windows, cross-ambiguity functions, or varying \(p\) near the transition. An equivalent treatment in unindexed optical/cubic-phase or signal-processing literature remains possible. Full text of Lieb's 1990 primary paper was not accessible here; its published abstract and Jung's full-text statement of the inequality support only the specific comparison described above. No independent priority determination has been made.

## References

1. P. Jung, *Weighted Norms of Ambiguity Functions and Wigner Distributions*, first public arXiv version 6 January 2006, arXiv:cs/0601017, https://arxiv.org/abs/cs/0601017. Full primary text inspected, especially Sections I–II and Theorems 3–4.
2. P. Jaming, *Zero-free regions of radar ambiguity functions and moments*, first public arXiv version 16 June 2006, arXiv:math/0606397, https://arxiv.org/abs/math/0606397. Full primary text inspected, especially Sections 1 and 3, Theorem 3.1.
3. E. H. Lieb, *Integral bounds for radar ambiguity functions and Wigner distributions*, Journal of Mathematical Physics 31 (1990), 594–599, DOI:10.1063/1.528894. Abstract available; full text not inspected.
4. C. Wang, Y. Wang and S. Li, *Inverse synthetic aperture radar imaging of ship targets with complex motion based on match Fourier transform for cubic chirps model*, IET Radar, Sonar & Navigation 7 (2013), 994–1003, DOI:10.1049/iet-rsn.2013.0083. Full HTML text inspected, especially Sections 2, 3, and 5.
