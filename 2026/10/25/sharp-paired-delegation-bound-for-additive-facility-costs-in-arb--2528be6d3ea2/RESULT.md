# Sharp paired-delegation bound for additive facility costs in arbitrary metrics

## Finding

**Theorem.** Let \(k\ge2\) be an integer, \((X,d)\) a metric space, and \(x_1,\dots,x_{2k}\in X\) positions of \(2k\) *labeled* agents, with repeated positions permitted. For every \(k\)-subset \(S\) of agent indices set
\[
C(S)=\sum_{j\in S}\sum_{i=1}^{2k}d(x_i,x_j),\qquad C_*=\min_{|T|=k}C(T).
\]
Then, for every such \(S\),
\[
\boxed{C(S)\le\left(3-\frac2k\right)C_*.}
\]
The coefficient is optimal for each \(k\). In particular, partition the agents into \(k\) fixed pairs, locally nominate exactly one agent from each pair, and build all \(k\) facilities at the nominated agent locations. Every deterministic local-nomination rule (and, in fact, every feasible choice of \(k\) agent locations) satisfies this inequality. For every deterministic local-nomination rule the supremal approximation ratio, on line instances with \(C_*>0\), is exactly \(3-2/k\).

The lower-bound instance is the one already identified in Theorem 6.2 of Deligkas, Kanellopoulos, and Voudouris (2026). The matching upper bound, valid for *any* nominated set and *any* metric, is the additional result here.

## Assumptions and scope

All agents contribute equally to social cost, and every agent pays the **sum** of distances to every opened facility, not distance to the nearest or farthest facility. There are exactly \(2k\) labeled agents. A feasible selection contains \(k\) distinct **agent indices**; two selected agents at the same point represent two colocated facilities, as permitted by the motivating model. Distances satisfy symmetry, nonnegativity, zero diagonal, and the triangle inequality. When \(C_*=0\), the cost inequality still holds but the approximation ratio \(C(S)/C_*\) is not defined. The two-stage interpretation requires exactly \(k\) groups, each of size two, and one nominated representative per group. Determinism and locality are required only to assert the rule-by-rule sharpness construction; they are not needed for the universal upper bound. No incentive claim is made for an arbitrary nomination rule.

## Proof

**A balanced-partition metric lemma.** Let \(A\) and \(B\) partition the \(2k\) agent indices with \(|A|=|B|=k\). Define \(D_A=\sum_{\{i,j\}\subseteq A}d(x_i,x_j)\) and \(D_B\) analogously, each unordered pair counted once; put \(H=\sum_{i\in A,j\in B}d(x_i,x_j)\). For any distinct \(i,j\in A\) and any \(t\in B\), the triangle inequality gives \(d(x_i,x_j)\le d(x_i,x_t)+d(x_t,x_j)\). Summing over all such pairs and over the \(k\) choices of \(t\) gives
\[
kD_A\le(k-1)H.
\]
Indeed, each cross pair \((i,t)\) appears exactly \(k-1\) times on the right. The same argument applies with \(A,B\) swapped. Since the social cost counts both orientations within the selected half,
\[
C(A)=2D_A+H\le\left(3-\frac2k\right)H,
\qquad C(B)=2D_B+H\ge H.
\]
Thus **every equal-cardinality partition** satisfies
\[
C(A)\le\left(3-\frac2k\right)C(B).
\]

**Universal guarantee.** Let \(T\) attain \(C_*=C(T)\), and let \(U\) be its complement. By the balanced-partition lemma, \(C(U)\le(3-2/k)C(T)\). More directly, the lemma applied to each output \(S\) and its complement does *not* by itself compare \(S\) to \(T\) when the halves overlap. Instead use separability: define the individual location score \(h_j=\sum_i d(x_i,x_j)\), so \(C(S)=\sum_{j\in S}h_j\). Because \(T\) minimizes this sum, \(T\) may be chosen as the \(k\) indices with smallest scores. Its complement \(U\) then contains the \(k\) largest scores; hence \(C(S)\le C(U)\) for **every** size-\(k\) choice \(S\). Chaining the inequalities establishes the theorem.

