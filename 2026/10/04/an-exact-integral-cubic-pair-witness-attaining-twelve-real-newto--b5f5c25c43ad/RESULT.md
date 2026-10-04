# An exact integral cubic-pair witness attaining twelve real Newton singular starts
## Finding
Consider the real cubic system
\[
F_1(x,y)=-9000x^3-13498x^2y+2999x^2-6500xy^2+4499xy+2001x-1000y^3+1498y^2+998y+2,
\]
\[
F_2(x,y)=-2000x^3-7999x^2y-6002xy^2-12002xy+7998x-11999y^2+7998y-2.
\]
For the Newton-homotopy critical system
\[
\gamma_1=\partial_xF_1\,F_2-\partial_xF_2\,F_1,
\qquad
\gamma_2=\partial_yF_1\,F_2-\partial_yF_2\,F_1,
\]
let
\[
S=V_{\mathbf R}(\gamma_1,\gamma_2)\setminus V_{\mathbf R}(F_1,F_2).
\]
Then
\[
\#S=12.
\]
All twelve corresponding singular members of the cubic pencil are nodal, their singular points are affine and real, and their pencil parameters are pairwise distinct. Thus this explicit integral pair attains the cubic--cubic singular-start bound
\[
3(3-1)^2=12
\]
from Theorem 41 of Buettner--Hauenstein--Hills--Hong--Ponce Carrion--Schmidt.

## Assumptions and scope
The source studies bivariate Newton homotopies
\[
H(z,r;t)=F(z)-tF(r)
\]
and, for equal degrees, identifies singular starts by the critical system \(\gamma\). Its genericity hypotheses require smooth generator curves, a transverse complete-intersection base locus, the expected degree at infinity, and at most one ordinary double point on a singular Newton curve.

For this pair those hypotheses are checked exactly, not sampled numerically. The projective closures of \(F_1=0\) and \(F_2=0\) are smooth cubics; their nine base points are simple, transverse, and all real. Every singular member relevant to \(S\) has one nondegenerate affine node, and no pencil member is singular at infinity.

The classification \(14Q30\) is used because the initiating work and the present statement are explicitly about computational real algebraic geometry.

## Proof
Let
\[
R_F(y)=\operatorname{Res}_x(F_1,F_2).
\]
Exact elimination gives
\[
\deg R_F=9.
\]
The polynomial \(R_F\) is squarefree and has nine real roots. A lexicographic Gröbner basis for \((F_1,F_2)\) is in shape position, with one polynomial linear in \(x\) and one univariate polynomial in \(y\). Hence each root of \(R_F\) determines exactly one base point. The Jacobian determinant
\[
J=\det\begin{pmatrix}
\partial_xF_1&\partial_yF_1\\
\partial_xF_2&\partial_yF_2
\end{pmatrix}
\]
has no common zero with \(F_1,F_2\), so all nine base points are transverse.

Now set
\[
R_\gamma(y)=\operatorname{Res}_x(\gamma_1,\gamma_2).
\]
Exact elimination gives
\[
\deg R_\gamma=21,
\]
and \(R_\gamma\) is squarefree with twenty-one real roots. Because every base point annihilates \(\gamma\), one has an exact division
\[
R_\gamma=R_F\,Q
\]
up to a nonzero rational scalar, where \(Q\) has degree twelve. The verifier proves that \(Q\) is squarefree, coprime to \(R_F\), and has twelve real roots. A lexicographic Gröbner basis for \((\gamma_1,\gamma_2)\) is again in shape position. Therefore those twelve roots correspond bijectively to twelve real points of \(S\).

It remains to verify the source's local genericity conditions. Reducing \(F_2\) modulo the Gröbner basis of \((\gamma_1,\gamma_2)\) and taking the greatest common divisor with \(Q\) shows that \(F_2\) is nonzero at every point of \(S\). Thus the pencil parameter
\[
\lambda=F_1/F_2
\]
is well-defined there.

