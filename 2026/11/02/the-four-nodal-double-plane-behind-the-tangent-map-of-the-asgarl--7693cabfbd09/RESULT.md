# The four-nodal double plane behind the tangent map of the Asgarli–Ghioca curve

## Finding
Let \(k\) be any field of characteristic different from \(2\) and \(3\), and put \(s=x+y+z\). The rational map
\[
\Phi:\mathbf P^2\dashrightarrow\mathbf P^2,\qquad [x:y:z]\longmapsto[yz(3x-s):xz(3y-s):xy(3z-s)]
\]
which records tangents at the smooth rational points of the Asgarli–Ghioca plane curve is the anticanonical map of the blowup of seven explicit points. Its Stein factor is the normal degree-two del Pezzo surface
\[
Y:\quad w^2=(ab+ac+bc)^2-3abc(a+b+c)\subset\mathbf P(1,1,1,2).
\]
Over an algebraic closure, its branch quartic is the union of two smooth conics meeting transversely at exactly four points; hence \(Y\) has exactly four ordinary double points of type \(A_1\). The blowup of the seven points gives the minimal resolution of \(Y\), contracting the strict transforms of four lines, each of self-intersection \(-2\). For every finite field \(\mathbb F_q\) of characteristic greater than \(3\), the number of rational points of the branch quartic is exactly \(4\) if \(q\equiv2\pmod3\), and \(2q-2\) if \(q\equiv1\pmod3\).

## Assumptions and scope
Coordinates \([a:b:c]\) are coordinates on the target dual plane, and \(w\) has weight two. The seven source points are \([1:0:0],[0:1:0],[0:0:1],[0:1:-1],[1:0:-1],[1:-1:0],[1:1:1]\). The asserted resolution and singularity type are geometric statements over \(\bar k\); the displayed equations are defined over \(k\). If \(\mathbb F_q\) occurs, \(q\) is a prime power of characteristic greater than \(3\). The tangent interpretation requires the rational smooth points of the particular degree-\(q-1\) plane curve \(x^{q-1}+y^{q-1}+z^{q-1}-3(x+y+z)^{q-1}=0\), as in the cited primary source; the del Pezzo theorem concerns the fixed cubic rational map, not that curve's full geometric Gauss map.

## Proof
Write \(F_1=yz(3x-s)\), \(F_2=xz(3y-s)\), \(F_3=xy(3z-s)\). If \(xyz\ne0\), the common-zero equations force \(3x=3y=3z=s\), giving the single base point \([1:1:1]\). On a coordinate line, their common zeros are its two coordinate vertices and its intersection with \(s=0\); thus the seven points listed above exhaust the base locus. Their local linear terms generate the maximal ideal (at the three vertices from the other two cubics, at the three diagonal intersections from a transverse coordinate and \(s\), and at \([1:1:1]\) from the two independent differences). All seven are reduced simple base points. Evaluation of ten degree-three monomials at them has rank seven, so the three independent cubics \(F_i\) form the complete net of cubics through the base points. After blowing up, it is the base-point-free anticanonical system \(|-K_X|\), and \(K_X^2=9-7=2\).

To determine the generic degree, use affine source chart \(s=1\), and let a generic target point be \([a:b:c]\). There is a scalar \(\lambda\) with \(3-1/x=\lambda a\), \(3-1/y=\lambda b\), and \(3-1/z=\lambda c\). Therefore \(x=(3-\lambda a)^{-1}\), etc. The relation \(x+y+z=1\), on multiplying by the three denominators, is
\[
\lambda\bigl(abc\lambda^2-2(ab+ac+bc)\lambda+3(a+b+c)\bigr)=0.
\]
The factor \(\lambda=0\) corresponds to \([1:1:1]\), an excluded base point. Hence the degree-two extension has discriminant, up to the square factor \(4\),
\[
B=(ab+ac+bc)^2-3abc(a+b+c).
\]
Its integral closure over the target is the double-plane hypersurface \(Y:w^2=B\). In particular, the degree-two map is separable, and \(Y\) is rational since it has the function field of the source plane. Its weighted adjunction gives \(-K_Y=\mathcal O_Y(1)\) and \((-K_Y)^2=2\).

