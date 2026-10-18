# A sharp five-individual reversal of richness–Rao covariance under ultrametric rarefaction

## Finding

Let a finite population of \(N\) labeled individuals be assigned to species, and let \(d_{ij}=d_{ji}\geq0\), with \(d_{ii}=0\), be fixed species dissimilarities. Draw a uniformly random subset of \(m\) individuals without replacement, where \(2\leq m\leq N\). Write \(X_i\) for the sampled count of species \(i\), and define sampled species richness and pairwise Rao diversity by
\[
K_m=\sum_i \mathbf 1_{\{X_i>0\}},\qquad
Q_m=\binom m2^{-1}\sum_{i<j} d_{ij} X_i X_j.
\]

**Sharp first failure.** For every \(N\leq4\), every positive integer abundance profile and every symmetric nonnegative dissimilarity array, \(\operatorname{Cov}(K_m,Q_m)\geq0\). At \(N=5\), strict negative covariance occurs even when \(d\) is the leaf-distance metric of a rooted ultrametric tree with positive branch lengths. A witness has four species with abundances \((2,1,1,1)\), with distance \(H=3\) from the duplicated species to each singleton and distance \(\ell=1\) between any two singleton species. Its covariances at sample sizes \(m=2,3,4,5\) are exactly
\[
\left(\frac{21}{100},\frac{3}{100},-\frac1{25},0\right).
\]

**Exact arbitrary-distance near-census criterion.** For any integer \(r\geq2\), consider one species \(A\) with two individuals and \(r\) singleton species \(B_1,\ldots,B_r\). Put \(N=r+2\), sample \(m=N-1\), and write
\[
U=\sum_{i=1}^{r}d(A,B_i),\qquad
V=\sum_{1\leq i<j\leq r}d(B_i,B_j).
\]
Then
\[
\boxed{\operatorname{Cov}(K_{N-1},Q_{N-1})
=\frac{4\bigl(2V-(r-2)U\bigr)}{(r+2)^2r(r+1)}.}
\]
For \(r\geq3\), if \(\overline d_{\mathrm{out}}=U/r\) and \(\overline d_{\mathrm{in}}=2V/[r(r-1)]\), this covariance is negative **exactly when**
\[
\overline d_{\mathrm{out}}>\frac{r-1}{r-2}\,\overline d_{\mathrm{in}}.
\]

**Instability arbitrarily close to an ultrametric star.** Suppose \(0<\ell<H\), all distances from \(A\) to \(B_i\) equal \(H\), and all distances between different \(B_i\) equal \(\ell\). These distances are realized by a rooted ultrametric tree having a positive outgroup edge of length \(H/2\), a singleton-cluster basal edge of length \((H-\ell)/2\), and positive singleton pendant edges of length \(\ell/2\). In this family,
\[
\boxed{\operatorname{Cov}(K_{N-1},Q_{N-1})
=\frac{4\bigl((r-1)\ell-(r-2)H\bigr)}{(r+2)^2(r+1)}.}
\]
For \(r\geq3\), it is strictly negative if and only if \(H/\ell>(r-1)/(r-2)\). For **every** fixed \(H/\ell>1\), however close to one, some sufficiently large \(r\) satisfies this condition. At \(m=2\), the same population always has strictly positive covariance, so an increase in sample size changes its covariance sign. The negative case is robust under sufficiently small ultrametric-preserving refinements of the clustered tips into strictly binary trees.

## Assumptions and scope

The population is fixed; individual labels distinguish organisms of the same species. The sampling law is simple random sampling without replacement of exactly \(m\) individuals. Species are correctly identified and dissimilarities do not depend on sampling. The general exact criterion permits any symmetric nonnegative off-diagonal dissimilarities; the ultrametric corollary assumes positive phylogenetic leaf distances. We do not assert a sign law for every population with \(N\geq5\).

Here \(Q_m\) is the mean dissimilarity of unordered pairs of **distinct sampled individuals**. The conventional empirical with-replacement Rao quadratic entropy is \(Q_m^{\mathrm{Rao}}=\frac{m-1}{m}Q_m\) when within-species distances vanish; therefore \(\operatorname{Cov}(K_m,Q_m^{\mathrm{Rao}})\) has the **same sign** at each fixed \(m\). This multiplicative normalization must not be omitted when quoting numerical covariance values.

## Proof

**1. Universal four-individual lower boundary.** If \(m=N\), then \(K_m\) is constant. If \(m=2\), then \(K_m\) takes the values one and two, with \(Q_m=0\) whenever \(K_m=1\) and \(Q_m\geq0\) whenever \(K_m=2\). Hence the covariance is nonnegative. The remaining nontrivial case for \(N\leq4\) is \(N=4,m=3\). With at most two species, whenever richness varies it takes values one and two and pairwise diversity vanishes at richness one. With four singleton species, richness is constant. The only other species-abundance multiset is \((2,1,1)\). Name the doubleton species \(A\), and the singletons \(B,C\). Omitting one individual from \(A\) gives \(K=3\) and \(Q=[d(A,B)+d(A,C)+d(B,C)]/3\). Omitting \(B\) or \(C\) gives \(K=2\); its conditional mean pairwise diversity is \([d(A,B)+d(A,C)]/3\). Each richness value occurs with probability one half. Thus
\[
\operatorname{Cov}(K_3,Q_3)=\frac{d(B,C)}{12}\geq0.
\]
This covers every abundance profile, every \(m\), and every \(N\leq4\). No metric triangle inequality was needed.

