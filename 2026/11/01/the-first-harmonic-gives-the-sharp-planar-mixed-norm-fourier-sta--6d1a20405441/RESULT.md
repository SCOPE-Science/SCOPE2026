# The first harmonic gives the sharp planar mixed-norm Fourier stability gap for every exponent \(q\ge27\)

## Finding

For any real \(q\ge27\), let \(J_k\) denote the Bessel function of the first kind of nonnegative integer order \(k\), and put
\[
I_k(q)=\int_0^\infty |J_k(r)|^q r\,dr.
\]
Then the strict *first-nonconstant-mode ordering*
\[
I_1(q)>I_k(q)\qquad(k=2,3,\ldots)
\]
holds uniformly throughout that real half-line. In particular the optimal planar mixed-norm Fourier-extension stability coefficient is
\[
\Gamma_{2,q}=4\pi^2\bigl(I_0(q)^{2/q}-I_1(q)^{2/q}\bigr),\qquad q\ge27.
\]
The equality cases are zero, the constant functions, and the nonzero first spherical harmonics. The number \(27\) is an explicit sufficient bound, **not** a claimed optimal transition point.

## Assumptions and scope

Take unnormalized arclength \(d\sigma\) on \(\mathbb S^1\). For \(f\in L^2(\mathbb S^1,d\sigma)\), set
\[
\widehat{f\sigma}(x)=\int_{\mathbb S^1}e^{-ix\cdot\omega}f(\omega)\,d\sigma(\omega),\quad
\|F\|_{L^q_{\mathrm{rad}}L^2_{\mathrm{ang}}}=
\left(\int_0^\infty\left(\int_{\mathbb S^1}|F(r\theta)|^2d\sigma(\theta)\right)^{q/2}r\,dr\right)^{1/q}.
\]
Let \(P_0\) be orthogonal projection onto constants and \(C_{2,q}\) the sharp extension norm. The coefficient \(\Gamma_{2,q}\) is the largest number such that
\[
C_{2,q}^{2}\|f\|_2^2-\|\widehat{f\sigma}\|_{L^q_{\mathrm{rad}}L^2_{\mathrm{ang}}}^2
\ge\Gamma_{2,q}\|f-P_0f\|_2^2
\]
for every \(f\in L^2(\mathbb S^1,d\sigma)\). The underlying spectral stability theorem is due to Xu; the new assertion here determines its first nonconstant maximizing mode for the specified real half-line.

## Proof

**1. Uniform strict amplitude bound beyond degree one.** We prove
\[
\sup_{r\ge0}|J_k(r)|<\tfrac12\qquad(k\ge2).
\]
For \(k\ge3\), Landau's bound \(|J_k(r)|<(7/10)k^{-1/3}\) suffices because \(7/(10\sqrt[3]{3})<1/2\).

For \(k=2\), consider \(x=r^2\) and the polynomial
\[
U(x)=\frac{x}{8}-\frac{x^2}{96}+\frac{x^3}{3072}-\frac{x^4}{184320}+\frac{x^5}{17694720}.
\]
The alternating Bessel series gives \(J_2(r)\le U(r^2)\) for \(0\le r\le4\). To certify \(U(x)<1/2\) on \([0,16]\), put \(t=x/16\) and express \(1/2-U(16t)\) in the Bernstein basis of degree \(20\). Its power coefficients are
\[
(a_0,a_1,a_2,a_3,a_4,a_5)=(1/2,-2,8/3,-4/3,16/45,-8/135),
\]
its Bernstein coefficients are
\[
b_j=\sum_{\ell=0}^{\min(5,j)}a_\ell
\frac{\binom{j}{\ell}}{\binom{20}{\ell}},\quad 0\le j\le20,
\]
and exact rational arithmetic gives \(\min_{0\le j\le20} b_j=61/43605>0\), at \(j=11\). Because the Bernstein basis is nonnegative and sums to one, this proves \(J_2(r)<1/2\) for \(0\le r\le4\). The alternating series also gives the lower bound
\[
J_2(r)\ge\frac{x}{8}\left(1-\frac{x}{12}+\frac{x^2}{384}-\frac{x^3}{23040}\right)\ge0,\qquad0\le x\le16,
\]
since the polynomial in parentheses is decreasing and equals \(7/45\) at \(x=16\). Thus the absolute-value bound is valid on this interval. For \(r\ge4\), the classical Watson/Nicholson bound \(|J_2(r)|^2\le2/(\pi\sqrt{r^2-4})\le1/(\pi\sqrt3)<1/4\) completes the proof.

