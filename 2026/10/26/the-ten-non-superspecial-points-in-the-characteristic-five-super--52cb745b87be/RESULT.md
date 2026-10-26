# The ten non-superspecial points in the characteristic-five supersingular Howe parameter locus

## Finding

Let \(k=\overline{\mathbb F}_5\). For \(\lambda\in k\) and \(A,B\in k^\times\), put
\[
f_1(x)=x^3+A,\qquad f_2(x)=(x-\lambda)^3+B.
\]
Assume \(f_1\) and \(f_2\) are coprime, and write \(H_{\lambda,A,B}\) for the smooth projective normalization of the fiber product of the elliptic double covers \(z^2=f_1(x)\) and \(w^2=f_2(x)\). This is a genus-four Howe curve. Its Jacobian is supersingular **if and only if** one of the following mutually exclusive conditions holds:

1. \(\lambda=0\) and \(B=-A\). Then the Jacobian has \(a\)-number \(4\). This superspecial boundary is already known, not claimed as new.
2. \(\lambda\ne0\). Set \(a=A/\lambda^3\), \(b=B/\lambda^3\) and \(s=a+b\). Then
\[
a=3s^2+3s-1,\qquad b=2s^2+3s+1,
\qquad h(s):=2s^{10}+2s^8-s^6+1=0
\]
in characteristic five. Every one of the ten distinct geometric roots of \(h\) gives a valid, smooth Howe curve whose Jacobian has \(a\)-number exactly \(3\), hence is supersingular but **not** superspecial.

The exact factorization over the prime field is
\[
h(s)=2(s^3+s^2+2)(s^3-s^2-2)(s^4+2s^2-2),
\]
where both cubics and the quartic are irreducible. Thus six of the ten normalized nonzero-shift parameters have minimal field of definition \(\mathbb F_{125}\), and the other four have minimal field of definition \(\mathbb F_{625}\). In particular there is no nonzero-shift supersingular member over \(\mathbb F_5\) or \(\mathbb F_{25}\) with these coordinate-marked equations.

For every integer \(m\ge1\), with \(q=5^m\), the **number of coefficient-marked triples** \((\lambda,A,B)\in\mathbb F_q\times(\mathbb F_q^\times)^2\) satisfying the coprimality hypothesis and yielding supersingular \(H_{\lambda,A,B}\) is exactly
\[
(q-1)\bigl(1+6\mathbf 1_{3\mid m}+4\mathbf 1_{4\mid m}\bigr).
\]
There are \(q-1\) known superspecial triples with \(\lambda=0\), and \((q-1)(6\mathbf 1_{3\mid m}+4\mathbf 1_{4\mid m})\) non-superspecial triples. In particular the total marked counts for \(q=5,25,125,625\) are \(4,24,868,3120\).

## Assumptions and scope

All geometric supersingularity assertions concern the Jacobians after base extension to \(k\). Smoothness requires \(A,B\ne0\) and \(\gcd(f_1,f_2)=1\); the two cubic polynomials are then separable and share only their projective branch point at infinity. The count concerns the **specified monic cubic presentations with a fixed affine coordinate \(x\)**, not equivalence classes of curves or of presentations. The normalizing operation for \(\lambda\ne0\) rescales \(x\) by \(\lambda\), and does not purport to identify all quadratic twists over \(\mathbb F_q\). The classification ranges over every algebraic extension of \(\mathbb F_5\) and every admissible parameter triple in the displayed family.

This is a natural characteristic-five subclass: each supersingular elliptic curve in characteristic five has \(j=0\) over \(k\), hence the short-Weierstrass cubic in the standard Howe description can be chosen with vanishing linear term. The result is deliberately stated for normalized marked equations; no count of abstract genus-four isomorphism classes is inferred.

## Proof

