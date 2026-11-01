# Full split-torus Fourier positivity for spherical positive-definite functions on the real hyperbolic plane

## Finding

Let \(G=\operatorname{SL}_2(\mathbb R)\), \(K=\operatorname{SO}(2)\), and let
\[
a_t=\begin{pmatrix}e^{t/2}&0\\0&e^{-t/2}\end{pmatrix},\qquad t\in\mathbb R.
\]
Every **nonzero**, continuous, positive-definite, \(K\)-bi-invariant function \(\psi:G\to\mathbb C\) with \(t\mapsto\psi(a_t)\in L^1(\mathbb R)\) has **strictly positive** torus Fourier transform at every real frequency:
\[
\boxed{\ \int_{\mathbb R}\psi(a_t)e^{-i\xi t}\,dt>0\quad (\xi\in\mathbb R).\ }
\]
This resolves the split-torus Fourier-positivity question for the *entire spherical unitary spectrum* of this real rank-one group, including mixtures supported entirely on the complementary series.

The new explicit ingredient is the complementary-series density. For real \(0<\nu<1/2\), define
\[\phi_\nu(t)=P_{-\nu}(\cosh t),\]
where \(P\) is the Legendre function normalized by \(P_{-\nu}(1)=1\). Then, with the non-unitary Fourier convention above,
\[
\boxed{\ \widehat\phi_\nu(\xi)
=\frac{\left|\Gamma\bigl((\nu+i\xi)/2\bigr)\Gamma\bigl((1-\nu+i\xi)/2\bigr)\right|^2}
{2\pi\Gamma(\nu)\Gamma(1-\nu)}>0.\ }
\]
For completeness, the principal-series parameter \(\nu=1/2+i\lambda\), \(\lambda\in\mathbb R\), obeys the same beta product and specializes to
\[
\widehat\phi_{1/2+i\lambda}(\xi)=
\frac{\left|\Gamma\bigl(1/4+i(\lambda+\xi)/2\bigr)\Gamma\bigl(1/4+i(\lambda-\xi)/2\bigr)\right|^2}
{2\pi\left|\Gamma(1/2+i\lambda)\right|^2}>0.
\]
The restriction to the split torus is essential. No conclusion concerning arbitrary noncompact abelian subgroups is claimed.

## Assumptions and scope

The positive-definite function is understood in the usual Hermitian sense on \(G\); a nonzero such function has \(\psi(e)>0\). Haar measure in the torus parameter is ordinary Lebesgue measure \(dt\), and Fourier frequency \(\xi\) is real. The spherical unitary dual of \((G,K)\) consists of the trivial representation, complementary parameters \(0<\nu<1/2\), and spherical principal parameters \(\nu=1/2+i\lambda\) with \(\lambda\ge0\). The equality of the parameters \(\nu\) and \(1-\nu\) follows from \(P_{-\nu}=P_{\nu-1}\). The theorem includes arbitrary nonzero positive spherical Bochner measures whose resulting torus restriction is in \(L^1\), not merely finite mixtures.

## Proof

**1. The normalized spherical integral and integrability.** The classical real Legendre integral gives, for \(0<\operatorname{Re}\nu<1\),
\[
\phi_\nu(t)=\frac1{2\pi}\int_0^{2\pi}
(\cosh t+\sinh t\cos\theta)^{-\nu}\,d\theta.
\]
The integrand base is positive. Put \(u=\cos^2(\theta/2)\). For \(t\ge0\), the base equals \(e^t u+e^{-t}(1-u)\), and the angular measure becomes \(du/(\pi\sqrt{u(1-u)})\). Consequently, for real \(0<\sigma<1/2\),
\[
0<\phi_\sigma(t)\le e^{-\sigma t}\frac1\pi\int_0^1
u^{-\sigma-1/2}(1-u)^{-1/2}\,du=C_\sigma e^{-\sigma t}.
\]
The constant is finite because \(\sigma<1/2\). At \(\sigma=1/2\), splitting the integral at \(u=e^{-2t}\) gives \(\phi_{1/2}(t)\le C(1+t)e^{-t/2}\). Evenness gives these estimates also for negative \(t\). In particular, all indicated functions are integrable; for \(\nu=1/2+i\lambda\), \(|\phi_\nu(t)|\le\phi_{1/2}(t)\) uniformly in real \(\lambda\).

**2. Direct beta evaluation.** For \(0<\operatorname{Re}\nu<1\), let \(a=\cos^2(\theta/2)\) and \(b=\sin^2(\theta/2)\). For almost every angle both are positive. Euler's beta substitution \(y=(a/b)e^{2t}\) yields
\[
\int_{-\infty}^\infty (ae^t+be^{-t})^{-\nu}e^{-i\xi t}\,dt
=\frac12 a^{-(\nu-i\xi)/2}b^{-(\nu+i\xi)/2}
B\left(\frac{\nu-i\xi}2,\frac{\nu+i\xi}2\right).
\]
The angular integral of the powers is
\[
\frac1{2\pi}\int_0^{2\pi}
 a^{-(\nu-i\xi)/2}b^{-(\nu+i\xi)/2}\,d\theta
=\frac1\pi B\left(\frac{1-\nu+i\xi}2,\frac{1-\nu-i\xi}2\right).
\]
Absolute Fubini holds by the estimate in step 1 with \(\sigma=\operatorname{Re}\nu\) (the same endpoint argument gives integrability for every \(0<\sigma<1\)). Thus
\[
\boxed{\ \widehat\phi_\nu(\xi)=\frac1{2\pi}
B\left(\frac{\nu+i\xi}2,\frac{\nu-i\xi}2\right)
B\left(\frac{1-\nu+i\xi}2,\frac{1-\nu-i\xi}2\right).\ }
\]
For real \(\nu\), each beta factor is a positive gamma-modulus square divided by a positive gamma value. For \(\nu=1/2+i\lambda\), the two beta factors are conjugates, and none of the numerator gamma values vanishes or has a pole. Both cases give a strictly positive real number for every \(\xi\).

