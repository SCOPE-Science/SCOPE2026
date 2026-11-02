# Complete dyadic quotient-set closures for the quartics \(X^4+cX^2\)

## Finding
For every odd integer \(c\), define \(f_c(X)=X^4+cX^2\), and put
\[
R_c=\left\{\frac{f_c(a)}{f_c(b)}:a,b\in\mathbb Z_{>0},\ f_c(b)\ne0\right\}\subset\mathbb Q.
\]
Write \(U=\mathbb Z_2^\times\), \(U_4=1+4\mathbb Z_2\), and define three index-two open subgroups of \(\mathbb Q_2^\times\):
\[
H_1=\bigcup_{j\in\mathbb Z}2^jU_4,\qquad
H_3=\bigcup_{j\in\mathbb Z}2^{2j}U,\qquad
H_5=\bigcup_{j\in\mathbb Z}2^j(-1)^jU_4.
\]
Then the following complete classification holds:
\[
\boxed{\quad
\overline{R_c}^{\,\mathbb Q_2}=
\begin{cases}
\{0\}\cup H_1,&c\equiv1\pmod8,\\
\{0\}\cup H_3,&c\equiv3\pmod8,\\
\{0\}\cup H_5,&c\equiv5\pmod8,\\
\mathbb Q_2,&c\equiv7\pmod8.
\end{cases}\quad}
\]
The non-dense cases thus realize three distinct open index-two subgroups, not merely three congruence obstructions. In particular, \(R_c\) is dense in \(\mathbb Q_2\) exactly when \(c\equiv7\pmod8\).

## Assumptions and scope
All statements quantify over every odd \(c\in\mathbb Z\), including negative \(c\). Zero polynomial values are allowed in the numerator and excluded from denominators. Valuations are normalized by \(\nu_2(2)=1\). The closure is taken in the usual field topology of \(\mathbb Q_2\). The theorem makes no assertion about even coefficients, other primes, or the real closure of the ratio set.

## Proof
**1. From integer inputs to dyadic inputs.** Positive integers are dense in \(\mathbb Z_2\). Since polynomial evaluation is continuous, and division is continuous when the denominator is nonzero, the closure of \(R_c\) equals the closure of all dyadic quotients \(f_c(x)/f_c(y)\), with \(x,y\in\mathbb Z_2\) and \(f_c(y)\ne0\). Conversely, every such dyadic quotient is approximated by quotients at positive integers with nonvanishing denominators.

**2. A ball-isometry lemma.** The squares of dyadic units comprise exactly \(1+8\mathbb Z_2\). For odd \(c\) and every \(k\ge0\), let \(g_k(t)=t(c+2^{2k}t)\) on \(B=1+8\mathbb Z_2\). When \(t,s\in B\),
\[
g_k(t)-g_k(s)=(t-s)\bigl(c+2^{2k}(t+s)\bigr).
\]
The factor in parentheses is odd, including when \(k=0\) because \(t+s\) is even. Thus \(g_k\) is an exact \(2\)-adic isometry on \(B\). Moreover \(g_k(t)\equiv g_k(1)\pmod8\). For each \(N\ge3\), the \(2^{N-3}\) inputs in \(B\pmod{2^N}\) have distinct images, and therefore fill the \(2^{N-3}\) elements of the ball \(g_k(1)+8\mathbb Z_2\pmod{2^N}\). Compactness yields the exact identity
\[
\boxed{g_k(B)=c+2^{2k}+8\mathbb Z_2}\qquad(k\ge0).
\]
For completeness, the unit-square assertion follows from the standard square-root lifting: every odd square is \(1\pmod8\), while any \(t\equiv1\pmod8\) has roots modulo \(8\), and a root modulo \(2^N\) can be lifted modulo \(2^{N+1}\) by adding either \(0\) or \(2^{N-1}\) for \(N\ge3\); compatibility gives a dyadic square root.

**3. Exact dyadic images on each input-valuation stratum.** If \(x\) is odd, put \(t=x^2\in B\). Then \(f_c(x)=g_0(t)\), so
\[
\{f_c(x):x\in\mathbb Z_2^\times\}=c+1+8\mathbb Z_2.
\]
For \(c\equiv1,5\pmod8\), this is \(2(\alpha+4\mathbb Z_2)\) with \(\alpha=(c+1)/2\) odd; \(\alpha\equiv1\pmod4\) in the first case and \(\alpha\equiv3\pmod4\) in the second. For \(c\equiv3\pmod8\) it is \(4U\). For \(c\equiv7\pmod8\) it is the entire ball \(8\mathbb Z_2\).

If \(x=2^k u\), with \(k\ge1\) and \(u\in U\), put \(t=u^2\in B\). Then
\[
\frac{f_c(x)}{2^{2k}}=g_k(t),\qquad
\left\{\frac{f_c(2^ku)}{2^{2k}}:u\in U\right\}=
\begin{cases}
(c+4)+8\mathbb Z_2,&k=1,\\
c+8\mathbb Z_2,&k\ge2.
\end{cases}
\]
Both displayed sets contain only units. In particular, all nonzero values for even input valuation \(k\) have exact output valuation \(2k\).

