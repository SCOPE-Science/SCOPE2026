# Singleton detection stochastically enriches species-richness tails under random sampling

## Finding

Fix a species in a finite community. Under either uniform sampling without replacement from a known finite census or independent categorical sampling with fixed species probabilities, conditioning on **exactly one sampled individual of that species** can only increase the entire upper-tail distribution of observed species richness. This holds for every species, every sample size, every admissible abundance vector, and every upper-tail threshold. Consequently, observed richness has nonnegative covariance with the sample singleton count, and so does any nondecreasing function of observed richness.

More precisely, let \(K\) be the number of distinct species in a size-\(m\) sample, let \(Y_j\) be the sample count of fixed species \(j\), and let \(F_1=\sum_j\mathbf 1_{\{Y_j=1\}}\). If \(\Pr(Y_j=1)>0\), then for every integer \(h\),
\[
\boxed{\Pr(K\ge h\mid Y_j=1)\ge\Pr(K\ge h).}
\tag{1}
\]
Indeed, the conditional law of \(K\) given \(Y_j=1\) first-order stochastically dominates its conditional law given **any** other feasible value of \(Y_j\). Thus, for every real-valued nondecreasing function \(\phi\) on the finite range of richness,
\[
\boxed{\operatorname{Cov}(\phi(K),\mathbf 1_{\{Y_j=1\}})\ge0,\qquad
\operatorname{Cov}(\phi(K),F_1)\ge0.}
\tag{2}
\]
When \(\mathbb E[F_1]>0\), the richness law reweighted by its number of singleton species first-order stochastically dominates the unweighted richness law:
\[
\frac{\mathbb E[F_1\mathbf 1_{\{K\ge h\}}]}{\mathbb E[F_1]}
\ge \Pr(K\ge h).
\tag{3}
\]

The frequency-one requirement is sharp for *universal positive covariance*. For every integer \(r\ge2\), at the same sample size \(m=r+1\), there exist finite community profiles with positive \(\operatorname{Cov}(K,\mathbf 1_{\{Y_j=r\}})\) and others with negative covariance. In particular:

* With two species each of abundance \(r+1\), tag one. Its covariance is
\[
\boxed{\operatorname{Cov}(K,\mathbf 1_{\{Y_j=r\}})
=\frac{2(r+1)^2}{\binom{2r+2}{r+1}^2}>0.}
\tag{4}
\]
* With a tagged species of abundance \(r\) and \(r+1\) further singleton species, the same covariance is strictly negative.

Equations (1)--(4), including the opposite-sign constructions for every \(r\ge2\), form one joint conditional-dependence theorem about species richness and exact-frequency counts.

## Assumptions and scope

**Finite-census scheme.** There are \(s\ge1\) labeled species with abundances \(a_i\ge1\), total \(N=\sum_i a_i\), and an unordered sample of \(m\) distinct individuals selected uniformly from the \(\binom Nm\) subsets, for any integer \(1\le m\le N\).

**Independent scheme.** There are \(s\ge1\) species with fixed probabilities \(p_i>0\), \(\sum_i p_i=1\), and exactly \(m\ge1\) independent categorical draws. Species \(j\) is fixed before sampling.

In both schemes, \(Y_i\) denotes the sample count of species \(i\), \(K=\sum_i\mathbf 1_{\{Y_i>0\}}\), and \(F_1=\sum_i\mathbf 1_{\{Y_i=1\}}\). Conditional assertions are made only when the conditioning event has positive probability. If it has zero probability, the corresponding singleton-indicator covariance is zero. The theorem concerns equally weighted species richness, not abundance-weighted diversity or imperfect detection.

## Proof

**Conditional composition.** Fix the tagged species \(j\), and write \(Y=Y_j\). For each integer \(t\ge0\) that is feasible among the other \(s-1\) species, define \(R_t\) as the number of other species observed in \(t\) draws. In the finite-census scheme the draws form a uniformly random \(t\)-subset of the \(N-a_j\) non-tagged individuals. In the independent scheme they are \(t\) independent draws from the other-species law \(p_i/(1-p_j)\). For the one-species case the value \(R_t=0\) is used whenever feasible.

Under either sampling scheme, conditional on \(Y=y\), the other-species sample has exactly this law with \(t=m-y\). Therefore
\[
K\mid(Y=y)\ \overset d=\ \mathbf 1_{\{y>0\}}+R_{m-y}.
\tag{5}
\]
For uniform sampling without replacement, this follows by dividing the number of size-\(m\) samples of tagged count \(y\) into the independent choice of \(y\) tagged and \(m-y\) non-tagged individuals. For independent sampling, it follows by conditioning on the number of tagged draws.

**One common nested coupling.** The sequence \((R_t)\) may be realized on a *single* probability space as richness from the first \(t\) draws in a uniformly random ordering of the non-tagged individuals (finite census), or the first \(t\) terms of an independent non-tagged draw sequence (independent scheme). Along each realization,
\[
0\le R_{t+1}-R_t\le1.
\tag{6}
\]
Suppose \(\Pr(Y=1)>0\). If \(y=0\) is feasible, (6) gives \(R_m\le1+R_{m-1}\). If \(y\ge2\) is feasible, monotonicity gives \(1+R_{m-y}\le1+R_{m-1}\). At \(y=1\) there is equality. Therefore on this coupling
\[
\mathbf 1_{\{y>0\}}+R_{m-y}\le1+R_{m-1}
\quad\text{for every feasible }y.
\tag{7}
\]
In the finite-census scheme, the availability of \(Y=1\) guarantees \(m-1\le N-a_j\), and if \(Y=0\) is feasible then \(m\le N-a_j\), so every nested sample in (7) is valid. In the independent scheme, all non-tagged sample lengths are valid when \(\Pr(Y=1)>0\).

