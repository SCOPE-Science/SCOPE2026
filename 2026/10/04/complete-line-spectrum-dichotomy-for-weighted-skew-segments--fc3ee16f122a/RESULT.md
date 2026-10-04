# Complete line-spectrum dichotomy for weighted skew segments
## Finding
Let \(d\ge 3\), and let
\[
I_j=\{p_j+t v_j:0\le t\le T_j\},\qquad j=1,2,
\]
where \(v_1,v_2\) are unit vectors, \(T_1,T_2>0\), and \(v_1,v_2,p_2-p_1\) are linearly independent. Let
\[
\mu=c_1\mathcal H^1\!\restriction I_1+c_2\mathcal H^1\!\restriction I_2,
\qquad c_1,c_2>0,\qquad c_1T_1+c_2T_2=1.
\]
Then every spectrum of \(\mu\) that is contained in an affine line is obtained as follows, and every set obtained in this way is a spectrum.

Choose \(u\in\mathbb R^d\setminus\{0\}\) such that
\[
|\langle u,v_1\rangle|=c_1,
\qquad
|\langle u,v_2\rangle|=c_2,
\]
and such that the projected intervals
\[
J_j=\{\langle u,x\rangle:x\in I_j\}
\]
have disjoint interiors. Their lengths are \(c_jT_j\), hence \(|J_1|+|J_2|=1\). Let \(g\ge0\) be the distance between \(J_1\) and \(J_2\). Up to an arbitrary translation \(\lambda_0\in\mathbb R^d\), the complete list is:

1. If \(g\in\mathbb Z_{\ge0}\), then
\[
\Lambda=\lambda_0+\mathbb Z u.
\]
2. In addition, if
\[
c_1T_1=c_2T_2=\frac12
\quad\text{and}\quad
n=2g+1\in\mathbb N,
\]
then for every odd integer \(p\),
\[
\Lambda=\lambda_0+u\left(2\mathbb Z\cup\left(\frac pn+2\mathbb Z\right)\right).
\]

Consequently, unless the two segments carry equal mass \(1/2\), every line-contained spectrum is a translate of a single lattice. Non-lattice line spectra occur only in the equal-mass case, and then only at the half-integral projected-gap positions encoded by \(2g+1\in\mathbb N\).

For the skew pair
\[
I_1=\{(t,0,0):0\le t\le1\},\qquad
I_2=\{(0,t,1):0\le t\le1\},
\]
with \(c_1=c_2=1/2\), the recent construction uses \(u_0=(1/2,1/2,1/2)\) and obtains the lattice spectrum \(\mathbb Z u_0\). The classification also gives the genuinely non-lattice line spectrum
\[
u\left(2\mathbb Z\cup\left(\frac12+2\mathbb Z\right)\right),
\qquad u=(1/2,1/2,1),
\]
because the corresponding projected intervals are \([0,1/2]\) and \([1,3/2]\).

## Assumptions and scope
A spectrum means an orthonormal basis of exponentials \(e^{2\pi i\langle\lambda,x\rangle}\) in \(L^2(\mu)\). Endpoints of intervals are immaterial because they have zero \(\mathcal H^1\)-measure. The result classifies spectra that are contained in an affine line; it does not claim that every spectrum of a non-coplanar two-segment measure is linear. Indeed, the recent source gives examples with spectra not contained in any straight line.

The vector \(u\) is a scaled direction vector, not necessarily a unit vector. For a fixed spectral line its normalization by \(|\langle u,v_j\rangle|=c_j\) is unique up to sign.

## Proof
Translate a line-contained spectrum so that it contains the origin. Write its supporting line as \(\mathbb R w\) with \(|w|=1\), so the spectrum has the form \(\{\sigma w:\sigma\in\Sigma_w\}\).

First, the scalar projection \(P_w(x)=\langle w,x\rangle\) must be one-to-one \(\mu\)-almost everywhere. Every exponential with frequency in \(\mathbb Rw\) is measurable with respect to \(P_w\). If \(P_w\) had a positive-measure fiber multiplicity, the closed span of those exponentials would lie in the proper subspace of functions measurable with respect to \(P_w\), contradicting completeness. For two non-degenerate segment components this means \(\langle w,v_j\rangle\ne0\) and the two projected intervals have disjoint interiors.