**2. Exact near-census formula.** In the one-doubleton community, drawing \(m=N-1=r+1\) individuals is equivalent to omitting a uniformly random labeled individual. The event that an \(A\) individual is omitted has probability \(2/(r+2)\), richness \(r+1\), and conditional pairwise diversity
\[
Q_A=\frac{U+V}{\binom{r+1}{2}}.
\]
The event that a singleton \(B_j\) is omitted has total probability \(r/(r+2)\), richness \(r\), and the conditional diversity for the particular omitted species is
\[
Q_{B_j}=\frac{2\sum_{i\neq j}d(A,B_i)+
\sum_{i<k:\,i,k\neq j}d(B_i,B_k)}{\binom{r+1}{2}}.
\]
Averaging over \(j\) counts each outgroup–singleton distance exactly \(r-1\) times, each with coefficient two, and each singleton–singleton distance exactly \(r-2\) times. Therefore
\[
\overline Q_B=
\frac{2(r-1)U+(r-2)V}{r\binom{r+1}{2}},
\quad Q_A-\overline Q_B=
\frac{2V-(r-2)U}{r\binom{r+1}{2}}.
\]
For a two-level richness variable with levels differing by one, the covariance with any other variable equals the product of the two level probabilities times the difference of conditional means. Thus
\[
\operatorname{Cov}(K_{N-1},Q_{N-1})=
\frac{2r}{(r+2)^2}(Q_A-\overline Q_B),
\]
which simplifies to the claimed formula because \(\binom{r+1}{2}=r(r+1)/2\). This argument is exact for every integer \(r\geq2\) and every fixed symmetric dissimilarity array.

**3. Ultrametric specialization and sharpness.** Substituting \(U=rH\) and \(V=\binom r2\ell\) yields the displayed ultrametric formula. For \(r\geq3\), all denominators and \(\ell\) are positive, so the strict sign condition follows by rearrangement. Setting \(r=3,H=3,\ell=1\) gives the negative covariance \(-1/25\) at \(N=5,m=4\), making the universal \(N\leq4\) result sharp. Exact enumeration of its five possible omitted individuals proves the displayed near-census value; the other sampling depths are verified by direct enumeration, with their rational outputs specified above. For fixed \(H/\ell=1+\delta\), take any integer \(r>2+1/\delta\); then \((r-1)/(r-2)=1+1/(r-2)<1+\delta\), giving strict negative covariance.

At \(m=2\), there is a positive probability of drawing the two \(A\) individuals, in which case \(K=1,Q=0\); every other pair has \(K=2,Q>0\). Hence the covariance is strictly positive. Finally, the near-census covariance is linear and therefore continuous in the finitely many distances. Strict negativity survives sufficiently small distance changes, including ultrametric-preserving binary resolutions with positive branch lengths.

## Verification

The self-contained script `check.py` enumerates labeled-individual subsets using exact rational arithmetic and independently compares them with the closed near-census formula. The included `certificate.json` records 65 nonnegative small-population dissimilarity-basis checks, 40 arbitrary-distance one-doubleton formula comparisons, and 150 ultrametric formula comparisons, plus the five-individual covariance sequence. These finite tests corroborate, but are not substitutes for, the unrestricted algebraic proof. Execute `python check.py` in the directory containing both verification files and compare its standard output with `certificate.json` byte for byte.

## Relationship to prior work

Botta-Dukát (2005) establishes that adding a species can reduce Rao quadratic diversity for particular abundance and distance configurations. This deterministic nonmonotonicity motivates the question, but does not itself determine the joint sample covariance, a sharp first population size, or a near-census threshold. Pavoine and Bonsall (2009) study distributions maximizing Rao diversity, a different optimization problem. Ricotta, Pavoine, Bacaro, and Acosta (2012) derive abundance-weighted functional-rarefaction expectation curves. Their expected-diversity monotonicity does not imply the sign of richness–diversity covariance at a fixed sampling depth. The equal-dissimilarity special case is Gini–Simpson diversity; known nonnegative richness–Simpson covariance results do not extend to arbitrary ultrametric dissimilarities.

## Limitations

The exact sign criterion concerns a one-doubleton, otherwise singleton abundance profile at the next-to-complete sampling depth. The unrestricted nonnegative lower boundary concerns **any** nonnegative symmetric distance array but only populations of at most four individuals. The ultrametric instability examples vary the number of species with the distance contrast; they do not characterize all fixed ultrametric trees or all sampling depths. Neither positive nor negative covariance establishes an ecological causal mechanism, and no result is asserted for unequal inclusion probabilities, correlated sampling, trait measurement error, or unrooted Faith diversity. Originality comparison with unavailable complete texts remains incomplete and requires independent assessment.

## References

1. Botta-Dukát, Z. (2005). Rao's quadratic entropy as a measure of functional diversity based on multiple traits. *Journal of Vegetation Science* 16, 533–540. First online: 2005-02-24. DOI: 10.1111/j.1654-1103.2005.tb02393.x.
2. Pavoine, S. and Bonsall, M. B. (2009). Biological diversity: distinct distributions can lead to the maximization of Rao's quadratic entropy. *Theoretical Population Biology* 75, 153–163. Online: 2009-02-20. DOI: 10.1016/j.tpb.2009.01.008.
3. Ricotta, C., Pavoine, S., Bacaro, G., and Acosta, A. T. R. (2012). Functional rarefaction for species abundance data. *Methods in Ecology and Evolution* 3, 519–525. First online: 2012-01-04. DOI: 10.1111/j.2041-210X.2011.00178.x.
4. Pavoine, S. (2026). The rich-Rao quadratic entropy. *Ecological Indicators* 182, 114512. DOI: 10.1016/j.ecolind.2025.114512. (Later comparison source, not archive motivation.)
