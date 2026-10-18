# Sharp sampling-effort reversal in Jaccard autosimilarity

## Finding

The Jaccard similarity of the species lists detected by two replicate samples from the **same** finite community need not increase with the number of individuals sampled. In the independent-replicate, fixed-size without-replacement model defined below, every positive-integer species-abundance profile containing at most five individuals has nondecreasing expected Jaccard autosimilarity across sample sizes. At six individuals, the only profile (up to species relabeling) with a strict decrease is \((1,5)\), whose expectation decreases from \(7/9\) at sample size two to \(3/4\) at sample size three.

For every integer \(N\ge3\), the two-species community \((1,N-1)\) has exactly
\[
E_N(1)=\frac{(N-1)^2+1}{N^2},\qquad
E_N(m)=1-\frac mN+\left(\frac mN\right)^2\quad(2\le m\le N).
\]
Consequently, \(E_N(m+1)-E_N(m)=(2m+1-N)/N^2\) for \(2\le m<N\). For \(N\ge6\), the expectation initially rises from sample size one to two, then falls for all integers \(m\ge2\) with \(2m+1<N\), eventually rising to \(1\). Its minimum over \(m\ge2\) is reached at the integer(s) nearest \(N/2\), and approaches \(3/4\) as \(N\) grows.

A second exact phase law holds if the two size-\(m\) replicate samples are **jointly drawn disjointly** from the same census: for \(2\le m\le\lfloor N/2\rfloor\), their expected Jaccard similarity for \((1,N-1)\) is \(1-m/N\). Thus independent and disjoint sampling protocols differ in expectation by exactly \((m/N)^2\) over this range. In particular, at half-census sampling in an even-sized community the two expectations are \(3/4\) and \(1/2\), respectively.

## Assumptions and scope

A census contains \(s\ge1\) species with positive integer abundances \(\mathbf a=(a_1,\ldots,a_s)\), with \(N=\sum_i a_i\) labeled individuals. Each independent replicate chooses one of the \(\binom Nm\) labeled size-\(m\) subsets uniformly, with no repeated individual within a replicate. **The two replicates are drawn independently**, so their selected individuals may overlap. Write \(U_m,V_m\) for their nonempty sets of detected **species**, not their sets of labeled individuals, and define \(J_m=|U_m\cap V_m|/|U_m\cup V_m|\) and \(E_{\mathbf a}(m)=\mathbb E[J_m]\). All claims of monotonicity concern this expectation, not any sample path or deterministic nested pair of species lists.

The disjoint-replicate comparison uses another, expressly different joint design: first choose two disjoint labeled subsets of size \(m\) uniformly among ordered disjoint pairs, possible only for \(2m\le N\). Each marginal subset remains uniform, but the two replicates are not independent. The results do not concern independent sampling of an unlimited population with replacement, noisy species detection, or different underlying communities.

## Proof

**Exact finite-population support formula.** For any nonempty subset of species \(S\subseteq\{1,\ldots,s\}\), write \(A(S)=\sum_{i\in S}a_i\) and
\[
W_m(S)=\sum_{T\subseteq S}(-1)^{|S|-|T|}\binom{A(T)}m,
\]
with \(\binom{x}{m}=0\) when \(x<m\). By inclusion–exclusion, \(W_m(S)\) counts the size-\(m\) labeled subsets whose detected-species set is exactly \(S\). Hence
\[
E_{\mathbf a}(m)=\frac1{\binom Nm^2}
\sum_{S,T\ne\varnothing}W_m(S)W_m(T)
\frac{|S\cap T|}{|S\cup T|}.
\]
This is an **exact rational** finite sum, with no limiting approximation.

**Sharp six-individual boundary.** Unordered abundance profiles are exactly the nondecreasing positive-integer partitions of their census size. The accompanying standalone program generates all \(29\) such partitions of \(N=1,\ldots,6\), applies the preceding exact formula at every sample size, and independently recomputes the same expectations by explicitly selecting labeled individual subsets, forming their detected-species masks, and pairing those subsets. There are \(135\) profile/sample-size computations. The output certificate lists every exact rational expectation. For all profiles of size at most five, every forward difference is nonnegative; among the eleven profiles of size six, the sole negative forward difference occurs for \((1,5)\), between sizes two and three. Generation of all partitions by recursively choosing successive parts at least as large as the preceding part establishes exhaustiveness; the two independently implemented exact counting methods agree on every cell.

