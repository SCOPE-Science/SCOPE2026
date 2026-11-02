# The four-factor layer of three-prime \(2\)-near-perfect integers

## Finding
Let \(\sigma(n)\) be the sum of the positive divisors of \(n\), and let \(\omega(n)\) and \(\Omega(n)\) be the numbers of distinct prime factors and prime factors with multiplicity, respectively. An integer \(n\) is **\(2\)-near-perfect** when there exist two *distinct* positive divisors \(d_1,d_2\mid n\) satisfying
\[
\sigma(n)=2n+d_1+d_2.
\]
For every positive integer \(n\) satisfying \(\omega(n)=3\) and \(\Omega(n)=4\), the integer \(n\) is \(2\)-near-perfect if and only if
\[
\boxed{n\in\{84,90,126,132,156,198,220,364,380,550\}.}
\]
For each of these ten integers, the *unordered* pair of omitted divisors is unique:

| \(n\) | Prime factorization | \(\{d_1,d_2\}\) |
|---:|:---|:---|
| 84 | \(2^2\cdot3\cdot7\) | \(\{14,42\}\) |
| 90 | \(2\cdot3^2\cdot5\) | \(\{9,45\}\) |
| 126 | \(2\cdot3^2\cdot7\) | \(\{18,42\}\) |
| 132 | \(2^2\cdot3\cdot11\) | \(\{6,66\}\) |
| 156 | \(2^2\cdot3\cdot13\) | \(\{2,78\}\) |
| 198 | \(2\cdot3^2\cdot11\) | \(\{6,66\}\) |
| 220 | \(2^2\cdot5\cdot11\) | \(\{20,44\}\) |
| 364 | \(2^2\cdot7\cdot13\) | \(\{4,52\}\) |
| 380 | \(2^2\cdot5\cdot19\) | \(\{4,76\}\) |
| 550 | \(2\cdot5^2\cdot11\) | \(\{5,11\}\) |

In particular, no odd integer with \(\omega(n)=3\) and \(\Omega(n)=4\) is \(2\)-near-perfect, and no integer of the form \(2pq^2\), for odd primes \(p<q\), is \(2\)-near-perfect.

## Assumptions and scope
All primes are positive rational primes. Whenever \(p<q\) appear together they are distinct odd primes. All positive divisors, including \(n\) itself, are allowed in the definition; the ten actual omitted pairs happen to consist of proper divisors. The theorem is unconditional and ranges over every positive integer satisfying the stated prime-factor-count restrictions.

Every integer with \(\omega(n)=3\) and \(\Omega(n)=4\) has three prime exponents \(2,1,1\). If it is even, it has exactly one of the forms \(4pq\), \(2p^2q\), or \(2pq^2\) with \(p<q\) odd primes. If it is odd, it has the form \(r^2st\) with distinct odd primes \(r,s,t\). These cases exhaust the domain.

## Proof
**1. Excluding odd integers.** Each odd case has two primes to the first power and one to the second. The quotient \(\sigma(n)/n\) is maximal when the three primes are \(3,5,7\), with the square on \(3\): the local factor \(1+1/p+1/p^2\) and the factor \(1+1/p\) both decrease with \(p\), and the extra factor from squaring, \(1+1/(p(p+1))\), is largest at the smallest prime. Consequently
\[
\frac{\sigma(n)}n\le
\left(1+\frac13+\frac19\right)
\left(1+\frac15\right)
\left(1+\frac17\right)
=\frac{624}{315}<2.
\]
This contradicts \(\sigma(n)=2n+d_1+d_2>2n\).

**2. The \(4pq\) case.** Multiplicativity gives
\[
\Delta:=\sigma(4pq)-8pq=7(p+1)(q+1)-8pq=(7-p)q+7(p+1).
\]
When \(p\ge17\), \(\Delta<(7-p)p+7(p+1)=-p^2+14p+7<0\). When \(p=13\), the next larger prime \(q\ge17\) gives \(\Delta\le98-6\cdot17=-4\). When \(p=11\), positivity requires \(q<21\), hence \(q\in\{13,17,19\}\).

Suppose \(p\in\{3,5,7\}\). Set \(c=7-p\) and \(B=7(p+1)\); then \(\Delta=cq+B\). Every divisor of \(4pq\) is either \(a\) or \(aq\), with \(a\mid4p\). Two divisors not divisible by \(q\) have sum at most \(6p<\Delta\), so at least one omitted divisor contains \(q\). If exactly one does, its equation is
\[
(a-c)q=B-b\qquad(a,b\mid4p).
\]
Since \(B-b\ge B-4p>0\), the integer \(a-c\) is positive, and \(q\le B\). If both omitted divisors contain \(q\), the equation is \((a+b-c)q=B\), again forcing \(q\le B\). Therefore the only candidates have \(q\le28,42,56\) for \(p=3,5,7\), respectively, along with the three candidates for \(p=11\). An exhaustive check of these 32 prime pairs (each has twelve distinct divisors) gives exactly
\[
\begin{array}{c|l}
p & (q,\{d_1,d_2\})\\\hline
3 &(7,\{14,42\}),(11,\{6,66\}),(13,\{2,78\})\\
5 &(11,\{20,44\}),(19,\{4,76\})\\
7 &(13,\{4,52\})\\
11&\text{none}.
\end{array}
\]
The `verify.py` script independently enumerates all twelve divisors for each finite candidate and every unordered pair.

