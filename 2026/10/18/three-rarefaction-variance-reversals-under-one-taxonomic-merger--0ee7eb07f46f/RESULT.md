# Three rarefaction-variance reversals under one taxonomic merger first occur at sixteen individuals

## Finding

For every finite species census with a positive-integer abundance multiset \(a=(a_1,\ldots,a_s)\), total \(N\le15\), and every merger of **exactly two distinct taxa** into one taxon by adding their abundance counts, the variance difference
\[
\Delta_a(m)=\operatorname{Var}(R_{\mathrm{merged}}(m))-\operatorname{Var}(R_a(m))
\]
has at most **two strict adjacent sign reversals** as sample size \(m\) ranges over the integers \(2,\ldots,N-1\). Here \(R_a(m)\) is the number of observed taxa in a uniform size-\(m\) subset of the \(N\) individually distinguishable organisms, sampled without replacement.

At \(N=16\), exactly **one** pair consisting of an unordered abundance profile and an unordered pair of its taxa, modulo relabeling, has at least three such reversals. Its original profile is
\[
a=(1,1,1,1,1,1,1,1,2,6),
\]
and merging a singleton with the two-individual taxon yields
\[
b=(1,1,1,1,1,1,1,3,6).
\]
The exact differences at \(m=2,3,\ldots,15\), in that order, are
\[
\left(\frac{43}{3600},\frac{899}{62720},\frac{2017}{254800},-\frac{131}{366912},-\frac{271}{56056},-\frac{3199}{915200},\frac{7}{2860},\frac{573}{57200},\frac{1795}{112112},\frac{26587}{1467648},\frac{3949}{254800},\frac{141}{15680},\frac{1}{900},-\frac{1}{256}\right).
\]
Consequently the sign reversals are at the adjacent sample-size steps \(4\to5\), \(7\to8\), and \(14\to15\). No assertion is made about the maximum possible number of reversals at larger census sizes.

## Assumptions and scope

Every original taxon has strictly positive integral abundance. Every individual is equally eligible for the sample, and each size-\(m\) subset is equiprobable. The two selected taxa are merged **before** categorizing the sampled individuals, preserving all individual identities and the total \(N\). The case \(m=1\) always has zero richness variance, as does the full census \(m=N\); therefore only \(2\le m\le N-1\) is compared. A *strict adjacent reversal* between consecutive sample sizes \(m\) and \(m+1\) means \(\Delta_a(m)\Delta_a(m+1)<0\); a zero difference does not count as a strict reversal. The classification is up to permutations of taxa and interchange of the two merged taxa.

## Proof

For nonnegative integers \(t\), adopt \(\binom{t}{m}=0\) when \(m>t\), and set
\[
q_i(m)=\frac{\binom{N-a_i}{m}}{\binom Nm},\qquad q_{ij}(m)=\frac{\binom{N-a_i-a_j}{m}}{\binom Nm}.
\]
Let \(I_i\) denote the indicator that taxon \(i\) appears at least once in a size-\(m\) sample. Then \(R_a(m)=\sum_i I_i\), \(\mathbb E I_i=1-q_i\), and
\[
\operatorname{Cov}(I_i,I_j)=q_{ij}-q_iq_j.
\]
It follows, exactly and for every admissible \(m\), that
\[
\operatorname{Var}(R_a(m))=\sum_i q_i(1-q_i)+2\sum_{i<j}(q_{ij}-q_iq_j).\tag{1}
\]
This is the classical hypergeometric rarefaction-variance identity, not claimed as new. It computes every difference in the statement using rational arithmetic.

The remaining result is a finite complete classification, reproducible in the two accompanying data and code files. Every positive-integer abundance multiset summing to \(N\) is represented exactly once by a weakly increasing sequence. The recurrence that outputs such sequences chooses its first entry \(x\ge\text{lower}\) and recursively enumerates the remainder \(N-x\) using entries at least \(x\); termination at remainder zero gives a unique representation of every partition. For each partition, the only distinct choices of two taxa up to relabeling are the distinct unordered pairs of entries appearing in that partition. Replacing each such pair \((x,y)\) by \(x+y\), and sorting, enumerates **all** single taxonomic mergers, and none are omitted.

