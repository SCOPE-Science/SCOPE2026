# Axial Fourier-zero transition for truncated balls in dimensions three, five and seven

## Finding
Let \(d\in\{3,5,7\}\), let \(-1<h<1\), and define the proper spherical cap
\[
C_{d,h}=\{(y,s)\in\mathbb R^{d-1}\times\mathbb R:|y|^2+s^2<1,\ s>h\}.
\]
With angular-frequency Fourier convention \(\widehat f(\xi)=\int f(x)e^{-i\xi\cdot x}\,dx\), write \(e_d\) for its symmetry-axis unit vector.

**Dimension-three and dimension-five rigidity.** For every proper cap height \(-1<h<1\) and every real \(t\),
\[
\widehat{\mathbf1_{C_{3,h}}}(t e_3)\ne0,
\qquad
\widehat{\mathbf1_{C_{5,h}}}(t e_5)\ne0.
\]
This includes cap heights \(h<0\), where the corresponding one-dimensional section density is not monotone.

**Dimension-seven breakdown.** There are infinitely many distinct negative cap heights \(h_n\to-1\) and positive frequencies \(t_n\to\infty\) for which
\[
\widehat{\mathbf1_{C_{7,h_n}}}(t_n e_7)=0.
\]
They may be indexed by all sufficiently large positive integers so that
\[
h_n=-1+\frac{\sqrt3}{\pi n}+O(n^{-2}),\qquad
 t_n=\pi n+\frac\pi6+\frac{\sqrt3}{2}+O(n^{-1}).
\]
For each fixed \(h>-1\), however, the axial transform has only finitely many real zeros (possibly none). Thus the sequence involves simultaneously vanishing truncation and increasing frequency; it does not assert infinitely many zeros for one fixed proper cap.

## Assumptions and scope
The caps are intersections of the open unit Euclidean ball with a coordinate half-space. Frequency is measured in radians (the kernel is \(e^{-i\xi\cdot x}\)). Only the **axial restriction** of the Fourier transform is considered; the theorem makes no assertion that the full transform is zero-free in all frequency directions. Dimensions \(3,5,7\) correspond to the section exponents \(m=1,2,3\). All cap heights are strictly between \(-1\) and \(1\).

## Proof
Write \(m=(d-1)/2\). Integration over transverse balls gives, with \(v_{d-1}>0\) the volume of the unit ball in \(\mathbb R^{d-1}\),
\[
\widehat{\mathbf1_{C_{d,h}}}(t e_d)
=v_{d-1}\int_h^1(1-s^2)^m e^{-its}\,ds.
\]
Conjugation does not alter real zeros, so study \(F_{m,h}(t)=\int_h^1(1-s^2)^m e^{its}\,ds\). Clearly \(F_{m,h}(0)>0\).

For \(t\ne0\) put \(z=it\), \(p_m(s)=(1-s^2)^m\), and define the real-coefficient endpoint polynomial
\[
Q_m(s,z)=\sum_{k=0}^{2m}(-1)^k p_m^{(k)}(s)z^{2m-k}.
\]
Repeated integration by parts is **exact** for this polynomial density:
\[
F_{m,h}(t)=\frac{e^{it}Q_m(1,it)-e^{ith}Q_m(h,it)}{(it)^{2m+1}}.\tag{1}
\]
Consequently any nonzero real Fourier zero must satisfy both
\[
|Q_m(h,it)|=|Q_m(1,it)|,\qquad
 e^{it(1-h)}=Q_m(h,it)/Q_m(1,it),\tag{2}
\]
whenever the denominator is nonzero.

The following exact polynomial identities follow by expanding the derivatives in \(Q_m\), multiplying conjugate endpoint polynomials, and collecting powers of \(t\):
\[
\begin{aligned}
D_1(h,t)&:=|Q_1(h,it)|^2-|Q_1(1,it)|^2
 =(1-h^2)^2t^4,\\
D_2(h,t)&=(1-h^2)^3t^6\big((1-h^2)t^2+8\big),\\
D_3(h,t)&=(1-h^2)^4t^8\big((1-h^2)^2t^4+12(1-2h^2)t^2+180\big).
\end{aligned}\tag{3}
\]
Both \(D_1\) and \(D_2\) are strictly positive for \(-1<h<1\), \(t\ne0\); this contradicts the necessary modulus equation in (2), proving the first assertion. In particular the results are not inferred merely from numerical absence of zeros.

For dimension seven, write \(\kappa=1-h^2\). When \(h\) is negative and sufficiently close to \(-1\), we have \(0<\kappa<\sqrt5-2\) and the polynomial in the final parentheses of \(D_3\) has the positive-frequency root
\[
t_+(h)=\frac{\sqrt{6\big(1-2\kappa+\sqrt{1-4\kappa-\kappa^2}\big)}}{\kappa}>0.\tag{4}
\]
The identity \(D_3(h,t_+(h))=0\) shows the complex ratio
\[
R(h)=\frac{Q_3(h,i t_+(h))}{Q_3(1,i t_+(h))}
\]
has modulus one. It is well-defined near \(-1\) because
\[
Q_3(1,z)=48(z^3-6z^2+15z-15)
\]
has nonzero leading term on that branch.

