# Four species are the sharp threshold for Simpson-matched rarefaction ranking reversals

## Finding
Let \(m\ge 1\). Two communities have strictly positive species-frequency vectors \(p=(p_1,\ldots,p_m)\) and \(q=(q_1,\ldots,q_m)\), each summing to one. From each community sample \(k\) individuals independently with replacement, and write \(R_p(k)\) and \(R_q(k)\) for the expected numbers of distinct species observed. Suppose the communities have equal Gini–Simpson diversity, namely \(\sum_i p_i^2=\sum_i q_i^2\).

**Sharp support-size dichotomy.** For \(m\le3\), the sign of \(R_p(k)-R_q(k)\) is constant for all integers \(k\ge3\); in fact, the difference is either strictly of one sign for every such \(k\), or identically zero. For every \(m\ge4\), there are two \(m\)-species communities with the same Gini–Simpson diversity and species count for which the sign of this expected-richness difference reverses as sample size increases.

For \(m=4\), an exact witness is
\[
p=\frac1{21}(1,4,6,10),\qquad q=\frac1{21}(2,2,8,9).
\]
Both have Gini–Simpson diversity \(32/49\). Yet \(R_p(k)>R_q(k)\) for every integer \(3\le k\le7\), while \(R_p(k)<R_q(k)\) for **every integer** \(k\ge8\). At \(k=1,2\) the expected species counts agree. The asserted minimum is the number of positive-frequency species, not the earliest sample size at which any such reversal might occur.

## Assumptions and scope
The sampling model is individual-based iid multinomial sampling **with replacement** from fixed, known, positive species frequencies. Each community has exactly \(m\) possible species; species labels need not be paired across communities. Sample size \(k\) is a nonnegative integer, and the comparison concerns the expectation of observed species richness, not realized richness or confidence intervals. Gini–Simpson diversity is \(D(p)=1-\sum_i p_i^2\). The pair need not have the same Shannon entropy or the same species-frequency multiset. No spatial aggregation, detectability bias, correlated sampling, or sample-based incidence process is included.

## Proof
**Step 1: exact accumulation curve.** A particular species of frequency \(p_i\) is missing from \(k\) independent draws with probability \((1-p_i)^k\). Summing discovery indicators gives
\[
R_p(k)=\sum_{i=1}^{m}\bigl[1-(1-p_i)^k\bigr].
\]
Hence \(R_p(1)=1\), and \(R_p(2)=2-\sum_i p_i^2\). Equal Gini–Simpson indices therefore force equality of the accumulation curves at sample sizes one and two.

**Step 2: at most three species prohibit reversal.** If \(m=1\) the vector is unique. If \(m=2\), equality of the first and second power sums of the frequencies determines their unordered pair, so the two accumulation curves coincide for every \(k\).

For \(m=3\), set \(x_i=1-p_i\) and \(y_i=1-q_i\). Their elementary symmetric sums of degrees one and two agree: \(e_1(x)=e_1(y)=2\), and equality of their sums of squares implies \(e_2(x)=e_2(y)\). Denote these common quantities by \(e_1,e_2\), and put \(e_x=x_1x_2x_3\) and \(e_y=y_1y_2y_3\). In formal power series in \(z\), define
\[
E_x(z)=\prod_{i=1}^3(1-x_i z)=1-e_1z+e_2z^2-e_xz^3,
\]
with \(E_y(z)\) analogously, and
\[
G_x(z)=\sum_{i=1}^3\frac1{1-x_i z}
=\frac{3-2e_1z+e_2z^2}{E_x(z)},\qquad
G_y(z)=\sum_{i=1}^3\frac1{1-y_i z}.
\]
Their difference factors exactly as
\[
G_y(z)-G_x(z)
=(e_y-e_x)z^3 G_x(z)\frac1{E_y(z)}.
\]
Every coefficient of \(G_x(z)\) and every coefficient of \(1/E_y(z)=\prod_i(1-y_i z)^{-1}\) is strictly positive: all \(x_i,y_i\) lie strictly between zero and one. Consequently the coefficient of \(z^k\) in \(G_y-G_x\) has the sign of \(e_y-e_x\) for **every** \(k\ge3\), unless this difference vanishes identically. But that coefficient is precisely
\[
\sum_i y_i^k-\sum_i x_i^k=R_p(k)-R_q(k).
\]
If \(e_x=e_y\), the two characteristic cubics coincide, so \(p\) and \(q\) are permutations and all the richness curves coincide. This proves the universal no-reversal result through three species without finite extrapolation.