Let \(\nu=(P_w)_\#\mu\). Projection is then a Hilbert-space isomorphism from \(L^2(\mu)\) onto \(L^2(\nu)\), and \(\Sigma_w\) is a spectrum of \(\nu\). On the image of \(I_j\), the density of \(\nu\) with respect to Lebesgue measure is
\[
\frac{c_j}{|\langle w,v_j\rangle|}.
\]
An absolutely continuous spectral measure has constant density on its support. Therefore these two numbers are equal; call their common value \(D>0\). Set \(u=Dw\). Then
\[
|\langle u,v_j\rangle|=c_j
\]
for both \(j\), and the pushforward under \(P_u(x)=\langle u,x\rangle\) is exactly Lebesgue measure on
\[
\Omega=J_1\cup J_2.
\]
The lengths are \(|J_j|=c_jT_j\), so \(|\Omega|=1\).

It remains to classify spectra of a union of two disjoint intervals of total length one. Let
\[
r=\min(c_1T_1,c_2T_2)\le\frac12
\]
and let \(g\) be the gap between the projected intervals. After translation, reflection, and relabeling, \(\Omega\) is equivalent to
\[
(0,r)\cup(a,a+1-r),\qquad a=r+g.
\]
Łaba's two-interval classification says that every spectrum containing zero is in one of exactly two cases:
\[
a-r\in\mathbb Z,\qquad \Sigma=\mathbb Z,
\]
or
\[
r=\frac12,\qquad a=\frac n2,\qquad
\Sigma=2\mathbb Z\cup\left(\frac pn+2\mathbb Z\right)
\]
for an integer \(n\ge1\) and an odd integer \(p\). Substituting \(a=r+g\) gives precisely the two alternatives stated above. Multiplication by \(u\) lifts \(\Sigma\) back to the original frequency line.

Conversely, suppose \(u\) satisfies the stated slope balance and projected-disjointness conditions. Then projection by \(P_u\) is one-to-one almost everywhere and sends \(\mu\) to Lebesgue measure on \(J_1\cup J_2\). In either listed case, Łaba's theorem supplies the stated one-dimensional spectrum. The projection principle then lifts it to a spectrum of \(\mu\). Finally, translating any spectrum by \(\lambda_0\) multiplies the entire exponential basis by one fixed unimodular character, so arbitrary affine translates remain spectra.

## Verification
The accompanying script `verify_line_spectra.py` checks the recent skew example and the additional exceptional branch. For \(u=(1/2,1/2,1)\), it verifies exactly that the projected intervals are \([0,1/2]\) and \([1,3/2]\), so \(g=1/2\) and \(n=2\). It then computes a finite Gram window for
\[
2\mathbb Z\cup\left(\frac12+2\mathbb Z\right)
\]
and obtains numerical error below \(3\times10^{-16}\). It also rechecks the lattice branch \(u_0=(1/2,1/2,1/2)\). The script is a regression check of the formulas; the infinite classification is established by the proof above, not by finite computation.

## Relationship to prior work
Wu's 2026 paper proves that every constant-density measure on two non-coplanar segments admits a straight-line spectrum. Its proof chooses one direction whose two projected intervals meet at an endpoint, producing the lattice branch with \(g=0\). The paper does not classify all straight-line spectra in the non-coplanar case.

Kolountzakis and Wu prove the projection principle for line spectra: when projection onto a line is one-to-one almost everywhere, line spectra are exactly spectra of the projected one-dimensional measure. Dutkay and Lai supply the uniformity theorem forcing an absolutely continuous spectral measure to have constant density. Łaba classifies all spectra of a union of two intervals of total length one.

The present statement combines these ingredients to close the line-spectrum classification for the weighted non-coplanar geometry. The new structural consequence is the lattice-versus-two-coset dichotomy and the fact that the non-lattice branch is confined exactly to equal segment masses. The derivation is short once the earlier theorems are assembled; no new one-dimensional Fuglede theorem is claimed.

## Limitations
Only spectra contained in an affine line are classified. Non-coplanar two-segment measures can also possess spectra not lying on any straight line, so this is not a classification of all spectra of \(\mu\). The proof relies on the published one-dimensional two-interval classification and the standard uniformity theorem for absolutely continuous spectral measures. A literature search found no prior statement of this complete weighted skew line-spectrum dichotomy, but an equivalent corollary may exist under different notation.

## References
1. Sha Wu, *Spectrality of Weighted Measures on Two Line Segments*, arXiv:2609.27364v1, 23 September 2026. 2020 MSC 42C15, 42C30.
2. Mihail N. Kolountzakis and Sha Wu, *Spectrality of a measure consisting of two line segments*, Journal of Fourier Analysis and Applications 32(4), 2026; arXiv:2501.11367v2.
3. Izabella Łaba, *Fuglede's conjecture for a union of two intervals*, Proceedings of the American Mathematical Society 129 (2001), 2965--2972; arXiv:math/0002067v1.
4. Dorin Ervin Dutkay and Chun-Kit Lai, *Uniformity of measures with Fourier frames*, Advances in Mathematics 252 (2014), 684--707; arXiv:1202.6028.
5. Mihail N. Kolountzakis, Ruxi Shi, and Sha Wu, *Spectra for finite unions of line segments*, arXiv:2512.19872v1, 2025.
