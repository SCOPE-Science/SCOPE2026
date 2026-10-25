# A parity phase diagram and orientation character for perfect-matching complexes of multi-theta graphs

## Finding
For every integer \(r\ge 4\) and every sequence of integers \(\ell_1,\ldots,\ell_r\ge 2\), let \(\Theta(\ell_1,\ldots,\ell_r)\) be the simple graph obtained by joining two distinguished vertices \(u,v\) by \(r\) internally vertex-disjoint paths of lengths \(\ell_i\). Let \(q\) be the number of even lengths. Write \(\mathcal P(G)\) for the **perfect-matching complex** of a finite graph \(G\): its simplicial facets are its perfect matchings, viewed as subsets of the graph's edge set; if no perfect matching exists, its realization is void.

The complete homotopy classification is
\[
|\mathcal P(\Theta)|\simeq
\begin{cases}
S^{r-2},&q=0,\\
\mathrm{point},&q=2,\\
\varnothing,&q\notin\{0,2\}.
\end{cases}
\]
The contractible case is nonempty. Consequently, in the all-odd case, the only nonzero reduced integral homology group is \(\widetilde H_{r-2}(\mathcal P(\Theta);\mathbb Z)\cong\mathbb Z\). Every automorphism that permutes equal-length paths acts on this rank-one group by the sign of its permutation of the \(r\) paths. The simultaneous reversal of every path, exchanging \(u\) and \(v\), acts by \(+1\) on this group. These actions commute.

For all-odd paths the top homology dimension is \(r-2=\beta_1(\Theta)-1\), where \(\beta_1(\Theta)=r-1\) is the cycle rank of the underlying graph. The family supplies planar series-parallel examples with nonzero perfect-matching homology in arbitrarily high degrees.

## Assumptions and scope
All graphs are finite, simple, and undirected. Path lengths count edges. Distinct paths intersect only at \(u,v\). The lower bound \(\ell_i\ge2\) ensures there are no parallel direct edges, and the internal vertex set of every path is nonempty. The result concerns perfect-matching complexes, **not** ordinary matching complexes. A simplex in \(\mathcal P(G)\) is a set of edges extendible to a perfect matching of \(G\). The phrase “void” refers to an empty geometric realization, not to a nonempty contractible complex.

## Proof
Write the vertices along path \(i\) as \(u=w_{i,0},w_{i,1},\ldots,w_{i,\ell_i}=v\). For any perfect matching \(M\), let \(t_i\in\{0,1,2\}\) be the number of its two terminal vertices matched by edges of path \(i\). The \(\ell_i-1\) internal vertices must all be covered by edges of the same path, so parity forces
\[
t_i\equiv\ell_i-1\pmod2,\qquad\sum_{i=1}^r t_i=2.
\]
Thus each even-length path forces \(t_i=1\), while an odd-length path has \(t_i=0\) or \(2\). It follows immediately that there is no perfect matching unless \(q=0\) or \(q=2\). Conversely, both exceptional counts produce perfect matchings, as follows.

If \(q=0\), exactly one path has \(t_i=2\) and all the others have \(t_j=0\). Once the active path \(i\) is chosen, every edge of the perfect matching is forced: on each inactive path the internal vertices pair consecutively, while on the active path its two endpoint edges are chosen and the remaining internal vertices pair consecutively. Denote this unique matching by \(M_i\). The two alternating edge selections on a fixed odd-length path are disjoint. Therefore, for every nonempty index set \(J\subseteq\{1,\ldots,r\}\),
\[
\bigcap_{i\in J}M_i\ne\varnothing\quad\Longleftrightarrow\quad J\ne\{1,\ldots,r\}.
\]
Indeed, if \(J\) is proper, choose a path outside \(J\); all matchings indexed by \(J\) include the consecutive internal edges of this inactive path, and at least one such edge exists. For the full index set, each path appears both active and inactive, and the disjoint alternating choices leave no graph edge common to every \(M_i\).

