# Unique matching and minimum paired-domination census of cycle prisms in the \(2\pmod 3\) class

## Finding
Let \(P_n=C_n\square K_2\), with vertices \((i,r)\) for \(i\in\mathbb Z/n\mathbb Z\) and \(r\in\{0,1\}\), horizontal edges \((i,r)(i+1,r)\), and vertical rungs \((i,0)(i,1)\). A paired-dominating set \(S\) is a dominating vertex set for which the induced graph \(P_n[S]\) has a perfect matching. Let \(\gamma_{\mathrm{pr}}\) denote the minimum size of such a set, and let \(a_n\) count distinct minimum paired-dominating **vertex sets**, not choices of matchings.

**Theorem.** For every integer \(m\ge1\), put \(n=3m+2\) and \(k=m+1\). Then
\[
\gamma_{\mathrm{pr}}(P_n)=2k=\frac{2(n+1)}3,
\qquad
 a_n=n(2k+1)=\frac{n(2n+5)}3.
\]
Moreover, **every** minimum paired-dominating set has exactly one perfect matching in its induced subgraph. The matching's edge-start columns, in cyclic order, have exactly one gap of length two and \(k-1\) gaps of length three. For any fixed position of the unique short gap, there are exactly \(2k+1\) allowable edge-type sequences, described explicitly below. In particular \(a_5=25\), \(a_8=56\), \(a_{11}=99\), \(a_{14}=154\), and \(a_{17}=221\).

## Assumptions and scope
The graphs are finite simple cycle prisms with labelled columns and rows and \(n=3m+2\ge5\). An edge of type \(V_i\) is the rung in column \(i\), of type \(T_i\) is the top-row edge between columns \(i,i+1\), and of type \(B_i\) is the analogous bottom-row edge. Its *start column* is \(i\), irrespective of type. Counts distinguish vertex subsets in the fixed labelled graph; they do not quotient by rotations, reflections or layer exchanges. No assertion about the minimum-set count in the other two residue classes is made.

## Proof
**1. A tight cover.** Choose a perfect matching \(M\) in any paired-dominating set \(S\). If \(|S|=2q\), the \(q\) edges of \(M\) have disjoint endpoint sets. For any edge \(e=uv\), write \(Q_e=N[u]\cup N[v]\), its closed endpoint-neighborhood. Each \(Q_e\) has exactly six vertices when \(n\ge5\). As \(S\) dominates, \(\bigcup_{e\in M}Q_e=V(P_n)\), so \(2n\le6q\), hence \(q\ge\lceil n/3\rceil=k\). At equality \(q=k\), the sum of covering multiplicities minus the number of vertices equals \(6k-2n=2\). We call this the **overlap budget**.

**2. Columns and gaps.** The shapes \(Q_{V_i}\), \(Q_{T_i}\), \(Q_{B_i}\), respectively, cover these column-row sets (indices cyclic):

- \(V_i\): both rows in columns \(i-1,i,i+1\).
- \(T_i\): top row in \(i-1,i,i+1,i+2\), and bottom row in \(i,i+1\).
- \(B_i\): the row-swapped version of \(T_i\).

Two matching edges with the same start column would have to be \(T_i,B_i\), whose shapes overlap in four vertices. Edges with consecutive start columns are either incompatible as matching edges or have shapes intersecting in at least four vertices. Both contradict the overlap budget. Thus consecutive cyclic start-column gaps are at least two. A gap of four or more is impossible: at the column two positions after the preceding start, the preceding shape leaves at least one row uncovered, and no shape starting outside this gap can cover that vertex. Hence every cyclic gap equals two or three. Since there are \(k\) starts in \(n=3k-1\) columns, precisely one gap is two and the other \(k-1\) gaps are three.

Rotate columns so the edge preceding the short gap begins at \(0\). The ordered starts then are \(0,2,5,8,\ldots,3k-4\), modulo \(n\). Write their types as \(t_0,t_1,\ldots,t_{k-1}\in\{V,T,B\}\). Across any gap of three, complete coverage of the middle boundary column forces one of the transitions
\[
V\to V,\qquad T\to V,\quad T\to B,\qquad B\to V,\quad B\to T.
\]
These are also sufficient to avoid uncovered vertices along that gap. The respective shape overlaps are \(0,1,0,1,0\). Across the one gap of two, the intersection sizes between the preceding type (row) and the following type (column) are
\[
\begin{array}{c|ccc}
 &V&T&B\\\hline
V&2&1&1\\
T&3&2&2\\
B&3&2&2
\end{array}.
\]
The \(T\to V\) and \(B\to V\) short-gap possibilities violate the budget. All other entries are compatible with covering that gap. With the cyclic three-gap transition rule, the displayed overlap counts add to exactly two, which verifies global coverage as well as necessity. Every listed assignment consists of pairwise vertex-disjoint matching edges because all their start columns differ by at least two.

