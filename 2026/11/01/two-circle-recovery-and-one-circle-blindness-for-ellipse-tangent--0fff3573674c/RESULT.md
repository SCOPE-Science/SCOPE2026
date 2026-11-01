# Two-circle recovery and one-circle blindness for ellipse tangent-chord products

## Finding
Let \(E\subset\mathbb R^2\) be a filled ellipse with semiaxes \(a\ge b>0\) and center \(O\). Let \(r\in(0,b)\) be known. For each unoriented normal \(n\in S^1\), the line through \(rn\) perpendicular to \(n\) meets \(E\) at endpoints \(A_n,B_n\). Define the **tangent-chord product**
\[
Q_r(n)=|A_n-rn|\,|B_n-rn|.
\]
A uniformly distributed normal makes \(Q_r\) a random variable; its distribution forgets all angular labels.

**Complete one-circle inverse classification.** Let \(q_-\le q_+\) be the lower and upper endpoints of the essential range of \(Q_r\). If \(q_-<q_+\), then both endpoints lie strictly on the same side of \(r^2\). Denote by \(q_c\) the endpoint closer to \(r^2\), and by \(q_f\) the endpoint farther away. Then
\[
\lambda=\frac{q_f-r^2}{q_c-r^2}>1,\qquad
b^2=q_c+\frac{r^2}{\lambda},\qquad
 a^2=\lambda b^2.
\]
Thus just the two unlabeled range endpoints determine the ellipse up to Euclidean congruence. If \(q_-=q_+=q_0\ne r^2\), the ellipse must be the circle of squared radius \(q_0+r^2\).

The **only failure of one-circle recovery** is \(Q_r\equiv r^2\). Its complete fiber consists of all centered ellipses satisfying
\[
\frac1{a^2}+\frac1{b^2}=\frac1{r^2}.
\]
This is an infinite one-parameter family up to congruence, including the circle of radius \(\sqrt2r\). No observation of the full labeled function \(Q_r(n)\) at that one radius resolves this ambiguity.

**Minimum number of concentric measurement circles.** Fix \(0<s<r\), with the radius-\(r\) disk interior to the ellipse. The two *unlabeled* distributions \(\operatorname{Law}(Q_r)\) and \(\operatorname{Law}(Q_s)\) uniquely recover \(a,b\) for every ellipse in this class. Two distinct circles are necessary for a design that succeeds on every such ellipse, because at either individual radius the noncongruent resonance family has identical full angular product functions.

**Exact probability law.** If \(q_-<q_+\), the distribution is absolutely continuous, with
\[
f_{Q_r}(q)=\frac{\sqrt{(q_--r^2)(q_+-r^2)}}{\pi|q-r^2|\sqrt{(q-q_-)(q_+-q)}}\,,\qquad q_-<q<q_+.
\]
When the endpoints coincide, the law is the corresponding point mass. Moreover, its range width is exactly
\[
q_+-q_-=(a^2-b^2)\left|1-r^2\left(\frac1{a^2}+\frac1{b^2}\right)\right|.
\]
The zero factor quantifies the loss of sensitivity at the equipotential radius and shows that no uniform inverse-continuity estimate can extend over the resonant family.

## Assumptions and scope
The ellipse and the measurement disks have a common center; the center can be taken as the origin. The radius \(r\) is known, the disk lies strictly in the ellipse, and directions are Euclidean-uniform. Congruence identifies rotations, reflections, and translations; orientation of the principal axes is not recovered from unlabeled data. The theorem does **not** assert that two circles recover arbitrary convex bodies or off-center ellipses.

All displayed inversions use exact population distributions (equivalently their exact support endpoints). The one-circle minimality is a global statement over the full class of centered ellipses containing the chosen disk, not a claim that two radii are needed at a nonresonant ellipse.

## Proof
Let \(M\) be the positive-definite symmetric matrix defining the ellipse \(E=\{x:x^\mathsf TMx\le1\}\), with eigenvalues \(\alpha=1/a^2\) and \(\beta=1/b^2\), where \(0<\alpha\le\beta\). Put \(T=\alpha+\beta\). Choose any unit normal \(n\) and an orthogonal unit tangent \(v\). Points on the tangent line to the radius-\(r\) circle have the form \(rn+uv\). Their ellipse intersection parameter \(u\) satisfies
\[
(v^\mathsf TMv)u^2+2r(n^\mathsf TMv)u+(r^2n^\mathsf TMn-1)=0.
\]
Because \(r<b\), the constant term is negative; the two real roots have opposite signs. Vieta's identity therefore gives the unsigned product
\[
Q_r(n)=\frac{1-r^2n^\mathsf TMn}{v^\mathsf TMv}
=r^2+\frac{1-r^2T}{v^\mathsf TMv}. \tag{1}
\]
The second equality follows from \(n^\mathsf TMn+v^\mathsf TMv=T\). The Rayleigh quotient \(v^\mathsf TMv\) ranges over exactly \([\alpha,\beta]\). If \(a>b\) and \(1-r^2T\ne0\), (1) is strictly monotone in this quotient. Its two extremal products, at the principal-axis normals, are
\[
q_x=b^2-\frac{r^2b^2}{a^2},\qquad
q_y=a^2-\frac{r^2a^2}{b^2}.\tag{2}
\]
Direct subtraction gives
\[
q_y-q_x=(a^2-b^2)(1-r^2T),\qquad
\frac{q_y-r^2}{q_x-r^2}=\frac{a^2}{b^2}.\tag{3}
\]
Both deviations in the ratio share the sign of \(1-r^2T\), with the one corresponding to \(q_y\) farther from zero. Thus the endpoint closer to \(r^2\) is \(q_x\), and the farther is \(q_y\), irrespective of which is larger. Solving (2)–(3) yields the asserted inverse. A circle has \(v^\mathsf TMv\) constant and \(Q_r\equiv a^2-r^2\). For a noncircle, (1) is constant precisely when \(1-r^2T=0\); its value then equals \(r^2\). Conversely, any two positive eigenvalues summing to \(1/r^2\) define an ellipse strictly containing the radius-\(r\) disk, since each eigenvalue is strictly below \(1/r^2\). This proves the entire failure fiber and the point-mass classifications.

