# The least five-layered factorial is \(14!\)

## Finding

Among positive integers \(m\), the smallest index for which the positive divisors of \(m!\) can be partitioned into five equal-sum groups is exactly \(m=14\). Equivalently,
\[\min\{m\ge1:m!\text{ is five-layered}\}=14.\]

## Assumptions and scope

The factorial, its full set of **positive** divisors, the conventional divisor-sum function \(\sigma\), and five **disjoint nonempty** groups are intended. No assertion is made about the five-layeredness of \(m!\) for \(m>14\).

## Proof

Let \(D(N)\) be the set of all positive divisors of the positive integer \(N\), and write \(\sigma(N)=\sum_{d\in D(N)}d\). A five-layered integer admits a partition of \(D(N)\) into five nonempty disjoint subsets, each of sum \(\sigma(N)/5\).

**Exclusion of earlier factorials.** If \(N\) is five-layered, the unique group containing the divisor \(N\) has sum at least \(N\), so \(\sigma(N)\ge5N\). For every divisor \(u\mid v\), the product \(\sigma(u)/u=\prod_p(1+p^{-1}+\cdots+p^{-a_p})\), with absent prime factors omitted, is no greater than \(\sigma(v)/v\), since every factor is monotone in the exponent. Therefore, as \(m!\mid13!\) for \(1\le m\le13\), we have \(\sigma(m!)/(m!)\le\sigma(13!)/(13!)\). Factorization gives
\[13!=2^{10}3^55^2\cdot7\cdot11\cdot13=6\,227\,020\,800,\qquad \sigma(13!)=31\,044\,179\,712<5(13!)=31\,135\,104\,000.\]
Thus none of the thirteen earlier factorials is five-layered.

**Construction at the boundary.** We have
\[14!=2^{11}3^55^27^2\cdot11\cdot13=87\,178\,291\,200,\qquad \sigma(14!)=442\,487\,616\,480,\]
so the required common group sum is
\[T=\sigma(14!)/5=88\,497\,523\,296.\]
Here are four subsets of \(D(14!)\), each displayed as a complete list of its decimal integer elements. All entries are distinct across the four lists.


\(A_1\) (5 elements):

```text
87178291200, 1245404160, 73382400, 443520, 2016
```
\(A_2\) (7 elements):

```text
43589145600, 29059430400, 14529715200, 1210809600, 107627520, 793800, 1176
```
\(A_3\) (10 elements):

```text
21794572800, 17435658240, 12454041600, 10897286400, 9686476800, 8717829120, 7264857600, 242161920, 4633200, 5616
```
\(A_4\) (27 elements):

```text
7925299200, 6706022400, 6227020800, 5811886080, 5448643200, 4843238400, 4358914560, 4151347200, 3962649600, 3632428800, 3487131648, 3353011200, 3228825600, 3113510400, 2905943040, 2724321600, 2641766400, 2490808320, 2421619200, 2235340800, 2179457280, 2075673600, 1981324800, 581188608, 10108800, 41600, 160
```


Direct integer addition gives \(\sum_{d\in A_i}d=T\) for each \(1\le i\le4\), and every listed integer divides \(14!\). Put \(A_5=D(14!)\setminus(A_1\cup A_2\cup A_3\cup A_4)\). Then \(A_1,\ldots,A_5\) are pairwise disjoint and cover all positive divisors. Since \(\tau(14!)=2592\), the complement has \(2592-(5+7+10+27)=2543>0\) elements, and its sum equals
\[\sigma(14!)-4T=T.\]
Consequently, \(14!\) is five-layered, and its index \(14\) is minimal. \(\square\)


## Verification

The standalone accompanying `verify.py` independently enumerates all divisors of \(13!\) and \(14!\) by trial division up to their integer square roots. It separately computes \(\sigma\) from prime-factor Euler products, checks the exact values above, validates membership and disjointness of all \(49\) displayed divisors, checks each group's sum against \(T\), and explicitly calculates the remaining fifth group. The exhaustive finite arithmetic certificate establishes the boundary case; the monotone abundancy argument proves exclusion of **all** lower factorials without requiring a finite search over every possible partition.

Run using `python3 verify.py` with Python 3's standard library. The output begins `VERIFIED` only after every assertion succeeds.

## Relationship to prior work

Jokar's 2022 study proves the factorial three-layer and four-layer classifications (Theorems 5.15 and 5.18) and explicitly conjectures a general sufficient criterion for practical integers to be \(k\)-layered (Conjecture 5.23). The displayed five-layered factorial certificate is a different, subsequent natural boundary case, outside the numerical range up to \(10^10\) of that paper's Remark 5.22. Mahanta, Saikia, and Yaqubi (2020) investigate general \(k\)-layered constructions, but their accessible conditions do not state this factorial threshold. A five-divisibility criterion for \(\sigma\), by itself, gives a necessary condition rather than the partition required here.

## Limitations

The claim is a least-index theorem, **not** a classification of all five-layered factorials and not a proof of the general practical-number conjecture. The lists are an exact finite witness; the lower-bound argument covers \(1\le m\le13\). Literature searches cannot exclude independent, unindexed equivalent proofs.

## References

1. F. Jokar, *On \(k\)-layered numbers*, arXiv:2207.09053, first posted 19 July 2022. https://arxiv.org/abs/2207.09053
2. P. J. Mahanta, M. P. Saikia and D. Yaqubi, *Some properties of Zumkeller numbers and \(k\)-layered numbers*, Journal of Number Theory **217** (2020), 218–236. https://doi.org/10.1016/j.jnt.2020.05.003
