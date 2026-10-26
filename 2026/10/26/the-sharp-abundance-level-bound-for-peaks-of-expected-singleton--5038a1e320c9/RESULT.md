# The sharp abundance-level bound for peaks of expected singleton richness

## Finding

For a finite species assemblage with \(m\ge2\) species sampled independently with replacement, suppose the positive species probabilities \(p_1,\ldots,p_m\) sum to one. Let \(L\) be the number of *distinct* probabilities. For \(n\ge1\), let \(F_1(n)\) be the number of species represented exactly once in an \(n\)-individual sample, and put \(s_n=\mathbb E F_1(n)\). A **strict singleton-richness peak** is an integer \(n\ge2\) for which \(s_n>s_{n-1}\) and \(s_n>s_{n+1}\), or \(n=1\) when \(s_1>s_2\).

**Theorem.** The number of strict singleton-richness peaks is at most \(L\). This is sharp for every integer \(L\ge2\): there exist strictly positive species probabilities with exactly \(L\) distinct levels and exactly \(L\) strict peaks. For one species, the singleton expectation is one at \(n=1\) and zero at all larger sample sizes, so there is one initial peak.

An explicit three-species example is \((p_1,p_2,p_3)=(9899,100,1)/10000\). Its three strict peaks occur at sample sizes \(1\), \(102\), and \(9999\); the exact-rational verifier checks the six neighboring inequalities.

## Assumptions and scope

All draws are independent and identically distributed with replacement from a fixed finite probability vector; there is no temporal change in abundances, sample dependence, non-detection, or ecological recruitment. Species must have positive sampling probabilities. The parameter \(n\) is an integer sample size, not a species-abundance class. A repeated probability counts once toward \(L\), irrespective of the number of species sharing it. This is a bound for the *expectation* of the singleton count, not a claim about modes of its random distribution.

## Proof

**Exact expectation.** The indicator that species \(i\) occurs exactly once has probability \(np_i(1-p_i)^{n-1}\); therefore
\[
s_n=n\sum_{i=1}^m p_i(1-p_i)^{n-1}.
\]
For \(m\ge2\), all \(p_i\) belong to \((0,1)\). Group species having equal probability, with distinct values \(q_j\), multiplicities \(c_j\ge1\), and \(\lambda_j=\log(1-q_j)<0\). Define a continuous interpolation for \(t\ge0\):
\[
S(t)=t\sum_{j=1}^L\frac{c_jq_j}{1-q_j}e^{\lambda_j t}.
\]
Then \(S(n)=s_n\) for every positive integer, \(S(0)=0\), and \(S(t)>0\) for \(t>0\). Its derivative is the exponential polynomial
\[
S'(t)=\sum_{j=1}^L\frac{c_jq_j}{1-q_j}(1+\lambda_jt)e^{\lambda_jt}.
\]

**Root lemma.** If \(\lambda_1,\ldots,\lambda_L\) are distinct real numbers and \(P_j\) are real polynomials of degree at most one, a nonzero function \(H(t)=\sum_{j=1}^LP_j(t)e^{\lambda_jt}\) has at most \(2L-1\) real zeros counted with multiplicity. One proof proceeds by induction: divide by \(e^{\lambda_1t}\); differentiating twice annihilates \(P_1\), and transforms every other summand into a polynomial of degree at most one multiplied by \(e^{(\lambda_j-\lambda_1)t}\). Repeated Rolle's theorem gives at least \(r-2\) zeros of the second derivative if the original has \(r\) zeros. The induction hypothesis bounds the latter by \(2(L-1)-1\), hence \(r\le2L-1\). If the differentiated function vanishes identically, the original was a polynomial of degree at most one after multiplication, and the bound is immediate. The assertion also holds when fewer than \(L\) summands are present.

