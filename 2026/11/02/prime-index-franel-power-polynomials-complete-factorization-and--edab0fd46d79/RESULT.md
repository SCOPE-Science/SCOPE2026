# Prime-index Franel power polynomials: complete factorization and tame discriminant

## Finding
For every odd prime \(p\) and integer \(r\ge3\), let
\[
F_{p,r}(X)=\sum_{k=0}^{p}\binom pk^{r}X^k,\qquad Q_{p,r}(X)=F_{p,r}(X)/(X+1).
\]
Then \(Q_{p,r}\) is an integral monic reciprocal polynomial of degree \(p-1\), irreducible over both \(\mathbb Q\) and \(\mathbb Q_p\). Thus \((X+1)Q_{p,r}(X)\) is the **complete rational irreducible factorization**.

Every zero of \(F_{p,r}\) is simple, negative and real. Of the \(p-1\) zeros of \(Q_{p,r}\), precisely \((p-1)/2\) lie in \((-1,0)\) and precisely \((p-1)/2\) lie in \(( -\infty,-1)\); the two sets are exchanged by \(\alpha\mapsto\alpha^{-1}\).

For any root \(\alpha\) of \(Q_{p,r}\) in an algebraic closure of \(\mathbb Q_p\), normalized by \(\nu_p(p)=1\),
\[
\nu_p(\alpha+1)=\frac1{p-1},\qquad
[\mathbb Q_p(\alpha):\mathbb Q_p]=e(\mathbb Q_p(\alpha)/\mathbb Q_p)=p-1.
\]
Finally, writing \(\Delta_{p,r}=\operatorname{Disc}(Q_{p,r})\in\mathbb Z_{>0}\),
\[
\nu_p(\Delta_{p,r})=p-2,\qquad
\frac{\Delta_{p,r}}{p^{p-2}}\equiv(-1)^{(p-1)/2}\pmod p.
\]
These are exact local assertions; no formula for the full integer discriminant away from \(p\) is asserted.

## Assumptions and scope
The parameters are precisely any odd prime \(p\) and integer \(r\ge3\). The ordinary Franel polynomial corresponds to \(r=3\), with \(F_{p,3}(1)\) the familiar prime-index Franel number. Valuations of algebraic numbers use the extension of the usual \(p\)-adic valuation normalized by \(\nu_p(p)=1\). A polynomial is reciprocal if its coefficients are palindromic.

## Proof
**Integral factor and Eisenstein translation.** Set \(a_k=\binom pk^r\). Symmetry \(a_k=a_{p-k}\) makes \(F_{p,r}(X)=X^pF_{p,r}(1/X)\), with \(p\) odd; therefore \(F_{p,r}(-1)=0\). Division by the monic integer factor \(X+1\) yields \(Q_{p,r}\in\mathbb Z[X]\), monic, constant term one, and reciprocal of degree \(m=p-1\).