**Sharpness for arbitrary selections.** Put \(2k-1\) labeled agents at location \(0\) and one agent at \(1\). Any \(k\) indices at \(0\) have cost \(C_*=k\); a set containing the unique outlier and \(k-1\) zero-indices has cost \((2k-1)+(k-1)=3k-2\), and attains the ratio.

**Rule-by-rule paired-delegation sharpness.** Take one pair with agent locations \(0\) and \(1\). Since its nomination is local and deterministic, it chooses one endpoint. Populate every remaining pair with two agents at the **other** endpoint. The nomination from the first pair is now the unique selected outlier, while the other \(k-1\) nominations all lie at the common endpoint, producing exactly the sharp configuration above (up to exchanging the endpoint labels). This proves a lower bound for every local rule, without supposing incentive compatibility. Combined with the upper bound it gives its exact worst-case ratio. All examples have \(C_*=k>0\).

## Verification

The file `verify.py` independently recomputes distance matrices, all \(k\)-subsets, balanced-partition triangle inequalities, and pairwise local choices for every integer-line profile on \(2k\) labeled agents over \(\{0,1,2\}\) for \(k=2,3,4\), and for four-point Manhattan square profiles at \(k=2,3\). It checks the exact sharp examples for \(2\le k\le100\) using rational arithmetic. Executing `python3 verify.py` passed **702,815 exact assertions**. These finite tests corroborate but do not replace the triangle-inequality proof for arbitrary metrics and all \(k\).

## Relationship to prior work

Deligkas, Kanellopoulos, and Voudouris (2026, arXiv:2601.15258) introduce the two-stage distributed agent-constrained setting. Their Theorem 6.1 bounds a specific strategyproof mechanism in the general \(m\ge k\) group model by \(3+2/k\) for \(k\ge3\); their Theorem 6.2 establishes the lower bound \(3-2/k\) using precisely a \(k\)-pair configuration. The present proof provides a matching upper bound on that **restricted but natural pair-size subfamily** and shows that neither line geometry nor a particular representative-selection rule is needed. It does not resolve the general \(m\ge k\) gap. Deligkas, Lotfi, and Voudouris (2025) study the centralized agent-constrained setting, without independently nominated pair representatives; that work does not furnish the distributed, paired-regime guarantee. Other cited distributed metric-voting and facility-location work concerns distinct aggregation models.

## Limitations

The result requires exactly twice as many equally weighted agents as facilities and the sum-over-all-facilities objective. Larger groups, fewer facilities than groups, unequal weights, nearest-facility costs, and randomized policies' *best possible* expected ratios are outside the claim. The proof uses the standard triangle inequality; the novel scope is the exact, quantitatively sharp and rule-independent characterization of the paired-delegation case. The pre-existing lower-bound example is not presented as a new discovery. No independent scientific audit has been performed, and overlap in unindexed literature remains possible.

## References

1. A. Deligkas, P. Kanellopoulos, A. A. Voudouris, *Distributed Agent-Constrained Truthful Facility Location*, arXiv:2601.15258, first submitted 2026-01-21, Sections 2 and 6, especially Theorems 6.1–6.2. https://arxiv.org/abs/2601.15258
2. A. Deligkas, M. Lotfi, A. A. Voudouris, *Agent-constrained truthful facility location games*, Journal of Combinatorial Optimization 49 (2025), article 24, https://pmc.ncbi.nlm.nih.gov/articles/PMC11906575/.
3. H. Chan, A. Filos-Ratsikas, B. Li, M. Li, C. Wang, *Mechanism Design for Facility Location Problems: A Survey*, IJCAI 2021, https://livrepository.liverpool.ac.uk/3127550/.
