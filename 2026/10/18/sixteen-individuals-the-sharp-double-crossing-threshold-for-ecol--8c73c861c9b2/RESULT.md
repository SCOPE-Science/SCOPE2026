# Sixteen individuals: the sharp double-crossing threshold for ecological rarefaction

## Finding

Consider two ecological assemblages, each comprising the same total number \(N\) of individuals, grouped into species of positive integer abundances. For each integer sample size \(1\le k\le N\), select \(k\) individuals uniformly without replacement and let \(R_\lambda(k)\) be the expected number of distinct species under abundance partition \(\lambda\). A **double ranking reversal** means that for some integers \(2\le k_1<k_2<k_3\le N\), the three nonzero differences \(R_\lambda(k_i)-R_\mu(k_i)\) have signs \(+,-,+\) or \(-,+,-\).

**Sharp threshold and complete boundary classification.** No pair of abundance partitions of a common census of at most \(15\) individuals exhibits a double ranking reversal. At \(N=16\) there are exactly two unordered abundance-partition pairs exhibiting this behavior:

\[
\{(8,2,2,2,2),(7,5,1,1,1,1)\},\qquad
\{(8,2,2,2,2),(6,6,1,1,1,1)\}.
\]

For the first pair, the six-species assemblage has greater expected richness at sample sizes \(k=2,3\), less at \(4\le k\le10\), and greater again at \(11\le k\le16\). For the second pair, the six-species assemblage leads at \(2\le k\le4\), trails at \(5\le k\le10\), and leads at \(11\le k\le16\). The curves tie at \(k=1\) in both cases.

## Assumptions and scope

An assemblage has exactly \(N\) individuals, divided into \(s\) nonempty species with integer counts \(\lambda=(\lambda_1,\ldots,\lambda_s)\), where \(\lambda_1\ge\cdots\ge\lambda_s\ge1\) and \(\sum_i\lambda_i=N\). Species labels are irrelevant: only the multiset of abundances matters. Two assemblages have the **same** census size \(N\), but their numbers of species may differ. Samples are uniformly random size-\(k\) subsets without replacement, and the two expected-richness values are compared at the same integer \(k\). A strict sign reversal is counted after any zero differences are discarded.

The result does not concern independent draws with replacement, sampling-area effects, confidence intervals, or smooth interpolations between integer sample sizes.

## Proof

**Exact rarefaction formula.** A species with \(a\) individuals is absent from a uniformly sampled \(k\)-subset with probability \(\binom{N-a}{k}/\binom{N}{k}\). Here \(\binom{m}{k}=0\) whenever \(k>m\). By linearity of expectation,

\[
R_\lambda(k)=s-\frac{\sum_{a\in\lambda}\binom{N-a}{k}}{\binom{N}{k}}
\quad(1\le k\le N).
\]

Set \(F_\lambda(k)=\binom{N}{k}R_\lambda(k)\), an integer. Since \(\binom{N}{k}>0\), the sign of any expected-richness difference equals the sign of \(F_\lambda(k)-F_\mu(k)\). Specifically,

\[
F_\lambda(k)=|\lambda|\binom{N}{k}
-\sum_{a\in\lambda}\binom{N-a}{k}.
\]

**Completeness of the finite certificate.** A nonincreasing positive abundance sequence summing to \(N\) is exactly an integer partition of \(N\). All such partitions are generated once by recursively choosing their largest part \(j\), and then enumerating partitions of \(N-j\) with every part at most \(j\). Exhaustion over unordered pairs of these partitions therefore covers all possible pairs of assemblages, up to species relabeling. The accompanying standalone checker performs the comparison using exact integer \(F\)-profiles at every integer \(k\); its exhaustive loop covers all \(1\le N\le16\) and every unordered pair. It also independently constructs the same partition sets via multiplicity histograms, preventing a missing-class artifact in the primary generator.

The partition counts for \(N=1,2,\ldots,16\) are
\[
1,2,3,5,7,11,15,22,30,42,56,77,101,135,176,231.
\]
All unordered pairs at each \(N\le15\) have fewer than two strict ranking reversals. At \(N=16\), all \(\binom{231}{2}=26{,}565\) unordered pairs are checked, and exactly the two stated pairs have two reversals. This is a complete finite proof because the recursion enumerates the full mathematical domain and the sign calculations are exact, rather than sampled.

