# Singleton conditioning universally increases observed species richness

## Finding

Suppose a population has at least two species. Select a specified focal species \(j\), draw \(n\ge1\) individuals, let \(N_j\) be the focal count, and let \(K\) be the number of represented species. Under either (i) \(n\) independent draws from any finite categorical distribution with at least two strictly positive probabilities, or (ii) a simple random sample of \(n\) distinct individuals from any finite census with at least two species present, if \(\Pr(N_j=1)>0\), then for every integer \(k\),
\[
\Pr(K\ge k\mid N_j=1)\ge\Pr(K\ge k).
\]
This is first-order stochastic dominance, valid for arbitrary heterogeneous abundance profiles; it is not merely an expectation or covariance inequality. In the independent-draw model, if \(n\ge2\), the inequality is strict at \(k=2\).

For every nondecreasing real function \(g\) of richness, and with \(F_1\) the number of singleton species, the two models consequently satisfy
\[
\operatorname{Cov}(g(K),F_1)\ge0.
\]
In the independent-draw model with \(n\ge2\) and strictly increasing \(g\), this covariance is strictly positive. No multiplicity \(r\ge2\) can replace the singleton event \(N_j=1\) in a universal first-order dominance theorem: for every sample size \(n\ge r\), positive-parameter counterexamples exist in both sampling models.

## Assumptions and scope

