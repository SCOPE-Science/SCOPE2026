# Exact \(3\)-adic exponent-carrier dichotomy for friends of \(10\)

## Finding
Let \(n\) be a friend of \(10\), so \(n\ne10\) and \(\sigma(n)/n=9/5\). Write
\[
n=\prod_{p\mid n}p^{a_p}.
\]
Then every \(a_p\) is even, \(3\nmid n\), and
\[
\sum_{\substack{p\mid n\\ p\equiv1\pmod 3}}\nu_3(a_p+1)=2.
\]
Thus the primes \(p\equiv1\pmod3\) whose exponent is \(2\pmod6\) form a set of size exactly one or two. If there is one, its exponent is \(8\) or \(44\pmod{54}\). If there are two, each corresponding exponent is \(2\) or \(14\pmod{18}\). Every other prime \(p\equiv1\pmod3\) occurs to an exponent \(0\) or \(4\pmod6\).

## Assumptions and scope
A friend of \(10\) means a positive integer \(n\ne10\) with \(\sigma(n)/n=\sigma(10)/10=9/5\). The statement is conditional because no friend of \(10\) is currently known. The proof uses only elementary properties of the divisor-sum function and the standard lifting-the-exponent identity at the prime \(3\).

The literature-led starting point is the established structure that a friend of \(10\) is an odd square coprime to \(6\), together with the published congruence observation that at least one prime \(p\equiv1\pmod3\) occurs with exponent \(2\pmod6\). The result below refines that existence statement to an exact allocation of the two available \(3\)-adic valuation units.

## Proof
From \(\sigma(n)/n=9/5\) we have
\[
5\sigma(n)=9n.
\]
First, \(5\mid n\). If \(2\mid n\), then \(10\mid n\); strict monotonicity of the abundancy index under proper divisibility would force \(n=10\), contrary to friendship. Hence \(n\) is odd. The displayed equation then makes \(\sigma(n)\) odd. For odd \(n\), the divisor sum is odd exactly when every prime exponent is even, so \(n\) is a square.

We next verify \(3\nmid n\), rather than taking it only as a cited premise. Suppose \(3\mid n\). Since \(n\) is a square and \(5\mid n\), both \(3^2\) and \(5^2\) divide \(n\). If either exponent were at least \(4\), monotonicity would contradict \(I(n)=9/5\), because
\[
I(3^4 5^2)=\frac{3751}{2025}>\frac95,
\qquad
I(3^2 5^4)=\frac{10153}{5625}>\frac95.
\]
Thus \(3^2\parallel n\) and \(5^2\parallel n\). Since \(13=\sigma(3^2)\) and \(31=\sigma(5^2)\), multiplicativity gives \(13\cdot31\mid\sigma(n)\); the equation \(5\sigma(n)=9n\) then forces \(13\cdot31\mid n\). Because \(n\) is a square,
\[
3^2 5^2 13^2 31^2\mid n.
\]
But
\[
I(3^2 5^2 13^2 31^2)=\frac{20191}{10075}>\frac95,
\]
a contradiction. Hence \(3\nmid n\).

Taking \(3\)-adic valuations in \(5\sigma(n)=9n\) now gives
\[
\nu_3(\sigma(n))=2.
\]
By multiplicativity,
\[
2=\sum_{p\mid n}\nu_3(\sigma(p^{a_p})).
\]
All \(a_p\) are even. If \(p\equiv2\pmod3\), then the geometric sum has an odd number of alternating residues,
\[
\sigma(p^{a_p})=1+p+\cdots+p^{a_p}\equiv1\pmod3,
\]
so its \(3\)-adic valuation is zero. If \(p\equiv1\pmod3\), then
\[
\sigma(p^{a_p})=\frac{p^{a_p+1}-1}{p-1},
\]
and lifting the exponent yields
\[
\nu_3(\sigma(p^{a_p}))
=\nu_3(p^{a_p+1}-1)-\nu_3(p-1)
=\nu_3(a_p+1).
\]
This proves the exact identity.

Because \(a_p\) is even, \(\nu_3(a_p+1)>0\) is equivalent to \(a_p\equiv2\pmod6\). A sum of positive integer valuations equal to \(2\) has only two partitions: \(2\), or \(1+1\). In the first case, \(a_p+1\) is divisible by \(9\) but not \(27\); with \(a_p\) even this is equivalent to \(a_p\equiv8\) or \(44\pmod{54}\). In the second case, each \(a_p+1\) is divisible by \(3\) but not \(9\), equivalently \(a_p\equiv2\) or \(14\pmod{18}\). All remaining primes \(p\equiv1\pmod3\) have \(3\nmid a_p+1\), hence \(a_p\equiv0\) or \(4\pmod6\).

## Verification
The accompanying checker verifies the three exact abundancy inequalities used to exclude \(3\mid n\), tests the local valuation formula
\[
\nu_3(\sigma(p^a))=\nu_3(a+1)
\]
for primes \(p\equiv1\pmod3\) and even exponents in a finite regression range, tests zero valuation for \(p\equiv2\pmod3\), and exhaustively checks the stated residue classes for valuation levels \(0,1,2\) across the same exponent range. These computations are regression checks only; the theorem is proved symbolically above.

## Relationship to prior work
Ward's 2008 theorem proves that a friend of \(10\) is an odd square with at least six distinct prime factors, and that at least one prime \(p\equiv1\pmod3\) occurs with exponent \(2\pmod6\). Ward also proves that if there is only one such prime, its exponent is \(8\pmod{18}\). The exact valuation identity here is stronger: it shows there can be at most two such primes, excludes the \(26\pmod{54}\) residue from Ward's singleton congruence, and completely describes the two-prime case.

Thackeray's 2023 preprint, later published in 2024, raises the distinct-prime lower bound to ten and gives primary MSC2020 \(11A25\); it does not state an exact \(3\)-adic allocation among exponents. Chatterjee--Mandal--Mandal's 2024 preprint develops necessary conditions for friends of \(10\), including a prime congruent to \(1\pmod6\), but again does not state the valuation identity or the one-versus-two carrier dichotomy. Mandal's 2025 paper proves a different global restriction, namely that not all half-exponents are \(1\pmod3\); inspection of its exponent theorems found neither the exact valuation sum nor the modulo-
\(54\)/modulo-
\(18\) dichotomy. OEIS A074902 records known friendly numbers and explicitly notes that the status of \(10\) remains unresolved; it does not tabulate hypothetical prime-exponent patterns for a friend of \(10\).

## Limitations
The theorem does not prove that \(10\) is solitary and gives no existence construction for a friend. It constrains only the \(3\)-adic contribution of prime-power divisor sums; other prime-adic constraints remain independent. Literature and database searches cannot constitute an absolute novelty proof, although the most directly relevant papers on exponent structure and the standard friendly-number table were inspected and no implication-equivalent statement was found.

## References
- H. R. Thackeray, *Each friend of 10 has at least 10 nonidentical prime factors*, arXiv:2310.15900v1, 2023; MSC2020 11A25.
- T. Chatterjee, S. Mandal, S. Mandal, *A note on necessary conditions for a friend of 10*, arXiv:2404.00624v1, 2024.
- J. Ward, *Does Ten Have a Friend?*, arXiv:0806.1001, 2008.
- S. Mandal, *Exploring the Relationships Between the Divisors of Friends of 10*, arXiv:2504.08295v1, 2025.
- OEIS A074902, *Known friendly numbers*.
