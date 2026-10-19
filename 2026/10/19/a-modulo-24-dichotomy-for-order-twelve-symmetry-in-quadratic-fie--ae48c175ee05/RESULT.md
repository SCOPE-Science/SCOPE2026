# A modulo-24 dichotomy for order-twelve symmetry in quadratic-field Fourier compression

## Finding
Let \(p\ge5\) be an odd prime, let \(K=\mathbb F_{p^2}\), let \(H=(K^\times)^2\), and let \(\chi:H\to\mathbb C^\times\) be any character of **exact order twelve**. Choose one representative from each of the two nonzero \(H\)-orbits in \(K\). Define the unnormalized compressed Fourier matrix by
\[
M_{\chi}(r,s)=\sum_{h\in H}\chi(h)\exp\left(\frac{2\pi i}{p}\operatorname{Tr}_{K/\mathbb F_p}(rsh)\right).
\]
Then the following dichotomy holds for all four order-twelve characters:

* If \(p\bmod24\in\{13,17,19,23\}\), precisely two entries of \(M_\chi\) vanish; the other two, located on distinct rows and columns, have absolute value \(p\).
* If \(p\bmod24\in\{1,5,7,11\}\), **all four entries are nonzero**.

In every case \(M_\chi\) is invertible. In the first case the compressed Fourier transform maps every single nonzero orbit component bijectively onto one other orbit component. In particular, for any such orbit-supported, nonzero \(\chi\)-symmetric function \(f\), both supports have size \((p^2-1)/2\).

The exceptional classes \(p\equiv17,19\pmod{24}\) do not follow from the two elementary explanations for Gauss-sum equality: the character is nontrivial on \(\mathbb F_p^\times\), and Frobenius does not exchange its two full-field extensions.

## Assumptions and scope
A multiplicative character has exact order twelve if its image contains a primitive twelfth root of unity. Since \(24\mid p^2-1\), the square subgroup \(H\) has order divisible by twelve and has exactly \(\varphi(12)=4\) such characters. The canonical additive character is defined by the field trace in the displayed formula. Replacing orbit representatives only rescales and permutes rows or columns by unit-modulus factors; hence the asserted zero pattern and modulus are independent of those choices.

Here the phrase **monomial matrix** means a square matrix with exactly one nonzero entry in each row and column. The nonvanishing-minors property for a two-by-two matrix requires both invertibility and absence of zero entries. The dichotomy concerns this index-two, exact-order-twelve slice only, not all characters of the square subgroup.

## Proof
Fix a generator \(g\) of \(K^\times\), and write \(\zeta=\exp(2\pi i/24)\). The two multiplicative characters of \(K^\times\) extending \(\chi\) are \(\xi\) and \(\xi\eta\), where \(\eta\) is the quadratic character; each is of order \(24\). Their values at \(g\) are \(\zeta^t\) and \(\zeta^{t+12}\) for some \(t\in(\mathbb Z/24\mathbb Z)^\times\).

Write \(G(\alpha)=\sum_{x\in K^\times}\alpha(x)\psi(x)\), where \(\psi(x)=\exp(2\pi i\operatorname{Tr}(x)/p)\). The character-extension computation for the compressed Fourier transform, or a direct even/odd projection, gives a matrix equivalent by unit-modulus row/column factors to
\[
\frac12\begin{pmatrix}
G(\xi)+G(\xi\eta)&G(\xi)-G(\xi\eta)\\
G(\xi)-G(\xi\eta)&G(\xi)+G(\xi\eta)
\end{pmatrix}.
\]
Both Gauss sums have absolute value \(p\), and their product is nonzero. Thus the compressed determinant is nonzero. It is monomial exactly when \(G(\xi)=\pm G(\xi\eta)\); otherwise each entry is nonzero. If equality holds, the two surviving entries have absolute value \(p\).

Set \(J=J(\xi,\eta)=\sum_{x\in K}\xi(x)\eta(1-x)\) with nontrivial characters extended by zero. The Jacobi–Gauss identity gives
\[
J=\frac{G(\xi)G(\eta)}{G(\xi\eta)},\qquad G(\eta)=\pm p.
\]
Consequently the relevant Gauss-sum equality is equivalent to \(J=\pm p\).

We establish the latter by a cyclotomic divisibility argument. For any unit \(t\) modulo \(24\), define
\[
E_r(t)=t+(rt\bmod24),\qquad r=p\bmod24,
\]
where the residues \(t\) and \((rt\bmod24)\) are represented by integers from \(1\) to \(23\). Apply Stickelberger's digit-sum valuation formula to a primitive order-\(24\) character: at the prime above \(p\) specified by a Teichmüller embedding, its Gauss sum has \(p\)-normalized valuation
\[
\frac{s_p((p^2-1)t/24)}{p-1}=\frac{E_r(t)}{24},
\]
up to the harmless replacement of every exponent \(t\) by its negative caused by the convention for character and Teichmüller lifts. The equality or inequality of the valuations for \(t\) and \(t+12\) is unaffected by that replacement. All primes above \(p\) in \(\mathbb Q(\zeta)\) arise by cyclotomic conjugation, so checking all eight units \(t\) tests the divisibility of every conjugate of \(J\).

