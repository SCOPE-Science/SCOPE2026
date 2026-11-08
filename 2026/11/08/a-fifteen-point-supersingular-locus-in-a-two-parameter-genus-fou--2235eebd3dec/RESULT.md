# A fifteen-point supersingular locus in a two-parameter genus-four square-Jacobian family

## Finding
Let \(k=\overline{\mathbb F}_5\). For \(u,v\in k\), put
\[
S_{u,v}(x)=(x^2+1)\bigl(v(x^2+1)^4+4u x^2(x^2+1)^2+16x^4\bigr)
\]
and let \(X_{u,v}\) be the smooth projective model of \(y^2=S_{u,v}(x)\). The exact smooth parameter locus is
\[
\mathcal U=\{(u,v)\in k^2:v(u^2-4v)(1+u+v)\ne0\}.
\]
Define, with all coefficients reduced modulo \(5\),
\[
P(u,v)=2u^3+u^2+(2-u^2-2u)v,
\quad H(u)=u^{15}-u^{11}+2u^{10}-2u^6-u^5+2u+1.
\]
For every \((u,v)\in\mathcal U\), the Newton polygon, \(5\)-rank, and Cartier \(a\)-number of \(\operatorname{Jac}(X_{u,v})\) are exactly as follows:

| Condition | \(5\)-rank | \(a\)-number | Newton slopes, with multiplicity |
| --- | ---: | ---: | --- |
| \(P(u,v)\ne0\) | \(4\) | \(0\) | \(0\) four times and \(1\) four times |
| \(P(u,v)=0,\ H(u)\ne0\) | \(2\) | \(2\) | \(0\) twice, \(\tfrac12\) four times, \(1\) twice |
| \(P(u,v)=H(u)=0\) | \(0\) | \(2\) | \(\tfrac12\) eight times |

The supersingular locus consists of **exactly fifteen distinct smooth geometric coefficient pairs**. One is \((u,v)=(-1,2)=(4,2)\) over \(\mathbb F_5\). The remaining fourteen form a single degree-\(14\) Frobenius orbit. Thus, no member of this smooth family is superspecial, including its supersingular members. These statements count normalized coefficient pairs, **not isomorphism classes**.

## Assumptions and scope
Throughout, the characteristic is \(5\), \(k\) is algebraically closed, and parameters range over the stated smooth locus; all polynomial identities involving parameters are in \(\mathbb F_5[u,v]\). For the Frobenius-orbit assertion, the equations are defined over \(\mathbb F_5\). By \(5\)-rank we mean the dimension over \(\mathbb F_5\) of geometric \(5\)-torsion, and by Cartier \(a\)-number the dimension of the kernel of Cartier on global regular differentials. Supersingular means all Newton slopes are \(\tfrac12\); superspecial would require \(a=4\).

## Proof
**1. Smoothness.** Set \(t=x^2\) and
\[
R(t)=v(t+1)^4+4ut(t+1)^2+16t^2.
\]
Away from \(t=-1\), divide by \((t+1)^4\) and put \(w=4t/(t+1)^2\): this gives \(R(t)/(t+1)^4=w^2+uw+v\). The map \(x\mapsto w=4x^2/(x^2+1)^2\) is only ramified at \(x=0,\pm1\) away from its poles, with branch values \(0,1\); its poles are not roots of \(R\), since \(R(-1)=16\ne0\). Therefore \(R(x^2)\) has eight distinct roots disjoint from the two roots of \(x^2+1\) exactly when \(v(u^2-4v)(1+u+v)\ne0\). In that case \(S\) is squarefree of degree ten and \(X\) is smooth of genus four. If a factor vanishes, a multiple root occurs (or the polynomial degree drops), so this criterion is exact.

