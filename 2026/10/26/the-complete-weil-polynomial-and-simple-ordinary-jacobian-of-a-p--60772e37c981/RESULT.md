# The complete Weil polynomial and simple ordinary Jacobian of a plane-filling sextic over \(\mathbb F_3\)

## Finding

Let \(C\subset\mathbb P^2_{\mathbb F_3}\) be defined by
\[
F(X,Y,Z)=X^5Y+X^5Z-X^3Y^3+X^3Z^3+XZ^5+Y^5Z-Y^3Z^3=0.
\]
This is the \(q=3,\ k=2\) member of the degree-\(q+3\) plane-filling pencil introduced by Asgarli and Ghioca [AG]. It is a geometrically smooth plane sextic of genus \(10\), containing all \(13\) points of \(\mathbb P^2(\mathbb F_3)\). Its Hasse--Weil zeta function is exactly
\[
Z(C/\mathbb F_3,T)=\frac{L(T)}{(1-T)(1-3T)},
\]
where \(L(T)=\sum_{i=0}^{20}c_iT^i\). The coefficient vector, ordered by ascending power, is
\[
\begin{split}
(c_0,\ldots,c_{20})={}&(1,9,46,173,527,1377,3198,6775,13353,24841,44020,\\
&74523,120177,182925,259038,334611,384183,378351,301806,177147,59049).
\end{split}
\]
The polynomial \(L(T)\) is irreducible over \(\mathbb Q\), already irreducible modulo \(23\). The Jacobian \(J(C)\) is therefore **simple over \(\mathbb F_3\)**. Since \(c_{10}=44020\not\equiv0\pmod3\), \(J(C)\) is ordinary, with \(3\)-rank \(10\) and \(a\)-number \(0\). No geometric absolute-simplicity assertion is made.

## Assumptions and scope

All equations are interpreted in characteristic \(3\). The polynomial in [AG, Equation (1)] is
\[
X^2(X^qY-XY^q)+Y^2(Y^qZ-YZ^q)+(Z^2+kX^2)(Z^qX-ZX^q).
\]
Setting \(q=3\) and \(k=2\) gives precisely the displayed \(F\). Smoothness, the Weil polynomial and the base-field isogeny conclusion concern this one fixed \(\mathbb F_3\)-model. The given coefficient vector determines all extension-field point counts, not merely those explicitly enumerated below. The previous existence/smoothness and ordinarity context for this pencil is acknowledged and not presented as the new claim; the exact Frobenius polynomial and simplicity are the new arithmetic conclusions.

## Proof

**1. Geometric smoothness.** Differentiating the sextic in characteristic \(3\) gives
\[
F_X=2X^4(Y+Z)+Z^5,\qquad
F_Y=X^5+2Y^4Z,\qquad
F_Z=X^5+2XZ^4+Y^5.
\]
On \(Z=0\), if \(X\ne0\) then \(F_Y=X^5\ne0\), while at \([0:1:0]\) one has \(F_Z=1\). Thus no point at infinity is singular. On \(Z=1\), put \(x=X/Z\), \(y=Y/Z\). A common zero of the partial derivatives must satisfy
\[
x^4(y+1)=1,\qquad x^5=y^4,\qquad x=y^4(y+1).
\]
The latter two identities follow directly from \(F_Y=F_Z=0\), and together with the first are equivalent to the common-gradient condition. Consequently, \(y\) must satisfy
\[
G(y)=y^{16}(y+1)^5-1=0.
\]
Substitution of \(x=y^4(y+1)\) in \(F(x,y,1)\), followed by division by \(G(y)\), leaves
\[
R(y)=-y^{18}+y^{12}-y^4-y^3.
\]
The Euclidean algorithm in \(\mathbb F_3[y]\) yields \(\gcd(G,R)=1\), as reproduced in `check_arithmetic.py`. Hence no common-gradient zero lies on the curve. The plane sextic is geometrically smooth, therefore geometrically irreducible by Bézout, and its genus is \((6-1)(6-2)/2=10\). Its rational-point set is all \(\mathbb P^2(\mathbb F_3)\) because each Frobenius alternating binomial vanishes there; this also independently checks the first enumerated count.

**2. Exact point counts.** In the affine chart \(Z=1\), the equation reads
\[
f_x(y)=y^5-(x^3+1)y^3+x^5y+x^5+x^3+x=0.
\]
For any \(m\ge1\) and \(Q=3^m\), the number of distinct \(\mathbb F_Q\)-roots of \(f_x\) equals
\[
\deg\gcd\bigl(f_x(y),\ y^Q-y\bigr)
\]
in \(\mathbb F_Q[y]\), including when \(f_x\) itself is not squarefree. At infinity, \(F(X,Y,0)=X^3Y(X^2-Y^2)\) has exactly four distinct rational projective zeros over every \(\mathbb F_{3^m}\). Therefore
\[
\#C(\mathbb F_Q)=4+\sum_{x\in\mathbb F_Q}\deg\gcd\bigl(f_x(y),\ y^Q-y\bigr).
\]
The exact values for \(m=1,\ldots,10\), computed by a complete field-element traversal in `verify.cpp`, are:

