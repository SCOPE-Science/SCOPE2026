# A one-crossing singleton–doubleton covariance law in dominant-species rarefaction

## Finding

Fix integers \(n\ge3\) and \(r\ge n-1\). A finite ecological census consists of one dominant species with \(B\ge2\) individually labeled members and \(r\) further species, each represented by exactly one labeled individual. Draw a uniform size-\(n\) subset without replacement from its \(N=B+r\) individuals. Let \(F_1\) and \(F_2\) be the numbers of species observed exactly once and exactly twice in the draw. Define

\[
p_j(B,r,n)=\frac{\binom Bj\binom r{n-j}}{\binom{B+r}n},\qquad
T_{n,r}(B)=\frac{nB}{B+r}-2-p_1(B,r,n).
\]

Binomial coefficients with inadmissible arguments are zero. Then

\[
\boxed{\operatorname{Cov}(F_1,F_2)=p_2(B,r,n)T_{n,r}(B).}
\]

For every fixed \(n\ge3\) and \(r\ge n-1\), the real-valued sequence \(T_{n,r}(B)\) is *strictly increasing* in positive integer \(B\). It is negative at \(B=2\) and positive for all sufficiently large \(B\). Because \(p_2>0\), the covariance is negative before a unique sign transition, may be zero at one integer abundance, and is positive afterward. In particular, the first strictly positive value

\[
B^+_{n,r}=\min\{B\ge2:\operatorname{Cov}(F_1,F_2)>0\}
\]

exists and is characterized exactly by the displayed rational inequality \(T_{n,r}(B)>0\).

For fixed \(n\ge3\), as the number \(r\) of singleton species grows,

\[
\boxed{\frac{B^+_{n,r}}r\longrightarrow\frac{q_n}{1-q_n}},\qquad
nq_n\bigl[1-(1-q_n)^{n-1}\bigr]=2,
\]

where the latter equation has exactly one solution \(q_n\in(0,1)\). Increasing survey depth makes the limiting *dominant fraction* \(q_n\) strictly decrease. Moreover, \(nq_n\) tends to the unique positive solution \(c\) of \(c(1-e^{-c})=2\), numerically \(c\approx2.238645834606\).

Sample depth two is the sharp boundary for this sign-switch phenomenon: for *every* community, a uniform two-individual sample satisfies \(\operatorname{Cov}(F_1,F_2)=-2\operatorname{Var}(F_2)\le0\). At depth three and \(r=2\), the census abundances \((B,1,1)\) yield covariance \(-1/2\) for \(B=2\), exactly zero for \(B=5\), and \(15/196\) for \(B=6\). Thus three draws and four census individuals are already sufficient to realize negative dependence; the same sample depth permits positive dependence with a larger dominant population.

## Assumptions and scope

The complete, known census has one species with abundance \(B\) and \(r\) species with abundance one. Individuals are distinguishable for sampling; all \(\binom Nn\) subsets are equiprobable. Sampling is without replacement and detects the species identity of every sampled individual perfectly. The theorem's strict sign-transition statement assumes \(n\ge3\), \(r\ge n-1\), \(B\ge2\); the covariance identity itself holds for any valid \(n\le B+r\) when the quantities are defined. \(F_1,F_2\) are **frequency-of-frequency counts**, not numbers of separate surveys or species detected at least once. No stochastic abundance model is imposed on the fixed census.

## Proof

**1. Reduction and covariance identity.** Let \(M\) be the number of sampled individuals belonging to the one dominant species. Hypergeometric counting gives \(\Pr(M=j)=p_j(B,r,n)\), \(\mathbb E M=nB/(B+r)\). Since each other species is a singleton in the census, for each draw

\[
F_1=n-M+\mathbf1_{\{M=1\}},\qquad F_2=\mathbf1_{\{M=2\}}.
\]

The second variable is Bernoulli with success probability \(p_2\), and on its success event \(F_1=n-2\). Consequently