**2. A uniform sixth-moment ceiling.** For all \(k\ge2\), split the radial integral at \(2k\). Landau's order bound and the same Watson/Nicholson inequality yield
\[
\begin{aligned}
I_k(6)&\le\int_0^{2k}\Bigl(\frac7{10}k^{-1/3}\Bigr)^6r\,dr
+\int_{2k}^\infty\left(\frac{2}{\pi\sqrt{r^2-k^2}}\right)^3r\,dr\\
&=2\left(\frac7{10}\right)^6+\frac8{\pi^3\sqrt3\,k}
\le2\left(\frac7{10}\right)^6+\frac4{\pi^3\sqrt3}<\frac13.
\end{aligned}
\]
The last strict comparison follows, for example, from \(\pi>3\), \(\sqrt3>5/3\) and \(2(7/10)^6+4/45<1/3\). Since \(\sup|J_k|<1/2\), for every real \(q\ge6\) we obtain
\[
I_k(q)<\frac13\left(\frac12\right)^{q-6}=\frac{64}{3}2^{-q},\qquad k\ge2.
\]

**3. A certified interval of mass in degree one.** The alternating Taylor series gives, for \(0\le r\le21/10\),
\[
J_1(r)\ge L(r):=\frac r2-\frac{r^3}{16}+\frac{r^5}{384}-\frac{r^7}{18432}.
\]
The second derivative is \(L''(r)=r(-1152+160r^2-7r^4)/3072<0\) for \(r>0\), since the quadratic in \(r^2\) has negative discriminant. The two exact endpoint evaluations satisfy \(L(8/5)>9/16\) and \(L(21/10)>9/16\). Concavity therefore proves \(J_1(r)>9/16\) throughout \([8/5,21/10]\). Hence
\[
I_1(q)>\int_{8/5}^{21/10}\left(\frac9{16}\right)^q r\,dr
=\frac{37}{40}\left(\frac9{16}\right)^q.
\]

**4. Uniform comparison.** Exact integer arithmetic verifies
\[
\frac{37}{40}\left(\frac98\right)^{27}>\frac{64}{3}.
\]
Because \(9/8>1\), the inequality persists for all real \(q\ge27\). Combining the previous bounds gives
\[
I_1(q)>\frac{37}{40}\left(\frac9{16}\right)^q
>\frac{64}{3}2^{-q}> I_k(q),\qquad k\ge2.
\]
Xu's exact planar mode-decomposition stability theorem (Theorem 1.3 and Remark 3 in the cited preprint) now identifies the sharp coefficient with the difference between degree-zero and degree-one modal norms. Its equality classification gives exactly the families stated above.

## Verification

Run `python3 CHECK.py` in the directory containing the accompanying standalone script. It checks all nontrivial rational certificates: the Bernstein degree-elevation identity, the positive coefficient minimum, the lower polynomial on \([0,16]\), endpoint values, and the strict threshold comparison at \(q=27\). The analytic ingredients taken from the literature (Landau's order bound, Watson's envelope, and Xu's spectral reduction) are separately named in the references; finite arithmetic checks alone are not presented as proofs of those infinite statements.

## Relationship to prior work

Xu (2026) proves degree-zero dominance for all \(q>4\), describes the exact spectral form of the sharp stability coefficient, and explicitly notes in Remark 3 that the maximizing positive degree in dimension two is not determined for every real \(q>4\). The present result supplies that missing index, and hence a closed sharp stability formula, on the infinite real interval \(q\ge27\). Carneiro–Oliveira e Silva–Sousa (2019) and Ciccone–Sousa (2025) prove degree-zero maximization on parameter ranges and endpoint/special-exponent mode comparisons but do not state this uniform positive-degree result on \(q\ge27\). The strict endpoint order due to Landau, by itself, does not furnish the stated finite-exponent bound.

## Limitations

The sufficient threshold \(27\) is not known to be optimal and no ordering is claimed for \(4<q<27\). The result concerns the planar radial–angular mixed norm, not the unmixed \(L^q(\mathbb R^2)\) extension norm. The exact coefficient is specified by convergent Bessel integrals, not an elementary closed form. Prior implicit coverage in further literature remains a nonzero originality risk. Independent mathematical validation has not been performed.

## References

1. Z. Xu, *Sharp radial–angular mixed norm Fourier extension and global stability on spheres*, first submitted 2026-10-14, arXiv:2610.19648; Theorems 1.2–1.4, Remark 3, Lemma 3.7 and Section 5. https://arxiv.org/abs/2610.19648
2. E. Carneiro, D. Oliveira e Silva and M. Sousa, *Sharp mixed norm spherical restriction*, arXiv:1710.10365; Advances in Mathematics 341 (2019), 583–608; Theorems 1–3. https://arxiv.org/abs/1710.10365
3. V. Ciccone and M. Sousa, *Global and local maximizers for some Fourier extension estimates on the sphere*, arXiv:2312.07309; Journal of Fourier Analysis and Applications 31 (2025), article 70; Section 2 and Section 3. https://link.springer.com/article/10.1007/s00041-025-10201-7
4. L. J. Landau, *Bessel Functions: Monotonicity and Bounds*, Journal of the London Mathematical Society 61 (2000), 197–215. https://doi.org/10.1112/S0024610799008352