**1. Genus and Jacobian decomposition.** The two cubic double covers of \(\mathbb P^1\) have disjoint sets of three finite simple branch points, and a single common branch point at infinity. Their normalized fiber product has genus \(4\). The involution-quotient decomposition of Howe gives a pair of degree-two isogenies, whose composites are multiplication by two, between \(J(H)\) and \(E_1\times E_2\times J(C)\), where \(C:y^2=f_1f_2\) has genus two. As \(2\) is invertible in characteristic five, this identifies their \(5\)-torsion group schemes. Both \(E_i\) have \(j=0\) and are supersingular. Therefore
\[
J(H)\text{ supersingular}\quad\Longleftrightarrow\quad J(C)\text{ supersingular},
\qquad a(H)=2+a(C).
\]
These decomposition and Cartier criteria are due to earlier authors and are not asserted here as discoveries.

**2. Explicit Cartier--Manin matrix.** Write \(f(x)=f_1(x)f_2(x)\). In the differential basis \(dx/y,x\,dx/y\), use the matrix of coefficients \(\gamma_4,\gamma_9,\gamma_3,\gamma_8\) of \(f(x)^2\), with the convention of Kudo--Harashita--Senda. Direct binomial expansion modulo five yields
\[
M=\begin{pmatrix}
 A\lambda^2(3\lambda^3+2B)&2(A+B)\\
 A(2\lambda^6+B\lambda^3+2AB+2B^2)&\lambda(3A+4B)
\end{pmatrix}.
\]
For a genus-two curve in odd characteristic, supersingularity is equivalent to \(M M^{(5)}=0\), where \(M^{(5)}\) denotes entrywise fifth power. The \(a\)-number is \(2-\operatorname{rank}(M)\).

**3. Zero-shift case.** At \(\lambda=0\), the matrix is
\[
M=\begin{pmatrix}0&2(A+B)\\2AB(A+B)&0\end{pmatrix}.
\]
Because \(AB\ne0\), the product \(MM^{(5)}\) vanishes exactly if \(A+B=0\). Then \(M=0\), so \(a(C)=2\) and \(a(H)=4\). Coprimality follows since \(A\ne B=-A\) in characteristic five. The resulting superspecial construction appears in the earlier Howe-curve literature.

**4. Nonzero-shift elimination.** For \(\lambda\ne0\), substitute \(x=\lambda t\), \(a=A/\lambda^3\), \(b=B/\lambda^3\). Multiplying the degree-six equation by a nonzero constant does not affect supersingularity, and the normalized matrix is the \(\lambda=1\) case of the preceding formula. Direct expansion gives
\[
\det M=ab\bigl((a+b)^2-a+b-2\bigr).
\]
The nilpotence condition forces \(\det M=0\). Since \(ab\ne0\), putting \(s=a+b\) and solving the two linear relations yields exactly
\[
a=3s^2+3s-1,\qquad b=2s^2+3s+1.
\]
At these substitutions, \(M_{12}=2s\). The final polynomial will have nonzero constant term, so all its roots have \(s\ne0\). For any rank-one \(2\times2\) matrix \(\bigl(\begin{smallmatrix}u&v\\w&z\end{smallmatrix}\bigr)\) with \(v\ne0\), the identity \(MM^{(5)}=0\) is equivalent to \(u v^4+z^5=0\): use \(uz=vw\) (the determinant relation), and factor the rank-one rows. Here
\[
u=2s^4-s^2-s,\quad v=2s,\quad z=2s^2+s+1,
\]
so this identity is exactly
\[
(2s^4-s^2-s)s^4+(2s^2+s+1)^5
=2s^{10}+2s^8-s^6+1=0.
\]
Conversely, every admissible root of this polynomial forces the rank-one matrix to be nilpotent under the semilinear composition, proving supersingularity. Its nonzero \(v\) gives \(\operatorname{rank}(M)=1\), hence \(a(C)=1\), \(a(H)=3\).