For the density, let \(\theta\) be uniform on \([0,2\pi)\). In a principal-axis frame,
\[
Z=v^\mathsf TMv=\alpha\sin^2\theta+\beta\cos^2\theta.
\]
For \(\alpha<\beta\), \(Z\) has the arcsine density \(1/[\pi\sqrt{(z-\alpha)(\beta-z)}]\) for \(\alpha<z<\beta\). With \(C=1-r^2T\ne0\), (1) is the monotone change of variables \(q=r^2+C/z\). Its Jacobian is \(|dz/dq|=|C|/(q-r^2)^2\). Substituting the two endpoint relations for \(z=\alpha,\beta\) and simplifying yields the displayed density, including the cases \(C>0\) and \(C<0\). This change of variables also proves normalization. Formula (3) yields the range-width identity.

Finally, two distinct radii \(s,r\) cannot both satisfy \(1-s^2T=1-r^2T=0\). If the ellipse is noncircular, its product law at at least one of those radii has nontrivial support and hence determines both axes by (2)–(3). If the ellipse is circular, each law is an atom and gives its radius. Necessity of two in a universal design follows from the infinite one-circle resonance fiber. The width identity gives a sequence of distinct ellipses with exactly equal data at resonance, precluding a single-valued continuous inverse there.

## Verification
The standalone `verify.py` checks the quadratic-intersection identity, the endpoint inverse on both sides of the equipotential radius, the resonance family, the two-radius separation, and normalization of the exact density by high-accuracy quadrature. These finite numerical and symbolic checks are supplementary; all quantified assertions follow from the displayed identities and arcsine change of variables.

## Relationship to prior work
González-García, Jerónimo-Castro, Jiménez-Desantiago and Morales-Amaya (2021) define equipotential circles and explicitly acknowledge that every noncircular ellipse has a unique equipotential circle. That **known** resonance phenomenon is not claimed as a new discovery here. Their article investigates which convex bodies have equipotential circles, not recovery of ellipse axes from the *unlabeled distribution or range* of nonconstant products, nor the sharp universal one-versus-two-circle measurement distinction.

Makai and Martini (2016) consider recovery of convex bodies from **tangent-section lengths**. A separate publicly available ellipse theorem, *Global planar Barker–Larman rigidity for arbitrary ellipses* (2026), proves injection of the fully **direction-labeled chord-length** function, allowing arbitrary ellipse centers. Chord length and the product of its two contact-point segments are different observables, and retaining angular labels is stronger than retaining only two endpoints of an unlabeled product distribution. The earlier injectivity statement does not supply the present product-range inversion or its resonance obstruction. An older conic-geometry source may conceivably have derived the same algebraic range reconstruction; absolute historical priority is not certified.

## Limitations
This is a complete exact inverse statement for concentric ellipses, not a statistical estimator with sample-size guarantees. A one-circle law is infinitely nonidentifying on the resonance family, and inverse conditioning necessarily deteriorates nearby. The joint use of two circles assumes their radii and common center are known. The known equipotential ellipse identity predates this analysis; novelty is limited to the distributional inverse classification, explicit endpoints, and two-circle universal design.

## References
1. I. González-García, J. Jerónimo-Castro, V. Jiménez-Desantiago and E. Morales-Amaya, *Convex bodies with equipotential circles*, arXiv:2107.11670v1, first public 24 July 2021, especially Section 1 and Theorem 1. https://arxiv.org/abs/2107.11670
2. E. Makai, Jr. and H. Martini, *Unique local determination of convex bodies*, arXiv:1602.00959v1, 2 February 2016, especially the introduction. https://arxiv.org/abs/1602.00959
3. *Global planar Barker–Larman rigidity for arbitrary ellipses*, public mathematical research record (2026). https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-global-planar-barker-larman-rigidity-for-arbitrary-ellipses--17ed1eab809b
