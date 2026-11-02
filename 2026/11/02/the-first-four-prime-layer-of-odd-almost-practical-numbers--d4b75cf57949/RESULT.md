# The first four-prime layer of odd almost practical numbers

## Finding
A positive integer \(n\) is **almost practical** when every integer \(j\) with \(3\le j\le\sigma(n)-3\) is a sum of distinct positive divisors of \(n\). Let \(\omega(n)\) and \(\Omega(n)\) count distinct primes and prime factors with multiplicity, respectively. Among **odd** integers with \(\omega(n)=4\) and \(\Omega(n)\le5\), no number with \(\Omega(n)=4\) is almost practical. For \(\Omega(n)=5\), the complete set is
\[
\{315p:11\le p\le103,\ p\text{ prime}\}
\cup\{525\cdot11,525\cdot13,735\cdot11,735\cdot13,105\cdot11^2\}.
\]
There are exactly 28 integers in this set, with minimum \(3465\) and maximum \(32445\). The sharp structural statement is that if \(A\) denotes the subset sums of the 12 positive divisors of 315, then for every **positive integer** \(t\), all integers \(3,\ldots,624(t+1)-3\) lie in \(A+tA\) if and only if \(t\le103\). In particular, for every prime \(p>7\), \(315p\) is almost practical if and only if \(p\le103\).

## Assumptions and scope
Write \(\sigma(n)=\sum_{d\mid n}d\). Each positive divisor can be used at most once in a subset sum. If \(A\) is a finite subset of integers, \(A+tA=\{a+tb:a,b\in A\}\). All prime variables below are positive rational primes. This theorem is restricted to odd integers with four distinct prime factors, total prime multiplicity at most five, and does not purport to classify more highly composite exponent layers.

## Proof
**Necessary initial factors.** In the stated domain the integers 3, 5 and 7 lie strictly between 2 and \(\sigma(n)-2\). For an odd integer, the only subset of distinct odd positive divisors summing to 3, 5 or 7, when these values must all be representable, requires the individual divisors 3, 5 and 7: combinations of distinct smaller available odd divisors cannot give these values. Consequently the distinct prime factors are \(3,5,7,p\) for some prime \(p>7\). At total multiplicity four, \(n=105p\). At total multiplicity five, the only shapes are \(315p\), \(525p\), \(735p\), and \(105p^2\).

**Finite two-hole induction.** Suppose the distinct subset sums of some initial divisors are all integers from 0 through their total \(s\), except \(2\) and \(s-2\). If one introduces a new divisor \(d\ge3\), with \(d\le s-2\) and \(d\ne s-4\), then the union of old and \(d\)-translated old subset sums is exactly the interval from 0 through \(s+d\) except \(2\) and \(s+d-2\). Indeed the translated holes \(d+2\) and \(s+d-2\) and the old hole \(s-2\) are filled by the other interval whenever the stated inequalities hold; only the two extreme holes remain. The initial divisors \(1,3,5\), with total 9, meet the induction hypothesis. Thus an ordered divisor list starting \(1,3,5\) for which every later divisor \(d\), preceded by divisor sum \(s\), has \(s-2-d\ge0\) and \(s-2-d\ne2\), proves almost practicality.

**The sharp 315-extension interval lemma.** The proper divisors of 315 are
\[
1,3,5,7,9,15,21,35,45,63,105,
\]
with sum 309. Successive application of the preceding induction shows that their subset sums cover 0 through 309 except 2 and 307. Including the divisor 315 gives the precise set
\[
A=\{0,1\}\cup[3,306]\cup\{308,309,315,316\}\cup[318,621]\cup\{623,624\},
\]
where integer intervals are intended. In particular \(A\) is symmetric about 312 (\(A=624-A\)).

We prove \([3,624(t+1)-3]\subseteq A+tA\) for every integer \(1\le t\le103\). Use the two long subsets \([3,306]\) and \([318,621]\) of \(A\). For every consecutive run \([u,v]\) of at least two integers within \(A\), their translates by \(tb\) as \(b\) ranges through that run cover the **single** interval \([tu+3,tv+621]\), provided \(t\le304\) and \(t(v-u)\ge11\). The first condition bridges successive translates of either long interval; the second bridges the gap between the two families. For \(1\le t\le10\), apply this to the runs \([3,306]\) and \([318,621]\): their resulting intervals overlap since \(12t\le120<619\). For \(11\le t\le103\), apply it instead to the four runs \([3,306]\), \([308,309]\), \([315,316]\), \([318,621]\). Each run satisfies \(t(v-u)\ge11\), and consecutive resulting intervals overlap because the successive gaps in their \(b\)-indices are 2, 6, 2 and \(6t\le618<619\). Thus \([3t+3,621t+621]\subseteq A+tA\) throughout the range.

The initial interval \([3,3t+2]\) is already contained in \(A\) when \(t\le101\). For \(t=102\), the sole additional missing value 307 equals \(205+102\); for \(t=103\), the additional missing values 307, 310, 311 equal \(204+103\), \(207+103\), \(208+103\), respectively. These witnesses all lie in \(A+tA\), since 1 and each displayed first summand belong to \(A\). By the symmetry \(A=624-A\), the whole set \(A+tA\) is symmetric about \(312(t+1)\). The symmetric upper interval is therefore covered as well, completing sufficiency.