**2. Two genus-two factors.** On \(X\) there are commuting involutions \((x,y)\mapsto(-x,y)\) and \((x,y)\mapsto(-x,-y)\), whose product is the hyperelliptic involution. Their quotient curves are
\[
D_+:Y^2=(t+1)R(t),\qquad D_-:Y^2=t(t+1)R(t).
\]
Both quotients have genus two, and their pullbacks to \(\operatorname{Jac}(X)\) give an isogeny from \(\operatorname{Jac}(D_+)\times\operatorname{Jac}(D_-)\) with \(2\)-power kernel. To see this, the two involution-eigenspaces in \(H^0(X,\Omega^1)\) each have dimension two and are complementary; the associated norm/pullback identities kill the finite kernel by a power of \(2\). In characteristic five this is a prime-to-\(5\) isogeny.

Write \(s=(t-1)/(t+1)\), and set \(U=-u-2\), \(V=1+u+v\). Direct substitution gives
\[
R(t)=(t+1)^4\bigl(s^4+Us^2+V\bigr).
\]
Rescaling the square coordinates (over \(k\)) identifies \(D_+\) with \(z^2=(1-s)(s^4+Us^2+V)\) and \(D_-\) with \(z^2=(1+s)(s^4+Us^2+V)\). The substitution \(s\mapsto-s\) identifies these curves. Consequently, \(\operatorname{Jac}(X_{u,v})\) is prime-to-\(5\) isogenous to the square of the genus-two Jacobian
\[
C_{U,V}:z^2=(s^4+Us^2+V)(s+1).
\]
The parameter involution \(T(u,v)=(-u-2,1+u+v)\) preserves \(\mathcal U\): it swaps \(v\) with \(1+u+v\) and fixes \(u^2-4v\).

**3. Cartier and stable Frobenius ranks.** For arbitrary smooth \(C_{a,b}:z^2=(s^4+as^2+b)(s+1)\), write \(f(s)=(s^4+as^2+b)(s+1)\). The characteristic-five Cartier--Manin coefficient matrix, from the coefficients of \(f(s)^2\) in positions \(5i-j\) for \(1\le i,j\le2\), is
\[
M(a,b)=\begin{pmatrix} A&4ab\\2&D\end{pmatrix},\qquad A=a^2+2ab+2b,\quad D=2a+1.
\]
Its determinant is \(P(a,b)=AD-8ab\). Since the lower-left entry is \(2\), its rank is exactly two when \(P\ne0\) and exactly one when \(P=0\). On the rank-one locus \(M=\binom{A}{2}(1,D/2)\), so \(MM^{(5)}=0\) exactly when \(A^5+D=0\). (Here \(M^{(5)}\) denotes entrywise fifth powers.) In genus two the stable Frobenius rank is \(2,1,0\), according as \(P\ne0\), \(P=0\) but \(MM^{(5)}\ne0\), or \(MM^{(5)}=0\). Thus these cases give respectively genus-two \(5\)-ranks \(2,1,0\), with \(a\)-numbers \(0,1,1\). A genus-two \(5\)-rank-zero Jacobian is supersingular, while the \(5\)-rank-one Newton slopes are \(0,\tfrac12,\tfrac12,1\). Doubling the factors under the prime-to-five isogeny gives the three genus-four rows.

