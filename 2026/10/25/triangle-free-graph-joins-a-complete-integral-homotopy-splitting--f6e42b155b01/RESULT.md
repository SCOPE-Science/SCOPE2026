# Triangle-free graph joins: a complete integral homotopy splitting for three-clique avoidance

## Finding
Let \(r\ge2\), and let \(G_1,\ldots,G_r\) be pairwise vertex-disjoint, nonempty finite simple **triangle-free** graphs. Write \(G=G_1\vee\cdots\vee G_r\) for their graph join (all edges between different factors), \(A_i=\operatorname{Ind}(G_i)\), and \(\operatorname{CF}_3(G)\) for the simplicial complex of vertex subsets inducing no triangle. Then there is an **integral homotopy equivalence**

\[
\boxed{\operatorname{CF}_3(G)\simeq
\bigvee^{\binom{r-1}{2}}S^1\ \vee\
\bigvee_{i=1}^{r}\bigvee^{r-1}\Sigma A_i\ \vee\
\bigvee_{1\le i<j\le r}(A_i*A_j).}
\]

Here \(\Sigma\) is unreduced suspension, \(*\) is simplicial join, and a wedge indexed by zero terms is omitted. The decomposition is a homotopy classification for **every** such graph join, not merely a homology or Euler-characteristic identity. In particular, arbitrary homotopy complexity in the individual independence complexes propagates through the specified suspensions and pairwise joins, with one universal degree-one contribution from the incidence pattern.

For a concrete infinite family, suppose \(G_i=C_{n_i}\) with \(n_i\ge4\). Set \(n_i=3k_i+e_i\) with \(0\le e_i\le2\), and define \(\rho_i=2\) for \(e_i=0\) and \(\rho_i=1\) otherwise, and \(\delta_i=k_i-1\) for \(e_i=0,1\), \(\delta_i=k_i\) for \(e_i=2\). Then
\[
\operatorname{CF}_3(C_{n_1}\vee\cdots\vee C_{n_r})\simeq
\bigvee^{\binom{r-1}{2}}S^1\vee
\bigvee_i\bigvee^{(r-1)\rho_i}S^{\delta_i+1}\vee
\bigvee_{i<j}\bigvee^{\rho_i\rho_j}S^{\delta_i+\delta_j+1}.
\]
Coincident sphere dimensions are combined by adding multiplicities. For example, three joined five-cycles give \(S^1\vee\bigvee^6S^2\vee\bigvee^3S^3\); four joined four-cycles give \(\bigvee^{21}S^1\).

## Assumptions and scope
Graphs are finite, simple, undirected, and nonempty, with vertex-disjoint factors. A face of \(\operatorname{CF}_3\) is exactly a vertex subset containing no three pairwise adjacent vertices. The graph join \(\vee\) should not be confused with a disjoint union. The simplicial join of two complexes on disjoint vertices is denoted \(*\). Homotopy is of geometric realizations; all coefficients underlying the statement are integral, with no localization or characteristic assumption. An independence complex contains all independent vertex sets, including the empty face. The cycle example excludes triangles, since \(C_3\) is not triangle-free.

## Proof
**Step 1: classify every face.** Write \(V_i=V(G_i)\) and \(\Delta_i=\Delta(V_i)\) for the full simplex on that vertex set. A face cannot meet three factors, because any three vertices from distinct factors form a triangle in the graph join. If it meets exactly two factors \(i,j\), it may contain no internal edge in either one, because such an edge plus a vertex of the other factor would be a triangle. Conversely, independent choices from precisely two factors make no triangles, and every subset of a single factor is admissible because that factor is triangle-free. Thus there is the exact equality of simplicial complexes
\[
\operatorname{CF}_3(G)=P\cup\bigcup_{i=1}^{r}\Delta_i,
\qquad P=\bigcup_{1\le i<j\le r}(A_i*A_j).
\]
The intersection \(P\cap\Delta_i=A_i\). The interiors of the distinct \(\Delta_i\) are disjoint, and their geometric realizations share no vertices.

**Step 2: split the pairwise-join core.** Consider the incidence category with objects the singleton indices \(i\) and unordered pairs \(ij\), and with its only nonidentity arrows \(i\to ij\) and \(j\to ij\). Give these objects spaces \(A_i\) and \(B_{ij}=A_i*A_j\), with the usual simplicial inclusions. Its colimit is \(P\). Since the category has no composable nonidentity arrows, and the latching map \(A_i\sqcup A_j\hookrightarrow B_{ij}\) is a simplicial cofibration for each \(ij\), the diagram's homotopy colimit maps by a homotopy equivalence to \(P\) (equivalently use the elementary mapping-cylinder construction for a graph of spaces).

Every arrow \(A_i\hookrightarrow B_{ij}\) is nullhomotopic: choose one vertex of \(A_j\); the inclusion factors, up to homotopy, through the cone \(A_i*\{v_j\}\) inside \(B_{ij}\). The diagram therefore has the same homotopy colimit as one with all incidence arrows constant; there is no higher composition-compatibility issue. Each \(B_{ij}\) is path connected because it is a join of two nonempty complexes.