**3. The \(2p^2q\) case.** Here
\[
\Delta:=\sigma(2p^2q)-4p^2q
=(3+3p-p^2)q+3(p^2+p+1).
\]
For \(p\ge7\), the coefficient of \(q\) is negative. Since \(q>p\),
\[
\Delta< -p^3+6p^2+6p+3
\le -p^2+6p+3<0,
\]
where the second inequality uses \(p-6\ge1\). Hence \(p\) is either \(3\) or \(5\). For \(p=5\), the formula becomes \(93-7q\), so \(q\in\{7,11,13\}\); only \(q=11\) works, with omitted pair \(\{5,11\}\).

For \(p=3\), \(\Delta=3q+39\), and every divisor is \(a\) or \(aq\) with \(a\in\{1,2,3,6,9,18\}\). Two divisors without \(q\) have sum at most \(18+9=27<\Delta\). With exactly one \(q\)-divisible omitted divisor we get \((a-3)q=39-b\), so \(a>3\) and \(q\le(39-1)/3<13\). With two \(q\)-divisible omitted divisors we get \((a+b-3)q=39\). Since \(q>3\) is prime, this would require \(q=13\) and distinct \(a,b\) summing to \(6\), which is impossible in the displayed divisor set. Thus only \(q\in\{5,7,11\}\) remain. Direct pair comparison yields precisely \(\{9,45\},\{18,42\},\{6,66\}\), respectively.

**4. The \(2pq^2\) case.** Now
\[
\Delta:=\sigma(2pq^2)-4pq^2
=(3-p)q^2+3(p+1)(q+1).
\]
For \(p\ge7\), because \(q\ge p+2\),
\[
3(p+1)(q+1)\le3(q-1)(q+1)<4q^2\le(p-3)q^2,
\]
so \(\Delta<0\). For \(p=5\), \(\Delta=-2q^2+18(q+1)<0\) for \(q\ge11\), leaving only \(q=7\). For \(p=3\), \(\Delta=12(q+1)\). If \(q\ge13\), then \(q^2>12(q+1)=\Delta\), excluding any divisor divisible by \(q^2\); the two largest remaining divisors are \(6q\) and \(3q\), whose sum \(9q<\Delta\). Thus only \(q\in\{5,7,11\}\) remain. Exhaustive divisor-pair checks for the four possibilities \((p,q)=(3,5),(3,7),(3,11),(5,7)\) yield none.

All possibilities have now been exhausted. The finite enumeration in Steps 2–4 tests *every* pair of distinct divisors of each remaining integer, establishing both the listed ten examples and the uniqueness of their unordered omitted pairs. \(\square\)

## Verification
Run `python3 verify.py` in the directory containing this document. It requires only the Python 3 standard library. It independently constructs divisors and checks all unordered pairs in the 32 finite \(4pq\) cases, the six finite \(2p^2q\) cases, and the four finite \(2pq^2\) cases. It also rederives the possible \(q\) values for \(p=3\) in the middle case and checks the exact odd-case inequality. The expected output begins with `VERIFY_OK unique_examples=10`. The finite verifier is exhaustive **only because** the algebraic exclusions above reduce every infinite branch to those finite sets; standalone numerical testing beyond those sets would not prove the theorem.

## Relationship to prior work
Aryan, Madhavani, Parikh, Slattery and Zelinsky (first public arXiv version 2023-10-02, subsequently *Integers* 24 (2024), A61) classify \(2\)-near-perfect numbers with exactly two distinct prime factors in specified exponent families; the present theorem concerns three distinct prime factors. Fearon, Foushee, Porosoff, Skula, Zelinsky and Zhang (arXiv:2508.06651, first public 2025-08-08) complete the two-prime-support classification. Their later publicly available version includes a table of initial three-prime examples and explicitly identifies classification of three-prime-support families as a further direction, but gives no classification at \(\omega(n)=3,\Omega(n)=4\).

The existing squarefree three-prime result for \(2pq\) concerns \(\Omega(n)=3\), so is disjoint. An earlier classification of \(2p^2q\) already determines four of the present ten cases. The new content is the complete **three-prime, four-factor** theorem, including the six \(4pq\) cases, the obstruction for \(2pq^2\), the odd obstruction, and the cross-shape exhaustiveness. The OEIS sequence A341475 records many individual examples, but a finite list of terms does not imply the infinite exclusion theorem.

## Limitations
This does not classify \(2\)-near-perfect numbers with three prime supports and \(\Omega(n)\ge5\), nor those with more than three distinct prime supports. The proof depends on elementary inequalities and small exhaustive finite divisor-pair calculations, with a fully reproducible standalone checker. Novelty is assessed against identified literature and indexed mathematical records, not asserted as an absolute priority certificate.

## References
1. V. Aryan, D. Madhavani, S. Parikh, I. Slattery, J. Zelinsky, “On 2-Near Perfect Numbers,” arXiv:2310.01305 (first submitted 2023-10-02); *Integers* 24 (2024), A61, https://math.colgate.edu/~integers/y61/y61.pdf.
2. R. Fearon, H. Foushee, B. Porosoff, A. Skula, J. Zelinsky, K. Zhang, “Complete characterization of 2-near perfect numbers with exactly 2 prime factors,” arXiv:2508.06651 (first submitted 2025-08-08), https://arxiv.org/abs/2508.06651.
3. OEIS Foundation, A341475, “2-near-perfect numbers,” https://oeis.org/A341475.
4. Published mathematical record, “Squarefree \(2\)-near-perfect numbers with three prime factors,” https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-squarefree-2-near-perfect-numbers-with-three-prime-factors--ab9cfade94ac.
