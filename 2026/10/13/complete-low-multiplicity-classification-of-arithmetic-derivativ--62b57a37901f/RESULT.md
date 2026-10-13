# Complete low-multiplicity classification of arithmetic-derivative/aliquot coincidences

## Finding
For every integer \(n\ge2\) with at most four prime factors counted with multiplicity,
\[
D(n)=\sigma(n)-n\quad\Longleftrightarrow\quad n\text{ is prime or }n\in\{12,18,220\}.
\]
Here \(D\) is the arithmetic derivative and \(\sigma\) the sum of positive divisors. Thus no composite with \(\Omega(n)\le2\) is a solution; the unique solutions at multiplicities \(3\) and \(4\) are, respectively, \(12,18\) and \(220\).

## Assumptions and scope
For integers \(n\ge1\), set \(D(1)=0\), \(D(p)=1\) for primes, and \(D(ab)=aD(b)+bD(a)\). Thus, for \(n=\prod_i p_i^{e_i}\),
\[
D(n)=n\sum_i\frac{e_i}{p_i}.
\]
The divisor sum is \(\sigma(n)=\sum_{d\mid n}d\), and the aliquot sum is \(s(n)=\sigma(n)-n\). The multiplicity \(\Omega(n)=\sum_i e_i\). The classification concerns \(n\ge2\), \(\Omega(n)\le4\); the excluded integer \(1\) also satisfies \(D(1)=s(1)=0\).

## Proof
Write \(E(n)=\sigma(n)-n-D(n)\). We exhaust the partitions of the exponent total \(\Omega(n)\le4\); in each expression, displayed primes are distinct.

**Squarefree integers.** If \(n=p_1\cdots p_k\) with \(k\ge2\), expand \(\prod_i(p_i+1)\). The leading term is \(n\), and the sum of all terms missing exactly one prime equals \(D(n)\). At least the constant term remains, so \(E(n)>0\). If \(k=1\), both sides of \(D(p)=s(p)=1\) agree.

**Prime powers.** For \(a\ge2\),
\[
E(p^a)=\sum_{j=0}^{a-1}p^j-ap^{a-1}<0,
\]
since every summand is at most \(p^{a-1}\) and one is strictly smaller. This covers all nonprime one-support cases.

**One squared prime and one single prime.** If \(n=p^2q\), then
\[
E(p^2q)=(p+1)-(p-1)q.
\]
Hence \(E=0\) requires \(q=(p+1)/(p-1)=1+2/(p-1)\). The prime and distinctness restrictions leave exactly \((p,q)=(2,3)\) and \((3,2)\), producing \(12\) and \(18\).

**One cubed prime and one single prime.** If \(n=p^3q\),
\[
E(p^3q)=(p^2+p+1)-(2p^2-p-1)q.
\]
For every \(p\ge2\), the positive denominator \(2p^2-p-1\) satisfies \(2(2p^2-p-1)>p^2+p+1\), since \(3(p^2-p-1)>0\). Thus \(E=0\) would give \(q<2\), impossible for a prime.

**Two squared primes.** For distinct primes \(p<q\),
\[
E(p^2q^2)=-(p-1)q^2-(p^2-p-1)q+(p^2+p+1).
\]
Since \(p^2-p-1\ge1\) for \(p\ge2\) and \(q\ge p+1\),
\[
E(p^2q^2)\le -(p-1)(p+1)^2+p^2+p+1=-p^3+2p+2<0.
\]
(The final polynomial is at most \(-2\) for integer \(p\ge2\).)

**One squared prime and two other primes.** For \(n=p^2qr\),
\[
E(p^2qr)=(1-p)qr+(p+1)(q+r)+(p^2+p+1).
\]
If \(p\) is odd, the first two summands are even and the last is odd, so \(E\ne0\). If \(p=2\), necessarily \(q,r\) are distinct odd primes; \(E=0\) is equivalent to
\[
(q-3)(r-3)=16.
\]
The two factors must be positive even integers. Up to exchange, the only possibilities are \((q-3,r-3)=(2,8)\) or \((4,4)\), yielding \((q,r)=(5,11)\) or \((7,7)\). The latter violates distinctness, so \(n=2^2\cdot5\cdot11=220\) is unique.

The possible exponent patterns up to total \(4\) have now all been treated: pure powers, squarefree products, \((2,1)\), \((3,1)\), \((2,2)\), and \((2,1,1)\). Direct substitution confirms \(D(12)=s(12)=16\), \(D(18)=s(18)=21\), and \(D(220)=s(220)=284\), completing both implications. \(\square\)

## Verification
The included standalone `verify.py` computes arithmetic derivatives by the product-rule recurrence, proper-divisor sums by a divisor sieve, and \(\Omega\) by least-prime-factor recursion. Run `python verify.py --limit 500000`. A completed execution reported `VERIFY_OK limit=500000 omega_le4_checked=373796 composite_zeros=[12, 18, 220] boundary_omega5=396`. The direct boundary check gives \(D(396)=\sigma(396)-396=696\) and \(\Omega(396)=5\). The finite test is corroboration and is not the proof of the infinite statement.

## Relationship to prior work
OEIS A211991 defines exactly the signed difference \(D(n)-s(n)\). OEIS A212127 lists the zeros, recording the primes and early composite values \(12,18,220\), but the inspected entries supply numerical witnesses rather than a theorem excluding other integers with \(\Omega(n)\le4\). Ufnarovski and Åhlander (2003) give the general arithmetic-derivative formula, not this complete small-multiplicity classification. The result therefore classifies a natural multiplicity stratum of an already documented equation; it does not claim to discover the listed integers.

## Limitations
No classification for \(\Omega(n)\ge5\) is asserted: \(396\) already supplies another composite equality at multiplicity \(5\). The theorem is established by elementary exhaustive exponent-pattern reasoning and does not assert uniqueness in unsearched publications. The computational check uses a finite range only.

## References
- O. E. Pol, OEIS A211991, “Difference between the arithmetic derivative of n and the sum of proper divisors of n,” entry authored 18 December 2012, https://oeis.org/A211991.
- O. E. Pol, OEIS A212127, “Numbers n whose arithmetic derivative equals the sum of its proper divisors,” entry authored 18 December 2012, https://oeis.org/A212127.
- V. Ufnarovski and B. Åhlander, “How to Differentiate a Number,” *Journal of Integer Sequences* 6 (2003), Article 03.3.4, published 17 September 2003, https://cs.uwaterloo.ca/journals/JIS/VOL6/Ufnarovski/ufnarovski.pdf.
