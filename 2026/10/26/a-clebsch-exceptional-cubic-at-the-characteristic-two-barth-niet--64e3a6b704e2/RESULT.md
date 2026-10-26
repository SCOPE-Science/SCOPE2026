# A Clebsch exceptional cubic at the characteristic-two Barth–Nieto quintic

## Finding

The coefficientwise characteristic-two reduction of the integral Barth–Nieto quintic has an isolated singular point whose projectivized tangent cone is the smooth Clebsch cubic surface. Its blowup resolves the isolated germ, the exceptional cubic has discrepancy zero, and the completed local Tjurina length is exactly \(16\).

More precisely, over an algebraically closed field \(k\) of characteristic \(2\), set
\[
N=V(e_1(X_0,\ldots,X_5),e_5(X_0,\ldots,X_5))\subset\mathbb P^5_k,
\]
where \(e_j\) is the degree-\(j\) elementary symmetric polynomial. Its entire **reduced** singular locus is
\[
\operatorname{Sing}(N)_{\mathrm{red}}=\{E\}\cup\bigcup_{|I|=3}L_I,
\qquad E=[1:1:1:1:1:1],\quad
L_I=\{e_1=0,\ X_i=0\ (i\in I)\}.
\]
There are exactly \(20\) distinct boundary lines, and \(E\) belongs to none of them. These lines have \(15\) intersection points, each with precisely two nonzero equal coordinates; each such point lies on four lines, and every line contains three of them. Thus the marked incidence configuration is \((15_4,20_3)\). The threefold is geometrically integral and normal.

## Assumptions and scope

The base field is any algebraically closed field of characteristic two. The equations above define the **specific integral symmetric model** of the Barth–Nieto quintic after coefficientwise reduction. The singular-locus equality is set-theoretic (equivalently, equality of reduced subschemes). At the distinguished point \(E\), the local Tjurina scheme is calculated scheme-theoretically.

## Proof

**1. Exhaustion of the singular locus.** Inside the hyperplane \(e_1=0\cong\mathbb P^4\), the hypersurface \(e_5=0\) is singular precisely where its six partial derivatives are all equal. Write \(P=\prod_{i=0}^5 X_i\). On the dense coordinate torus, \(e_5=P\sum_iX_i^{-1}\), so at a point of \(N\) on that torus,
\[
\frac{\partial e_5}{\partial X_i}=-\frac P{X_i^2}.
\]
Equality of all partials in characteristic two implies equality of the six coordinates, hence the sole torus singularity is \(E\). This point lies on \(N\), since \(6=0\) in characteristic two.

A point with exactly one zero coordinate is not on \(N\), since \(e_5\) is then the product of the five nonzero coordinates. At a point with exactly two zero coordinates, the only possibly nonzero partials occur at those zeros, and each equals the product of the four other nonzero coordinates; thus these partials are nonzero but some others vanish, and the point is smooth on \(N\). At a point with three or more zero coordinates, every partial of \(e_5\) vanishes, so the point is singular. Such points of \(e_1=0\) are exactly the union of the \(20\) lines \(L_I\): for a fixed triple of zero coordinates, the other three coordinates satisfy one independent linear equation and hence form a projective line. The points with four zero coordinates are the \(15\) points \(P_{ab}\) with \(X_a=X_b\ne0\) and all other coordinates zero. The incidence counts follow from choosing the triple of zeros among the four zero coordinates of \(P_{ab}\), and choosing the remaining pair among a line's three available coordinates.

**2. Exact local equation and smooth tangent cubic.** Work in \(X_5=1\) and write \(X_i=1+y_i\) for \(0\le i\le4\). The hyperplane equation is \(\sum_{i=0}^4 y_i=0\), so eliminate \(y_4=y_0+y_1+y_2+y_3\). Elementary-symmetric binomial expansion in characteristic two gives the exact identity
\[
e_5(1+y_0,\ldots,1+y_4,1)
=e_1(y_0,\ldots,y_4)+e_3(y_0,\ldots,y_4)+\prod_{i=0}^4y_i.
\]
Consequently the completed local equation is
\[
\widehat{\mathcal O}_{N,E}
\cong k[[y_0,y_1,y_2,y_3]]/(f),\quad
f=C+Q,\quad C=e_3(y_0,\ldots,y_4),\quad Q=\prod_{i=0}^4 y_i.
\]
Here \(C\) is homogeneous cubic and \(Q\) homogeneous quintic. Newton's identities on the linear hyperplane \(\sum y_i=0\) in characteristic two yield \(C=\sum_{i=0}^4y_i^3\). The projectivized tangent cone is therefore
\[
S=V(\textstyle\sum_{i=0}^4y_i,\ \sum_{i=0}^4y_i^3)\subset\mathbb P^4_k.
\]
If \(S\) were singular, the five squares \(y_i^2\) would all be equal by the Jacobian criterion. As the Frobenius square map is injective on a field, all five \(y_i\) would be equal; their sum is then that common value (since five is odd), forcing all to vanish. Hence \(S\) is smooth. This is the smooth characteristic-two diagonal Clebsch cubic surface.

