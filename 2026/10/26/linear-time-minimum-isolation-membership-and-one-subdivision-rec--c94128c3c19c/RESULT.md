# Linear-time minimum-isolation membership and one-subdivision recognition in trees

## Finding

**Theorem.** For every finite nonempty tree \(T\) on \(n\) vertices, the isolation number \(\iota(T)\), and each of the three sets of vertices belonging to *all*, *some but not all*, or *no* minimum isolating sets, can be computed together in \(O(n)\) time and \(O(n)\) space, on a unit-cost RAM with adjacency-list input. The algorithm is an explicit constant-state directed-edge dynamic program followed by one prefix/suffix rerooting pass. Consequently, given any nonstar tree \(T\), whether subdividing **some single edge** increases \(\iota(T)\) is decidable in \(O(n)\) time.

Here \(S\subseteq V(T)\) is *isolating* when \(V(T)\setminus N_T[S]\) is independent, and \(\iota(T)\) is the minimum cardinality of such an \(S\). For a vertex \(v\), put
\[
J_v=\min\{|S|:S\text{ isolating},\ v\in S\},\qquad
K_v=\min\{|S|:S\text{ isolating},\ v\notin S\},
\]
with empty minima equal to \(+\infty\). The algorithm returns every \(J_v,K_v\), not only the three membership classes. In particular \(\iota(T)=\min\{J_v,K_v\}\) for each \(v\); membership in no minimum isolating set is equivalent to \(J_v>\iota(T)\), membership in every one to \(K_v>\iota(T)\), and otherwise the vertex belongs to some but not all of them.

## Assumptions and scope

The graph is finite, undirected, simple, connected and acyclic; a one-vertex tree is allowed for membership calculations. Computation takes place over \(\mathbb N\cup\{+\infty\}\), with the usual min-plus conventions. An edge \(uv\) is isolated by \(S\) exactly when at least one of \(u,v\) is dominated by \(S\), i.e. lies in \(N_T[S]\). The subdivided-edge recognition consequence assumes a nonstar tree because the cited characterization is stated for that class. No assertion about full isolation subdivision numbers \(2,3,4\), or about general graphs, is made.

## Proof

**1. Directed-edge state.** For each oriented edge \(u\to v\), remove \(uv\) and let \(U\) be the component containing \(u\). Define
\[
F_{u\to v}(p,s,d)\in\mathbb N\cup\{+\infty\},\qquad p,s,d\in\{0,1\},
\]
as the minimum number of selected vertices in \(U\) under these constraints: the external vertex \(v\) has prescribed selection bit \(p\); the vertex \(u\) has prescribed selection bit \(s\); its domination bit \(d\) is exactly the truth value of \(s=1\), or \(p=1\), or at least one selected neighbour of \(u\) in \(U\); and each edge completely inside \(U\) has at least one dominated endpoint. The external vertex is not charged, and edge \(uv\) is not yet tested. Thus every feasible tree-wide selection restricts to compatible directed-edge states, and compatible states can be glued because the graph has no cycles.

Suppose the other neighbours of \(u\) are \(w_1,\ldots,w_k\). For each incoming message \(F_{w_i\to u}\), define
\[
A_{1,i}=\min_{a,b\in\{0,1\}}F_{w_i\to u}(1,a,b),\quad
A_{0,i}=\min_{a,b\in\{0,1\}}F_{w_i\to u}(0,a,b),\quad
B_i=F_{w_i\to u}(0,0,1),
\]
\[
C_i=\min_{b\in\{0,1\}}F_{w_i\to u}(0,0,b),\qquad
D_i=\min_{b\in\{0,1\}}F_{w_i\to u}(0,1,b).
\]
For this collection set \(S_1=\sum_i A_{1,i}\), \(S_0=\sum_i A_{0,i}\), \(B=\sum_i B_i\), and \(N=\sum_i C_i\). Let \(Y\) be the minimum cost of the child components **with at least one child selected**, when \(u\) itself is unselected. Starting at \((N,Y)=(0,+\infty)\), incorporate children in any order by
\[
N'=N+C_i,\qquad Y'=\min\bigl\{Y+\min(C_i,D_i),\ N+D_i\bigr\}.
\]
The exhaustive possible finite entries in \(F_{u\to v}\) are then
\[
F_{u\to v}(p,1,1)=1+S_1\quad(p=0,1),\qquad
F_{u\to v}(1,0,1)=S_0,
\]
\[
F_{u\to v}(0,0,0)=B,\qquad
F_{u\to v}(0,0,1)=Y;
\]
all other entries are \(+\infty\). To verify the non-obvious cases: when both \(u\) and its external neighbour are unselected, \(u\) is undominated precisely when no child is selected. In that case every edge \(uw_i\) forces \(w_i\) to be dominated, giving \(B\). If a child is selected, \(u\) is dominated and its incident edges impose no additional condition; this gives \(Y\). If \(u\) is selected, all its incident edges are already covered; if the external vertex is selected, the same holds even when \(u\) is not. These cases prove all state equations by induction on the component order, including the empty-child base case.

**2. Constant-size associative aggregate.** A collection of incoming messages is represented by the five entries \((S_1,S_0,B,N,Y)\). Combining the aggregates of disjoint collections \(L\) and \(R\) is associative: the first four coordinates add, and the final coordinate is
\[
Y_{L\cup R}=\min\{Y_L+\min(N_R,Y_R),\ N_L+Y_R\}.
\]
Indeed, a selected child must occur in \(L\) or, if none occurs there, in \(R\). This is simply minimization over Boolean OR, so association and the identity aggregate \((0,0,0,0,+\infty)\) follow. Applying the state formulas to the aggregate gives the outgoing message in constant time.

