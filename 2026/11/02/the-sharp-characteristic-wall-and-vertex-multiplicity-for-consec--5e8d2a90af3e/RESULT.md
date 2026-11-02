# The sharp characteristic wall and vertex multiplicity for consecutive power-sum complete intersections

## Finding
Let \(k\) be algebraically closed of prime characteristic \(p\). For consecutive power sums \(P_j^{(n)}=\sum_{i=1}^{n}X_i^j\), \(1\le j\le m\), with \(3\le m<p\) and \(n\ge m+1\), put
\[
X_{n,m}=\operatorname{Proj}\bigl(k[X_1,\ldots,X_n]/(P_1^{(n)},\ldots,P_m^{(n)})\bigr).
\]
This is a projective complete intersection of dimension \(n-m-1\) and degree \(m!\). Its *sharp smoothness criterion* is
\[
\boxed{X_{n,m}\text{ is smooth if and only if } n<p.}
\]
At the first singular value \(n=p\), the singular locus consists of the single point \(v=[1:\cdots:1]\), and
\[
\boxed{e(\mathcal O_{X_{p,m},v})=m!.}
\]
Moreover, the entire graded coordinate ring is a polynomial extension of the \((p-1)\)-variable power-sum ring. Thus the boundary falls into three distinct geometries: a length-\(m!\) nonreduced point when \(p=m+1\); a reduced union of \(m!\) lines meeting at \(v\) when \(p=m+2\); and an integral normal cone with an isolated vertex singularity when \(p\ge m+3\).

## Assumptions and scope
The field is algebraically closed of prime characteristic \(p\), the number of equations satisfies \(3\le m<p\), and \(n\ge m+1\). These hypotheses ensure every integer \(1,\ldots,m\) is invertible. The homogeneous scheme structure is the one induced by the displayed ideal, not merely its underlying zero set. Multiplicity means Hilbert--Samuel multiplicity of the local ring at the stated closed point. Statements of geometric irreducibility and reducedness refer to the algebraic closure, already taken in the hypotheses.

## Proof
**1. The complete-intersection structure.** Write \(e_j^{(n)}\) for the degree-\(j\) elementary symmetric polynomial. Newton's identities
\[
j e_j^{(n)}=\sum_{r=1}^{j}(-1)^{r-1}e_{j-r}^{(n)}P_r^{(n)},\qquad e_0^{(n)}=1,
\]
are triangular, and \(j\) is invertible for \(j\le m\). Hence the ideal of the first \(m\) power sums equals the ideal of \(e_1^{(n)},\ldots,e_m^{(n)}\). The fundamental theorem of symmetric polynomials, together with the standard monomial basis for the polynomial ring over its elementary symmetric subring, shows \(e_1^{(n)},\ldots,e_n^{(n)}\) is a homogeneous regular sequence in \(k[X_1,\ldots,X_n]\) in every characteristic. Equivalently, the polynomial ring is finite free over \(k[e_1^{(n)},\ldots,e_n^{(n)}]\); this also follows from the standard coinvariant monomial basis. Therefore the initial \(m\) elements form a regular sequence. As \(n>m\), their projective zero scheme has pure dimension \(n-m-1\), and Bezout's degree formula for a complete intersection gives \(\prod_{j=1}^{m}j=m!\).