\[
\operatorname{Cov}(F_1,F_2)
=p_2\bigl((n-2)-\mathbb EF_1\bigr)
=p_2\bigl(\mathbb EM-2-\Pr(M=1)\bigr).
\]

This proves the exact expression without assuming independence between species counts.

**2. Strict abundance monotonicity.** Set \(g(m)=m-\mathbf1_{\{m=1\}}\) on nonnegative integers. Its values are \(g(0)=g(1)=0\), followed by \(g(m)=m\) for \(m\ge2\); hence \(g\) is nondecreasing, and strictly increases from \(1\) to \(2\). The sign factor is \(T_{n,r}(B)=\mathbb E[g(M)]-2\).

Couple the uniform size-\(n\) samples from censuses with \(B\) and \(B+1\) dominant individuals as follows. Select a uniform size-\(n\) subset from the larger census. If its new dominant individual is absent, retain that subset as the smaller-census sample. If the new individual is present, remove it and replace it by one uniformly selected old individual not already selected. The resulting size-\(n\) subset is uniform in the old census: every particular old size-\(n\) subset receives total probability

\[
\frac{1+n/(B+r-n+1)}{\binom{B+r+1}n}=\frac1{\binom{B+r}n}.
\]

Under this coupling \(M_B\le M_{B+1}\). The inequality in \(\mathbb E[g(M)]\) is strict: there is positive probability that the larger sample contains both the added dominant individual and exactly one old dominant individual, plus \(n-2\) singleton individuals, and the replacement chosen from the remaining singleton species. Such an event has positive probability because \(B\ge1\) and \(r\ge n-1\); on it \(M_{B+1}=2\), \(M_B=1\), and \(g\) increases by two. Therefore \(T_{n,r}(B+1)>T_{n,r}(B)\).

**3. Opposite endpoint signs.** At \(B=2\), \(M\le2\), so \(g(M)\le2\). The event \(M=1\) has positive probability for \(r\ge n-1\), and \(g(1)=0\); thus \(T_{n,r}(2)<0\). With \(r,n\) fixed and \(B\to\infty\), all \(n\) sampled individuals are dominant with probability tending to one. Hence \(T_{n,r}(B)\to g(n)-2=n-2>0\). Since \(p_2>0\) for \(B\ge2\), the sign conclusions follow. The covariance itself need not increase monotonically; only the sign-governing factor does.

**4. Rare-tail asymptotics.** If \(r\to\infty\) with \(n\) fixed and \(B/r\to b\in(0,\infty)\), then \(M\) converges in distribution to a binomial variable with success probability \(q=b/(b+1)\). The sign factor therefore converges to

\[
H_n(q)=nq\bigl[1-(1-q)^{n-1}\bigr]-2.
\]

This function is strictly increasing on \((0,1)\), since

\[
H_n'(q)=n\bigl[1-(1-q)^{n-1}+(n-1)q(1-q)^{n-2}\bigr]>0.
\]

Its endpoint values are \(-2\) and \(n-2>0\). Thus its unique zero \(q_n\) determines a unique \(b_n=q_n/(1-q_n)\). Evaluating the finite-population sign factor at \(B=\lfloor(b_n-\varepsilon)r\rfloor\) and \(B=\lceil(b_n+\varepsilon)r\rceil\), for any sufficiently small \(\varepsilon>0\), and using strict monotonicity brackets \(B^+_{n,r}/r\) between \(b_n-\varepsilon+o(1)\) and \(b_n+\varepsilon+o(1)\). This proves the first limit.

