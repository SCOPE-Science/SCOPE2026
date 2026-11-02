# The first strict improvement on the consecutive-sum prefix benchmark occurs at 24

## Finding

For a nonempty strictly increasing sequence \(a=(a_1,\ldots,a_t)\) of integers in \([1,N]\), let \(S(a)\) be its set of sums \(a_i+\cdots+a_j\) over all \(1\le i\le j\le t\). Write \(M(N)=\max_a |S(a)|\) and \(T_N=(1,2,\ldots,N)\). Then, among all positive integers \(N\), the smallest for which \(M(N)>|S(T_N)|\) is **\(N=24\)**. At that first crossing, \(M(24)=188\) while \(|S(T_{24})|=186\), and the **unique maximizing sequence** is

\[
(1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24).
\]

Moreover, \(M(N)=|S(T_N)|\) for every \(1\le N\le23\). No assertion is made about larger \(N\).

## Assumptions and scope

All summands are distinct positive integers in increasing order, with no prescribed sequence length. Only nonempty sequences and nonempty consecutive intervals are counted. Two intervals with equal integer sum contribute a single element to \(S(a)\). The result is a finite theorem for \(1\le N\le24\), not an asymptotic assertion.

## Proof

**Reduction to an exhaustive finite certificate.** Every admissible sequence is uniquely represented by one nonzero \(N\)-bit mask \(m\): the integer \(i\in[1,N]\) appears precisely when bit \(i-1\) of \(m\) is set. Conversely, every such mask describes an admissible increasing sequence. Thus all \(2^N-1\) candidates are covered without duplication.

For the increasing sequence selected by a mask, form its prefix sums \(p_0=0\) and \(p_j=\sum_{i=1}^{j}a_i\). The consecutive sums are **exactly** the positive differences \(p_j-p_i\) for \(0\le i<j\le t\). Hence their cardinality is obtained with exact integer comparisons by marking each positive difference once. Every difference lies between \(1\) and \(N(N+1)/2\), so a finite array indexed over this range is sufficient, with no collision of unrelated values.

The attached source file `verify_interval.cpp` implements this exhaustive procedure for every \(N=1,\ldots,24\), enumerating masks \(m=1,\ldots,2^N-1\). Its `seen` array stores the *current mask* as a stamp: a difference is counted if and only if `seen[difference] != mask`. Because masks are nonzero and unique during each fixed \(N\), and the array is freshly initialized for each \(N\), the stamping rule is equivalent to clearing the Boolean array for every candidate. No approximation, randomized search, pruning, or skipped candidate occurs. The code records the global maximum, number of maximizing masks, the full-mask value, and a maximizing mask. It asserts the exact computed maxima for all \(N\le24\), equality with the full-mask value for all \(N<24\), and at \(N=24\) asserts maximum \(188\), full-mask value \(186\), exactly one maximizing mask, and maximizing mask \(2^{24}-1-2^{10}\), which omits precisely \(11\). These assertions all passed on execution. This establishes the claimed threshold, both exact values, and uniqueness for the complete finite domain.

The number of examined masks across all lengths is \(\sum_{N=1}^{24}(2^N-1)=33,554,406\). At the critical \(N=24\), all \(16,777,215\) candidates were examined. Since every admissible sequence corresponds to one of those masks, the finite census constitutes an exhaustive proof, rather than a sample of the search space.

## Verification

Compile with `g++ -O3 -std=c++17 verify_interval.cpp -o verify_interval` and execute `./verify_interval`. A successful replay ends with `VERIFY_OK masks=33554406 first_strict_improvement_n=24 maximum=188 full=186 unique_omitted=11`. The verifier additionally performs selected independent difference-count comparisons against a separately implemented Boolean-array routine for \(N\le17\). Those supplementary comparisons are safeguards, not substitutes for the exhaustive mask enumeration. This proof is conditional on the transparent integer implementation's correct execution; full external validation is not claimed.

The exact sequence of maxima for \(N=1,\ldots,24\) is
\[
1,3,5,9,12,16,21,27,33,40,47,55,63,70,77,89,101,110,123,134,146,159,171,188.
\]

## Relationship to prior work

Beker's investigation of Erdős and Graham's consecutive-sum problem identifies the full increasing sequence as a natural but asymptotically suboptimal benchmark, and establishes nontrivial extremal asymptotic bounds. The present finite result determines the **first exact crossover**, before which the benchmark is optimal, and classifies all maximizers at the crossover. It does not sharpen Beker's asymptotic constants or resolve a new asymptotic question.

## Limitations

Only the exact threshold and the first crossover extremizers are determined; behavior for \(N>24\) is not classified. The gain at the first crossing is only two distinct sums, and its mathematical interest is the *sharp first loss of optimality of the canonical benchmark*, not the size of this gain. Other unpublished computational tables could conceivably contain the same cutoff. This work has not undergone independent mathematical review.

## References

1. Adrian Beker, *On a problem of Erdős and Graham about consecutive sums in strictly increasing sequences*, first public version 16 November 2023, arXiv:2311.10087v1; *Bulletin of the London Mathematical Society* **56** (2024), 2749–2759, DOI: 10.1112/blms.13098. Primary MSC: 11B13.
2. Paul Erdős and Ronald L. Graham, *Old and New Problems and Results in Combinatorial Number Theory* (1980), the source of the motivating consecutive-sum problem.
