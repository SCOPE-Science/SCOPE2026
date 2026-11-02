# A mod-36 rigidity law forbidding Smith triples in Fibonacci–Lucas doubling

## Finding
Let \(F_0=0\), \(F_1=1\), \(L_0=2\), \(L_1=1\), and let both sequences obey \(X_{n+2}=X_{n+1}+X_n\). For each integer \(n\geq1\), define the digit-root obstruction
\[
T_n=F_{2n}-F_n-L_n=F_nL_n-F_n-L_n.
\]
It has the exact local valuation laws
\[
\nu_2(T_n)=\begin{cases}1,&3\mid n,\\0,&3\nmid n,\end{cases}
\qquad
\nu_3(T_n)=\begin{cases}1,&n\equiv5\pmod8,\\0,&n\not\equiv5\pmod8.\end{cases}
\]
The valuations are those of the nonzero integer \(|T_n|\). In particular, neither \(4\) nor \(9\) divides \(T_n\) at any index.

Let \(s_b(m)\) be the sum of base-\(b\) digits of \(m\geq1\), and put \(P_b(m)=\sum_{p^e\parallel m}e\,s_b(p)\). A base-\(b\) Smith number is a composite integer \(m\) satisfying \(s_b(m)=P_b(m)\). For every integer base \(b\geq2\) with \(4\mid(b-1)\) or \(9\mid(b-1)\), the three numbers \(F_n\), \(L_n\), and \(F_{2n}\) cannot all be Smith numbers in base \(b\). This holds in particular for decimal Smith numbers at every positive index.

## Assumptions and scope
All recurrences and indices are over the ordinary nonnegative integers, with \(n\geq1\). The Smith definition excludes primes, as usual; conditional statements concerning Smith terms only apply when the terms are composite. The local valuations are unrestricted in \(n\) and do not require factorization of any Fibonacci or Lucas term. The base extension is restricted to bases with \(4\mid(b-1)\) or \(9\mid(b-1)\); no analogous assertion is made for other bases.

## Proof
Write
\[
Q=\begin{pmatrix}1&1\\1&0\end{pmatrix}.
\]
Its powers satisfy \((Q^n)_{12}=F_n\) and \(\operatorname{tr}(Q^n)=L_n\), including \(n=0\). Direct exact recurrence calculation gives
\[
Q^6=\begin{pmatrix}13&8\\8&5\end{pmatrix}\equiv I\pmod4,
\qquad
Q^{24}=\begin{pmatrix}75025&46368\\46368&28657\end{pmatrix}\equiv I\pmod9.
\]
Therefore the pair \((F_n,L_n)\), and hence \(T_n\), is periodic modulo \(4\) with period dividing \(6\), and modulo \(9\) with period dividing \(24\). It suffices to calculate the finitely many residues in these **proved complete periods**.

For indices \(n\equiv0,1,2,3,4,5\pmod6\), the six residues \(T_n\pmod4\) are
\[
(2,3,3,2,3,3).
\]
Thus \(T_n\equiv2\pmod4\) precisely when \(3\mid n\), and \(T_n\equiv3\pmod4\) otherwise. These establish the exact \(2\)-adic valuations.

For indices \(n\equiv0,1,\ldots,23\pmod{24}\), the complete residue vector \(T_n\pmod9\) is
\[
(7,8,8,2,2,3,1,2,1,8,8,8,2,3,7,5,4,8,8,5,2,3,4,8).
\]
Every entry is nonzero. The only entries divisible by \(3\) occur at residues \(5\), \(13\), and \(21\), where the value is exactly \(3\pmod9\). These three classes are precisely \(n\equiv5\pmod8\), so the exact \(3\)-adic valuation formula follows. In particular \(T_n\neq0\) for all \(n\geq1\).