**Independent witness verification.** Write \(B=(8,2,2,2,2)\), \(A_1=(7,5,1,1,1,1)\), and \(A_2=(6,6,1,1,1,1)\). The integer numerators \(F_{A_i}(k)-F_B(k)\), in order \(k=1,\ldots,16\), are respectively

\[
(0,1,3,-22,-168,-518,-930,-1031,-628,-11,363,364,196,64,12,1)
\]

and

\[
(0,2,12,14,-84,-392,-804,-947,-592,-2,364,364,196,64,12,1).
\]

Each displayed entry is computed from the exact hypergeometric formula. A separate independent check in the program explicitly iterates all \(2^{16}\) labeled subsets of each boundary assemblage and obtains the same expected-richness numerator at every sample size. This verifies both constructions without reusing the hypergeometric formula.

The universal claim follows from the exhaustive enumeration; the two displayed numerator vectors prove sharpness and the stated phases.

## Verification

Run `python3 check_rarefaction.py` from a directory containing the supplied standalone script. It needs only the Python standard library and uses integer arithmetic throughout. It prints partition and pair counts for each \(N\), confirms that the double-reversal count is zero below \(16\) and exactly two at \(16\), independently checks partition generation by abundance histograms, and compares the formula against direct enumeration of all \(65{,}536\) labeled subsets for each boundary profile. The verified run completed with `PASS`.

## Relationship to prior work

Heck, van Belle, and Simberloff (1975) developed the hypergeometric expected-richness calculation underlying individual-based rarefaction. Lande, DeVries, and Walla (2000) studied ranking changes in expected species-accumulation curves under a population-frequency sampling model and analyzed a Simpson-diversity criterion for crossing. Gotelli and Colwell (2001) explicitly observed that individual-based rarefaction curves may cross twice and described the ecological pitfalls of comparing communities at only one standardized sample size. Chao and collaborators (2014) broadened rarefaction and extrapolation methods in a Hill-number framework.

The **existence** of multiple crossings is therefore not asserted as new. The result here is the exact smallest *integer equal-census size* allowing two strict observed-sample-size ranking reversals **under hypergeometric sampling**, and a complete enumeration of the two boundary abundance-profile pairs. The cited analyses do not state or imply either finite sharp boundary as presented here. A broader or differently indexed enumeration could still contain the same fact; this bibliographic possibility remains open.

## Limitations

The threshold is exact for integer sample sizes and equal finite census totals. It is not a universal lower bound for analytical interpolation between sizes, continuous-time species detection, independent-with-replacement sampling, unequal census totals, or incidence-based quadrat sampling. The two boundary profiles are mathematical assemblages rather than empirical case studies. The result quantifies a minimal combinatorial obstruction to sample-size-invariant ranking; it does not measure the frequency of double crossings in natural communities, establish ecological significance of a particular species count, or replace uncertainty intervals in real biodiversity comparisons. Originality is based on source comparisons and search, not proof of absence from all literature.

## References

1. Heck, K. L., Jr., van Belle, G., and Simberloff, D. (1975), *Explicit Calculation of the Rarefaction Diversity Measurement and the Determination of Sufficient Sample Size*, **Ecology** 56, 1459–1461. DOI: `10.2307/1934716` (online date verified 1975-10-01).
2. Lande, R., DeVries, P. J., and Walla, T. R. (2000), *When Species Accumulation Curves Intersect: Implications for Ranking Diversity Using Small Samples*, **Oikos** 89, 601–605. DOI: `10.1034/j.1600-0706.2000.890320.x`.
3. Gotelli, N. J., and Colwell, R. K. (2001), *Quantifying Biodiversity: Procedures and Pitfalls in the Measurement and Comparison of Species Richness*, **Ecology Letters** 4, 379–391. DOI: `10.1046/j.1461-0248.2001.00230.x`.
4. Chao, A., Gotelli, N. J., Hsieh, T. C., Sander, E. L., Ma, K. H., Colwell, R. K., and Ellison, A. M. (2014), *Rarefaction and Extrapolation with Hill Numbers*, **Ecological Monographs** 84, 45–67. DOI: `10.1890/13-0133.1`.
