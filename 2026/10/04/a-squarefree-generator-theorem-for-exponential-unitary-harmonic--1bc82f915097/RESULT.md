# A squarefree-generator theorem for exponential-unitary harmonic numbers
## Finding
Fix an integer \(a\ge2\) and a prime \(p\). Put
\[
t_a=2^{\omega(a)},\qquad E_a(p)=\sum_{d\parallel a}p^{a-d},\qquad M_a(p)=\frac{E_a(p)}{\gcd(E_a(p),t_a)},
\]
where \(d\parallel a\) means that \(d\) is a unitary divisor of \(a\). For every squarefree integer \(m\ge1\) with \(\gcd(m,p)=1\), the integer \(n=p^a m\) has integral harmonic mean of its exponential-unitary divisors if and only if \(M_a(p)\) is squarefree and
\[
m=M_a(p)s
\]
for a squarefree \(s\) satisfying \(\gcd(s,pM_a(p))=1\). Thus this fixed \((a,p)\) stratum is empty when \(M_a(p)\) is not squarefree, while otherwise its counting function satisfies
\[
N_{a,p}(X)=C_{a,p}X+O_{a,p}(\sqrt X),\qquad C_{a,p}=\frac{6}{\pi^2p^aM_a(p)}\prod_{q\mid pM_a(p)}\frac{q}{q+1}.
\]

## Assumptions and scope
An exponential-unitary divisor of \(n=\prod r_i^{e_i}\) is a divisor \(\prod r_i^{f_i}\) in which every \(f_i\) is a unitary divisor of \(e_i\), meaning \(f_i\mid e_i\) and \(\gcd(f_i,e_i/f_i)=1\). An exponential-unitary harmonic number is one whose exponential-unitary divisors have integral harmonic mean. The theorem treats the complete stratum in which exactly one prime exponent can exceed \(1\): \(n=p^a m\), with \(a\ge2\), \(p\) prime, and \(m\) squarefree and coprime to \(p\). The pair \((a,p)\) is fixed in the asymptotic statement.

## Proof
The exponent \(1\) has only one unitary divisor, so every prime dividing the squarefree factor \(m\) occurs in every exponential-unitary divisor of \(n\). Hence those divisors are exactly
\[
mp^d\qquad(d\parallel a).
\]
The number of unitary divisors of \(a\) is \(t_a=2^{\omega(a)}\). Therefore the harmonic mean \(H_{e*}(n)\) of the exponential-unitary divisors is
\[
H_{e*}(n)=\frac{t_a}{\sum_{d\parallel a}(mp^d)^{-1}}
=\frac{p^a m t_a}{E_a(p)},
\qquad E_a(p)=\sum_{d\parallel a}p^{a-d}.
\]
Since \(a\parallel a\), the summand with \(d=a\) equals \(1\), while all other summands are divisible by \(p\). Consequently
\[
\gcd(E_a(p),p)=1.
\]
Thus \(H_{e*}(n)\) is integral exactly when \(E_a(p)\mid mt_a\). Write \(g=\gcd(E_a(p),t_a)\), \(E_a(p)=gM_a(p)\), and \(t_a=gt'\). Then \(\gcd(M_a(p),t')=1\), so
\[
E_a(p)\mid mt_a\quad\Longleftrightarrow\quad M_a(p)\mid m.
\]
Because \(m\) is squarefree, this is possible exactly when \(M_a(p)\) is squarefree. In that case, writing \(m=M_a(p)s\), squarefreeness of \(m\) and \(\gcd(m,p)=1\) is equivalent to \(s\) being squarefree with \(\gcd(s,pM_a(p))=1\). This proves the classification.

