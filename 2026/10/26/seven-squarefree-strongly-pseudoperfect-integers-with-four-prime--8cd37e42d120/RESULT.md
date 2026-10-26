# Seven squarefree strongly pseudoperfect integers with four prime factors

## Finding
A positive integer \(n\) is *strongly pseudoperfect* if some set \(S\) of divisors of \(n\) is closed under \(d\mapsto n/d\) and satisfies \(\sum_{d\in S}d=2n\).

**Theorem.** For every squarefree positive integer \(n\) with exactly four distinct prime factors, \(n\) is strongly pseudoperfect if and only if
\[
 n\in\{210,330,546,714,1770,3198,3486\}.
\]
For each of these seven integers, the complementary-pair-closed divisor set \(S\) satisfying the equation is **unique**. In every case \(1,n\in S\). The omitted complementary divisor pairs are exactly:

| \(n\) | Omitted pairs \((d,n/d)\) |
|---|---|
| 210 | (5,42), (6,35), (7,30), (10,21) |
| 330 | (2,165), (15,22) |
| 546 | (6,91), (13,42), (14,39), (21,26) |
| 714 | (3,238), (17,42) |
| 1770 | (3,590), (10,177) |
| 3198 | (6,533), (39,82) |
| 3486 | (6,581), (7,498) |

## Assumptions and scope
The classification concerns **all** squarefree integers with precisely four distinct prime factors, with no bound on the integer or on its largest prime factor. All divisors and subset sums are over positive integers. An omitted pair is an unordered pair \(\{d,n/d\}\); there are eight such pairs when \(n\) is squarefree with four prime factors. No assertion is made about integers with repeated prime factors or more than four prime factors.

## Proof
**1. Complementary-pair equation.** Write \(\sigma(n)=\sum_{d\mid n}d\). Since \(n\) is squarefree with four prime factors, it is not a square and its sixteen divisors split into eight disjoint complementary pairs. A divisor set \(S\) as in the definition exists precisely when some selection of the eight pairs, regarded as omitted, has total sum
\[
\Delta(n)=\sigma(n)-2n.
\]
In particular \(\sigma(n)\ge2n\) is necessary.

**2. Prime-support reduction.** Write the distinct prime factors in ascending order. If \(n\) is odd, then
\[
\frac{\sigma(n)}n\le\frac43\frac65\frac87\frac{12}{11}<2,
\]
so \(n\) is even. Write \(n=2abc\), where \(3\le a<b<c\) are odd primes. If \(a\ge11\), then
\[
\frac{\sigma(n)}n\le\frac32\frac{12}{11}\frac{14}{13}\frac{18}{17}<2.
\]
If \(a=7\), then \(b\ge13\) also makes \(\sigma(n)<2n\); for \(b=11\), the abundance inequality forces \(c\le72/5\), hence \(c=13\). For \(n=2\cdot7\cdot11\cdot13=2002\), one has \(\Delta(n)=28\); every complementary-pair sum is at least \(2\sqrt{2002}>28\), so this integer fails. If \(a=5\), the abundance inequality for \(n=2\cdot5\cdot b\cdot c\) yields, whenever \(b>9\),
\[
c\le\frac{9(b+1)}{b-9}.
\]
Consequently \(b\in\{7,11,13,17\}\); \(b\ge19\) forces \(c<b\), impossible.

If \(a=3\), put \(n=6bc\). Direct multiplication gives \(\Delta(n)=12(b+c+1)\). Four complementary pairs have respective sums
\[
b+6c,\quad2b+3c,\quad3b+2c,\quad6b+c,
\]
whose total is \(12(b+c)<\Delta(n)\). Therefore an omitted pair must be among \(\{1,6bc\}\), \(\{2,3bc\}\), \(\{3,2bc\}\), \(\{6,bc\}\). The smallest such sum is \(bc+6\). Hence
\[
bc+6\le12(b+c+1),\qquad(b-12)(c-12)\le150.
\]
For \(b\ge23\), the next possible prime \(c\) is at least \(29\), violating this inequality. Thus \(b\in\{5,7,11,13,17,19\}\).

