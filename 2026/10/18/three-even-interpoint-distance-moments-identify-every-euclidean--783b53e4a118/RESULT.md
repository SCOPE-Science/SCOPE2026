# Three even interpoint-distance moments identify every Euclidean parallelogram

## Finding

For every nondegenerate Euclidean parallelogram \(K\subset\mathbb R^2\), let \(X,Y\) be independent points sampled uniformly from its area, and put
\[
m_j(K)=\mathbb E\|X-Y\|^{2j}\qquad(j=1,2,3).
\]
Then **the three real numbers \((m_1,m_2,m_3)\) determine \(K\) up to Euclidean congruence**, including all rhombi, rectangles, squares, and oblique parallelograms. Explicit rational operations and square roots recover its squared side lengths and absolute side-vector dot product, hence its side lengths and acute unoriented edge-line angle.

The initial pair \((m_1,m_2)\) does **not** determine a parallelogram: there are two noncongruent nondegenerate parallelograms with identical first two moments \((1/3,13/60)\) but respective third moments \(43/210\) and \(1133/5600\). Thus three moments are necessary and sufficient **among these initial consecutive even moments**; no minimality assertion is made about arbitrary pairs of other invariants.

## Assumptions and scope

Write an arbitrary translate of \(K\) as
\[
K=x_0+\{s a+t b:-\tfrac12\le s,t\le\tfrac12\},
\]
with nonzero, linearly independent side vectors \(a,b\in\mathbb R^2\). Put \(A=\|a\|^2>0\), \(B=\|b\|^2>0\), and \(C=\langle a,b\rangle\). Nondegeneracy means \(C^2<AB\). Reversing a side-vector sign or interchanging the two vectors leaves the parallelogram unchanged up to translation; consequently a congruence class is specified by the unordered pair \(\{A,B\}\) and \(|C|\).

Both points \(X,Y\) are sampled independently with replacement under the **normalized two-dimensional Lebesgue area measure**. There is no sampling of random lines, boundary points, or independent direction labels. No area, diameter, perimeter, orientation, or side-count statistic is supplied in addition to the three scalar moments. Translations and reflections are ignored in Euclidean congruence.

## Proof

Because the affine parametrization of \(K\) has constant nonzero Jacobian, \(X-Y=aU+bV\), where \(U,V\) are independent differences of two independent uniform variables on \([-1/2,1/2]\). Both differences have triangular density \(1-|u|\) on \([-1,1]\), hence, for each integer \(r\ge0\),
\[
\mathbb E U^{2r}=\mathbb E V^{2r}=\frac{2}{(2r+1)(2r+2)},\qquad
\mathbb E U^{2r+1}=\mathbb E V^{2r+1}=0. \tag{1}
\]
Write \(S=A+B\), \(P=AB\), and \(Z=C^2\). Since
\[
\|X-Y\|^2=A U^2+B V^2+2C UV,
\]
expanding the first three powers and using (1) gives the exact identities
\[
\begin{aligned}
m_1&=\frac{S}{6},\\
m_2&=\frac{S^2}{15}-\frac{7P}{90}+\frac{Z}{9},\\
m_3&=\frac{S^3}{28}-\frac{31SP}{420}+\frac{2SZ}{15}. \tag{2}
\end{aligned}
\]
For example, the unsymmetrized expressions for the higher moments are
\[
\begin{aligned}
m_2&=\frac{A^2+B^2}{15}+\frac{AB}{18}+\frac{C^2}{9},\\
m_3&=\frac{A^3+B^3}{28}+\frac{A^2B+AB^2}{30}+\frac{2(A+B)C^2}{15}.
\end{aligned}
\]
These formulas are valid even at \(A=B\) or \(C=0\); there is no division by the angle or difference of side lengths.

The first moment recovers \(S=6m_1>0\). Define observable quantities
\[
q=m_2-\frac{S^2}{15},\qquad r=\frac{m_3}{S}-\frac{S^2}{28}.
\]
By (2), the unknowns \((P,Z)\) satisfy
\[
\begin{pmatrix}q\\r\end{pmatrix}
=\begin{pmatrix}-7/90&1/9\\-31/420&2/15\end{pmatrix}
\begin{pmatrix}P\\Z\end{pmatrix}.
\]
The determinant of this matrix is \(-41/18900\ne0\), so its **universal inverse** is
\[
\boxed{P=\frac{-2520q+2100r}{41},\qquad
Z=\frac{-1395q+1470r}{41}.} \tag{3}
\]
Because the original data arise from a nondegenerate parallelogram, \(P>0\), \(0\le Z<P\), and \(S^2\ge4P\). The unordered squared side lengths are the two roots of \(\lambda^2-S\lambda+P\), namely
\[
\boxed{\{A,B\}=\left\{\frac{S+\sqrt{S^2-4P}}{2},\frac{S-\sqrt{S^2-4P}}{2}\right\},\qquad |C|=\sqrt Z.} \tag{4}
\]
Thus the complete Gram matrix of the two side vectors is determined up to changing the sign of a generator and swapping generators. Such modifications do not alter a centered parallelogram. Conversely, positive-definite Gram matrices with the same entries after these modifications yield Euclidean-congruent planar generator pairs. This proves the reconstruction theorem for every nondegenerate parallelogram.