**5. All roots are admissible and the field count is exact.** Modulo five the product \(h=2uvw\) has monic irreducible factors
\[
u=s^3+s^2+2,\quad v=s^3-s^2-2,\quad w=s^4+2s^2-2.
\]
Irreducibility follows from the standard polynomial Frobenius tests: each cubic has no prime-field root, and the quartic has no root and no irreducible quadratic factor (equivalently the Euclidean gcd tests with \(s^{5}-s\) and \(s^{25}-s\) both give \(1\)). These factors are distinct. Furthermore,
\[
\operatorname{Res}_x\bigl(x^3+a,(x-1)^3+b\bigr)
=-s^6+s^4+2s^2-2=-(s^2-1)(s^4-2).
\]
Euclidean division over \(\mathbb F_5[s]\) gives
\[
\gcd(h,s)=\gcd(h,3s^2+3s-1)=\gcd(h,2s^2+3s+1)
=\gcd(h,(s^2-1)(s^4-2))=1.
\]
Thus all ten geometric roots give nonzero \(a,b\), nonzero \(s\), and coprime cubics. The irreducible-factor degrees imply exactly \(6\mathbf 1_{3\mid m}+4\mathbf 1_{4\mid m}\) roots in \(\mathbb F_{5^m}\). For every nonzero \(\lambda\) there is a unique \((A,B)=(\lambda^3a,\lambda^3b)\) for each such root. When \(\lambda=0\), the known branch contributes the \(q-1\) possibilities \(A\in\mathbb F_q^\times\), \(B=-A\). Summing proves the stated count.

## Verification

The standalone standard-library file `verify.py` performs arithmetic in \(\mathbb F_5\), \(\mathbb F_{25}\), \(\mathbb F_{125}\), and \(\mathbb F_{625}\). It checks the displayed factorization, irreducibility and gcd certificates, recomputes the Cartier matrix by independent direct expansion of \(f^2\), verifies the resulting semilinear nilpotence and smoothness at all ten roots, and exhaustively enumerates admissible triples for \(q=5\) and \(q=25\). Invoking `python3 verify.py` prints `VERIFY_OK`. The algebraic polynomial identities and the proof of the classification, rather than finite enumeration, establish the theorem over all extensions.

## Relationship to prior work

Kudo--Harashita--Senda (2019 preprint) proved the Howe-curve isogeny decomposition and supersingularity criterion, and proved existence of supersingular genus-four Howe curves in every characteristic greater than three. Kudo--Harashita--Howe (2020) treat the superspecial locus, in particular the known zero-shift construction when the characteristic is congruent to five modulo six; this known special case is included solely to make the **present marked-family classification complete**. Kudo--Harashita (2016) classify superspecial genus-four curves in small characteristics. Ohashi (2026) studies superspecial generalized Howe families with completely decomposable Jacobians. The present narrower-but-different determination is the complete non-superspecial \(a=3\) arithmetic parameter locus in characteristic five, its irreducible field-of-definition decomposition and its exact coefficient-marked census. It is **not** a claim to a new genus-four existence theorem or a new superspecial curve.

## Limitations

The formula counts coordinate-marked models, not distinct isomorphism classes or quadratic twists. No explicit Hasse--Weil zeta polynomial of any individual Howe curve is claimed. The original authors' general criterion is a main premise, and unpublished or unindexed earlier characteristic-five calculations may overlap the explicit elimination. The standalone finite checks do not substitute for the complete symbolic argument above. No independent audit or independent validation has been performed.

## References

1. M. Kudo, S. Harashita, H. Senda, *The existence of supersingular curves of genus 4 in arbitrary characteristic*, arXiv:1903.08095 (first public 2019-03-19), and *Research in Number Theory* 6 (2020), article 44, doi:10.1007/s40993-020-00217-x.
2. M. Kudo, S. Harashita, E. W. Howe, *Algorithms to enumerate superspecial Howe curves of genus 4*, arXiv:2006.11499 (2020), especially Section 5.
3. M. Kudo, S. Harashita, *Superspecial curves of genus 4 in small characteristic*, arXiv:1607.01114 (2016).
4. R. Ohashi, *Superspecial generalized Howe curves of genus 4, 5, and 6 with completely decomposable Jacobians*, arXiv:2604.18074 (2026).
