# Exact singleton-rarefaction envelope and the dominant-species staircase

## Finding

Let \(N\ge S\ge2\) be integers. A community has exactly \(S\) species with strictly positive integer abundances \(a_1,\ldots,a_S\) summing to \(N\). Sample exactly \(k\) individuals uniformly without replacement, where \(2\le k\le N\), and denote by \(F_1\) the number of species represented exactly once in the sample.

**Finite-envelope theorem.** A maximizing community always exists in which \(S-1\) abundances differ by at most one and the last abundance is arbitrary. Specifically, for each integer \(1\le L\le N-S+1\), set
\[
q_L=\left\lfloor\frac{N-L}{S-1}\right\rfloor,\qquad r_L=N-L-(S-1)q_L.
\]
Then the exact global maximum is
\[
\max_{\substack{a_i\in\mathbb Z_{\ge1}\\\sum_i a_i=N}}\mathbb E F_1
=\frac1{\binom Nk}\max_{1\le L\le N-S+1}
\left[
L\binom{N-L}{k-1}
+(S-1-r_L)q_L\binom{N-q_L}{k-1}
+r_L(q_L+1)\binom{N-q_L-1}{k-1}
\right].
\]
Binomial coefficients are zero when the lower argument is outside \([0,\text{upper}]\). This requires only \(N-S+1\) candidate evaluations, rather than enumerating every abundance partition. The theorem guarantees *one* such maximizer; it does not claim that every maximizer has this form.

**Macroscopic sampling staircase.** Fix \(S\ge2\) and suppose integers \(k_N\) obey \(k_N/N\to\rho\in(0,1)\). Whenever \(\rho\ne1/j\) for every integer \(j\ge2\), put \(m=\lfloor1/\rho\rfloor\). For all sufficiently large \(N\), the *unique maximizing abundance multiset* is
\[
\{N-(S-1)m,\underbrace{m,\ldots,m}_{S-1}\},
\]
and its optimal expected singleton count converges to
\[
(S-1)m\rho(1-\rho)^{m-1}.
\]
At exact reciprocal sampling fractions, this uniqueness conclusion is not asserted. In particular, the asymptotically optimal rare-species abundance decreases stepwise as the sampling fraction increases; this is not the uniform-abundance optimum of every sampling regime.

For example, with \(N=9\), \(S=3\), the unique maximizing abundance multisets at sample depths \(k=4,5,6\) are, respectively, \((3,3,3)\), \((2,2,5)\), and \((1,1,7)\).

## Assumptions and scope

Each of the \(N\) individuals is distinct, and all subsets of size \(k\) have equal probability. Abundances are *integer counts*, every community species is present, and both \(N\) and \(S\) are fixed during the finite optimization. There is no replacement, dispersal, detection heterogeneity, species dependence beyond the fixed counts, or distributional prior over abundance vectors. The objective is expected sample-singleton richness, not total sample richness or the number of true census singletons. In the asymptotic statement, \(S\) is held fixed while \(N\) grows, and \(k_N/N\) has a nontrivial limit strictly between zero and one.

## Proof

**1. Exact singleton expectation.** The number of size-\(k\) subsamples containing exactly one individual of a species of size \(a\) is \(a\binom{N-a}{k-1}\). By indicator linearity,
\[
\mathbb E F_1=\frac{1}{\binom Nk}\sum_{i=1}^S f(a_i),\qquad f(a)=a\binom{N-a}{k-1}.
\]
The binomial convention above applies at every boundary, including \(k=N\).

**2. A single change of direction in marginal returns.** For \(k\ge3\), define \(D(a)=f(a+1)-f(a)\) for integer \(1\le a<N\). Direct binomial subtraction gives
\[
D(a)=\frac{\binom{N-a-1}{k-2}(N-k+1-ka)}{k-1}
\quad (1\le a\le N-k+1),
\]
and \(D(a)=0\) for \(a>N-k+1\). For \(1\le a\le N-k+1\), the second difference is
\[
D(a+1)-D(a)=\frac{\binom{N-a-2}{k-3}}{k-2}\big(ka-2(N+1-k)\big).
\]
After this range, the second difference is zero. Thus with
\[
t=\max\left\{1,\left\lceil\frac{2(N+1-k)}{k}\right\rceil\right\},
\]
the marginal sequence \(D\) is nonincreasing on indices up through \(t\) and nondecreasing on indices from \(t\) onward. This also covers the boundary between the negative marginal value and the terminal zero plateau. For \(k=2\), \(f(a)=a(N-a)\) has decreasing marginals everywhere and is handled separately.

**3. Concentrate high entries, balance the remainder.** Begin at any global maximizing positive integer abundance vector. If two entries \(a\le b\) both exceed \(t\), replace them by \(a-1,b+1\). Its objective change is \(D(b)-D(a-1)\ge0\) because \(a-1\ge t\) and the marginals are nondecreasing thereafter. Repeat until at most one entry exceeds \(t\); each transfer removes mass from a smaller high entry, so the process terminates while keeping all entries positive. Now, among all the remaining entries at most \(t\), if two are \(a<b-1\), replace them by \(a+1,b-1\). The gain is \(D(a)-D(b-1)\ge0\) since both indices are within the decreasing-marginal part. This smoothing terminates at a balanced integer multiset: all but possibly one abundance differ by at most one. Because the starting vector was globally optimal, these nondecreasing exchanges preserve the maximum. If no entry ever exceeds \(t\), smooth all \(S\) entries. If \(k=2\), global concavity gives a balanced optimum directly. Parameterizing the distinguished entry as \(L\) yields the displayed exact finite envelope.

