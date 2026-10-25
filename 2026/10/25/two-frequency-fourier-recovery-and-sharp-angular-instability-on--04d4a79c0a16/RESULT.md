# Two-frequency Fourier recovery and sharp angular instability on a pair of concentric spheres

## Finding

Let \(d\ge2\), \(0<a<b\), and \(\nu=d/2-1\). On the unit sphere \(S^{d-1}\), let \(\sigma\) be normalized surface measure. For \(f_a,f_b\in L^1(S^{d-1},\sigma)\), define the finite signed/complex measure
\[
\mu=(\theta\mapsto a\theta)_*(f_a\sigma)+(\theta\mapsto b\theta)_*(f_b\sigma)
\]
and its Fourier transform \(\widehat\mu(\xi)=\int e^{-i\xi\cdot x}\,d\mu(x)\). Let \(j_{\nu,1}\) be the first positive zero of \(J_\nu\). If
\[
0<u<v<j_{\nu,1}/b,
\]
then the two complete angular traces \(\widehat\mu(u\omega)\) and \(\widehat\mu(v\omega)\), \(\omega\in S^{d-1}\), determine both densities uniquely. A single frequency sphere never determines two arbitrary densities on the source spheres.

There is also an exact sharp high-angular-degree instability. In a degree-\(\ell\) spherical-harmonic channel, ignore the harmless unit-modulus factor \((-i)^\ell\) and write its real measurement matrix as
\[
M_\ell=\begin{pmatrix}
\phi_\ell(au)&\phi_\ell(bu)\\
\phi_\ell(av)&\phi_\ell(bv)
\end{pmatrix},\qquad
\phi_\ell(z)=2^\nu\Gamma(\nu+1)z^{-\nu}J_{\ell+\nu}(z).
\]
For every \(\ell\ge0\), \(\det M_\ell<0\). Define \(\kappa_\ell=\Gamma(\nu+1)/(2^\ell\Gamma(\ell+\nu+1))\) and \(\Delta=(b^2-a^2)(v^2-u^2)>0\). As \(\ell\to\infty\), its singular values satisfy
\[
\sigma_{\max}(M_\ell)=\kappa_\ell(bv)^\ell(1+O(\ell^{-1})),
\qquad
\sigma_{\min}(M_\ell)=\kappa_\ell(au)^\ell\frac{\Delta}{4(\ell+\nu+1)}(1+O(\ell^{-1})).
\]
In particular,
\[
\frac{\sigma_{\max}(M_\ell)}{\sigma_{\min}(M_\ell)}
=\frac{4(\ell+\nu+1)}{\Delta}
\left(\frac{bv}{au}\right)^\ell(1+O(\ell^{-1})).
\]
Thus two arbitrarily low but distinct frequency spheres give exact uniqueness while the inverse on unrestricted \(L^2\) densities is unbounded, with an explicit sharp factorial/angular conditioning law.

## Assumptions and scope

The source consists of exactly two concentric spheres of radii \(a,b\) with independently variable absolutely continuous angular densities; all spheres have the same known center. Data comprise the full complex Fourier transform restricted to two centered observation spheres, not intensities or finitely many sampling directions. Frequency normalization uses \(e^{-i\xi\cdot x}\), not the \(2\pi\)-frequency convention. The operator singular values use orthonormal spherical-harmonic coordinates with respect to the probability measure \(\sigma\) on each of the two source and observation spheres. The Fourier field may be complex. No uniform bounded inverse is claimed.

## Proof

**1. Harmonic reduction.** Let \(Y_{\ell,k}\) be an orthonormal basis of degree-\(\ell\) spherical harmonics in \(L^2(S^{d-1},\sigma)\). The Funk–Hecke/plane-wave identity gives, for every \(z>0\),
\[
\int_{S^{d-1}}e^{-iz\omega\cdot\theta}Y_{\ell,k}(\theta)\,d\sigma(\theta)
=(-i)^\ell\phi_\ell(z)Y_{\ell,k}(\omega).
\]
The formula extends to the harmonic coefficients of \(L^1\) densities by Fubini. Consequently, each degree/azimuthal channel of the pair of measured traces equals \((-i)^\ell M_\ell\) times the two source coefficients. There is no mixing between channels. The constant in \(\phi_\ell\) follows from normalized surface measure and yields \(\phi_0(0)=1\).

**2. Strict two-radius nonsingularity.** Put \(\alpha=\ell+\nu\ge0\). The standard Bessel product is
\[
J_\alpha(z)=\frac{(z/2)^\alpha}{\Gamma(\alpha+1)}
\prod_{m=1}^{\infty}\left(1-\frac{z^2}{j_{\alpha,m}^2}\right).
\]
The Bessel first-zero monotonicity gives \(j_{\alpha,1}\ge j_{\nu,1}\). In the stated frequency interval every \(\phi_\ell(rt)\), for \(r\in\{a,b\}\), is strictly positive. For \(R(t)=\phi_\ell(at)/\phi_\ell(bt)\), logarithmic differentiation of the locally uniformly convergent product gives
\[
\frac{d}{dt}\log R(t)
=2t\sum_{m\ge1}\left(
\frac{b^2}{j_{\alpha,m}^2-b^2t^2}
-\frac{a^2}{j_{\alpha,m}^2-a^2t^2}
\right)>0.
\]
Indeed each summand is strictly positive for \(0<t<j_{\alpha,1}/b\). Hence
\[
\det M_\ell=\phi_\ell(bu)\phi_\ell(bv)[R(u)-R(v)]<0.
\]
Every harmonic coefficient pair is recovered by a nonsingular matrix. Vanishing of every harmonic coefficient of an \(L^1\) function implies its vanishing almost everywhere, since spherical harmonics span a dense subspace of continuous functions on the sphere. This establishes uniqueness. With one measured frequency sphere each harmonic channel has a single linear equation in two unknown coefficients, so even a single nonzero spherical-harmonic pair can lie in its nullspace. This proves minimality of two complete observation spheres.

