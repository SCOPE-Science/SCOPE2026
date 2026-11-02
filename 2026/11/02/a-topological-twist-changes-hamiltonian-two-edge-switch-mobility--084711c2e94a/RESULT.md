# A topological twist changes Hamiltonian two-edge-switch mobility from isolated states to a star

## Finding
For an integer \(n\geq5\), form two cubic graphs with vertex set \(\{(i,a):0\leq i<n,\ a\in\{0,1\}\}\). Include the rung \((i,0)(i,1)\) for every \(i\) and the horizontal edges \((i,a)(i+1,a)\) for \(0\leq i<n-1\). Complete the two rows either by *parallel* seams \((n-1,a)(0,a)\), obtaining the circular ladder \(P_n=C_n\square K_2\), or by *crossed* seams \((n-1,a)(0,1-a)\), obtaining the Möbius ladder \(M_n\) on \(2n\) vertices.

Let \(\mathscr H(G)\) be the graph whose vertices are the **unoriented Hamiltonian cycles, identified with their edge sets**, of \(G\). Two such cycles are adjacent when one is obtained from the other by deleting exactly two edges and inserting exactly two different edges, without losing Hamiltonicity (a Hamiltonian two-edge switch). Equivalently, their symmetric difference is an alternating four-cycle.

**Theorem.** For every \(n\geq5\),
\[
\mathscr H(P_n)\cong
\begin{cases}
 nK_1,&n\text{ odd},\\
 (n+2)K_1,&n\text{ even},
\end{cases}
\qquad
\mathscr H(M_n)\cong
\begin{cases}
 K_{1,n}\sqcup2K_1,&n\text{ odd},\\
 K_{1,n},&n\text{ even}.
\end{cases}
\]
In particular, every Hamiltonian cycle of the cylindrical ladder is frozen under single two-edge switches, whereas the twisted ladder has a distinguished rim cycle joined by one switch to \(n\) distinct two-rung cycles. When \(n\) is odd, exactly two additional all-rung Hamiltonian cycles of the Möbius ladder remain frozen; when \(n\) is even, the Möbius-ladder switch graph is connected and has diameter two.

The known total Hamiltonian-cycle counts \(n\), \(n+2\), \(n+1\), and \(n+3\) are **not** advanced as new. The finding is the complete graph of admissible local Hamiltonian switches and its strong dependence on the seam twist.

## Assumptions and scope
All graphs are simple, finite, undirected and unweighted. A Hamiltonian cycle is one spanning simple cycle, *not* an oriented or rooted traversal. The two-edge switch must result in another spanning single cycle; a switch that splits a cycle into two or more circuits is illegal. The formulas apply to all integers \(n\geq5\) without a parity or largeness qualification. The case \(n=4\) has additional horizontal four-cycles in \(P_4\) and is deliberately outside the uniform statement (both programs nevertheless check it).

The graphs have the same number of vertices, edges, degree sequence and corresponding rung quadrilaterals. The only distinction in their presentation is whether the two horizontal seams are crossed. This is precisely the operation of making a cylindrical strip into a Möbius strip.

## Proof
**Step 1: Convert Hamiltonian cycles into a matching condition on the horizontal edges.** Let \(H\) be a Hamiltonian cycle of either ladder and \(S\subseteq\mathbb Z/n\mathbb Z\) the set of column indices whose rungs are in \(H\). At a vertex in column \(i\notin S\), both incident horizontal edges must lie in \(H\). At a vertex in column \(i\in S\), precisely one of its two incident horizontal edges lies in \(H\). Consequently, the omitted horizontal edges form a matching whose endpoints are exactly the two vertices in each selected column, with no other endpoints. In particular, a missing horizontal edge connects vertices of consecutive selected columns only.