For each resulting comparison, compute its rational differences from (1) for every integer \(m=2,\ldots,N-1\). Then count precisely the adjacent products of consecutive differences that are strictly negative. The exhaustive counts are:

| \(N\) | Abundance multisets | Distinct merger types | Types with at least three strict reversals |
|---:|---:|---:|---:|
| 1–7 | 44 | 62 | 0 |
| 8 | 22 | 47 | 0 |
| 9 | 30 | 73 | 0 |
| 10 | 42 | 114 | 0 |
| 11 | 56 | 170 | 0 |
| 12 | 77 | 253 | 0 |
| 13 | 101 | 365 | 0 |
| 14 | 135 | 525 | 0 |
| 15 | 176 | 738 | 0 |
| 16 | 231 | 1033 | **1** |

The `taxon_merger_census.csv` file records all \(3380\) distinct merger comparisons, their sign strings in increasing sample-size order, and their number of strict adjacent reversals. The unique row with three has the displayed abundance profiles. Every rational difference in that row is generated independently by the standalone verifier. These finite exhaustive calculations, together with the proved coverage of the enumeration and exact moment identity, establish the minimality and uniqueness claims.

## Verification

Run `python verify_taxon_merger_three_reversals.py taxon_merger_census_recreated.csv` using Python 3.9 or later. The program checks the rational formula against a separate integer-coefficient computation of the **full** sample-richness distribution: each taxon of abundance \(a_i\) contributes the generating polynomial \(\sum_{j=0}^{a_i}\binom{a_i}{j}z^j t^{\mathbf1_{j>0}}\), and coefficient multiplication counts samples simultaneously by number of chosen individuals and observed taxa. All original and merged profiles are checked by both methods. Compare the regenerated CSV to the embedded `taxon_merger_census.csv` byte-for-byte. The run produced one and only one three-reversal type, and all moment cross-checks passed.

## Relationship to prior work

Heck, van Belle, and Simberloff (1975) provide the foundational hypergeometric expectation and variance formulas for species richness under rarefaction. Gotelli and Colwell (2001) stress the sensitivity of richness comparisons to sampling depth and taxonomic levels, and discuss crossings of *expected* richness curves. Nipperess and Matsen (2013) generalize rarefaction moments to phylogenetic diversity and recover richness variance as a star-tree case. These sources provide the underlying measurement theory; their accessible material does not give the sharp threshold for **three reversals in the difference of two variance curves constrained to differ by exactly one taxonomic merger**, nor the unique first occurrence. A theorem about crossing expected richness curves does not imply this variance classification: under a merger, the expected richness difference is always nonnegative, while the variance difference here changes sign three times.

## Limitations

This is a sharp finite-census classification only through sixteen individuals, not a bound for larger censuses or for repeated/weighted mergers. It assumes uniform sampling without replacement and perfect identification of the retained taxonomic categories, not population-estimation uncertainty, spatial aggregation, ecological interactions, or uncertainty in species delimitation. Exact enumeration is an exhaustive proof only within its explicitly enumerated finite domain. The result is mathematically exact conditional on these premises, but independent verification of originality against the entire historical literature remains outstanding. The foundational 1975 article was available in publisher abstract but not inspected in full; its direct contribution is the known moment formula.

## References

1. Heck, K. L. Jr., van Belle, G., and Simberloff, D. (1975), *Explicit Calculation of the Rarefaction Diversity Measurement and the Determination of Sufficient Sample Size*, Ecology 56, 1459–1461. https://doi.org/10.2307/1934716
2. Gotelli, N. J., and Colwell, R. K. (2001), *Quantifying biodiversity: procedures and pitfalls in the measurement and comparison of species richness*, Ecology Letters 4, 379–391. https://doi.org/10.1046/j.1461-0248.2001.00230.x
3. Nipperess, D. A., and Matsen, F. A. IV (2013), *The mean and variance of phylogenetic diversity under rarefaction*, Methods in Ecology and Evolution 4, 566–572, first arXiv version 2012-08-31. https://arxiv.org/abs/1208.6552