For every base \(b\ge2\), the positional digit identity gives \(s_b(m)\equiv m\pmod{b-1}\). Also the prime-factor digit-sum function is completely additive: \(P_b(xy)=P_b(x)+P_b(y)\) for positive integers. If \(F_n\), \(L_n\), and \(F_{2n}=F_nL_n\) were all base-\(b\) Smith, we would have
\[
s_b(F_{2n})=P_b(F_{2n})=s_b(F_n)+s_b(L_n).
\]
Reducing modulo \(b-1\) would imply \(T_n\equiv0\pmod{b-1}\). When \(4\mid(b-1)\) or \(9\mid(b-1)\), this contradicts one of the proven valuation bounds. The Smith-triple assertion follows without any assumption about the prime factors.

For the published common Smith index \(n=827\), the complete factorization tables list \(F_{827}\) and \(L_{827}\) as Smith numbers; their digit sums and prime-factor digit sums are \(809\) and \(802\). Independently constructing these two recurrence terms gives \(s_{10}(F_{1654})=1592\), and hence
\[
s_{10}(F_{1654})-P_{10}(F_{1654})=1592-(809+802)=-19.
\]
Thus \(F_{1654}\) fails the Smith property, even though the two factors at index \(827\) have it. Primality of the large factors in the published tables is imported from those sources; the unrestricted modular theorem does not depend on their primality certificates.

## Verification
The standalone Python standard-library program `artifacts/verify.py` checks both displayed matrix-period certificates by modular matrix multiplication, independently computes the six and twenty-four complete obstruction residues, and compares their consequences against direct recurrences through index \(10000\). It separately multiplies the published index-\(827\) factors, independently generates the recurrence terms, checks factor products, and recomputes the three decimal digit sums and the exact Smith deficit. Its output is recorded in `VERIFICATION.md`. The all-index theorem follows from the matrix periods and full residue tables, not from the longer empirical comparison.

## Relationship to prior work
Dario, Gonçalves, and Oliveira (2026, arXiv:2609.01955v1) introduce their Fibonacci/Lucas Smith searches, use \(F_{2n}=F_nL_n\) and additivity of prime-factor digit sums to compute even-index Smith tests, and identify \(827\) as a common Fibonacci–Lucas Smith index. Their Sections 5–6 do not state the exact \(2\)-adic and \(3\)-adic laws for \(F_{2n}-F_n-L_n\), nor the unrestricted impossibility of the three simultaneous Smith properties. The two relevant OEIS lists record common indices, rather than this conditional exclusion; Kelly's factorization tables support the numerical illustration. The underlying Fibonacci modular periodicity and digit-root congruence are classical; the contribution is their complete sharp combination for the natural Smith-doubling obstruction, not the classical ingredients themselves.

## Limitations
The Smith-triple impossibility does not answer whether further indices besides \(827\) make both \(F_n\) and \(L_n\) Smith. No claim is made that the local congruence itself is difficult or requires large-number factorization. The base extension is not asserted for bases outside the two stated congruence families. The factor-table illustration uses previously published prime-factor identification, not independently produced primality certificates. A differently formulated older result could already imply the obstruction; priority therefore remains subject to independent literature assessment.

## References
1. R. P. Dario, J. L. Gonçalves, M. P. N. Oliveira, *When Fibonacci and Lucas Meet Smith: A Computational Exploration*, arXiv:2609.01955v1 (first public version September 2, 2026), https://arxiv.org/abs/2609.01955.
2. S. S. Gupta, *Numbers k such that Fibonacci(k) is a Smith number*, OEIS A382922, https://oeis.org/A382922.
3. R. P. Dario, *Numbers k such that Lucas(k) is a Smith number*, OEIS A395686, https://oeis.org/A395686.
4. B. Kelly, *Fibonacci factorizations, indices 0–1000*, https://mersennus.net/fibonacci/f1000.txt, especially index 827.
5. B. Kelly, *Lucas factorizations, indices 0–1000*, https://mersennus.net/fibonacci/l1000.txt, especially index 827.
