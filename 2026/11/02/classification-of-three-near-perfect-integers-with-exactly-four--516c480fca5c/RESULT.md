# Classification of three-near-perfect integers with exactly four prime factors

## Finding

Write \(\omega(n)\) for the number of distinct prime divisors of \(n\), and \(\Omega(n)\) for the number counted with multiplicity. A positive integer is **three-near-perfect** (with exactly three omissions) if there exist three distinct positive divisors \(d_1,d_2,d_3\) such that
\[
\sigma(n)=2n+d_1+d_2+d_3.
\]
Among the integers with \(\omega(n)=3\) and \(\Omega(n)=4\), precisely the following \(25\) satisfy this equation:
\[
 n\in \{60,84,90,132,140,156,220,234,260,308,342,350,364,490,532,550,572,666,726,740,748,820,1148,1316,1484\}.
\]
The complete, unordered omitted-divisor triples are as follows; in total there are \(32\) triples. Every divisor appearing is proper.

| \(n\) | Factorization | \(\sigma(n)-2n\) | All unordered omitted-divisor triples |
|---:|:---|---:|:---|
| 60 | \(2^2\cdot 3\cdot 5\) | 48 | \(\{3,15,30\}\); \(\{6,12,30\}\) |
| 84 | \(2^2\cdot 3\cdot 7\) | 56 | \(\{2,12,42\}\); \(\{7,21,28\}\) |
| 90 | \(2\cdot 3^2\cdot 5\) | 54 | \(\{3,6,45\}\); \(\{6,18,30\}\); \(\{9,15,30\}\) |
| 132 | \(2^2\cdot 3\cdot 11\) | 72 | \(\{2,4,66\}\); \(\{6,22,44\}\) |
| 140 | \(2^2\cdot 5\cdot 7\) | 56 | \(\{1,20,35\}\); \(\{7,14,35\}\) |
| 156 | \(2^2\cdot 3\cdot 13\) | 80 | \(\{2,26,52\}\) |
| 220 | \(2^2\cdot 5\cdot 11\) | 64 | \(\{4,5,55\}\) |
| 234 | \(2\cdot 3^2\cdot 13\) | 78 | \(\{13,26,39\}\) |
| 260 | \(2^2\cdot 5\cdot 13\) | 68 | \(\{1,2,65\}\) |
| 308 | \(2^2\cdot 7\cdot 11\) | 56 | \(\{1,11,44\}\) |
| 342 | \(2\cdot 3^2\cdot 19\) | 96 | \(\{1,38,57\}\) |
| 350 | \(2\cdot 5^2\cdot 7\) | 44 | \(\{2,7,35\}\); \(\{5,14,25\}\) |
| 364 | \(2^2\cdot 7\cdot 13\) | 56 | \(\{2,26,28\}\) |
| 490 | \(2\cdot 5\cdot 7^2\) | 46 | \(\{1,10,35\}\) |
| 532 | \(2^2\cdot 7\cdot 19\) | 56 | \(\{4,14,38\}\) |
| 550 | \(2\cdot 5^2\cdot 11\) | 16 | \(\{1,5,10\}\) |
| 572 | \(2^2\cdot 11\cdot 13\) | 32 | \(\{2,4,26\}\) |
| 666 | \(2\cdot 3^2\cdot 37\) | 150 | \(\{2,37,111\}\) |
| 726 | \(2\cdot 3\cdot 11^2\) | 144 | \(\{1,22,121\}\) |
| 740 | \(2^2\cdot 5\cdot 37\) | 116 | \(\{5,37,74\}\) |
| 748 | \(2^2\cdot 11\cdot 17\) | 16 | \(\{1,4,11\}\) |
| 820 | \(2^2\cdot 5\cdot 41\) | 124 | \(\{1,41,82\}\) |
| 1148 | \(2^2\cdot 7\cdot 41\) | 56 | \(\{1,14,41\}\) |
| 1316 | \(2^2\cdot 7\cdot 47\) | 56 | \(\{2,7,47\}\) |
| 1484 | \(2^2\cdot 7\cdot 53\) | 56 | \(\{1,2,53\}\) |

## Assumptions and scope

All integers are positive. The primes \(p<q\) below are distinct odd primes. A solution has exactly three **distinct** omissions, with no assumption that the omitted triples are unique. The classification is for every integer with \(\omega(n)=3\) and \(\Omega(n)=4\); it is **not** a classification of all three-near-perfect integers.