**3. Large-degree determinant.** For each fixed positive \(z\), the absolutely convergent Bessel series yields
\[
\phi_\ell(z)=\kappa_\ell z^\ell
\left[1-\frac{z^2}{4(\ell+\nu+1)}+O(\ell^{-2})\right]
\]
with errors uniform over the four fixed arguments \(au,bu,av,bv\). Multiplication in the determinant cancels the leading products because \((au)(bv)=(av)(bu)\), leaving
\[
\det M_\ell
=-\kappa_\ell^2(abuv)^\ell
\frac{\Delta}{4(\ell+\nu+1)}
(1+O(\ell^{-1})).
\]
The positive constant \(\Delta\) comes from
\[
(au)^2+(bv)^2-(av)^2-(bu)^2=(b^2-a^2)(v^2-u^2).
\]
Because \(b>a\) and \(v>u\), the bottom-right entry dominates all other entries exponentially as \(\ell\to\infty\). Thus \(\sigma_{\max}(M_\ell)=\kappa_\ell(bv)^\ell(1+O(\ell^{-1}))\). The product of the two singular values is \(|\det M_\ell|\), giving the displayed sharp expression for \(\sigma_{\min}\) and the condition number. Since \(\kappa_\ell(au)^\ell\to0\) faster than any inverse power, no bounded inverse exists on the full angular \(L^2\) direct sum.

## Verification

A standalone high-precision checker (`checker.py`) numerically confirms the strict determinant sign in dimensions \(2,3,5\), the predicted determinant and two singular-value leading constants at increasing degrees, and the normalized degree-channel plane-wave integral in dimension \(3\). The output is saved as `checker_output.txt`; run with `python checker.py` after installing the single dependency in `requirements.txt`. These finite checks verify normalization and critical constants but do not replace the all-degree Bessel-product argument. Direct asymptotic errors are evaluated relative to the stated leading terms, without using floating-point rank decisions for the proof.

## Relationship to prior work

González Vieli, *A uniqueness result for the Fourier transform of measures on the sphere* (first public online 8 December 2011), proves the precise one-source-sphere/one-observation-sphere Bessel nonvanishing criterion in all dimensions. Its Proposition 1.2 and spherical-harmonic identity have been inspected in the complete five-page article. It does not provide the two-independent-source/two-measurement determinant sign or the sharp singular-value asymptotics here. Chattopadhyay, Ghosh, Giri and Srivastava (2020), Theorem 13, classify two-or-more observation spheres for a *single* source sphere; its full text was inspected and it does not treat two independent source-shell densities or two-by-two high-degree singular values. Lev (2011) and Sjölin (2011) cover Heisenberg uniqueness for the planar unit circle with other measurement sets; only bibliographic descriptions/abstracts of these papers were accessible for comparison, so older equivalent formulations remain a priority risk. Classical Bessel zeros and product identities are recorded in NIST DLMF §10.21; their use is explicitly credited, not treated as new.

## Limitations

The frequency inequality is an explicit sufficient recovery region, not a claimed necessary-and-sufficient condition for all observation radii. Unknown centers, more than two source shells, finite-direction samples, intensity-only data, and statistical/noise-optimal reconstruction lie outside the result. No lower stability bound uniform over all harmonic degrees is possible for these data; the singular-value formula quantifies this ill-conditioning. A broader inverse-source theorem not retrieved in the searched literature might imply part or all of the result. This is a self-review, not independent validation.

## References

1. F. J. González Vieli, “A uniqueness result for the Fourier transform of measures on the sphere,” *Bulletin of the Australian Mathematical Society* **86** (2012), 78–82, DOI 10.1017/S0004972711002942, first published online 8 December 2011; full PDF: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C23F3970E0BD3264095D749D97FC7C3D/S0004972711002942a.pdf/uniqueness_result_for_the_fourier_transform_of_measures_on_the_sphere.pdf.
2. NIST Digital Library of Mathematical Functions, §10.21(i), (iii), (iv), Bessel-zero interlacing, infinite product, and monotonicity: https://dlmf.nist.gov/10.21.
3. N. Lev, “Uniqueness theorems for Fourier transforms,” *Bulletin des Sciences Mathématiques* **135** (2011), 134–140, DOI 10.1016/j.bulsci.2010.12.002 (bibliographic/abstract access only).
4. A. Chattopadhyay, S. Ghosh, D. K. Giri and R. K. Srivastava, “Heisenberg uniqueness pairs on the Euclidean spaces and the motion group,” *Comptes Rendus Mathématique* **358** (2020), 365–377, DOI 10.5802/crmath.48, full PDF: https://www.numdam.org/item/10.5802/crmath.48.pdf.
5. P. Sjölin, “Heisenberg uniqueness pairs and a theorem of Beurling and Malliavin,” *Bulletin des Sciences Mathématiques* **135** (2011), 125–133, DOI 10.1016/j.bulsci.2010.12.004 (bibliographic/abstract access only).
