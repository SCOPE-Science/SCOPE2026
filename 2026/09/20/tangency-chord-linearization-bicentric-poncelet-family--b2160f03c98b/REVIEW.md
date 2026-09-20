# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The mathematical reduction is closed and exact. The two tangency chords of a bicentric quadrilateral are perpendicular, and in a tangential quadrilateral the two outer diagonals and the two tangency chords are concurrent. Thus the fixed-circle family may be studied by rotating a perpendicular pair of chords of the incircle through their fixed common point.

The classical chord-tangent locus calculation gives
\[
R^2=\frac{r^4(2r^2-p^2)}{(r^2-p^2)^2},\qquad p=IP.
\]
Solving this in terms of \(\Delta=\sqrt{4R^2+r^2}\) gives
\[
p^2=r^2\frac{\Delta-3r}{\Delta-r}.
\]
If the orthogonal chord pair is rotated by an angle \(\alpha\), direct distance-to-line geometry gives
\[
k^2=4(r^2-p^2\sin^2\alpha),\qquad
l^2=4(r^2-p^2\cos^2\alpha).
\]
Hence the sum \(k^2+l^2\) is fixed and the whole feasible set in squared-chord coordinates is exactly the stated line segment. The endpoint values are obtained when one chord passes through the incircle center.

The area step uses two known identities: \(K=kl d_1d_2/(k^2+l^2)\) and \(d_1d_2=2r(\Delta+r)\). They reduce immediately to
\[
s=\frac{\Delta-r}{2r^2}kl.
\]
The two defect identities then follow from \(4uv=(u+v)^2-(u-v)^2\) and, with \(M=4r^2\),
\[
uv-M[(u+v)-M]=(M-u)(M-v).
\]
No inequality estimate is hidden in these derivations. The lower-defect factors are nonnegative because \(k,l\le2r\).

The equality cases were checked geometrically. Equal tangency chords characterize a kite among tangential quadrilaterals, and a cyclic kite is a right kite. If one tangency chord is a diameter, the tangents at its endpoints are parallel, so the outer cyclic tangential quadrilateral is an isosceles tangential trapezoid. The square \(R=\sqrt2r\) is the common degenerate endpoint where the fixed-circle family collapses.

A standalone SymPy 1.14.0 script checks all main algebraic reductions and separately constructs representative tangent quadrilaterals from perpendicular chord pairs; the numerical circumradii are constant under rotation and agree with the exact locus formula. The computation is supplementary and not required by the proof.

## Originality

**PASS, to the best of our knowledge.**

The novelty claim deliberately excludes the classical infrastructure. Stastna's 2005 exposition of Fuss' problem explicitly gives the perpendicular-tangency-chord characterization, the tangent construction from perpendicular chords, and the rotating right-angle locus used to derive Fuss' relation. Salazar (2006) is another short treatment of Fuss' theorem. These facts are background, not findings claimed here.

Josefsson's 2010 work develops formulas for tangency chords of a tangential quadrilateral. His 2011 area paper explicitly restates the formula
\[
K=\frac{kl d_1d_2}{k^2+l^2}
\]
and relates tangency-chord imbalance to bimedian imbalance. The present record does not claim those formulas.

Bencze and Dragan (2021) prove the Blundon--Eddy semiperimeter bounds and, importantly, obtain exact factorizations of the same upper and lower semiperimeter deficits in terms of differences of the four outer side lengths. This is a close prior result. The claimed contribution here is different: the deficits are expressed exactly through the two contact diagonals, and the contact-diagonal pair itself is shown to have a complete fixed-radii line-segment profile.

Dragan and Bencze (2023) study tangent lengths and the contact quadrilateral. Their paper explicitly proves orthodiagonality of the contact quadrilateral and radius-dependent formulas for products and perimeter bounds of its four sides. No tangency-chord squared-sum, complete two-diagonal image, or the displayed contact-diagonal defect factorizations was located there. Josefsson (2023) studies the diagonal point and related collinearities, providing another nearby check on the configuration.

