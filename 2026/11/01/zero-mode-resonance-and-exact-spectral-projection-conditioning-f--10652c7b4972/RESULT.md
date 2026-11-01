# Zero-mode resonance and exact spectral-projection conditioning for triangular rotation cocycles

## Finding
Fix an irrational angle \(\alpha/(2\pi)\notin\mathbb Q\). On \(\mathcal H=L^2(\mathbb T;\mathbb C^2)\), let \((Uf)(\theta)=f(\theta+\alpha)\) and, for positive real \(a,b\) and any complex trigonometric polynomial \(c(\theta)=\sum_{n\in F}c_ne^{in\theta}\), set
\[
T_{a,b,c}=\begin{pmatrix}aU&M_cU\\0&bU\end{pmatrix}.
\]
Here \(F\subset\mathbb Z\) is finite, missing coefficients are zero, and \(M_c\) denotes multiplication by \(c\).

**Separated radii.** If \(a\ne b\), the spectrum is exactly the disjoint union of the circles of radii \(a\) and \(b\). With
\[
h_{a,b}(\theta)=\sum_{n\in F}\frac{c_n}{b-ae^{in\alpha}}e^{in\theta},
\]
the Riesz projection onto the complete spectral component of radius \(a\) is
\[
P_{a,b,c}=\begin{pmatrix}I&-M_{h_{a,b}}\\0&0\end{pmatrix},\qquad
\|P_{a,b,c}\|=\sqrt{1+\|h_{a,b}\|_\infty^2}.
\]
The two components realize the largest possible number for a two-dimensional fiber.

**Closing the gap.** Fix \(r>0\). As positive \(a,b\to r\) with \(a\ne b\),
\[
\lim |a-b|\,\|P_{a,b,c}\|=|c_0|.
\]
If \(c_0=0\), the projections remain uniformly bounded and converge in norm to the idempotent with upper-right entry \(-M_{h_{r,r}}\), where
\[
h_{r,r}(\theta)=\sum_{\substack{n\in F\\n\ne0}}\frac{c_n}{r(1-e^{in\alpha})}e^{in\theta}.
\]
If \(c_0\ne0\), the projections diverge in norm at exact reciprocal-gap order.

**Collision and power growth.** At \(a=b=r\), the spectrum is the single circle of radius \(r\), and
\[
\lim_{N\to\infty}\frac{\|T_{r,r,c}^N\|}{N r^N}=\frac{|c_0|}{r}.
\]
In particular, the normalized powers are uniformly bounded precisely when \(c_0=0\); then \(T_{r,r,c}\) is similar to \(r(U\oplus U)\). A nonzero mean produces linear Jordan-type amplification even though the off-mean frequencies can always be removed by a bounded similarity.

**Exact two-mode law.** If \(c(\theta)=c_0+c_ne^{in\theta}\) for a fixed nonzero integer \(n\), then for \(a\ne b\)
\[
\|P_{a,b,c}\|=\left[1+\left(\frac{|c_0|}{|b-a|}+\frac{|c_n|}{|b-ae^{in\alpha}|}\right)^2\right]^{1/2}.
\]
This includes the sharp bounded limit \(\left[1+|c_n|^2/(r^2|1-e^{in\alpha}|^2)\right]^{1/2}\) when \(c_0=0\). The zero-mode coefficient is therefore the precise obstruction to a uniformly conditioned spectral splitting in this family.

## Assumptions and scope
The circle carries normalized Haar measure. The angle is irrational modulo \(2\pi\), the fiber is complex two-dimensional, \(a,b,r>0\), and the coupling is a finite complex Fourier series. No regularity or uniformity statement is claimed for infinite Fourier series: small divisors can prevent the collision similarity even when the mean is zero. The power-growth limit concerns collision at fixed \(r\); the spectral projection exists only when \(a\ne b\).

## Proof
1. The Fourier characters diagonalize \(U\) with eigenvalues \(e^{in\alpha}\). Irrationality makes these dense in the unit circle, so \(\sigma(U)=\mathbb T\). For \(a\ne b\), all denominators \(b-ae^{in\alpha}\) are nonzero. Define the bounded invertible shear \(S=\begin{pmatrix}I&M_h\\0&I\end{pmatrix}\). Since \(UM_h=M_{h\circ R_\alpha}U\), direct multiplication gives
\[
S\begin{pmatrix}aU&0\\0&bU\end{pmatrix}S^{-1}
=\begin{pmatrix}aU&M_{bh-a(h\circ R_\alpha)}U\\0&bU\end{pmatrix}.
\]
For the displayed Fourier coefficients, \(bh-a(h\circ R_\alpha)=c\), giving the similarity and exactly the two spectral circles.