**Step 3: an exact four-species reversal.** For the displayed vectors, both frequency sums are \(21/21=1\), and both squared numerator sums equal
\[
1^2+4^2+6^2+10^2=2^2+2^2+8^2+9^2=153.
\]
Thus both have \(D=1-153/441=32/49\). Direct use of Step 1 yields
\[
R_p(k)-R_q(k)=\frac{\Delta_k}{21^k},\qquad
\Delta_k=2\cdot19^k+13^k+12^k-20^k-17^k-15^k-11^k.
\]
Exact integer evaluation gives, for \(k=3,4,5,6,7\), the respective numerators
\[
24,\quad1152,\quad32040,\quad604800,\quad5638584,
\]
all positive, and for \(k=8,9,10,11,12,13\) the numerators
\[
-140168448,\ -10249508280,\ -396673344000,\ -12491277276456,\ -352662979794048,\ -9289460576923800,
\]
all negative. For every \(k\ge14\), the integer inequality \(20^{14}>2\cdot19^{14}\) implies \(20^k>2\cdot19^k\), while \(17^k+15^k>13^k+12^k\). Hence \(\Delta_k<0\) for all \(k\ge14\). The four-species ordering therefore reverses once, between sample sizes seven and eight, and never returns.

**Step 4: extension to every larger number of species.** For \(m>4\), multiply each of the four displayed species frequencies by \(1/2\), then append \(m-4\) common species, each of probability \(1/[2(m-4)]\), to both communities. Total masses are one, species counts are equal, and equality of squared-frequency sums persists. The expected richness contributions of the common appended species cancel. At sample size three, the difference of expected richness is exactly \(1/8\) of the four-species difference, namely positive \(3/9261\). For large integer \(k\), the negative term \(-(1-1/42)^k\) from the first community's unique rarest base species dominates every other uncancelled term, whose bases do not exceed \(1-2/42\). Thus the difference is eventually negative. Every \(m\ge4\) permits reversal, completing sharpness.

## Verification
Run the accompanying standard-library Python script `verify.py`, sending its stdout to `certificate.json`. It independently evaluates exact integer power sums, independently enumerates multinomial occupancy compositions for sample sizes \(2,3,4,5,7,8\), verifies all eleven required finite sign checks, checks the exact tail inequality at \(14\), and sanity-tests fifteen Simpson-matched pairs of ternary frequency vectors across sample sizes \(3\) through \(16\). The exported certificate is included in the package. The finite ternary grid is a diagnostic; the unlimited theorem is proved by the formal-series factorization, and the infinite four-species tail by an explicit integer inequality.

## Relationship to prior work
Lande, DeVries and Walla (2000) [1], inspected in accessible primary full text, derive the standard expected-species formula and analyze crossings when the community with *lower actual richness* has *higher Simpson diversity*. Their argument and numerical butterfly example do not give a Simpson-matched, equal-richness reversal or the three-versus-four species cutoff. Thompson and Withers (2003) [2], also inspected in primary full text, simulate how rarity and evenness affect accumulation-curve crossings. Their simulations vary Simpson diversity and predominantly involve 24 or more species; they do not imply the exact equal-index minimal-size classification. Chao, Wang and Jost (2013) [3] study entropy and the expected accumulation curve and its slopes; their full accessible methods and discussion contain no corresponding fixed-Simpson reversal threshold. Tóthmérész (1995) [4] and Liu et al. (2007) [5] treat broader diversity-ordering concepts; those may be relevant to a reformulation of the result, but material accessible here did not establish this precise theorem. The new assertion is the sharp matched-Simpson support-size dichotomy and its exact small witness, not the general fact that accumulation curves can cross or the standard indicator expectation formula.

## Limitations
The mathematical claims concern expectations under exact iid with-replacement sampling; they do not imply that two noisy empirical estimates can reliably be ranked with samples of size seven or eight. An equal Gini–Simpson index does not entail equal Shannon index or habitat-level equivalence. A literature-equivalent theorem under a power-majorization or Laplace-transform-order formulation remains a bibliographic risk despite targeted comparisons; independent bibliographic assessment has not been performed.

## References
[1] Lande, R., DeVries, P. J., and Walla, T. R. (2000), *When species accumulation curves intersect: implications for ranking diversity using small samples*, Oikos 89, 601–605. DOI: 10.1034/j.1600-0706.2000.890320.x.

[2] Thompson, G. G., and Withers, P. C. (2003), *Effect of species richness and relative abundance on the shape of the species accumulation curve*, Austral Ecology 28, 355–360. DOI: 10.1046/j.1442-9993.2003.01294.x.

[3] Chao, A., Wang, Y. T., and Jost, L. (2013), *Entropy and the species accumulation curve: a novel entropy estimator via discovery rates of new species*, Methods in Ecology and Evolution 4, 1091–1100. DOI: 10.1111/2041-210X.12108.

[4] Tóthmérész, B. (1995), *Comparison of different methods for diversity ordering*, Journal of Vegetation Science 6, 283–290. DOI: 10.2307/3236223.

[5] Liu, C., Whittaker, R. J., Ma, K., and Malcolm, J. R. (2007), *Unifying and distinguishing diversity ordering methods for comparing communities*, Population Ecology 49, 89–100. DOI: 10.1007/s10144-006-0026-0.
