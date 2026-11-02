# Optimal connected domination on circular ladders: complete exchange geometry

## Finding

Let \(P_n=C_n\square K_2\), with \(n\geq6\). Write \(\gamma_c(P_n)\) for its minimum connected dominating-set cardinality and let \(\mathcal R_n\) have all minimum connected dominating sets as vertices, with two adjacent precisely when one selected vertex is removed and one previously unselected vertex is inserted. Then

\[
\gamma_c(P_n)=n,\qquad |V(\mathcal R_n)|=2n^2+2,
\qquad |E(\mathcal R_n)|=4n(n+2).
\]

The configurations admit the complete, nonredundant classification A/B/C below. Their exchange graph is connected, has degree polynomial

\[
D_n(t)=\sum_{S\in V(\mathcal R_n)}t^{\deg(S)}
=2t^{2n}+4nt^6+4nt^5+2n(n-4)t^4,
\]

and the two complete-rail configurations are at exchange distance exactly \(n\).

## Assumptions and scope

Every graph here is finite, simple and undirected. Index the two rail levels by \(s\in\{0,1\}\) and the columns by \(i\in\mathbb Z/n\mathbb Z\). Vertices \((s,i)\) and \((s,j)\) are adjacent when \(j=i\pm1\) modulo \(n\), and \((0,i)\) is adjacent to \((1,i)\). A set \(S\) is *connected dominating* if \(P_n[S]\) is connected and every vertex outside \(S\) has a neighbor in \(S\). Exchange adjacency is the unrestricted one-for-one replacement relation (token jumping), not necessarily movement along a ladder edge.

Here is the exact classification, with all column arithmetic modulo \(n\):

* \(A_s\) consists of the entire level \(s\) rail, for \(s=0,1\).
* \(B_{y,d,s}\) has column \(y\) empty, column \(y+d\) doubly occupied, and every other column singly occupied; \(1\leq d\leq n-1\), \(s\in\{0,1\}\). If \(d=1\) or \(d=n-1\), all singletons are at level \(s\). Otherwise, columns \(y+1,\ldots,y+d-1\) have singleton level \(s\), and columns \(y+d+1,\ldots,y+n-1\) have singleton level \(1-s\).
* \(C_{y,s}\) has consecutive empty columns \(y,y+1\); doubly occupied columns \(y-1,y+2\); and all other columns singly occupied at level \(s\).

The three families contain respectively \(2\), \(2n(n-1)\), and \(2n\) distinct sets.

## Proof

**1. Optimal size and exhaustive classification.** Encode a column by \(0,U,L,X\) depending on whether it contains no selected vertex, only the upper, only the lower, or both. Let \(r\) be the number of empty columns. The occupied-column projection of a nonempty connected set is a connected subset of the column cycle. Thus, if \(r>0\), its empty columns form one consecutive run. Domination forbids three successive empty columns, since no selected vertex could dominate either vertex in the middle column; hence \(r\leq2\).

If \(r=0\), the size is at least \(n\); equality means one selected vertex per column, and connectivity then forces the same level throughout, yielding \(A_0,A_1\). If \(r=1\), the size is at least \(n-1\). A hypothetical size-\(n-1\) solution has only singletons, and connectedness forces them all to be on the same level along the occupied path; the vertex of the opposite level in the empty column is then undominated. Thus the size is at least \(n\). At equality exactly one occupied column is doubled. Removing that doubled column divides the occupied path into up to two strings of singleton columns; each nonempty string must be monochromatic for connectivity. If the doubled column is interior, domination of both vertices of the empty column forces the two singleton strings to be on opposite levels. If the doubled column is an endpoint, the other singleton string may have either level. This is precisely family \(B\), and each member is connected and dominating.

If \(r=2\), the two empty columns are consecutive. To dominate both vertices of either empty column, its sole adjacent occupied boundary column must be doubled. The other \(n-4\) occupied columns must be nonempty, forcing size at least \(n\). At equality, all nonboundary occupied columns are singletons, which have a common level by connectivity: these are exactly the configurations \(C\). They too are connected and dominating. Since each whole rail is connected dominating, the minimum is exactly \(n\), and there are no other minima. Counting the parameters gives \(2+2n(n-1)+2n=2n^2+2\).

