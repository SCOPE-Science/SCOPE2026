# A sharp 29-site threshold for two turning points in two-species zeta retention

## Finding

For the exact all-subsets retention-rate curve of a two-species incidence survey, **29 sites is the smallest survey size at which the sequence of retention rates can change monotonic direction twice**. At 29 sites, the unique unequal species-occupancy pair admitting two direction changes is \((22,26)\), up to exchanging species; it makes exactly two changes.

For the first five retention rates in this example,
\[
(R_1,R_2,R_3,R_4,R_5)=\left(\frac{139}{168},\frac{115}{139},\frac{4453}{5382},\frac{92114}{111325},\frac{27713}{33496}\right),
\]
and hence \(R_1>R_2<R_3<R_4>R_5\). In particular the curve has a strict local minimum at order two and a strict local maximum at order four.

The following exact identity explains the underlying competition for any finite number of species:
\[
R_{k+1}-R_k=\frac{(n-k)\sigma_k^2-(\mu_k-k)(n-\mu_k)}{(n-k)(n-k-1)(\mu_k-k)}.
\]
Here \(\mu_k\) and \(\sigma_k^2\) are respectively the mean and variance of species occupancy under the binomially tilted weights defined below. Increasing retention occurs exactly when the occupancy-variance contribution exceeds the finite-population depletion contribution.

## Assumptions and scope

Fix \(n\ge2\) distinguishable sites and a nonempty finite list of species, each with a nonempty set of occupied sites. Write \(r_i\in\{1,\ldots,n\}\) for the number of sites occupied by species \(i\). For each integer \(1\le k\le n\), sample a \(k\)-element site subset uniformly from all \(\binom nk\) subsets. Define \(Z_k\) as the expected count of species occurring in **every** site of the subset (intersection richness). Consequently,
\[
Z_k=\frac{1}{\binom nk}\sum_i\binom{r_i}{k},\qquad
\binom{a}{k}=0\text{ for }k>a.
\]
When \(Z_{k+1}>0\), define the conditional retention ratio \(R_k=Z_{k+1}/Z_k\). To count turns, form signs of all consecutive differences \(R_{k+1}-R_k\) among defined adjacent ratios; delete zero signs, then count sign changes in the resulting list. This does not count a terminal undefined ratio as a turn.

For the sharp finite classification there are exactly two species with occupancies \(1\le r\le s\le n\). Ratios \(R_1,\ldots,R_{s-1}\) are positive. A concrete 29-site realization has species A on sites \(1,\ldots,22\), and species B on sites \(4,\ldots,29\). Their intersection occupies 19 sites, their union all 29 sites. The location or overlap of species matters to the incidence matrix but not to the all-subsets mean \(Z_k\).

## Proof

**Step 1: Retention curvature identity.** For general occupancy counts \(r_i\), fix \(1\le k\le n-2\) with \(Z_{k+1}>0\). Put
\[
w_{i,k}=\frac{\binom{r_i}{k}}{\sum_j\binom{r_j}{k}},\quad
\mu_k=\sum_iw_{i,k}r_i,\quad
\sigma_k^2=\sum_iw_{i,k}(r_i-\mu_k)^2.
\]
The weights sum to one; \(\mu_k>k\) because \(Z_{k+1}>0\). The elementary binomial identity \(\binom{r}{k+1}=\binom rk(r-k)/(k+1)\), combined with the same identity in the site denominator, gives
\[
R_k=\frac{\mu_k-k}{n-k},\qquad
R_{k+1}=\frac{\mathbb E_k[(r-k)(r-k-1)]}{(n-k-1)(\mu_k-k)},
\]
where \(\mathbb E_k\) is expectation under weights \(w_{i,k}\). The numerator of the second expression equals \(\sigma_k^2+(\mu_k-k)^2-(\mu_k-k)\). Subtraction gives the claimed identity, with positive denominator. The identity therefore provides an exact variance-versus-depletion sign test, not a statistical approximation.