Let \(\omega^2+\omega+1=0\) with \(\omega\ne1\). Expanding using that relation gives the exact factorization
\[
B=(ab+\omega ac+\omega^2bc)(ab+\omega^2ac+\omega bc).
\]
Each factor is a nonsingular ternary quadratic form (all three off-diagonal coefficients are nonzero, with determinant nonzero in characteristic other than two). Subtracting the two factors and imposing either one shows their intersection is precisely \([1:0:0],[0:1:0],[0:0:1],[1:1:1]\). Their linear gradients are independent at those four points; Bézout's theorem also supplies intersection number four. Therefore \(B=0\) has exactly four transverse ordinary nodes and no other singularities. In local coordinates \(u,v\) for the two conic branches, \(Y\) has equation \(w^2=uv\), an \(A_1\) singularity.

The four source lines \(x=0\), \(y=0\), \(z=0\), and \(s=0\) each contain exactly three of the seven base points. Their strict transforms on \(X\) are disjoint smooth rational curves of self-intersection \(1-3=-2\), and \((-K_X)\) has degree zero on them. The cubic map contracts each; their images are respectively the four nodes of \(Y\). The normal double cover has no other singularities, so the induced birational morphism \(X\to Y\) resolves precisely those four nodes. Since \(A_1\) resolutions are unique minimal resolutions and these are \(-2\)-curves, this is the minimal resolution.

For the arithmetic statement, Frobenius fixes the two branch conics separately if and only if \(\omega\in\mathbb F_q\), equivalently \(q\equiv1\pmod3\). Then each conic has \(q+1\) rational points and their four rational intersections are counted twice, yielding \(2(q+1)-4=2q-2\). If \(q\equiv2\pmod3\), Frobenius exchanges the conics, so the rational points of their union lie in their intersection, which consists of the four displayed rational points. This proves the formulas.

## Verification
The exact factorization follows by substitution \(\omega^2=-\omega-1\); the source base locus, full cubic-net rank, and inverse quadratic are explicit computations detailed in the proof. The accompanying standalone finite-field checker enumerates rational branch points and target tangent multiplicities for \(q=5,7,11,13,17,19,23,25,31,49\); the tangent multiplicity checks are corroboration of previously known arithmetic, not part of the novelty claim. It prints `TANGENT_FILLING_DOUBLE_PLANE_CHECKS_PASS`. Finite tests are not a proof of the statements for arbitrary fields.

## Relationship to prior work
Asgarli and Ghioca introduced the plane curve and derived the tangent formula and its tangent-filling property. The complete one-/two-contact tangent statistics and a rational deck involution have also already been recorded for this family; neither is claimed new. The classical degree-two del Pezzo/Geiser construction gives general structure for blowups of seven points. The additional claim here is the exact special seven-point anticanonical model, split-conic factorization of its branch quartic, precise four-node resolution, and uniform arithmetic branch-point count. These are not consequences of the mere number of rational tangent contacts, although the previously known explicit involution motivates the comparison.

## Limitations
The result does not compute the full moduli of the singular del Pezzo, all degenerations in characteristics two or three, or the geometric Gauss map of the high-degree plane curve outside its rational smooth locus. Prior literature on special Geiser involutions and the complete source paper may contain equivalent coordinate presentations; novelty has not been independently audited. The point count concerns the branch quartic, not the total number of points of \(Y\).

## References
Asgarli, S., and Ghioca, D., *Tangent-filling plane curves over finite fields*, arXiv:2302.13420, first version publicly posted February 26, 2023. Classical facts on anticanonical maps of weak degree-two del Pezzo surfaces, separable double covers, and rational double points are used only in their standard form.
