# Sharp conditional fourth-power profile for spherical mixed Fourier extension

## Finding

Let \(\sigma\) be unnormalized surface measure on \(\mathbb S^2\). For \(f\in L^2(\mathbb S^2,d\sigma)\), define
\[
\widehat{f\sigma}(x)=\int_{\mathbb S^2}e^{-ix\cdot\omega}f(\omega)\,d\sigma(\omega),\qquad
\mathcal N(f)^4=\int_0^\infty\left(\int_{\mathbb S^2}|\widehat{f\sigma}(r\theta)|^2\,d\sigma(\theta)\right)^2 r^2\,dr.
\]
Write \(P_0f\) for the orthogonal projection of \(f\) onto constants, and for nonzero \(f\) set
\[
b(f)=\frac{\|f-P_0f\|_{L^2(\sigma)}^2}{\|f\|_{L^2(\sigma)}^2}\in[0,1].
\]
Then the **optimal bound at each prescribed nonconstant mass** \(b\) is
\[
\boxed{\displaystyle
\mathcal N(f)^4\le\frac{(2\pi)^6}{\pi}\left(1-\frac43 b(f)+\frac45 b(f)^2\right)\|f\|_{L^2(\sigma)}^4.}
\]
For every \(b\in[0,1]\), the bound is attained. Equality for nonzero \(f\) holds **if and only if** \(f=P_0f+P_1f\), where \(P_1\) projects onto spherical harmonics of degree one. Thus the entire sharp fixed-mass profile, not only the unrestricted constant or a local deficit, is determined. Equivalently, the exact sharp fourth-power deficit is
\[
\frac{(2\pi)^6}{\pi}\|f\|_2^4-\mathcal N(f)^4\ \ge\ \frac{(2\pi)^6}{\pi}\left(\frac43 b-\frac45 b^2\right)\|f\|_2^4,
\]
with equality characterized as above.

The key mixed Bessel-moment identity, valid for **every** integer \(k\ge0\), is
\[
\boxed{\displaystyle
\int_0^\infty J_{1/2}(r)^2J_{k+1/2}(r)^2\,dr=\frac{1}{\pi(2k+1)}.}
\]
The remaining extremal input is the strict decreasing order of the diagonal fourth moments, established by Xu (2026): \(\int_0^\infty J_{k+1/2}(r)^4\,dr\) strictly decreases with \(k\).

## Assumptions and scope

All functions may be complex-valued. The Fourier transform, surface measure and radial--angular norm are exactly those defined above, with no normalized angular probability measure. No smoothness assumption on \(f\) beyond \(L^2\) is required. The exponent is exactly four; the ambient space is exactly \(\mathbb R^3\). The zero function satisfies the homogeneous bound but does not have a defined \(b(f)\). The stated equality classification includes all constant-plus-first-harmonic mixtures with any complex amplitudes and orientations.

## Proof

**1. Modal reduction.** Let \(f_k=P_kf\), \(a_k=\|f_k\|_2^2\ge0\), and \(A=\sum_{k\ge0}a_k=\|f\|_2^2\). The Fourier--Bessel identity for spherical harmonics, with \(d=3\), is
\[
\widehat{f_k\sigma}(r\theta)=(2\pi)^{3/2}(-i)^k r^{-1/2}J_{k+1/2}(r)f_k(\theta).
\]
Angular orthogonality and Tonelli therefore give
\[
\mathcal N(f)^4=(2\pi)^6\sum_{k,l\ge0}a_ka_l M_{kl},\quad
M_{kl}=\int_0^\infty J_{k+1/2}(r)^2J_{l+1/2}(r)^2\,dr.
\]
All these moments are finite; the absolute convergence of the nonnegative series follows from \(M_{kl}\le\sqrt{M_{kk}M_{ll}}\) and the boundedness of the diagonal moment sequence. This also justifies the reduction for general \(L^2\) data via partial harmonic sums.

**2. Exact constant--mode cross moments.** Let \(j_k(r)=\sqrt{\pi/(2r)}J_{k+1/2}(r)\), with the value at zero understood continuously. Write \(L_k(t)=P_k^{\mathrm{Leg}}(t)\), the ordinary Legendre polynomial. Its standard Fourier representation is
\[
 j_k(r)=\frac{i^{-k}}{2}\int_{-1}^1e^{irt}L_k(t)\,dt.
\]
Legendre orthogonality and Plancherel imply
\[
\int_0^\infty j_k(r)^2\,dr=\frac{\pi}{2(2k+1)}.
\]
The product \(j_k(r)^2\) is the Fourier transform, up to a constant phase, of the compactly supported continuous convolution \((L_k\mathbf1_{[-1,1]})*(L_k\mathbf1_{[-1,1]})\). This convolution vanishes at its support endpoints \(\pm2\). Fourier inversion for the integrable function \(j_k^2\) consequently yields
\[
\int_0^\infty\cos(2r)j_k(r)^2\,dr=0.
\]
Since \(J_{1/2}(r)=\sqrt{2/(\pi r)}\sin r\), it follows that
\[
M_{0k}=\frac4{\pi^2}\int_0^\infty\sin^2r\,j_k(r)^2\,dr
=\frac2{\pi^2}\int_0^\infty j_k(r)^2\,dr
=\frac1{\pi(2k+1)}.
\]
In particular \(M_{00}=1/\pi\) and \(M_{01}=1/(3\pi)\). For all \(k\ge1\), \(M_{0k}\le M_{01}\), with equality only for \(k=1\).

