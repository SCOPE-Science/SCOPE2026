# Critical fourth-moment Bessel staircase and the square-root Fourier modal gap

## Finding

Let \(J_\nu\) be the real Bessel function of the first kind, and for each integer \(k\geq0\) define the truncated critical circle moment
\[
E_k(R)=\int_0^R rJ_k(r)^4\,dr,\qquad R>0.
\]
For every integer \(0\leq k<\ell\) and every \(R>0\), the **exact finite-aperture identity** is
\[
E_k(R)-E_\ell(R)
=\frac{R^2}{2}\sum_{j=k}^{\ell-1}
\frac{\bigl(J_j(R)^2+J_{j+1}(R)^2\bigr)^2}{2j+1}>0.
\tag{1}
\]
Although every \(E_j(R)\) diverges logarithmically as \(R\to\infty\), its pairwise differences converge to an explicit strictly ordered staircase:
\[
\lim_{R\to\infty}\bigl(E_k(R)-E_\ell(R)\bigr)
=\frac{2}{\pi^2}\sum_{j=k}^{\ell-1}\frac1{2j+1}.
\tag{2}
\]
For \(q>4\), set
\[
I_k(q)=\int_0^\infty |J_k(r)|^q r\,dr,
\qquad \lambda_k(q)=I_k(q)^{2/q}.
\]
For each fixed \(k\geq1\), as \(q\downarrow4\),
\[
I_0(q)-I_k(q)\longrightarrow\frac{2}{\pi^2}\sum_{j=0}^{k-1}\frac1{2j+1},
\qquad
\lambda_0(q)-\lambda_k(q)
\sim\frac{1}{\pi\sqrt3}\left(\sum_{j=0}^{k-1}\frac1{2j+1}\right)\sqrt{q-4}.
\tag{3}
\]
Under the standard unnormalized surface-measure convention for the Fourier extension operator on the unit circle, the corresponding **exact fixed-mode asymptotic** is
\[
\lim_{q\downarrow4}
\frac{C_{2,q}^2\|Y_k\|_2^2
-\|\widehat{Y_k\sigma}\|_{L^q_{\mathrm{rad}}L^2_{\mathrm{ang}}}^2}{\sqrt{q-4}\,\|Y_k\|_2^2}
=\frac{4\pi}{\sqrt3}\sum_{j=0}^{k-1}\frac1{2j+1},
\tag{4}
\]
for every nonzero pure degree-\(k\) circle harmonic \(Y_k\). Here \(C_{2,q}=(2\pi)I_0(q)^{1/q}\) is the sharp extension norm for \(q>4\), established by Xu (2026). The claim concerns fixed modes, **not** an identification of the maximizing nonzero mode or the globally optimal stability constant at finite \(q\).

## Assumptions and scope

The parameter \(R\) is any positive finite real number; \(k,\ell\) are integers with \(0\leq k<\ell\), while \(q>4\) approaches \(4\) from above with \(k\) fixed. The Fourier transform is \(\widehat{f\sigma}(x)=\int_{\mathbb S^1}e^{-ix\cdot\omega}f(\omega)\,d\sigma(\omega)\), where \(\sigma\) denotes **unnormalized** arc-length measure. The radial–angular norm is
\[
\|F\|_{L^q_{\mathrm{rad}}L^2_{\mathrm{ang}}}
=\left(\int_0^\infty\left(\int_{\mathbb S^1}|F(r\theta)|^2\,d\sigma(\theta)\right)^{q/2}r\,dr\right)^{1/q}.
\]
The strict ordering in (1) is a cutoff-at-the-origin statement, and (3)–(4) are **fixed-degree** limits; no assertion is made uniform in growing degrees.

## Proof

**Exact cutoff identity.** More generally, for real \(\nu>-1/2\), let \(a(r)=J_\nu(r)\), \(b(r)=J_{\nu+1}(r)\), and \(S(r)=a(r)^2+b(r)^2\). The two Bessel derivative recurrences give
\[
a'(r)=\frac{\nu}{r}a(r)-b(r),\quad
b'(r)=a(r)-\frac{\nu+1}{r}b(r),\quad
S'(r)=\frac{2\nu}{r}a(r)^2-\frac{2(\nu+1)}r b(r)^2.
\]
Differentiation therefore yields the **pointwise algebraic identity**
\[
\frac{d}{dr}\bigl(r^2S(r)^2\bigr)
=2r(2\nu+1)\bigl(a(r)^4-b(r)^4\bigr).
\tag{5}
\]
Since \(J_\nu(r)=O_\nu(r^\nu)\) as \(r\downarrow0\), the lower boundary term \(r^2S(r)^2\) vanishes for \(\nu>-1/2\). Integrating (5) proves (1) after telescoping over \(\nu=j\). Each summand is strictly positive: consecutive Bessel functions cannot have a common positive zero, for otherwise the first-order recurrence forces both \(J_j\) and its derivative to vanish, contradicting uniqueness for the Bessel equation. In fact (5) proves the individual positive identity for every real \(\nu>-1/2\).

**Renormalized limit.** The fixed-order Hankel expansion shows
\[
J_j(R)=\sqrt{\frac2{\pi R}}\left(\cos\bigl(R-\tfrac{j\pi}2-\tfrac\pi4\bigr)+O_j(R^{-1})\right),
\]
with the complementary sine phase for \(J_{j+1}\). Thus \(J_j(R)^2+J_{j+1}(R)^2=2/(\pi R)+O_j(R^{-2})\). Each summand on the right of (1) converges to \(2/[\pi^2(2j+1)]\), proving (2). The individual integrals diverge because the average of the fourth power of a sinusoid is \(3/8\), giving \(E_j(R)=(3/(2\pi^2))\log R+O_j(1)\).