**3. Count type sequences.** If \(t_0=V\), either all types are \(V\), or \(t_1\) is chosen to be \(T\) or \(B\). In the latter case, the types alternate \(T,B,T,\ldots\) until some final nonvertical index \(j\in\{1,\ldots,k-1\}\), after which all entries are \(V\). The cyclic last-to-first gap of three supplies the required single nonvertical-to-vertical transition and consumes the remaining unit of overlap. This gives \(1+2(k-1)\) sequences. If \(t_0\in\{T,B\}\), no subsequent entry can be vertical: vertical-to-nonvertical is forbidden across a gap of three. All entries after \(t_1\) must alternate top and bottom, and the final-to-first three-gap transition uniquely determines \(t_1\) for each of the two choices of \(t_0\). Thus there are two more sequences. In total, there are \(2k+1\) per position of the unique short gap. There are exactly \(n\) possible positions, hence \(n(2k+1)\) dominating matchings with \(k\) edges. In particular at least one exists, giving the upper bound \(\gamma_{\mathrm{pr}}(P_n)\le2k\).

**4. Distinct vertex sets and unique matchings.** Suppose a minimum paired-dominating vertex set \(S\) supported two distinct perfect matchings. Their symmetric difference would contain an alternating cycle of length at least four. Fix one matching and its shape cover \(\{Q_e\}\). Every vertex on that alternating cycle lies in the shape of its own matched edge and in the shape of another matched edge, because an edge of the second matching joins it to a vertex belonging to a different first-matching edge. Consequently at least four vertices have cover multiplicity at least two, contradicting the overlap budget of two. Thus every minimum set has a **unique** induced perfect matching, and counting matching edge sets also counts distinct vertex sets. This establishes the claimed formula.

## Verification
The package includes two source-only checkers with distinct search spaces. Compile and run `verify_minima.cpp` using `g++ -O3 -std=c++17 verify_minima.cpp -o verify_minima && ./verify_minima` for direct exhaustive enumeration of labelled vertex subsets, testing domination and recursively testing the existence of an induced perfect matching, at \(n=5,8,11,14,17\). Run `python3 verify_shapes.py` for an independent exhaustive enumeration of disjoint matching edges whose endpoint-neighborhoods cover the prism, at \(n=5,8,11,14\). Both checkers returned `VERIFY_OK`; the first observed counts \(25,56,99,154,221\), and the second \(25,56,99,154\) with exactly the asserted gap pattern. These finite checks are corroboration, **not** a substitute for the four-step all-\(m\) proof above.

## Relationship to prior work
Lu and Wu (arXiv:2609.30152v1, first released 24 September 2026) prove a sharp upper bound for the **minimum cardinality** of paired-dominating sets in arbitrary cubic bipartite graphs. Even-index cycle prisms form a subfamily, but an upper bound on the cardinality does not enumerate optimal vertex sets or imply their unique perfect-matching property. Mynhardt and Schurch (2011) investigate paired domination in general prism graphs and characterize selected equality relations between paired-domination numbers; its abstract does not establish the present size-refined census. Allagan (2026) counts *ordinary* minimum dominating sets in cycle prisms, without requiring an induced perfect matching. The exact census here is not a reformulation of ordinary dominion.

## Limitations
The result is restricted to cycle-prism circumferences congruent to two modulo three. It counts labelled vertex sets, not automorphism orbits. The source search did not establish historical uniqueness: notably, the full text of the 2011 prism paper could not be examined, so a previously unrecognized equivalent count remains possible. This is a self-contained mathematical proof and computational corroboration, not independent external validation.

## References
1. C. Lu and Q. Wu, *Paired Domination in Cubic Bipartite Graphs*, arXiv:2609.30152v1 (24 September 2026), https://arxiv.org/abs/2609.30152.
2. C. M. Mynhardt and M. Schurch, *Paired domination in prisms of graphs*, Discussiones Mathematicae Graph Theory **31** (2011), 5–23, DOI:10.7151/dmgt.1526.
3. H. Allagan, *Exact Dominion of the Prism Graph: Enumeration by Congruence Class via Cyclic Words*, International Journal of Mathematics and Mathematical Sciences (2026), DOI:10.1155/ijmm/1411005.
4. T. W. Haynes and P. J. Slater, *Paired-domination in graphs*, Networks **32** (1998), 199–206.