Suppose \(\varnothing\ne S\ne\mathbb Z/n\mathbb Z\). Starting at the boundary of a maximal cyclic run of selected columns, the first selected column has no selected neighbor beyond the boundary, so both its vertices are forced to omit the horizontal edges leading to the next column. The same two vertices of that next column are thereby already matched. Iterating shows that **each maximal run of \(S\) has even length** and that its missing horizontal edges are forced, in consecutive paired cuts. This is valid also when a run crosses the twisted seam: both horizontal edges in that cut simply cross the rows together. Thus \(H\) is specified by a nonempty collection of \(r=|S|/2\) distinct column cuts, with both horizontal edges of each selected cut removed and the two endpoint rungs inserted. These cuts are disjoint in their column endpoints; no other edges may change.

**Step 2: Count the circuits created by cuts.** If \(r\geq1\), delete the two horizontal edges at each chosen cut from the two-row strip before adding the rungs. Between any two consecutive chosen cuts there are two horizontal paths (possibly with an exchange of rows across the twisted seam). The two rungs at the interval's endpoints join those two paths into one closed circuit; paths for different intervals have disjoint vertices. This gives **exactly \(r\) disjoint circuits**, independently of the seam type. In particular, for a nonempty proper selected-rung set, the resulting spanning two-factor is Hamiltonian if and only if \(r=1\). These are exactly the \(n\) Hamiltonian cycles with rungs at two consecutive columns. Every one is uniquely indexed by the intervening column cut.

**Step 3: Handle the two extreme cases.** If \(S=\varnothing\), the horizontal edges give two separate \(n\)-cycles in \(P_n\), but one connected perimeter of length \(2n\) in \(M_n\). Thus the no-rung Hamiltonian cycle occurs only for the Möbius ladder.

If \(S=\mathbb Z/n\mathbb Z\), each vertex uses its rung plus exactly one horizontal edge. The selected horizontal edges must therefore form a perfect matching of the horizontal subgraph. For \(P_n\), that subgraph consists of two disjoint \(n\)-cycles: a perfect matching is possible only for even \(n\), and there are two alternating choices on each rail. Of the four joint choices, the two with opposite alternating phases produce a single \(2n\)-cycle; the two with equal phases decompose into small disjoint squares. Hence there are exactly two all-rung Hamiltonian cycles of \(P_n\) for even \(n\) and none for odd \(n\).

For \(M_n\), the horizontal subgraph is one \(2n\)-cycle and has exactly two perfect matchings. For even \(n\), each gives matching pairs on the two rails in the same phase, closing into \(n/2\) separate four-cycles. For odd \(n\), the twist offsets those phases; following the alternating rung and horizontal edges traverses all \(2n\) vertices before returning. Thus exactly two all-rung Hamiltonian cycles exist when \(n\) is odd, and none when \(n\) is even. Steps 1--3 classify **all** Hamiltonian cycles and recover the known static counts.

**Step 4: Classify the legal switches.** Deleting two cycle edges and adding two different edges while maintaining degree two at all vertices is possible precisely along an alternating four-cycle. For \(n\geq5\), every four-cycle of either ladder is one of its \(n\) rung quadrilaterals: two adjacent rungs and the pair of horizontal edges joining their columns. A square switch therefore changes the number of selected rungs by exactly two, never by zero.

The unique rim Hamiltonian cycle of \(M_n\) uses both horizontal edges in every rung quadrilateral and no rungs. Switching at any one of the \(n\) squares produces precisely the corresponding two-rung Hamiltonian cycle. Conversely, from a two-rung cycle, switching its defining square removes both rungs and returns the full horizontal subgraph. That is Hamiltonian for \(M_n\) and disconnected for \(P_n\). Switching a different square, if locally permitted at all, would create four rungs; by Step 2 it would give two circuits rather than a Hamiltonian cycle, except potentially if \(n=4\), which was excluded. Finally, an all-rung Hamiltonian cycle, when it exists, contains exactly one horizontal edge from each rung quadrilateral and hence has no alternating rung quadrilateral on which to switch. Every possible two-edge switch has now been considered.

Therefore the Möbius rim is adjacent to all \(n\) two-rung cycles and there are no other switch edges, while the cylindrical ladder has no switch edges at all. The two extra Möbius cycles when \(n\) is odd are isolated. This is exactly the asserted decomposition. \(\square\)

