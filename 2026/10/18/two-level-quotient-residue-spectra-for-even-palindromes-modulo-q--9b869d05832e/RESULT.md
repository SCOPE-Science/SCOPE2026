# Two-level quotient-residue spectra for even palindromes modulo \(q^2\)

## Finding
Let \(q\ge3\) be an odd prime, \(b=q-1\), and \(m\ge1\). Write \(\mathcal P_{q,m}\) for the set of canonical base-\(b\) palindromes having exactly \(2m\) digits (leading digit nonzero). Each is divisible by \(q=b+1\). For a residue \(r\in\mathbb Z/q\mathbb Z\), define
\[
N_{q,m}(r)=\#\{P\in\mathcal P_{q,m}:P/q\equiv r\pmod q\}.
\]
Set
\[
T=(q-2)(q-1)^{m-1},\qquad z=\#\{j:1\le j<m,\ q\mid(2m-1-2j)\}.
\]
Thus \(T=\#\mathcal P_{q,m}\). With \(\mathbf1_E\) denoting the indicator of a congruence condition, the complete spectrum is
\[
\boxed{N_{q,m}(r)=\frac Tq+\begin{cases}
(-1)^{m-z}(q-1)^z\left(\mathbf1_{r\equiv m-1\ (\bmod\ q)}+\mathbf1_{r\equiv-m\ (\bmod\ q)}-\frac2q\right),&q\nmid(2m-1),\\[4pt]
(q-2)(-1)^{m-1-z}(q-1)^z\left(\mathbf1_{r\equiv m-1\ (\bmod\ q)}-\frac1q\right),&q\mid(2m-1).
\end{cases}}
\]
Every expression is an integer. In the first case the two distinguished residue classes are distinct. Hence there are exactly two values among the \(q\) class counts for every \(m\), and the counts are never exactly uniform. Since \(z\le\lceil(m-1)/q\rceil\), their relative discrepancy from \(1/q\) tends exponentially to zero as \(m\to\infty\) at each fixed \(q\).

For instance, with \(q=11\), \(b=10\), and \(m=2\), exactly \(90\) four-digit decimal palindromes exist. Nine have quotient by \(11\) congruent to \(1\) and another nine have quotient congruent to \(9\); eight have each of the other nine quotient residues. Thus exactly eight four-digit decimal palindromes are divisible by \(121\). This is an example, not a separate claim.

## Assumptions and scope
The prime \(q\) is odd, \(m\) is any positive integer, all residues are taken modulo \(q\), and exactly \(2m\) base-\(q-1\) digits are required. Non-leading digits may be zero. The prime hypothesis permits nonzero coefficients to be invertible modulo \(q\); the statement is not asserted for arbitrary composite \(b+1\) or for odd-length palindromes. The quotient \(P/q\) is an integer because every even-length palindrome in this base has the forced divisor \(q\).

## Proof
Write each palindrome uniquely as
\[
P=\sum_{j=0}^{m-1}a_j\bigl(b^j+b^{2m-1-j}\bigr),
\qquad1\le a_0\le q-2,\quad0\le a_j\le q-2\ (1\le j<m).
\]
As \(b=q-1\), the binomial theorem gives \(b^k\equiv(-1)^k(1-kq)\pmod{q^2}\) for all \(k\ge0\). Because \(2m-1\) is odd, the two powers in each parenthesis have opposite parity; therefore their sum is divisible by \(q\), and
\[
\frac{P}{q}\equiv\sum_{j=0}^{m-1}a_jw_j\pmod q,
\qquad w_j=(-1)^j(2m-1-2j).
\]
The endpoint and total weights obey
\[
w_0=2m-1,\qquad A=\sum_{j=1}^{m-1}w_j=1-m,\qquad A+w_0=m.
\]
These identities follow by pairing consecutive terms in the alternating sum; they hold also at \(m=1\), for which \(A=0\).

Let \(\zeta=\exp(2\pi i/q)\) and fix a nonzero character parameter \(t\pmod q\). Because \(q\) is prime, any nonzero \(w_j\pmod q\) satisfies
\[
\sum_{a=0}^{q-2}\zeta^{taw_j}=-\zeta^{-tw_j},
\]
while the same sum equals \(q-1\) when \(q\mid w_j\). This is the complete \(q\)-term character sum minus its omitted last digit \(a=q-1\equiv-1\pmod q\). There are exactly \(z\) zero weights among \(j=1,\ldots,m-1\). Their product, with all other internal digit sums, is consequently
\[
(-1)^{m-1-z}(q-1)^z\zeta^{-tA}.
\]
For the leading digit \(a_0\in\{1,\ldots,q-2\}\), its character sum is \(-1-\zeta^{-tw_0}\) if \(q\nmid w_0\), and is \(q-2\) otherwise. Thus the nontrivial Fourier coefficient of the quotient residue count equals
\[
(-1)^{m-z}(q-1)^z\bigl(\zeta^{-tA}+\zeta^{-t(A+w_0)}\bigr)
\]
when \(q\nmid(2m-1)\), and equals
\[
(q-2)(-1)^{m-1-z}(q-1)^z\zeta^{-tA}
\]
when \(q\mid(2m-1)\). For the trivial character \(t=0\), the coefficient is simply \(T\). Fourier inversion uses
\[
\sum_{t=1}^{q-1}\zeta^{-tu}=q\mathbf1_{u\equiv0\ (\bmod\ q)}-1.
\]
Substituting \(A=1-m\), \(A+w_0=m\) yields exactly the two displayed formulas, including the signs and all boundary cases.

If \(q\nmid(2m-1)\), the distinguished classes \(m-1\) and \(-m\) differ modulo \(q\); two classes have one count and the remaining \(q-2\) have a second count differing by \((q-1)^z\) in absolute value. If \(q\mid(2m-1)\), a single class \(m-1\) differs from the other \(q-1\) by \((q-2)(q-1)^z\). All differences are positive, so exact uniformity never occurs. Finally, as \(2\) is invertible modulo the odd prime \(q\), the equation \(2m-1-2j\equiv0\pmod q\) selects a single congruence class of \(j\pmod q\), giving \(z\le\lceil(m-1)/q\rceil\). Dividing either formula by \(T\) proves the asserted exponential decay.

## Verification
The standalone `checker.py` implements the displayed closed formula using only integers, independently counts the remainders of actual palindrome coefficients modulo \(q^2\) by dynamic programming, and also directly enumerates actual palindromic integers for small cases. It passed every residue for \(q\in\{3,5,7,11,13,17\}\), \(1\le m\le25\), and direct enumeration at \(q\in\{3,5,7\}\), \(1\le m\le4\). To reproduce, run `python3 checker.py`. This is finite corroboration; the infinite conclusion is established by the character-sum proof above.

## Relationship to prior work
Banks, Hart, and Sakata (2004), *Almost All Palindromes Are Composite*, study congruence distributions of palindromic integers, derive the elementary factorization of the relevant character sums (Lemma 3.1), and establish asymptotic uniformity under coprimality restrictions (Corollary 4.5). Their restriction \(\gcd(Q,b(b^2-1))=1\) excludes the modulus \(Q=q^2\) used here because \(q=b+1\), and their conclusions do not give the exact two-level quotient spectrum at each length. The elementary forced divisor \(q\mid P\) by itself reveals none of the higher-modulus counts. A related exact classification modulo divisors of \(b+1\) records only the first residue layer and does not imply these \(q^2\) counts. The present statement is a prime-square refinement of the exceptional forced-divisor case, not a claim of uniformity for unrelated moduli.

## Limitations
Only odd prime \(q=b+1\), even lengths, and residue classes modulo \(q^2\) are treated. Higher prime powers and arbitrary bases are not classified. The historical paper *Modular Palindromes* (Hansen, 1971) and *Palindromes: Density and Divisibility* (Schmidt, 1988) were located bibliographically but their full texts could not be inspected, leaving a risk of an implicit earlier equivalent. The proof is self-contained once elementary roots-of-unity orthogonality is accepted; the finite code does not certify all parameters.

## References
1. W. D. Banks, D. N. Hart, M. Sakata, *Almost All Palindromes Are Composite*, first preprint 2004-05-04, arXiv:math/0405056v1, especially Lemma 3.1 and Corollaries 4.4–4.5. https://arxiv.org/pdf/math/0405056
2. R. T. Hansen, *Modular Palindromes*, Mathematics Magazine 44 (1971), 208–212. DOI:10.1080/0025570X.1971.11976148. Bibliographic record only.
3. H. Schmidt, Jr., *Palindromes: Density and Divisibility*, Mathematics Magazine 61 (1988), 297–300. https://www.jstor.org/stable/2689549. Bibliographic record and secondary description only.
4. OEIS A045571, odd-digit palindromes divisible by \(11\); its cited result concerns a different length and modulus. https://oeis.org/A045571
