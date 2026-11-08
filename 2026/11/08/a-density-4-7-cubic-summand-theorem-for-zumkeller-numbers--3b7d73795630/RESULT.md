# A density-\(4/7\) cubic-summand theorem for Zumkeller numbers

## Finding
Let \(\mathcal Z\) be the positive integers whose positive divisors split into two equal-sum sets. Let
\[\mathcal R_3=\{N\ge1:N=z+x^3,\quad z\in\mathcal Z,\quad x\in\mathbb Z_{>0}\}.\]
For every integer \(j\ge0\), the represented numbers have full relative natural density in the stratum of integers with \(\nu_2(N)=3j\). Precisely,
\[\lim_{X\to\infty}\frac1X\#\{N\le X:N\in\mathcal R_3,\ \nu_2(N)=3j\}=2^{-(3j+1)}.\]
Consequently,
\[\boxed{\liminf_{X\to\infty}\frac{\#(\mathcal R_3\cap[1,X])}{X}\ge\frac47}.\]
In particular, almost every odd integer is a positive cube plus a Zumkeller number.

## Assumptions and scope
All integers are positive except explicitly stated indices. We set \(\nu_2(N)=a\) for \(2^a\mid N\) and \(2^{a+1}\nmid N\). A Zumkeller number is an integer whose complete set of positive divisors admits an equal-sum bipartition. The assertion is about natural density, not universal representability or a sharp exception cutoff. The supporting 2023 source explicitly proposes study of Zumkeller numbers plus higher powers such as cubes.

## Proof
**Lemma 1 (a Zumkeller progression).** Let \(p\) be an odd prime, and choose an integer \(k\ge1\) with \(p\le2^{k+1}-1\). Then \(z=2^kp\) is Zumkeller. Indeed set \(T=2^{k+1}-1\), \(A=(T-p)/2\), and \(B=(T+1)/2\). Since \(0\le A,B\le T\), express \(A\) and \(B\) independently as sums of distinct powers \(1,2,\ldots,2^k\). The first collection of divisors \(2^i\), and the second collection of divisors \(p2^i\), together sum to
\[A+pB=\frac{(p+1)T}{2}=\frac{\sigma(2^kp)}2.\]
For every integer \(t\ge0\), the number
\[z_t=z(1+2pt)=z+tM,\qquad M=2^{k+1}p^2,\]
is also Zumkeller: its second factor is coprime to \(z\), and coprime multiplication preserves the Zumkeller property. This construction is consistent with the published two-prime-support criterion and the coprime multiplication lemma; only its use for cubic sums is new here.

**Lemma 2 (cubic covering).** Fix an integer \(a\ge0\) with \(3\mid a\), and a prime \(p\equiv2\pmod3\). Choose \(k>a\) large enough for Lemma 1, and put \(z=2^kp\), \(M=2^{k+1}p^2\). If \(\nu_2(N)=a\) and \(p\nmid N\), then the congruence
\[x^3\equiv N-z\pmod M\]
has a solution \(1\le x\le M\). To see this, write \(a=3j\). The right side has exact \(2\)-adic valuation \(a\), because \(k>a\); its odd quotient modulo \(2^{k+1-a}\) has a cube root since the cube map is an automorphism of the group of odd units modulo every power of two. Multiplying that cube root by \(2^j\) gives the required solution modulo \(2^{k+1}\). Also \(p\nmid N-z\), and the cube map on units modulo \(p^2\) is bijective since \(3\nmid p(p-1)\). The Chinese remainder theorem joins these congruences to obtain \(x\) modulo \(M\). If \(N\ge z+M^3\), then \(N-x^3=z+tM\) for an integer \(t\ge0\), which is Zumkeller by Lemma 1.

**Density argument.** There are infinitely many distinct primes congruent to \(2\) modulo \(3\). For any fixed \(j\ge0\) and any finite collection of \(K\) such primes, Lemma 2 shows that every sufficiently large integer of valuation \(3j\) which is not divisible by at least one of those primes is represented. Writing \(P\) for their product, the exceptional integers in this stratum are, apart from finitely many, divisible by \(P\), and therefore have upper natural density at most \(1/(2^{3j+1}P)\). Letting \(K\) grow shows that the exceptional set has density zero in each fixed stratum. The full valuation-\(3j\) stratum has density \(2^{-(3j+1)}\), proving the asserted limit. For any fixed \(J\), summing the disjoint strata \(j=0,\ldots,J\) gives the lower bound \(\sum_{j=0}^J2^{-(3j+1)}\). Letting \(J\to\infty\) gives \(\frac12\sum_{j=0}^{\infty}8^{-j}=4/7\).  \(\square\)

## Verification
The independent exact-integer Python program `verify.py` constructs divisor subset sums for small \(2^kp\), evaluates cubic residues modulo \(2^{k+1}p^2\), and verifies that every admissible congruence class has a cubic root for seven selected \((p,k,a)\) instances, including \(a=0,3,6\). All checks passed. These are finite consistency tests; the proof of the infinite assertion is the preceding group-theoretic and density argument.

## Relationship to prior work
Somu, Kukla, and Tran, *Some Results on Zumkeller Numbers*, arXiv:2310.14149v1 (publicly posted 22 October 2023), prove additive results involving two Zumkeller numbers, primes, squares and practical numbers, and explicitly propose studying a Zumkeller number plus a cube in Section 5. Their inspected Sections 2–5 do not state the cubic lower-density theorem. Mahanta, Saikia, and Yaqubi study the family \(2^kp\) and provide the underlying arithmetic classification; this proof does not claim that criterion as new. Related density-one results for prime summands and positive-density results for square summands are not implication-equivalent to cubic summands, whose local power map has a different valuation constraint.

## Limitations
The lower bound \(4/7\) is not claimed to be optimal, and existence of a global natural density is not proved. The argument supplies no uniform threshold across all primes or all \(2\)-adic strata. Published or unindexed work on cubic summands beyond the inspected sources remains an originality risk; searches cannot prove priority. No independent audit has been performed.

## References
1. S. T. Somu, A. Kukla, D. V. K. Tran, *Some Results on Zumkeller Numbers*, arXiv:2310.14149v1 (2023-10-22), https://arxiv.org/html/2310.14149v2 .
2. P. J. Mahanta, M. P. Saikia, D. Yaqubi, *Some properties of Zumkeller numbers and k-layered numbers*, Journal of Number Theory (2020), DOI:10.1016/j.jnt.2020.05.003.

