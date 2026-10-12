# Fourteen exact components and their densities for the reciprocal-cube divisor-sum range

## Finding

Put \(f(n)=\sigma_{-3}(n)=\sum_{d\mid n}d^{-3}\) for every positive integer \(n\), and define
\[
T=\zeta(3)\prod_{p\in\{2,3,5,7\}}(1-p^{-3}).
\]
The closure of \(f(\mathbb N)\) is the disjoint union of **exactly fourteen** closed intervals \(I_j=[a_j,b_jT]\). For each \(j\), the natural density of positive integers \(n\) with \(f(n)\in I_j\) exists and equals the rational number \(\delta_j\) in the table. All endpoints are exact; the right column lists the coefficient \(b_j\), not the product \(b_jT\).

| \(j\) | \(a_j\) | \(b_j\) | \(\delta_j\) |
| ---: | ---: | ---: | ---: |
| 1 | \(1\) | \(1\) | \(8/35\) |
| 2 | \(344/343\) | \(343/342\) | \(4/105\) |
| 3 | \(126/125\) | \(125/124\) | \(2/35\) |
| 4 | \(6192/6125\) | \(42875/42408\) | \(1/105\) |
| 5 | \(28/27\) | \(1029/988\) | \(2/15\) |
| 6 | \(392/375\) | \(128625/122512\) | \(1/30\) |
| 7 | \(9/8\) | \(9/8\) | \(4/35\) |
| 8 | \(387/343\) | \(343/304\) | \(2/105\) |
| 9 | \(567/500\) | \(1125/992\) | \(1/35\) |
| 10 | \(6966/6125\) | \(42875/37696\) | \(1/210\) |
| 11 | \(73/64\) | \(196/171\) | \(2/15\) |
| 12 | \(4599/4000\) | \(6125/5301\) | \(1/30\) |
| 13 | \(7/6\) | \(9261/7904\) | \(1/15\) |
| 14 | \(147/125\) | \(18375/15314\) | \(1/10\) |

In particular, the last right endpoint equals \(\zeta(3)\), and \(\sum_{j=1}^{14}\delta_j=1\).

## Assumptions and scope