The complex \(\mathcal P(\Theta)\) is the union of the \(r\) simplices \(\Delta(M_i)\). Every nonempty geometric intersection of these simplices is itself a simplex and hence contractible. Their nerve contains every proper subset of \(\{1,\ldots,r\}\), but not the full set: it is exactly \(\partial\Delta^{r-1}\). The simplicial nerve theorem therefore gives the integral homotopy equivalence \(|\mathcal P(\Theta)|\simeq S^{r-2}\).

If \(q=2\), let \(a,b\) be the two even-length paths. They must each engage exactly one terminal, so the unique possibilities are to match \(u\) through \(a\) and \(v\) through \(b\), or vice versa. Along every path the remaining matching edges are forced. Thus there are exactly two perfect matchings. Since \(r\ge4\), at least one odd-length path remains unused by both assignments; the internal matching of that path contains an edge common to the two perfect matchings. The perfect-matching complex is consequently the union of two simplices with a nonempty simplex intersection, so is contractible.

For the homology action in the all-odd case, path permutations carry the facet \(\Delta(M_i)\) to \(\Delta(M_{\sigma(i)})\). The nerve identification is natural on integral homology: its Čech complex has canonical degree-zero generators for every nonempty facet intersection, and is the augmented chain complex of the nerve. Hence the top homology is the orientation lattice of \(\partial\Delta^{r-1}\), on which \(\sigma\) acts by \(\operatorname{sgn}(\sigma)\). Simultaneously reversing all paths preserves each of the alternating matching edge sets \(M_i\), hence each facet and each canonical intersection generator; it therefore acts as the identity. This proves all assertions.

## Verification
The companion standalone Python file `verify_theta.py` independently constructs the graph from its path lengths, enumerates perfect matchings recursively, reconstructs the facet-intersection nerve, and computes mod-two reduced homology for small complexes by exact bitset Gaussian elimination. It verifies 1,424 parameter instances with path counts from two through six, including 182 exact mod-two homology calculations. It also checks 15 signed simplicial Lefschetz values for generating arm transpositions and terminal exchange in equal-length, all-odd examples. These finite checks corroborate the universal parity and orientation formulas; the infinite classification rests on the proof above, not on exhaustive enumeration.

## Relationship to prior work
Bayer, Jelić Milutinović and Vega introduced perfect-matching complexes and analyzed honeycomb families, including sphere and contractibility phenomena by the nerve theorem and discrete Morse theory [1]. Chandrakar and Singh investigated polygonal line tilings and rectangular ladders [2]. Agarwal and Basak treated perfect-matching complexes of Möbius and circular ladders in 2026 [3]. The present graphs have arbitrarily many internally disjoint paths between the same two terminals, with terminal degree at least four. They are not the honeycomb, polygonal-line, or regular ladder families treated in those results. The contribution here is a complete parity-dependent homotopy classification and integral orientation character for this distinct two-terminal series-parallel family. The classical even-cycle case is deliberately excluded by \(r\ge4\).

## Limitations
The classification requires internally disjoint paths of length at least two and at least four arms. It does not classify arbitrary series-parallel graphs, nor ordinary matching complexes. An equivalent result may exist under the terms *multi-theta*, *generalized theta* or *subdivided dipole*; the literature comparison is not a proof of global uniqueness. Some relevant recent full texts were inaccessible, and independent mathematical assessment has not been performed.

## References
[1] M. Bayer, M. Jelić Milutinović, J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, Electronic Journal of Combinatorics 30 (2023), #P2.45, DOI:10.37236/11525.

[2] H. Chandrakar, A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, Annals of Combinatorics 29 (2025), 1211–1233, DOI:10.1007/s00026-025-00755-0; earlier preprint arXiv:2407.05809.

[3] A. Agarwal, B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601, first publicly posted 2026-08-31.