Because each such integer has a prime exponent pattern \((2,1,1)\), its even forms are precisely \(4pq\), \(2p^2q\), and \(2pq^2\). The cases with the squared odd prime not equal to the smaller odd prime are included in the last form \(2pq^2\). There are no odd solutions.

## Proof

**1. Odd exclusion and properness.** Suppose \(n\) is odd, with prime support at least \(3,5,7\) and exactly one exponent equal to two. By monotonicity of \(\sigma(\ell^e)/\ell^e\) in the prime \(\ell\), and by assigning the square to the smallest prime to maximize the product,
\[
\frac{\sigma(n)}n\le\frac{13}9\frac65\frac87=\frac{624}{315}<2.
\]
Thus its divisor-sum surplus is nonpositive. For the three possible even exponent patterns, the corresponding maximal ratios of \(\sigma(n)/n\) occur at \(p=3,q=5\) and are, respectively,
\[
\frac74\frac43\frac65=\frac{14}5\quad\text{for }4pq,
\qquad
\frac32\frac{13}9\frac65=\frac{13}5\text{ for }2p^2q,
\qquad
\frac32\frac43\frac{31}{25}=\frac{62}{25}\text{ for }2pq^2.
\]
In each case the ratio is less than \(3\), so \(\sigma(n)-2n<n\). Therefore any omitted divisor in a solution is necessarily proper: omitting \(n\) itself would already exceed the total surplus.

**2. The shape \(4pq\).** Multiplicativity gives
\[
\Delta:=\sigma(4pq)-8pq=(7-p)q+7p+7=56-(p-7)(q-7).
\]
Every sum of three distinct positive divisors is at least \(1+2+4=7\). If \(p\ge11\), then \((p-7)(q-7)\le49\), leaving only \((p,q)=(11,13),(11,17),(11,19)\); for \(p\ge13\), the smallest possible product is at least \(6\cdot10=60\). For \(p\in\{3,5,7\}\), split a possible omitted triple into terms not divisible by \(q\) and those divisible by \(q\). The former contribute \(B\), the latter \(Cq\). Since \(4pq\) itself is excluded, the non-\(q\) divisors are \(\{1,2,4,p,2p,4p\}\). The three largest have sums \(22,35,49\), respectively, for \(p=3,5,7\). Thus
\[
(C-(7-p))q=7p+7-B\ge \begin{cases}6,&p=3,\\7,&p=5,\\7,&p=7.\end{cases}
\]
In particular \(C-(7-p)\ge1\), hence \(q\le7p+7\). Thus \(q\le28,42,56\) respectively. There are exactly \(32\) candidate prime pairs for this shape after combining these ranges with \(p=11\).

**3. The shape \(2p^2q\).** Here
\[
\Delta=(3+3p-p^2)q+3(p^2+p+1).
\]
If \(p\ge7\), the coefficient of \(q\) is negative and \(q\ge p+2\), so
\[
\Delta\le-p^3+4p^2+12p+9<0
\]
(the last inequality holds for all \(p\ge7\)). If \(p=5\), then \(\Delta=93-7q\), and a sum of three distinct divisors is at least \(1+2+5=8\), so only \(q\in\{7,11\}\) survive. If \(p=3\), then \(\Delta=3q+39\). The divisors not divisible by \(q\) are \(\{1,2,3,6,9,18\}\); their three largest sum to \(33\). Writing the omitted sum as \(Cq+B\) therefore gives
\[
(C-3)q=39-B\ge6,
\]
so \(C\ge4\) and \(q\le39\). This leaves \(12\) candidate prime pairs.

**4. The shape \(2pq^2\).** In this case
\[
\Delta=(3-p)q^2+3(p+1)(q+1).
\]
For \(p\ge7\), we have \((p-3)/(p+1)\ge1/2\) and \(q\ge11\), while \(q^2>6(q+1)\), hence \(\Delta<0\). For \(p=5\), the expression is \(-2q^2+18(q+1)\), which is negative when \(q\ge11\); only \(q=7\) remains. For \(p=3\), \(\Delta=12(q+1)\). If \(q\ge13\), then \(q^2>12(q+1)=\Delta\), so an omitted divisor cannot be divisible by \(q^2\). The possible remaining divisors are
\[
1,2,3,6,q,2q,3q,6q.
\]
The three largest are \(6q,3q,2q\), summing to \(11q<12(q+1)\). Thus \(q\in\{5,7,11\}\). This leaves \(4\) candidate prime pairs in all.

