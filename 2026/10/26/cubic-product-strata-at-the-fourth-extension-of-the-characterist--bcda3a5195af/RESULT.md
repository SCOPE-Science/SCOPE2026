# Cubic-product strata at the fourth extension of the characteristic-five Fermat quartic

## Finding
Let \(K=\mathbb F_{625}\), and let \(C/K\) be the base change of the Fermat quartic \(X^4+Y^4+Z^4=0\) over \(\mathbb F_5\). Define \(C^\circ\) by \(XYZ\ne0\). For any projective point \(P=[X:Y:Z]\in C^\circ(K)\), the class of \(XYZ\) in \(K^\times/(K^\times)^3\) is well-defined, because projective rescaling multiplies it by a cube.

**Theorem.** Among the \(656\) points of \(C^\circ(K)\), exactly \(80\) have trivial cubic-product class, and the other two cubic classes occur exactly \(288\) times each. All \(12\) coordinate-section points are \(K\)-rational; hence \(\#C(K)=668\). The natural order-\(16\) diagonal \(\mu_4^2\)-action is free on \(C^\circ(K)\). Its trivial-class locus is exactly five orbits, represented by the possible fourth-power pairs
\[
(A,B)=(1,3),(2,2),(3,1),(\omega,\omega^2),(\omega^2,\omega),
\quad \omega^2+\omega+1=0.
\]
The two nontrivial cubic classes each comprise eighteen free orbits.

Let \(D\) denote the normalization of the cyclic degree-three cover of \(C\) with function-field equation \(s^3=XY/Z^2\). Then \(D\) is geometrically connected of genus \(19\), and \(\#D(K)=252\).

## Assumptions and scope
The base field is exactly \(\mathbb F_5\), the extension exactly \(K=\mathbb F_{5^4}\), and the plane quartic is the displayed model (smooth because \(5\nmid4\)). Characteristic is prime to \(3\) and \(4\). The group \(\mu_4^2\) is defined over \(\mathbb F_5\). A cubic-product class is assigned only where all three homogeneous coordinates are nonzero; on the boundary, the product is zero. The cover \(D\) is understood as the smooth projective normalization, not the singular naive projective closure.

## Proof
Write every torus point uniquely as \([u:v:1]\), so \(u^4+v^4=-1\). The group \(K^\times\) has order \(624=4\cdot156\) and the fourth-power subgroup \(H=(K^\times)^4\) therefore has order \(156\), with four fourth roots for each of its elements. Let \(A=u^4\) and \(B=v^4=-1-A\). Since \(H\) is precisely the subgroup of the \(156\)-th roots of unity, possible values of \(A\) are exactly the roots in \(K\) of
\[
G(T)=\gcd\bigl(T^{156}-1,(T+1)^{156}-1\bigr)\in\mathbb F_5[T].
\]
The monic gcd has degree \(41\). Its roots are simple (both input polynomials are separable), and all are in \(K\), because \(156\mid624\). Hence precisely \(41\) ordered fourth-power pairs occur, with \(4\cdot4=16\) points per pair. This gives \(41\cdot16=656\) torus points.

For \(z\in K^\times\) write \(\chi(z)=z^{208}\in\mu_3\); this tests whether \(z\) is a cube. Because \(AB=(uv)^4\) and \(4\equiv1\pmod3\), \(\chi(uv)=\chi(AB)\). Moreover \(B=-1-A\), and \(208\) is even, so the trivial-class pairs correspond precisely to common roots of \(G(T)\) and \((T(T+1))^{208}-1\). Exact Euclidean division in \(\mathbb F_5[T]\) gives
\[
\gcd\bigl(G(T),(T(T+1))^{208}-1\bigr)
=T^5+T^3-T^2-1
=(T-1)(T-2)(T-3)(T^2+T+1).
\]
Both gcds are reproduced by the included pure-Python checker using complete polynomial Euclidean arithmetic, not a sample of field points. Thus there are five fourth-power pairs with trivial cubic product and exactly \(5\cdot16=80\) such points. The remaining \(36\cdot16=576\) points have nontrivial class. The \(\mathbb F_5\)-Frobenius \(z\mapsto z^5\) swaps the two primitive cube roots of unity and preserves the curve, so the two nontrivial classes have equal cardinality \(288\). The sixteen diagonal transformations independently multiply \(u\) and \(v\) by fourth roots of unity; this action is free on the torus and its fourth-power pairs are exactly its orbits. Every fourth root of unity in \(K\) is a cube, since the subgroup of order \(4\) lies in \((K^\times)^3\), so the cubic classes are constant on these orbits.

The three coordinate lines meet the smooth quartic transversely in four points each, because \(-1\) is a fourth power in \(K\). Their intersections are disjoint, yielding twelve further points and total \(668\).

The function \(f=XY/Z^2\in K(C)^\times\) has a simple zero at each of the eight points on \(X=0\) or \(Y=0\), and a pole of order two at each of the four points on \(Z=0\). Thus its Kummer extension by a cubic root is geometrically connected (it is not a cube even geometrically), is totally tamely ramified at exactly twelve geometric points, and is unramified elsewhere. Riemann--Hurwitz gives \(2g(D)-2=3(2\cdot3-2)+12(3-1)=36\), so \(g(D)=19\). Over \(K\), each of the \(80\) cube-product torus points has three rational lifts; each of the \(12\) ramified boundary points has one rational lift. All other points have no rational lift. Hence \(\#D(K)=3\cdot80+12=252\).

## Verification
Run `python3 fermat_quartic_cube_check.py` using an ordinary Python 3 installation. It independently computes the two monic polynomial gcds and their squarefreeness over \(\mathbb F_5\), realizes the extension \(K=\mathbb F_5[\theta]/(\theta^4+\theta-1)\), and enumerates the fourth-power subgroup, confirming the quotient counts \((5,18,18)\), the point totals, and an explicit noncube point. Its expected terminal line starts `VERIFY_OK`. The polynomial gcd is a complete exact certificate for this fixed-field classification; it is not a finite sample used to infer an unproved infinite assertion.

For example, choosing \(\theta^4+\theta-1=0\), the point
\[
[u:v:1]=[3+\theta^2:2+4\theta^2+\theta^3:1]
\]
lies on \(C(K)\) and satisfies \((uv)^{208}=\theta+\theta^2+4\theta^3\ne1\), so its cubic-product class is nontrivial.

## Relationship to prior work
Voloch and Zieve (arXiv:1310.1772, Corollary 1.1) proved that on the degree-\(q-1\) Fermat curve over \(\mathbb F_{q^i}\), for \(i=1,2,3\), the product of the three homogeneous coordinates is always a cube. They expressly noted a counterexample at \(i=4\) for \(q=2\) in Section 4. The theorem here does **not** claim to discover failure at the fourth extension in general. It determines instead the complete cubic-class distribution, diagonal-orbit geometry, and associated genus-\(19\) Kummer-cover point count for the smooth positive-genus quartic in characteristic five. General diagonal-curve point-count methods can determine the total number of points on \(C\) but do not, without a further character-weighted comparison, supply this product-class partition. Some character-sum or unpublished tables may implicitly contain the numerical specialization.

## Limitations
This is a fixed-extension arithmetic statement, not a formula for all extensions, all Fermat curves, or all Kummer covers. The exact polynomial gcds have been checked computationally with transparent Euclidean code; an independent research audit has not been conducted. Originality searches cannot exclude unindexed historical character-sum evaluations or database tables. The relevant earlier article of Moisio on rational-point counts was located but its complete text was not inspected; it concerns the base Fermat point counts for extensions of degree two and three and is not known here to classify cubic-product values over the fourth extension.

## References
Voloch, J. F. and Zieve, M. E., *Rational points on some Fermat curves and surfaces over finite fields*, arXiv:1310.1772v1 (public 2013-10-07), especially Corollary 1.1 and Section 4. https://arxiv.org/pdf/1310.1772

Moisio, M. J., *On the number of rational points on some families of Fermat curves over finite fields*, Finite Fields and Their Applications **13** (2007), 546–562, DOI:10.1016/j.ffa.2005.10.003 (abstract consulted).
