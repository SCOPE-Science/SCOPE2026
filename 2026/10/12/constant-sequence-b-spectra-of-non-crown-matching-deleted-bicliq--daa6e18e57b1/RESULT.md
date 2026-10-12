# Constant-sequence b-spectra of non-crown matching-deleted bicliques
## Finding
Let \(G_{m,n,t}=K_{m,n}-M_t\), where \(2\le m\le n\), \(1\le t\le m\), and \(M_t\) is a matching of size \(t\). Exclude the balanced full-matching crown, so \((m,n,t)\ne(m,m,m)\). For each integer \(q\ge2\), write \(S_q=(q^\infty)\) for the infinite constant sequence.

Then \(G_{m,n,t}\) realizes \(S_q\) exactly when \(2\le q\le m\). Whenever it is realized,
\[
\operatorname{Spec}_{S_q}(G_{m,n,t})=\{2\},
\]
and consequently
\[
\chi_{S_q}(G_{m,n,t})=\phi_{S_q}(G_{m,n,t})=2.
\]
For \(q>m\), \(S_q\) is not realized.

Thus a nonempty matching deletion short of the balanced full-matching endpoint never creates a realization of a constant requirement \(q\ge2\) with three or more colors.
## Assumptions and scope
All graphs are finite and simple. Let the bipartition be \(A=\{a_1,\ldots,a_m\}\) and \(B=\{b_1,\ldots,b_n\}\), and take the deleted matching to be \(M_t=\{a_i b_i:1\le i\le t\}\). The excluded balanced full-matching endpoint is the only endpoint in this family where the proof's mixed-color-class obstruction can fail globally. The theorem deliberately concerns the genuinely matching-deleted, non-crown regime \(1\le t\le m\); it does not restate the undeleted complete-bipartite boundary.

A color-dominating vertex is a vertex whose closed neighborhood contains every color used. A coloring realizes \(S_q=(q^\infty)\) with \(k\) colors when every one of the \(k\) color classes contains at least \(q\) color-dominating vertices. The \(S_q\)-spectrum is the set of all such \(k\).
## Proof
First suppose \(2\le q\le m\). The bipartition coloring with color classes \(A\) and \(B\) is proper. Every vertex has a neighbor in the opposite shore: deleting a matching removes at most one opposite-shore neighbor from each vertex, while both shores have size at least two, and the excluded disconnected case lies at the omitted balanced full-matching endpoint. Hence every vertex sees both colors in its closed neighborhood and is color-dominating. The two color classes therefore contain \(m\) and \(n\) color-dominating vertices, so this coloring realizes \(S_q\). Thus \(2\) belongs to the \(S_q\)-spectrum.

It remains to rule out \(k\ge3\). In any proper coloring of \(G_{m,n,t}\), a color class meeting both shores must be exactly one deleted matched pair \(\{a_i,b_i\}\). Indeed, a cross-shore same-color pair must be nonadjacent, hence must be one of the deleted pairs, and no third vertex can join that class because it is adjacent to one endpoint.

If \(q\ge3\), such a mixed color class is impossible in a realizing coloring because it has only two vertices and therefore cannot contain \(q\) color-dominating vertices. Hence every color class is contained in one shore. With at least three colors, one shore contains at least two distinct color classes. A vertex in either of those classes has no neighbors in its own shore, so its closed neighborhood cannot contain the other same-shore color. Thus those classes have no color-dominating vertices, a contradiction.

Now let \(q=2\). Suppose some color class is mixed. It must be a deleted pair \(\{a_i,b_i\}\), and because the class needs two color-dominating vertices, both \(a_i\) and \(b_i\) are color-dominating. For every other color \(c\), vertex \(a_i\) can see \(c\) only on \(B\setminus\{b_i\}\), while \(b_i\) can see \(c\) only on \(A\setminus\{a_i\}\). Therefore every other color occurs on both shores. Every color class is consequently another deleted matched pair. Since the color classes cover all vertices, this forces \(m=n=t\), contrary to the hypothesis. Thus no mixed color class exists. As in the previous paragraph, three or more pure classes force two classes onto one shore and hence leave those classes without color-dominating vertices. Therefore \(k\le2\).

We have proved that when \(2\le q\le m\), the only possible realized color count is \(2\), and the bipartition coloring realizes it.

Finally let \(q>m\). Any realizing coloring with three or more colors is impossible by the preceding pure/mixed argument because now \(q\ge3\). A proper two-coloring of this connected bipartite graph is its bipartition coloring up to exchanging the colors, and its smaller color class has only \(m<q\) vertices. It cannot contain \(q\) color-dominating vertices. Hence \(S_q\) is not realized.
## Verification
The proof above is analytic for every admissible \(m,n,t,q\). The standalone checker `artifacts/verify.py` is only a finite stress test. It independently constructs every non-crown graph in the stated family with \(2\le m\le n\), total order at most \(9\), and \(m\le4\). For each such graph and every \(q\) from \(2\) through \(m+1\), it exhaustively enumerates proper colorings up to permutation of color names by restricted-growth strings, computes color-dominating vertices directly from closed neighborhoods, and compares the largest realized color count with the theorem.

Observed replay output:

`ALL CHECKS PASSED; profiles=66; canonical_colorings_checked=24043; max_order=9`

Finite enumeration is not used to infer the universal theorem.
## Relationship to prior work
Jakovac and Lang introduced sequence \(b\)-colorings and the \(S\)-spectrum, including the constant-sequence notation \(q^\infty\). Their general theory gives degree-based upper bounds and observes that every connected bipartite graph has a two-coloring in which every vertex is color-dominating. Their paper does not classify constant-sequence spectra of matching-deleted bicliques: full-text searches found no occurrence of “crown” or “complete bipartite,” and the sole “bipartite” discussion concerns the different sequence \((2,1^\infty)\). Their conclusion explicitly leaves exact \(S\)-spectra for particular graph classes largely open.

Targeted searches under “sequence b-coloring,” “matching-deleted biclique,” “complete bipartite,” “crown,” and “two color-dominating vertices” found no published theorem implying the stated non-crown classification. The closest indexed crown result concerns proper conflict-free coloring, a different coloring predicate, while the closest indexed \(b\)-chromatic result concerns the classical one-CDV-per-color parameter rather than the constant requirement \(q\ge2\).
## Limitations
The theorem excludes both the undeleted case \(t=0\) and the balanced full-matching crown \(m=n=t\); these boundary families are not part of the claimed new statement. It treats constant sequences \(S_q=(q^\infty)\) with \(q\ge2\), not arbitrary non-increasing sequences. No claim is made for deleting a nonmatching edge set, for disconnected graphs, or for other generalized \(b\)-coloring notions.
## References
1. M. Jakovac and M. S. Lang, “Sequence b-colorings in graphs,” arXiv:2609.08484v1, submitted 2026-09-08, AMS 2020 classification 05C15.
2. D. Vijayalakshmi and G. Mohanappriya, “b-Chromatic Number of Corona Product of Crown Graph and Complete Bipartite Graph with Path Graph,” Kongunadu Research Journal 2(2) (2015), 30–33, DOI 10.26524/krj311. This older paper concerns classical \(b\)-coloring of corona products and does not state the sequence-coloring classification above.