For \(1\le k\le p-1\), the binomial coefficient \(\binom pk\) is divisible by \(p\). Since \(r\ge3\),
\[
F_{p,r}(X)\equiv 1+X^p\pmod{p^2}.
\]
Write \(H(Y)=Q_{p,r}(Y-1)=F_{p,r}(Y-1)/Y\). The freshman's-dream identity gives
\[
H(Y)\equiv Y^{p-1}\pmod p.
\]
Moreover, differentiating \(F_{p,r}(X)=(X+1)Q_{p,r}(X)\) at \(X=-1\) gives \(H(0)=F_{p,r}'(-1)\). The two endpoint coefficients contribute \(p\) modulo \(p^2\) to this derivative; all interior contributions are divisible by \(p^2\), so
\[
H(0)\equiv p\pmod{p^2}.
\]
Hence \(H\) is Eisenstein at \(p\), irreducible over \(\mathbb Q_p\), and so is \(Q_{p,r}\); irreducibility over \(\mathbb Q\) follows. The Eisenstein Newton polygon has the sole segment from \((0,1)\) to \((m,0)\). Every root \(\beta\) of \(H\) therefore has \(\nu_p(\beta)=1/m\), giving the asserted shifted-root valuation and total ramification. In particular, \(H(0)\ne0\), so \(-1\) is a simple root of \(F_{p,r}\).

**Real zeros.** For each fixed \(p\), define the finite sequence \(\gamma_k=\binom pk\) for \(0\le k\le p\) and \(\gamma_k=0\) thereafter. Its exponential generating polynomial is
\[
\sum_{k\ge0}\gamma_k\frac{z^k}{k!}
=\sum_{k=0}^p\binom pk\frac{z^k}{k!}=L_p(-z),
\]
where \(L_p\) is the classical Laguerre polynomial. All zeros of \(L_p\) are positive and simple, hence \(L_p(-z)\) has only negative real zeros. By the Pólya–Schur multiplier-sequence criterion, multiplying every coefficient of a real-rooted polynomial by \(\gamma_k\) preserves real-rootedness. Starting with \(F_{p,1}(X)=(1+X)^p\) and applying this operator \(r-1\) times yields \(F_{p,r}\), all of whose zeros are real. All its coefficients are positive with nonzero constant term, so no zero is nonnegative. Since \(Q_{p,r}\) is irreducible in characteristic zero it is separable; \(-1\) is simple by \(H(0)\ne0\). Finally, the reciprocal even-degree polynomial \(Q_{p,r}\) has zeros paired as \((\alpha,1/\alpha)\), neither member equal to \(-1\) or \(0\); each negative pair straddles \(-1\). Thus the two counts are exactly \(m/2\).

**Exact tame discriminant and unit.** Write
\[
H(Y)=Y^m+\sum_{j=0}^{m-1}b_jY^j,
\qquad p\mid b_j,
\quad \nu_p(b_0)=1.
\]
At any root \(\beta\), the leading derivative term \(m\beta^{m-1}\) has valuation \((m-1)/m<1\), since \(p\nmid m\). Every other derivative term \(jb_j\beta^{j-1}\) has valuation at least one. Consequently
\[
\nu_p(H'(\beta))=\frac{m-1}{m}.
\]
As \(H\) is monic and separable,
\[
\operatorname{Disc}(H)=(-1)^{m(m-1)/2}\prod_{H(\beta)=0}H'(\beta).
\]
It follows immediately that \(\nu_p(\operatorname{Disc}(H))=m-1\). More precisely, each quotient \(H'(\beta)/(m\beta^{m-1})\) is congruent to \(1\) modulo the maximal ideal of the totally ramified splitting field. Their product, being a \(p\)-adic rational integer, is congruent to \(1\pmod p\). Since \(\prod\beta=b_0\) (\(m\) is even), we obtain
\[
\frac{\operatorname{Disc}(H)}{p^{m-1}}
\equiv(-1)^{m(m-1)/2}m^m
\left(\frac{b_0}{p}\right)^{m-1}
\equiv(-1)^{m/2}\pmod p.
\]
Here \(m=p-1\equiv-1\pmod p\), \(m\) is even, and \(b_0/p\equiv1\pmod p\). Translation leaves discriminants unchanged, proving the two displayed discriminant claims. Positivity of the discriminant follows alternatively from the \(m\) distinct real roots of \(Q_{p,r}\), since it is the product of squared root differences.

## Verification
Run \(\texttt{python3 verify.py}\) using only the Python standard library. The script independently builds the coefficient arrays, performs exact integer synthetic division and translation, checks the Eisenstein coefficient conditions, computes discriminants with an integer Sylvester determinant via the Bareiss algorithm, and counts the real roots using exact rational Sturm sequences for selected cases. It checks \(p\in\{3,5,7,11\}\), \(r\in\{3,4,5\}\). The script's finite computations test the formulas only at those parameters; the symbolic arguments above prove the infinite family.

## Relationship to prior work
Franel's numbers and their binomial-power generalizations are classical. Guo (2014) studies the Franel polynomial \(\sum_k\binom nk^3X^k\) and establishes congruences involving Franel numbers; its accessible full text does not present the prime-index quotient factorization, ramification, or discriminant. Straub and Zudilin (2022) investigate recurrences and Apéry limits of unweighted binomial-power sums, not these roots or local discriminants. Z.-H. Sun (2015) proves congruences for Franel sums, not the prime-index factor classification. The classical Pólya–Schur multiplier-sequence theorem supplies the real-rootedness mechanism and is used here as prior mathematics, not asserted to be new.

The \(r=2\) polynomial is related by an affine transformation to a Legendre polynomial, and a 2026 work addresses the irreducibility of Legendre polynomials; **this classification deliberately restricts to \(r\ge3\)** and makes no novelty claim for \(r=2\). Published research on prime-index Apéry polynomials likewise concerns a different binomial coefficient family and does not imply the assertion here. Searches over direct formula aliases, generalized Franel sums, Legendre equivalences, and index records did not identify equivalent coverage, but this is not proof of uniqueness.

## Limitations
No claim is made for composite indices, \(p=2\), the complete discriminant outside the distinguished prime, or the full Galois group over \(\mathbb Q\). A logically possible equivalent classification in unlocated literature remains an originality risk. Independent external validation has not been performed. Finite computations do not establish universal quantifiers without the proof above.

## References
1. V. J. W. Guo, *Proof of a supercongruence conjectured by Z.-H. Sun*, arXiv:1404.6978v1, 28 April 2014. https://arxiv.org/html/1404.6978v1
2. A. Straub and W. Zudilin, *Sums of powers of binomials, their Apéry limits, and Franel's suspicions*, arXiv:2112.09576v2, 2022. https://arxiv.org/html/2112.09576v2
3. Z.-H. Sun, *Congruences involving Franel numbers*, arXiv:1502.02499, 2015. https://arxiv.org/abs/1502.02499
4. Z. Deng, *A proof of the irreducibility conjecture for Legendre polynomials*, arXiv:2609.22336, 2026. https://arxiv.org/abs/2609.22336
5. Pólya–Schur multiplier-sequence criterion; see the statement in *Real-rooted and stable polynomials*, https://www.symmetricfunctions.com/realRooted.htm