By (5)--(7), for every threshold \(h\) and feasible \(y\),
\[
\Pr(K\ge h\mid Y=1)\ge\Pr(K\ge h\mid Y=y).
\tag{8}
\]
Averaging the right-hand side over \(Y\) proves (1). Integrating this first-order stochastic dominance against any nondecreasing \(\phi\) proves
\(\mathbb E[\phi(K)\mid Y=1]\ge\mathbb E[\phi(K)]\). Multiplying by \(\Pr(Y=1)\) proves the first part of (2); the zero-probability case is immediate. Summing over all species proves the second part. Setting \(\phi(K)=\mathbf 1_{\{K\ge h\}}\) yields (3).

**Sharpness across frequency levels.** Fix \(r\ge2\) and let \(m=r+1\). In the profile \((r+1,r+1)\), the richness equals two except when all \(m\) individuals sampled come from one species, in which case it equals one. Denote \(B=\binom{2r+2}{r+1}\). The two all-one-species samples give \(\mathbb E[K]=2-2/B\). For the tagged first species, \(\Pr(Y=r)=(r+1)^2/B\), and \(Y=r\) forces \(K=2\). Consequently
\[
\operatorname{Cov}(K,\mathbf 1_{\{Y=r\}})
=\Pr(Y=r)(2-\mathbb E[K])=2(r+1)^2/B^2>0.
\]
For the profile \((r,1,\ldots,1)\) with \(r+1\) singleton species, \(Y=r\) forces exactly two detected species, whereas every other feasible \(Y=y<r\) forces at least three. Both kinds of event have positive probability. Thus \(\mathbb E[K\mid Y=r]=2<\mathbb E[K]\), giving negative covariance. This proves the claimed sharp r-frequency contrast for all \(r\ge2\).

## Verification

The standalone Python file `verify.py` independently enumerates labeled-individual samples, constructs the exact joint distribution of tagged-species count and sample richness, and checks the stronger fixed-count dominance (8) at every attainable threshold. It exhausts all 96 integer abundance partitions through census size nine, all sample sizes, and every tagged species, using rational arithmetic. It also checks three heterogeneous independent species laws through seven draws by direct enumeration of all categorical sequences and checks both signs for every frequency \(r=2,\ldots,7\). In the verified execution, **12,127** exact stochastic-order inequalities were checked, all passed. The program reproduces the closed-form positive covariance (4), and the negative examples by exact enumeration.

The unrestricted statements follow from the explicit coupling proof (5)--(8), not from finite experiments. The proof does not require numerical approximations or computer-assisted infinite certification.

## Relationship to prior work

Gnedin, Hansen and Pitman (2007) study occupancy richness and counts of boxes with given frequencies, including moment and covariance formulas (their Section 2, especially equations (1)--(4)) and variance/large-sample theory. Their model is independent sampling from infinitely many categories. The inspected material does not assert tagged-singleton conditional first-order stochastic dominance, cover finite uniform-without-replacement census samples, or establish the opposite-sign frequency boundary.

Coddington and colleagues (2009) motivate interpreting observed singleton counts jointly with richness during ecological sampling and survey completeness assessment. Their empirical and resampling analysis does not present an exact conditional-order law.

Chao and Lin (2012) derive species-richness estimator bounds under sampling without replacement. The accessible abstract concerns estimator behavior, not conditional order; their complete technical article was not inspected, so exact coverage by that source remains an unresolved bibliographic risk.

The published result “A one-switch covariance law for occupancy richness and frequency counts” proves exact richness--frequency covariance signs in the **uniform independent-box model** and explicitly excludes conditional stochastic order and nonuniform laws from its claims. Its positive singleton covariance is a special consequence of (2) in that model. Conversely, (1)--(4) do not provide that work's complete higher-frequency sign-switch formula for uniform boxes. The present theorem supplies finite-census and heterogeneous-law generality, per-tag conditional dominance of every richness tail, and a sharp arbitrary-frequency loss of sign universality.

## Limitations

The result assumes exchangeable sampling of labeled individuals (finite-census scheme) or independent draws with fixed species probabilities (independent scheme). It is not an inference about a specific observed survey, nor a guarantee under spatial clustering, imperfect detection, selective collection, or time-varying abundances. No strict inequality is asserted in degenerate cases; the event \(Y_j=1\) may have zero probability. The sharpness contrast concerns the sign of covariance with a **tagged exact-frequency event** for each \(r\ge2\), not a sign classification for the full frequency count \(F_r\) for every community. Full coverage of older ecological-estimation and urn-model literature has not been established; independent bibliographic examination remains warranted.

## References

1. A. Gnedin, B. Hansen, J. Pitman, “Notes on the occupancy problem with infinitely many boxes: general asymptotics and power laws,” *Probability Surveys* 4 (2007), 146–171, arXiv:math/0701718, first publicly submitted 2007-01-24, https://arxiv.org/abs/math/0701718.
2. J. A. Coddington, I. Agnarsson, J. A. Miller, M. Kuntner, G. Hormiga, “Undersampling bias: the null hypothesis for singleton species in tropical arthropod surveys,” *Journal of Animal Ecology* 78 (2009), 573–584, first published 2009-03-31, DOI 10.1111/j.1365-2656.2009.01525.x.
3. A. Chao, C.-W. Lin, “Nonparametric lower bounds for species richness and shared species richness under sampling without replacement,” *Biometrics* 68 (2012), 912–921, published 2012-02-20, DOI 10.1111/j.1541-0420.2011.01739.x.
4. “A one-switch covariance law for occupancy richness and frequency counts,” publicly available result, 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-one-switch-covariance-law-for-occupancy-richness-and-frequency--93dddb2be813.