2. Riesz projections are similarity covariant. Conjugating \(\operatorname{diag}(I,0)\) gives \(P=\begin{pmatrix}I&-M_h\\0&0\end{pmatrix}\). At every point \(\theta\) this is the row \((1,-h(\theta))\) followed by inclusion in the first coordinate. Its Hilbert-space norm is \(\sqrt{1+|h(\theta)|^2}\). Taking the essential supremum proves the exact projection-norm identity. In a two-mode polynomial, the independent phase \(e^{in\theta}\) ranges over the whole circle, hence the supremum modulus of the two terms is their sum of absolute values.

3. Write \(h_{a,b}=c_0/(b-a)+g_{a,b}\), where \(g_{a,b}\) consists of nonzero frequencies. As \(a,b\to r>0\), all finitely many denominators for \(n\ne0\) stay away from zero because the angle is irrational. Thus \(g_{a,b}\to h_{r,r}\) uniformly. Consequently \(|a-b|\|h_{a,b}\|_\infty\to|c_0|\), and the exact projection norm gives the stated reciprocal-gap law. If \(c_0=0\), uniform convergence of \(h\) implies convergence of the projections in operator norm.

4. At collision, the same shear constructed only with nonzero Fourier frequencies gives
\[
T_{r,r,c}=S\begin{pmatrix}rU&c_0U\\0&rU\end{pmatrix}S^{-1}.
\]
The two entries of this constant triangular matrix commute; therefore its \(N\)-th power is \(r^N\begin{pmatrix}U^N&N(c_0/r)U^N\\0&U^N\end{pmatrix}\). Undoing the shear, the normalized \(N\)-th power differs from the rank-one upper-block operator \(N(c_0/r)\begin{pmatrix}0&U^N\\0&0\end{pmatrix}\) by a block matrix of norm at most \(1+2\|h_{r,r}\|_\infty\). Since \(U^N\) is unitary, its upper-block operator has norm one. Dividing by \(N\) proves the exact limit. When \(c_0=0\), the similarity is to a scalar multiple of a unitary, so normalized powers are uniformly bounded. When \(c_0\ne0\), their linear growth rules out power boundedness. The collision spectrum is one circle by triangular resolvent inversion away from \(r\mathbb T\) and the unchanged quotient diagonal spectrum.

## Verification
The accompanying `check.py` uses deterministic finite computations to test the Fourier cohomological equation in both regimes and the sharp two-mode supremum. It checks finite numerical instances only; the all-angle and all-degree statements follow from the preceding analytic similarity and finite Fourier argument, not from sampling. The proof also covers vanishing coefficients and both orders of \(a\) and \(b\).

## Relationship to prior work
Duru, Ilter, Kitover, and Orhon, *Operators commuting with \(L^\infty\) on Köthe–Bochner spaces* (arXiv:2610.24853), prove decomposability of spectral projections for operator-valued weighted composition operators and a bound of two spectral components for two-dimensional fibers (Corollaries 3.4 and 3.8). These results motivate the present exact model but do not supply its projection-condition number or collision mean-mode criterion. Earlier work on upper triangular operator matrices and nonautonomous dichotomy spectra addresses spectral invariance and diagonal significance, rather than the Fourier-mode-dependent conditioning law computed here. Elementary Fourier cohomology and shear similarities are used transparently in this proof; priority for this particular quantitative formulation is not independently established.

## Limitations
This is a complete assertion only for finite Fourier couplings and two-dimensional complex fibers. It does not establish a universal quantitative projection bound for arbitrary measurable cocycles. At spectral collision the two circles merge and there is no Riesz projection separating them. The result is a proved formula for this model, not a general solution to cocycle reducibility or a classification of spectral projections for all Köthe–Bochner operators.

## References
1. H. Duru, S. Ilter, A. Kitover and M. Orhon, *Operators commuting with \(L^\infty\) on Köthe–Bochner spaces*, arXiv:2610.24853 (first public 2026-10-17), especially Corollaries 3.4, 3.8 and Section 4. https://arxiv.org/abs/2610.24853.
2. B. P. Duggal, I. H. Jeon and I. H. Kim, *Upper triangular operator matrices, asymptotic intertwining and Browder, Weyl theorems*, Journal of Inequalities and Applications (2013), article 268. https://doi.org/10.1186/1029-242X-2013-268.
3. C. Pötzsche, *Dichotomy spectra of triangular equations*, Discrete and Continuous Dynamical Systems 36 (2016), 423–450. https://doi.org/10.3934/dcds.2016.36.423.
