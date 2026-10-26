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
The scheme where the Cartier operator on \(H^0(C_{u,v},\Omega^1)\) vanishes (the superspecial locus) consists of **exactly ten reduced geometric points** of \(U\). In the full affine parameter plane, the two Cartier-entry equations define a zero-dimensional complete intersection of length \(25\): ten reduced points on \(U\), together with one length-\(15\) scheme supported at the excluded triple-collision parameter \((u,v)=(2,1)\).

The smooth ten are indexed by eight distinct roots of
\[
 G(u)=(u+1)(u+3)(u+5)(u-3)(u^2-5u-1)(u^2-u-4)
\]
(each admits exactly one compatible \(v\)), and two additional parameters \((u,v)=(2,3),(2,4)\). All equations and constants are read in characteristic \(11\). This is a count of points in the **specified marked-branch parameter space**, not a count of isomorphism classes of curves.

## Assumptions and scope
The characteristic is exactly \(11\) and \(k\) is algebraically closed. The parameter coordinates \((u,v)\) symmetrize the two unordered branch pairs \(\{\pm\sqrt a\}\) and \(\{\pm\sqrt b\}\), with the branch pair \(\{\pm1\}\) distinguished. No quotient by all changes of hyperelliptic coordinate is taken. A model is smooth of genus two exactly when \(v(u^2-4v)(1-u+v)\ne0\), since the six branch roots must be nonzero and distinct.

For the entire affine plane the phrase "superspecial equations" refers to the polynomial extension of the smooth-family Cartier-entry equations; at the excluded singular-curve point it does **not** assert the existence of a genus-two Jacobian.

## Proof
Put \(q(T)=(T-1)(T^2-uT+v)=T^3-(1+u)T^2+(u+v)T-v\). The defining sextic is \(f(x)=q(x^2)\). For a smooth genus-two hyperelliptic curve in odd characteristic, the Cartier--Manin matrix in a standard basis of regular differentials has entries obtained from the coefficients \(c_j=[x^j]f(x)^{(p-1)/2}\) at the four positions \(j=p-1,p-2,2p-1,2p-2\), with a possible transpose depending on the basis convention. In characteristic \(p=11\), \(f(x)^5\) is even, so the off-diagonal entries \(c_9\) and \(c_{21}\) vanish. The diagonal entries are
\[
 A(u,v)=[T^5]q(T)^5,\qquad B(u,v)=[T^{10}]q(T)^5.
\]
Thus the scheme of vanishing Cartier operator is exactly \(V(A,B)\) on the smooth base; a genus-two curve has vanishing Cartier operator if and only if its Jacobian is superspecial.

Exact binomial expansion modulo \(11\) gives
\[
\begin{aligned}
A={}&u^5+3u^4v+u^3v^2-2u^3v+u^2v^3-4u^2v^2\\
 &+3uv^4+2uv^3-3uv^2+v^5-5v^4-5v^3,\\
B={}&-u^5-3u^4+2u^3v-u^3+4u^2v-u^2+3uv^2\\
 &-2uv-3u+5v^2+5v-1.
\end{aligned}
\]
The polynomial \(A\) is monic of degree five in \(v\), while \(B\) has degree two in \(v\) with nonzero constant leading coefficient \(5\). Their exact resultant, obtained from the Sylvester determinant, is
\[
 \operatorname{Res}_v(A,B)
 =-(u-2)^{17}(u+1)(u+3)(u+5)(u-3)
 (u^2-5u-1)(u^2-u-4).
\]
The six factors other than \(u-2\) are squarefree and mutually coprime over \(\overline{\mathbb F}_{11}\), of total degree eight. Every simple root of the resultant corresponds to exactly one reduced intersection point of \(V(A,B)\). At \(u=2\), direct polynomial gcd gives
\[
 \gcd(A(2,v),B(2,v))=(v-1)^3(v-3)(v-4)
\]
up to multiplication by a unit. Both \((2,3)\) and \((2,4)\) have Jacobian determinant \(\partial_u A\,\partial_v B-\partial_v A\,\partial_u B=8\ne0\), and hence are transverse reduced intersection points.

