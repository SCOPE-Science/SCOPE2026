# A hidden \(A_8\) point at infinity on the six-node expressive sextic
## Finding
Let \(C\) be the polynomial sextic of Fomin--Shustin Example 8.4, parametrized by
\[
 t\longmapsto \bigl(P(t),Q(t)\bigr)
 =\bigl(-8t^6+24t^4+4t^3-18t^2-6t+1,\,-2t^4+4t^2-1\bigr).
\]
Write \(\overline C\subset\mathbf P^2_{\mathbf C}\) for its projective closure. Fomin--Shustin prove that the affine curve has exactly six hyperbolic nodes. The projective closure has exactly one further singular point, and its complete complex singularity basket is
\[
6A_1+A_8.
\]
More precisely, the unique point at infinity is \(p=[1:0:0]\). It is a unibranch \(A_8\) point with Puiseux pair \((2,9)\), so \(\delta(\overline C,p)=4\) and \(\mu(\overline C,p)=8\). Its intersection multiplicity with the line at infinity is
\[
(\overline C\cdot L_\infty)_p=6.
\]
Because this polynomial curve is \(L_\infty\)-regular in the sense of the source, its polar intersection invariant is therefore
\[
\mu(\overline C,p,L_\infty)=8+6-1=13.
\]
The normalization of \(\overline C\) is \(\mathbf P^1\).

## Assumptions and scope
All statements are over \(\mathbf C\), except that the six affine nodes are the real hyperbolic nodes established in the source. The curve is the sextic defined by the displayed polynomial parametrization; no assertion is made about unrelated sextics with six nodes. The symbol \(\mu(\overline C,p,L_\infty)\) denotes the polar intersection invariant defined by Fomin--Shustin, not the ordinary Milnor number and not a global Milnor number at infinity.

## Proof
Homogenizing the parametrization to degree six gives a morphism \(\phi:\mathbf P^1\to\mathbf P^2\):
\[
\begin{aligned}
X(u,v)&=-8u^6+24u^4v^2+4u^3v^3-18u^2v^4-6uv^5+v^6,\\
Y(u,v)&=-2u^4v^2+4u^2v^4-v^6,\\
Z(u,v)&=v^6.
\end{aligned}
\]
These forms have no common zero: if \(Z=0\), then \(v=0\) and \(X=-8u^6\neq0\). Since the image is the degree-six curve stated in Example 8.4 and \(\phi^*\mathcal O_{\mathbf P^2}(1)\) has degree six, the generic degree of \(\phi\) is one. Hence \(\phi\) is the normalization map and the normalization is \(\mathbf P^1\).

The equation \(Z=v^6\) shows that the only normalization point above \(L_\infty\) is \([u:v]=[1:0]\), mapping to \(p=[1:0:0]\). Put \(s=v/u\) and work in the chart \(X\neq0\). Define local coordinates
\[
\eta=Y/X,\qquad \zeta=Z/X.
\]
With
\[
\begin{aligned}
X(s)&=-8+24s^2+4s^3-18s^4-6s^5+s^6,\\
Y(s)&=-2s^2+4s^4-s^6,\\
Z(s)&=s^6,
\end{aligned}
\]
one has \(\operatorname{ord}_s(\eta)=2\). Make the analytic coordinate change \(\xi=\zeta+8\eta^3\). Its numerator is exactly
\[
Z(s)X(s)^2+8Y(s)^3
=-s^9(s^2+2s-2)
\bigl(7s^7-2s^6-78s^5-72s^4+96s^3+96s^2-32s-32\bigr).
\]
The two factors after \(s^9\) are nonzero at \(s=0\), while \(X(0)\neq0\). Thus
\[
\operatorname{ord}_s(\eta)=2,\qquad \operatorname{ord}_s(\xi)=9.
\]
Because \(\gcd(2,9)=1\), the branch has Puiseux pair \((2,9)\). A multiplicity-two irreducible plane branch with this pair is analytically equivalent, after Weierstrass completion of the square and a one-variable coordinate change, to \(y^2-x^9=0\); hence it is of type \(A_8\). Consequently
\[
\delta(\overline C,p)=\frac{(2-1)(9-1)}2=4,
\qquad
\mu(\overline C,p)=2\delta-1+1=8.
\]
Also
\[
(\overline C\cdot L_\infty)_p=\operatorname{ord}_s Z(s)=6.
\]

The source proves that the affine part has six simple nodes, each contributing \(\delta=1\). The arithmetic genus of a plane sextic is \(10\), while
\[
6\cdot1+4=10.
\]
Since the normalization has genus zero, this exhausts the genus defect and confirms that there are no additional singularities.

Finally, Fomin--Shustin's characterization of irreducible polynomial expressive curves implies that this curve is \(L_\infty\)-regular. By their definition of \(L_\infty\)-regularity,
\[
\mu(\overline C,p,L_\infty)
=\mu(\overline C,p)+(\overline C\cdot L_\infty)_p-1
=8+6-1=13.
\]

## Verification
The accompanying exact symbolic checker verifies the homogenized map, absence of base points, the source's difference-resultant factorization, the unique point at infinity, the exact order-two/order-nine local coordinate calculation, and the genus and polar-intersection arithmetic. In particular, the order-nine assertion is certified by an exact polynomial factorization, not by numerical truncation.

The local analytic identification with \(A_8\) uses the standard characteristic-zero classification of multiplicity-two plane branches: after a Weierstrass quadratic equation is completed to a square, an odd discriminant order \(9\) is reduced by a one-variable analytic coordinate change to the normal form \(y^2-x^9\).

## Relationship to prior work
Fomin--Shustin, Example 8.4, gives this polynomial parametrization, computes the difference-resultant, and proves that all twelve parameter roots are real, yielding six affine hyperbolic nodes and expressivity. Their general theory also supplies \(L_\infty\)-regularity and the identity defining the polar intersection invariant. The inspected source does not state the local analytic type at infinity, the Puiseux pair \((2,9)\), the complete basket \(6A_1+A_8\), or the value \(13\) of the polar invariant for this example.

The new step is the projective local calculation at the unique normalization point over infinity and its genus accounting. It explains where the four units of genus defect not supplied by the six visible affine nodes occur.

## Limitations
This result concerns the specific sextic parametrization in Example 8.4. It does not classify singularities at infinity for arbitrary expressive polynomial curves. The six affine nodes are taken from the exact resultant-and-node verification in the source; the accompanying checker independently reproduces the resultant factorization but does not replace the source's real-node transversality argument. The originality search found no indexed statement of the same projective basket, but poorly indexed or differently coordinated computations remain a residual possibility.

## References
1. S. Fomin and E. Shustin, *Expressive curves*, arXiv:2006.14066v4; first public version arXiv:2006.14066v1 (2020-06-24). See Definition 3.1, the discussion of \(L_\infty\)-regularity, Theorem 7.10 as used in Section 8, and Example 8.4.
