# Ten reduced superspecial parameters and a length-15 boundary collision in characteristic eleven

## Finding
Let \(k\) be algebraically closed of characteristic \(11\). Put \(u=a+b\), \(v=ab\), and consider the family of genus-two curves
\[
 C_{u,v}:\quad y^2=(x^2-1)(x^4-u x^2+v).
\]
Its smooth parameter open set is
\[
 U=\operatorname{Spec}k[u,v,\{v(u^2-4v)(1-u+v)\}^{-1}].
\]
The zero scheme of the relative Cartier operator on the smooth base consists of **exactly ten reduced geometric points**. In the full affine parameter plane, the two Cartier-entry equations define a zero-dimensional complete intersection of length \(25\): ten reduced points on \(U\), together with a local length-\(15\) scheme supported at the excluded triple collision \((u,v)=(2,1)\).

Eight of the smooth parameters are indexed by the distinct roots of
\[
 G(u)=(u+1)(u+3)(u+5)(u-3)(u^2-5u-1)(u^2-u-4),
\]
with a unique compatible \(v\) for each such root. The other two are \((u,v)=(2,3),(2,4)\). Constants and equations are in characteristic \(11\).

## Assumptions and scope
The coordinates \((u,v)\) symmetrize the two unordered branch pairs \(\{\pm\sqrt a\}\) and \(\{\pm\sqrt b\}\), with \(\{\pm1\}\) distinguished. No quotient by all changes of hyperelliptic coordinate is taken. A model is smooth of genus two exactly when \(v(u^2-4v)(1-u+v)\ne0\), which is the condition that the six finite branch roots are nonzero and distinct.

“Superspecial” on the smooth base means that the Jacobian is superspecial. On the whole affine plane, the equations are only the polynomial extension of the relative Cartier entries; they do not define a superspecial Jacobian at the singular-curve parameter.

## Proof
Put \(q(T)=(T-1)(T^2-uT+v)\) so that the defining sextic is \(f(x)=q(x^2)\). In the standard basis of regular differentials, the relative Cartier entries in odd characteristic are the coefficients of \(f(x)^{(p-1)/2}\) at \(p-1,p-2,2p-1,2p-2\), up to transpose. In characteristic \(11\), \(f(x)^5\) is even, so the entries at the odd indices \(9,21\) vanish. The diagonal entries cutting out the zero scheme on \(U\) are
\[
 A(u,v)=[T^5]q(T)^5,\qquad B(u,v)=[T^{10}]q(T)^5.
\]
For a geometric fiber, vanishing Cartier is equivalent to maximal \(a\)-number (here \(2\)), i.e. to superspeciality of the Jacobian.

Exact binomial expansion modulo \(11\) gives
\[
\begin{aligned}
 A={}&u^5+3u^4v+u^3v^2-2u^3v+u^2v^3-4u^2v^2\\
  &+3uv^4+2uv^3-3uv^2+v^5-5v^4-5v^3,\\
 B={}&-u^5-3u^4+2u^3v-u^3+4u^2v-u^2+3uv^2\\
  &-2uv-3u+5v^2+5v-1.
\end{aligned}
\]
Here \(A\) is monic of degree five in \(v\), and the coefficient of \(v^2\) in \(B\) is \(3u+5=3(u-2)\); in fact \(B(2,v)=0\) identically. Let \(R=k[u,v]/(A)\), finite free over \(k[u]\) with basis \(1,v,\ldots,v^4\). The determinant of multiplication by \(B\) on \(R\), equivalently the Sylvester resultant, is
\[
 \operatorname{Res}_v(A,B)=-(u-2)^{17}G(u).
\]
This determinant formula uses monicity of \(A\), not preservation of the degree of \(B\) upon specialization. At any \(u=u_0\), the cokernel of the multiplication matrix over the discrete valuation ring \(k[u]_{(u-u_0)}\) is the localization of \(k[u,v]/(A,B)\) there. The matrix has nonzero determinant, so its cokernel length over this ring equals the order of the determinant (diagonalize over the discrete valuation ring and sum the orders of the invariant factors). The residue field is \(k\); this length is the sum of the geometric local lengths at the points over \(u_0\).

The eight roots of \(G\) are simple and distinct from \(2\): its four linear roots are distinct, the two quadratics have nonzero discriminants \(7\) and \(6\) modulo \(11\), and the quadratics have no common roots with each other or with the given linear factors. Each root therefore supports one reduced intersection point by the cokernel length argument. At \(u=2\), the scheme-theoretic fiber is defined by
\[
A(2,v)=(v-1)^3(v-3)(v-4),\qquad B(2,v)=0.
\]
It has length five. The full local schemes supported at its three points together have length \(17\), the order of the determinant at \(u=2\). Both \((2,3)\) and \((2,4)\) have Jacobian determinant \(\partial_u A\,\partial_v B-\partial_v A\,\partial_u B=8\ne0\) and have local length one. The remaining point \((2,1)\) has local length \(17-2=15\).

The determinant proves finite support, so the two equations cut out a zero-dimensional complete intersection in the affine plane. The total length is \(17+8=25\). Equivalently, there is no intersection at infinity: the top degree part of \(B\) is \(-u^5\), and the top degree part of \(A\) at \(u=0\) is \(v^5\). Both equations have degree five, so Bézout gives the same length.

Finally, the excluded boundary has components \(v=0\), \(v=u-1\), and \(v=u^2/4\). The monic gcds of the two restrictions on these components are, respectively, \(1\), \((u-2)^5\), and \((u-2)^5\). In particular, only \((2,1)\) lies on the boundary. This proves the ten-plus-fifteen decomposition.

## Verification
Run `python3 verify.py` with Python 3 and SymPy. The script reconstructs \(q^5\), the two Cartier coefficients, the resultant, the boundary gcds, the \(u=2\) fiber gcd, and the two nonzero Jacobians with exact arithmetic modulo eleven. Expected output begins `VERIFY_OK`. The support over an algebraically closed field and the local lengths follow from the finite free projection argument, not a finite-field point search.

## Relationship to prior work
Ohashi treats this exact even-sextic family in work on Rosenhain forms (Lemma 3.3), assuming superspeciality in order to compare maximality and minimality. Harashita and Yamamoto prove a general multiplicity-one theorem for the genus-two superspecial locus in smooth Rosenhain coordinates. Katsura and Takashima classify the two abstract superspecial genus-two isomorphism classes in characteristic eleven (Section 7.2). The present calculation concerns the specified marked plane: it computes the local length of the extended coefficient ideal at its excluded triple collision, which is not a smooth moduli multiplicity or an invariant of an abstract superspecial curve.

## Limitations
The ten points do not represent ten abstract curves up to isomorphism. The boundary length is a length of the extended coefficient-equation intersection, not a claim about a superspecial locus on a compactification. No publication-priority claim is made.

## References
- R. Ohashi, *On the Rosenhain Forms of Superspecial Curves of Genus Two*, arXiv:2308.11963, especially Lemma 3.3.
- S. Harashita and Y. Yamamoto, *The Multiplicity-One Theorem for the Superspeciality of Curves of Genus Two*, arXiv:2409.13212, especially Theorem B.
- T. Katsura and K. Takashima, *Counting Richelot Isogenies between Superspecial Abelian Surfaces*, arXiv:2003.00633, Section 7.2.
