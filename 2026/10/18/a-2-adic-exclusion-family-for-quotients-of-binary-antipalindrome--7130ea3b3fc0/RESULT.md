# A 2-adic exclusion family for quotients of binary antipalindromes

## Finding
Let \(\mathcal A\) denote the positive integers whose canonical binary expansions have even length and are equal to the bitwise-complement of their reversals. Set
\[
\mathcal U=\mathbb Z_{>0}\setminus\bigl(\mathbb Z_{>0}\cap\mathcal A/\mathcal A\bigr).
\]
For each integer \(j\ge0\), place an odd integer \(N\) in \(\mathcal E\) precisely when
\[
2\cdot4^j\le N<4^{j+1},\qquad
h=\nu_2(N-1)\ge1,\qquad
(2^h+1)N<4^{j+1}2^h.
\]
Here \(\nu_2\) is the exact exponent of \(2\) dividing a positive integer. Then \(\mathcal E\subseteq\mathcal U\), and the **exact lower asymptotic density of the explicit set** \(\mathcal E\) is
\[
\underline d(\mathcal E)
=\frac16-\frac13\sum_{h=1}^{\infty}\frac1{2^h(2^h+1)}
=0.08816659344948140306\ldots.
\]
Consequently \(\underline d(\mathcal U)\ge\underline d(\mathcal E)>0.08816\), strengthening the published \(1/60\) lower bound for the unrepresentable integers. This does **not** claim equality for \(\underline d(\mathcal U)\).

## Assumptions and scope
All integer quotients are positive, and neither binary integer is written with leading zeros. An antipalindromic word of length \(2m\) has first bit \(1\) and last bit \(0\). The bound addresses only the binary antipalindromic quotient set, not ordinary binary palindromes or quotients in arbitrary bases. The auxiliary exclusion set \(\mathcal E\) includes selected odd integers of even binary length, not every unrepresentable integer.

## Proof
**1. A forced length difference.** Suppose \(N=A/B\) is a positive integer and \(A,B\in\mathcal A\), with respective binary lengths \(2s,2t\). Necessarily
\[
2^{2s-1}\le A<2^{2s},\quad 2^{2t-1}\le B<2^{2t},\quad
\tfrac12 4^{s-t}<N<2\cdot4^{s-t}.
\]
If \(2\cdot4^j\le N<4^{j+1}\), these strict bounds force \(s-t=j+1\). Indeed \(s-t\le j\) contradicts the lower bound on \(N\), whereas \(s-t\ge j+2\) would force \(N>8\cdot4^j\).

**2. Digit-prefix transport.** Fix odd \(N\) in the stated range and set \(h=\nu_2(N-1)\), \(r=h+1\), and \(L=2t\), the binary length of \(B\). Since \(B\) is even, \(2^r\mid B(N-1)=A-B\). Thus \(A,B\) have the same \(r\) trailing digits whenever both have length at least \(r\). Antipalindromicity transports equality of trailing digits to equality of leading digits, because complement-reversal is an involution.

If \(L<r\), reduction modulo \(2^L\) gives \(A\equiv B\pmod{2^L}\); the trailing \(L\) bits of \(A\) are the entire word representing \(B\). Its leading \(L\) bits are therefore also the word representing \(B\). Hence
\[
A\ge B\,2^{2s-L}=B4^{s-t},
\]
which gives \(N\ge4^{j+1}\), impossible.

If \(L\ge r\), the leading \(r\) digits of \(A,B\) coincide. Let \(v\) be the integer they represent, so \(2^{r-1}\le v\le2^r-1\). Taking strict upper and weak lower endpoint estimates from those prefixes,
\[
N=\frac AB > \frac{v\,2^{2s-r}}{(v+1)2^{2t-r}}
=\frac{v}{v+1}4^{s-t}
\ge\frac{2^{h}}{2^{h}+1}4^{j+1}.
\]
This contradicts the defining strict inequality for \(\mathcal E\). Both cases are impossible, proving \(\mathcal E\subseteq\mathcal U\).

