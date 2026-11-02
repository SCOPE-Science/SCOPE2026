# Exact exchange distances and distance profile for minimum connected domination in crown graphs

## Finding

**Theorem.** Fix an integer \(n\ge 3\). Let \(G_n=K_{n,n}-M\) be the crown graph with vertex classes \(\{L_1,\ldots,L_n\}\) and \(\{R_1,\ldots,R_n\}\), where \(L_iR_j\) is an edge precisely when \(i\ne j\). Define a *connected dominating set* (CDS) as a vertex set that dominates the entire graph and induces a connected graph. Write \(\mathcal C_n(z)=\sum_{S\text{ CDS}}z^{|S|}\). Then
\[
\mathcal C_n(z)=\left((1+z)^n-1-nz\right)^2-\binom n2z^4.
\]
All inclusion-minimal CDS have size four. They are exactly the sets \(\{L_i:i\in A\}\cup\{R_j:j\in B\}\) with \(A,B\in\binom{[n]}2\) and \(A\ne B\). Their number \(\binom n2\left(\binom n2-1\right)\) was previously recorded as a crown-graph minimum-CDS count (OEIS A033487, annotation dated 2017-06-29); the count itself is **not** asserted to be new.

Define the token-exchange reconfiguration graph \(\mathcal R_n\) on these minimum sets by joining two sets when they differ in exactly one chosen graph vertex. Let \(H_n=J(n,2)\), whose vertices are two-subsets of \([n]\), adjacent when they share exactly one element. The graph \(\mathcal R_n\) is canonically isomorphic to the Cartesian square \(H_n\square H_n\) with its diagonal \(\{(A,A)\}\) deleted. For any \((A,B),(C,D)\in V(\mathcal R_n)\), put \(\delta(X,Y)=2-|X\cap Y|\). The complete shortest-path metric is
\[
 d_{\mathcal R_n}\big((A,B),(C,D)\big)
 =\delta(A,C)+\delta(B,D)
  +\mathbf 1_{\{C=B,\ D=A,\ |A\cap B|=1\}}.
\]
In particular \(\mathcal R_n\) is connected and has diameter three at \(n=3\), and four at every \(n\ge4\). In contrast, token sliding along an edge of \(G_n\), while preserving minimum connected domination, admits no move: all its minimum-set configurations are isolated.

Put \(v=\binom n2\), \(k=2(n-2)\), \(q=\binom{n-2}{2}\), and \(g(t)=1+kt+qt^2\). The **entire ordered-pair distance enumerator**, including ordered pairs at zero distance, is
\[
\mathcal D_n(t)
 =\sum_{X,Y\in V(\mathcal R_n)}t^{d_{\mathcal R_n}(X,Y)}
 =v(v-2)g(t)^2+v\big(1+kt^2+qt^4\big)+vk(t^3-t^2).
\]
Thus the numbers of ordered pairs at distances zero through four are, respectively,
\[
 v(v-1),\quad 2v(v-2)k,\quad v(v-2)(k^2+2q),\quad
 2v(v-2)kq+vk,\quad v(v-2)q^2+vq.
\]
The degree is \(2k-2\) at each of the \(vk\) vertices \((A,B)\) with \(|A\cap B|=1\), and \(2k\) at each of the \(vq\) vertices with \(|A\cap B|=0\); the edge count is \(vk(v-2)\).

## Assumptions and scope

All graphs are finite, simple, undirected, and labeled by \([n]\). Sets are counted with their labels. The polynomial counts *all* CDS, not only minimum or inclusion-minimal sets. Exchange moves replace exactly one chosen vertex by any previously unchosen vertex; sliding moves additionally require the two exchanged vertices to be adjacent in \(G_n\). The ordered-pair polynomial counts both orientations of distinct endpoints and includes all \(v(v-1)\) diagonal ordered pairs. No assertion is made about other graph families or independent publication priority.

## Proof