**Step 2: All integer candidates.** With two species and \(1\le r<s\le n\), abbreviate \(A_k=\binom rk+\binom sk\) and \(B_k=\binom nk\). Their retention ratios are
\[
R_k=\frac{A_{k+1}B_k}{A_kB_{k+1}}
\quad(1\le k<s).
\]
For each \(1\le k\le s-2\), clearing only strictly positive denominators gives
\[
\operatorname{sgn}(R_{k+1}-R_k)
=\operatorname{sgn}(T_k),\quad
T_k=A_kA_{k+2}B_{k+1}^{2}-A_{k+1}^{2}B_kB_{k+2}.
\]
Thus a completely integer-only finite classification requires no root finding or floating-point comparisons. Every unlabeled pair of distinct species occupancies is represented by exactly one \((r,s)\). The standalone `verify_zeta.py` performs exactly the nested finite loops: \(2\le n\le29\), \(2\le s\le n\), \(1\le r<s\), \(1\le k\le s-2\), computes \(T_k\), drops zero signs, and counts changes. These loops exhaust \(\sum_{n=2}^{28}\binom n2=\binom{29}{3}=3654\) candidates for \(n\le28\), none with two turns; the 406 candidates at \(n=29\) have exactly one pair with two turns, \((r,s)=(22,26)\). This is an exhaustive finite proof supported by the complete included integer-checking algorithm, not an inference from a partial sample. If \(r=s\), the factor of two cancels, giving \(R_k=(r-k)/(n-k)\), a nonincreasing sequence, so equality cases introduce no missing candidates.

**Step 3: Exact witness.** For \(n=29,r=22,s=26\), the first four consecutive differences are
\[
\begin{aligned}
R_2-R_1&=-\frac{1}{23352},\\
R_3-R_2&=\frac{37}{748098},\\
R_4-R_3&=\frac{27323}{599151150},\\
R_5-R_4&=-\frac{300819}{3728942200}.
\end{aligned}
\]
The remaining differences through \(R_{25}-R_{24}\) are strictly negative by the same exact integer sign computation. Hence exactly two turns occur. Because the lower-order census rules out two turns below 29 and the full 29-site census identifies this pair uniquely, both minimality and uniqueness hold.

## Verification

Run `python3 verify_zeta.py` with an ordinary Python 3 interpreter. The verifier uses only standard-library exact integers and fractions. It prints:

`VERIFY_OK lower_pairs=3654 boundary_pairs=406 unique_pair=(22, 26) direct_subsets=146595 weighted_curvature_identities=56`

Beyond the exhaustive \(T_k\) sign census, it checks the five displayed exact fractions and their four differences, directly enumerates 146,595 subsets of the specified two-species 29-site incidence matrix for depths one through five, and compares the general variance identity against independently constructed exact-rational zeta ratios for 56 test cases. The general identity itself has an algebraic proof, not merely finite numerical corroboration.

## Relationship to prior work

Hui and McGeoch (2014) introduced zeta diversity and explicitly interpreted successive zeta ratios as conditional retention probabilities. Latombe and colleagues (2018) describe the all-combinations calculation and retention-ratio implementation. McGeoch and colleagues (2019) introduced retention-rate curves as an ecological analysis device and discussed increasing, asymptotic, and modal empirical shapes. These works motivate the natural mathematical question about possible numbers of turns. The present result gives an exact **two-species, finite-sites minimum and uniqueness classification**, together with a general occupancy-variance sign identity; it does not challenge the accuracy of published empirical typologies or their original zeta definitions.

## Limitations

The theorem concerns all-subsets uniform without-replacement averages in a deterministic presence–absence matrix, not one particular sampled subset, estimated curves, species abundance, unequal inclusion probabilities, or spatially constrained site sampling. The onset at 29 sites does not imply ecological prevalence: the witness's successive retention differences are extremely small, so finite-sample noise could obscure both turning points. The finite sharp bound concerns at most 29 sites and exactly two species; it does not bound the number of turns for arbitrary numbers of sites or species, nor establish a biological assembly process. A previously unindexed exact combinatorial enumeration or stronger general theorem could subsume the minimum and should be checked independently.

## References

1. Hui, C., and M. A. McGeoch. 2014. “Zeta Diversity as a Concept and Metric That Unifies Incidence-Based Biodiversity Patterns.” *The American Naturalist* 184:684–694. DOI: 10.1086/678125. First available online 24 September 2014.
2. Latombe, G., M. A. McGeoch, D. A. Nipperess, and C. Hui. 2018. “zetadiv: An R package for computing compositional change across multiple sites, assemblages or cases.” bioRxiv preprint DOI: 10.1101/324897. Text for the original zeta implementation and ratios.
3. McGeoch, M. A., G. Latombe, N. R. Andrew, S. Nakagawa, D. A. Nipperess, and colleagues. 2019. “Measuring continuous compositional change using decline and decay in zeta diversity.” *Ecology* 100:e02832. DOI: 10.1002/ecy.2832.
