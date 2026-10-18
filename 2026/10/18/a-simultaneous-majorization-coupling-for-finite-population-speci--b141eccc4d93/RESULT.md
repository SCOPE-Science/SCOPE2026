# A simultaneous majorization coupling for finite-population species accumulation

## Finding

**Theorem (whole-curve dominance and its exact tail gain).** Let \(s\ge2\), and let \(\boldsymbol a=(a_1,\ldots,a_s)\) be strictly positive integers with sum \(N\). Independently for each abundance profile under comparison, a rarefaction curve \(K_m\), \(0\le m\le N\), is defined by taking a uniformly random ordering of all \(N\) individual organisms and counting the number of species in its first \(m\) positions. Consider a unit balancing transfer from a donor of abundance \(a\) to a recipient of abundance \(b\), where \(a\ge b+2\), retaining the other abundances; the new pair is \((a-1,b+1)\).

There exists a coupling of the **two complete random curves**, with their required respective uniform-permutation laws, such that
\[
K_m^{\mathrm{balanced}}\ge K_m^{\mathrm{original}}\quad\text{for every }m\in\{0,\ldots,N\}\quad\text{simultaneously almost surely}.
\]
In particular, one can couple their first discovery times of every requested richness threshold so that each threshold is reached no later after balancing.

For the exact improvement of any fixed upper tail, let the other species have abundances \(c_1,\ldots,c_{s-2}\), totaling \(R=N-a-b\). Define \(W(t,q)\) as the number of \(t\)-element subsets of these \(R\) labeled individuals that represent exactly \(q\) other species, with \(W(t,q)=0\) outside the feasible domain. Write \(\binom u v=0\) for \(v<0\) or \(v>u\), including when \(u\ge0\) and \(v\) is nonintegral (the arguments below are integral). For each \(0\le m\le N\) and every integer \(r\),
\[
\binom Nm\bigl[\Pr(K_m^{\mathrm{balanced}}\ge r)-\Pr(K_m^{\mathrm{original}}\ge r)\bigr]
=\sum_{j=2}^{a}\left[\binom{a-1}{j-1}-\binom b{j-1}\right]W(m-j,r-2)\ge0.
\]
Also, for \(0\le m\le N\),
\[
\mathbb E K_m^{\mathrm{balanced}}-\mathbb E K_m^{\mathrm{original}}
=\frac{\binom{N-b-1}{m-1}-\binom{N-a}{m-1}}{\binom Nm},
\]
interpreted as zero when \(m=0\). It is strictly positive **if and only if** \(2\le m\le N-b\), and is zero otherwise.

By composing the simultaneous couplings, if a strictly positive integer abundance vector \(\boldsymbol a\) majorizes another such vector \(\boldsymbol d\) of the same total and length (so \(\boldsymbol d\) is obtainable by unit balancing transfers and permutations), one can jointly couple the two **entire** rarefaction processes with \(K_m(\boldsymbol d)\ge K_m(\boldsymbol a)\) at every sample size almost surely.

## Assumptions and scope

Sampling is *uniform without replacement* from a finite, fully labeled census, and the same random ordering underlies every sample-size prefix **within** each curve. There are \(s\ge2\) nonempty species. Species labels can be permuted without changing richness. The coupling is synthetic: it does not assert that a single physical specimen-ordering simultaneously generates both relabeled censuses.

For \(q\ge0\), the exact coefficient \(W(t,q)\) can be computed as the coefficient of \(z^t u^q\) in
\[
\prod_{i=1}^{s-2}\left(1+u\bigl[(1+z)^{c_i}-1\bigr]\right).
\]
For \(s=2\), the empty product is one. All formulas include endpoint sizes \(m=0,N\) under the zero-outside-range binomial convention.

## Proof

**Step 1: pair-only discovery time.** Fix the two altered species with combined abundance \(S=a+b\). Draw their \(S\) individuals in a uniformly random order, and write only the pair-type word. This word is uniform over all \(\binom Sa\) binary words with \(a\) donor symbols and \(b\) recipient symbols. Define \(T\) as the first pair-word position at which **both** types have appeared, so \(2\le T\le S\). For \(1\le j\le S\),
\[
\Pr(T>j)=\frac{\binom aj+\binom bj}{\binom Sj}.
\]
Indeed, the event that the first \(j\) pair symbols are all one type partitions into the all-donor and all-recipient cases. For the balanced pair, the same formula replaces \((a,b)\) by \((a-1,b+1)\). Therefore the original minus the balanced survival probability equals
\[
\frac{\binom{a-1}{j-1}-\binom b{j-1}}{\binom Sj}\ge0,
\]
because \(a-1\ge b+1>b\) and binomial coefficients \(\binom nj\) are nondecreasing in the nonnegative upper index for fixed nonnegative \(j\). For \(j=0\) the survival probabilities both equal one. Thus \(T_{\mathrm{balanced}}\) is stochastically no larger than \(T_{\mathrm{original}}\).

**Step 2: a simultaneous coupling of all prefixes.** By the inverse-CDF (quantile) construction, couple the two integer-valued discovery times so that \(T_{\mathrm{balanced}}\le T_{\mathrm{original}}\) almost surely. Given each coupled discovery time, draw its corresponding binary pair-word from its *true conditional distribution*. This preserves the uniform binary-word marginal for both models. For any prefix of length \(j\), the number of represented pair species is zero at \(j=0\), one for \(1\le j<T\), and two for \(j\ge T\). Hence the balanced pair has at least as many represented pair species for **every** pair-prefix length \(j\), simultaneously.

