# Arbitrary fixed-instance EF1 feasibility patterns on weighted stars

## Finding

For each integer \(m\ge 3\), **every** subset of the intermediate agent counts \(\{2,\ldots,m-1\}\) can be exactly the set of those counts permitting a connected \(\mathrm{EF1}_{\mathrm{outer}}\) allocation of one fixed, identically valued \(m\)-leaf star. All vertex values can be **positive, pairwise distinct integers**, and all existence and nonexistence decisions have a strict margin: the pattern persists under sufficiently small independent changes of the values.

Specifically, let \(K_{1,m}\) be a star with central vertex of value \(c\ge0\) and leaf values \(0\le a_1\le\cdots\le a_m\), shared additively by all agents. For \(2\le k\le m-1\), let \(r=m-k+1\). A connected \(\mathrm{EF1}_{\mathrm{outer}}\) allocation into exactly \(k\) nonempty bundles exists **if and only if**

\[
a_{r+1}\ \ge\ c+\sum_{i=1}^{r-1} a_i.\tag{1}
\]

For \(k=1,m,m+1\), such an allocation always exists. Hence there are exactly \(2^{m-2}\) attainable Boolean feasibility patterns as \(k\) runs from \(1\) through \(m+1\); this is the maximum combinatorially possible because the three endpoint counts are forced feasible.

The six-vertex star with central value \(6\) and sorted leaf values \((4,5,9,16,23)\) has the feasibility sequence

\[
(\text{yes},\text{no},\text{yes},\text{no},\text{yes},\text{yes})
\]

for \(k=1,2,3,4,5,6\), respectively. Six vertices are the smallest possible size of any connected graph admitting a **single fixed valuation profile** with two separate intervals of infeasible agent counts, when allocations use nonempty bundles and \(k\le |V|\).

## Assumptions and scope

The items are the \(m+1\) vertices of a finite undirected star. An allocation into \(k\) bundles is a partition of all vertices into \(k\) nonempty sets, each inducing a connected subgraph. All \(k\) agents have the **same nonnegative additive** utility \(v(X)=\sum_{z\in X}v(\{z\})\). A partition is connected \(\mathrm{EF1}_{\mathrm{outer}}\) if for every ordered pair of distinct recipients \(i,j\), either \(v(A_i)\ge v(A_j)\), or there is \(z\in A_j\) such that removing \(z\) leaves \(A_j\setminus\{z\}\) connected (or empty) and \(v(A_i)\ge v(A_j\setminus\{z\})\). The empty remainder after deleting a singleton is allowed and has value zero. The convention here requires **nonempty** allocated bundles, and thus \(1\le k\le m+1\). The results concern this one valuation profile across different counts of identical agents; they do not concern guarantees quantified over all valuation profiles.

## Proof

**Exact feasibility criterion.** Fix \(2\le k\le m-1\) and put \(r=m-k+1\ge2\). In any connected allocation, exactly one bundle contains the star's center. Every other bundle consists of a singleton leaf, since two leaves without the center do not induce a connected subgraph. Consequently, the central bundle contains the center and exactly \(r\) leaves; call the chosen set of leaves \(R\), and let \(U\) be the nonempty set of unchosen leaves.

No recipient envies a singleton bundle beyond the outer-one-item tolerance, since its unique leaf may be removed and the resulting value is zero. For a singleton leaf in \(U\), the permissible one-vertex deletions from the central bundle are exactly the \(r\) leaves in \(R\): deleting the center would leave at least two isolated leaves and so would not preserve connectivity. Let \(h(R)=\max_{i\in R}a_i\), \(s(R)=\sum_{i\in R}a_i\), and \(b(U)=\min_{i\in U}a_i\). It follows directly from the definition that the partition satisfies \(\mathrm{EF1}_{\mathrm{outer}}\) if and only if

\[
b(U)\ \ge\ c+s(R)-h(R).\tag{2}
\]

For every \(r\)-element set \(R\), the smallest unselected leaf has value at most \(a_{r+1}\), because among the first \(r+1\) sorted leaves at least one is unselected. Likewise, \(s(R)-h(R)\) is the sum of the \(r-1\) selected values other than a largest one, and is at least \(\sum_{i=1}^{r-1}a_i\). Thus (2) implies (1). Conversely, selecting precisely the \(r\) least-valued leaves gives \(b(U)=a_{r+1}\) and \(s(R)-h(R)=\sum_{i=1}^{r-1}a_i\), so (1) implies (2). This proves the equivalence without any genericity assumption and includes all ties and zero values.

