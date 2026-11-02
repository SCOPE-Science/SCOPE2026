# Leaf multiplicities and exact online shattering of rooted comb paths

## Finding

For any integer \(m\ge 1\), and positive integers \(a_1,\ldots,a_m\), construct a rooted comb \(T(a_1,\ldots,a_m)\) with a spine \(v_1,\ldots,v_m\), directed away from its root \(v_1\). For each \(i\), attach exactly \(a_i\) new leaves directly to \(v_i\). For \(i<m\), the spine edge \(v_iv_{i+1}\) is present. Every hypothesis is the vertex set of one complete root-to-leaf path, and each Boolean query tests membership of an original tree vertex in that path. Write \(\mathcal P(a_1,\ldots,a_m)\) for this concept class.

Let \(N=\sum_{i=1}^m a_i\), and let \(K(a_1,\ldots,a_m)\) be the largest number of consecutive, nonempty, disjoint index intervals, arranged from left to right, such that each contains at least two leaves in total; an unused terminal suffix of groups is allowed. Equivalently, greedily accumulate the weights from left to right and close a block immediately when its sum first reaches two, resetting the accumulator to zero. Then, for \(N\ge2\),
\[
\operatorname{VCdim}(\mathcal P)=1,\qquad
\operatorname{Ldim}(\mathcal P)=1+\lfloor\log_2 K(a_1,\ldots,a_m)\rfloor.
\]
For \(N=1\), both dimensions are zero. The Littlestone dimension is also the optimal deterministic realizable online mistake bound.

For fixed \(m\ge2\), every positive profile has Littlestone dimension either \(\lfloor\log_2 m\rfloor\) or \(1+\lfloor\log_2 m\rfloor\), with the larger value occurring exactly when \(K\ge 2^{\lfloor\log_2 m\rfloor}\). These two possibilities can occur at equal spine length, equal leaf count and even the same multiset of leaf multiplicities. For example, the profiles \((1,1,2,2,1,1)\) and \((1,2,1,2,1,1)\), both with eight leaves, have Littlestone dimensions three and two respectively, while both have VC dimension one. Thus the arrangement of multiplicities, not merely their sum or multiset, controls adaptive shattering.

## Assumptions and scope

Trees are finite, rooted and all \(a_i\) are strictly positive integers. The path concepts are distinct subsets of the **original** vertex set; no auxiliary order tests, leaf-to-leaf paths, edge queries, or extra labels are allowed. Querying a leaf selects exactly one path hypothesis. Querying the spine vertex \(v_j\), for \(j\ge2\), selects exactly the paths ending in groups \(j,j+1,\ldots,m\). Querying \(v_1\) has constant answer one. The definition of \(K\) is group-respecting: a group of \(a_i\) leaves cannot be split between two intervals.

The value of \(K\) can be computed in \(O(m)\) time by the stated greedy scan. In particular, when \(N\ge2\) it is at least one and at most \(\min\{m,\lfloor N/2\rfloor\}\).

## Proof

**(1) Classification of queries.** A root-to-leaf path ends at one and only one of the \(a_i\) leaves in some group \(i\). The only nonconstant queries are single-leaf tests, supported by a unique hypothesis, and spine tests, supported by a final segment of the groups. All paths have the same ancestor chain until they enter their terminating group.

**(2) VC dimension.** If two queried vertices are incomparable in the ancestor order, no path contains both, so the labeling \((1,1)\) is impossible. If they are comparable, a path containing the descendant also contains the ancestor, so one mixed labeling is impossible. No pair of vertices is VC-shattered. If \(N\ge2\), any leaf query realizes both labels on different path hypotheses, giving VC dimension one. With \(N=1\), the class contains one hypothesis and has VC dimension zero.

**(3) Upper bound on Littlestone dimension.** Suppose a complete depth-\(d\) adaptive decision tree is shattered, with \(d\ge2\). At each query node before the last decision level, both answer subfamilies must contain at least two distinct hypotheses (indeed they must each shatter a positive-depth binary tree). A leaf query has only one positive hypothesis, and the root query is constant, so all such earlier nodes must query spine vertices. The answer histories of these spine tests divide the groups into \(2^{d-1}\) nonempty **consecutive intervals**: every branch corresponds to the intersection of some suffixes and complements of suffixes. The final query at each history must split its remaining hypothesis set into two nonempty parts, requiring that interval to contain at least two leaves. These intervals therefore form a consecutive group partition (they cover all groups because every path follows exactly one of the first \(d-1\) answer histories), so \(2^{d-1}\le K\). Thus \(d\le1+\lfloor\log_2K\rfloor\). For \(d=1\) this bound also holds when \(N\ge2\).

