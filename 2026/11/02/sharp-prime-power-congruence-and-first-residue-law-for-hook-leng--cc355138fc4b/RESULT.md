# Sharp prime-power congruence and first residue law for hook-length and core-partition series

## Finding

For a prime \(p\) and an integer \(a\geq1\), put \(t=p^a\) and use the formal Euler product
\[
E(q)=\prod_{m\geq1}(1-q^m)\in\mathbb Z[[q]].
\]
Consider the Nekrasov–Okounkov and \(t\)-core generating series
\[
F_{t^2}(q)=E(q)^{t^2-1},\qquad
C_t(q)=\frac{E(q^t)^t}{E(q)}.
\]
The congruence between these two integer-coefficient series has the **exact universal exponent** \(a+1\):
\[
F_{p^{2a}}(q)\equiv C_{p^a}(q)\pmod{p^{a+1}},\qquad
F_{p^{2a}}(q)\not\equiv C_{p^a}(q)\pmod{p^{a+2}}.
\]
The first coefficient that differs modulo \(p^{a+2}\) occurs at the *exact index* \(n=p^{a-1}\), where
\[
[q^{p^{a-1}}]\big(F_{p^{2a}}(q)-C_{p^a}(q)\big)
\equiv-p^{a+1}\pmod{p^{a+2}}.
\]
In addition, the complete leading discrepancy
\[
D_{p,a}(q)=\frac{F_{p^{2a}}(q)-C_{p^a}(q)}{p^{a+1}}\in\mathbb Z[[q]]
\]
is explicitly determined modulo \(p\). If \(p\) is odd, define
\[
s_p(m)=\sum_{\substack{d\mid m\\p\nmid d}}\overline d^{-1}\in\mathbb F_p,
\]
where \(\overline d^{-1}\) is the inverse of \(d\) modulo \(p\). Then
\[
\boxed{D_{p,a}(q)\equiv
-C_{p^a}(q)\sum_{m\geq1}s_p(m)q^{p^{a-1}m}\pmod p.}
\]
For \(p=2\), the first residue law instead has a theta-series correction:
\[
\boxed{D_{2,a}(q)\equiv C_{2^a}(q)
\sum_{r\geq1}\left(q^{2^{a-1}r^2}+q^{2^ar^2}\right)\pmod2.}
\]
All claims are identities in formal power series; no analytic convergence assumption is required.

## Assumptions and scope

The prime \(p\) is arbitrary, including \(2\); \(a\) ranges over all positive integers; \(q\) is a formal indeterminate. The notation \(U\equiv V\pmod{p^k}\) for two series in \(\mathbb Z[[q]]\) means coefficientwise divisibility by \(p^k\), for *every* nonnegative exponent. The notation \([q^n]U\) extracts the coefficient of \(q^n\). Every displayed quotient is interpreted in \(\mathbb Z[[q]]\), since \(E(q)\) and \(E(q^t)\) have unit constant terms. The inverse-divisor sum belongs to \(\mathbb F_p\), not to the rational numbers. No result for non-prime-power \(t\) is asserted.

## Proof

**1. A prime-power lifting identity.** Define
\[
E_j(q)=E(q^{p^j}),\qquad
Q_p(q)=\frac{E(q)^p}{E(q^p)}.
\]
The elementary freshman's-dream congruence, applied coefficientwise to the Euler product, gives \(E(q)^p\equiv E(q^p)\pmod p\). Thus there is a unique \(R_p(q)\in q\mathbb Z[[q]]\) such that
\[
Q_p(q)=1+pR_p(q).
\]
For any integer \(k\geq1\), the binomial identity
\[
r\binom{p^k}{r}=p^k\binom{p^k-1}{r-1}
\]
shows that the valuation of \(p^r\binom{p^k}{r}\) is at least \(k+r-\nu_p(r)\) whenever the binomial coefficient is nonzero. For odd \(p\), \(r-\nu_p(r)\geq2\) for all \(r\geq2\). For \(p=2\), the same inequality holds for \(r\geq3\), whereas the quadratic term satisfies
\[
4\binom{2^k}{2}=2^{k+1}(2^k-1).
\]
Consequently, for every \(k\geq1\),
\[
(1+pR)^{p^k}\equiv
\begin{cases}
1+p^{k+1}R\pmod{p^{k+2}},&p\text{ odd},\\
1+2^{k+1}(R+R^2)\pmod{2^{k+2}},&p=2.
\end{cases}
\]
This is a coefficientwise congruence for arbitrary \(R\in\mathbb Z[[q]]\).

**2. Telescoping the two partition generating series.** The exact formal product identity
\[
\frac{F_{p^{2a}}(q)}{C_{p^a}(q)}
=\frac{E_0(q)^{p^{2a}}}{E_a(q)^{p^a}}
=\prod_{j=0}^{a-1}
Q_p(q^{p^j})^{p^{2a-1-j}}
\]
holds without reduction modulo any prime power. For every \(j<a-1\), the lifting identity makes its factor equal to \(1\) modulo \(p^{a+2}\). For the final index \(j=a-1\), the exponent is \(p^a\), so
\[
\frac{F_{p^{2a}}(q)}{C_{p^a}(q)}\equiv
\begin{cases}
1+p^{a+1}R_p(q^{p^{a-1}}),&p\text{ odd},\\
1+2^{a+1}\big(R_2(q^{2^{a-1}})+R_2(q^{2^{a-1}})^2\big),&p=2
\end{cases}
\pmod{p^{a+2}}.
\]
Since \(C_{p^a}(q)\) has integer coefficients and constant term \(1\), multiplication gives coefficientwise divisibility by \(p^{a+1}\) and determines \(D_{p,a}\) modulo \(p\).

