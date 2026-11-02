# The length-nine low-rank Hasse locus in a genus-three Klein-four family in characteristic seven

## Finding
Let \(k\) be algebraically closed of characteristic \(7\). Within the smooth normalized family
\[
C_{a,b}:\quad y^2=x^8+a x^6+b x^4+a x^2+1,
\]
the Jacobian \(7\)-rank is computed by three explicit polynomials
\[
P=(a-3)(a^2-a-b),\qquad Q=(a+3)(a^2+a-b),\qquad
R=(b+1)(b^2-b-a^2):
\qquad f_7(C_{a,b})=\#\{P,Q,R\ne0\}.
\]
The determinantal scheme where \(f_7\le1\), **restricted to the smooth coefficient surface**, has length \(9\) and support at seven points of \(\mathbb F_7^2\). Six are reduced, transverse rank-one points:
\[
(a,b)=(3,5),(4,5),(3,2),(4,2),(5,6),(2,6).
\]
The seventh is \((0,0)\), the superspecial rank-zero point, with local scheme defined by the square of its maximal ideal and hence length three. Thus the lower-rank scheme is nonreduced at its unique rank-zero point. The claim concerns normalized parameters, not distinct curve isomorphism classes.

## Assumptions and scope
The characteristic is exactly \(7\), and \(a,b\) range over all of \(k\) for which the octic is squarefree. Its exact discriminant over \(\mathbb Z[a,b]\) is
\[
256(2a-b-2)^2(2a+b+2)^2(a^2-4b+8)^4.
\]
Put \(D=(2a-b-2)(2a+b+2)(a^2-4b+8)\). The smooth family is \(D\ne0\) and every member has genus three. The polynomial is invariant under \(x\mapsto-x\) and reciprocal under \(x\mapsto1/x\), giving a Klein-four action by the involutions \((x,y)\mapsto(-x,y)\) and \((x,y)\mapsto(1/x,y/x^4)\); all three nonidentity involution quotients have genus one on the smooth locus. Consequently, the Jacobian splits up to a prime-to-\(7\) isogeny into three elliptic curves. The rank assertions are equivalently the ordinary/supersingular-factor pattern. They are proved directly below without requiring quotient equations.

## Proof
For a squarefree octic defining a genus-three hyperelliptic curve, \(dx/y,x\,dx/y,x^2\,dx/y\) form a basis of holomorphic differentials. The characteristic-\(7\) coefficient-form Cartier–Manin/Hasse–Witt matrix has entries \(H_{ij}=[x^{7i-j}]f(x)^3\) for \(1\le i,j\le3\). Polynomial expansion in \(\mathbb F_7[a,b,x]\) yields
\[
H=\begin{pmatrix}A&0&E\\0&R&0\\E&0&A\end{pmatrix},
\qquad A=a(a^2-b+3),\quad E=3(a^2+b),\quad R=(b+1)(b^2-b-a^2).
\]
Changing from the first and third basis vectors to their sum and difference diagonalizes the coefficient matrix by a transformation defined over \(\mathbb F_7\), because \(2\) is invertible. The resulting diagonal entries are
\[
A+E=(a-3)(a^2-a-b)=P,\quad
A-E=(a+3)(a^2+a-b)=Q,\quad R.
\]
For semilinear Frobenius/Cartier, repeated iteration after this constant-field basis change simply multiplies successive seventh-power twists of the diagonal entries. Their nonvanishing is unchanged by twists. Therefore the stable Frobenius rank, namely the Jacobian \(7\)-rank, equals the number of nonzero entries among \(P,Q,R\); the \(a\)-number equals three minus that number.