**(4) Matching lower bound.** Put \(r=\lfloor\log_2K\rfloor\). By the definition of \(K\), there is a division of the \(m\) groups into at least \(2^r\) consecutive blocks, each containing at least two leaves. Merge neighboring blocks until exactly \(2^r\) remain, absorbing any unused terminal groups into the final block. At the first \(r\) query levels, use spine membership queries at successive boundaries to implement a balanced binary search among these \(2^r\) blocks. The query at a boundary selects precisely the later blocks, conditional on the current interval. At each of the \(2^r\) final nodes, query one leaf in that block, which divides the remaining hypotheses into a nonempty singleton-positive branch and a nonempty negative branch. This is a complete shattered tree of depth \(r+1\), proving equality.

**(5) Greedy computation of \(K\).** In any maximum packing, the first completed interval can be shortened to the earliest prefix of weight at least two: doing so leaves at least as many complete groups for subsequent intervals and does not decrease the achievable count. Repeat inductively after its endpoint. Any final incomplete suffix may remain unused. This is exactly the stated linear-time greedy rule.

**(6) Fixed-length phase and ordering effect.** Pairing consecutive groups produces \(\lfloor m/2\rfloor\) qualifying intervals, while no partition has more than \(m\) intervals. For \(m\ge2\), the formula in the finding and these inequalities imply \(\lfloor\log_2m\rfloor\le \operatorname{Ldim}\le1+\lfloor\log_2m\rfloor\). The larger value occurs precisely when \(K\ge2^{\lfloor\log_2m\rfloor}\). For the first displayed six-group profile, the qualifying blocks are \([1,2],[3],[4],[5,6]\), giving \(K=4\); for the second, greedy blocks are \([1,2],[3,4],[5,6]\), giving \(K=3\). Hence the exact dimensions are three and two. The standard characterization of Littlestone dimension as the optimal deterministic realizable mistake bound gives the online-learning interpretation.

## Verification

The standalone Python 3 program `verify_comb.py` constructs the actual rooted tree, enumerates each root-to-leaf path as a vertex subset, and computes the Littlestone dimension via the complete finite version-space recurrence
\[
D(S)=\max_{q:\,S_q^0,S_q^1\ne\varnothing}\bigl(1+\min\{D(S_q^0),D(S_q^1)\}\bigr),
\]
with value zero for a singleton hypothesis set (and zero when no query splits). It separately tests static two-point shattering and compares with the closed formula. Every ordered composition of \(N\) into positive group sizes was checked for \(1\le N\le10\): precisely \(\sum_{N=1}^{10}2^{N-1}=1023\) cases, all passing. Additional displayed profiles have formula predictions. The verifier checks finite instances only; the unrestricted proof is above.

Run `python3 verify_comb.py` from the folder containing these files. Python's standard library suffices.

## Relationship to prior work

Walker, *Tree Dimension and the Sauer–Shelah Dichotomy* (first public March 23, 2022), studies the dimension of leaf subsets in complete binary trees and their connection to Littlestone and VC shattering. Its main results give general combinatorial inequalities and leaf-set classifications; they do not provide an exact Littlestone calculation for **vertex-membership families of root-to-leaf paths** in weighted rooted combs. The distinction between its ambient binary-tree leaf-set invariant and the present dual path-concept system matters.

Ghazi, Golowich, Kumar and Manurangsi, *Near-tight closure bounds for Littlestone and threshold dimensions* (first public July 7, 2020), prove general upper bounds for arbitrary Boolean aggregations of concept classes. Their closure bounds do not imply the group-respecting two-leaf block criterion or the exact one-bit arrangement effect. These are specialized structural statements, not consequences of an asymptotic closure inequality.

Finite threshold classes and singleton concept classes are standard ingredients, but neither their separate Littlestone dimensions nor the generic cardinality upper bound determines the Littlestone dimension of this **mixed** query system: the profiles \((1,1,2,2,1,1)\) and \((1,2,1,2,1,1)\) have the same size and coordinate multiplicity multiset yet different ranks. The proof above identifies the missing ordered packing parameter. Related exact calculations for fixed-width intervals, all chain intervals and rooted-tree ideals concern different hypothesis families and do not imply this weighted comb classification.

## Limitations

The theorem concerns rooted comb trees with leaves directly attached to each spine vertex. General rooted trees may have branching side subtrees and query supports which are neither suffixes nor singletons, so the upper-bound argument does not apply there. The finite verifier stops at ten leaves; it is not an infinite certificate. Specialized literature under names such as laminar subset-query games, hierarchical search with singleton tests, or online point identification could contain equivalent prior results; comprehensive historical priority and independent mathematical review have not been established.

## References

- Roland Walker, *Tree Dimension and the Sauer–Shelah Dichotomy*, arXiv:2203.12211, first submitted 2022-03-23, sections 1 and 1.1 and 1.2. https://arxiv.org/abs/2203.12211
- Badih Ghazi, Noah Golowich, Ravi Kumar, Pasin Manurangsi, *Near-tight closure bounds for Littlestone and threshold dimensions*, arXiv:2007.03668, first submitted 2020-07-07; *Proceedings of Machine Learning Research* 132 (2021), sections 1 and 2. https://arxiv.org/abs/2007.03668 ; https://proceedings.mlr.press/v132/ghazi21a.html