**3. Resolution and discrepancy.** Blow up the origin in the four-dimensional smooth affine ambient space. In each standard chart, dividing the strict transform by the cube of the exceptional parameter gives a local equation of the form \(C(\mathbf z)+t^2Q(\mathbf z)=0\). Along the exceptional divisor \(t=0\), its gradient in the \(\mathbf z\) directions is nonzero because \(S\) is smooth. Thus the strict transform is smooth near the exceptional cubic and resolves the isolated germ at \(E\); the exceptional divisor is precisely \(S\). The canonical discrepancy for a degree-three hypersurface singularity in a smooth fourfold is \((4-1)-3=0\), by adjunction on the ambient blowup.

**4. Exact intrinsic local Tjurina length.** In the chosen four local variables the quadratic leading terms of \(f_{y_j}\), for \(0\le j\le3\), are \(C_{y_j}\). Since \(S\subset\mathbb P^3\) is smooth, the four quadratic partials have no common projective zero: Euler's identity for the cubic forces \(C=0\) whenever all four partials vanish. Therefore the four quadrics form a homogeneous regular sequence in \(k[y_0,\ldots,y_3]\). Their quotient has Hilbert series
\[
\frac{(1-t^2)^4}{(1-t)^4}=(1+t)^4
\]
and graded dimensions \((1,4,6,4,1)\), total length \(16\). The standard initial-regular-sequence lemma for the \(\mathfrak m\)-adic filtration applies to the actual partial derivatives \(f_{y_j}=C_{y_j}+Q_{y_j}\): because their leading forms constitute a regular sequence, the associated graded Jacobian quotient is the homogeneous quadratic complete intersection just computed. Thus its completed local length is exactly \(16\). Euler's identity for \(f=C+Q\), in characteristic two, reads
\[
\sum_{j=0}^3y_j f_{y_j}=3C+5Q=C+Q=f.
\]
Therefore \(f\) already lies in its Jacobian ideal, and the intrinsic Tjurina quotient has the same length \(16\). No finite point count is used to infer this local length.

**5. Geometric integrality and normality.** The complete singular support has dimension one; a reducible projective degree-five hypersurface in \(\mathbb P^4\) has distinct components intersecting in dimension at least two, and a generically nonreduced component is everywhere singular along a three-dimensional locus. Both contradict the proven singular support. Hence \(N\) is reduced and geometrically integral. A hypersurface is Cohen–Macaulay, so \(N\) satisfies Serre's \(S_2\); its singular locus has codimension at least two, giving \(R_1\). Thus \(N\) is geometrically normal.

## Verification

The standalone Python program `verify.py` uses integer arithmetic and sparse polynomials over \(\mathbb F_2\). It checks the exact local identity, the four-variable Euler relation, the quadratic gradient relations, and the homogeneous Jacobian Hilbert function \((1,4,6,4,1,0,0)\) through degree six. It exhaustively enumerates the \(31\) rational points of the containing hyperplane over \(\mathbb F_2\), including the \(16\) singular rational points, and verifies the \((15_4,20_3)\) boundary incidence. As an additional finite-field consistency check it examines all \(85\) points of \(\mathbb P^3(\mathbb F_4)\) for tangent-cone singularities. Smoothness over the algebraic closure and completeness of the singular locus follow from the algebraic arguments above, **not** from finite enumeration.

Reproduce using `python3 verify.py` with Python 3 and no external dependencies.

## Relationship to prior work

The characteristic-zero Barth–Nieto quintic is classically known to have ten isolated Segre nodes together with twenty singular lines [1,2]. The ten node coordinates, obtained from three plus signs and three minus signs, all specialize to \(E\) in characteristic two, but that coordinate coincidence alone does not determine the local scheme or its Tjurina length. The present claim is about the **characteristic-two special fibre** and its precise local singularity. The appearance of the abstract smooth characteristic-two Clebsch cubic is consistent with the separate classification in [3]; that classification does not by itself establish its occurrence as this tangent cone. Earlier accounts of the integral model and its modular geometry do not, in the portions inspected, provide this specific degeneration and local calculation. The original 1994 article [4] was not available for complete examination and could contain related formulations.

## Limitations

The Jacobian scheme along the twenty boundary lines is not classified beyond reduced support. The blowup is proved to resolve the **germ at** \(E\), not to resolve the entire threefold or determine a global semistable arithmetic model. The special fibre may differ from reductions of other birational models. Related earlier modular treatments could overlap; independent verification has not been performed.

## References

[1] K. Hulek, I. Nieto, G. K. Sankaran, *Heisenberg-invariant Kummer surfaces*, arXiv:alg-geom/9712025 (first public 1997-12-19).

[2] K. Hulek, J. Spandaw, B. van Geemen, D. van Straten, *The modularity of the Barth–Nieto quintic and its relatives*, arXiv:math/0010049 (first public 2000-10-05).

[3] I. Dolgachev, A. Duncan, *Automorphisms of cubic surfaces in positive characteristic*, arXiv:1712.01167, especially characteristic-two Clebsch and Fermat cubic surfaces.

[4] W. Barth, I. Nieto, *Abelian surfaces of type (1,3) and quartic surfaces with 16 skew lines*, Journal of Algebraic Geometry 3 (1994), 173–222 (full original text not inspected).