**3. Exact first nonconstant diagonal moment.** For \(L_1(t)=t\), its self-convolution \(F_1=L_1\mathbf1_{[-1,1]}*L_1\mathbf1_{[-1,1]}\) is even and, for \(0\le x\le2\), is
\[
F_1(x)=\int_{x-1}^{1}t(x-t)\,dt=-\frac{x^3}{6}+x-\frac23,\qquad F_1'(x)=1-\frac{x^2}{2}.
\]
By differentiating the Fourier transform and applying Plancherel,
\[
M_{11}=\frac1{4\pi}\int_{-2}^{2}|F_1'(x)|^2\,dx
=\frac1{2\pi}\int_0^2\left(1-\frac{x^2}{2}\right)^2dx
=\frac7{15\pi}.
\]
This coefficient is exact, with no numerical quadrature.

**4. Full-spectrum comparison and extremizers.** Xu's strict modal-ordering theorem at \(d=3,q=4\) says \(M_{00}>M_{11}>M_{22}>\cdots\). Consequently, for \(k,l\ge1\), Cauchy--Schwarz yields
\[
M_{kl}\le\sqrt{M_{kk}M_{ll}}\le\frac7{15\pi},
\]
and the last inequality is strict whenever either index exceeds one. Put \(a_0=(1-b)A\) and \(\sum_{k\ge1}a_k=bA\). Splitting the quadratic sum into the constant block, the constant--nonconstant block and the nonconstant block gives
\[
\frac{\mathcal N(f)^4}{(2\pi)^6}
\le\frac{A^2}{\pi}\left[(1-b)^2+\frac23b(1-b)+\frac7{15}b^2\right]
=\frac{A^2}{\pi}\left(1-\frac43b+\frac45b^2\right).
\]
When \(a_k=0\) for all \(k\ge2\), all inequalities used above are equalities, giving an extremizer at every prescribed \(b\). Conversely, if any such \(a_k>0\), the corresponding positive diagonal contribution is strictly below the upper bound, hence equality is impossible. This proves both sharpness and the complete equality classification.

## Verification

The included standalone `CHECK.py` performs exact rational polynomial-convolution computations for Legendre modes and independently checks the two critical constants, the cross-moment identities, strict low-mode diagonal ordering, and finite-dimensional sharp inequalities. It does not replace Xu's analytical infinite-mode ordering theorem. The proof above verifies the normalization and all factors of \(2\pi\) without numerical integration. The supplied checker needs Python 3 and only its standard library.

## Relationship to prior work

Carneiro, Oliveira e Silva and Sousa (2017 preprint, 2019 journal) introduced the sharp radial--angular mixed Fourier extension problem and proved constant-mode optimality for admissible even exponents, including \(d=3,q=4\). Xu (first posted October 14, 2026) proved the complete strictly decreasing moment ordering and a sharp **linear-in-nonconstant-mass squared-norm** stability inequality. These are acknowledged premises. Neither inspected text gives the sharp fourth-power conditional curve for **every fixed** value of \(b\), nor the exact constant--all-mode cross-moment formula. In particular, squaring Xu's Minkowski-based squared-norm estimate gives a strictly larger bound at every \(0<b<1\), since \(1/3<\sqrt{7/15}\). The new exact profile captures the cross-mode interaction missing from that bound.

## Limitations

The claim addresses the radial--angular mixed norm, not the ordinary \(L^4(\mathbb R^3)\) extension norm. It is specific to dimension three and exponent four, and it relies on the recent global diagonal Bessel-moment ordering. No assertion about other dimensions or exponents is made. The novelty assessment is relative to inspected and indexed sources; an earlier unindexed equivalent fixed-mass inequality remains possible. Independent mathematical audit has not been performed.

## References

1. Z. Xu, *Sharp radial--angular mixed norm Fourier extension and global stability on spheres*, arXiv:2610.19648, first posted 2026-10-14, especially Theorems 1.2--1.3 and the Fourier--Bessel reduction. https://arxiv.org/abs/2610.19648
2. E. Carneiro, D. Oliveira e Silva, and M. Sousa, *Sharp mixed norm spherical restriction*, arXiv:1710.10365 (2017), *Advances in Mathematics* 341 (2019), 583--608. https://arxiv.org/abs/1710.10365
3. NIST Digital Library of Mathematical Functions, Chapter 10, spherical Bessel Fourier integrals, especially §10.59. https://dlmf.nist.gov/10.59
