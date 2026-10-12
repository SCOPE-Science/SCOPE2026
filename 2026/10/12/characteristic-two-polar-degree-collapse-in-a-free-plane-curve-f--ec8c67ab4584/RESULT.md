# Characteristic-two polar-degree collapse in a free plane-curve family

## Finding
Let \(m\ge2\) be an integer, and set
\[
A_m=x^m y^m+y^m z^m+x^m z^m,\qquad
B_m=x^m+y^m,\qquad C_m=y^m+z^m,\qquad F_m=A_m B_m C_m.
\]
For the polar/gradient rational map \(\Phi_{F_m}=[(F_m)_x:(F_m)_y:(F_m)_z]\), cancel the common factor of its three homogeneous coordinates, and measure degree by the total generic function-field degree, **including inseparable multiplicity**.

Over an algebraically closed field of characteristic two, when \(m\) is even all three partial derivatives vanish. When \(m\ge3\) is odd, the defining polynomial is reduced and the map is dominant, with
\[
\boxed{\deg\Phi_{F_m}=2m-2.}
\]
It is generically inseparable. The exact base scheme of its reduced polynomial coordinate system \(\nabla P_m\), where \(P_m=B_mC_m\), has three vertices of lengths \((m-1)^2\) and \(m^2\) transverse pencil intersections of length one. In characteristic zero the corresponding degree is \(2m^2+2m-2\); the characteristic-zero singularity counts needed for that comparison have been established previously. The characteristic-two drop is therefore \(2m^2\) for every odd \(m\ge3\).

## Assumptions and scope
Work over an algebraically closed field \(k\). In characteristic two, all polynomial equalities are in \(k[x,y,z]\), and the assertions for odd \(m\) require \(m\ge3\). The map is a rational map on \(\mathbb P^2_k\); base-point lengths mean dimensions of its localized projective base-scheme rings. The gradient map of an equation with identically zero derivatives is undefined; this should not be confused with the polar map of its reduced support.

## Proof
**1. The characteristic-two cancellation.** In characteristic two, direct expansion gives
\[
A_m=B_mC_m+y^{2m}.
\]
Writing \(P_m=B_mC_m\), it follows that
\[
F_m=P_m^2+y^{2m}P_m,\qquad
\nabla F_m=y^{2m}\nabla P_m.
\]
If \(m\) is even, \(F_m\) is a square (all exponent vectors are even), and its gradient is identically zero. For odd \(m\),
\[
\nabla P_m=\big(x^{m-1}C_m,\ y^{m-1}(x^m+z^m),\ z^{m-1}B_m\big).
\]
The three displayed coordinates have no nonconstant common factor: the first and third already are coprime, as \(x,z,B_m,C_m\) have no common irreducible factor in the indicated combination. Thus the cancelled polar map is exactly \(\Phi_{P_m}\).

**2. Reducedness.** For odd \(m\), \(B_m\) and \(C_m\) are products of \(m\) distinct lines and are coprime. The polynomial \(A_m\) is irreducible: over \(k(x,y)\) it gives \(z^m=x^my^m/(x^m+y^m)\). At any simple prime divisor of \(x^m+y^m\), the rational function on the right has valuation \(-1\). A root of this equation therefore has valuation \(-1/m\), forcing ramification index at least \(m\), and hence field degree \(m\). This proves irreducibility. Restricting \(A_m\) to any line factor of \(B_m\) or \(C_m\) gives a nonzero monomial, so these factors are coprime to \(A_m\). Thus \(F_m\) is reduced.

**3. Complete polar base scheme.** Let \(J=( (P_m)_x,(P_m)_y,(P_m)_z )\). A point with all coordinates nonzero belongs to \(V(J)\) exactly when \(B_m=C_m=0\). In the affine chart \(y=1\), these are the \(m^2\) distinct points \([a:1:b]\) with \(a^m=b^m=1\). The local parameters \(B_m,C_m\) meet transversely because \(m\) is odd, so the localized gradient ideal equals \((B_m,C_m)\); each contributes length one. On the coordinate axes, the only additional base points are \([1:0:0],[0:1:0],[0:0:1]\). At each, two of the three gradient entries generate a local ideal of the form \((u^{m-1},v^{m-1})\) times units; the third entry lies in that ideal. Hence each vertex has base length \((m-1)^2\). Note that \(P_m(0,1,0)=1\), so the middle vertex is an off-divisor gradient base point for \(P_m\).