**3. The odd-prime correction is an inverse-divisor sum.** For odd \(p\), expanding a single factor and dividing by \(1-z^p\) gives
\[
\frac{(1-z)^p}{1-z^p}=1+
\frac{\sum_{j=1}^{p-1}(-1)^j\binom pj z^j}{1-z^p}.
\]
The integral quantities \(\binom pj/p\) satisfy
\[
\frac{(-1)^j}{p}\binom pj\equiv -j^{-1}\pmod p
\qquad(1\leq j<p).
\]
Modulo \(p\), the first-order term \(R_p\) of the product of these factors is the sum of their first-order terms. Every term of degree \(m\) corresponds uniquely to a factor indexed by a divisor \(m/d\), with \(d\mid m\) and \(p\nmid d\). Hence
\[
R_p(q)\equiv
-\sum_{m\geq1}\left(\sum_{\substack{d\mid m\\p\nmid d}}d^{-1}\right)q^m\pmod p.
\]
Substituting this expression into the formula from Step 2 proves the odd-prime assertion.

**4. The dyadic correction is a square theta series.** For \(p=2\), the local identity is
\[
\frac{(1-z)^2}{1-z^2}=1-\frac{2z}{1+z}.
\]
Therefore, modulo \(2\), the coefficient of \(q^m\) in \(R_2(q)\) is the number of positive divisors of \(m\), reduced modulo \(2\). A positive integer has an odd number of divisors exactly when it is a square. It follows that
\[
R_2(q)\equiv\sum_{r\geq1}q^{r^2}\pmod2,
\qquad
R_2(q)^2\equiv\sum_{r\geq1}q^{2r^2}\pmod2,
\]
where the second identity is the Frobenius square in characteristic \(2\). These give the displayed dyadic formula.

**5. Sharpness and the first failure.** Both corrections in Steps 3 and 4 begin with coefficient \(-1\) at \(q^1\) (where \(-1=1\) in characteristic \(2\)) and have zero constant term. Hence the correction after substitution of \(q^{p^{a-1}}\) has no term below degree \(p^{a-1}\), and its coefficient there is \(-1\) modulo \(p\). Multiplying by \(C_{p^a}(q)\), whose constant term is \(1\), does not alter the first nonzero term. This gives the asserted first failure and proves that \(p^{a+2}\) is not a universal congruence modulus. The proof covers all primes, all positive \(a\), and all coefficient indices.

## Verification

The included standard-library Python program `verify.py` derives the two generating series independently by exact integer recurrences. It checks the universal modulus, the earliest failure degree, and *all* coefficients of both first-residue formulas up to the tested degree. Running `python3 verify.py` produces

`VERIFY_OK cases=12 full_coefficient_checks=1392 dyadic_cases=4`

The test cases include \(p\in\{2,3,5,7,11\}\) and selected exponents \(1\leq a\leq4\), with maximum checked degree \(120\). These finite tests corroborate but do not replace the formal infinite proof above.

## Relationship to prior work

Sharma's 2026 study proves that the coefficientwise congruence \(F_{t^2}\equiv C_t\pmod t\) for every degree holds precisely for prime powers \(t\), and proves the stronger modulus \(p^2\) for \(t=p\). Its Proposition 2 does not state the exact modulus \(p^{a+1}\) at arbitrary prime-power exponents, the first disagreement index modulo \(p^{a+2}\), or the inverse-divisor and dyadic theta correction laws. The present theorem concerns these additional quantitative aspects only; the underlying freshman's-dream technique and partition generating-function identities are prior work.

Han and Ono's earlier work establishes equivalence of the zero sets of the coefficients of \(F_9\) and \(C_3\), not the all-prime-power leading error. Han's earlier work develops the hook-length formula and related \(t\)-core products. OEIS A000731 and A033687 list the \(t=3\) coefficient sequences, but the listed coefficient data do not by themselves supply the uniform all-prime formula. These comparisons do not establish absolute priority; other congruence or formal-group literature may contain an equivalent general theorem.

## Limitations

The theorem treats formal coefficientwise congruences for \(t\) a prime power only; it makes no asymptotic claim, no assertion for non-prime-power \(t\), and no claim that the proof technique is new. The normalized discrepancy is determined modulo \(p\), not to all higher \(p\)-adic orders. Finite checks cannot certify the universal identities independently of the written proof. The literature comparison is best-effort; any inaccessible or not-indexed prior result using general prime-adic Euler-product congruences might imply the main statement. An independent mathematical and priority audit has not been performed.

## References

1. Meenu Sharma, *A Prime-Power Dichotomy for Nekrasov--Okounkov Hook Lengths and \(t\)-Core Partitions* (first public 2026-10-01), arXiv:2610.01422, https://arxiv.org/abs/2610.01422.
2. Guo-Niu Han and Ken Ono, *Hook lengths and 3-cores* (2008 preprint; published 2011), arXiv:0805.2461, https://arxiv.org/abs/0805.2461.
3. Guo-Niu Han, *The Nekrasov–Okounkov hook length formula: refinement, elementary proof, extension and applications*, Annales de l'Institut Fourier 60 (2010), 1–29, https://doi.org/10.5802/aif.2515.
4. OEIS A000731, Euler-product eighth-power coefficients, https://oeis.org/A000731; OEIS A033687, three-core partition counts, https://oeis.org/A033687.
