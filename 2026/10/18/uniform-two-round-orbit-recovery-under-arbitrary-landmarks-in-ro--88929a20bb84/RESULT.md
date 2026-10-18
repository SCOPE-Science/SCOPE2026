# Uniform two-round orbit recovery under arbitrary landmarks in rook graphs

## Finding

Let \(m,n\ge 2\), and let \(R_{m,n}=K_m\square K_n\) be the finite rook graph on \([m]\times[n]\). Two different squares are adjacent precisely when they share a row or a column. Choose **any** set \(F\subseteq[m]\times[n]\), possibly empty, and assign each member of \(F\) its own distinct initial colour. All other vertices share an initial colour. Apply ordinary synchronous one-dimensional counting colour refinement, retaining old colours at each round.

**Theorem.** At the end of at most two rounds, the resulting colour classes are exactly the orbits of the pointwise stabilizer \(\operatorname{Aut}(R_{m,n})_{(F)}\). Thus the answer remains exact for arbitrarily many, arbitrarily arranged individually marked squares. This is a within-graph orbit theorem, not an assertion that the graph is identified among arbitrary graphs by two-variable counting logic.

Let \(a\) and \(b\) denote the numbers of rows and columns, respectively, touched by \(F\). Put
\[
 A=a+\mathbf1_{a<m},\qquad B=b+\mathbf1_{b<n}.
\]
If \(m\ne n\), or if \(F\) is **not** a nonattacking rook placement (two marked squares share a row or a column), the exact number of stable classes is \(AB\). If \(m=n\) and no two members of \(F\) share a row or a column (including \(F=\varnothing\)), it is
\[
 \boxed{\binom{A+1}{2}}.
\]
The formulas remain valid when all rows or all columns are touched.

Class sizes are equally explicit. Outside the square nonattacking case, each row category is either one individually fixed occupied row or the set of \(m-a\) untouched rows; column categories are analogous, of sizes \(1\) and \(n-b\). The class indexed by a row category of size \(u\) and a column category of size \(v\) has \(uv\) vertices. In the square nonattacking case, let the \(A\) row-category weights be \(w_1,\ldots,w_A\), each equal to \(1\) for an occupied row and (when present) \(n-a\) for the untouched rows. The class indexed by \(\{i,j\}\) has size \(w_i^2\) when \(i=j\) and \(2w_iw_j\) otherwise.

**Sharpness.** Two rounds cannot be replaced by one uniformly. In every nonsquare \(R_{m,n}\), individualizing a single square leaves its row-neighbours and column-neighbours together after one round although they belong to different stabilizer orbits. A square-board example is \(R_{4,4}\) with \(F=\{(0,0),(0,1),(1,2)\}\): round one has \(11\) classes while round two and the orbit partition have \(12\).

## Assumptions and scope

The graph relation is ordinary undirected adjacency, **not** three separately named row/column/symbol equivalence relations. Indices can start at zero or one. Each marked vertex receives a **different** initial colour; markers are fixed pointwise rather than merely setwise. A round records a vertex's previous colour and the multiset of previous colours on its open neighbourhood. A colour class always means an equivalence class, not a particular numerical implementation of colour IDs.

For \(m,n\ge2\), the full graph automorphism group consists of independent row and column permutations, together with global interchange of the two coordinate families only if \(m=n\). For dimensions at least three this follows from the maximal row and column cliques and their intersection pattern; when one dimension is two, the longer cliques determine the corresponding family; the \(2\)-by-\(2\) case is the four-cycle, whose dihedral group has the same description. Individual markings restrict this group as in the proof below.

## Proof

**Step 1: describe every pointwise-stabilizer orbit.** Write \(F=\{f_1,\ldots,f_t\}\), with \(f_i=(r_i,c_i)\). Every row containing a mark is fixed by any coordinate-preserving automorphism that fixes every \(f_i\); all untouched rows may be freely permuted. The same holds for columns. Thus coordinate-preserving stabilizer orbits are the Cartesian products of the row and column categories described above.

A coordinate interchanging automorphism of a square board can fix all marks if and only if no two marks share a row or column. Necessity: if two distinct marks share a row, the interchanged images would share a column, impossible if both are fixed; the column case is symmetric. Sufficiency: if the marks form a nonattacking placement, the bijections sending each occupied row to the same marked cell's occupied column (and vice versa), extended arbitrarily on untouched coordinates, produce an interchange fixing all marks. This interchange takes the orbit cell indexed by \((i,j)\) to that indexed by \((j,i)\). Hence the stated orbit counts and sizes follow in both cases.

**Step 2: distinguish the coordinate categories when \(m\ne n\).** After round one, the colour of a vertex determines, for every \(i\), whether that vertex is \(f_i\), adjacent to \(f_i\), or neither. For any vertex \(x\), round two consequently determines
\[
 c_i(x)=|N(x)\cap N(f_i)|,
\]
because adjacency to \(f_i\) is a union of first-round colour classes and round two counts neighbours in each such class. If an unmarked \(x\) is adjacent to \(f_i\), then
\[
 c_i(x)=\begin{cases}n-2,&x\text{ shares a row with }f_i,\\m-2,&x\text{ shares a column with }f_i.\end{cases}
\]
No further common neighbours occur in either case. These two integers differ when \(m\ne n\), and first-round adjacency separates both from the nonadjacent case. Thus the second-round signature determines separately the set of marked row indices and the set of marked column indices agreeing with \(x\), exactly identifying the row and column categories. The marked vertices are already singletons. The second-round partition therefore refines the orbit partition and, by automorphism invariance, equals it.