For fixed \(q\in(0,1)\), the quantity \(nq[1-(1-q)^{n-1}]\) strictly increases with \(n\), so its root \(q_n\) strictly decreases with \(n\). Also \(2<nq_n<3\) for all \(n\ge3\): the lower inequality is immediate from the root equation; for the upper one, evaluate the left side at \(q=3/n\) (at \(n=3\), use the endpoint), observing \((1-3/n)^{n-1}\le\exp[-3(n-1)/n]\le e^{-2}\), hence the value exceeds \(3(1-e^{-2})>2\). Consequently \(q_n\to0\), the bounded sequence \(nq_n\) has limit points, and every such limit point solves \(c(1-e^{-c})=2\). Strict monotonicity of \(c(1-e^{-c})\) on positive \(c\) gives the unique limit.

**5. Sharp two-draw comparison and rational examples.** Every two-individual sample has either two singleton species or one doubleton species, so \(F_1+2F_2=2\) identically and \(\operatorname{Cov}(F_1,F_2)=-2\operatorname{Var}(F_2)\). At \((n,r)=(3,2)\), substituting \(B=2,5,6\) in the hypergeometric formula gives respectively \(-1/2,0,15/196\). This also confirms a possible exact integer equality at the unique sign change.

## Verification

A standalone standard-library script `verify.py` implements the two independent routes to \(\operatorname{Cov}(F_1,F_2)\): (i) the closed rational hypergeometric formula and (ii) an exhaustive enumeration of uniformly sampled **labeled individual subsets**. For 155 small admissible parameter triples the two exact fractions agree, including negative, zero, and positive cases. It additionally checks 43,608 strictly positive adjacent differences of \(T_{n,r}(B)\) across a finite grid, reproduces exact examples and brackets the limiting binomial roots numerically. The saved `certificate.json` is deterministic and can be reproduced with `python verify.py`. The finite computations are not a substitute for the unlimited-integer and asymptotic proofs above.

## Relationship to prior work

Good–Turing and Chao richness/coverage methods motivate attention to \(F_1,F_2\). Heck, van Belle and Simberloff (1975) studied finite-sample rarefaction richness moments; Pan, Chao and Foissner (2009) derived species-richness bounds and observed that sampling without replacement requires generalized hypergeometric rather than multinomial frequency models; Chao and Jost (2012) developed analytic coverage-based rarefaction using singleton counts and doubleton-based extrapolation. Those accessible results do not state the exact one-dominant-species \(\operatorname{Cov}(F_1,F_2)\) sign transition or the sample-effort scaling proved here. Related published mathematical records on covariance of richness with frequency counts in uniform occupancy, and on covariance of successive discoveries, address different random variables and sampling models. The present result is a distinct finite-population within-sample covariance comparison, not a reformulation of the variance of observed richness.

## Limitations

This is a stylized dominant-plus-singletons census and assumes uniform individual sampling, perfect identification, and no replacement. It establishes population-moment behavior, not finite-sample confidence-interval coverage or estimator bias. Although \(F_1,F_2\) appear in richness/coverage estimators, their covariance alone does not determine the sampling variance of a nonlinear estimator. It does not claim a universal one-crossing law for arbitrary species-abundance profiles. Full-text access was unavailable for the 1975 finite-rarefaction paper; undiscovered equivalent work on hypergeometric frequency counts remains a bibliographic risk. Independent scientific validation has not been performed.

## References

1. Heck, K. L., Jr., G. van Belle, and D. Simberloff (1975), “Explicit Calculation of the Rarefaction Diversity Measurement and the Determination of Sufficient Sample Size,” *Ecology* 56:1459–1461. Published 1975-10-01. DOI: https://doi.org/10.2307/1934716 (accessible abstract).
2. Pan, H.-Y., A. Chao, and W. Foissner (2009), “A Nonparametric Lower Bound for the Number of Species Shared by Multiple Communities,” *Journal of Agricultural, Biological, and Environmental Statistics*. Open full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC2899312/ (sections 2 and 7).
3. Chao, A., and L. Jost (2012), “Coverage-based rarefaction and extrapolation: standardizing samples by completeness rather than size,” *Ecology* 93:2533–2547. Published 2012-12-01. DOI: https://doi.org/10.1890/11-1952.1 (accessible full text).
