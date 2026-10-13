# An exact semiprime support sieve for the average-divisor increment equation
## Finding
Let \(\sigma(n)\) denote the sum of the positive divisors of \(n\), and let \(\tau(n)\) denote their number. Consider the equation
\[
\sigma(n+1)-\sigma(n)=\frac{\sigma(n)}{\tau(n)}. \tag{1}
\]

**Theorem.** For distinct primes \(p<q\), if \(n=pq\) satisfies (1), then
\[
p\in\{2,3\}.
\]
The two surviving prime-support branches obey the further constraints
\[
p=2\ \Longrightarrow\ q\equiv15\pmod{16},\qquad
p=3\ \Longrightarrow\ q\equiv11\pmod{12}.
\]
The branch with smaller prime \(3\) has an exact parametrization: \(n=3q\) satisfies (1) if and only if there exists \(r\in\mathbb Z_{\ge0}\) for which
\[
q=12r+11\text{ is prime},\qquad \sigma(18r+17)=20(r+1). \tag{2}
\]
For instance \(r=20\) and \(r=4115\) give
\[
n=753\quad\text{and}\quad n=148173.
\]

## Assumptions and scope
The theorem concerns *squarefree semiprimes*, meaning products of two **distinct** primes \(p<q\). Prime squares and integers with more than two prime factors are outside its scope.

For such a semiprime,
\[
\sigma(pq)=(p+1)(q+1),\qquad \tau(pq)=4.
\]
Consequently, (1) is equivalent to
\[
4\sigma(pq+1)=5(p+1)(q+1). \tag{3}
\]
The result is an unrestricted exclusion of all smaller prime factors \(p\ge5\), plus a residue sieve and an exact odd-argument reduction for the remaining branches. It does **not** establish that the \(p=2\) branch is empty.

## Proof
**Step 1: a bound for the smaller prime.** For any even integer \(m\ge4\), the divisors \(1,m/2,m\) are distinct. Thus
\[
\sigma(m)>\frac{3m}{2}.
\]
If \(p,q\) are odd, then \(m=pq+1\) is even. Substitution into (3) yields
\[
5(p+1)(q+1)>6(pq+1),
\]
which is equivalent to
\[
(p-5)(q-5)<24. \tag{4}
\]
For \(p\ge11\), since \(q\ge13\), the left side is at least \(48\), contradicting (4). When \(p=7\), (4) forces \(q<17\), hence \(q\in\{11,13\}\). Both pairs fail (3):
\[
\sigma(78)=168\ne120=\frac54(8)(12),
\]
\[
\sigma(92)=168\ne140=\frac54(8)(14).
\]

**Step 2: excluding \(p=5\).** Let \(q>5\) be prime and put \(m=5q+1\). Equation (3) requires
\[
\sigma(m)=\frac{15}{2}(q+1)=\frac{3m}{2}+6. \tag{5}
\]
If \(q\equiv1\pmod4\), then \(m=2t\) for an odd integer \(t>1\). Multiplicativity gives \(\sigma(m)=3\sigma(t)\), so (5) would require
\[
\sigma(t)=t+2.
\]
No odd integer \(t>1\) satisfies this: a prime has \(\sigma(t)=t+1\), whereas an odd composite has at least the additional proper divisor \(3\) or larger and therefore \(\sigma(t)\ge t+4\).

If \(q\equiv3\pmod4\), then \(4\mid m\) and \(m\ge36\). Its distinct divisors \(1,m/4,m/2,m\) give
\[
\sigma(m)\ge\frac{7m}{4}+1>\frac{3m}{2}+6
\]
for \(m>20\), contradicting (5). Thus no \(p=5\) case occurs. Combining with Step 1 proves \(p\in\{2,3\}\).

**Step 3: the \(p=3\) branch.** For odd prime \(q>3\), equation (3) reads
\[
\sigma(3q+1)=5(q+1). \tag{6}
\]
If \(q\equiv1\pmod4\), then \(m=3q+1\) is divisible by \(4\). For \(q\ge13\), the divisor lower bound gives
\[
\sigma(m)\ge\frac{7m}{4}+1>5(q+1),
\]
because the difference of the two right-hand sides is \((q-9)/4>0\). The only remaining prime in this residue class is \(q=5\), for which \(\sigma(16)=31\ne30\). Therefore \(q\equiv3\pmod4\).

Set \(t=(3q+1)/2\), which is then odd. Multiplicativity in (6) gives
\[
3\sigma(t)=5(q+1).
\]
In particular \(3\mid q+1\), so \(q\equiv2\pmod3\). Together with \(q\equiv3\pmod4\), this is
\[
q\equiv11\pmod{12}.
\]
Write \(q=12r+11\) with \(r\ge0\). Then \(t=18r+17\), and the exact equation becomes
\[
\sigma(18r+17)=20(r+1).
\]
Conversely, if \(q=12r+11\) is prime and this last equality holds, all preceding identities reverse, proving that \(n=3q\) satisfies (1). This proves (2).

