# The 140 components of the reciprocal-fourth unitary divisor range

## Finding
For a positive integer \(n\), define the unitary reciprocal-fourth divisor sum
\[
F(n)=\sigma^*_{-4}(n)=\sum_{d\mid n,\,\gcd(d,n/d)=1}d^{-4}
=\prod_{p^a\parallel n}(1+p^{-4a}).
\]
Its value set has **exactly 140 connected components in its closure**, or equivalently **139 bounded gaps**. Every component is a nondegenerate interval with exact endpoints, as follows.

Let \(P=\{2,3,5,7,11,13\}\), let \(K=\prod_{p\in P}(1+p^{-4})\), and set
\[
T=\prod_{p\ge17}(1+p^{-4})=\frac{105}{\pi^4K}.
\]
The attached `INTERVALS.tsv` lists precisely 140 pairs of positive rational numbers \((a,b)\), one on each row. The 140 pairwise disjoint connected components, in increasing order, are exactly
\[
[a,Tb].
\]
The table is defined intrinsically and reproducibly by the six-prime recursion below; it does not use floating-point endpoints.

## Assumptions and scope
All primes are positive rational primes; \(n\) ranges over **all** positive integers, including prime powers and \(n=1\), not merely squarefree integers. The bar denotes closure in the real line. The claim is for the fixed exponent \(-4\), not for all real exponents. Empty prime products equal one. The number \(T\) is strictly greater than one. Every displayed interval is closed; all gaps between consecutive intervals are open and nonempty.

## Proof
**1. The prime tail is an interval.** For primes \(p\ge17\), put \(w_p=\log(1+p^{-4})\). It suffices to show
\[
w_p\le\sum_{q>p}w_q
\]
for every prime \(p\ge17\). By exponentiation, it is enough to establish \(1+p^{-4}\le\prod_{q>p}(1+q^{-4})\). For each of the 456 primes in \([17,3275)\), `verify.py` finds the next ten primes \(q_1,\ldots,q_{10}\) and verifies exactly, by multiplying integer numerators and denominators,
\[
1+p^{-4}<\prod_{j=1}^{10}(1+q_j^{-4}).
\]
Its integer prime sieve certifies that the 462nd and 463rd primes are \(3271\) and \(3299\), so this list covers every prime before the next step applies. For any prime \(p\ge3299\), Sanna's Lemma 2.1, quoting Dusart's consecutive-prime bound from prime index \(463\) onward, gives
\[
p_{j+1}\le p_j\bigl(1+(2\log^2p_j)^{-1}\bigr).
\]
The elementary inequalities \(e<11/4\), \((11/4)^8<3275\), and \(p\ge3299\) imply \(\log p>8\). Thus the two next primes satisfy \(q_1<(11/10)p\) and \(q_2<(11/10)^2p\). Consequently,
\[
q_1^{-4}+q_2^{-4}>p^{-4}\bigl((10/11)^4+(10/11)^8\bigr)>p^{-4},
\]
where the last comparison is an exact rational inequality; hence the product of the next two factors already exceeds \(1+p^{-4}\). The required inequality holds for every prime \(p\ge17\).

Since \(\sum_{p\ge17}w_p<\infty\), the intervals \([0,\sum_{q>p}w_q]\) and \([w_p,w_p+\sum_{q>p}w_q]\) overlap at every stage. The standard elementary greedy/compactness argument for summable binary subsums proves that all sums \(\sum_{p\ge17}\epsilon_pw_p\), \(\epsilon_p\in\{0,1\}\), fill the whole interval \([0,\sum_{p\ge17}w_p]\). Finite subsums are dense therein. Exponentiating, finite squarefree products over primes at least 17 have closure \([1,T]\). Allowing higher prime powers does not enlarge this set, because each corresponding factor lies between one and \(1+p^{-4}\). Thus the **entire** unitary contribution from primes at least 17 has closure exactly \([1,T]\).

**2. Eliminating large exponents of six small primes.** Represent a closed interval \([a,Tb]\), with positive rational \(a\le b\), by the pair \((a,b)\). Begin with the one-pair set \(\mathcal I_0=\{(1,1)\}\). Process successively \(p=13,11,7,5,3,2\) with cutoffs
\[
L_{13}=L_{11}=L_7=L_5=2,\qquad L_3=3,\qquad L_2=4.
\]
For each currently represented interval \((a,b)\), form the candidates
\[
(a,b(1+p^{-4L_p}))\quad\text{and}\quad
(a(1+p^{-4e}),b(1+p^{-4e})),\quad 1\le e<L_p.
\]
Take their represented intervals, sort by increasing left endpoint, and replace each run of overlapping or touching intervals by its union; each merged interval is again encoded as \((a,b)\) with right endpoint \(Tb\). This deterministic prescription defines the entire `INTERVALS.tsv` table.

