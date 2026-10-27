# Sharp imbalance ordering of pairwise component-count association in random graphs

## Finding
For a finite Erdős–Rényi graph \(G(n,p)\), the critical probability at which two component-size counts change the sign of their *second factorial cumulant* is a strictly Schur-convex function of the two component sizes at fixed total size. Equivalently, for every integer \(n\ge 2\), \(1\le a,b\), \(a+b\le n\), define
\[
\pi_n(a,b)=1-\left(\frac{(n-a)!(n-b)!}{n!(n-a-b)!}\right)^{1/(ab)}.
\]
Let \(N_a\) denote the number of connected components of order \(a\), and set
\[
K_{a,b}=\mathbb E[N_a(N_b-\mathbf1_{\{a=b\}})]-\mathbb E[N_a]\,\mathbb E[N_b].
\]
For \(0<p<1\), \(K_{a,b}<0\), \(=0\), or \(>0\), according as \(p<\pi_n(a,b)\), \(p=\pi_n(a,b)\), or \(p>\pi_n(a,b)\). For distinct sizes this is the ordinary covariance; for equal sizes it is the factorial rather than ordinary covariance.

The genuinely comparative assertion is: for any fixed \(4\le s\le n\) and integers \(1\le a<\lfloor s/2\rfloor\),
\[
\pi_n(a,s-a)>\pi_n(a+1,s-a-1).
\]
Thus among all size pairs with total \(s\), the threshold is uniquely smallest for the most balanced unordered pair and uniquely largest for \(\{1,s-1\}\). Over all feasible pairs the smallest threshold is \(1/n\) at \(\{1,1\}\), and the largest is \(1-n^{-1/(n-1)}\) at \(\{1,n-1\}\) (distinct extremes for \(n\ge3\)). If \(a+b>n\), the factorial cumulant is strictly negative.

In particular, for every \(n\ge5\) there is a nonempty open interval of probabilities with
\[
\operatorname{Cov}(N_2,N_3)>0>\operatorname{Cov}(N_1,N_4)
\]
within the *same random graph*, even though both pairs prescribe five vertices in total. For \(n=5\), \(p=13/40\) is one such probability.

## Assumptions and scope
The graph has labeled vertex set \([n]\). Every unordered edge is independently present with common probability \(p\in(0,1)\). All counts include non-induced connected components of the random graph in the usual sense: their vertex sets induce connected subgraphs with every edge to the complement absent. The theorem concerns the second *factorial* cumulant \(K_{a,b}\), which differs from \(\operatorname{Var}(N_a)\) when \(a=b\). The order comparison does not assert that ordinary variances change sign. No asymptotic assumptions are imposed.

## Proof
**Step 1 (exact sign reduction, from standard tuple enumeration).** Let \(u_m(p)\) be the probability that \(G(m,p)\) is connected. It is strictly positive for \(m\ge1\), \(0<p<1\). Writing \(q=1-p\), the one-component expectation is
\[
\mu_a=\binom na u_a(p)q^{a(n-a)}.
\]
Fix ordered disjoint vertex sets of sizes \(a,b\). For both sets to be distinct components, the two internal graphs must be connected, while each outgoing edge is absent. Exactly \(ab\) cross-edges were counted twice in the product of the two single-component probabilities. Therefore
\[
\mathbb E[N_a(N_b-\mathbf1_{\{a=b\}})]
=\binom na\binom{n-a}b u_a(p)u_b(p)
q^{a(n-a)+b(n-b)-ab}.
\]
For \(a+b\le n\), division by \(\mu_a\mu_b\) gives
\[
\frac{K_{a,b}}{\mu_a\mu_b}=R_n(a,b)q^{-ab}-1,
\qquad R_n(a,b)=\frac{(n-a)!(n-b)!}{n!(n-a-b)!}.
\]
The strict sign trichotomy follows because the expression increases strictly with \(p\) and crosses zero at \(\pi_n(a,b)\). When \(a+b>n\), two such disjoint components cannot exist, so \(K_{a,b}=-\mu_a\mu_b<0\).

**Step 2 (positive Laplace representation).** Set \(\tau_n(a,b)=-\log R_n(a,b)/(ab)\), so \(\pi_n=1-e^{-\tau_n}\). Telescoping the falling factorials yields
\[
\tau_n(a,b)=\frac1{ab}\sum_{i=0}^{a-1}\sum_{j=0}^{b-1}
\log\frac{n-i-j}{n-i-j-1}.
\]
Define the increasing sequence \(g_n(k)=\log((n-k)/(n-k-1))\) for \(0\le k\le n-2\). Its positive exponential integral is
\[
 g_n(k)=\int_0^\infty\frac{e^{-(n-1)t}(1-e^{-t})}{t}\,e^{kt}\,dt.
\]
For \(m\ge1\), set \(F_m(t)=m^{-1}\sum_{i=0}^{m-1}e^{it}=(e^{mt}-1)/(m(e^t-1))\). Interchanging a finite sum and a positive integral gives
\[
\tau_n(a,b)=\int_0^\infty\frac{e^{-(n-1)t}(1-e^{-t})}{t}
F_a(t)F_b(t)\,dt.
\]
The representation is finite for \(a+b\le n\), because the largest exponential power in the finite product is \(e^{(a+b-2)t}\).