All prime powers and all positive integers are permitted. Here \(\zeta(3)=\sum_{m\ge1}m^{-3}\). The closure is taken in the usual real topology, and natural density means \(\lim_{X\to\infty}X^{-1}\#\{n\le X:f(n)\in I_j\}\). Finite prime-support valuations below are ordinary \(p\)-adic valuations, not restrictions on the theorem. No assertion concerns arbitrary real exponents other than the fixed exponent \(-3\).

## Proof

**1. An interval from primes above seven.** Write \(F_p(a)=\sum_{h=0}^a p^{-3h}\) and \(F_p(\infty)=(1-p^{-3})^{-1}\). For every prime \(q\ge11\) we claim
\[
\prod_{p>q}(1-p^{-3})^{-1}\ge F_q(\infty).
\]
Indeed, because the product is at least \(1+\sum_{p>q}p^{-3}\), it suffices that \(\sum_{p>q}p^{-3}>1/(q^3-1)\). For \(q=11,13,17,19,23\), respectively, it suffices to use the later-prime sets \(\{13,17,19\}\), \(\{17,19,23,29\}\), \(\{19,23,29\}\), \(\{23,29,31\}\), and \(\{29,31,37\}\); each strict rational comparison is asserted in the accompanying verifier. For every prime \(q\ge29\), Nagura's theorem gives three successive larger primes \(r_i<(6/5)^iq\), \(1\le i\le3\). Thus
\[
\sum_{p>q}p^{-3}>q^{-3}\sum_{i=1}^3(5/6)^{3i}
=q^{-3}\frac{11160125}{10077696}>\frac1{q^3-1}.
\]
The last inequality holds already for \(q=29\) and hence for larger \(q\). The exact greedy interval lemma in Sanna (2015, Lemma 2.3) now applies: successively choose exponents at primes at least \(11\), taking the largest factor not exceeding a target and using the remaining Euler-product domination to eliminate a positive residual gap. Consequently
\[
\overline{\{f(m):\gcd(m,210)=1\}}=[1,T].
\]
This is an infinite statement; the few prime checks above only establish the starting inequalities for Nagura's tail theorem.

**2. Four exponent partitions.** For \((p,k)=(2,2),(3,1),(5,1),(7,1)\), exact inequalities give
\[
\frac{F_p(k+1)}{F_p(k)}<T<\frac{F_p(k)}{F_p(k-1)}.
\]
Hence the intervals \(F_p(a)[1,T]\) with \(a\ge k\) overlap successively and fill, in closure, \([F_p(k),TF_p(\infty)]\). For the four small primes form states \(a=0,\ldots,k-1\) (fixed exponent) and \(a\ge k\) (high exponent). Each combined state is an interval
\[
\left[\prod_{p\le7}L_p,\ T\prod_{p\le7}U_p\right],
\]
where \((L_p,U_p)=(F_p(a),F_p(a))\) for a fixed state and \((F_p(k),F_p(\infty))\) for a high state. Multidimensional intervals are connected because changing one high exponent at a time yields overlapping subintervals. Conversely every integer has exactly one of these states, and the tail factor lies in \([1,T]\). Consequently the range closure is exactly the union of \(3\cdot2\cdot2\cdot2=24\) candidate closed intervals.

**3. Exact finite union certificate.** Let \(B=\prod_{p\in\{2,3,5,7\}}(1-p^{-3})\), \(S=\sum_{m=1}^{100}m^{-3}\). Integral-test tails imply strict rational bounds
\[
B\left(S+\frac1{2\cdot101^2}\right)<T<B\left(S+\frac1{2\cdot100^2}\right).
\]
The standard-library verifier `verify_components.py` generates all 24 rational interval pairs, orders their left endpoints, and compares successive endpoints against these two rational bounds. Every overlap and gap comparison is strict and resolved by these enclosures; merging gives exactly the fourteen rows of the table, separated by thirteen strictly positive gaps. The smallest gap is certified to exceed \(10^{-3}\). This is an exhaustive rational comparison of 24 symbolic intervals, not finite sampling of integers.

**4. Density of each component.** For each prime, the proportion of integers with \(v_p(n)=a\) is \((p-1)/p^{a+1}\), and the proportion with \(v_p(n)\ge k\) is \(p^{-k}\). The four valuations are asymptotically independent by the Chinese remainder theorem. A state therefore has the product of these four rational probabilities. The fourteen component states form the disjoint groups determined in step 3; summing the state weights yields the listed \(\delta_j\). Their sum is one. Every integer in a state maps to its designated component, while every component contains the full corresponding interval in the closure by steps 1–2. This proves the component counts, endpoints, and densities. \(\square\)

## Verification

Run `python3 verify_components.py` with Python 3 standard library. The script checks the five finite prime-tail inequalities, the four high-exponent cutoff inequalities, an exact rational enclosure of \(T\), all twenty-four state intervals, the fourteen exact merged endpoints, the fourteen rational density weights, and the total mass. A successful run ends with `CERTIFICATE_OK ordinary_sigma_minus_three components=14 candidates=24 tail_threshold=11 rational_density_total=1`. The code is a finite certificate for the arithmetic comparisons; the infinite tail and natural-density deductions are proved mathematically above.

## Relationship to prior work

Defant (arXiv:1506.05432v1, publicly available 2015-06-17) established the connectedness transition for generalized divisor ranges, not the present component count. Sanna (arXiv:1507.08091v1, 2015-07-29) proved that every fixed exponent above one admits a finite interval decomposition and rational component densities; Sanna supplied the explicit case \(r=2\), with three components, and a plot near \(r=3\), but did not state the fourteen exact intervals and weights here. Achenjang and Berger (arXiv:1808.07550, Remark 5.5) noted that Sanna's plot suggests \(C_3\ge14\); that is only a lower bound, not this matching upper bound or exact endpoint/density classification. Zubrilina (arXiv:1711.02871) studied general bounds and prime obstructions. The ordinary divisor function here differs from the unitary-divisor function and the alternating-divisor function.

## Limitations

The finding is a complete exact fixed-parameter calculation, not a formula for all real exponents. It relies on the established Nagura prime-gap theorem and Sanna's greedy interval argument; the standalone code verifies only finite rational consequences. Prior literature may contain unindexed exact calculations not detected by targeted searches.

## References

1. C. Defant, *On the Density of Ranges of Generalized Divisor Functions*, arXiv:1506.05432v1 (2015). https://arxiv.org/abs/1506.05432
2. C. Sanna, *On the closure of the image of the generalized divisor function*, arXiv:1507.08091v1 (2015), especially Theorem 1.1, Lemma 2.3 and the example at exponent two. https://arxiv.org/abs/1507.08091
3. A. Achenjang and B. Berger, arXiv:1808.07550 (2018), Remark 5.5. https://arxiv.org/abs/1808.07550
4. M. Zubrilina, arXiv:1711.02871 (2017). https://arxiv.org/abs/1711.02871
5. J. Nagura, *On the interval containing at least one prime number*, Proceedings of the Japan Academy 28 (1952), 177–181.
