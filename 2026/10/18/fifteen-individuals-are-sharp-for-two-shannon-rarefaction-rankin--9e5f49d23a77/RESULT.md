# Fifteen individuals are sharp for two Shannon-rarefaction ranking reversals at fixed richness

## Finding

Fix a finite census of \(N\) individually labelled organisms partitioned into \(s\ge2\) present species, with positive integer abundance multiset \(\mathbf a=(a_1,\ldots,a_s)\). Draw a uniformly random \(m\)-subset without replacement and let \(\widehat H_{\mathbf a}(m)=-\sum_i (J_i/m)\log(J_i/m)\), interpreting \(0\log0=0\), where \(J_i\) is the observed count of species \(i\). Write \(F_{\mathbf a}(m)=\mathbb E\widehat H_{\mathbf a}(m)\), for \(1\le m\le N\).

For any two positive-integer abundance multisets with the **same** census size \(N\le14\) and the **same** number \(s\) of species, the nonzero sequence \(\{F_{\mathbf a}(m)-F_{\mathbf b}(m):2\le m\le N\}\) changes sign at most once. For \(N=15\), exactly one unordered pair, up to species relabelling and exchange of the two communities, has two sign reversals:

\[
\mathbf a=(1,1,4,4,5),\qquad \mathbf b=(2,2,2,2,7).
\]

For this pair, \(F_{\mathbf a}(m)>F_{\mathbf b}(m)\) for \(2\le m\le10\), the inequality reverses for \(11\le m\le14\), and \(F_{\mathbf a}(15)>F_{\mathbf b}(15)\). Every one of these inequalities is strict. This is a complete classification of the first population-size layer under the stated equal-richness comparison, not an assertion about all census sizes.

## Assumptions and scope

Sampling is uniform among the \(\binom Nm\) subsets of distinct labelled organisms, without replacement. Abundances are positive integers and their order does not matter. The compared assemblages have identical total abundance \(N\) and identical richness \(s\), but otherwise arbitrary compositions. The outcome is the expected **sample plug-in Shannon entropy** (natural logarithms), not an entropy-bias-corrected estimator, Shannon entropy of the population, or expected exponentiated Hill diversity. Sign reversals ignore exact ties; the universal claim covers every \(2\le N\le15\) in the finite ranges stated above.

## Proof

For species \(i\) with census abundance \(a_i\), its sampled count is hypergeometric:

\[
\Pr(J_i=j)=\frac{\binom{a_i}{j}\binom{N-a_i}{m-j}}{\binom Nm},
\]

with inadmissible binomial terms interpreted as zero. Linearity of expectation therefore gives the exact identity

\[
F_{\mathbf a}(m)=\log m-\frac{1}{m\binom Nm}
\sum_{i=1}^{s}\sum_{j=2}^{\min(a_i,m)}
 j\binom{a_i}{j}\binom{N-a_i}{m-j}\log j.
\]

(The \(j=1\) term vanishes because \(\log1=0\).) Hence at fixed \(N,m\), the difference of two such entropies is an integer linear combination of \(\log j\), divided by \(m\binom Nm\): the \(\log m\) terms cancel. Factoring every \(j\) into primes converts its sign into the sign of a sum of integers times \(\log2,\log3,\ldots\), involving only primes not exceeding \(N\).

The complete, executable finite proof is `verify_entropy_cross.py`. It recursively generates **every** nondecreasing positive-integer partition of each \(2\le N\le15\). It groups partitions by number of parts, enumerates every unordered same-richness pair, forms each exact integer log-coefficient vector for every \(2\le m\le N\), and counts strict sign reversals after omitting exact zeros. There is no sample-based truncation or graph-isomorphism assumption. The generator is complete by choosing the least remaining part recursively and making every subsequent part at least that large; uniqueness follows from the sorted representation.

Crucially, the sign comparison is **not** a floating-point approximation. For each prime \(p\le13\), set \(x=(p-1)/(p+1)\) and use

