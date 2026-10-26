# An exact insertion-budget criterion for stable directed trust games

## Finding

**Theorem (universal total balancedness, exactly characterized).** Fix a function \(F\) taking finite multisets of nonnegative real weights to nonnegative reals, with \(F(\varnothing)=0\). Form the directed-graph coalition game defined below, on any finite loopless weighted directed graph. The following statements are equivalent:

1. For every such graph and every nonempty vertex set \(S\), the restricted cooperative game on \(S\) has a nonempty core.
2. For every finite multiset \(U\) of nonnegative weights and \(b\ge0\),
\[
 F(U\uplus\{b\})\le F(U)+b.
\tag{1}
\]

When (1) holds, an explicit core allocation is available for **every** restricted game. When additionally \(F(\{b\})=b\) for every \(b\ge0\), the full-game core is the **singleton** given by the sum of incoming weights at each vertex. Operators satisfying both conditions include minimum, maximum, arithmetic mean, either median convention, and all fixed-quantile order statistics. If (1) fails, an explicit in-star with a two-player restricted subgame having empty core witnesses failure.

## Assumptions and scope

Take any nonempty finite vertex set \(N\) with at least two vertices and a loopless digraph \(E\subseteq N\times N\). Each arc \((i,j)\in E\) has weight \(a_{ij}\ge0\); absent arcs are **omitted** from the incoming multiset rather than counted as zeros. Repeated weights from different arcs count with multiplicity. For \(U\subseteq N\setminus\{j\}\), write \(B_j(U)\) for the multiset of weights \(a_{ij}\) with \(i\in U\) and \((i,j)\in E\). Define \(v(\varnothing)=0\), and for every coalition \(T\subseteq N\),
\[
 v(T)=\sum_{j\in T}\left(\sum_{\substack{i\in T\\(i,j)\in E}}a_{ij}+F\big(B_j(N\setminus T)\big)\right).
 \tag{2}
\]

The core of the restriction to \(S\) consists of vectors \(x\in\mathbb R^S\) with \(\sum_{j\in S}x_j=v(S)\) and \(\sum_{j\in T}x_j\ge v(T)\) for every \(T\subseteq S\). Here **restriction** means retaining the original worth \(v(T)\), including exposures to vertices of \(N\setminus S\), rather than recomputing on the induced graph. Total balancedness means that each such restriction has a nonempty core. There is no uniform upper bound on the nonnegative arc weights; the original trust-score setting \([0,1]\) is a contained special case.

## Proof

**Sufficiency and explicit restricted cores.** Assume (1). For a nonempty \(S\subseteq N\), define
\[
 x_j^S=\sum_{\substack{i\in S\\(i,j)\in E}}a_{ij}+F\big(B_j(N\setminus S)\big),\qquad j\in S.
 \tag{3}
\]

Summing (3) over \(j\in S\) gives exactly \(v(S)\), so efficiency holds. Fix any \(T\subseteq S\) and \(j\in T\), and put \(U_j=B_j(N\setminus S)\) and \(V_j=B_j(S\setminus T)\). Disjointness of the source vertex sets gives \(B_j(N\setminus T)=U_j\uplus V_j\). Iterating (1) once per member of \(V_j\) yields
\[
 F(U_j\uplus V_j)-F(U_j)\le\sum_{b\in V_j}b.
 \tag{4}
\]

Subtracting the \(j\)-contribution to \(v(T)\) from (3) gives exactly
\[
 \sum_{\substack{i\in S\setminus T\\(i,j)\in E}}a_{ij}+F(U_j)-F(U_j\uplus V_j)\ge0.
 \tag{5}
\]

Summing (5) over \(j\in T\) proves coalitional rationality. This works for all restrictions, including \(S=N\) and singleton \(S\); hence the class is totally balanced.

**Necessity by a two-player restricted obstruction.** Suppose (1) fails: some nonnegative multiset \(U=\{u_1,\ldots,u_m\}\) and \(b\ge0\) obey \(F(U\uplus\{b\})>F(U)+b\). Construct an in-star with target \(j\), distinguished source \(p\), and distinct outside sources \(q_1,\ldots,q_m\), where the only arcs are \(p\to j\) of weight \(b\) and \(q_k\to j\) of weight \(u_k\). For the restricted player set \(S=\{p,j\}\), the coalition worths are
\[
 v(\{p\})=0,\qquad v(\{j\})=F(U\uplus\{b\}),\qquad v(S)=b+F(U).
 \tag{6}
\]

A two-player core could exist only if the sum of the two singleton worths did not exceed \(v(S)\). Equation (6) violates that condition, so the restriction has empty core. This proves the converse, even when \(m=0\) and the ambient graph has only two vertices.