Independently sample a common uniformly random interleaving of the \(S\) pair positions with the \(R\) other positions, and a common uniformly random sequence of the other individuals' species. This interleaving has the same law under both abundance profiles. At every total-prefix size \(m\), both models have seen the same number \(j\) of pair positions and the same collection of other species. The pair-prefix inequality therefore gives the claimed \(K_m\) inequality for every \(m\), simultaneously. Finally, uniformly randomize individual labels within each species conditional on the species words; this yields actual uniformly random permutations of individually distinguished organisms for each census.

**Step 3: exact upper-tail kernel.** Fix a size-\(m\) unordered sample. Suppose it contains \(j\) individuals from the altered pair and \(m-j\) from the unaltered species, exactly \(q\) of the latter being represented. When \(j\ge1\), the number of pair selections showing exactly one altered species is \(\binom aj+\binom bj\) originally and \(\binom{a-1}j+\binom{b+1}j\) afterward. The original-minus-new difference is exactly \(\delta_j=\binom{a-1}{j-1}-\binom b{j-1}\). The total number \(\binom Sj\) of pair selections remains constant; consequently \(\delta_j\) cases shift from one to two represented pair species after balancing. The zero-pair-species case \(j=0\) is unchanged. For the upper-tail event \(K_m\ge r\), this shift crosses the threshold precisely when \(q=r-2\). Multiplying \(\delta_j\) by the exact other-species subset count \(W(m-j,r-2)\), summing over \(j\), and dividing by \(\binom Nm\), gives the claimed nonnegative kernel. Terms \(j=1\) and \(j>a\) vanish.

**Step 4: exact expectation and strictness.** If a species has \(x\) individuals, the probability it is absent from a size-\(m\) sample is \(\binom{N-x}m/\binom Nm\). Linearity of expectation and two applications of Pascal's identity show that the only altered species contribute exactly
\[
\frac{\binom{N-b-1}{m-1}-\binom{N-a}{m-1}}{\binom Nm}.
\]
Since \(N-b-1\ge N-a+1\), the numerator is strictly positive precisely for integer \(m-1\) between \(1\) and \(N-b-1\) inclusive, equivalently \(2\le m\le N-b\); outside this range both terms vanish or agree.

**Step 5: general majorization.** Every majorization relation between fixed-length integral abundance profiles with the same total can be resolved by finitely many unit transfers from a larger to a smaller component, plus coordinate permutations. Apply Step 2 to each adjacent pair of profiles. The gluing lemma for couplings (successively sample each next process conditionally on the preceding process) realizes all intermediate full curves jointly, so transitivity of the samplewise inequalities gives the final simultaneous coupling.

## Verification

The standalone `verify_rarefaction.py` uses only standard Python integer arithmetic. It directly enumerates the coefficient-defined richness count distribution, verifies the exact tail-improvement kernel for every feasible integer threshold and sample size, independently verifies the expectation and strictness formula, and directly enumerates the two-type discovery-time survival law. Executing `python verify_rarefaction.py` produced: 506 integer abundance partitions through total size 14; 1,846 directed unit balancing transfers; 24,966 transfer/sample-size pairs; 150,643 exact tail checks; and 280 exact two-type-word survival checks, all passing. These finite checks test the algebra but do not replace the general proof.

For illustration, from \((4,3,1)\) to \((4,2,2)\) with \(N=8\), the upper-tail differences multiplied by \(\binom 83\) at \(m=3\) equal \(1\) for \(r=2\) and \(4\) for \(r=3\), exactly as the kernel predicts.

## Relationship to prior work

The classical finite-census rarefaction expectation and multiple-hypergeometric observed-class distribution are prior work. Zoroa et al. (2016) establish stochastic ordering under probability balancing for **independent draws with replacement**. Wong and Yue (1973) likewise treat **independent** sampling. The present statement instead couples the **entire prefix richness path of a fixed finite census without replacement**, and gives an explicit nonnegative coefficient kernel for all richness upper tails after each individual-unit balancing transfer. These hypotheses and conclusions are not interchangeable with an iid with-replacement theorem. The existence of such a coupling does not imply the stronger 'single PMF sign crossing' property sometimes called strong stochastic dominance.

## Limitations

The theorem requires a fixed finite census, uniform sampling without replacement, positive integer species abundances, and the balancing (majorization) order; incomparable abundance vectors may have crossing richness curves. It does not assert monotonicity of variance, conditional processes under spatial sampling, abundance estimation from incomplete detection, or results for changing species identities. An equivalent formulation may already exist in the extensive literature on multivariate hypergeometric majorization; complete bibliographic exhaustiveness or independent verification is not claimed. The mathematical proof is not a model of behavioral or ecological dynamics.

## References

1. N. Zoroa, E. Lesigne, M.-J. Fernández-Sáez, P. Zoroa, and J. Casas, *The coupon collector urn model with unequal probabilities in ecology and evolution*, arXiv:1608.00155 (first public submission July 30, 2016), https://arxiv.org/abs/1608.00155.
2. C. K. Wong and P. C. Yue, *A majorization theorem for the number of distinct outcomes in n independent trials*, Discrete Mathematics (1973), DOI: 10.1016/0012-365X(73)90070-8.
3. P. Walton, *The Number of Observed Classes from a Multiple Hypergeometric Distribution*, Journal of the American Statistical Association (1986), DOI: 10.1080/01621459.1986.10478254.
4. A. W. Marshall, I. Olkin, and B. C. Arnold, *Inequalities: Theory of Majorization and Its Applications*, 2nd ed. (2011), chapter on sampling from a finite population.