**3. Exact finite reduction.** Every remaining candidate is of the form \(n=mc\), with \(c\) prime and larger than the prime factors of the squarefree three-prime core \(m\). The ten possible cores are
\[
m\in\{6b:b=5,7,11,13,17,19\}\cup\{10b:b=7,11,13,17\}.
\]
Let \(D(m)\) denote the eight positive divisors of \(m\). Each complementary pair of divisors of \(mc\) is uniquely \(\{d,(m/d)c\}\) for \(d\in D(m)\). For any omitted index set \(I\subseteq D(m)\), write
\[
A_I=\sum_{d\in I}\frac md,\qquad B_I=\sum_{d\in I}d.
\]
The omitted-sum equation becomes
\[
(A_I-\sigma(m)+2m)c=\sigma(m)-B_I.\tag{1}
\]
The exhaustive eight-bit enumeration of all \(256\) sets \(I\), for each of the ten listed cores, verifies that there is **no** set with both \(A_I=\sigma(m)-2m\) and \(B_I=\sigma(m)\). Thus equation (1) gives at most one possible \(c\) per set, namely
\[
c=\frac{\sigma(m)-B_I}{A_I-\sigma(m)+2m}.
\]
Retaining only integer primes \(c\) exceeding the largest prime of \(m\) gives the complete table:

| Core | Eligible final prime \(c\) |
|---|---|
| \(6\cdot5\) | 7, 11, 59 |
| \(6\cdot7\) | 13, 17, 83 |
| \(6\cdot11\) | none |
| \(6\cdot13\) | 41 |
| \(6\cdot17\) | none |
| \(6\cdot19\) | none |
| \(10\cdot7\), \(10\cdot11\), \(10\cdot13\), \(10\cdot17\) | none |

Every retained integer has exactly one qualifying omitted index set; the corresponding omitted pairs appear in the Finding table. The exact eight-bit proof certificate in `verify.py` implements equation (1) directly in integer arithmetic, checks the identity-denominator branch, exhausts all \(256\) possibilities for every core, and independently enumerates all eight complementary pairs for each of the seven retained integers. This completes both implications and uniqueness. \(\square\)

## Verification
Execute `python3 verify.py` from the directory containing this result. It requires Python 3 only and prints `VERIFY_OK count=7 unique_omission_masks=7 core_masks=256 per case brute_limit=5000`. The checker also independently enumerates **all** squarefree four-prime integers through \(5000\) and compares their divisor-pair subset sums. The finite census is a cross-check only; completeness for arbitrarily large primes follows from the support reduction and equation (1), not from that census.

## Relationship to prior work
Wang and Zelinsky (2026), *Strongly Pseudoperfect Numbers*, introduce constructions, restrictions, and examples; their Table 2 lists \(210\) and \(330\) individually, but does not state this complete unrestricted four-prime squarefree classification or uniqueness of all seven representations. The published indexed classification for \(\Omega(n)\le3\) addresses an earlier multiplicity layer and does not imply the present \(\Omega(n)=4\), squarefree classification. The OEIS sequence A334405 tabulates small examples, but a finite table does not establish the present infinite-scope exclusion. The seven-number result is an exact natural first squarefree support layer beyond the three-factor obstruction.

## Limitations
The proof uses a small exact finite arithmetic certificate to close the ten residual cores; the full enumeration is reproducible in `verify.py`. This is a self-review and has not undergone independent audit. An unindexed equivalent classification or stronger general theorem could affect priority. No conclusion is drawn about prime-support layers beyond four or about arbitrary multiples of these integers.

## References
1. Audrey Wang and Joshua Zelinsky, *Strongly Pseudoperfect Numbers*, arXiv:2609.36068, first posted 2026-09-28; relevant definitions, Theorems 5–6, Section 4, and Table 2 (2026 version). https://arxiv.org/pdf/2609.36068
2. Tim McCormack and Joshua Zelinsky, *Weighted Versions of the Arithmetic-Mean-Geometric Mean Inequality and Zaremba's Function*, arXiv:2312.11661. https://arxiv.org/abs/2312.11661
3. OEIS A334405, *Strongly pseudoperfect numbers* (database of initial terms). https://oeis.org/A334405
4. *Strongly pseudoperfect integers with \(\Omega(n)\le3\)*, indexed published mathematics record, 2026. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-strongly-pseudoperfect-integers-with-omega-n-le3--e44b0bb26fb1