For \(r\in\{13,17,19,23\}\), direct residue arithmetic gives
\[
E_r(t)=E_r((t+12)\bmod24)
\quad\text{for every }t\in(\mathbb Z/24\mathbb Z)^\times.
\]
Indeed for representatives \(t=1,5,7,11\), both sides have respective ordered values
\[
\begin{array}{c|rrrr}
r&1&5&7&11\\\hline
13&14&22&26&34\\
17&18&18&30&30\\
19&20&28&20&28\\
23&24&24&24&24
\end{array}
\]
(the other four units are obtained by adding twelve). Since \(v_p(G(\eta))=1\), the Jacobi–Gauss identity gives \(v_{\mathfrak p}(J)=1\) at every prime \(\mathfrak p\) of \(\mathbb Q(\zeta)\) above \(p\). The prime \(p\) is unramified in this cyclotomic field because \(p\nmid24\). As \(J\) is an algebraic integer, these valuations imply \(J/p\) is an algebraic integer.

Every Galois conjugate of \(J\) has complex modulus \(p\), since all three characters \(\xi\), \(\eta\), and \(\xi\eta\) are nontrivial. Kronecker's theorem therefore forces the integral element \(J/p\in\mathbb Q(\zeta)\) to be a root of unity. Moreover, the substitution \(x\mapsto1/x\) in the Jacobi sum yields
\[
J(\xi,\eta)=\eta(-1)J((\xi\eta)^{-1},\eta)=J(\xi^{11},\eta),
\]
because \(\eta(-1)=1\) in the quadratic field and \(\xi\eta=\xi^{13}\). Hence \(J\) is fixed by the automorphism \(\zeta\mapsto\zeta^{11}\). Every root of unity in \(\mathbb Q(\zeta_{24})\) is a power of \(\zeta_{24}\), and the only such powers fixed by this automorphism are \(1\) and \(-1\). It follows that \(J=\pm p\), as claimed.

For \(r\in\{1,5,7,11\}\), use \(t=1\) and \(t+12=13\). Then
\[
(E_r(1),E_r(13))\in\{(2,26),(6,30),(8,32),(12,36)\}.
\]
Their unequal Stickelberger valuations imply \(G(\xi)\ne\pm G(\xi\eta)\) for the primitive character chosen with exponent one. All order-twelve characters arise by cyclotomic conjugation, which preserves both equality and inequality of these sums, so this holds for every exact-order-twelve \(\chi\). This completes the dichotomy.

Finally, \(\xi\) restricts to \(\chi\) on \(H\) and \(\mathbb F_p^\times\) is generated by \(g^{p+1}\). For \(p\equiv17,19\pmod{24}\), the restrictions \(\xi|_{\mathbb F_p^\times}\) have orders \(4\) and \(6\), respectively, and are therefore nontrivial. Frobenius exchanges the extensions only when \(p\equiv13\pmod{24}\), since the two exponents differ by twelve. Thus the classes \(17,19\) represent an additional obstruction beyond those two elementary mechanisms.

## Verification
The standalone `checker.py` carries out independent exact computations in \(\mathbb F_p[u]/(u^2-d)\), where \(d\) is an explicit quadratic nonresidue. It constructs a primitive multiplicative generator, enumerates all terms of \(J(\xi,\eta)\), and reduces every power of a primitive 24th root of unity modulo \(X^8-X^4+1\). It verifies the \(\pm p\) dichotomy for all eight primitive exponents and for the twenty primes up to \(79\), covering all eight possible residue classes modulo \(24\). No floating-point arithmetic is used. The program also checks the residue/digit-sum condition for all eight residue classes and prints `CHECK_PASS` on success.

Run from a directory containing the extracted package with `python3 checker.py` (standard library only). The general result is proved above; finite checks provide a separate consistency test rather than a proof by extrapolation.

## Relationship to prior work
Garcia, Karaali, and Katz, Theorem 6.7, identify equality of the two Gauss sums as the exact obstruction to nonvanishing minors for index-two compressed transforms; their Remark 6.8 explicitly requests precise conditions and supplies a table for \(\mathbb F_{25}\). The present statement resolves one complete, infinite, fixed-character-order slice, including residue classes where elementary Frobenius and subfield arguments do not apply. Díaz Padilla and Ochoa Arango discuss the same compressed-transform framework and solve a different index-three problem.

The published result *A subfield-trivial character forces monomial compressed Fourier transforms in quadratic fields* applies to subgroups of index at least four, with index dividing \(p+1\) and characters trivial on \(\mathbb F_p^\times\). It is not a stronger theorem covering this index-two situation. The published cubic Gauss-sum-equality census concerns \(\mathbb F_{p^3}\), not the order-twelve symmetry in \(\mathbb F_{p^2}\). Stickelberger's valuation theorem, Jacobi–Gauss identities, cyclotomic integrality, and Kronecker's theorem are classical ingredients rather than novelty claims.

## Limitations
This does not classify characters of orders other than twelve or extension degrees other than two. The nonzero entries' complex phases are not determined, only their magnitudes and support geometry. An equivalent number-theoretic statement could occur under terminology concerning pure Jacobi sums or pure Gauss sums; bibliographic coverage in that specialized literature is not guaranteed.

## References
1. S. R. Garcia, G. Karaali, and D. J. Katz, *An improved uncertainty principle for functions with symmetry*, arXiv:1807.07648 (first public version, 19 July 2018), Theorem 6.7 and Remark 6.8, https://arxiv.org/abs/1807.07648.
2. D. F. Díaz Padilla and J. A. Ochoa Arango, *On an uncertainty principle for small index subgroups of finite fields*, arXiv:2310.09992 (first public version, 16 October 2023), https://arxiv.org/abs/2310.09992.
3. *A subfield-trivial character forces monomial compressed Fourier transforms in quadratic fields*, published-finding corpus published result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-subfield-trivial-character-forces-monomial-compressed-fourier--707f906e4c49.
4. Standard forms of the Stickelberger Gauss-sum valuation theorem, the Jacobi–Gauss identity, and Kronecker's theorem on algebraic integers of unit-modulus conjugates.