**Passage to the critical exponent.** For each fixed integer \(j\) and \(4<q\leq5\), the Hankel expansion uniformly gives, for large \(r\),
\[
r|J_j(r)|^q=\left(\frac2\pi\right)^{q/2}r^{-1-(q-4)/2}
\left[|\cos(r-\tfrac{j\pi}2-\tfrac\pi4)|^q+O_j(r^{-1})\right].
\tag{6}
\]
Write \(m(q)=\pi^{-1}\int_0^\pi|\cos t|^q\,dt\). The periodic part minus its mean has a bounded periodic primitive, uniformly for \(q\in[4,5]\). Integration by parts against \(r^{-1-(q-4)/2}\) shows that its tail beyond \(R\) is \(O_j(R^{-1})\) **uniformly** over \(q\in[4,5]\). The remainder in (6) has the same uniform tail bound. Consequently
\[
I_j(q)=\frac{2(2/\pi)^{q/2}m(q)}{q-4}+O_j(1),\quad
(q-4)I_j(q)\longrightarrow\frac3{\pi^2},
\tag{7}
\]
because \(m(4)=3/8\). For any two fixed consecutive orders, the two periodic leading terms in (6) differ by a half-period phase and hence have **equal means**; their difference has uniformly bounded periodic primitive. Its integral over \([R,\infty)\) is uniformly \(O_j(R^{-1})\), and compact-interval convergence implies
\[
\lim_{q\downarrow4}(I_j(q)-I_{j+1}(q))
=\int_0^\infty r\bigl(J_j(r)^4-J_{j+1}(r)^4\bigr)\,dr
=\frac2{\pi^2(2j+1)}.
\tag{8}
\]
Telescoping gives the first part of (3). By the mean value theorem for \(x\mapsto x^{2/q}\), using the common asymptotic (7),
\[
\lambda_0(q)-\lambda_k(q)
=\left(\frac2q\right)\xi_q^{2/q-1}(I_0(q)-I_k(q)),
\quad \xi_q\sim\frac3{\pi^2(q-4)}.
\]
It follows that the coefficient of \(\sqrt{q-4}\) equals \(\bigl(2/\pi^2\bigr)/(2\sqrt{3/\pi^2})=1/(\pi\sqrt3)\), times the odd reciprocal sum, proving (3).

**Fourier normalization.** The Fourier–Bessel formula for a degree-\(k\) harmonic on \(\mathbb S^1\) is \(\widehat{Y_k\sigma}(r\theta)=2\pi(-i)^kJ_k(r)Y_k(\theta)\). Hence its squared mixed norm is \((2\pi)^2I_k(q)^{2/q}\|Y_k\|_2^2\). The sharp degree-zero operator norm \(C_{2,q}=2\pi I_0(q)^{1/q}\) is a cited result, not newly proven here. Substitution in (3) gives (4).

## Verification

The standalone \(verify_bessel.py\) checks the algebraic derivative formula symbolically, numerical finite-radius identities for multiple degrees and radii, and the predicted approach of the normalized gaps to their explicit constants using a mean-tail-subtracted Bessel quadrature. These computations support, but are not substituted for, the infinite-domain proof above. Equations (5)–(8), including the uniform tail argument, supply the logical verification for all stated quantifiers.

## Relationship to prior work

Carneiro–Oliveira e Silva–Sousa (2018/2019) introduced the harmonic-mode reduction for sharp mixed-norm spherical Fourier extension and obtained mode-zero extremality in several ranges. Xu (first publicly posted October 14, 2026) proved mode-zero dominance for every finite admissible exponent and sharp stability; in dimension two the paper explicitly excludes the divergent endpoint \(q=4\) and leaves the identity of the best nonzero mode for arbitrary finite \(q>4\) undetermined. The results here concern the hitherto unresolved **exact finite-aperture critical hierarchy**, its nontrivial finite-part values, and fixed-mode singular spectral-gap asymptotics. Ciccone–Sousa (2025) concerns extremal exponent ranges rather than these endpoint coefficients. All Fourier–Bessel identities and classical Bessel asymptotics are attributed to existing special-function theory.

## Limitations

No complete ordering for all untruncated \(I_k(q)\) at arbitrary \(q>4\) is claimed; neither the maximizing nonconstant harmonic degree nor the globally optimal stability coefficient is identified in dimension two. The limit \(q\downarrow4\) is fixed-mode, not uniform when \(k\) grows. The exact cutoff identity follows from classical recurrence relations and could be implicit in older special-function tables, so historical priority for that particular identity is not settled. No independent review has been performed.

## References

1. Zewei Xu, *Sharp radial–angular mixed norm Fourier extension and global stability on spheres*, arXiv:2610.19648, first posted October 14, 2026. https://arxiv.org/abs/2610.19648
2. Emanuel Carneiro, Diogo Oliveira e Silva, Mateus Sousa, *Sharp mixed norm spherical restriction*, arXiv:1710.10365, *Advances in Mathematics* 341 (2019), 583–608. https://arxiv.org/abs/1710.10365
3. Valentina Ciccone, Mateus Sousa, *Global and local maximizers for some Fourier extension estimates on the sphere*, *Journal of Fourier Analysis and Applications* 31 (2025), article 70. https://doi.org/10.1007/s00041-025-10201-7
4. NIST Digital Library of Mathematical Functions, Chapter 10, *Bessel Functions*, particularly derivative recurrences and large-argument expansions. https://dlmf.nist.gov/10