To justify the first candidate, both omitting \(p\) and taking \(p\) to a power at least \(L_p\) are permitted. Direct rational comparisons show \(1+p^{-4L_p}\le T\) for every listed cutoff. The original interval has multiplicative width \(Tb/a\ge T\). Hence each interval from any exponent \(e\ge L_p\) overlaps the omitted-prime interval; their union is exactly \([a,Tb(1+p^{-4L_p})]\), attained at its far endpoint using exponent \(L_p\). The other candidates represent all remaining exponents \(1\le e<L_p\), so the recursion is exact. The condition \(1+p^{-4(L_p-1)}>T\) is also checked, confirming the cutoff is minimal for this argument.

**3. Certified exact component count.** To compare endpoints \(a\) and \(Tb\) without floating-point ambiguity, use Machin's identity \(\pi=16\arctan(1/5)-4\arctan(1/239)\) and even partial sums through 40 alternating-series terms. These give exact rational bounds \(\pi_-<\pi<\pi_+\) and therefore \(T_-<T<T_+\). For every candidate pair, the code proves either that its left endpoint is at most \(T_-\) times the current right coefficient (certain overlap) or greater than \(T_+\) times that coefficient (certain gap). There are no undecided comparisons.

The certified stage counts (prime, cutoff, candidates, merged components) are
\[
(13,2,2,2),\ (11,2,4,4),\ (7,2,8,8),\ (5,2,16,16),\ (3,3,48,48),\ (2,4,192,140).
\]
At the last stage, 192 candidate bands coalesce into precisely 140 maximal intervals. The same exact rational bounds certify \(Tb<a'\) for every pair of consecutive final intervals \([a,Tb]\), \([a',Tb']\). Therefore there are exactly 140 connected components and exactly 139 bounded complementary gaps. No inference from finite samples of the original integers is used. \(\square\)

## Verification
Run `python3 verify.py` beside `INTERVALS.tsv` using Python 3's standard library. The checker performs 456 integer-product tail tests; certifies the 463rd-prime transition and the rational prime-gap consequence; constructs the Machin rational enclosure; checks all cutoff inequalities; merges all interval candidates with rigorous upper/lower bounds for \(T\); asserts the six stage counts and all 139 strict gaps; and regenerates and byte-compares all 140 rational endpoint rows. Expected terminal verdict: `VERIFY_OK` and `interval_endpoint_table=VERIFIED`. An additional independent floating-point finite-exponent enumeration (exponents up to 12 for each small prime) yielded the same successive counts and final 140 bands; this auxiliary numerical test is not used as an infinite proof.

## Relationship to prior work
Defant, *Ranges of Unitary Divisor Functions* (first public version 2015), defines the unitary range-closure component count and proves the exact **connectedness threshold**. Its Section 3 explicitly proposes studying the number of components for larger exponents, without this 140-component formula or endpoint table. Sanna, *On the Closure of the Image of the Generalized Divisor Function* (2015), gives an exact finite-interval framework for the **ordinary** divisor sum, whose prime-power factors differ, and reproduces the needed Dusart prime-gap bound. Published values for the unitary exponent \(-2\) and a previously recorded \(-3\) classification concern different local factors and do not determine the present 140 intervals. In particular the 52 nontrivial merges at the prime two cannot be inferred from those prior component counts. No stronger published statement covering this exact \(-4\) unitary classification was identified in the inspected sources; this is not a claim of exhaustive literature coverage.

## Limitations
The theorem gives no general formula in a variable real exponent, does not prove monotonicity of the number of components, and does not resolve asymptotic conjectures as the exponent grows. An equivalent earlier unindexed computation or an applicable general classification may exist. The numerical independent cross-check is finite and does not replace the analytic tail proof or the exact rational certificate. Independent external audit has not been performed.

## References
1. Colin Defant, *Ranges of Unitary Divisor Functions*, arXiv:1507.02654, first posted 2015-07-09; see Theorem 1.1 and Section 3.
2. Carlo Sanna, *On the Closure of the Image of the Generalized Divisor Function*, arXiv:1507.08091, first posted 2015-07-29; see Lemma 2.1 and Theorem 1.1.
3. Pierre Dusart, *Autour de la fonction qui compte le nombre de nombres premiers*, thesis (1998), Proposition 1.10, as quoted precisely in Sanna's Lemma 2.1.
