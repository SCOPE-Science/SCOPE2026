# Eight individuals are the sharp boundary for two peaks in expected singleton counts

## Finding

Consider a finite community with species abundances \(\mathbf a=(a_1,\ldots,a_s)\) of positive integers and total \(N=\sum_i a_i\). For each \(m\in\{1,\ldots,N\}\), select uniformly one \(m\)-element subset of the \(N\) distinguishable individuals, without replacement. Let \(f_1(m)\) count the species represented by **exactly one** selected individual, and write \(F_{\mathbf a}(m)=\mathbb E[f_1(m)]\). A strict interior peak is an integer \(2\le m\le N-1\) for which \(F_{\mathbf a}(m-1)<F_{\mathbf a}(m)>F_{\mathbf a}(m+1)\).

**Sharp boundary and complete first layer.** Every positive-integer abundance multiset with \(N\le7\) has at most one strict interior peak. For \(N=8\), exactly one abundance multiset, up to permutation of species, has two: \(\mathbf a=(5,2,1)\), with peaks at \(m=2\) and \(m=6\). Its exact sequence is

\[
\bigl(F_{(5,2,1)}(m)\bigr)_{m=1}^{8}
=\left(1,\frac{17}{14},\frac{33}{28},\frac87,\frac{65}{56},\frac{33}{28},\frac98,1\right).
\]

Two structural contrasts hold for **every** finite census, without a size bound: if each species has the same abundance, the expected singleton curve is unimodal (allowing equal adjacent values); if every species has abundance one or two, the curve is a concave quadratic in sample size (or an affine function if no species has abundance two). These restrictions show why heterogeneity in abundance is needed for the observed double peak.

## Assumptions and scope

Individuals are individually distinguishable, their species labels and total abundances are fixed, and every size-\(m\) subset has probability \(1/\binom Nm\). There is no replacement, species-detection error, environmental heterogeneity, or population growth during sampling. The term *singleton* refers to a species appearing once **in the sample**, not necessarily a species having census abundance one. A peak must be strict and interior; the endpoints \(m=1,N\) are not counted. Communities are identified up to permutation of species, so positive integer partitions enumerate the different abundance configurations.

## Proof

For a species with population abundance \(a\), the number of size-\(m\) samples containing exactly one individual of that species is \(a\binom{N-a}{m-1}\). The exact expectation therefore is

\[
F_{\mathbf a}(m)=\frac{1}{\binom Nm}
\sum_{i=1}^{s}a_i\binom{N-a_i}{m-1},
\qquad 1\le m\le N,
\]

where a binomial coefficient is zero when the lower index is outside its usual range. This identity is classical elementary hypergeometric counting and is **not** claimed as a new formula.

For the finite minimality and uniqueness assertions, enumerate the complete set of nonincreasing positive-integer partitions of each \(N\in\{1,\ldots,8\}\). The recursive exhaustive rule appends any next part from \(1\) through the smaller of the previous part and the remaining total; the empty remainder terminates a partition. Every partition has a unique first part and remaining nonincreasing tail, so the recursive procedure is exhaustive and free of duplicates, by induction on its remaining total.

For each partition, evaluate the displayed expectation as an exact rational number at every sample size. A strict peak is detected using only exact integer cross-products or rational comparisons. The complete table `census.csv` contains **all 66** profiles, their full rational sequences, and all strict peak positions. The census tallies are:

| \(N\) | Partitions | No strict peaks | One strict peak | Two strict peaks |
|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 | 0 |
| 2 | 2 | 2 | 0 | 0 |
| 3 | 3 | 2 | 1 | 0 |
| 4 | 5 | 4 | 1 | 0 |
| 5 | 7 | 5 | 2 | 0 |
| 6 | 11 | 6 | 5 | 0 |
| 7 | 15 | 7 | 8 | 0 |
| 8 | 22 | 12 | 9 | 1 |

The unique two-peak line is the multiset \((5,2,1)\). For the first peak, \(17/14>1\) and \(17/14>33/28\). For the second, \(33/28=66/56>65/56\) and \(33/28=66/56>9/8=63/56\). This proves strictness, the bound, and uniqueness at the first possible census size.

