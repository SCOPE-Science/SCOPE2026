# The least integer with a three-way equal-sum unitary-divisor partition

## Finding
A positive integer \(n\) is *unitary three-layered* if its set of positive unitary divisors admits a partition into three classes of equal sums. Then
\[
\boxed{\min\{n\ge1:n\text{ is unitary three-layered}\}=30030=2\cdot3\cdot5\cdot7\cdot11\cdot13.}
\]
Moreover, every unitary three-layered integer has **at least six distinct prime factors**, and six is sharp. The first possible prime-support boundary is unusually close: the largest possible unitary abundancy for at most five distinct prime factors is
\[
\frac{1152}{385}=3-\frac3{385}<3.
\]
The minimum is attained by an exact partition of all \(64\) unitary divisors of \(30030\).

## Assumptions and scope
For \(d\mid n\), call \(d\) *unitary* when \(\gcd(d,n/d)=1\); let \(\mathcal U(n)\) be the set of positive unitary divisors and \(\sigma^*(n)=\sum_{d\in\mathcal U(n)}d\). All three partition classes are disjoint, their union is \(\mathcal U(n)\), and every class has sum \(\sigma^*(n)/3\). The theorem concerns unitary, not ordinary, divisors. Distinct prime factors are counted without multiplicity. The proof works for every positive integer, with no bound on primes or exponents. Empty classes are not relevant because all sums are positive.

## Proof
**Necessary unitary abundancy.** If the unitary divisors of \(n\) split into three equal-sum classes, the class containing \(n\) has sum at least \(n\). Thus \(\sigma^*(n)\ge3n\).

For \(n=\prod_{i=1}^r p_i^{a_i}\), where \(p_1<\cdots<p_r\) are primes and \(a_i\ge1\), the unitary divisors choose either \(1\) or the full prime-power block in each coordinate. Consequently
\[
\frac{\sigma^*(n)}n=\prod_{i=1}^r\left(1+\frac1{p_i^{a_i}}\right).
\]
For \(r\le5\), each \(p_i\) is at least the \(i\)-th smallest prime and each \(p_i^{a_i}\ge p_i\). Therefore, with all omitted factors bounded above by \(1+1/q_i\) and all factors greater than one,
\[
\frac{\sigma^*(n)}n\le
\left(1+\frac12\right)\left(1+\frac13\right)
\left(1+\frac15\right)\left(1+\frac17\right)
\left(1+\frac1{11}\right)=\frac{1152}{385}<3.
\]
The same inequality trivially holds for \(n=1\). Hence \(r\ge6\) for a unitary three-layered integer. The least integer with six distinct prime factors is the product of the six smallest primes, namely \(30030\). This proves the universal lower bound.

**Exact attainment.** Let \(N=30030\). Because \(N\) is squarefree, every ordinary divisor is unitary. In particular, \(|\mathcal U(N)|=2^6=64\), and
\[
\sigma^*(N)=(2+1)(3+1)(5+1)(7+1)(11+1)(13+1)=96768.
\]
Define two explicit disjoint sets of unitary divisors:
\[
A=\{14,210,2002,30030\},\qquad
B=\{455,770,6006,10010,15015\}.
\]
Each displayed integer divides \(N\); the two sets have no common element. Their sums are
\[
14+210+2002+30030=32256
\quad\text{and}\quad
455+770+6006+10010+15015=32256.
\]
Let \(C=\mathcal U(N)\setminus(A\cup B)\). This is a fully specified third set comprising \(55\) unitary divisors. Its sum is \(96768-2\cdot32256=32256\). Hence \(A,B,C\) give the desired equal-sum three-partition, proving attainment and the sharp six-prime support boundary. Combining the lower bound and witness proves the asserted minimum.

## Verification
The accompanying standalone `verify.py` reconstructs \(\mathcal U(30030)\) directly using divisibility and the gcd criterion, checks all \(64\) elements, verifies disjointness, coverage, all three class sizes and sums, independently checks \(\sigma^*(30030)=96768\), and computes the exact rational support bound \(1152/385\). Its output is `VERIFY_OK: unitary_divisors=64; class_sizes=4,5,55; class_sum=32256; support_bound=1152/385; least_integer=30030`. The infinite lower bound is justified symbolically in the proof; the finite checker is a reproducibility aid, not an extrapolation.

## Relationship to prior work
The published notion of a unitary Zumkeller integer uses **two** equal-sum classes of unitary divisors; see OEIS A290466 (2017) and Das (2024). Jokar (2022) and Mahanta, Saikia and Yaqubi (2020) study \(k\)-layered numbers formed from **all ordinary divisors**; the minimum for ordinary three-layered numbers is \(120\). The present theorem applies the familiar number-of-classes parameter to the unitary divisor system and determines its first nontrivial three-class threshold. The ordinary and unitary divisor systems coincide at squarefree \(30030\), but an unrestricted minimum or ordinary-divisor sufficient condition does not imply a unitary minimum. In particular, existing ordinary three-layered examples such as \(120\) have nonunitary proper divisors essential to their partitions. The five-prime unitary abundancy obstruction and the explicit six-prime unitary partition are the distinguishing ingredients.

The inspected 2024 unitary Zumkeller paper treats two-way partitions and half-Zumkeller questions, not three-way classes; the inspected 2020 and 2022 layered-number sources treat ordinary divisors. No covering minimum or six-prime unitary three-way theorem was identified in targeted mathematical-record and literature searches. This does not establish unconditional historical priority.

## Limitations
This theorem determines the least unitary three-layered integer and minimum distinct-prime support; it does not classify all integers having the property, all six-prime solutions, or the least integer for more than three classes. The support bound is a necessary condition, not a general sufficient condition for every six-prime integer. An unindexed equivalent result remains a possible bibliographic overlap. Independent review has not been performed.

## References
- Ivan N. Ianakiev, OEIS A290466, *Unitary Zumkeller numbers* (initial public entry 2017-08-03), https://oeis.org/A290466 .
- Farid Jokar, *On \(k\)-layered numbers* (first public arXiv 2022-07-19), https://arxiv.org/abs/2207.09053 .
- Bhabesh Das, *On unitary Zumkeller numbers*, Notes on Number Theory and Discrete Mathematics 30 (2024), 436–442, https://doi.org/10.7546/nntdm.2024.30.2.436-442 .
- Pankaj Jyoti Mahanta, Manjil P. Saikia and Daniel Yaqubi, *Some properties of Zumkeller numbers and \(k\)-layered numbers* (arXiv 2020-08-07), https://arxiv.org/abs/2008.11096 .
- Jaroslav Krizek, OEIS A204830, *Numbers with three equal ordinary-divisor sums* (2012), https://oeis.org/A204830 .
