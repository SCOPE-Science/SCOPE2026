# An infinitesimally full but pointwise parabolic automorphism scheme for the characteristic-two Witt algebra

## Finding
Let \(k\) be **any** field of characteristic \(2\), and put \(A=k[x,y]/(x^2,y^2)\), \(W=\operatorname{Der}_k(A)\), and \(V=A/k1\). Then the affine automorphism group **scheme** \(\mathcal G=\underline{\operatorname{Aut}}_k(A)\) has the coordinate presentation
\[
\mathcal G\cong\operatorname{Spec}\bigl(k[a,b,f,g,s,t,c,e,(ag+bf)^{-1}]/(c^2,e^2)\bigr)
\]
where this is an isomorphism of **schemes**, not a direct-product description of the group law. In particular,
\[
\mathcal G\cong\operatorname{GL}_{2,k}\times\mathbb A_k^2\times\operatorname{Spec}(k[c,e]/(c^2,e^2))
\]
as schemes; its reduced group has dimension \(6\), while its tangent Lie algebra has dimension \(8\). The natural homomorphism \(\mathcal G\to\operatorname{PGL}(V)\) has geometric-point image exactly the maximal parabolic preserving the line \(k\overline{xy}\), but its differential is an isomorphism onto \(\mathfrak{pgl}(V)\). Thus this subgroup scheme has a **proper reduced image** and nevertheless an **infinitesimally surjective** map to \(\operatorname{PGL}_3\).

## Assumptions and scope
The base \(k\) is an arbitrary field of characteristic \(2\), not necessarily algebraically closed or finite. Every functor-of-points assertion concerns a **commutative** \(k\)-algebra \(R\). The quotient \(V=A/k1\) is a three-dimensional \(k\)-space; the phrase image on geometric points refers to field-valued points after algebraic extension. No assertion of global or scheme-theoretic surjectivity is made. The subgroup of \(\operatorname{PGL}(V)\) on points is specified by preservation of the indicated line.

## Proof
**1. Full automorphism scheme.** Any \(R\)-algebra endomorphism of \(A_R=R[x,y]/(x^2,y^2)\) is specified uniquely by
\[
\phi(x)=c+ax+by+sxy,\qquad \phi(y)=e+fx+gy+txy.
\]
In characteristic \(2\), the relations \(\phi(x)^2=\phi(y)^2=0\) are exactly \(c^2=e^2=0\). Put \(\Delta=ag+bf\). In the quotient by the nilpotent ideal \((c,e)\), the induced map on the radical modulo its square has matrix \(\begin{psmallmatrix}a&f\\b&g\end{psmallmatrix}\), and the top graded piece has coefficient \(\Delta\). Hence it is invertible there exactly if \(\Delta\) is a unit. A map of finite free \(R\)-modules is invertible precisely when its determinant is a unit; since the ideal \((c,e)\) is nilpotent (its cube is zero), invertibility modulo this ideal is equivalent to invertibility over \(R\). Thus \(\phi\) is an algebra automorphism if and only if \(\Delta\in R^\times\), proving the representing coordinate ring without restricting to field points.

**2. Reduction and tangent space.** The nilradical of the representing ring is exactly \((c,e)\), since the quotient is the reduced, smooth coordinate ring of \(\operatorname{GL}_2\times\mathbb A^2\). This nilpotent ideal satisfies \((c,e)^3=0\), and each geometric fiber of this infinitesimal factor has length \(4\), with basis \(1,c,e,ce\). Hence \(\dim\mathcal G=6\), but the tangent dimension at the identity is \(8\), consisting of the six usual coefficients and the two first-order constants. Equivalently, a tangent automorphism \(\operatorname{id}+\varepsilon D\) of \(A\otimes_k k[\varepsilon]/(\varepsilon^2)\) is determined by an arbitrary derivation \(D\), for which \(D(x)\) and \(D(y)\) are arbitrary elements of the four-dimensional algebra \(A\).