**Step 3 (strict imbalance ordering).** For each fixed \(t>0\), let
\[
 h_t(x)=\log\frac{e^{tx}-1}{x(e^t-1)},\qquad x>0.
\]
Direct differentiation gives
\[
 h_t''(x)=\frac1{x^2}-\frac{t^2e^{tx}}{(e^{tx}-1)^2}>0,
\]
where strictness follows from \(2\sinh(tx/2)>tx\). For any integers \(2\le a\le b\), strict convexity implies
\[
 h_t(a-1)+h_t(b+1)>h_t(a)+h_t(b).
\]
Exponentiating shows \(F_{a-1}(t)F_{b+1}(t)>F_a(t)F_b(t)\). Integrating against the strictly positive weight in Step 2 proves \(\tau_n(a-1,b+1)>\tau_n(a,b)\) whenever \(a+b\le n\). As \(\pi_n\) increases strictly with \(\tau_n\), this proves strict Schur-convexity and both fixed-total equality cases.

**Step 4 (global endpoints and simultaneous opposing covariances).** Because \(g_n\) is strictly increasing, enlarging either independent discrete uniform index in the finite average in Step 2 increases \(\tau_n\) strictly (compare the old mean with the newly added largest index). Hence its global minimum occurs at \(a=b=1\) and its maximum, by fixed-total imbalance and monotonicity in the total, at \(\{a,b\}=\{1,n-1\}\). The first value is \(\tau_n(1,1)=\log(n/(n-1))\), whereas
\[
\tau_n(1,n-1)=\frac1{n-1}\sum_{j=0}^{n-2}g_n(j)=\frac{\log n}{n-1}.
\]
Applying \(\pi_n=1-e^{-\tau_n}\) gives the claimed bounds. For \(n\ge5\), the strict comparison \(\pi_n(2,3)<\pi_n(1,4)\) produces an open interval of \(p\) where their ordinary covariances have opposite signs; these sizes are all distinct, so no diagonal correction is involved. At \(n=5,p=13/40\), exact rational comparison verifies the displayed example. This completes the proof.

## Verification
The accompanying standalone Python program `verify_component_size_phase.py` uses exact rational arithmetic. It enumerates every labeled edge state for orders \(2\le n\le6\) at three rational probabilities and independently computes second factorial moments, comparing them with the formula derived in Step 1. It checks strict ordering of all feasible pairs for \(3\le n\le80\) by comparing integer powers of exact rational thresholds; and it verifies the opposite-sign example at \(n=5,p=13/40\). These finite checks confirm implementation and small cases but do not establish the unrestricted theorem, which follows from Steps 1–4.

## Relationship to prior work
The component enumeration in Step 1 is **not claimed as new**. In particular, Sun's Proposition 3.2 (arXiv:2608.04799, 2026) gives exact ordered factorial moments with prescribed component sizes and surpluses, from which this two-component count formula follows by summing surplus labels. The contribution assessed here is the strict size-imbalance ordering of every pairwise association threshold, together with its complete finite-size extremes and coexistence of positive and negative covariances between distinct size counts. Earlier work on the isolate-versus-component count provides one boundary subfamily but not a proof of strict imbalance ordering across all pairs. De Ambroggio and Roberts (arXiv:2101.05358) study largest-component deviations rather than this sign-ordering problem; Andreis, König and Patterson (arXiv:1901.01876) study large deviations of the full cluster-size spectrum. No priority conclusion is drawn solely from the absence of matching phrases in these sources.

## Limitations
The result applies to homogeneous independent-edge \(G(n,p)\) and does not establish analogous orderings for inhomogeneous, fixed-edge-count, or dependent random-graph models. The diagonal statistic is the factorial cumulant, not the ordinary variance. Historical-priority uncertainty remains: an equivalent strict Schur-convexity theorem for normalized disjoint-subset probabilities may exist in classical combinatorics or probability literature. Independent external audit has not been performed.

## References
1. De Ambroggio and Roberts, *Unusually large components in near-critical Erdős–Rényi graphs via ballot theorems*, arXiv:2101.05358 (first public 2021-01-13), DOI: 10.1017/S0963548321000584.
2. Sun, *Uniform High Order Factorial Moment Bounds for the Critical Erdős–Rényi Component Process*, arXiv:2608.04799 (2026), Proposition 3.2.
3. Andreis, König and Patterson, *A large-deviations principle for all the cluster sizes of a sparse Erdős–Rényi graph*, arXiv:1901.01876 (2019).