**Analytical family.** For the profile \((1,N-1)\), a sample of size \(m\ge2\) always contains the dominant species. Its rare singleton appears with probability \(t=m/N\). For independently sampled replicates the two rare-species detection indicators are independent Bernoulli variables of parameter \(t\). Their detected-species lists agree, giving Jaccard value \(1\), unless exactly one replicate detects the singleton, giving value \(1/2\). The disagreement probability is \(2t(1-t)\), proving \(E_N(m)=1-t(1-t)\). At sample size one the lists consist of one species each, and the probability of a match is \(((N-1)/N)^2+(1/N)^2\). Subtracting successive values proves the stated exact difference. For \(N=6\), the entire sequence is
\[
\left(\frac{13}{18},\frac79,\frac34,\frac79,\frac{31}{36},1\right).
\]
In particular the first decrease cannot occur before \(N=6\), and does occur there. The limiting minimum follows by substituting the integer(s) nearest \(N/2\) into \(1-t+t^2\).

**Disjoint design.** When two size-\(m\) samples are disjoint, the unique rare individual belongs to at most one. For \(m\ge2\), both samples necessarily contain the dominant species; the probability that the singleton is in either sample is \(2m/N\). Thus the Jaccard value is \(1/2\) with this probability and \(1\) otherwise, proving \(E_N^{\mathrm{disjoint}}(m)=1-m/N\). For \(m=1\) it instead equals \(1-2/N\), since the Jaccard value is zero when the singleton is selected. The two formulas prove the exact design gap \((m/N)^2\) for all feasible \(m\ge2\).

## Verification

Run `python3 verify_jaccard.py` from the directory containing that file. It uses only the Python standard library and writes `census_n_le_6.csv`; the included CSV is the corresponding complete output. The program compares inclusion–exclusion to a separate direct enumeration of labeled samples for all \(135\) finite cells, checks the general singleton/dominant formula for \(3\le N\le120\), verifies the first-difference identity, and independently enumerates ordered disjoint replicate pairs for small populations. The finite census is exhaustive for \(N\le6\); finite checks are supplementary, not proofs of the arbitrary-\(N\) formulas above.

## Relationship to prior work

Wolda (1981) introduced the expected-null similarity of two samples from a single fauna as a key ecological baseline and analyzed sample-size effects for several indices by simulation; the article's selected binary coefficients did not include the present fixed-size Jaccard census theorem. Cao, Williams, and Larsen (2002) explicitly used within-community Jaccard **autosimilarity** to assess sample representativeness. Chao, Chazdon, Colwell, and Shen (2005) analyzed classic Jaccard sample-size bias and compared equal-sized replicates from one assemblage, sampling with replacement within each replicate. These papers motivate the objective but do not establish the stated sharp finite cutoff or the contrast between independent and disjoint finite-census sampling laws in the inspected material. Published mathematical research records on successive species discovery and richness-diversity covariance address different observables and do not imply this result.

## Limitations

This is a statement about an idealized completely known two-species extremal census and exact expectations under two specified sampling designs. The observed similarity in a particular realization may behave differently. The small-census uniqueness assertion applies only at \(N=6\); no classification for every larger abundance profile is claimed. Disjoint pairs are feasible only when \(2m\le N\). The ecological implication is a limitation of using autosimilarity itself as a monotone sampling-completeness surrogate, not an inference about ecological succession or a recommendation to change field protocols without accounting for sampling design. Bibliographic risk remains because the complete Cao et al. (2002) text could not be obtained; an unlocated equivalent formulation may exist. Independent literature and mathematical audit have not been performed.

## References

- Wolda, H. (1981). “Similarity indices, sample size and diversity.” *Oecologia* 50, 296–302. DOI: 10.1007/BF00344966. Open primary text: https://ecoevol.ufg.br/adrimelo/div/Wolda1981.pdf.
- Cao, Y., Williams, D. D., and Larsen, D. P. (2002). “Comparison of ecological communities: The problem of sample representativeness.” *Ecological Monographs* 72, 41–56. DOI: 10.1890/0012-9615(2002)072[0041:COECTP]2.0.CO;2. First publicly released by the publisher on 2002-02-01.
- Chao, A., Chazdon, R. L., Colwell, R. K., and Shen, T.-J. (2005). “A new statistical approach for assessing similarity of species composition with incidence and abundance data.” *Ecology Letters* 8, 148–159. DOI: 10.1111/j.1461-0248.2004.00707.x. Primary full text: https://www.robertkcolwell.org/publications/7597.pdf. First online 2004-12-17.