**3. Global image on the quotient.** When \(R\) is reduced, \(c=e=0\), and in the ordered basis \((\overline{x},\overline{y},\overline{xy})\) the action on \(V_R\) has matrix
\[
M=\begin{pmatrix}a&f&0\\b&g&0\\s&t&\Delta\end{pmatrix}.
\]
Thus the projective class lies in the maximal parabolic \(P\) stabilizing \(R\overline{xy}\). Conversely, for a field \(K/k\) and an arbitrary element of \(P(K)\), choose a block-matrix representative \(\begin{psmallmatrix}B&0\\w&\delta\end{psmallmatrix}\) with \(B\in\operatorname{GL}_2(K)\), \(\delta\ne0\). Multiplying the representative by \(\lambda=\delta/\det B\) makes its bottom-right entry equal to the determinant of the upper block: \(\lambda\delta=\det(\lambda B)\). This gives the required automorphism of \(A_K\). The map of reduced algebraic groups onto \(P\) is in fact an isomorphism, by this regular inverse on the parabolic block-chart. Since \(P\subsetneq\operatorname{PGL}_3\), the geometric-point image is proper of dimension \(6\).

**4. Differential is full.** A derivation \(D\in W\) is specified by eight coefficients
\[
D(x)=u+bx+cy+dxy,\qquad D(y)=v+fx+gy+hxy.
\]
Using Leibniz, \(D(xy)=vx+uy+(b+g)xy\). Its action on \(V\) is therefore the traceless matrix
\[
\rho(D)=\begin{pmatrix}b&f&v\\c&g&u\\d&h&b+g\end{pmatrix}.
\]
The eight entries \(u,v,b,c,d,f,g,h\) map bijectively and linearly to all of \(\mathfrak{sl}_3(k)\): in characteristic \(2\), the displayed trace is \(2(b+g)=0\), and the trace condition on an arbitrary \(3\times3\) matrix determines its third diagonal entry as the sum of its first two. The commutator of derivations acts on \(V\) by the matrix commutator. Because \(3\) is invertible in \(k\), the natural Lie map \(\mathfrak{sl}_3\to\mathfrak{pgl}_3=\mathfrak{gl}_3/kI\) is an isomorphism. The differential of \(\mathcal G\to\operatorname{PGL}(V)\) sends \(D\) to the class of \(\rho(D)\), hence is an isomorphism. This completes all assertions.

## Verification
The coordinate argument is over every commutative \(k\)-algebra, not just points of an algebraically closed field. A standalone checker `verify.py` enumerates the reduced automorphisms over \(\mathbb F_2\) and \(\mathbb F_4\), compares counts with \(q^2|\operatorname{GL}_2(\mathbb F_q)|\), checks their induced three-dimensional matrices and projective parabolic constraint, and checks the displayed derivation representation exhaustively over \(\mathbb F_2\). The general proof does not depend on finite verification.

## Relationship to prior work
Premet's 2015 preprint identifies the exceptional characteristic-two Witt algebra \(W(2;1)\) as \(\mathfrak{sl}_3\), furnishing the Lie-theoretic context. Boos (2015) studies parabolic conjugation on nilpotent matrices; parabolic orbit results concern the reduced action and do not themselves describe the nonreduced automorphism group scheme or the differential of its action. The new claim is **not** that the Witt–special-linear isomorphism or the parabolic subgroup is previously unknown; it is their simultaneous group-scheme realization, with the explicit length-four infinitesimal thickening and the differential-isomorphism/proper-point-image distinction. Searches also compared other characteristic-two non-smooth automorphism schemes, for a different Leibniz algebra, which do not imply this group-scheme calculation.

## Limitations
The displayed product is of underlying schemes and is not asserted to split the group law. The map to \(\operatorname{PGL}_3\) is not claimed surjective as a morphism of schemes, nor is its scheme-theoretic image characterized by an ideal. No classification of orbit closures or all infinitesimal subgroup schemes is attempted. A bounded literature search cannot prove absolute publication priority; an uninspected general classification of truncated-polynomial automorphism group schemes might imply part of the formula. The cited parabolic paper's full text was not obtained in this run, so the assessment distinguishes its accessible abstract from a full-text inspection.

## References
- Magdalena Boos, *Finite Parabolic Conjugation on Varieties of Nilpotent Matrices*, arXiv:1504.05367v1, first posted 2015-04-21, https://arxiv.org/abs/1504.05367.
- Alexander Premet, *A modular analogue of Morozov's theorem on maximal subalgebras of simple Lie algebras*, arXiv:1512.05614v1, first posted 2015-12-17, https://arxiv.org/abs/1512.05614, Section 4.4, p.40 (Witt \(W(2;1)\cong\mathfrak{sl}_3\)).
- Nham V. Ngo, *On nilpotent commuting varieties and cohomology of Frobenius kernels*, arXiv:1401.6820v1, first posted 2014-01-27, https://arxiv.org/abs/1401.6820. This concerns commuting varieties and dimension, not the automorphism group scheme studied here.