For the counting statement, assume \(M=M_a(p)\) is squarefree and put \(Y=X/(p^aM)\). The classification gives
\[
N_{a,p}(X)=\#\{s\le Y:\ s\text{ squarefree},\ \gcd(s,pM)=1}\}.
\]
The standard squarefree counting argument by Möbius inversion, with the finitely many primes dividing \(pM\) excluded, yields
\[
\#\{s\le Y:\ s\text{ squarefree},\ \gcd(s,Q)=1}\}
=\frac6{\pi^2}\prod_{q\mid Q}\frac q{q+1}Y+O_Q(\sqrt Y).
\]
Taking \(Q=pM\) gives the stated constant and error term. If \(M_a(p)\) is not squarefree, the classification shows that the counting function is identically zero.

## Verification
The bundled `verify.py` independently enumerates unitary divisors of each exponent and computes the harmonic mean divisibility directly. It compares that definition with the theorem for every \(2\le a\le12\), every prime \(p<40\), and every squarefree \(m\le500\) coprime to \(p\), totaling \(36,025\) triples. Its replay output is:

`VERIFY_OK checked=36025 hits=[(2, 2, 3, 12), (2, 2, 15, 60), (2, 2, 21, 84), (2, 2, 33, 132), (2, 2, 39, 156), (2, 2, 51, 204), (2, 2, 57, 228), (2, 2, 69, 276), (2, 2, 87, 348), (2, 2, 93, 372), (2, 2, 105, 420), (2, 2, 111, 444)] spots=[(2, 2, 3, 2, 3, True), (2, 3, 4, 2, 2, True), (4, 2, 9, 2, 9, False), (4, 3, 28, 2, 14, True), (6, 2, 57, 4, 57, True), (6, 3, 352, 4, 88, False), (8, 2, 129, 2, 129, True), (10, 2, 801, 4, 801, False)]`

The finite replay corroborates the exact criterion; it is not used to prove the unrestricted classification or the asymptotic.

## Relationship to prior work
Tóth and Minculete introduced exponential-unitary divisors and the associated divisor functions. Minculete's thesis then defines exponential harmonic numbers of type 4 exactly through the harmonic mean of exponential-unitary divisors and gives examples and sufficient constructions, including a proposition for a class of e-semiproper perfect numbers. The inspected thesis section does not state an exact criterion for the one-repeated-prime/squarefree-cofactor stratum, nor a density for a fixed \((a,p)\) layer. OEIS A349025 records the multiplicative denominator function \(E_a(p)\), and A349026 tabulates exponential-unitary harmonic numbers, but neither entry states the squarefree-generator classification or the asymptotic.

The theorem is not a reformulation of exponential-unitary perfectness: integrality of the harmonic mean asks for divisibility by \(E_a(p)\), while exponential-unitary perfectness asks for a divisor-sum equality. It is also distinct from ordinary exponential harmonicity, where all divisors of the exponent rather than only unitary divisors are used.

## Limitations
The theorem does not classify integers with two or more nonsquarefree prime-power components. The asymptotic is only for each fixed pair \((a,p)\); no uniformity in \(a\) or \(p\) is claimed. The density constant is positive exactly in the squarefree-generator cases, but the theorem does not classify all pairs \((a,p)\) for which \(M_a(p)\) is squarefree. The literature comparison cannot exclude an equivalent result hidden in unindexed sources, although the exact thesis section, exact OEIS tables, targeted web searches, and semantic research-result searches were checked.

## References
1. L. Tóth and N. Minculete, “Exponential unitary divisors,” arXiv:0910.2798, first public version 2009-10-15.
2. N. Minculete, “Concerning Some Arithmetic Functions Which Use Exponential Divisors,” *Acta Universitatis Apulensis* 28 (2011), 125–133. The paper lists the single MSC classification 11A25.
3. N. Minculete, *Contribuţii la studiul proprietăţilor analitice ale funcţiilor aritmetice – Utilizarea e-divizorilor*, Ph.D. thesis, Academia Română, 2012, Section 4.3, especially pp. 90–94; thesis defense recorded on 2012-03-16.
4. OEIS A349025, the exponential-unitary reciprocal-sum denominator function.
5. OEIS A349026, exponential-unitary harmonic numbers.