For every \(t\ge104\), the integer \(j=309t+622\) is an interior gap of \(A+tA\). If the coefficient \(b\in A\) satisfies \(b\le308\), the required remaining summand \(j-tb\ge t+622>624\); if \(b=309\), that summand is the missing value 622; there is no \(b\in A\) strictly between 309 and 315; if \(b\ge315\), then \(j-tb\le622-6t<0\). Thus \(j\notin A+tA\). This proves the exact cutoff. For any prime \(p>7\), the positive divisors of \(315p\) split as those of 315 and \(p\) times those of 315, so their subset-sum set is \(A+pA\).

**Excluding the squarefree layer.** Let \(C\) be the subset-sum set of divisors of 105. Its total is 192. The proper divisors \(1,3,5,7,15,21,35\) sum to 87, so \(C\) misses every integer from 88 through 104; it also misses 190 (the complement of the impossible sum 2). For every prime \(p\ge11\), the interior integer \(87p+190\) is outside \(C+pC\): if its coefficient \(b\le86\), the remainder exceeds 192; for \(b=87\) the remainder 190 is missing; coefficients 88 through 104 are unavailable; coefficients at least 105 give a negative remainder. Hence no \(105p\) is almost practical.

**The two middle exponent locations.** For \(525p\) or \(735p\) with a prime \(p\ge17\), the required integer 14 cannot be assembled: the available divisors below 15 are exactly \(1,3,5,7\), and none of their distinct subsets sums to 14. Consequently only \(p=11\) or 13 can work. Each of \(5775,6825,8085,9555\) has 24 divisors, beginning \(1,3,5\), and all 21 successive values \(s-2-d\) are nonnegative and different from 2, by exact enumeration in `verify.py`. The two-hole induction establishes almost practicality for all four.

**The squared new prime.** The same value-14 obstruction excludes \(105p^2\) for \(p\ge17\). For \(p=13\), the interior integer \(17389\) is outside \(C+13C+169C\): writing it as \(a+13b+169c\) with \(a,b,c\in C\), any \(c\le86\) makes the remaining sum greater than \(192(1+13)=2688\); \(c\in[88,104]\) is unavailable; \(c\ge105\) is too large; and \(c=87\) would require \(a+13b=2686\), forcing \(b=192\), \(a=190\), again impossible. Finally \(105\cdot11^2=12705\) has 24 divisors beginning \(1,3,5\) and passes all 21 two-hole-induction inequalities (checked exactly in `verify.py`). Thus only \(p=11\) works here.

The 23 primes between 11 and 103 inclusive, the four middle-location cases, and the one squared-new-prime case yield exactly 28 integers. The least is \(315\cdot11=3465\), as claimed.

## Verification
The independent `verify.py` enumerates divisors by integer square root and computes subset-sum reachability by both exact bitsets and a descending Boolean dynamic program. It verifies the nine omitted sums for 315, the exclusion-set premises for 105, every integer shift \(1\le t\le104\) of the sharp interval lemma, all 21 induction inequalities for each of the five exceptional positive integers, and all 28 classified examples. The output is `VERIFY_OK bases=4 base_holes315=9 two_block_t=1..104 boundary=103 positives=28 min=3465 max=32445`. The script checks finite premises and examples; the universal classification follows from the explicit interval and obstruction arguments above.

## Relationship to prior work
Stewart's 1954 paper developed the structural criterion for odd almost practical numbers. Jokar's *On k-layered numbers* (arXiv:2207.09053, first public 2022-07-19), Section 3, restates this criterion and records closure under multiplication of an **already** almost practical odd integer by an existing prime factor. The recently obtained three-prime-support classification determines exactly the almost practical integers \(3^a5^b7^c\) with \(a\ge2\) and \(a+b+c\ge5\), explicitly excluding four-prime support. The present theorem determines the first four-prime exponent layers, including an unbounded prime parameter with a sharp cutoff. The base integer 315 is not almost practical, so Stewart's closure result does not imply its prime-extension threshold.

OEIS A174535 lists individual odd almost practical integers, including many examples enumerated here. Tabulating those values is not the originality claim: the new content is the full \(\Omega(n)=5\), \(\omega(n)=4\) classification and the sharp integer-shift interval lemma. General subset-sum criteria and algorithms decide particular inputs, but the compared statements do not provide the uniform 103 cutoff or eliminate every prime above it.

## Limitations
This is a result for a natural first exponent layer, not a classification for all odd almost practical integers with four prime factors. The supporting 1954 paper was not inspected directly in full; its precise relevant assertions were read in Jokar's accessible later exposition, leaving a residual bibliographic risk that an equivalent consequence was already known. Independent mathematical audit has not been performed.

## References
1. B. M. Stewart, *Sums of Distinct Divisors*, American Journal of Mathematics 76 (1954), 779–785, DOI 10.2307/2372651.
2. F. Jokar, *On k-layered numbers*, arXiv:2207.09053, first version July 19, 2022; especially Section 3, Proposition 3.6, Theorem 3.8, Proposition 3.10.
3. OEIS A174535, *Odd almost practical numbers*.
4. *Three-prime-support classification of odd almost practical numbers*, published mathematical record, 2026, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-three-prime-support-classification-of-odd-almost-practical-numbe--4d74b378e55d.