**1. Characterize and enumerate CDS.** For any vertex set \(S\), let \(A=\{i:L_i\in S\}\) and \(B=\{j:R_j\in S\}\). If \(A\) is empty, \(S\) has no edges and cannot dominate/induce a connected graph. If \(A=\{i\}\), then \(R_i\), if unchosen, has no chosen neighbor, whereas if chosen it is isolated in the induced graph; either way a CDS is impossible. The same holds if \(|B|\le1\). Conversely, \(|A|,|B|\ge2\) ensures every graph vertex is dominated, since it has a neighbor among at least two chosen opposite-shore indices. Each selected vertex has a selected neighbor. With \(|A|\ge3\), any two right-shore vertices share a left-shore neighbor, and all selected left vertices attach to the right shore; hence the induced graph is connected. The same argument applies when \(|B|\ge3\). With \(|A|=|B|=2\), the induced graph is disconnected precisely when \(A=B\), in which case it consists of two disjoint cross edges; otherwise it is a four-vertex path. This proves the exact criterion and the stated all-CDS polynomial by subtracting the \(\binom n2\) excluded four-sets.

A permissible \((2,2)\) set has no deletable vertex. Conversely, any CDS of larger size can delete a chosen vertex while retaining a CDS. When both side counts are at least three, remove an arbitrary selected vertex from one side. When they are \((3,2)\) or \((2,3)\), at most one of the three possible deletions on the larger side results in the forbidden equal two-subsets; choose another. Repeating gives a proper CDS subset. Thus the inclusion-minimal sets are precisely the admissible \((2,2)\) sets; each is indexed uniquely by \((A,B)\) with \(A\ne B\).

**2. Exchange graph and degrees.** Replacing one chosen vertex cannot change the number selected on each shore: every admissible minimum set contains exactly two from each. Therefore an exchange replaces one element of exactly one of \(A,B\), producing a Johnson edge while avoiding the diagonal. This is the induced off-diagonal Cartesian-square description. Each factor \(H_n\) has degree \(k\). For a fixed \((A,B)\), deleting the forbidden neighbor \((B,B)\) from first-coordinate moves and \((A,A)\) from second-coordinate moves removes two edges exactly when \(A\) and \(B\) are adjacent in \(H_n\). There are \(vk\) ordered adjacent pairs and \(vq\) ordered disjoint pairs. The degree claims follow; the handshake lemma gives \(vk(v-2)\) edges. A token slide would exchange vertices in opposite bipartition classes of \(G_n\), breaking the required two-per-shore counts, so no slide exists.

**3. Exact distance formula.** In \(H_n\), \(\delta(A,C)=2-|A\cap C|\) is the shortest-path distance. If this distance is two, there are exactly four common neighbors of \(A,C\), each selecting one element of \(A\) and one of \(C\). All paths in the off-diagonal Cartesian square have length at least \(\delta(A,C)+\delta(B,D)\). We now construct paths meeting this lower bound except for the stated adjacent swap.

If just one coordinate changes, a length-one move is legal because the destination is off-diagonal; for a length-two move choose an intermediate common neighbor avoiding the other fixed coordinate (at least three of the four suffice). If both coordinate distances are one, moving the first coordinate then the second works unless \(C=B\); reversing the order works unless \(D=A\). The sole case where both orders fail is the swap \((C,D)=(B,A)\) with \(A,B\) Johnson-adjacent. A two-step route is then impossible; choosing any common Johnson neighbor \(E\ne A,B\) yields the legal three-step route \((A,B)\to(E,B)\to(E,A)\to(B,A)\).

If the coordinate distances are two and one, choose a common neighbor \(E\) of the two distance-two endpoints avoiding both fixed second-coordinate endpoints. Of the four possibilities at least two remain. The route through \((E,B)\), then \((E,D)\), then the target has length three and stays off-diagonal; the reversed case is symmetric. If both coordinate distances are two, choose a common neighbor \(E\) of \(A,C\) different from \(B\). Choose a common neighbor \(F\) of \(B,D\) different from \(E,C\). With four common neighbors per distance-two pair, both choices exist, and \((A,B)\to(E,B)\to(E,F)\to(C,F)\to(C,D)\) is a valid length-four path. Finally, identical endpoints require no moves. These cases prove the metric formula, connectivity, and the claimed diameters (for \(n=3\) the off-diagonal square of a triangle is a six-cycle; for \(n\ge4\) distance-four pairs exist).