**4. Quotient closures.** If \(c\equiv7\pmod8\), the odd-input values already fill \(8\mathbb Z_2\); the quotient set of nonzero elements of that ball is \(\mathbb Q_2^\times\). Thus the full dyadic closure is \(\mathbb Q_2\).

If \(c\equiv3\pmod8\), odd inputs give every element of \(4U\), and even inputs have valuations \(2k\) for \(k\ge1\). Consequently every nonzero quotient has even valuation. Conversely, odd/odd quotients fill \(U\); for every positive even valuation \(2r\) take a numerator with even input valuation \(r+1\) and vary an odd-input denominator over \(4U\). Negative even valuations follow by reciprocation. Thus the nonzero closure is exactly \(H_3\).

Suppose \(c\equiv1\) or \(5\pmod8\). Every even-input normalized unit is \(1\pmod4\), while the odd-input values have valuation one and normalized unit congruent to \(\alpha\pmod4\), where \(\alpha=1\) or \(3\) respectively. Therefore any quotient with even valuation has normalized unit \(1\pmod4\), and any quotient with odd valuation has normalized unit \(\alpha\pmod4\). These restrictions give \(H_1\) and \(H_5\), respectively.

They are sharp at every valuation and to every precision. At valuation zero, odd/odd quotients fill \(U_4\), since the normalized odd-input image is the entire coset \(\alpha+4\mathbb Z_2\). At positive odd valuation \(2r-1\), take even-input numerator valuation \(r\) and an odd-input denominator, varying the denominator; this fills the normalized unit coset \(\alpha U_4\). Negative odd valuations follow by inversion. For each positive even valuation \(2r\), choose even-input numerator and denominator valuations \((r+1,1)\) and \((r+2,2)\), respectively. The first choice fills normalized units \(5+8\mathbb Z_2\), because \(c/(c+4)\equiv5\pmod8\); the second fills \(1+8\mathbb Z_2\). Together they fill \(U_4\); negative even valuations again follow by inversion.

Finally, for every odd \(c\) the values at \(x=2^k\) approach zero as \(k\to\infty\), so zero belongs to the quotient-set closure. No other points are possible because each of the listed nonzero subgroups is open and closed within \(\mathbb Q_2^\times\). This proves all cases. \(\square\)

## Verification
The standalone reproducibility script `verify.py` checks unit-square residue coverage and the exact image-coset lemma through finite powers of two for multiple positive and negative odd coefficients. It also enumerates quotient-unit residues modulo \(16\) for normalized valuations from \(-5\) through \(5\) and compares them with the claimed case distinctions. Those computations are finite consistency checks; the all-coefficient and all-precision theorem is proved by the isometry and lifting argument above.

## Relationship to prior work
Miska, Murru and Sanna (2018), *On the \(p\)-adic denseness of the quotient set of a polynomial image*, gives a simple-root sufficiency criterion, a complete criterion for degrees at most two, and a splitting-polynomial criterion below degree \(31\). Its Question 1.14 seeks effective criteria for general polynomials. In the present family, the class \(c\equiv7\pmod8\) is already implied by its simple-root result and is included to make the classification complete; the other three cases have only the double dyadic root \(0\), since \(-c\) is not a square in \(\mathbb Q_2\). The exact closed subgroups in these non-split cases are the substantive additional statements.

Antony, Barman, Gajović and Širola, *On \(p\)-adic denseness of quotients of values of integral forms*, treats primarily multivariate homogeneous forms and provides sufficient quartic-form criteria for primes greater than three. Its inspected Theorem 5.3 does not apply to the present \(p=2\) univariate image or give these closures. The binary quadratic-form theorem of Donnay, Garcia and Rouse concerns a different input domain and does not imply this quartic classification. No priority claim beyond the inspected evidence is made.

## Limitations
This is an exact local theorem only at the prime two, only for the specified one-parameter quartic family with odd coefficient, and only for closures of quotient sets of polynomial values; it does not characterize quotient sets pointwise. The elementary proof does not establish uniqueness in the entire published literature. Full independent mathematical review has not been performed.

## References
1. P. Miska, N. Murru and C. Sanna, *On the \(p\)-adic denseness of the quotient set of a polynomial image*, arXiv:1807.08947 (first public 2018-07-24), *Journal of Number Theory* 197 (2019), 218–227; especially Theorem 1.2, Propositions 1.4–1.5 and Question 1.14.
2. D. Antony, R. Barman, S. Gajović and D. Širola, *On \(p\)-adic denseness of quotients of values of integral forms*, arXiv:2308.08907 (first public 2023-08-17), especially Theorem 5.3 in the accessible 2025 version.
3. C. Donnay, S. R. Garcia and J. Rouse, *\(p\)-adic quotient sets II: Quadratic forms*, *Journal of Number Theory* 201 (2019), 23–39, DOI:10.1016/j.jnt.2019.02.023.
