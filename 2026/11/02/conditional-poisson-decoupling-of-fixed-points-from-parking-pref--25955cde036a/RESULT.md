# Conditional Poisson decoupling of fixed points from parking-preference multiplicities

## Finding
Let \(\pi=(\pi_1,\ldots,\pi_n)\) be a uniform classical parking function. Its fixed-preference count \(F_n=\#\{i:\pi_i=i\}\) becomes asymptotically Poisson with mean one **even after the entire labelled preference-multiplicity vector is revealed**. Writing \(c_j=\#\{i:\pi_i=j\}\), and \(\mathcal H_n=\sigma(c_1,\ldots,c_n)\), the quantitative mode of convergence is
\[
\mathbb E\,d_{\mathrm{TV}}\bigl(\mathcal L(F_n\mid\mathcal H_n),\operatorname{Pois}(1)\bigr)\longrightarrow0.
\]
In particular, uniformly over all histogram-measurable events \(A_n\) and subsets \(B_n\subseteq\mathbb Z_{\ge0}\),
\[
\left|\Pr(A_n,F_n\in B_n)-\Pr(A_n)\Pr(\operatorname{Pois}(1)\in B_n)\right|\longrightarrow0.
\]
This is conditional decorrelation from an increasing-dimensional statistic, not only convergence of one fixed finite-dimensional vector.

## Assumptions and scope
For each integer \(n\ge2\), sample uniformly from the \((n+1)^{n-1}\) sequences \(\pi\in\{1,\ldots,n\}^n\) for which all cars successfully park by moving right from their preferred space. The multiplicities \(c_j\) count preferred spaces, **not** final parking positions. Conditional laws are regular discrete conditional distributions. The elementary symmetric polynomial \(e_r(c)\) is the sum of products of \(r\) distinct entries, and \((z)_r=z(z-1)\cdots(z-r+1)\). Total-variation distance is the supremum over all measurable subsets of the nonnegative integers.

## Proof
**Step 1: exact factorial moments under the complete frequency vector.** The parking-function condition depends only on the multiset of preference values; therefore, given \((c_1,\ldots,c_n)\), every word realizing those counts is equally likely. For pairwise distinct positions \(i_1,\ldots,i_r\), the chance that \(\pi_{i_t}=i_t\) simultaneously for all \(t\) is \(\prod_t c_{i_t}/(n)_r\). Summing over all ordered distinct position tuples proves, for all integers \(0\le r\le n\),
\[
\mathbb E[(F_n)_r\mid\mathcal H_n]=\frac{r!e_r(c_1,\ldots,c_n)}{(n)_r}.
\]
Since \(\sum_jc_j=n\), this gives \(\mathbb E[F_n\mid\mathcal H_n]=1\) and, for \(n\ge2\),
\[
\operatorname{Var}(F_n\mid\mathcal H_n)=\frac{n^2-\sum_j c_j^2}{n(n-1)}=1-\frac{\sum_jc_j(c_j-1)}{n(n-1)}.
\]

**Step 2: controlling repeated preferences.** Pollak's circular parking argument places \(n\) independent preferences in \(n+1\) cyclic spaces and rotates each preference vector by its unique empty final space to obtain a classical parking function. Each rotation orbit has exactly \(n+1\) members and exactly one canonical parking function. Every quantity invariant under cyclic relabelling of preferred spaces therefore has the same distribution in this circular model and in the uniform parking-function model (with one extra zero-count space added). In particular, if
\[
J_n=\sum_{j=1}^n\binom{c_j}{2},
\]
then pairwise collision counting gives \(\mathbb EJ_n=\binom n2/(n+1)\). Thus
\[
\mathbb E\sum_{j=1}^n c_j^2=n+\frac{n(n-1)}{n+1}<2n,
\qquad
\frac{\sum_jc_j^2}{n^2}\xrightarrow{\Pr}0.
\]
The final implication is Markov's inequality and needs no maximum-frequency estimate.

**Step 3: asymptotically Poisson conditional laws.** For a deterministic count vector \(c\) with \(\sum_jc_j=n\), draw \(r\) independent indices with probabilities \(c_j/n\). The chance that these indices are all different is precisely \(r!e_r(c)/n^r\). A union bound over index pairs yields
\[
0\le1-\frac{r!e_r(c)}{n^r}\le\binom r2\frac{\sum_jc_j^2}{n^2}.
\]
Together with \((n)_r/n^r\to1\), Step 2 implies that every fixed conditional factorial moment of \(F_n\) converges in probability to one, the corresponding factorial moment of \(\operatorname{Pois}(1)\). For deterministic sequences of multiplicity vectors on which \(\sum_jc_j^2/n^2\to0\), these bounds give convergence of all ordinary moments to those of \(\operatorname{Pois}(1)\). The Poisson law is moment-determinate; conditional mean one supplies tightness. Therefore the conditional laws converge weakly to \(\operatorname{Pois}(1)\), and on the countable state space of nonnegative integers this implies convergence in total variation. Applying the subsequence criterion to the random multiplicity vectors proves that the random conditional total-variation distance converges to zero in probability. Its bound by one upgrades this to convergence in expectation.

**Step 4: uniform independence.** For every \(A_n\in\mathcal H_n\) and \(B_n\subseteq\mathbb Z_{\ge0}\), condition on \(\mathcal H_n\) and bound the resulting difference by the expected conditional total-variation distance. Taking the supremum proves the asserted asymptotic factorization, including data-dependent histogram events.

## Verification
The accompanying standard-library-only `CHECK.py` enumerates every uniform parking function at sizes \(2\le n\le6\), independently enumerates every circular preference vector on \(n+1\) spaces, and checks the circular histogram law and exact conditional factorial-moment identities for \(0\le r\le\min(4,n)\). The delivered program passed 976 exact assertions. These are finite consistency tests; the unrestricted conditional-convergence theorem follows from the preceding proof.

## Relationship to prior work
Diaconis and Hicks (2016), *Probabilizing Parking Functions*, give Pollak's circular representation and identify the occupancy-frequency species distribution and classical occupancy asymptotics. Paguyo (2022), *Cycle structure of random parking functions*, establishes marginal Poisson limits for short cycle counts, including fixed points. Rubey and Yin (2025), *Fixed points and cycles of parking functions*, derive the exact finite marginal fixed-point distribution. The assertion here is different: uniform total-variation decoupling of fixed points from the **entire labelled frequency vector**, not a marginal distribution or a fixed finite tuple of occupancy counts. Stark (2026) studies matches to sorted multiset target words and has a different target-position convention; it does not directly state this conditional parking-function assertion. Pollak's bijection and the underlying marginal results are not claimed as new.

## Limitations
Only uniformly sampled classical parking functions are treated, and only the fixed-preference statistic \(\#\{i:\pi_i=i\}\). No finite-size total-variation convergence rate is claimed. The proof is a direct probabilistic consequence of exchangeability, a classical circular bijection and the elementary moment method; priority for this particular strong conditional formulation is not independently established. A relevant 2025 paper's full text was inaccessible during the comparison, although its reported theorem concerns the finite marginal law. No independent validation has been performed.

## References
1. Persi Diaconis and Angela Hicks, *Probabilizing Parking Functions*, arXiv:1611.09821, first submitted 2016-11-29. https://arxiv.org/abs/1611.09821
2. J. E. Paguyo, *Cycle structure of random parking functions*, arXiv:2202.08829, first submitted 2022-02-17. https://arxiv.org/abs/2202.08829
3. Martin Rubey and Mei Yin, *Fixed points and cycles of parking functions*, *Enumerative Combinatorics and Applications* 5 (2025), S2R10. https://doi.org/10.54550/ECA2025V5S2R10
4. Dudley Stark, *Poisson approximations of the number of fixed points in random multiset permutations*, arXiv:2608.00710, first submitted 2026-08-01. https://arxiv.org/abs/2608.00710
