# Branch geometry and full symmetric monodromy of the Shi–Xu–Zuo polynomial map

## Finding
Consider the polynomial morphism over \(\mathbb C\)
\[
F:\mathbb A^3_{x,y,z}\longrightarrow\mathbb A^3_{a,b,c},\quad
(a,b,c)=(y,zy-x^2,z^2+x^2y+zy^2+x^3).
\]
It is finite flat of degree \(4\). Its reduced critical divisor is the union of the two smooth affine planes
\[
E_1=\{x=0\},\qquad E_2=\{3xy+4y^2+4z=0\}.
\]
The reduced branch locus consists of exactly two distinct irreducible hypersurfaces, \(B=0\) and \(R=0\), given below. The first is a Whitney umbrella with a single pinch point at the origin and a line of ordinary double crossings away from that point. The global geometric monodromy group of the associated generically étale degree-four covering is the full symmetric group \(S_4\).

## Assumptions and scope
Everything is over the algebraically closed field \(\mathbb C\) of characteristic zero. A branch point means a target point above which \(F\) is not étale, equivalently a point of the finite image of its critical divisor. Statements about the branch locus refer to its reduced hypersurface structure. Geometric monodromy is the image of the fundamental group of the complement of the branch locus acting on a geometric four-point fiber. The separate Bernstein–Sato ideal of the polynomial tuple is not computed here.

Put
\[
B(a,b,c)=b^2+a^3b-a^2c.
\]
For \(t\) an indeterminate, define
\[
\beta(a,t)=-t^2-\tfrac34a^2t-a^3,\qquad
\gamma(a,t)=t^3+(a+\tfrac9{16}a^2)t^2+\tfrac34a^3t.
\]
Define the second polynomial canonically by the following exact resultant (with the conventional normalization specified):
\[
R(a,b,c)=256\operatorname{Res}_t\bigl(\beta(a,t)-b,\gamma(a,t)-c\bigr).
\]
It is a polynomial over the integers and obeys \(R(0,b,c)=-256(b^3+c^2)\). Its coefficient of \(c^2\) is the nonzero constant \(-256\). The standalone verifier evaluates the complete polynomial explicitly.

## Proof
**(1) Finiteness and degree.** Write \(a=y\) and \(b=az-x^2\). From \(az=x^2+b\) and the third defining equation, direct multiplication by \(a^2\) gives the monic relation
\[
P_{a,b,c}(x)=x^4+a^2x^3+2(b+a^3)x^2+b^2+a^3b-a^2c=0.
\]
The defining equation for the third target coordinate also gives the monic relation
\[
z^2+a^2z+ax^2+x^3-c=0.
\]
Thus both \(x\) and \(z\) are integral over \(\mathbb C[a,b,c]\), so \(F\) is finite. Over \(a\ne0\), the formula \(z=(x^2+b)/a\) identifies its fiber with the quartic equation \(P=0\). This quartic is generically separable (see the discriminant below), so the generic degree is \(4\). The target is regular, while the finite source ring \(\mathbb C[x,y,z]\) is Cohen–Macaulay of dimension \(3\). Finite miracle flatness makes this morphism flat, hence its finite locally free degree is four everywhere.

**(2) Critical and branch components.** The exact determinant of the Jacobian matrix with target coordinates \((a,b,c)\) is
\[
\det(dF)=x(3xy+4y^2+4z).
\]
The two factors define smooth distinct planes. On \(E_1\), putting \(y=a,x=0\) yields \(b=az\) and \(c=z^2+a^2z\), whence \(B=0\). The map \(E_1\to V(B)\) is generically one-to-one for \(a\ne0\), so its image is exactly the irreducible surface \(V(B)\), by finiteness of \(F\).