| \(m\) | \(\#C(\mathbb F_{3^m})\) |
|---:|---:|
| 1 | 13 |
| 2 | 21 |
| 3 | 34 |
| 4 | 73 |
| 5 | 288 |
| 6 | 708 |
| 7 | 2253 |
| 8 | 6529 |
| 9 | 19681 |
| 10 | 58236 |

The field representation uses degree-\(m\) monic polynomials over \(\mathbb F_3\) listed directly in the program. The program confirms that the distinguished residue class has multiplicative period exactly \(3^m-1\) and visits each nonzero residue class once; hence these quotient rings are fields, with every field element traversed. It then computes \(y^{3^m}\bmod f_x\) by ten or fewer successive cubings and determines each gcd exactly. For \(m\le5\), the verifier also makes a separate direct examination of all affine pairs and checks agreement with the gcd method. There is no random sampling or uncompleted finite search.

**3. Exact Weil polynomial.** Set \(s_m=3^m+1-\#C(\mathbb F_{3^m})\) and \(c_0=1\). Newton identities give, for \(1\le k\le10\),
\[
k c_k=-\sum_{i=1}^k c_{k-i}s_i.
\]
They yield the first eleven displayed coefficients. For a smooth genus-ten curve over \(\mathbb F_3\), the Weil functional equation gives
\[
c_{20-k}=3^{10-k}c_k\qquad(0\le k\le10),
\]
which supplies the other ten without additional enumeration. `check_arithmetic.py` recomputes all twenty-one coefficients and checks every integer division.

**4. Irreducibility and ordinarity.** Reduction of \(L(T)\) modulo \(23\) has degree \(20\). Rabin's irreducibility criterion is satisfied: for \(j=4,10\),
\[
\gcd\bigl(L(T),T^{23^j}-T\bigr)=1\quad\text{in }\mathbb F_{23}[T],
\]
and \(T^{23^{20}}\equiv T\pmod{L(T)}\). These three checks are verified using only modular polynomial arithmetic in `check_arithmetic.py`. Hence \(L\) is irreducible over \(\mathbb F_{23}\) and therefore over \(\mathbb Q\). A reducible isogeny decomposition of the Jacobian over \(\mathbb F_3\) would factor its rational Frobenius polynomial; this is impossible. Finally, the coefficient in degree \(10\) of the Weil numerator is nonzero modulo \(3\), so the \(3\)-rank is maximal, equal to the genus. Thus the Jacobian is ordinary and its \(a\)-number is zero.

## Verification

Compile and run `verify.cpp` using `g++ -O3 -std=c++17 verify.cpp -o check && ./check`. The program prints all ten exact point counts and finishes with `VERIFY_OK`. Run `python3 check_arithmetic.py` separately; it checks the smoothness elimination identity and gcd, reconstructs the full Weil polynomial, checks its mod-\(23\) irreducibility and ordinarity, then finishes with `VERIFY_ARITHMETIC_OK`. Neither program needs a network connection or specialized computer-algebra libraries.

## Relationship to prior work

Asgarli and Ghioca [AG] introduced the degree-\(q+3\) plane-filling pencil, the rational-point smoothness criterion, and related existence questions. Its characteristic-three smooth member and ordinary status were known within accessible earlier arithmetic investigations. The present claim does **not** assert new construction, smoothness, plane-filling property, genus or generic ordinarity. It assigns the complete degree-\(20\) Weil polynomial to this natural specimen and proves that its ordinary ten-dimensional Jacobian is simple over its base field. An exact prior table or unpublished calculation containing this same polynomial or a stronger arithmetic theorem would subsume the new claim; no such coverage was located in the checked materials.

## Limitations

Simplicity is asserted over \(\mathbb F_3\), not after all field extensions. No assertion is made about the geometric endomorphism algebra, automorphism group or isomorphism classes of other sextics. The count certificates are finite, complete checks through extension degree ten, supplemented by the general Weil functional equation; they do not assume that finite experiments alone prove an infinite statement. Absence of a matching literature record is not proof of absolute priority, and unindexed zeta-function computations remain a residual originality risk.

## References

[AG] S. Asgarli and D. Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072v1, first public 2023-07-06; full text https://arxiv.org/html/2307.03072v1. In particular Equation (1), Theorem 1.2, Conjecture 1.5, and Sections 2--4.

[HK] M. Homma and S. J. Kim, *Nonsingular plane filling curves of minimum degree over a finite field and their automorphism groups: Supplements to a work of Tallini*, earlier foundational work cited in [AG]; not a source for the new sextic zeta computation.
