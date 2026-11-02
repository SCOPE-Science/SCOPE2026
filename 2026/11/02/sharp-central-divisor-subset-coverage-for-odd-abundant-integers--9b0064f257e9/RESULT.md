# Sharp central divisor-subset coverage for odd abundant integers with three prime factors

## Finding

For a positive integer \(n\), write \(\sigma(n)=\sum_{d\mid n}d\), \(\omega(n)\) for the number of distinct prime factors, and
\[
\mathcal R(n)=\left\{\sum_{d\in E}d:E\subseteq\{d:d\mid n\}\right\}.
\]
Every subset uses each **distinct positive divisor** at most once, including the empty subset.

**Theorem.** For every odd integer \(n>1\) with exactly three distinct prime factors and \(\sigma(n)>2n\),
\[
\boxed{[23,\sigma(n)-23]\cap\mathbb Z\ \subseteq\ \mathcal R(n).}
\]
The constant \(23\) is best possible: the odd abundant integer \(7425=3^3\cdot5^2\cdot11\) has no divisor subset summing to \(22\).

**Corollaries.** Every such \(n\) is semiperfect (some distinct proper positive divisors sum to \(n\)). Moreover, within this class, \(n\) is Zumkeller (its divisors split into two equal-sum classes) **if and only if** \(\sigma(n)\) is even. These assertions hold without any upper bound on \(n\) or on its prime exponents.

## Assumptions and scope

The domain is the full infinite family of odd abundant integers with \(\omega(n)=3\); no squarefree assumption is made. The theorem is a *central interval* result, not an assertion about sums below \(23\) or above \(\sigma(n)-23\). There is no claim for odd abundant integers with four or more distinct prime factors. For each \(n\), every integer in the stated closed interval is represented, not merely the existence of one partition.

## Proof

**Step 1: exactly eight minimal abundance thresholds.** For a prime \(p\) and integer \(a\ge1\), set
\[
I_p(a)=\frac{1+p+\cdots+p^a}{p^a}<\frac{p}{p-1}.
\]
This is strictly increasing in \(a\). If \(n\) is odd, abundant, and has three distinct primes \(p<q<r\), the product bound \(\sigma(n)/n<\prod_{s\in\{p,q,r\}}s/(s-1)\) forces \((p,q)=(3,5)\) and \(r\in\{7,11,13\}\): the respective excluded maximal products are \((5/4)(7/6)(11/10)<2\), \((3/2)(7/6)(11/10)<2\), and \((3/2)(5/4)(17/16)<2\).

Write \(n=3^a5^br^c\), with \(a,b,c\ge1\). Direct rational comparisons produce the following *complete monotone threshold description*:
\[
\begin{array}{c|l}
r&\text{minimal abundant exponent triples }(a,b,c)\\\hline
7&(3,1,1),\ (2,2,1),\ (2,1,2)\\
11&(3,2,1)\\
13&(5,2,1),\ (4,3,1),\ (4,2,2),\ (3,3,2).
\end{array}
\]
Here \(3^a5^br^c\) is abundant **exactly when** its exponent triple dominates at least one indicated triple coordinatewise. For completeness, the exhaustive exclusion reasoning is as follows.

For \(r=7\), \(a=1\) is impossible because \(I_3(1)(5/4)(7/6)=35/18<2\). At \((a,b,c)=(2,1,1)\) the index is \(208/105<2\), while increasing either \(b\) or \(c\) once gives an index above \(2\); increasing \(a\) once does too. For \(r=11\), \(a\le2\) is excluded by \(I_3(2)(5/4)(11/10)=143/72<2\), and \(b=1\) by \((3/2)I_5(1)(11/10)=99/50<2\). The index of \((3,2,1)\) is \(992/495>2\).

