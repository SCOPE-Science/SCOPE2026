# Frobenius splitting of the characteristic-five Klein quartic's flex triangles

## Finding
Let \(C/\mathbb F_5\) be the smooth projective Klein quartic
\[
 C: X^3Y+Y^3Z+Z^3X=0\subset\mathbb P^2_{\mathbb F_5}.
\]
Let \(W\subset C\) be its scheme of ordinary inflection points, equivalently the scheme-theoretic intersection of \(C\) with its Hessian. This is a reduced finite étale scheme of degree \(24\). Geometric Frobenius on \(W(\overline{\mathbb F}_5)\) has cycle type
\[
 \boxed{1^3\,3^1\,6^3}.
\]
The tangent to \(C\) at each \(P\in W\) meets \(C\) in the divisor \(3P+\tau(P)\), where \(\tau\) is a fixed-point-free permutation of \(W\) of order three. Its eight orbits are called *flex triangles*. The corresponding degree-eight finite étale triangle scheme \(T=W/\langle\tau\rangle\) has Frobenius cycle type
\[
 \boxed{1^2\,6^1}.
\]
Consequently, for every integer \(n\ge1\), the numbers of rational flex points and rational flex triangles over \(\mathbb F_{5^n}\) are respectively
\[
 \boxed{\#W(\mathbb F_{5^n})=3+3\mathbf1_{3\mid n}+18\mathbf1_{6\mid n}},\qquad
 \boxed{\#T(\mathbb F_{5^n})=2+6\mathbf1_{6\mid n}}.
\]
Their finite-scheme zeta functions are
\[
 \boxed{Z(W,t)=\frac1{(1-t)^3(1-t^3)(1-t^6)^3}},\qquad
 \boxed{Z(T,t)=\frac1{(1-t)^2(1-t^6)}}.
\]
In particular, three flex points and two flex triangles are rational over \(\mathbb F_5\), six flex points are rational over \(\mathbb F_{125}\), and all \(24\) flex points and all eight triangles split over \(\mathbb F_{5^6}\). These counts concern flexes and triangles, **not** all rational points of \(C\).

## Assumptions and scope
The ground field is \(\mathbb F_5\); the equation and its projective coordinates are fixed. A flex is a point where the tangent line has intersection multiplicity at least three. The Hessian criterion applies because the characteristic is neither two nor three. A triangle is an orbit of the residual-tangent-point map \(\tau\), not an arbitrary collinear triple; each orbit has three distinct points. All finite-scheme assertions use the reduced schemes proved below. No conclusions are asserted for nontrivial twists, other residue characteristics, or the geometric point count of the full curve.

## Proof
**1. Smoothness and Hessian.** Write \(F=X^3Y+Y^3Z+Z^3X\). A singular point with a zero coordinate would have to be a coordinate vertex, where a partial derivative is nonzero. If \(XYZ\ne0\), the three equations \(F_X=F_Y=F_Z=0\) give \(Z^3=2X^2Y\), \(X^3=2Y^2Z\), and \(Y^3=2Z^2X\), whence \(1=2^3=3\) in \(\mathbb F_5\), an impossibility. Thus \(C\) is smooth. The Hessian determinant reduces to
\[
 H=X^5Z+XY^5+YZ^5.
\]
Indeed, over the integers it is \(-54(X^5Z-5X^2Y^2Z^2+XY^5+YZ^5)\), and \(-54=1\) modulo five. On \(Z=0\), the common zeros of \(F,H\) are precisely \([1:0:0]\) and \([0:1:0]\). In the affine chart \(Z=1\), the point \((0,0)\) is the only common zero with \(x=0\). All three coordinate points are transverse intersection points, as follows immediately from the nonzero linear terms \((y,z)\), \((z,x)\), and \((x,y)\) of \((F,H)\) in suitable affine charts.

**2. The other twenty-one flexes.** On \(Z=1\), set \(F=y^3+x^3y+x\), \(H=x^5+xy^5+y\). Reduction of \(H\) modulo \(F\) gives
\[
 Q=-x^2y^2+(x^7+1)y+2x^5.
\]
For \(x\ne0\), eliminating \(y^2\) from \(F,Q\) gives
\[
 D(x)y+x^5(2x^7+3)=0,\qquad D(x)=x^{14}+1.
\]
Put \(N(x)=-x^5(2x^7+3)\). Substitution into \(Q\) yields the exact polynomial identity over \(\mathbb F_5\):
\[
 D(x)^2Q(x,N(x)/D(x))=x^5g(x),\quad
 g(x)=x^{21}+2x^{14}+x^7-1.
\]
As \(\gcd(g,D)=1\), this is an if-and-only-if elimination: each nonzero root of \(g\) determines exactly one point \((x,N(x)/D(x))\) of \(C\cap V(H)\). In particular, the degree-three polynomial in \(u=x^7\), \(u^3+2u^2+u-1\), and the relation \(u^2+1\) have constant nonzero remainder, proving the denominator is invertible at every such root.

Over \(\mathbb F_5\), the exact factorization is
\[
\begin{aligned}
 g_0&=x^3+x^2+3x+4,\\
 g_1&=x^6+x^4+2x^3+4x^2+2x+1,\\
 g_2&=x^6+2x^5+4x^4+x^3+2x^2+2x+1,\\
 g_3&=x^6+2x^5+4x^4+3x^3+4x^2+4x+1,\\
 g&=g_0g_1g_2g_3.
\end{aligned}
\]
All four factors are distinct and irreducible. Their irreducibility is independently checked by the finite-field polynomial gcd criterion in `VERIFY.py`. The same code checks that the affine Jacobian determinant \(F_xH_y-F_yH_x\), with \(H_y=1\) and \(H_x=y^5\), is nonzero at a representative root of each factor. Frobenius transitivity on each irreducible factor then proves transversality at all twenty-one roots. Hence \(C\cap V(H)\) consists of exactly 24 reduced ordinary flexes. Its Frobenius orbit sizes are three fixed coordinate flexes, one length-three orbit, and three length-six orbits.

**3. Tangent triangles and descent.** For each ordinary flex \(P\), write the tangent intersection divisor as \(3P+\tau(P)\). To evaluate \(\tau\), choose a nonzero tangent-direction vector \(v\) independent of \(P\) and write
\[
 F(P+s v)=c_3s^3+c_4s^4.
\]
The residual point is \(P-(c_3/c_4)v\) when \(c_4\ne0\), or \([v]\) otherwise. This formula uses homogeneous representatives, and \(c_3,c_4\) are obtained without differentiation by evaluating \(F(P+v)\) and \(F(P-v)\). The exact quotient-field calculations in the accompanying checker show \(\tau^3(P)=P\) and \(\tau(P)\ne P\) on a root representative from each \(g_i\), with the analogous statement for the three coordinate vertices. Since \(\tau\) commutes with Frobenius, it has eight three-element orbits on all geometric flexes.

The coordinate vertices form one pointwise rational triangle. The three points from \(g_0\) form one Frobenius-stable triangle: there can be no fixed point of \(\tau\), and the three flexes constitute one Frobenius orbit. To distinguish how the eighteen degree-six points group into triangles, compute in \(K=\mathbb F_5[u]/(g_1(u))\), using \(x=u\) and \(y=N(u)/D(u)\). The residual tangent point has affine \(x\)-coordinate
\[
 x'=1+2u^2+3u^3+4u^4+4u^5.
\]
Direct reduction shows \(g_2(x')=0\) in \(K\). Because the calculation respects Frobenius, \(\tau\) sends all six roots of \(g_1\) to the six roots of \(g_2\). Its order three then cyclically permutes the three sextic root orbits \(g_1,g_2,g_3\). Every remaining triangle contains one root from each such orbit, and Frobenius acts transitively on the six triangles. Thus the triangle-cycle type is \(1^2 6^1\). The stated rational counts and finite étale zeta factors follow from the closed-point/Frobenius-orbit formula.

## Verification
Run the included, standalone Python 3 checker with `python3 VERIFY.py`. It uses only the Python standard library and exact arithmetic modulo five. Its checks include the elimination identity, invertible denominator, the complete factorization and Rabin irreducibility tests, the four transverse root representatives, the tangent-successor order-three relation, and its action on the four Frobenius factors. It prints `VERIFY_OK`. The code checks finite algebraic certificates in extensions of degree at most six; it does not rely on a search over a finite subset as proof that there are no other geometric flexes. Completeness follows from the projective chart analysis and the elimination equivalence.

## Relationship to prior work
Elkies (1999), *The Klein Quartic in Number Theory*, Proposition in Section 2 and the accompanying Weierstrass-point discussion, establishes the classical 24-flex orbit in characteristic zero. Poonen–Schaefer–Stoll (arXiv:math/0508174, submitted 2005-08-10), Sections 11.1–11.2.1, establish eight Galois-stable triples of ordinary flexes and use them for Jacobian descent, including flex-resultant computations for a different twist. These sources motivate the canonical triangle configuration but do not present this fixed characteristic-five Klein model's Frobenius cycle types or finite-scheme zeta functions. Greg Egan's 2006 account gives an explicit classical 24-flex grouping, without arithmetic splitting in characteristic five. The contribution here is restricted to the exact arithmetic descent of the standard plane model's flex and triangle schemes at five.

## Limitations
The source comparison is not an exhaustive novelty certification. This is a statement about this model over \(\mathbb F_5\), not every Klein-quartic twist, other primes, all rational points of \(C\), or the geometric Jacobian's isogeny class. The verification is exact symbolic arithmetic paired with a conventional mathematical argument; it is not an independent external audit. Characteristic five is tame for the Hessian/ordinary-flex calculation; nothing is asserted about characteristics two, three, or seven.

## References
1. N. D. Elkies, *The Klein Quartic in Number Theory*, in *The Eightfold Way*, MSRI Publications 35 (1999), pp. 51–102, especially the discussion of the 24 Weierstrass/inflection points in Section 2. Full text: https://library.slmath.org/books/Book35/files/elkies.pdf .
2. B. Poonen, E. F. Schaefer, M. Stoll, *Twists of X(7) and primitive solutions to x²+y³=z⁷*, arXiv:math/0508174 (first submitted 2005-08-10), Sections 11.1 and 11.2.1. https://arxiv.org/abs/math/0508174 .
3. G. Egan, *Klein's Quartic Equation* (2006), section “The 168 symmetries”, discussing the classical 24 inflection points. https://www.gregegan.net/SCIENCE/KleinQuartic/KleinQuarticEq.html .