**Uniqueness of the full core for singleton-normalized aggregators.** Suppose (1) holds and also \(F(\{b\})=b\). Let
\[
 c_j=\sum_{\substack{i\in N\\(i,j)\in E}}a_{ij}.
 \tag{7}
\]

Formula (3) with \(S=N\) shows that \(c\) belongs to the full-game core. Since the sole outside vertex of \(N\setminus\{j\}\) is \(j\), singleton normalization implies
\[
 v(N\setminus\{j\})=v(N)-c_j.
 \tag{8}
\]

Indeed, every outgoing arc from \(j\) is restored exactly once as an external singleton contribution, while every arc entering \(j\) is absent from the complement coalition. Therefore any core vector \(y\) satisfies \(y_j\le v(N)-v(N\setminus\{j\})=c_j\). Both vectors have coordinate sum \(v(N)\); hence \(y=c\).

**Concrete aggregators.** For nonempty \(U\), minimum never increases when a weight is inserted; maximum increases by at most the inserted nonnegative weight; and arithmetic mean changes by \((b-\operatorname{mean}(U))/(|U|+1)\le b\). Their singleton and empty-set normalizations hold. For a rank statistic, sort the \(m\) weights and select the \(k(m)\)-th smallest, where \(1\le k(m)\le m\) and \(k(m+1)\le k(m)+1\). Inserting a zero gives an order statistic no larger than the previous selected statistic; increasing that new coordinate from zero to \(b\) changes any fixed-rank order statistic by at most \(b\). This proves (1). Fixed lower and upper medians and fixed-quantile ranks \(k(m)=\lceil \theta m\rceil\) for \(0<\theta\le1\) meet the rank condition, including both extreme quantiles. The empty multiset is assigned zero throughout.

**Concrete sharpness witness.** Set \(F(U)=\sum_{u\in U}u\) for \(|U|\le1\) and \(F(U)=2\sum_{u\in U}u\) otherwise. Two arcs of weight one entering a third vertex give \(v(\{j\})=4\), but \(v(N)=2\); no full-game core exists. This operator has the same empty-set and singleton normalization, but fails (1).

## Verification

The standalone standard-library checker `checks/verify.py` enumerates every nonnegative integer-weighted directed graph on two and three vertices with each possible arc of weight zero, one, or two (zero-weight arcs omitted). It additionally samples seeded sparse weighted graphs on four and five vertices. For each graph it checks all restricted-coalition core inequalities, efficiency, the incoming-weight singleton characterization, and complement identities, for six aggregators: minimum, maximum, arithmetic mean, lower median, upper median, and upper quartile. The run passed **6,228 exact-rational graph/aggregator cases**, plus the explicit failure witness. The finite tests support the proof but do not certify the universal quantifiers by themselves.

To reproduce: `python checks/verify.py` with Python 3.10 or later; no external dependencies.

## Relationship to prior work

Bandhana, Kroupa, and García (AAMAS 2024, Definition 3.1 and Proposition 3.4) introduce the minimum-based trust game and an incoming-weight core allocation. Ryzák and Kroupa (arXiv:2605.18157v1, Sections 2 and 5) prove uniqueness and total balancedness **for the minimum operator**, and explicitly identify average, median, and other order statistics as an unresolved external-aggregation direction in Section 6. This theorem supplies an exact *if and only if* operator criterion and shows that mean, max, and quantile aggregators preserve stability, although the minimum-specific unanimity decomposition and polynomial-time Shapley formulas need not survive. The proof does not claim novelty for the prior minimum case, incoming-weight argument, or Bondareva–Shapley equivalence between balance and core feasibility.

## Limitations

Only nonnegative, additive internal directed-arc weights are covered. The universal equivalence concerns nonempty cores of **all restricted games**, not a necessary condition for a particular graph's core. Singleton-core uniqueness additionally requires singleton normalization and is asserted only for the full game. No claim is made about superadditivity, monotonicity, exactness of games, individual incentive compatibility, Shapley/Banzhaf tractability, or signed weights. Publication priority for a generic operator-budget reformulation in less directly indexed literature is not independently resolved.

## References

1. D. Ryzák and T. Kroupa, *A Tractable Class of Cooperative Games Defined by Directed Networks: Unanimity Decomposition and Shapley Value*, first posted 18 May 2026, arXiv:2605.18157v1, https://arxiv.org/html/2605.18157v1 (especially Sections 2, 5, and 6).
2. A. Bandhana, T. Kroupa, and S. García, *Trust in Shapley: A Cooperative Quest for Global Trust in P2P Network*, AAMAS 2024, pp. 132–140, https://aamas.csc.liv.ac.uk/Proceedings/aamas2024/pdfs/p132.pdf (especially Definition 3.1 and Proposition 3.4).