**5. Exhaustive final comparison.** The previous arguments prove that every possible solution is among \(32+12+4=48\) explicitly finite prime pairs. For every pair, build the full divisor set using
\[
D(\ell^e)=\{1,\ell,\ldots,\ell^e\},\quad D(n)=\prod_{\ell^e\parallel n}D(\ell^e),
\]
then compute \(\Delta=\sum_{d\mid n}d-2n\) and test **every** three-element subset of \(D(n)\setminus\{n\}\) for sum \(\Delta\). Each tested integer has exactly \(12\) positive divisors, so this is a direct finite exact comparison of \(\binom{11}3=165\) triples per candidate. The complete enumeration, reproduced by the standalone source in the verification section, yields precisely the table above: \(17\) successes of shape \(4pq\), \(6\) of shape \(2p^2q\), and \(2\) of shape \(2pq^2\), with a total of \(32\) unordered triples. This finishes the exhaustive proof.

## Verification

Run `python3 near3_verify.py` with Python's standard library. It uses exact integer divisor generation, naive exact primality for the bounded candidate primes, and all three-element combinations of the proper divisor set; it independently cross-checks each closed-form surplus formula against the computed divisor sum. The expected output begins:

```
VERIFY_OK cases=48 by_shape=32,12,4 solutions=25 by_shape=17,6,2 witnesses=32
```

The script outputs every integer and its complete witness triples. The finite checker certifies the last step; the infinite exhaustiveness depends on the algebraic bounds in steps 1–4, not a search horizon.

## Relationship to prior work

Aryan–Madhavani–Parikh–Slattery–Zelinsky (arXiv:2310.01305, first public 2023-10-02), *On 2-Near Perfect Numbers*, introduces the general omitted-divisor viewpoint and classifies a two-prime-support slice for **two** omissions. Fearon–Foushee–Porosoff–Skula–Zelinsky–Zhang (arXiv:2508.06651, first public 2025-08-08), *Complete characterization of 2-near perfect numbers with exactly 2 prime factors*, explicitly studies three omissions in its Section 6.3, provides eight initial examples, and observes that multiple omitted-divisor triples complicate classifications. Neither inspected article contains a full classification for **three** omissions with three-prime support and four prime factors counted with multiplicity.

A previous classification of **two** omissions at these same prime-factor counts supplies neither a complete three-omission list nor all omitted triples; numerical overlap is not implication. The related exact-three-**deficient**-perfect equation has the opposite sign and is likewise not covering. Some individual values, in particular \(60\), were previously tabulated; the contribution is the universal prime bounds, exhaustive classification and all witness triples, not identification of \(60\) as an example.

## Limitations

The theorem is restricted to \(\omega(n)=3\), \(\Omega(n)=4\) and exactly three distinct omissions. It makes no claim about higher prime multiplicity or full three-near-perfect enumeration. Finite numerical enumeration by itself would not establish the infinite theorem, but the proof derives explicit global prime bounds before any finite checking. Bibliographic searches cannot exclude an unindexed equivalent theorem, and an independent audit has not been performed.

## References

1. Vedant Aryan, Dev Madhavani, Savan Parikh, Ingrid Slattery, Joshua Zelinsky, *On 2-Near Perfect Numbers*, arXiv:2310.01305, first posted 2023-10-02, https://arxiv.org/abs/2310.01305.
2. Richard Fearon, Henry Foushee, Benjamin Porosoff, Alexander Skula, Joshua Zelinsky, Kyle Zhang, *Complete characterization of 2-near perfect numbers with exactly 2 prime factors*, arXiv:2508.06651, first posted 2025-08-08, Section 6.3, https://arxiv.org/abs/2508.06651.
3. Paul Pollack and Vladimir Shevelev, *On perfect and near-perfect numbers*, Journal of Number Theory 132 (2012), 3037–3046, https://arxiv.org/abs/1011.6160.
4. OEIS A341475, sequence of two-near-perfect integers (an adjacent but distinct property), https://oeis.org/A341475.