**Step 4: the \(p=2\) branch.** Let \(n=2q\) with odd prime \(q\). Equation (3) becomes
\[
\sigma(2q+1)=\frac{15(q+1)}4. \tag{7}
\]
Integrality forces \(4\mid q+1\), hence \(q\equiv3\pmod4\). Then \(m=2q+1\equiv3\pmod4\).

For every odd integer \(m\equiv3\pmod4\), one has \(4\mid\sigma(m)\): in its prime factorization, some prime \(s\equiv3\pmod4\) has odd exponent \(2a+1\); the factor
\[
\sigma(s^{2a+1})=(1+s)(1+s^2+\cdots+s^{2a})
\]
is divisible by \(4\), and it divides \(\sigma(m)\) by multiplicativity. Applying this to (7) yields
\[
4\ \Bigm|\ \frac{15(q+1)}4.
\]
Since \(15\) is odd, it follows that \(16\mid q+1\), or
\[
q\equiv15\pmod{16}.
\]
This condition is only necessary; the theorem makes no sufficiency or nonexistence claim for this branch.

The four steps prove the theorem.

## Verification
The accompanying `verify.py` uses exact integer sieves to compute \(\sigma\), primality and the distinct-prime factorization of every squarefree semiprime up to \(2{,}000{,}000\). It compares (1) directly against (3), checks that every hit has smaller prime \(2\) or \(3\), and verifies each residue and parametrization restriction. It checks the exact witnesses \(753\) and \(148173\), including the underlying odd-divisor-sum identities.

The infinite exclusion of \(p\ge5\) and the parametrization follow from the symbolic proof, not from the finite computation.

## Relationship to prior work
OEIS A066176 is the exact sequence of solutions of (1), first authored on 14 December 2001. It displays the original numerical examples and the interpretation as a one-step divisor-sum increase equal to the average divisor size. Its inspected definition, comments, examples and programs do not give a semiprime support theorem.

OEIS A003601 classifies the *arithmetic numbers*, for which \(\sigma(n)/\tau(n)\) is integral. Every solution of (1) necessarily belongs to that class. Classical arithmetic-number results, including those of Bateman, Erdős, Pomerance and Straus, investigate divisibility and distribution of the divisor average without the separate adjacent-term condition in (1).

Oller-Marcén's full open-access paper characterizes arithmetic numbers via cyclotomic factorizations and gives exact criteria for prime powers and cube-free inputs, but it does not constrain \(\sigma(n+1)-\sigma(n)\). Those arithmetic-number criteria therefore do not imply the support exclusion or residue restrictions for the present equation.

OEIS A066177 concerns the *negative* increment, \(\sigma(n+1)-\sigma(n)=-\sigma(n)/\tau(n)\), so it is a distinct predicate. A related result on equal consecutive divisor sums treats zero increment rather than the positive divisor-average increment here.

Targeted searches of the exact database identifier, the defining equation, mean-divisor terminology, the semiprime formula (3), and the two residue classes did not locate a stronger implication covering this theorem.

## Limitations
The theorem makes no classification claim for integers that are not squarefree semiprimes. In the \(p=2\) branch the congruence is necessary, not sufficient; no general nonexistence theorem is claimed. In the \(p=3\) branch, the parametrization still requires a prime value and an exact divisor-sum equation, and infinitude is unknown.

The table check through \(2{,}000{,}000\) is finite evidence only. An equivalent elementary observation could occur in an unindexed discussion of the original sequence.

## References
1. OEIS Foundation, A066176, integers whose sum-of-divisors increment equals their average divisor size, initial entry by Joseph L. Pe, 14 December 2001.
2. OEIS Foundation, A003601, arithmetic numbers characterized by divisibility \(\tau(n)\mid\sigma(n)\).
3. OEIS Foundation, A066177, negative average-divisor increment.
4. P. T. Bateman, P. Erdős, C. Pomerance and E. G. Straus, “The arithmetic mean of the divisors of an integer,” in *Analytic Number Theory*, Lecture Notes in Mathematics 899 (1981), 197–220; lawful author-hosted PDF at `https://math.dartmouth.edu/~carlp/PDF/31.pdf`.
5. A. M. Oller-Marcén, “On arithmetic numbers,” *Mathematische Nachrichten* 288 (2015), 665–669, DOI `10.1002/mana.201400085`, open preprint arXiv:1206.1823 (8 June 2012).