External searches used exact and synonymous formulations involving bicentric/chord-tangent quadrilaterals, contact diagonals, tangency chords, perpendicular incircle chords, Poncelet families, semiperimeter profiles, and Blundon--Eddy defects. Current-index checks also included recent bicentric-quadrilateral material. No located source states the package of formulas (2)--(9) in RESULT.md.

The residual originality risk is material rather than cosmetic because the proof combines short classical ingredients. Dorrie's *100 Great Problems of Elementary Mathematics* (1965), section 39, is repeatedly cited for the chord-tangent locus but its full section was not directly inspected here. Josefsson's 2023 references identify Scherrer's 1933 work on bicentric quadrilaterals as an early source for diagonal-point geometry; that paper was not directly inspected. Tran Quang Hung's 2024 *A generalisation of Fuss' theorem* was identified and its bibliographic page and references were checked, but its full text was not directly inspected. Any of these could conceivably contain an equivalent formula under different notation. Accordingly no stronger originality claim is made.

## Value

**PASS.**

The fixed-radii Poncelet family becomes especially simple in the squared lengths of the two contact diagonals: its image is an explicit affine segment. This coordinates a classical family by geometrically intrinsic data, gives a direct inverse formula for \(R\), and yields an invariant ratio between the area of the outer bicentric quadrilateral and that of its contact quadrilateral.

The exact defect identities are stronger than merely re-proving the Blundon--Eddy inequalities: they quantify upper extremality by squared contact-diagonal imbalance and lower extremality by the product of the two deficits from being incircle diameters. Their equality factors transparently identify the right-kite and isosceles-trapezoid endpoints.

## Limitations

- Convex Euclidean bicentric quadrilaterals only.
- The line segment is an image statement for \((k^2,l^2)\), not an injective moduli parametrization.
- No claim is made for general tangential quadrilaterals, ex-bicentric quadrilaterals, or higher Poncelet polygons.
- The uninspected older and recent sources listed above are genuine originality uncertainties.
- The verification script supports algebra and representative geometry but is not a formal proof checker.

## Sources checked

- B. Stastna, *Fuss' Problem of the Chord-Tangent Quadrilateral* (2005): full presentation inspected, including perpendicular tangency chords, the construction, and the chord-tangent locus. https://math.fce.vutbr.cz/~pribyl/workshop_2005/prispevky/StastnaPr.pdf
- J. C. Salazar, *Fuss' theorem*, The Mathematical Gazette 90 (2006), 306--307: bibliographic page and references inspected. https://doi.org/10.1017/S002555720017980X
- M. Josefsson, *The Area of a Bicentric Quadrilateral*, Forum Geometricorum 11 (2011), 155--164: text inspected, especially the tangency-chord area formula and cited 2010 chord formulas. https://studyres.com/doc/14608666/the-area-of-a-bicentric-quadrilateral
- M. Bencze and M. Dragan, *A new proof of the Blundon-Eddy inequality and some applications*, Arhimede Mathematical Journal 8(2) (2021), 158--167: full relevant theorem and side-difference identities inspected. https://amj-math.com/wp-content/uploads/2022/01/AMJ2021-vol8iss2.pdf
- M. Dragan and M. Bencze, *Some relations between the tangent lengths of a bicentric quadrilateral*, Arhimede Mathematical Journal 10(1) (2023), 13--27: relevant contact-quadrilateral corollaries inspected. https://amj-math.com/wp-content/uploads/2023/07/AMJ2023-vol10iss1.pdf
- M. Josefsson, *Fifteen collinear points in bicentric quadrilaterals*, International Journal of Geometry 12(4) (2023), 13--27: diagonal-point section and references inspected. https://ijgeometry.com/wp-content/uploads/2023/09/2.-13-27.pdf
- T. Q. Hung, *A generalisation of Fuss' theorem*, The Mathematical Gazette 108 (2024), 532--536: bibliographic page and references inspected; full text not directly inspected. https://doi.org/10.1017/mag.2024.130