**4. Elimination and exact cardinality.** Write
\[
L(a)=2-a^2-2a,\qquad K(a)=a^2(2a+1),\qquad P(a,b)=L(a)b+K(a).
\]
The polynomials \(L,K\) are coprime. Hence \(P=0\) forces \(L(a)\ne0\) and \(b=-K(a)/L(a)\). Substitution gives \(L(a)A=2a^3\). Therefore the remaining rank-zero condition is equivalent to
\[
(2a^3)^5+(2a+1)L(a)^5=2H(a)=0.
\]
The separability certificate \(\gcd(H,H')=1\) shows exactly fifteen roots in \(k\). None is excluded by smoothness, since
\[
\gcd\bigl(H,L\bigr)=\gcd\bigl(H,K\bigr)
=\gcd\bigl(H,a^2L+4K\bigr)
=\gcd\bigl(H,(a+1)L-K\bigr)=1.
\]
All fifteen therefore give distinct smooth pairs \((a,b)\). The inverse involution \(T\) gives fifteen distinct smooth original pairs \((u,v)\). The identities \(P(T(u,v))=P(u,v)\) and \(H(-u-2)=-H(u)\) yield the simple displayed stratification in original coordinates.

Finally,
\[
H(a)=(a+1)J(a),
\]
where
\[
J(a)=a^{14}-a^{13}+a^{12}-a^{11}+2a^9-2a^8+2a^7-2a^6-a^4+a^3-a^2+a+1.
\]
The degree-\(14\) factor \(J\) is irreducible over \(\mathbb F_5\). A reproducible Rabin test verifies the three conditions \(a^{5^{14}}\equiv a\pmod J\), \(\gcd(J,a^{5^7}-a)=1\), and \(\gcd(J,a^{5^2}-a)=1\). The linear root of \(H\) is \(a=-1\), with \(b=2\), and this pair is fixed by \(T\). This proves the Frobenius-orbit assertion and completes the theorem.

## Verification
Run `python3 verify.py` with Python 3.8 or later in this package. The independent standard-library script recomputes all four entries of the Cartier coefficient matrix from the square of the genus-two defining polynomial, verifies elimination identities and the exact degree-fifteen polynomial, proves squarefreeness and smoothness by Euclidean gcd computations, executes the Rabin irreducibility test, exhaustively checks all smooth \(\mathbb F_5\)-parameters, and counts projective points of the unique rational supersingular member over \(\mathbb F_5\) and \(\mathbb F_{25}\) using an explicit finite-field arithmetic model. Expected terminal marker: `VERIFY_SQUARE_JAC_P5_OK`. The counts for this parameter are \((\#C(\mathbb F_5),\#X(\mathbb F_5))=(6,6)\) and \((\#C(\mathbb F_{25}),\#X(\mathbb F_{25}))=(26,26)\). These counts are cross-checks, not the proof of geometric supersingularity.

## Relationship to prior work
Bruin and Kulkarni, *On (2,2)-decomposable genus 4 Jacobians*, arXiv:2309.01959v1 (first posted September 5, 2023), Example 7.3, give this remarkable two-parameter hyperelliptic square-Jacobian family. Their theorem concerns decomposability and moduli, not the characteristic-five complete Newton and Cartier strata or the fifteen-point locus. Kudo, Harashita, and Senda, *The existence of supersingular curves of genus 4 in arbitrary characteristic*, arXiv:1903.08095 (2019), prove existence using Howe curves and explicitly use the genus-two Cartier-matrix supersingularity criterion. Their existence result does not classify this distinct square-Jacobian family. The classical Cartier--Manin formula and genus-two Newton polygon taxonomy are established inputs, not claimed innovations. Earlier calculations of this exact family already identified its nonordinary divisor and the one supersingular pair rational over \(\mathbb F_5\); neither fact is claimed new here. The additional contribution is an exhaustive geometric supersingular classification: the remaining fourteen parameters form a single irreducible degree-fourteen orbit, the nonordinary divisor has \(5\)-rank two away from these fifteen points, and the associated Newton-polygon classification is complete.

## Limitations
The theorem concerns smooth members of the specified marked two-parameter family over \(\overline{\mathbb F}_5\); it does not classify all genus-four curves or give distinct moduli-isomorphism classes. It does not calculate individual finite-field zeta functions. A previously unlocated equivalent specialization in an older supersingular-genus-two table is a residual priority risk. Independent mathematical validation has not been performed.

## References
1. N. Bruin and A. Kulkarni, *On (2,2)-decomposable genus 4 Jacobians*, arXiv:2309.01959v1, September 5, 2023, especially Example 7.3. https://arxiv.org/html/2309.01959v1
2. M. Kudo, S. Harashita, and H. Senda, *The existence of supersingular curves of genus 4 in arbitrary characteristic*, arXiv:1903.08095, March 19, 2019; Research in Number Theory 6 (2020), 44, especially Sections 1--2. https://link.springer.com/article/10.1007/s40993-020-00217-x
3. D. Harvey and A. V. Sutherland, *Computing Hasse--Witt matrices of hyperelliptic curves in average polynomial time*, arXiv:1402.3246, February 13, 2014. https://arxiv.org/abs/1402.3246