**2. Jacobian rank and the smooth side.** At a geometric point with homogeneous coordinates \((x_1,\ldots,x_n)\), the Jacobian of the equations has entries \(j x_i^{j-1}\). Because every \(j\le m\) is invertible, a Vandermonde minor shows
\[
\operatorname{rank}J=\min\bigl(m,\#\{x_1,\ldots,x_n\}\bigr).
\]
Suppose \(n<p\) and \(J\) has rank less than \(m\). Among the coordinates there are at most \(m-1\) distinct values. Let \(a_1,\ldots,a_r\) be the *distinct nonzero* values, with positive integer multiplicities \(c_1,\ldots,c_r\). Then \(r\le m-1\), and the first \(r\) power-sum equations give
\[
\sum_{s=1}^{r}c_s a_s^j=0\qquad(1\le j\le r).
\]
The square matrix \((a_s^j)_{1\le j,s\le r}\) has determinant \((\prod_s a_s)\prod_{s<t}(a_t-a_s)\ne0\). Hence every \(c_s=0\) in \(k\). But \(1\le c_s\le n<p\), so each is nonzero in \(k\), a contradiction. There must be a nonzero coordinate at a projective point. Thus the complete intersection is smooth whenever \(n<p\).

**3. The sharp obstruction.** For \(n\ge p\), take the projective coordinate vector consisting of \(p\) copies of \(1\) and \(n-p\) zeros. Each power sum vanishes because \(p=0\) in \(k\), while the coordinates assume at most two distinct values. Since \(m\ge3\), the Jacobian has rank smaller than \(m\). The projective complete intersection is therefore singular. (For \(n=p\), all \(p\) coordinates are \(1\).)

**4. The boundary is a graded polynomial extension.** Set \(T=X_p\) and \(Y_i=X_i-X_p\), \(1\le i<p\), so \(X_i=Y_i+T\). For each \(j\le m\), the binomial expansion yields
\[
P_j^{(p)}(Y_1+T,\ldots,Y_{p-1}+T,T)
=\sum_{r=1}^{j}\binom jr T^{j-r}P_r^{(p-1)}(Y),
\]
because the constant coefficient is \(pT^j=0\). These \(m\) equations are triangular in the \(P_j^{(p-1)}\), with diagonal entries \(1\). Thus there is an **isomorphism of graded rings**
\[
\frac{k[X_1,\ldots,X_p]}{(P_1^{(p)},\ldots,P_m^{(p)})}
\simeq
\left(\frac{k[Y_1,\ldots,Y_{p-1}]}{(P_1^{(p-1)},\ldots,P_m^{(p-1)})}\right)[T].
\]
When \(p\ge m+2\), the base projective scheme \(X_{p-1,m}\) is nonempty and smooth by Step 2, and the formula identifies \(X_{p,m}\) with its projective cone with vertex \(v\). Every point away from the vertex is smooth: its punctured affine-cone chart is locally a product with \(\mathbb G_m\) over the smooth base, while the \(T=0\) hyperplane is itself the smooth base. At \(v\) the affine chart \(T\ne0\) has coordinates \(y_i=Y_i/T\) and equations \(P_j^{(p-1)}(y)=0\); all vanish to positive homogeneous order, so the vertex is singular. When \(p=m+1\), the base homogeneous coordinate quotient is an Artinian ring supported at the origin and its projective spectrum is empty; nevertheless the graded polynomial-extension statement remains valid and the resulting projective scheme is supported at \(v\).

**5. Multiplicity and the three boundary regimes.** The local chart at \(v\) is the local ring at the origin of the homogeneous complete intersection in \(p-1\) variables given by degrees \(1,\ldots,m\). The leading forms are the equations themselves and are a regular sequence; its Hilbert--Samuel multiplicity is therefore \(\prod_{j=1}^{m}j=m!\). If \(p=m+1\), the same quotient is Artinian local of length \(m!>1\), producing a nonreduced point. If \(p=m+2\), the base has projective dimension zero; smoothness and degree imply it consists of precisely \(m!\) distinct geometric points, so its projective cone is the reduced union of \(m!\) distinct lines through \(v\). If \(p\ge m+3\), the smooth complete-intersection base has positive dimension. It is connected (projective connectedness of positive-dimensional complete intersections), hence integral; its graded ring is Cohen--Macaulay and regular away from the origin, which has codimension at least two. Serre's \(R_1+S_2\) criterion makes the graded ring normal. Its projective cone is integral and normal with sole singularity \(v\). This proves every assertion.

## Verification
A standalone standard-library Python script, `verify.py`, enumerates points over selected small prime fields and calculates the Jacobian rank modulo \(p\). It checks the smooth side, singular boundary, and the persistence of singularities after the boundary. The checked cases are explicitly finite and do not verify geometric smoothness or irreducibility over all algebraic closures. The proof above supplies those infinite statements through Newton identities, Jacobian rank, the graded coordinate change, and the complete-intersection local multiplicity calculation.

## Relationship to prior work
Giménez, Gottig, Palacios, Pérez and Privitelli study much more general systems of power sums over finite fields in arXiv:2610.32056v1, notably their geometric analysis in Section 3 and the projective-closure analysis in Section 3.1. They prove complete-intersection, radicality, and normality statements with explicit sufficient parameter inequalities, and describe bounds for the dimension of singular loci. In particular, their results **already establish normal complete-intersection behavior on a substantial overlapping large-\(n\) range**; neither that broad normality nor generic complete-intersection degrees are claimed here as new. The additional statement in this special consecutive, homogeneous family is the *if-and-only-if smoothness wall*, the explicit scheme-level translation-to-a-polynomial-extension at the first singular parameter, the unique vertex with its exact Hilbert--Samuel multiplicity, and the three geometric boundary regimes. Characteristic-zero power-sum ideal results (such as Conca--Singh--Soundararajan) concern a different characteristic regime. Earlier algebraic invariant theory supplies the classical elementary-symmetric and coinvariant facts used in Step 1.

## Limitations
The theorem requires consecutive exponents \(1,\ldots,m\), coefficients all equal to \(1\), zero right-hand sides, \(m\ge3\), and \(p>m\). It does not extend the sharp criterion to arbitrary exponents, arbitrary coefficients, nonhomogeneous level sets or characteristics dividing one of the exponents. The singular-locus assertion at \(n=p\) is scheme-theoretic in the sense that the complete-intersection equations and local multiplicity are identified, but it does not determine a minimal free resolution of the singular-locus Jacobian ideal. The result has not undergone an independent mathematical audit, and an equivalent observation may be implicit in classical characteristic-\(p\) symmetric-invariant literature.

## References
1. N. Giménez, J. F. Gottig, M. Palacios, M. Pérez and M. Privitelli, *Power Sum Varieties over Finite Fields*, arXiv:2610.32056v1, first posted 2026-10-23, especially Sections 3 and 3.1, https://arxiv.org/html/2610.32056v1.
2. A. Conca, A. K. Singh and K. Soundararajan, *Ideals generated by power sums*, Rev. Roumaine Math. Pures Appl. 69 (2025); the characteristic-zero comparison reference cited in reference 1.
3. Standard Newton identities, coinvariant-basis theorem for symmetric polynomials, and Serre's normality criterion (classical results; used with explicit hypotheses in the proof).