**4. Degree and dominance.** The three coprime gradient coordinates have degree \(2m-1\), and their base scheme is finite. Two general polar members therefore meet, by Bézout, with total intersection number \((2m-1)^2\). At each base point the two general members locally generate the displayed complete-intersection ideal, so their total fixed intersection length is
\[
3(m-1)^2+m^2.
\]
The residual intersection multiplicity is
\[
(2m-1)^2-3(m-1)^2-m^2=2m-2>0.
\]
If the gradient image had dimension less than two, two general polar members would have no residual intersections outside the base; therefore the map is dominant. For a dominant rational map between projective planes, the residual intersection number is its total function-field degree. This proves the stated formula even when its generic fiber is nonreduced.

**5. Inseparability.** In characteristic two, the Hessian \(H(P_m)\) is alternating, with zero diagonal and off-diagonal entries
\[
H_{xy}=(xy)^{m-1},\qquad H_{xz}=(xz)^{m-1},\qquad H_{yz}=(yz)^{m-1}.
\]
Thus it has rank exactly two at a generic point. Euler's identity differentiated once gives \(H(P_m)(x,y,z)^T=\nabla P_m\), because \(\deg P_m=2m=0\) in \(k\). Upon passing to projective tangent spaces, the gradient differential has rank exactly one, not two. Therefore the dominant gradient map is not generically separable.

**6. Characteristic-zero reference value.** The known complex singularity basket has two tangent-pencil centers, an ordinary \(m\)-fold vertex and \(m^2\) nodes. At each center, the union of two local ordinary \(m\)-fold components meets with intersection multiplicity \(2m^2\), so its Milnor number is \(2(m-1)^2+4m^2-1\). Hence the total Milnor number is \(14m^2-10m+3\). The standard characteristic-zero polar-degree formula yields
\[
(4m-1)^2-(14m^2-10m+3)=2m^2+2m-2.
\]
This complex calculation is included for comparison only; the complex basket is established in earlier work.

## Verification
The accompanying `verify.py` uses exact binary-field arithmetic. For \(m=3,5,7\), it checks the characteristic-two polynomial identity, the complete projective base-point support over a splitting field for the \(m\)-th roots of unity, and the predicted local-length arithmetic. It separately checks the characteristic-zero numerical Milnor/polar-degree identity for \(2\le m\le8\). The proof of the infinite family does **not** extrapolate from these finite computations.

Run with a Python 3 standard-library interpreter: `python verify.py`.

## Relationship to prior work
Dimca–Ilardi–Pokora–Sticlaru introduced the complex family, proved its freeness in Theorem 1.8, and supplied characteristic-zero Jacobian syzygies. Previously established refinements determine the complex local singularity basket, Milnor numbers and resolution. Those results imply the displayed characteristic-zero polar degree and are **not** claimed here as discoveries. The new result is the exact characteristic-two collapse of the *same integral equation*, its complete residual gradient-base scheme, its total rational-map degree, and generic inseparability. The cancellation to a two-pencil gradient system explains the reduction rather than merely illustrating it in small characteristics.

## Limitations
The claim concerns the fixed integral model and the original polynomial gradient map, not arbitrary projective models or replacements by the reduced support when \(m\) is even. No formula is asserted for odd prime characteristics or for the separable and purely inseparable degrees separately. The degree counts scheme multiplicities in the generic fiber; it is not a count of distinct geometric inverse images. No independent external validation or exhaustive publication-priority determination is claimed.

## References
Dimca, A.; Ilardi, G.; Pokora, P.; Sticlaru, G., *Construction of free curves by adding lines to a given curve*, arXiv:2301.01117v1 (first posted 2023-01-03), particularly Theorem 1.8, §4.7 and Remark 4.8; DOI:10.1007/s00025-023-02036-9.

Classical polar-degree formula for complex reduced plane curves with isolated singularities: \(\deg\nabla F=(\deg F-1)^2-\sum\mu_p\). The geometric local singularity basket used above is also recorded in the prior complex-family study associated with arXiv:2301.01117.
