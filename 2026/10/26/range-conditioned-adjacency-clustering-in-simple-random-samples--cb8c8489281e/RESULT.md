# Range-conditioned adjacency clustering in simple random samples is stochastically decreasing

## Finding

Select uniformly a subset \(S\) of cardinality \(k\) from \(\{1,\ldots,n\}\), where \(n\ge3\) and \(2\le k\le n\). Define the span \(R=\max S-\min S\) and local clustering count \(A=\#\{i:\,i,i+1\in S\}\). For \(r\in\{k-1,\ldots,n-1\}\), write \(z=r+1-k\).

When \(z=0\), the conditional adjacency count equals \(k-1\) with certainty. When \(z\ge1\), define \(H=k-A\), the number of consecutive selected blocks. The exact conditional distribution is
\[
\Pr(H=h\mid R=r)=\frac{\binom{k-1}{h-1}\binom{z-1}{h-2}}{\binom{r-1}{k-2}},\qquad 2\le h\le\min(k,z+1).
\]
Every other conditional probability is zero. This distribution is independent of the ambient population size \(n\).

The laws \(A\mid R=r\) decrease in first-order stochastic order as \(r\) increases. In particular, for each nondecreasing real function \(g\) on the finite support of \(R\),
\[
\operatorname{Cov}(A,g(R))\le0.
\]
For \(2\le k<n\) and strictly increasing \(g\), the covariance is strictly negative. When \(k=n\), the statistics are deterministic.

## Assumptions and scope

All \(\binom{n}{k}\) subsets of \(\{1,\ldots,n\}\) are equiprobable. The statistic \(A\) counts adjacent *selected* integers, not the number of runs; \(H=k-A\) is the number of nonempty runs. The span \(r\) must satisfy \(k-1\le r\le n-1\). A nondecreasing function includes constant functions, for which covariance is zero.

## Proof

**Conditional uniformity.** For any fixed span \(r\), there are \(n-r\) possible left endpoints. Given a left endpoint, both extreme sites are selected, and the \(k-2\) interior selected sites form a uniformly random subset of the \(r-1\) available interior sites. Thus the binary incidence word of the \(r+1\) sites between sample extremes is uniform among all length-\(r+1\) binary words with \(k\) ones, both endpoints one. Each such word occurs exactly \(n-r\) times in the ambient sample space.

**Joint enumeration.** If \(z=r+1-k=0\), there are no absent sites, so \(A=k-1\). If \(z\ge1\), a word with \(h\) one-runs has \(h\) positive one-block lengths summing to \(k\), chosen in \(\binom{k-1}{h-1}\) ways; it has \(h-1\) positive zero-block lengths summing to \(z\), chosen in \(\binom{z-1}{h-2}\) ways. There are \(\binom{r-1}{k-2}\) admissible incidence words in total. Every run of \(\ell\) ones contributes \(\ell-1\) adjacent selected pairs; hence \(A=k-h\). Division gives the stated probability.

**One-zero insertion coupling.** Let \(W_r\) be a uniformly random admissible word of length \(r+1\) with \(k\) ones, both endpoints one. Choose uniformly one of its \(r\) gaps between successive positions, and insert a zero in that gap. Every admissible length-\(r+2\) output word with \(k\) ones contains exactly \(z+1\) zeros; deleting any one of these zeros, while retaining the two endpoint ones, gives one admissible input and the corresponding insertion gap. Thus each output has exactly \(z+1\) equally weighted preimage pairs, even when zeros are consecutive. The output is therefore uniform among the longer admissible words. Inserting a zero cannot create an adjacency of ones and destroys exactly one adjacency if and only if its gap formerly separated two ones. Hence \(A_{r+1}\le A_r\) almost surely. This establishes first-order stochastic monotonicity.

**Covariance and strictness.** Conditional means therefore decrease with \(r\). For \(k\ge3\), direct counting of the \(r\) possible internal adjacent locations gives \(\mathbb E[A\mid R=r]=(k-1)(k-2)/(r-1)\), strictly decreasing on the entire span support. For \(k=2\), the conditional mean equals \(1\) at span one and \(0\) thereafter. For any independent copies \(R,R'\), the identity \(2\operatorname{Cov}(\mathbb E[A\mid R],g(R))=\mathbb E[(\mathbb E[A\mid R]-\mathbb E[A\mid R'])(g(R)-g(R'))]\) proves nonpositivity because the factors have opposite signs. If \(k<n\) and \(g\) is strictly increasing, the span support contains at least two distinct values and some pair of conditional means differs, so strict negativity follows. The total covariance identity completes the proof.

## Verification

The accompanying `verify.py` exhaustively enumerates every \(k\)-subset for \(3\le n\le12\) and \(2\le k<n\), independently computing conditional mass functions, conditional means, all first-order stochastic tail comparisons and unconditional covariance signs. It passes 2,750 exact rational/integer assertions. The infinite families of identities and inequalities follow from the proof, not from this finite experiment.

## Relationship to prior work

Classical fixed-composition runs laws count clusters in random sequences; Smeeton and Cox (2003) explain their statistical use and simulation. The present claim conditions additionally on the *sampled numerical span* and obtains an ambient-size-free finite conditional law plus a simultaneous monotone coupling for every span. Stepanov (2011) studies runs based on discrete order statistics and reports limiting laws for the number and longest length of runs; an accessible abstract does not establish the present exact conditional span family, but the full article was not available for complete comparison. Standard discrete order-statistics texts study the range and sampling without replacement, without a directly identified span-conditioned adjacency ordering.

## Limitations

This applies only to a uniform fixed-size sample of distinct consecutive integer labels. It is not a result for unequal inclusion probabilities, samples with replacement, arbitrary spacing metrics, or a universal stochastic inequality across different sample sizes. The proof gives monotonicity conditional on the span, not independence. Earlier implicit appearances of the zero-insertion coupling or its conditional law remain a priority risk, especially in the literature on binary runs and discrete order statistics.

## References

Smeeton, N., and Cox, N. J. (2003). *Do-it-yourself shuffling and the number of runs under randomness*. The Stata Journal 3(3), 270–277. DOI: 10.1177/1536867X0300300304.

Stepanov, A. (2011). *Runs based on discrete order statistics*. TWMS Journal of Applied and Engineering Mathematics 1(2), 185–191. https://dergipark.org.tr/en/pub/twmsjaem/article/761794.

Arnold, B. C., Balakrishnan, N., and Nagaraja, H. N. *A First Course in Order Statistics*. SIAM Classics in Applied Mathematics, chapter 3.