**Step 3: square boards with nonattacking marks.** Suppose \(m=n\) and the marked squares lie in pairwise distinct rows and columns. Each unmarked square is adjacent to either zero, one, or two distinct marked squares. Its first-round signature determines the **unordered** pair of row- and column-category labels: an adjacency to two marks labelled \(i,j\) forces the unordered pair \(\{i,j\}\); an adjacency only to \(i\) forces \(\{i,*\}\), where \(*\) denotes untouched coordinates; and zero adjacencies forces \(\{*,*\}\). The two orientations of an off-diagonal category pair are exchanged by a coordinate-interchanging automorphism fixing every mark. Hence round one already equals the stabilizer-orbit partition. The empty-mark case is uniform and is already stable at round zero.

**Step 4: square boards with attacking marks.** Choose two marked squares \(f_i,f_j\) sharing a row \(L\); the shared-column case follows by symmetry. The entire row \(L\) is a union of first-round colour classes: it consists of these two marked squares together with all their common neighbours. In a rook graph, the common neighbours of two distinct squares sharing a row are exactly the other squares in that row, including for a board of size two.

For each marked square \(f_s\notin L\), the set \(L\cap N(f_s)\) is the **single** square \(w_s\) in row \(L\) and column \(c_s\). Both \(L\) and \(N(f_s)\) are unions of first-round classes, so \(w_s\) is a first-round singleton, whether or not it was initially marked.

We now recover for every vertex \(x\) whether its column equals \(c_s\). If \(f_s\in L\), the answer is \(x=f_s\) for \(x\in L\), and otherwise it is \(x\sim f_s\). If \(f_s\notin L\), the answer is \(x\sim f_s\) for \(x\in L\), and otherwise it is \(x\sim w_s\). Every test used here is visible by round two because all \(f_s\) and \(w_s\) are already first-round singletons, while membership in \(L\) is first-round visible. Once the column coincidences are recovered, the row coincidences with marked squares follow from adjacency to \(f_s\): for \(x\ne f_s\), it shares the marked row if and only if it is adjacent to \(f_s\) and does **not** share \(f_s\)'s column. The case \(x=f_s\) is explicit. Thus round two recovers the ordered row/column-category pair, which is the complete orbit invariant in this case.

**Step 5: optimality of the uniform bound.** In a nonsquare board, a single marked square has both a row-neighbour and a column-neighbour; both are adjacent to the sole marker and consequently have identical first-round colours. But the dimension mismatch prevents a coordinate interchanging automorphism, so these vertices are not in the same orbit. For the square example in the finding, \((1,3)\) and \((2,2)\) are both unmarked and each is adjacent to exactly the third mark \((1,2)\), so they have identical first-round colours. They have different ordered row/column categories, and no coordinate interchange fixing the three marks exists because the first two marks share a row. Step 4 separates them by round two. This proves sharpness. \(\square\)

## Verification

Run \(\texttt{python3 verify_refinement.py}\) and \(\texttt{python3 verify_orbits.py}\). The first independently computes colour refinement and the predicted orbit partition for all initial marked sets of size at most three on all boards of dimensions \(2\) through \(4\) by \(2\) through \(5\), followed by reproducibly seeded additional larger cases. It checks both the two-round bound and two sharpness witnesses. The second enumerates explicit coordinate-preserving and interchange automorphisms on smaller boards and compares their pointwise stabilizer orbits to the closed formulas. The expected output tokens are recorded in \(\texttt{verification_output.txt}\); tests are finite corroboration only.

## Relationship to prior work

Arvind, Köbler, Rattan and Verbitsky establish a hierarchy of colour-refinement properties and prove that Johnson graphs \(J(n,2)\), i.e. line graphs of complete graphs, are Tinhofer. Their Appendix 0.A.2 classifies the orbits after arbitrary individualizations in that **different** graph family. The present result treats line graphs of complete **bipartite** graphs, allows rectangular boards and arbitrary landmarks, and additionally gives a sharp uniform **two-round** bound and an explicit orbit census. Neither the theorem for complete-graph line graphs nor its proof directly implies the same statement for induced cross-edge subgraphs. Kiefer, Schweitzer and Selman establish the broader two-variable counting-logic setting and the distinction between orbit refinement and graph identification. Product-graph and distinguishing-colouring references concern different invariants, rather than the two-round quantitative refinement claim.

## Limitations

This concerns the orbit partition inside the specified marked rook graph, not isomorphism identification among arbitrary competing graphs. No assertion is made about higher-dimensional Hamming graphs or general line graphs of bipartite graphs. The result is not a characterization of the colour-refinement behaviour of arbitrary non-singleton initial colour classes. Its exact scientific priority against all possible older specialist sources has not been independently established.

## References

1. V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (first posted 4 February 2015), especially Section 8 and Appendix 0.A.2. https://arxiv.org/abs/1502.01255
2. S. Kiefer, P. Schweitzer and E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792 (first posted 30 March 2015), particularly Sections 1–2. https://arxiv.org/abs/1503.08792
3. W. Imrich, J. Jerebic and S. Klavžar, *The distinguishing number of Cartesian products of complete graphs*, Electronic Journal of Combinatorics (2008). Used as contextual prior literature on coordinate-product symmetries, not as a colour-refinement result.