**4. A uniform limit for individual singleton probabilities.** For any species size \(a\ge1\), define \(p_N(a)=f(a)/\binom Nk\). By counting first the one sampled member of that species and then excluding its other members,
\[
p_N(a)=\frac{ak_N}{N}\frac{\binom{N-k_N}{a-1}}{\binom{N-1}{a-1}}.
\]
For each fixed \(a\), \(p_N(a)\to h_\rho(a)=a\rho(1-\rho)^{a-1}\). Moreover, uniformly over all positive integers \(a\),
\[
0\le p_N(a)\le\frac{ak_N}{N}\left(\frac{N-k_N}{N-1}\right)^{a-1}
\]
when \(a\le N-k_N+1\), and \(p_N(a)=0\) otherwise. The geometric factor is eventually bounded strictly below one because \(k_N/N\to\rho\in(0,1)\). Hence both \(p_N(a)\) and \(h_\rho(a)\) vanish uniformly in their large-\(a\) tails. Pointwise convergence on each finite prefix proves uniform convergence over all positive integer \(a\).

**5. Sharp asymptotic optimizer and uniqueness.** Consecutive values satisfy
\[
\frac{h_\rho(a+1)}{h_\rho(a)}=\frac{a+1}{a}(1-\rho).
\]
If \(\rho\) is not a reciprocal integer, the unique integer maximizer is \(m=\lfloor1/\rho\rfloor\), and the gap
\[
\delta=h_\rho(m)-\sup_{a\ne m}h_\rho(a)>0
\]
is strictly positive. In every \(S\)-species profile, at least one abundance is \(\ge N/S\), so its singleton contribution tends uniformly to zero. A feasible profile with the other \(S-1\) abundances equal to \(m\) has expected singleton count at least \((S-1)p_N(m)\). If a competing optimum had any other abundance (besides one chosen maximal entry) unequal to \(m\), uniform convergence and the gap \(\delta\) would give total at most \((S-1)p_N(m)-\delta/2+o(1)\), a contradiction for large \(N\). Thus every optimum eventually has precisely \(S-1\) entries equal to \(m\), with the final entry fixed by the sum. The limit follows directly. This argument proves eventual uniqueness of the *multiset*, not of species labelings.

## Verification

Run `python3 verify_singleton_profiles.py` with Python 3 and the standard library. The checker independently enumerates all nondecreasing integer abundance partitions for every \(2\le N\le28\), every eligible \(S\le7\), and every \(2\le k\le N\), and compares exhaustive maxima to the one-parameter candidate family. It checks the exact first- and second-difference identities at \(N\le74\), and independently enumerates uniform without-replacement samples in small instances to compare counts to the analytic expectation. It also checks the three \(N=9\) transitions and four finite large-\(N\) instances. Finite checks support the formulas but do not prove universal quantification; the exchange and tail arguments above supply that proof.

## Relationship to prior work

Heck, van Belle, and Simberloff (1975) calculate mean and variance of conventional rarefied *species richness*, not its fixed-abundance-class maximizer. Coddington and colleagues (2009) analyze ecological sampling bias in singleton frequencies, principally using empirical data and a lognormal sampling model; their primary article does not derive this fixed-\(N,S,k\) optimization. Chao and Jost (2012) develop richness/coverage-based rarefaction and discuss singleton-based coverage estimators, but not the global singleton envelope. Locey and White (2013) study the entire feasible set of species abundance distributions at fixed richness and total abundance; the accessible material does not establish the expected-sample-singleton extremizers. Bhimaraju, Chatterjee, and Varshney (2023) provide a related *continuous* concave-to-convex resource-allocation reduction; it motivates caution about treating the exchange shape as a new general optimization principle, but does not supply the integer hypergeometric formula or the reciprocal sampling-fraction staircase. The contribution assessed here is the **combined sharp ecological finite envelope and eventual optimizer classification**, not the general existence of exchange arguments.

## Limitations

Neither every finite maximizing multiset nor uniqueness at finite \(N\) is characterized. No boundary claim is made at sampling-fraction reciprocals or when the number of species grows with census size. Sampling without replacement and fixed strictly positive integer abundances are essential assumptions. The theorem is a mathematical upper benchmark for expected singleton counts, not a claim that natural ecological abundance vectors maximize them. Stronger previous literature may exist, especially in uninspected complete texts of feasible-set or resource-allocation studies. No independent validation has been performed.

## References

- Heck, K. L. Jr., van Belle, G., and Simberloff, D. (1975). Explicit Calculation of the Rarefaction Diversity Measurement and the Determination of Sufficient Sample Size. *Ecology* 56, 1459–1461. https://doi.org/10.2307/1934716
- Coddington, J. A., Agnarsson, I., Miller, J. A., Kuntner, M., and Hormiga, G. (2009). Undersampling bias: the null hypothesis for singleton species in tropical arthropod surveys. *Journal of Animal Ecology* 78, 573–584. https://doi.org/10.1111/j.1365-2656.2009.01525.x
- Chao, A., and Jost, L. (2012). Coverage-based rarefaction and extrapolation: standardizing samples by completeness rather than size. *Ecology* 93, 2533–2547. https://doi.org/10.1890/11-1952.1
- Locey, K. J., and White, E. P. (2013). How species richness and total abundance constrain the distribution of abundance. *Ecology Letters* 16, 1177–1185. https://doi.org/10.1111/ele.12154
- Bhimaraju, A., Chatterjee, A., and Varshney, L. R. (2023). Dynamic Resource Allocation to Minimize Concave Costs of Shortfalls. *IEEE Control Systems Letters* 7, 3633–3638. https://arxiv.org/abs/2312.00896