\[
\log p=2\sum_{r=0}^{399}\frac{x^{2r+1}}{2r+1}+R,\qquad
0<R<\frac{2x^{801}}{801(1-x^2)}.
\]

Rational arithmetic produces integer enclosures of each logarithm multiplied by \(10^{36}\). Signed sums of the endpoints certify the sign of every nonzero comparison, and an all-zero coefficient vector certifies any exact tie. An unresolved interval would stop verification rather than be interpreted as zero. The exhaustive census yields no two-reversal pairs for \(N\le14\), and exactly the one displayed unordered pair for \(N=15\).

The verified sign pattern for \(m=2,\ldots,15\) is nine positive entries, four negative entries, and one positive entry. Thus the inequalities and exactly two reversals hold at \(m=10\) to \(11\) and \(m=14\) to \(15\).

## Verification

Run `python3 verify_entropy_cross.py` using the supplied standalone standard-library program. It checks the complete census, exact integer-coefficient and rational-log sign certificates, first-layer uniqueness, and each witness sign. An independently structured cross-check literally enumerates all labelled \(m\)-subsets of both witness populations at sample sizes \(2,3,5,10,11,13,14,15\) and compares their averaged Shannon entropy with the hypergeometric identity. The latter check uses numerical logarithms only as a supplementary cross-check and is not the proof of strict signs. For the witness, approximate entropy differences at sample sizes \(10,11,14,15\) are respectively \(0.000604309215,-0.002116603436,-0.001172422466,0.001933602449\).

The exact census considered 175 nontrivial abundance profiles at \(N=15\), with 1,708 unordered equal-richness comparisons; 1,684 had no sign change, 23 had one and exactly one had two. Every comparison for \(N\le14\) had at most one change.

## Relationship to prior work

Chao, Wang and Jost (2013) study Shannon-entropy estimation, its connection with species-accumulation curves and the substantial dependence of plug-in entropy on sampling effort. That framework motivates comparing entropic rarefaction values at varying depths, but the examined article does not supply a sharp equal-census/equal-richness integer threshold for two ranking reversals. Chao and collaborators (2014) study Hill-number rarefaction and extrapolation; their Appendix J exhibits two crossings under **coverage-based** Shannon diversity for large assemblages of unequal richness while explicitly noting the corresponding sample-size-based curves in that example do not cross. Their sample-size/coverage distinction, and the difference between their Hill-diversity estimands and expected plug-in entropy, preclude treating that example as this finite classification. The main paper's inaccessible full text remains a bibliographic risk.

The finite classification is also distinct from thresholds for expected *number of distinct sampled species*, expected singleton counts, and sampled-richness variance: those are different statistics, and no one of their ranking statements determines the Shannon expectation ordering. The exact proof checks the entropy criterion directly.

## Limitations

The theorem concerns a complete finite census only through \(N=15\), identical census sizes and species richness, uniform sampling without replacement, and expected plug-in Shannon entropy. It neither bounds reversals for larger populations nor asserts this threshold if census size or richness differs across compared communities. It does not prove that the ranking differences are large enough to detect from noisy field measurements. Independent bibliographic review, including the inaccessible complete 2014 rarefaction treatment, remains outstanding.

## References

1. Chao, A., Wang, Y. T., and Jost, L. (2013). "Entropy and the species accumulation curve: a novel entropy estimator via discovery rates of new species." *Methods in Ecology and Evolution*. DOI: `10.1111/2041-210X.12108`. First publicly posted 19 August 2013.
2. Chao, A., Gotelli, N. J., Hsieh, T. C., et al. (2014). "Rarefaction and extrapolation with Hill numbers: a framework for sampling and estimation in species diversity studies." *Ecological Monographs*. DOI: `10.1890/13-0133.1`. The openly accessible Appendix J is `https://www.esapubs.org/archive/mono/M084/003/appendix-J.pdf`.