When \(k=m\), the central bundle contains the center and a single least-valued leaf, while every other bundle is a singleton leaf. Both vertices in the two-vertex central bundle are outer, and removing the center leaves a value no larger than that of every other leaf. Thus the allocation is fair. When \(k=m+1\), every vertex is a singleton. When \(k=1\), the whole star is the sole bundle. This proves the endpoint assertions.

**Constructing an arbitrary strict pattern.** Fix a subset \(B\subseteq\{2,\ldots,m-1\}\). Set the center value \(c=6\) and start with leaf values \(a_1=4\) and \(a_2=5\). For each integer \(r\) with \(2\le r\le m-1\), recursively define

\[
T_r=6+\sum_{i=1}^{r-1}a_i,\qquad
 a_{r+1}=\begin{cases}
 T_r+1,&m-r+1\in B,\\
 T_r-1,&m-r+1\notin B.
 \end{cases}\tag{3}
\]

The generated values are positive, strictly increasing, and distinct from the center. Indeed, \(T_2=10>5\), while \(T_{r+1}=T_r+a_r\) and \(a_{r+1}=T_r\pm1\) give \(T_{r+1}-a_{r+1}=a_r\mp1>0\) inductively. Also \(a_3\ge9>6\). For each \(r\), the gap in (1) is **exactly** \(+1\) when \(m-r+1\in B\), and \(-1\) otherwise. Hence the feasible counts are exactly \(\{1,m,m+1\}\cup B\), for the single valuation profile specified by (3). Finitely many strictly nonzero margins and distinct positive values preserve the pattern on an open neighborhood of that profile.

**The six-vertex boundary.** Taking \(m=5\) and \(B=\{3\}\) in (3) gives the stated example. Every connected graph on \(v\) vertices admits a connected \(\mathrm{EF1}_{\mathrm{outer}}\) allocation for \(k=v-1\) agents under arbitrary monotone valuations (Chen–Zwicker, Observation 2); singletons work for \(k=v\), and the whole graph works for \(k=1\). When \(v\le5\), only \(k=2,\ldots,v-2\) can be infeasible, at most two consecutive integers, so two separated nonempty intervals of infeasibility are impossible. The six-vertex example therefore has minimum order.

## Verification

Run the included standalone Python 3 program `verify_stars.py`, which has no third-party dependencies. It directly enumerates all star-connected partitions (up to the irrelevant names of identical agents), implements the ordered-pair definition of \(\mathrm{EF1}_{\mathrm{outer}}\) without using the theorem's inequality, and compares its outcomes to (1). It performed **49,055** exact-value direct-search comparisons over all sorted nonnegative integer leaf multisets from \(\{0,1,2,3,4\}\), for \(3\le m\le8\), all five center values, and every possible agent count. It also checked **1,022** different constructed feasibility patterns for \(3\le m\le11\), including direct search for small sizes, and checked the six-vertex alternating witness. All checks passed. These finite checks validate the implementation and examples; the unrestricted statements follow from the proof above, not from finite enumeration.

## Relationship to prior work

Chen and Zwicker (2024) study which agent counts are **universally guaranteed** to admit connected \(\mathrm{EF1}_{\mathrm{outer}}\) for a fixed graph and a valuation class. They conjecture an initial-yes / middle-no / final-yes structure for that graph-level universal spectrum; their Section 5 and Lemma 3 treat stars. Bousquet, Connor, Totschnig and Zeitoun (2026) investigate structural and algorithmic aspects of the same graph-level fairness problem, including tree spectra and binary-valued cases. Here the logical quantifier is different: **one prescribed common additive valuation is held fixed while the number of identical agents varies**. The present theorem gives every such fixed-profile pattern, rather than a graph-wide guarantee or a counterexample to the universal-spectrum conjecture. The graph-wide star obstruction statements do not decide the exact mix of successes and failures for one specified weighted instance.

## Limitations

This is a classification for stars with **common additive** valuations and nonempty bundles, not for arbitrary graphs or heterogeneous agent valuations. It does not refute or resolve the graph-wide universal-spectrum conjecture. Robustness means invariance under sufficiently small value perturbations, not adversarial robustness to arbitrary agent-specific preferences. The classification makes no algorithmic complexity claim beyond the explicit closed-form test and linear-time realization construction. Literature priority remains subject to any results in unindexed or inaccessible sources. No independent audit is claimed.

## References

1. N. Bousquet, F. Connor, A. Totschnig, and S. Zeitoun, *Fair Division of Graphs: Beyond Traceability* (first posted 2026-08-30), arXiv:2608.29902, https://arxiv.org/abs/2608.29902.
2. J. Chen and W. S. Zwicker, *Cutsets and EF1 Fair Division of Graphs* (first posted 2024-02-08), arXiv:2402.05884, https://arxiv.org/abs/2402.05884. See especially Section 5, Observation 2, Conjecture 1, and Lemma 3.