**3. Exact shell asymptotics.** Define
\[
u_h=\frac{4\cdot2^h}{2^h+1},\qquad
C=\sum_{h=1}^{\infty}\frac{u_h-2}{2^{h+1}}.
\]
For fixed \(j\), the integers \(N\in[2\cdot4^j,u_h4^j)\) with \(\nu_2(N-1)=h\) form one residue class modulo \(2^{h+1}\). Uniformly in every partial shell \([2\cdot4^j,y4^j)\), \(2\le y\le4\), their total count is
\[
4^jH(y)+O(j+1),\qquad
H(y)=\sum_{h=1}^{\infty}\frac{\min\{y,u_h\}-2}{2^{h+1}}.
\]
To justify the stated error, there are at most \(2j+2\) nonempty valuations \(h\) in a shell, each contributes at most one rounding error, and replacing the finite sum by the infinite one costs \(O(1)\) because its tail decays geometrically. The function \(H\) is increasing and concave on \([2,4]\), with \(H(2)=0\) and \(H(4)=C\). Consequently
\[
H(y)\ge\frac{C(y-2)}2.
\]
All completed shells before \([2\cdot4^j,4^{j+1})\) contribute \(\frac C3 4^j+o(4^j)\) elements of \(\mathcal E\). At \(x=y4^j\) within that shell,
\[
\frac{|\mathcal E\cap[1,x]|}{x}
=\frac{C/3+H(y)+o(1)}{y}
\ge\frac C6+o(1).
\]
Between consecutive shells, that ratio decreases and reaches \(C/6+o(1)\) at \(x=2\cdot4^{j+1}\). Thus the liminf is exactly \(C/6\), rather than merely bounded below by it.

Finally, since
\[
\frac{u_h-2}{2^{h+1}}=
\frac1{2^h}-\frac2{2^h(2^h+1)},
\]
we have \(C=1-2\sum_{h\ge1}1/(2^h(2^h+1))\), and the displayed density equals \(C/6\).

## Verification
A standalone exact-integer verifier (`verify.py`) constructs binary antipalindromes independently, tests the exclusion criterion by divisibility and integer arithmetic, and checks that no tested excluded \(N<5000\) is the quotient of tested antipalindromic numerator/denominator pairs with denominator length at most \(16\) bits. It also records complete shell counts through \(j=8\): \(1,7,32,134,539,2165,8665,34666\), and evaluates the convergent constant to 50 decimal places. These are finite consistency checks; the infinite assertion is proved in the preceding steps.

## Relationship to prior work
Bai, Meleshko, Riasat and Shallit (2022), Theorem 18 and Corollary 19, exhibit a three-prefix-bit obstruction and derive \(\underline d(\mathcal U)\ge1/60\). Their digit-comparison method motivates the present refinement. The new result keeps the full \(2\)-adic valuation \(\nu_2(N-1)\), treats short and long denominators uniformly, derives an infinite family of sharp prefix obstructions, and computes the exact lower density of their union. This is a strictly stronger quantitative density bound, not a restatement of the published finite three-bit certificate. The OEIS tables A351172 and A351173 enumerate only initial representable/unrepresentable values and do not determine this density.

## Limitations
This is only a lower bound on the lower asymptotic density of all unrepresentable integers. It neither determines that true density nor settles the conjecture that representable integers have zero density. The finite verifier cannot replace the proof. Equivalent results in literature outside the sources examined may exist; independent review has not been performed.

## References
1. J. H. Bai, J. Meleshko, S. Riasat, J. Shallit, *Quotients of Palindromic and Antipalindromic Numbers*, arXiv:2202.13694 (first public version February 28, 2022); *INTEGERS* 22 (2022), #A96. In particular §3.4, Theorem 18 and Corollary 19. https://arxiv.org/html/2202.13694v1
2. OEIS A351172, integers representable as quotients of binary antipalindromes. https://oeis.org/A351172
3. OEIS A351173, integers not representable as quotients of binary antipalindromes. https://oeis.org/A351173