For completeness, evaluate the constant-map graph of spaces. Choose a spanning tree in its connected bipartite incidence graph. Contracting the tree arcs identifies one basepoint in each \(B_{ij}\); at a singleton node \(i\) of degree \(r-1\), the \(r-1\) outgoing mapping cylinders contribute \(r-2\) unreduced suspensions of \(A_i\). Each non-tree incidence arc contributes one independent circle. The incidence graph has \(r+\binom r2\) nodes and \(2\binom r2\) edges, so its first Betti number is \(\binom{r-1}{2}\). The remaining vertex spaces are all the \(B_{ij}\). Consequently
\[
P\simeq \bigvee_{i<j}(A_i*A_j)\vee
\bigvee_i\bigvee^{r-2}\Sigma A_i\vee
\bigvee^{\binom{r-1}{2}}S^1.
\]
This also holds for disconnected \(A_i\), since the suspensions here are unreduced; no connectedness of any \(A_i\) was assumed.

**Step 3: attach the full factor simplices.** Each \(\Delta_i\) is contractible and attaches to \(P\) along the cofibration \(A_i\hookrightarrow P\). Since \(r\ge2\), this attaching map is nullhomotopic already inside \(A_i*A_j\subseteq P\) for some \(j\ne i\), by the cone constructed in Step 2. Attaching a contractible complex along a nullhomotopic cofibration is homotopy equivalent to wedging on \(\Sigma A_i\). The attachments for different \(i\) have disjoint interiors and can be performed successively; the nullhomotopies remain valid throughout. Hence
\[
\operatorname{CF}_3(G)\simeq P\vee\bigvee_i\Sigma A_i,
\]
which combines with Step 2 to give exactly \(r-1\) suspensions of each \(A_i\), proving the displayed general formula.

**Step 4: explicit cycle family.** The established independence-complex recurrence \(\operatorname{Ind}(C_n)\simeq\Sigma\operatorname{Ind}(C_{n-3})\), together with its initial cases, gives \(\operatorname{Ind}(C_{3k})\simeq S^{k-1}\vee S^{k-1}\), \(\operatorname{Ind}(C_{3k+1})\simeq S^{k-1}\), and \(\operatorname{Ind}(C_{3k+2})\simeq S^k\). Substituting these into the general formula and distributing suspension and joins across wedges gives the explicit family. For spheres, \(S^a*S^b\simeq S^{a+b+1}\). This finishes the proof.

## Verification
The included `verify.py` constructs cycle graph joins by their edges, generates all triangles directly from those edges, enumerates every nonempty subset without a triangle, and computes all reduced mod-two homology groups using signed simplicial incidence reduced modulo two. Its ten cases have between two and four cycle factors and include cycle lengths four, five, and six; it enumerates 2,784 nonempty simplices in total and matches the formula in every nonzero homological degree. Running `python3 verify.py` ends in `ALL_PASS cases 10 faces 2784`; exact output appears in `verification-output.txt`. This provides finite independent checks of the stated face definitions, not a substitute for the all-size integral homotopy proof.

## Relationship to prior work
Ghosh and Selvaraja, *Shellability in Clique-Free Complexes of Graphs* (arXiv:2602.09623v1, first submitted 2026-02-10), define these clique-free complexes and establish, in Proposition 3.2, a simplicial-join formula for **disjoint unions** of graphs. Their Theorem 3.3 concerns shellability of diamond-free chordal graphs, and the clique-attachment results address a different graph operation. The present graph-join formula involves dense cross edges, nonchordal triangle-free factors, and computes the complete integral homotopy type. Disjoint-union functoriality does not imply this result. The method uses standard homotopy colimits and mapping-cone splittings, not a claim of novelty for these general tools.

The previously studied internally matched multipartite special family is recovered by taking two factors to be disjoint unions of edges and any remaining factors to be isolated vertices. This is a proper special case: the present formula applies to arbitrary triangle-free factors, including cycles and graphs whose independence complexes have multiple nonzero homotopy dimensions. Thus the new claim is the universal graph-join splitting, not a re-count of that matching example.

The cycle independence-complex input is due to Kozlov and is recorded in Adamaszek, *Splittings of independence complexes and the powers of cycles* (arXiv:1106.6250, introduction). The cycle recurrence and its sphere counts are used as known background, not claimed as original.

## Limitations
The statement requires all factors to be nonempty and triangle-free, with at least two factors. It does not classify joins with factors containing internal triangles or more general forbidden clique sizes. The homotopy equivalence is not asserted to be equivariant under automorphisms permuting the factors, and no canonical integral homology basis is claimed. The literature comparison is limited to the identified primary texts and targeted searches; further equivalent formulations may exist under other terminology. Independent review has not been performed.

## References
1. R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1 (2026-02-10), https://arxiv.org/abs/2602.09623 .
2. M. Adamaszek, *Splittings of independence complexes and the powers of cycles*, arXiv:1106.6250 (2011), https://arxiv.org/abs/1106.6250 .
3. D. Kozlov, earlier independence-complex calculations for paths and cycles, as cited and summarized in Reference 2.