## Verification
Two complete, standalone Python programs accompany this statement:

- `check_matching.py` independently enumerates every perfect matching in the cubic graphs for \(4\leq n\leq18\), takes complements, tests Hamiltonicity by direct graph traversal, and connects any pair of Hamiltonian cycles whose symmetric difference has four edges. It checks every degree, edge count and connected-component size against the theorem (including the additional small case \(n=4\)). It does **not** use a preselected set of four-cycles.
- `check_dfs_templates.py` independently enumerates Hamiltonian cycles by vertex-by-vertex depth-first search for \(4\leq n\leq13\), constructs the explicit rim/two-rung/all-rung families, compares the actual edge sets, and reconstructs all Hamiltonian switches from the classified edge sets. It uses no perfect-matching enumeration.

Execute with standard Python 3: `python check_matching.py` and `python check_dfs_templates.py`. Their final success markers are `MATCHING_ENUMERATION_ALL_2_EDGE_SWITCHES_PASS` and `DFS_AND_EXPLICIT_TEMPLATES_PASS`. The finite checks are corroboration; Steps 1--4 supply the proof for every \(n\geq5\).

## Relationship to prior work
The Möbius ladders themselves originate with Guy and Harary (1967). Counting Hamiltonian cycles and other structures of Möbius ladders is historical work: McSorley (1998) and the compiled count in MathWorld cover the static number of cycles. Those counts are not claimed as new. Heinig (arXiv:1112.5101, first posted 2011-12-21), in particular his Theorem 15 and Lemma 17 and the discussion of prisms and Möbius ladders, studies the linear span of Hamiltonian cycles in graph cycle spaces, rather than the graph of one-step differences between Hamiltonian cycles. Takaoka (2018) gives the general Hamiltonian two-edge-switch operation and complexity/tractable-class theorems; the searchable full text of the 15-page article was checked for prism/Möbius-ladder terms and provides no corresponding component formula. More recent work on rectangular-grid Hamiltonian-cycle moves uses different (often double) switches and different boundary conditions.

The present statement concerns the **complete adjacency relation** under one legal switch, not the mere number of Hamiltonian cycles, the graph cycle-space span, or existence of a Hamiltonian tour. A static enumeration does not itself specify which pairs differ by one valid switch, and cycle-space generation is strictly weaker information about local reconfiguration. The theorem proves a sharp topological contrast: all states are frozen with parallel seams, while crossed seams create one degree-\(n\) hub, and for odd \(n\) two further frozen states.

## Limitations
The theorem does not address longer exchanges, multiple simultaneous square moves, randomly sampling Hamiltonian cycles, or generalizations to arbitrary cubic graphs. The full 1998 McSorley article could not be obtained; only the institutional abstract/bibliography and independently available Hamiltonian counts were accessible. Any unexamined switch discussion in that paper remains a possible historical-coverage risk. No claim of independent scholarly audit, publication priority, or comprehensive uniqueness is made.

## References
1. R. K. Guy and F. Harary, “On the Möbius Ladders,” *Canadian Mathematical Bulletin* **10** (1967), 493–496. DOI: 10.4153/CMB-1967-046-4.
2. J. P. McSorley, “Counting structures in the Möbius ladder,” *Discrete Mathematics* **184** (1998), 137–164. DOI: 10.1016/S0012-365X(97)00086-1.
3. P. C. Heinig, “On prisms, Möbius ladders and the cycle space of dense graphs,” arXiv:1112.5101 (first posted 2011-12-21); later *European Journal of Combinatorics* **36** (2014), 503–530.
4. A. Takaoka, “Complexity of Hamiltonian Cycle Reconfiguration,” *Algorithms* **11** (2018), article 140. DOI: 10.3390/a11090140.
5. A. Kazazi, “Reconfiguration of Hamiltonian Paths and Cycles in Rectangular Grid Graphs,” arXiv:2601.06749 (2026), for comparison of local versus double-switch formulations on open grids.