**2. Complete exchange table.** Abbreviate a family label by \(A(s),B(y,d,s),C(y,s)\). All parameters on the first coordinate are modulo \(n\); each row lists **every** one-vertex-exchange neighbor. The following strings are labels of configurations, not additional assumptions.

| Source | All exchange neighbors |
| --- | --- |
| \(A(s)\) | \(B(y,1,s),B(y,n-1,s)\) for all \(y\) |
| \(C(y,s)\) | \(B(y,n-1,s), B(y+1,n-2,s), B(y+1,1,s), B(y,2,1-s)\) |
| \(B(y,1,s)\) | \(A(s), B(y,2,1-s), B(y+2,n-1,s), B(y-1,2,1-s), C(y-1,s), B(y,n-1,s)\) |
| \(B(y,n-1,s)\) | \(A(s), B(y+1,n-2,s), C(y,s), B(y-2,1,s), B(y,n-2,s), B(y,1,s)\) |
| \(B(y,2,s)\) | \(C(y,1-s), B(y+1,1,1-s), B(y,1,1-s), B(y,3,s), B(y-1,3,s)\) |
| \(B(y,n-2,s)\) | \(B(y+1,n-3,s), B(y,n-3,s), B(y,n-1,s), B(y-1,n-1,s), C(y-1,s)\) |
| \(B(y,d,s)\), \(3\leq d\leq n-3\) | \(B(y+1,d-1,s), B(y,d-1,s), B(y,d+1,s), B(y-1,d+1,s)\) |

To verify that the table is exhaustive for every \(n\geq6\), observe that a single exchange removes exactly one selected vertex and inserts exactly one omitted vertex. In the column-count representation, the only possible transitions between the A/B/C occupancy patterns are: transferring a vertex from a double to an empty column (possibly producing A); moving a single vertex into an empty column (shifting an empty boundary); moving a vertex out of a double into a formerly singly occupied column (moving the double); or moving a singleton to a second singleton (creating or moving the C double/empty pair). A same-column swap would merely flip one singleton level; such a flip disconnects its singleton path, or, at a one-column boundary, leaves one level in the empty column undominated. The empty-run bound, the requirement that both ends of a two-empty run be doubled, and the uniform/opposite singleton-level requirements proved in step 1 determine the available endpoints in each case. Exhausting the two endpoint cases, the two one-step-from-endpoint cases, and the interior case \(3\leq d\leq n-3\) yields precisely the seven rows. Conversely, checking the displayed column patterns shows that every listed neighbor differs by exactly one removed and one inserted vertex; it is feasible by step 1. In particular, no appeal to a finite sample is used in the all-parameter classification of exchanges.

**3. Degrees and edges.** The two \(A\) vertices have degree \(2n\). Among the \(B\) vertices, those at offsets \(d=1,n-1\) number \(4n\) and have degree six; those at \(d=2,n-2\) number \(4n\) and have degree five; and those with \(3\le d\le n-3\) number \(2n(n-5)\) and have degree four. All \(2n\) vertices of family \(C\) have degree four. Therefore the claimed degree polynomial holds. Summing its degree-weighted coefficients and halving gives \(4n(n+2)\) undirected edges.

**4. Connectivity and an exact distance.** Each \(B(y,d,s)\) can follow a monotone offset path in the table to a \(B\) with offset one or \(n-1\), and then reach a whole-rail state. Each \(C\) has a \(B\) neighbor. The two whole-rail states have an explicit path

\[
A(s)\longrightarrow B(y,1,s)\longrightarrow B(y,2,1-s)
\longrightarrow B(y,3,1-s)\longrightarrow\cdots\longrightarrow
B(y,n-1,1-s)\longrightarrow A(1-s).
\]

It has exactly \(n\) exchanges. Every exchange changes at most one selected vertex, while the two whole rails are disjoint sets of \(n\) vertices, so their distance is at least \(n\). The path attains this bound, and the reconfiguration graph is connected.