**4. Ordered-pair distance enumerator.** In the full Cartesian square \(H_n\square H_n\), there are \(v^2g(t)^2\) ordered endpoint pairs at each weighted sum of coordinate distances. To restrict both endpoints to the off-diagonal vertex set, subtract pairs whose start lies on the diagonal and pairs whose finish lies on the diagonal, giving \(-2vg(t)^2\); add back the intersection where both endpoints are diagonal, contributing \(vg(t^2)\). This yields \(v(v-2)g(t)^2+vg(t^2)\) with the *coordinate-sum* metric. Exactly \(vk\) ordered endpoint pairs are adjacent-coordinate swaps, and those change distance from two to three, adding \(vk(t^3-t^2)\). Expanding establishes the formula and every distance-shell coefficient.

## Verification

The self-contained standard-library program `verify.py` constructs each crown graph from its original adjacency predicate, tests every nonempty vertex subset against domination and induced connectivity for \(3\le n\le7\), and compares all cardinality coefficients with the displayed CDS polynomial. It independently extracts all inclusion-minimal CDS, builds the token-exchange graph by symmetric difference, performs breadth-first search from every reconfiguration state, and compares all distances and the full ordered-pair profile. It prints `VERIFY_OK` only if all assertions succeed. The proof above, rather than the finite computations, establishes the assertions for every \(n\ge3\).

## Relationship to prior work

The known minimum connected domination size and its exact crown-graph configuration count are explicitly attributed to the 2017 crown-graph annotation of OEIS A033487; they are not the originality claim. Mynhardt and Nasserasr (2020, arXiv:2003.05956) describe dominating-set reconfiguration and Johnson-graph relationships at a general level, without giving this particular off-diagonal product metric or distance-shell enumerator. Abu-Khzam (2021, arXiv:2111.06026), Abu-Khzam and collaborators (2022, arXiv:2205.00086), and Sayadi (2019, arXiv:1908.02174) study connected-dominating-set enumeration and upper bounds, including related bipartite constructions, but their inspected results concern other host graphs, general algorithms, or bounds. The present focus is the all-pairs metric and exact distance distribution for exchanges among crown-graph minimum CDS. General two-particle configuration-space terminology is a possible equivalent formulation, and publication priority beyond the inspected sources is unresolved.

## Limitations

There is no independent mathematical audit or exhaustive literature census. In particular, an earlier unindexed theorem about two labeled noncolliding tokens on Johnson graphs could imply the reconfiguration metric and enumerator even without referencing crown graphs. The new asserted value is the exact integrated structural/distance classification; the known scalar minimum and its count are prior facts. The verifier checks finite orders, not the infinite theorem.

## References

1. OEIS, sequence A033487, annotation dated June 29, 2017: number of minimum connected dominating sets in crown graphs. https://oeis.org/A033487
2. C. M. Mynhardt and S. Nasserasr, *Reconfiguration of Colourings and Dominating Sets in Graphs: a Survey* (2020), arXiv:2003.05956. https://arxiv.org/abs/2003.05956
3. F. Abu-Khzam, *A Note on the Maximum Number of Minimal Connected Dominating Sets in a Graph* (2021), arXiv:2111.06026. https://arxiv.org/abs/2111.06026
4. F. Abu-Khzam et al., *Enumerating Connected Dominating Sets* (2022), arXiv:2205.00086. https://arxiv.org/abs/2205.00086
5. M. Y. Sayadi, *On the maximum number of minimal connected dominating sets in convex bipartite graphs* (2019), arXiv:1908.02174. https://arxiv.org/abs/1908.02174
