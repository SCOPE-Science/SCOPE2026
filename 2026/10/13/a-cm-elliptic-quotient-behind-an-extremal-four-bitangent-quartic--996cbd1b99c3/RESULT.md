# A CM elliptic quotient behind an extremal four-bitangent quartic
## Finding
Over \(\mathbb C\), consider the smooth plane quartic
\[
C:\ (X^2+T^2+Z^2)^2+TZ(T+Z)(T+2Z)=0.
\]
Bannai--Tokunaga--Yorisaki obtain this curve in their smooth maximal-concurrency example and identify the four ordinary bitangents
\[
T=-2Z,\qquad T=-Z,\qquad T=0,\qquad Z=0,
\]
which meet at \(p=[1:0:0]\).

The projective involution
\[
\iota[X:T:Z]=[-X:T:Z]
\]
preserves \(C\). On the affine chart \(Z=1\), define
\[
Y=X^2+T^2+1.
\]
Then the quartic equation becomes
\[
Y^2=-T(T+1)(T+2).
\]
Consequently \(C/\langle\iota\rangle\) is the elliptic curve
\[
E:\ Y^2=-T(T+1)(T+2),
\]
and after translating \(s=T+1\) it has the form \(Y^2=s-s^3\), hence \(j(E)=1728\). The fixed divisor of \(\iota\) on \(C\) is \(C\cap\{X=0\}\); it consists of four distinct points. Thus the degree-two map \(C\to E\) has exactly four ramification points, as required by Riemann--Hurwitz for a genus-three curve mapping to a genus-one curve.

The full projective stabilizer of the marked pair \((C,p)\) is
\[
\operatorname{Stab}_{\operatorname{PGL}_3(\mathbb C)}(C,p)=\langle\iota\rangle\cong C_2.
\]
Thus the extremal four-bitangent presentation carries a canonical visible bielliptic involution whose quotient is the square-lattice elliptic curve, but it has no further projective symmetry fixing the distinguished concurrence point.

## Assumptions and scope
The base field is \(\mathbb C\). The point \(p\) is part of the marked split-model presentation: it is the center of the pencil containing the four concurrent ordinary bitangents. The statement concerns projective automorphisms of the marked pair \((C,p)\), not the complete unmarked automorphism group of the abstract genus-three curve.

The source proves that this displayed quartic is smooth and has the four stated concurrent ordinary bitangents. Smoothness is also independently checked from the displayed equation in the included verification script.

## Proof
Write
\[
F=(X^2+q(T,Z))^2+r(T,Z),\qquad q=T^2+Z^2,\qquad r=TZ(T+Z)(T+2Z).
\]
The equation is even in \(X\), so \(\iota\) preserves \(C\). On \(Z=1\), the invariant function \(Y=X^2+T^2+1\) satisfies \(Y^2=-T(T+1)(T+2)\). This gives the quotient function field and shows that the quotient has genus one. Translating \(s=T+1\) gives \(Y^2=s-s^3\), which is isomorphic over \(\mathbb C\) to the Weierstrass form \(y^2=x^3-x\); therefore its \(j\)-invariant is \(1728\).

For the stabilizer, any projective transformation fixing \(p=[1:0:0]\) has a representative of the form
\[
\begin{pmatrix}
a&b&c\\0&d&e\\0&f&h
\end{pmatrix}.
\]
Because \(C\) is a smooth irreducible quartic, preservation of \(C\) means \(F\) is carried to a nonzero scalar multiple \(\lambda F\). Comparing the coefficients of \(X^4,X^3T,X^3Z\) gives \(\lambda=a^4\) and \(b=c=0\). Comparing the \(X^2\)-part and then the constant part gives
\[
q(Mv)=a^2q(v),\qquad r(Mv)=a^4r(v),
\]
where \(v=(T,Z)^t\) and \(M=\begin{psmallmatrix}d&e\\f&h\end{psmallmatrix}\). Setting \(N=M/a\), one has
\[
q(Nv)=q(v),\qquad r(Nv)=r(v).
\]
For \(N=\begin{psmallmatrix}u&v\\w&s\end{psmallmatrix}\), coefficient comparison in these two binary-form identities has Gröbner basis
\[
u-s,\quad v,\quad w,\quad s^2-1.
\]
Hence \(N=I\) or \(N=-I\). Up to projective scalar these give the identity and \(\iota\), respectively, proving the stabilizer claim.

Finally, the fixed points of \(\iota\) on \(C\) lie on \(X=0\). In the affine chart \(Z=1\), their \(T\)-coordinates are the roots of
\[
T^4+T^3+5T^2+2T+1,
\]
whose discriminant is \(4257\neq0\). There is no fixed point of \(C\) on \(X=0,Z=0\), so there are exactly four fixed points.

## Verification
The included `verify.py` performs exact symbolic checks with rational coefficients. It verifies the homogenization, smoothness on projective affine patches, invariance under \(\iota\), the quotient equation, \(j=1728\), the nonzero fixed-point discriminant \(4257\), and the Gröbner-basis calculation proving that the marked projective stabilizer has two elements. A fresh replay from the packaged file returns `VERIFY_OK`.

## Relationship to prior work
Bannai--Tokunaga--Yorisaki construct the quartic from a split model of a rational elliptic surface. Their Example 6.1 gives the equation and proves that the curve is smooth with four concurrent ordinary bitangents at parameters \(-2,-1,0,\infty\). Their paper studies involutions on the ambient elliptic surface, but the inspected full text does not state the induced projective involution of this plane quartic, identify its genus-one quotient, compute its \(j\)-invariant, or determine the projective stabilizer of the marked plane pair.

General work on bielliptic smooth plane quartics explains that genus-three plane quartics with involutions and elliptic quotients form natural automorphism strata. That general framework does not imply the source-specific equation \(E:Y^2=-T(T+1)(T+2)\), its value \(j=1728\), or the exact marked stabilizer without the calculation above.

## Limitations
The stabilizer statement is for the marked pair \((C,p)\). It does not assert that every abstract or projective automorphism of \(C\) fixes \(p\), and therefore it does not determine the complete unmarked automorphism group. The literature comparison used exact equation, quotient, automorphism, and concurrent-bitangent formulations, but an older equivalent computation in different coordinates remains a residual originality risk.

## References
S. Bannai, H.-o. Tokunaga, and E. Yorisaki, “Ramified and Split models of elliptic surfaces and bitangent lines of quartic curves,” arXiv:2304.07717v1, 16 April 2023; later published in Commentarii Mathematici Universitatis Sancti Pauli 71 (2023), 51–69.

E. Badr and F. Bars, “Bielliptic smooth plane curves and quadratic points,” arXiv:1805.02978; International Journal of Number Theory 17 (2021), 1047–1066.