## Verification

The standalone programs `verify_direct.py` and `verify_templates.py` use only Python's standard library. Run `python verify_direct.py` and `python verify_templates.py` separately in the directory containing the files. The first constructs the original graph as adjacency bitsets, independently enumerates every candidate of sizes \(n-1\) and \(n\) for \(6\le n\le11\), tests both domination and induced connectivity, and builds every legal exchange. The second generates all A/B/C templates and independently forms all one-vertex exchanges for \(6\le n\le38\), comparing the actual neighbor sets with every line of the symbolic table and checking the graph's connectedness, degree polynomial, and edge count. They emit `DIRECT_ALL_SUBSETS_AND_EXCHANGES_PASS` and `ALL_ADJACENCY_RULES_AND_CONNECTIVITY_PASS`, respectively, when all assertions succeed. They supply exhaustive finite cross-checks, while the proof above is what covers every \(n\ge6\).

## Relationship to prior work

Connected domination is a classical graph parameter, and enumeration of minimal connected dominating sets and their reconfiguration are distinct established research themes. Schurch (2005) studies general connected-domination bounds, doublers, and fixers in prisms but does not classify these minimum circular-ladder backbones or their exchange graph. Chandran, Das, Rajendraprasad and Varma (2010) use connected domination to bound rainbow connection, but do not enumerate optimal backbone sets on prisms. Golovach, Heggernes and Kratsch (2015) give algorithms and extremal bounds for inclusion-minimal connected dominating sets on specified graph classes, rather than the exact minimum-size set census on the circular ladder. Suzuki, Mouawad and Nishimura (2014) study add/delete reconfiguration of ordinary dominating sets. Lokshtanov, Mouawad, Panolan and Siebertz (2020) treat the connected version under token addition/removal and prove general complexity results. Neither operation permits a one-for-one fixed-size exchange at exactly the minimum without changing the graph model. Allagan and collaborators' 2026 prism enumeration addresses ordinary domination, for which the feasible sets and minimum size differ. The contribution asserted here is the complete optimal connected-configuration classification together with its precise exchange graph invariants, not the introduction of connected domination or reconfiguration.

## Limitations

The theorem is restricted to the simple prism family \(C_n\square K_2\) with \(n\ge6\) and to one-for-one replacements without a graph-edge movement restriction. It does not determine the full reconfiguration diameter or shortest distances for arbitrary pairs. Exact historical uniqueness cannot be guaranteed, particularly if an equivalent result appeared under maximum-leaf spanning-tree, dominating-backbone, or alternative swap terminology. Independent expert validation has not been performed.

## References

1. M. Schurch, *Domination Parameters of Prisms of Graphs*, University of Victoria MSc thesis (2005), particularly Sections 2.3 and 3.5. https://dspace.library.uvic.ca/bitstream/1828/825/1/schurch_2005.pdf
2. L. Sunil Chandran, A. Das, D. Rajendraprasad, N. M. Varma, *Rainbow Connection Number and Connected Dominating Sets*, arXiv:1010.2296v1 (first public version 2010-10-12). https://arxiv.org/abs/1010.2296
3. A. Suzuki, A. E. Mouawad, N. Nishimura, *Reconfiguration of Dominating Sets*, arXiv:1401.5714v1 (2014-01-22). https://arxiv.org/abs/1401.5714
4. P. A. Golovach, P. Heggernes, D. Kratsch, *Enumerating Minimal Connected Dominating Sets in Graphs of Bounded Chordality*, IPEC 2015. https://doi.org/10.4230/LIPIcs.IPEC.2015.307
5. D. Lokshtanov, A. E. Mouawad, F. Panolan, S. Siebertz, *On the Parameterized Complexity of Reconfiguration of Connected Dominating Sets*, IPEC 2020. https://doi.org/10.4230/LIPIcs.IPEC.2020.24
6. *Exact Dominion of the Prism Graph: Enumeration by Congruence Class via Cyclic Words*, *International Journal of Mathematics and Mathematical Sciences* (2026). https://doi.org/10.1155/ijmm/1411005