For sharpness within the initial moment sequence, take two positive-definite Gram matrices
\[
G_1=\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix},\qquad
G_2=\begin{pmatrix}5/4&\sqrt{33/160}\\\sqrt{33/160}&3/4\end{pmatrix}. \tag{5}
\]
Their determinants are \(3/4\) and \(117/160\), respectively, so each is realized by two linearly independent real vectors defining a parallelogram. They have the same \(S=2\), but the unordered squared side lengths \(\{1,1\}\) and \(\{5/4,3/4\}\) differ, so the parallelograms are not congruent. Substitution in (2) yields
\[
(m_1(G_1),m_2(G_1))=(m_1(G_2),m_2(G_2))
=\left(\frac13,\frac{13}{60}\right),
\]
while
\[
m_3(G_1)=\frac{43}{210},\qquad m_3(G_2)=\frac{1133}{5600},\qquad
m_3(G_1)-m_3(G_2)=\frac{41}{16800}>0.
\]
Therefore the first two even moments cannot suffice, completing the proof.

## Verification

The standalone standard-library program `verify.py` enumerates all multinomial coefficients of the triangular-density moment expansion in (2), checks the exact rational coefficient tables for the first three powers, reconstructs \((S,P,Z)\) from 300 seeded rational nondegenerate Gram configurations, and checks (5) and its exact moment discrepancy. Run `python3 verify.py`; the expected success marker is `THREE_EVEN_DISTANCE_MOMENTS_EXACT_OK`. The universal theorem is proved by (1)–(4) and the exact nonzero matrix determinant, not by finite trials.

## Relationship to prior work

O'Hara [1] studies identification of **generic** polygonal domains from the *entire* interpoint-distance distribution or Riesz energy function. The present result uses exactly three prescribed moments and addresses **all** parallelograms, a nongeneric parallel-sided class. Even a full-distribution uniqueness statement would not imply uniqueness from three particular moments. The full text of [1] could not be inspected; the abstract and bibliographic record support the stated comparison but a specialized finite-moment result in uninspected material remains a priority risk.

Martirosyan [2] gives direction-dependent chord-length and covariogram formulas for arbitrary convex quadrilaterals. Its sampled chord passes through a line with uniform transverse position *at a prescribed direction*; that measurement is not the distance between two independent area-uniform points and does not yield the three-moment inverse formula. The accessible full article defines the sampling convention and reports the direction-dependent formulas.

Bäsel [6] computes distance moments for **regular** polygons, including squares; such special-case calculations do not establish the full three-parameter all-parallelogram inverse.

Two closely related published mathematical records [3,4] provide distinct parallelogram invariants. [3] calculates the area-uniform **fourth** interpoint-distance moment as one component of a boundary/area comparison; its single fourth moment does not determine the three Gram parameters, and it supplies no sixth-moment inversion. [4] recovers parallelograms from **projection widths in random unlabeled directions**, using different data. An additional record [5] concerns the coefficient of the *short-distance tail* for general convex polygons rather than the first three global even moments. None of these inspected statements implies (3) or the explicit two-moment obstruction (5).

## Limitations

The result applies only to nondegenerate Euclidean parallelograms under independent normalized area-uniform endpoint sampling; it says nothing about more general quadrilaterals, random-line chord distributions, noisy empirical moments, or quantitative stability of reconstruction. It proves minimality only for the initial consecutive even moments, not for every possible pair of nonlinear statistics. A complete historical originality guarantee is not asserted: particularly, the full version of [1] was unavailable during source comparison.

## References

[1] J. O'Hara, *Identification of generic polygonal domains by integral-geometric invariants*, arXiv:2608.02288v1, first public 2026-08-03, https://arxiv.org/abs/2608.02288.

[2] D. M. Martirosyan, *Orientation-Dependent Chord Length Distribution in a Convex Quadrilateral*, Journal of Contemporary Mathematical Analysis 58 (2023), 416–430, https://doi.org/10.3103/S1068362323060055 (open-access HTML, Sections 1–6).

[3] *Fourth-chord moment amplification and angular phase transition for parallelograms*, public mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-fourth-chord-moment-amplification-and-angular-phase-transition-f--45b0568cfb6e.

[4] *Three unlabeled width statistics reconstruct a parallelogram with sharp stability*, public mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-three-unlabeled-width-statistics-reconstruct-a-parallelogram-wit--dcfda0360928.

[5] *Sharp uniform angular stability for the short-pair distance coefficient of convex polygons*, public mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-uniform-angular-stability-for-the-short-pair-distance-coef--24e8bcd8655b.

[6] U. Bäsel, *The moments of the distance between two random points in a regular polygon*, arXiv:2101.03815v1, first public 2021-01-11, https://arxiv.org/abs/2101.03815.