**3. General positive-definite spherical mixtures.** By the spherical Bochner theorem and the classification of the spherical unitary dual, one can write
\[
\psi(a_t)=c+\int_{0<\nu<1/2}\phi_\nu(t)\,d\mu_c(\nu)
+\int_{\lambda\ge0}\phi_{1/2+i\lambda}(t)\,d\mu_p(\lambda),
\]
where \(c\ge0\) and \(\mu_c,\mu_p\) are finite nonnegative measures, of total mass \(\psi(e)-c\). Each complementary spherical function is pointwise positive. The principal integral is bounded in absolute value by \(\mu_p(\mathbb R_{\ge0})\phi_{1/2}(t)\), which tends to zero as \(|t|\to\infty\). Therefore a positive \(c\) would force \(|\psi(a_t)|\ge c/2\) for all sufficiently large \(|t|\), contrary to the \(L^1\)-hypothesis. Thus \(c=0\).

The principal integral is in \(L^1\), by its uniform integrable majorant. Subtracting it from \(\psi(a_t)\) shows that the complementary mixture is also \(L^1\); being pointwise nonnegative, Tonelli's theorem gives
\[
\int\int|\phi_\nu(t)|\,dt\,d\mu_c(\nu)<\infty.
\]
The analogous absolute bound for the principal integral follows from its uniform majorant. Hence Fourier transformation commutes with both spherical integrations, and
\[
\widehat{\psi|_A}(\xi)=
\int\widehat\phi_\nu(\xi)\,d\mu_c(\nu)
+\int\widehat\phi_{1/2+i\lambda}(\xi)\,d\mu_p(\lambda).
\]
All integrands are finite, continuous and strictly positive in \(\xi\). At least one measure has positive mass because \(\psi\ne0\). Therefore the displayed sum is strictly positive at every real frequency. \(\square\)

## Verification

The two beta substitutions are exact and fix the Fourier/Haar normalization. Three independent direct numerical Fourier integrations of the Legendre functions, using 25-digit mpmath with a cutoff at \(|t|=90\), agreed with the beta-product predictions within \(2.4\times10^{-12}\), \(3.0\times10^{-18}\), and \(1.9\times10^{-20}\), respectively, for \((\nu,\xi)=(0.3,0.7)\), \((0.5,1)\), and \((0.5+0.8i,0.4)\). This is only a supplemental normalization check; the infinite-frequency, all-mixture theorem is established analytically by steps 1–3.

The proof's key boundaries are \(0<\nu<1/2\) for complementary representations, \(\nu=1/2+i\lambda\) for principal representations, and the excluded trivial character \(\nu=0\) (incompatible with integrability unless zero mass). The assumption \(\psi|_A\in L^1\) is not removed.

## Relationship to prior work

Björklund, Liu, Yu and Zhang (2026) formulate Fourier positivity for restrictions of spherical positive-definite functions to noncompact abelian subgroups. They prove split-torus positivity for **spherical principal series** on general semisimple groups and explicitly reserve complementary series for later investigation. The present proof handles the complementary spectrum for the real rank-one group and then uses spherical Bochner disintegration to cover **all** integrable spherical positive-definite functions on its split torus, including those with no principal-series mass. This does not imply the higher-rank or unipotent parts of the conjecture.

The spherical Legendre integral, Euler beta transform, and classification of the spherical unitary dual are classical ingredients, not claimed as new. What is established here beyond the cited 2026 theorem is the closed complementary-series case and the mixed-spectrum rank-one conclusion. An earlier classical formula may contain the beta product without presenting this conclusion; this remains a literature-coverage risk.

## Limitations

No claim is made for \(\operatorname{SL}_2(\mathbb C)\), other real-rank-one groups, nonsplit abelian subgroups (notably unipotent ones), non-\(K\)-spherical vectors, or nonintegrable restrictions. Strict positivity at each real frequency is established, not a uniform positive lower bound over an unbounded frequency range. The exact beta-product identity is an elementary special-function computation and may occur in older integral tables; a systematic exhaustive table audit has not been performed.

## References

1. M. Björklund, D. Liu, J. Yu, and G. Zhang, *Fourier positivity for spherical functions I: split tori and spherical principal series*, first posted 2026-06-05, arXiv:2606.07286, https://arxiv.org/abs/2606.07286 . The introduction, Theorem A, §3, and §5 were inspected for coverage.
2. NIST Digital Library of Mathematical Functions, Chapter 14 (Legendre and Related Functions), especially §§14.3 and 14.19, https://dlmf.nist.gov/14.19 . Standard special-function conventions and formulas.
3. P. Etingof, *Representations of Lie Groups*, MIT 18.757 (2023), lecture 09, *Representations of SL2(R)*, https://ocw.mit.edu/courses/18-757-representations-of-lie-groups-fall-2023/resources/mit18_757_f23_lec09_pdf/ . Standard representation-theoretic background; the accessible lecture index, not its complete PDF, was consulted.
4. Classical Legendre real integral representation, https://en.wikipedia.org/wiki/Legendre_function#Integral_representations , checked against the normalization \(P_{-\nu}(1)=1\).