There are no intersections at infinity: the homogeneous degree-five part of \(B\) is \(-u^5\), which forces \(u=0\) on the line at infinity, while the homogeneous degree-five part of \(A\) at \(u=0\) is \(v^5\ne0\). Consequently Bezout's theorem, or equivalently the monic-in-\(v\) resultant, gives total affine intersection length \(5\cdot5=25\). The \(u=2\) fiber has total length \(17\) by the resultant exponent; subtracting the two transverse points gives local length \(15\) at \((2,1)\).

Finally, the excluded singular-model boundary consists of \(v=0\), \(v=u-1\), and \(u^2=4v\). Taking the gcd of the two restrictions of \(A,B\) to each boundary component gives respectively \(1\), \((u-2)^5\), and \((u-2)^5\), up to units. The only intersection of \(V(A,B)\) with this boundary is therefore \((u,v)=(2,1)\). All eight simple resultant-root points and the two transverse \(u=2\) points are smooth curves. This proves the claimed ten-plus-fifteen decomposition.

## Verification
Run `python3 verify.py` with Python 3 and SymPy installed. The script reconstructs \(q^5\), the two Cartier coefficients, the degree-\(25\) resultant factorization, boundary-component gcds, the \(u=2\) fiber gcd, and the two nonzero transverse Jacobians with exact finite-field arithmetic. Expected output begins `VERIFY_OK`. The proof of geometric completeness is the intersection/resultant argument above, not a finite-field search.

## Relationship to prior work
Gutierrez and Shaska study hyperelliptic curves with extra involutions and their normal forms; Shaska describes the broader genus-two decomposable-Jacobian setting. Ohashi, in work on Rosenhain forms of superspecial genus-two curves, treats **this exact even-sextic family** as an antecedent to maximality/minimality criteria, but does not in the inspected lemma give the characteristic-eleven scheme cut out by its two Cartier coefficients. Harashita and Yamamoto prove a general multiplicity-one theorem for the genus-two superspecial locus in Rosenhain coordinates. That theorem provides context for reducedness in the smooth moduli space, but does not give the present exact marked-parameter count or the length-\(15\) collision at the excluded singular-curve boundary. Katsura and Takashima explicitly classify the two **abstract isomorphism classes** of superspecial genus-two curves in characteristic eleven (Section 7.2) and describe their Richelot isogenies; this does not determine the ten points in the specified marked-branch parameter space or the length of the extended Cartier intersection on its degenerate boundary. Those are the finite, scheme-theoretic outputs asserted here; no general multiplicity-one theorem or new isomorphism-class classification is claimed.

## Limitations
The ten points need not give ten distinct abstract isomorphism classes. The boundary length is a length of an **extended coefficient-equation intersection**, not a moduli-theoretic genus-two Jacobian at the degenerate parameter. The statement does not classify all superspecial genus-two curves, determine their individual fields of definition, or prove that no equivalently formulated older table exists. The known characteristic-eleven classification has only two abstract isomorphism classes, so the ten marked parameter values are not ten isomorphism classes. Equivalent prior presentations or unexamined tables could cover parts of the computation. No independent mathematical audit is claimed.

## References
- T. Shaska, *Determining the Automorphism Group of a Hyperelliptic Curve*, arXiv:math/0312284 (first public arXiv version 2003-12-15), https://arxiv.org/pdf/math/0312284.
- J. Gutierrez and T. Shaska, *Hyperelliptic Curves with Extra Involutions*, LMS J. Comput. Math. 8 (2005), 102--115; arXiv:math/0601456, https://arxiv.org/pdf/math/0601456.
- R. Ohashi, *On the Rosenhain Forms of Superspecial Curves of Genus Two*, arXiv:2308.11963, especially Lemma 3.3, https://arxiv.org/pdf/2308.11963.
- S. Harashita and Y. Yamamoto, *The Multiplicity-One Theorem for the Superspeciality of Curves of Genus Two*, arXiv:2409.13212, especially Theorem B, https://arxiv.org/pdf/2409.13212.
- T. Katsura and K. Takashima, *Counting Richelot Isogenies between Superspecial Abelian Surfaces*, arXiv:2003.00633, Section 7.2, https://arxiv.org/pdf/2003.00633.