For \(r=13\), \(a\le2\) is excluded by \(845/432<2\), and \(b=1\) by \(39/20<2\). At \(a=3\), \(c=1\) is excluded even as \(b\) tends to infinity (upper bound \(700/351<2\)), while \(b=2\) is excluded even as \(c\) tends to infinity (upper bound \(806/405<2\)); the base \((3,3,2)\) is abundant. At \(a=4\), the only lower corner \((4,2,1)\) has index \(52514/26325<2\), whereas both \((4,3,1)\) and \((4,2,2)\) are abundant. At \(a\ge5\), the base \((5,2,1)\) is abundant. All comparisons use the exact formula \(I_p(a)=(p^{a+1}-1)/((p-1)p^a)\); the companion checker repeats them with rational arithmetic.

The eight minimal abundant integers, in ascending order, are
\[
945,1575,2205,7425,78975,131625,342225,570375.
\]
Their abundances \(\sigma(n)-2n\) are respectively \(30,74,36,30,26,1014,1983,1170\), hence at least \(26\).

**Step 2: a general interval-extension lemma.** Let \(N=p^am\), with \(p\) an odd prime, \(a\ge1\), \(p\nmid m\), and \(m\) a product of positive powers of exactly two distinct odd primes. Put \(\Delta(t)=2t-\sigma(t)\). Then for every \(d\mid m\),
\[
\Delta(d)\le\Delta(m).
\tag{1}
\]
Indeed, increasing one prime-power exponent in any integer with at most two distinct odd prime factors changes \(\Delta\) by
\[
\Delta(p^bu)-\Delta(p^{b-1}u)
=p^{b-1}\left(2(p-1)u-p\sigma(u)\right),
\]
where \(u\) is a power of the other odd prime (or \(1\)). This is positive: if \(p=3\), then \(\sigma(u)/u<5/4\); if \(p\ge5\), then \(\sigma(u)/u\le3/2\), and \(2(p-1)-3p/2\ge1/2\). Repeated exponent increases establish (1).

List the divisors of \(m\) as \(r_1<\cdots<r_s=m\), and put \(R_{j-1}=\sum_{i<j}r_i\). Since every proper divisor of \(r_j\) is also a smaller divisor of \(m\), (1) implies
\[
r_j-R_{j-1}\le2r_j-\sigma(r_j)\le2m-\sigma(m).
\tag{2}
\]
Suppose \(\mathcal R(N)\) contains every integer in \([L,\sigma(N)-L]\), for a positive integer \(L\), and \(\sigma(pN)-2pN\ge2L-1\). The new divisors in \(pN\), absent from \(N\), are exactly \(p^{a+1}r_1,\ldots,p^{a+1}r_s\). Add them one at a time in increasing \(r_j\) order. If the current covered interval ends at \(\sigma(N)+p^{a+1}R_{j-1}-L\), the old and shifted intervals touch whenever
\[
p^{a+1}(r_j-R_{j-1})\le\sigma(N)-2L+1.
\]
By (2) it suffices to have \(p^{a+1}(2m-\sigma(m))\le\sigma(N)-2L+1\), which is **equivalent** to \(\sigma(pN)-2pN\ge2L-1\). Consequently,
\[
[L,\sigma(N)-L]\subseteq\mathcal R(N)
\quad\Longrightarrow\quad
[L,\sigma(pN)-L]\subseteq\mathcal R(pN)
\tag{3}
\]
under the stated assumptions. The overlap argument uses integer intervals; the endpoint is inclusive.

**Step 3: eight finite base certificates and infinite propagation.** For each of the eight bases of Step 1, an exhaustive exact subset-sum computation proves
\[
[23,\sigma(n)-23]\subseteq\mathcal R(n).
\tag{4}
\]
The attached standard-library-only verifier computes all divisors from the displayed prime powers and maintains a bitset \(B\) with the invariant that its set bits are precisely the attainable sums. Initially \(B=1\); when adding divisor \(d\), update \(B\leftarrow B\operatorname{OR}(B\ll d)\). This enumerates every possible choice of distinct divisors, so checking a continuous block of bits is a **complete finite proof** for (4), not sampling. A separate Boolean dynamic program cross-checks the two decisive base cases. In all eight bases, the interval check succeeds.