In model (i), fix an integer \(m\ge2\) and a finite vector of probabilities \((p_1,\ldots,p_m)\) with \(p_i>0\) and \(\sum_i p_i=1\). The \(n\) draws are independent and identically distributed with replacement. In model (ii), fix positive integer species census sizes \((c_1,\ldots,c_m)\), total size \(N=\sum_i c_i\), and sample exactly \(1\le n\le N\) distinct individuals uniformly without replacement. The focal event must have positive probability. Species richness \(K\) counts distinct species represented, and \(F_1=\#\{i:N_i=1\}\) counts species represented exactly once. These definitions also cover \(n=1\); the strict assertion requires \(n\ge2\). For a function \(g\), take its values on \(\{1,\ldots,n\}\), where finite moments are automatic.

## Proof

Fix the focal species \(j\). Independently of the random number \(T\) of sampled nonfocal individuals, construct a random list \(Y_1,Y_2,\ldots\) of nonfocal species labels. In model (i), the \(Y_t\) are independent draws from the categorical distribution with probabilities \(p_i/(1-p_j)\), for \(i\ne j\), and \(T\) is binomial with parameters \((n,1-p_j)\). In model (ii), let the list be the species labels in a uniformly random ordering of all \(N-c_j\) nonfocal census individuals, and take \(T\) independently with its usual hypergeometric distribution, the nonfocal count in a size-\(n\) census subsample. Both constructions reproduce the appropriate conditional uniform law for nonfocal labels given \(T=t\). In the census case the list need only be defined through its available length, and \(T\) cannot exceed that length.

Write \(R_t\) for the number of distinct species among the first \(t\) nonfocal labels, with \(R_0=0\). The resulting richness for an unconditional sample is
\[
K_{\mathrm u}=R_T+\mathbf1_{\{T<n\}}.
\]
Conditional on the focal species occurring exactly once, the remaining \(n-1\) observations are a uniform sample from the nonfocal individuals (model (ii)) or are independent renormalized nonfocal draws (model (i)). Consequently their conditional richness law is realized on the same probability space by
\[
K_{\mathrm s}=1+R_{n-1}.
\]
The event \(N_j=1\) being possible guarantees that \(n-1\) nonfocal individuals exist in model (ii). If \(T<n\), then \(R_T\le R_{n-1}\), so \(K_{\mathrm u}\le K_{\mathrm s}\). If \(T=n\), then adding one new observation changes richness by at most one: \(R_n\le R_{n-1}+1\), giving the same inequality. Thus \(K_{\mathrm u}\le K_{\mathrm s}\) almost surely under this coupling, proving stochastic dominance for every threshold \(k\).

For any nondecreasing \(g\), multiplying the expectation gap by \(\Pr(N_j=1)\) gives
\[
\operatorname{Cov}\bigl(g(K),\mathbf1_{\{N_j=1\}}\bigr)
=\Pr(N_j=1)\{\mathbb E[g(K)\mid N_j=1]-\mathbb E[g(K)]\}\ge0.
\]
Sum over focal species \(j\) to obtain the covariance assertion with \(F_1\). A focal species for which \(\Pr(N_j=1)=0\) contributes zero and needs no conditional distribution. For independent draws with \(n\ge2\), every \(p_j>0\) makes \(\Pr(N_j=1)>0\), and the unconditional event that all \(n\) draws are species \(j\) has positive probability \(p_j^n\), whereas \(N_j=1\) ensures \(K\ge2\). Therefore the inequality at \(k=2\), and hence for every strictly increasing \(g\), is strict for every focal species, implying strict covariance. In a finite census, strict covariance is not guaranteed; for example a full census has constant richness.

To prove sharpness of the singleton condition, take any integers \(n\ge r\ge2\). In the independent model, use \(n+1\) equally likely species, one designated focal and the other \(n\) nonfocal. The event \(N_j=r\) has positive probability and enforces \(K\le n-r+1<n\), whereas the unconditional event that the \(n\) draws hit all \(n\) nonfocal species exactly once has probability \(n!/(n+1)^n>0\), with richness \(n\). Thus at threshold \(k=n\) the proposed dominance fails. In the census model, take \(r\) individuals of the focal species and one individual of each of \(n\) other species; sample \(n\) individuals uniformly from these \(n+r\) individuals. Conditioning on \(N_j=r\) gives richness at most \(n-r+1<n\), but sampling all \(n\) nonfocal individuals has positive probability and richness \(n\). This proves that every \(r\ge2\) fails a universal dominance guarantee in both models.

## Verification

The companion standalone `verify.py` uses exact fractions and complete enumeration of independent-draw sequences and census subsamples for all positive census compositions with total size \(2\) through \(7\), at most four species, and sample size at most four. Its reproducible output is `certificate.json`. The certificate reports 718 model cases, 5,140 integer-threshold comparisons, 850 strict independent-draw checks, and 28 checked higher-multiplicity counterfamily parameter pairs. Run `python verify.py` in a folder containing no dependencies beyond the Python standard library. These finite tests check the stated identities only for their enumerated ranges; the proof for all sample sizes and abundance profiles is the coupling argument above.

## Relationship to prior work

Barbour and Gnedin's study of occupancy frequency counts provides a classical mathematical context for observed richness and counts of species observed \(r\) times. It develops asymptotic joint behavior and covariance structures; the inspected text does not derive this universal *conditional first-order stochastic order* for arbitrary categorical probabilities or finite-census sampling. An exact finite-uniform occupancy analysis entitled “A one-switch covariance law for occupancy richness and frequency counts” proves covariance sign transitions by multiplicity for equal box probabilities, but explicitly does not establish conditional stochastic monotonicity or heterogeneous sampling. Its positive singleton covariance is a consequence of the stronger conditional result here, restricted to its uniform model, not a duplicate theorem. Coddington and colleagues explain the empirical relevance of singleton observations to ecological species richness assessment; their study is not a universal stochastic comparison theorem. The sharp failure at every higher multiplicity distinguishes the qualitative singleton-only mechanism from generic moment identities.

## Limitations

The theorem addresses one fixed focal species and unconditional richness, not the distribution of richness conditioned on *some species* being a singleton. It does not assert independence or positive association among occupancy indicators. The finite-census model assumes uniform sampling of individuals without replacement, rather than unequal detection, spatial sampling, or adaptive sampling. The strictness statement applies to the iid model with at least two positive categories and \(n\ge2\); full finite censuses can have constant richness. The literature search cannot exclude an equivalent coupling already recorded under alternative occupancy or size-bias terminology; novelty is a best-knowledge assessment, not an independent certificate.

## References

1. A. D. Barbour and A. V. Gnedin, “Small counts in the infinite occupancy scheme,” arXiv:0809.4387 (first public version 2008-09-25), later *Electronic Journal of Probability* 14 (2009), 365–384, https://arxiv.org/abs/0809.4387 .
2. J. A. Coddington, I. Agnarsson, J. A. Miller, M. Kuntner and G. Hormiga, “Undersampling bias: the null hypothesis for singleton species in tropical arthropod surveys,” *Journal of Animal Ecology* 78 (2009), DOI: 10.1111/j.1365-2656.2009.01525.x .
3. “A one-switch covariance law for occupancy richness and frequency counts,” published research record (2026), https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-a-one-switch-covariance-law-for-occupancy-richness-and-frequency--93dddb2be813/RESULT.md .