The rank-at-most-one scheme is defined by the maximal \(2\times2\) minors of the diagonalized \(3\times3\) matrix, hence by \(I=(PQ,PR,QR)\). Restriction to the smooth locus is computed by saturation \(I:D^\infty\). Lexicographic elimination of the auxiliary inverse \(z\) from \((PQ,PR,QR,zD-1)\) over \(\mathbb F_7[z,b,a]\) gives the exact reduced Gröbner basis (lex \(b>a\))
\[
G=\{b^2-2a^2,\;2a^5+a^3b+3a^3-2ab,\;a^6+a^4+a^2\}.
\]
Its leading monomials are \(b^2,a^3b,a^6\). The nine standard monomials are
\[
1,a,a^2,a^3,a^4,a^5,b,ab,a^2b,
\]
so the saturated zero-dimensional scheme has exact length \(9\) over \(k\). This is a scheme-theoretic bound over the algebraic closure, not a finite-field point-count heuristic.

Direct substitution exhibits seven smooth \(\mathbb F_7\)-points where at least two factors vanish: the origin and the six rank-one points listed above. At each rank-one point precisely two of the factors vanish, with nonzero Jacobian determinant for those two factors: respectively \(1,1,1,1,6,6\) in the displayed order. Each such point is reduced of local length one. At the origin the first-order terms of the three factors are \(3(a+b),3(a-b),-b\), and their three pairwise products span all quadratic forms in \(a,b\). Thus the completed local determinantal ideal has full quadratic initial ideal and defines \(\mathfrak m^2\), of length three. These local contributions sum to \(6+3=9\), exhausting the exact Gröbner length; no additional geometric points or multiplicities exist. At the origin all three factors vanish, and at each of the other six points exactly two vanish, giving ranks zero and one respectively.

## Verification
Run `python verify.py` with the dependency version bounds in `requirements.txt`. The verifier independently expands the octic discriminant over integers, reconstructs the complete characteristic-seven coefficient matrix from \(f^3\), checks its three diagonal eigenfactors, derives the saturated Gröbner basis over \(\mathbb F_7\), counts exactly nine standard monomials, verifies all seven points and their smoothness, and computes the six nonzero Jacobian determinants. An additional complete enumeration of the \(49\) parameter pairs over \(\mathbb F_7\) returns smooth-rank counts \(1,6,12,12\) for ranks \(0,1,2,3\); this last finite-field enumeration is corroborative only. The Gröbner and local-algebra calculations establish completeness over \(k\).

## Relationship to prior work
Gutierrez, Sevilla, and Shaska introduced the genus-three hyperelliptic normal equations and extra-automorphism strata; Shaska and Thompson, Section 5.2.1, explicitly give the reciprocal two-parameter family with a Klein-four reduced automorphism action. These geometric equations are background, not new claims. Moriya and Kudo establish quotient/isogeny algorithms and superspecial genus-three Howe-curve enumeration. The superspecial origin and the possibility of decomposed Jacobians are not claimed as new. The present claim instead classifies the **entire rank-at-most-one parameter scheme** in characteristic seven and its nonreduced multiplicity, including six nonsuperspecial rank-one points. These features are not stated or implied by the inspected geometric parameterizations or superspecial-only classifications. The comparison does not exclude all earlier arithmetic tables or equivalent presentations.

## Limitations
Only this normalized two-parameter coefficient space and characteristic \(7\) are treated. The three involution quotients and the p-rank decomposition are valid on the smooth locus; no claim is made about singular members. The six parameter points need not be six distinct isomorphism classes. This work does not determine full Ekedahl–Oort types or Newton polygons away from the statements made, and historical priority awaits independent scholarly verification.

## References
1. J. Gutierrez, D. Sevilla, and T. Shaska, *Hyperelliptic curves of genus 3 with prescribed automorphism group*, arXiv:1209.2938v1 (13 September 2012), especially Section 3.
2. T. Shaska and F. Thompson, *Bielliptic curves of genus 3 in the hyperelliptic moduli*, arXiv:1305.4501v1 (20 May 2013), especially Section 5.2.1, Equation (23).
3. T. Moriya and M. Kudo, *Some explicit arithmetic on curves of genus three and their applications*, arXiv:2209.02926, especially Theorems 2 and 3.
4. R. Ohashi, *On the maximality of hyperelliptic Howe curves of genus 3*, arXiv:2112.11152 (2021), on superspecial arithmetic.