Every other odd abundant integer with three prime factors is obtained from a base by successive multiplications by primes already dividing that base, by Step 1. For such multiplication,
\[
\sigma(pN)=p\sigma(N)+\sigma(m),\qquad
\sigma(pN)-2pN=p\bigl(\sigma(N)-2N\bigr)+\sigma(m).
\]
As the current abundance is at least \(26\), \(p\ge3\), and \(\sigma(m)\ge(1+3)(1+5)=24\), every extension has abundance at least \(102>45=2\cdot23-1\). Thus (3) applies at every multiplication, proving the theorem for the whole infinite family.

**Step 4: optimality and consequences.** The only divisors of \(7425=3^3 5^2 11\) not exceeding \(22\) are \(1,3,5,9,11,15\); their \(64\) subsets do not sum to \(22\). Since \(7425\) is abundant, the uniform endpoint \(23\) cannot be lowered. Finally, for every odd abundant \(N\) in this class, its abundance \(A=\sigma(N)-2N\) is at least \(26\) by Step 1 and the abundance recurrence. Also \(A<N\), since \(\sigma(N)/N<(3/2)(5/4)(7/6)=35/16<3\), and \(A\le\sigma(N)-23\) because \(N\ge945\). Thus \(A\) belongs to the proved central interval and is a sum of distinct **proper** divisors (none can equal \(N\)). The complement of those divisors among all proper divisors sums to \((\sigma(N)-N)-A=N\), establishing semiperfectness. If \(\sigma(N)\) is even, its half lies in the same interval, giving a Zumkeller partition. The converse follows immediately because two equal integer sums require even \(\sigma(N)\). \(\square\)

## Verification

Run `python3 verify.py` using Python 3 with no third-party dependencies. The program independently checks the exact rational threshold inequalities, all eight full finite subset-sum intervals, the missing sum \(22\) for \(7425\), two alternative Boolean dynamic-program certificates, and five larger-exponent tests. Its output is:

`VERIFY_OK primitive_bases=8 maximum_base=570375 sharp_first_missing=22 sharp_base=7425 uniform_interval_start=23 base_divisor_counts=16,18,18,24,36,40,45,48 minimum_abundance=26 independent_boolean_bases=2 extensions=5`

The finite calculations certify precisely the eight base cases and the elementary rational comparisons. The infinitely quantified conclusion follows separately from the proved interval-extension lemma and the threshold classification; the five additional tests are only consistency checks.

## Relationship to prior work

Jokar's 2022 treatment of almost practical numbers recalls Stewart's odd-divisor coverage criterion and shows how almost practicality yields Zumkeller partitions when the divisor sum is even. In particular, almost practical odd integers have third distinct prime \(7\). This does not cover the present odd abundant families with third prime \(11\) or \(13\), including the sharp witness \(7425\), which is not almost practical because \(7\) is missing.

Fang's 2022 work gives extensive *finite bound* searches for odd weird numbers. The theorem here is an *unbounded prime-support structural result*, proves full central subset-sum coverage (stronger than non-weirdness), and has a sharp universal endpoint. The known table of eight odd primitive abundant integers with three distinct prime factors is independently rederived in Step 1, rather than treated as a new discovery. Targeted comparisons found no prior theorem giving the present central interval for all three supports; this is not an absolute priority guarantee.

## Limitations

The result concerns odd abundant integers with exactly three distinct prime factors. It leaves the existence of odd weird numbers with more prime factors open, and makes no assertion that the smaller edge sums \(1\) through \(22\) are uniformly attainable. Bibliographic searches may miss equivalent results, and independent audit has not been performed.

## References

1. F. Jokar, *On \(k\)-layered numbers*, arXiv:2207.09053v1, first posted 19 July 2022, especially §3 on almost practical numbers and Proposition 3.13.
2. W. Fang, *Searching on the boundary of abundance for odd weird numbers*, arXiv:2207.12906v1, first posted 26 July 2022, particularly its opening discussion and §3.
3. OEIS A188342 and A006038, supporting historical tables of odd primitive abundant integers; these tables are not proofs of the new subset-sum interval.
4. P. J. Mahanta, M. P. Saikia, D. Yaqubi, *Some properties of Zumkeller numbers and \(k\)-layered numbers*, Journal of Number Theory 217 (2020), 218–236, DOI:10.1016/j.jnt.2020.05.003 (related background).