Put \(\delta=1+h\). Direct expansion of (4) gives
\[
t_+(h)=\frac{\sqrt3}{\delta}-\frac{3\sqrt3}{2}+O(\delta),\qquad
 t_+(h)(1-h)=\frac{2\sqrt3}{\delta}-4\sqrt3+O(\delta).\tag{5}
\]
The exact derivative formula for \(Q_3\), with \(z=i t_+(h)\), gives the two finite limits
\[
\lim_{\delta\downarrow0}\delta^3Q_3(1,z)=-144\sqrt3\,i,\qquad
\lim_{\delta\downarrow0}\delta^3Q_3(-1+\delta,z)=216-72\sqrt3\,i.
\]
Therefore \(R(h)\to\tfrac12+\tfrac{\sqrt3}{2}i=e^{i\pi/3}\). On a sufficiently short interval \((-1,h_0]\) choose the continuous argument \(\theta(h)=\arg R(h)\) with
\[
\theta(h)=\pi/3+O(\delta).\tag{6}
\]
The real continuous function
\[
\Phi(h)=t_+(h)(1-h)-\theta(h)
\]
tends to \(+\infty\) as \(h\downarrow-1\), while remaining finite at \(h_0\). By the intermediate value theorem, for every sufficiently large integer \(n\) there is \(h_n\in(-1,h_0)\) with \(\Phi(h_n)=2\pi n\). Equation (2) then holds exactly with \(t_n=t_+(h_n)\), proving a genuine Fourier zero. The sequence tends to \(-1\), and (5)–(6), substituted into \(\Phi(h_n)=2\pi n\), yield precisely the two stated asymptotic expansions.

Finally, for any fixed proper height and \(m\ge1\), one integration by parts gives
\[
F_{m,h}(t)=-\frac{(1-h^2)^m e^{ith}}{it}+O_h(|t|^{-2})
\quad (|t|\to\infty),
\]
where the error follows from a further integration by parts. Hence \(F_{m,h}(t)\ne0\) for sufficiently large \(|t|\); its remaining real zeros are finite because it is a nonzero entire function and \(F_{m,h}(0)>0\).

## Verification
The standalone `check.py` expands the endpoint polynomials symbolically, verifies each of the three identities in (3) exactly, and compares 27 independent numerical quadratures with formula (1). It also locates three dimension-seven witnesses on the explicit branch (4), then confirms their Fourier integrals vanish to high precision. Run `python check.py` with the versions in `requirements.txt`; illustrative output is in `check_output.txt`. Finite witnesses are not used as proof of the infinite sequence, which follows from the argument-phase intermediate value theorem.

## Relationship to prior work
Benguria–Levitin–Parnovski (arXiv:0801.1617v1, 2008) study Fourier null varieties of convex domains and directional zeros, mostly under central symmetry. Their §4.11 contains a distinct example of an axial zero-free transform for a double-cone-shaped body whose section density is a simple power. Neither the cap geometry nor the dimension-seven phase-winding mechanism above follows directly from that example. The full relevant introduction and example were inspected.

Dimitrov–Rusev (2011) survey the classical Pólya theory of zeros of Fourier integrals of positive kernels. Pólya's nonvanishing sine-transform criterion for decreasing kernels addresses a related positivity regime; in particular cap sections restricted to \(h\ge0\) are decreasing. It does not cover the nonmonotone negative-height sections or the dimension-seven reappearance of real zeros. Relevant material from the accessible full-text survey was inspected; Pólya's original 1918 article was not separately inspected.

Earlier closely related spherical-shell, trapezoid, beta-Fourier and polytope-zero findings were compared by implication: they treat different geometries or untruncated beta densities, and do not supply the endpoint-modulus obstruction and high-frequency phase-winding sequence stated here. Database search and available-literature comparisons support a qualified originality assessment, not an exhaustive priority certificate.

## Limitations
The theorem gives no global classification of all dimension-seven cap heights admitting axial zeros, and no extension to general odd dimensions or nonaxial frequency directions. It does not assert uniqueness of the witness \(h_n\) for each index. The asymptotic constants refer to the angular-frequency convention stated above. An equivalent calculation may exist in classical, incompletely digitized Fourier-integral literature; independent review has not been performed.

## References
1. R. D. Benguria, M. Levitin, L. Parnovski, *Fourier transform, null variety, and Laplacian's eigenvalues*, arXiv:0801.1617v1, first posted 2008-01-10; relevant §§1, 3–4. https://arxiv.org/abs/0801.1617
2. D. K. Dimitrov, P. K. Rusev, *Zeros of entire Fourier transforms*, East Journal on Approximations **17** (2011), 1–110; relevant discussions of Pólya and nonvanishing Fourier integrals in §§3, 6. https://www.researchgate.net/publication/264963140_Zeros_of_entire_Fourier_transforms
3. G. Pólya, classical 1918 results on zeros of Fourier sine transforms, described and cited in Reference 2. Original article not independently inspected.