On \(E_2\), write \(x=t\), \(y=a\), and \(z=-\tfrac34at-a^2\). Substitution gives precisely \(b=\beta(a,t)\) and \(c=\gamma(a,t)\). Their elimination yields \(R=0\). The polynomial \(R\) is irreducible: because its coefficient of \(c^2\) is a nonzero constant, a nontrivial factorization would specialize at \(a=0\) to a nontrivial factorization (in positive \(c\)-degrees) of \(b^3+c^2\). The latter is irreducible in \(\mathbb C[b,c]\). Any factor of \(c\)-degree zero would divide that constant leading coefficient and hence be a unit. As \(E_2\) has dimension \(2\), its image is a surface: for fixed \(a\), \(\beta\) is a nonconstant quadratic and its fibers are finite, so the image has dimension \(2\). Thus \(F(E_2)=V(R)\). The components are distinct since \(B(0,b,c)=b^2\) and \(R(0,b,c)=-256(b^3+c^2)\). By the exact Jacobian factorization and finiteness, the reduced branch locus is \(V(BR)\), with no extra component on \(a=0\).

Equivalently, over \(a\ne0\), direct quartic discriminant calculation gives
\[
\operatorname{Disc}_T P_{a,b,c}(T)=-a^4B(a,b,c)R(a,b,c).
\]
The factor \(a^4\) is an artifact of eliminating \(z\) using division by \(a\), not an additional branch divisor.

**(3) Pinch geometry.** The polynomial change of target coordinate \(w=c-ab\) transforms the first branch equation to \(B=b^2-a^2w\). This is the standard pinch-point/Whitney-umbrella equation. Its singular locus is \(a=b=0\). On the open subset \(w\ne0\), adjoining a local analytic square root of \(w\) decomposes the germ into two transverse sheets. At \(w=0\) these sheets pinch, yielding exactly one pinch point, at \((a,b,c)=(0,0,0)\).

**(4) Full monodromy.** Restrict the map to the target affine line \(a=1,b=0\), parametrized by \(c\). On its inverse image, \(y=1,z=x^2\), so this restricted degree-four cover is the polynomial map \(c=f(x)=x^4+x^3+2x^2\). Its derivative \(f'(x)=x(4x^2+3x+4)\) has three distinct roots. Its discriminant is
\[
\operatorname{Disc}_T(T^4+T^3+2T^2-c)=-c(256c^2+251c+224),
\]
with three distinct roots because \(251^2-4\cdot256\cdot224=-166375\ne0\), and the quadratic has nonzero constant term. Thus the restricted connected polynomial cover has three distinct simple branch values, each giving a transposition. Monodromy is transitive (the source affine line is connected), and the group generated by transpositions acting transitively on four letters is \(S_4\). Its monodromy is a subgroup of that of \(F\), so the latter is also \(S_4\).

## Verification
The supplied independent symbolic replay recomputes the Jacobian determinant, both monic relations, the resultant defining \(R\), its relevant coefficients and specialization, the quartic discriminant and its factorization, and the three distinct simple branch values on \(a=1,b=0\). Run \(\texttt{python verify_branch.py}\) with SymPy installed. The symbolic checks support, rather than replace, the general algebraic arguments given above.

## Relationship to prior work
Shi, Xu and Zuo introduced this explicit polynomial map in their study of nonlinear zero loci of Bernstein–Sato ideals (arXiv:2610.04408v1, Theorem 1.2, first public October 3, 2026). Their paper concerns the Bernstein–Sato ideal and does not give the finite-cover degree, ramification components, branch-surface equations or covering monodromy reported here. Standard facts about finiteness, discriminants, pinch points, miracle flatness and transposition monodromy supply the methods; no novelty is asserted for these classical facts. Related database records on unrelated quartic discriminants and singular schemes do not imply these assertions for this particular morphism.

## Limitations
The branch locus is classified only with reduced scheme structure; its scheme-theoretic branch multiplicities, the singularities of the second irreducible component \(V(R)\), the intersection curve \(V(B,R)\), and local inertia at every stratum are not classified. No claim is made concerning the explicit generators of the Bernstein–Sato ideal. Priority is assessed against accessible literature and mathematical records, not certified exhaustive.

## References
1. Quan Shi, Yongxin Xu and Huaiqing Zuo, *Zero loci of Bernstein-Sato ideals are not necessarily linear*, arXiv:2610.04408v1 (October 3, 2026), Theorem 1.2.
2. Standard finite-morphism and miracle-flatness criteria; standard quartic discriminant, Whitney-umbrella, and covering-monodromy theory.