**3. Two tree passes.** Choose any root. In postorder compute all child-to-parent messages. In preorder, at every vertex, compute prefix and suffix aggregates of the incoming messages from its neighbours, including the already available parent-to-child message. Excluding one neighbour \(v\) takes one combination of the corresponding prefix and suffix aggregates, hence yields \(F_{u\to v}\) in constant time. Across all vertices, this requires \(O(\sum_u\deg(u))=O(n)\) operations and stores \(O(n)\) constant-sized messages. This is exact rerooting, not one independent run per vertex.

**4. Global optimum and vertex status.** For each vertex \(u\), aggregate messages from *all* its neighbours and denote the result \((S_1(u),S_0(u),B(u),N(u),Y(u))\). By the same exhaustive local case split, the exact constrained whole-tree minima are
\[
J_u=1+S_1(u),\qquad K_u=\min\{B(u),Y(u)\}.
\]
Choose any vertex \(r\). Then \(\iota(T)=\min\{J_r,K_r\}\). The three status classes are decided from the comparisons stated in the finding, in constant time per vertex. This proves the claimed linear bounds.

**5. Subdivision consequence.** Dettlaff, Lemańska, Mora, Ziemann and Żyliński [1, Theorem 3.2] prove that for a nonstar tree \(T\), subdividing some single edge raises the isolation number if and only if there exists a vertex \(u\) whose closed neighbourhood satisfies \(N_T[u]\subseteq\mathcal N_\iota(T)\), where \(\mathcal N_\iota(T)\) consists of vertices in no minimum isolating set. The computed comparisons \(J_v>\iota(T)\) identify precisely this set. Scanning all closed neighbourhoods takes another \(O(n)\) time, proving the recognition claim. This last equivalence relies on [1], rather than being re-proved here.

## Verification

The standalone `verify_isolation_reroot.py` implements the directed-message recurrence, associative prefix/suffix rerooting and both constrained costs using integer costs and mathematical infinity. It independently checks \(18{,}729\) trees (all labelled Prüfer trees with \(1\leq n\leq7\), plus 480 deterministic random trees of orders 8 through 13) against direct enumeration of all vertex subsets, comparing \(\iota(T)\), every \(J_v\), and every \(K_v\). For every labelled tree of orders 2 through 6 (1,441 trees), it also compares the closed-neighbourhood prediction with direct recomputation of the isolation number after each possible one-edge subdivision. The script outputs `VERIFY_OK independent_bf_tree_cases= 18729 subdivision_trees= 1441`. Additional input scaling tests at 1,000, 10,000, and 50,000 vertices checked implementation behaviour, not mathematical correctness. No finite test is used to justify the infinite claim; that follows from the local-state induction and associative rerooting proof.

## Relationship to prior work

Dettlaff et al. [1, Section 4] explicitly obtain a quadratic-time recognition algorithm from their structural characterization, anticipate a linear-time rerooting solution, and leave its formal development to future work. The present result gives that development with an explicit, checkable min-plus recurrence, and returns both forced-inclusion and forced-exclusion minima, producing all three optimal-membership classes. Ziemann and Żyliński [2] prove an analogous linear-time membership classification for **dominating sets**, a different feasibility predicate; its numerical states cannot directly characterize isolating sets. Chen et al. [3] and Wang et al. [4] provide efficient **optimization** for vertex-edge domination under structural restrictions, without in the inspected descriptions giving all optimum-membership statuses. Bartolo et al. [5] give a linear-time recognition result for trees on which **every** single-edge subdivision raises the isolation number, rather than existence of **some** edge as addressed here. The algorithms therefore differ in object or quantifier. The O(n) possibility was anticipated in [1]; no claim is made that generic rerooting itself is new.

## Limitations

The result establishes linear-time classification for tree inputs only, in the standard adjacency-list RAM model. It does not improve optimization for arbitrary graphs, solve classification of subdivision numbers 2, 3 or 4, or establish priority over every unpublished implementation or generic constraint-satisfaction framework. The proof uses the published characterization [1] for its final single-subdivision corollary. The historical-priority search is necessarily incomplete, and no independent external validation is claimed.

## References

[1] M. Dettlaff, M. Lemańska, M. Mora, R. Ziemann, P. Żyliński, *Isolation subdivision number of a graph*, arXiv:2606.21190 (first submitted June 19, 2026), especially Theorem 3.2 and Section 4. https://arxiv.org/abs/2606.21190

[2] R. Ziemann and P. Żyliński, *A linear time algorithm to compute vertices that belong to all, some and no minimum dominating sets in a tree and its consequences*, Opuscula Math. 45 (2025), 841–855. https://doi.org/10.7494/OpMath.2025.45.6.841

[3] J. Chen, Y.-P. Liang, C.-X. Wang, S.-J. Xu, *Algorithmic aspects of \(P_k\)-isolation in graphs and extremal graphs for a \(P_3\)-isolation bound*, Information Processing Letters 187 (2025), 106521.

[4] Y. Wang, H. Zhang, M. Lu, *Algorithm for finding vertex-edge domination number on graphs with bounded treewidth and related problems on planar graphs*, arXiv:2605.10487 (May 11, 2026). https://arxiv.org/abs/2605.10487

[5] K. Bartolo, P. Borg, M. Dettlaff, M. Lemańska, P. Żyliński, *Isolation critical graphs under multiple edge subdivision*, arXiv:2602.22980 (February 26, 2026). https://arxiv.org/abs/2602.22980