Every strict integer peak of \(s_n\) induces an interior local maximum of \(S\) on \((n-1,n+1)\), with the interval \((0,2)\) used for \(n=1\). Indeed, at its middle integer the interpolant strictly exceeds the endpoint values, so an interior maximum exists. The intervals for distinct strict integer peaks are disjoint because two strict integer peaks cannot be consecutive. Distinct interpolating maxima contribute at least one zero of \(S'\) each; between any two of them there is an intervening local minimum and hence an additional zero of \(S'\). More explicitly, any \(k\) ordered strict maxima separated by lower endpoint values force at least \(2k-1\) distinct zeros of \(S'\). The root lemma thus gives \(2k-1\le2L-1\), so \(k\le L\).

**Sharpness construction.** Fix \(L\ge2\). For \(j=2,\ldots,L\), set \(e_j=2^{j-2}\), choose \(0<\varepsilon\ll1\), and take \(p_j=\varepsilon^{e_j}\) and \(p_1=1-\sum_{j=2}^{L}\varepsilon^{e_j}\). All probabilities are positive, distinct, and sum to one for sufficiently small \(\varepsilon\). At the first sample, \(s_1=1\), while \(s_2\to0\), giving the initial peak. For each \(j\ge2\), set \(N_j=\lfloor\varepsilon^{-e_j}\rfloor\). Then \(N_jp_j\to1\), the contributions from all larger-probability species vanish exponentially, and those from all smaller-probability species vanish because \(N_jp_i\to0\). Consequently \(s_{N_j}\to e^{-1}\). Between successive scales use \(V_j=\lfloor\varepsilon^{-(e_j+e_{j+1})/2}\rfloor\); then \(s_{V_j}\to0\). Similarly \(s_{\lfloor\varepsilon^{-2e_L}\rfloor}\to0\) after the last scale. Thus the expected-singleton curve has \(L\) disjoint regions of strictly positive prominence, each containing an integer local maximum. To ensure these maxima are *strict*, choose \(\varepsilon\) transcendental and sufficiently small. For each fixed \(n\ge1\), \(s_{n+1}-s_n\) is a polynomial in \(\varepsilon\) with integer coefficients, not identically zero (at \(\varepsilon=0\), the \(n=1\) difference is \(-1\), and for \(n=2\) its leading term is \(-\varepsilon\), whereas for \(n\ge3\) it is \(+\varepsilon\)). Hence no adjacent expectations tie for transcendental \(\varepsilon\). Each region therefore contains a strict peak, and the previously proved upper bound shows there are exactly \(L\) of them.

## Verification

Run `python3 verify.py` using standard-library Python. The script computes the selected three-species singleton expectations as exact fractions, checks \(s_1>s_2\), \(s_{102}>s_{101},s_{103}\), and \(s_{9999}>s_{9998},s_{10000}\), as well as additional exact-separated-scale comparisons. Its output is the embedded `certificate.json`. These finite computations verify the explicit example only. The unbounded upper bound and all-level construction follow from the analytic arguments above.

## Relationship to prior work

Species-sampling theory has long studied accumulation and rarefaction curves. Heck, van Belle and Simberloff (1975) derive rarefaction richness expectations. Magurran (2005) discusses singleton abundance classes and sampling intensity. O'Hara (2005) evaluates richness estimators across changing sample sizes, and Chao and Jost (2012) study species-accumulation and coverage curves. The object here is different: the number of local maxima of the **expected number of species seen exactly once** as sampling size varies while abundances remain fixed. A modal singleton *abundance class* and a modal point on a *sampling-effort curve* are not equivalent. Standard exponential-polynomial zero-count methods supply the upper-bound tool; the claimed novelty is its sharp ecological interpretation and construction, not the root-count lemma.

## Limitations

No claim is made for dependent sampling, censoring, nonidentical detection, dynamic or infinite species pools, or fixed-census sampling without replacement. This establishes mathematical possibilities, not empirical prevalence. The construction requires extreme abundance separation as \(L\) increases. No external independent audit has been performed. The originality assessment remains subject to undiscovered occupancy/exponential-mixture formulations.

## References

- Heck, K. L., van Belle, G., and Simberloff, D. (1975). Explicit calculation of the rarefaction diversity measurement and the determination of sufficient sample size. *Ecology* 56, 1459–1461. DOI: 10.2307/1934716.
- Magurran, A. E. (2005). Species abundance distributions: pattern or process? *Functional Ecology* 19, 177–181. DOI: 10.1111/j.0269-8463.2005.00930.x.
- O'Hara, R. B. (2005). Species richness estimators: how many species can dance on the head of a pin? *Journal of Animal Ecology*. DOI: 10.1111/j.1365-2656.2005.00940.x.
- Mao, C. X., and Colwell, R. K. (2005). Estimation of species richness: mixture models, the role of rare species, and inferential challenges. *Ecology*. DOI: 10.1890/04-1078.
- Chao, A., and Jost, L. (2012). Coverage-based rarefaction and extrapolation: standardizing samples by completeness rather than size. *Ecology*. DOI: 10.1890/11-1952.1.