For \(p\in S\), the corresponding pencil member is
\[
h_p=F_2(p)F_1-F_1(p)F_2.
\]
The determinant of its Hessian at the singular point is obtained by evaluating
\[
D=\det\!\left(F_2\operatorname{Hess}(F_1)-F_1\operatorname{Hess}(F_2)\right).
\]
After reduction modulo \((\gamma_1,\gamma_2)\), the resulting univariate polynomial is coprime to \(Q\). Hence all twelve singularities are ordinary nodes.

Finally, eliminating \(y\) from \(Q(y)\) and the reduced equation \(F_1-\lambda F_2\) produces a degree-twelve polynomial in \(\lambda\). It is squarefree and has twelve real roots, so the twelve singular starts have pairwise distinct real critical values. A separate projective calculation with the degree-three and degree-two homogeneous parts of \(F_1,F_2\) shows that the equations for a singular point on the line at infinity have no projective solution. Therefore every singular pencil member has exactly the single affine node already counted.

Thus
\[
\#S=12=3(3-1)^2.
\]

## Verification
The accompanying `verify.py` carries out the proof over \(\mathbf Q\) with exact polynomial arithmetic. It checks unit Jacobian ideals for affine smoothness, squarefreeness of the leading binary cubics, absence of pencil singularities at infinity, transverse base points, shape-position Gröbner bases, exact resultant degrees, exact real-root counts, the quotient eliminant \(Q\), nonvanishing of the nodal Hessian determinant on \(S\), and distinctness of the twelve critical values.

Real-root counts are exact algebraic root counts, not floating-point sampling. Since each relevant eliminant is squarefree and its degree equals its exact number of real roots, no uncounted complex roots remain.

The saved verifier replay ends in `VERIFY_OK`.

## Relationship to prior work
Buettner--Hauenstein--Hills--Hong--Ponce Carrion--Schmidt prove
\[
\#S\le 3(d-1)^2
\]
when the two bivariate polynomials have equal degree \(d\). They give sharp examples for degree pairs \((2,1)\), \((2,2)\), \((3,1)\), and \((3,2)\), and explicitly leave open whether sharp examples exist for all degree pairs. Their displayed examples do not include a cubic--cubic pair.

The existence of real pencils of plane cubics with all twelve singular members real is classical and is not claimed here as new. In particular, real enumerative-geometry literature and the later classification of real cubic pencils explain why the number twelve is geometrically natural. Those sources do not state the integral pair above or certify its Newton-homotopy start locus through the exact affine elimination and genericity checks used here.

The contribution is therefore coefficient-level and reproducible: it supplies an explicit integral \((3,3)\) witness in the normalization used by the 2026 Newton-homotopy framework and an exact certificate that all twelve starts and all twelve critical values are real and simple.

## Limitations
This result does not settle the source's open sharpness question for arbitrary degree pairs. It handles one previously untabulated pair, \((3,3)\).

The coefficients were obtained by perturbing a real line-arrangement pencil and then certifying the resulting pair exactly; no minimality or optimality of the coefficient heights is claimed. Classical theory already gives broad existence of totally real cubic pencils, so novelty is restricted to this explicit integral witness and its exact Newton-homotopy certificate.

The verifier establishes the stated facts for this pair only. It does not infer a perturbation theorem for neighborhoods of these coefficients.

## References
1. J. Buettner, J. D. Hauenstein, C. Hills, H. Hong, F. Ponce Carrion, E. L. Schmidt, *Geometry of Newton homotopies: bivariate case*, arXiv:2609.30189v1, 2026.
2. F. Sottile, *Enumerative Real Algebraic Geometry*, 2001, discussion of real pencils of cubics and twelve real rational cubics.
3. S. Fiedler-Le Touzé, *Pencils of Cubics and Algebraic Curves in the Real Projective Plane*, CRC Press, 2019, especially the degree-twelve discriminant and real singular-pencil discussion.