For the two structural contrasts, first suppose each of the \(s\) species has abundance \(a\), with \(N=sa\). On the positive portion of the curve, the exact ratio is

\[
\frac{F(m+1)}{F(m)}
=\frac{(m+1)(N-a-m+1)}{m(N-m)}.
\]

Its comparison with one has numerator difference \(N-a+1-am\), which decreases strictly with \(m\). Hence positive consecutive changes can switch from increasing to decreasing only once; a terminal zero portion cannot create another peak. For \(a=1\) the curve is simply \(F(m)=m\). Now suppose the population has \(r\) species of abundance two and \(t\) species of abundance one, so \(N=2r+t\ge2\). Direct substitution gives

\[
F(m)=\frac{t m}{N}+\frac{2r\,m(N-m)}{N(N-1)}.
\]

This is concave in \(m\), strictly so when \(r>0\), proving the second contrast. The cases with just one individual are immediate.

## Verification

Run `python3 verify_singleton_peaks.py --verify-certificate census.csv` using Python 3.9 or later, without external packages. The checker constructs the integer partitions recursively **and independently** reconstructs their set by considering all choices of cuts in compositions of each \(N\). It computes singleton expectations both from the hypergeometric expression and from direct enumeration of all nonempty labeled-individual subsets, checking equality at every \(m\) for every partition. It then verifies the full rational certificate byte-for-byte, the eight census tallies, the unique abundance profile, and the exact witness values. An additional check compares finite equal-abundance profiles against the adjacent-ratio formula. These finite checks are an exhaustive proof of the bounded census claim because partition completeness and exact counting are established; the equal-abundance and one-or-two-abundance conclusions have independent symbolic proofs above.

## Relationship to prior work

Singleton counts are familiar ecological frequency-of-frequency statistics. Coddington et al. (2009) report their sensitivity to undersampling and examine empirical and simulated abundance profiles, rather than a sharp finite census for two strict maxima of their expectation. Colwell et al. (2012) define species frequency counts and compare rarefaction/extrapolation models; they explicitly distinguish the finite-population hypergeometric mechanism from a multinomial approximation, but do not give this eight-individual classification. Chao and Jost (2012) derive coverage-based sampling and use rare-frequency information for richness inference, not the strict peak structure here.

Comparison with a separate theorem on **differences between two singleton-expectation curves after abundance balancing** is important: a single-sign-switch statement for such differences does not imply that one fixed curve has at most one interior maximum. Conversely, the present finite peak classification does not constrain pairwise sign changes across profiles. The hypergeometric identity itself and its ecological motivation are established background; the claimed contribution is the smallest and uniquely classified double-peak profile plus the stated structural contrasts.

## Limitations

The exhaustive classification ends at \(N=8\); no bound on the number of peaks in larger communities is asserted. Only strict interior peaks count. The result makes no direct claim about the variance of singleton counts, their observed stochastic trajectories, asymptotic estimator accuracy, independent sampling with replacement, or species-detection imperfections. Its biological relevance is a mathematical warning against assuming a single smooth peak in the **expected absolute number** of sampled singletons, not an empirical assertion that such a profile commonly occurs in natural assemblages. Independent bibliographic validation has not been performed, and equivalent statements in the broader occupancy and urn literature remain a risk.

## References

- Coddington, J. A., Agnarsson, I., Miller, J. A., Kuntner, M., and Hormiga, G. (2009), *Undersampling bias: the null hypothesis for singleton species in tropical arthropod surveys*. Journal of Animal Ecology 78, 573–584. DOI: `10.1111/j.1365-2656.2009.01525.x` (first publicly dated March 31, 2009).
- Colwell, R. K., Chao, A., Gotelli, N. J., Lin, S.-Y., Mao, C. X., Chazdon, R. L., and Longino, J. T. (2012), *Models and estimators linking individual-based and sample-based rarefaction, extrapolation and comparison of assemblages*. Journal of Plant Ecology 5, 3–21. DOI: `10.1093/jpe/rtr044`. Author-hosted text: https://www.robertkcolwell.org/publications/6855.pdf .
- Chao, A., and Jost, L. (2012), *Coverage-based rarefaction and extrapolation: standardizing samples by completeness rather than size*. Ecology 93, 2533–2547. DOI: `10.1890/11-1952.1`.
