# Exact quantifier-rank profiles of finite rook graphs

## Finding

For all integers \(q\ge1\) and positive integers \(a,b,c,d\), write \(R_{a,b}=K_a\square K_b\) for the rook graph on the cells of an \(a\)-by-\(b\) rectangle: two distinct cells are adjacent precisely when they share a row or a column. The graphs are considered in the *unlabeled*, simple-graph first-order language consisting only of adjacency and equality; row and column relations are **not** named.

The sharp equivalence law is
\[
R_{a,b}\equiv_q R_{c,d}\quad\Longleftrightarrow\quad
\{\min(a,q),\min(b,q)\}_{\mathrm{multi}}
=\{\min(c,q),\min(d,q)\}_{\mathrm{multi}}.
\]
Here \(\equiv_q\) denotes agreement on **every** first-order sentence of quantifier rank at most \(q\); braces denote unordered multisets, retaining repeated entries. It follows that precisely \(q(q+1)/2\) distinct rank-\(q\) types are realized by the entire family. Each type has a least-order representative within this family, with its two factor sizes in \(\{1,\ldots,q\}\), and the largest of those least orders is exactly \(q^2\). For any two nonisomorphic rook graphs, the least distinguishing quantifier rank is precisely the first integer \(q\) at which the displayed multisets differ.

## Assumptions and scope

All graphs are finite, nonempty, undirected, loopless and simple; \(a,b\ge1\). The language has one symmetric adjacency predicate and equality; no coordinate predicates, constants, orders, or counting quantifiers are allowed. Quantifier rank measures nested quantifiers, including those in prenex sentences. The result is a classification **within the class of rook graphs**, not an assertion that its canonical representatives are smallest among arbitrary graphs of the same first-order type.

Write \(\operatorname{cut}_q(t)=\min(t,q)\). A rook graph has \(ab\) vertices. Its edges join cells agreeing in exactly one coordinate; its nonedges join cells agreeing in neither. Swapping the two factors gives an isomorphic graph.

## Proof

**Sufficiency, including the upper bound.** First swap the coordinate axes, if needed, so that \(\operatorname{cut}_q(a)=\operatorname{cut}_q(c)\) and \(\operatorname{cut}_q(b)=\operatorname{cut}_q(d)\). In the \(q\)-round Ehrenfeucht–Fraïssé game, Duplicator maintains an injective correspondence between the distinct first coordinates already selected in the two graphs and likewise between distinct second coordinates. On each Spoiler move, repeat the matched coordinate if it was previously chosen; for a previously unseen coordinate, choose a new unused coordinate in the corresponding other factor. This is always possible: by the time of any move at most \(q\) distinct values have been named in that coordinate, and factor sizes have the same truncation at \(q\). More precisely, if the source offers a previously unused value when \(t<q\) have been used, its factor size is greater than \(t\); equality of truncations implies that the other factor is also greater than \(t\). Thus the partial coordinate bijections can be prolonged through all \(q\) rounds. Equality of selected cells, and adjacency of distinct cells (agreement in at least one coordinate), are preserved. Duplicator wins, so the graphs agree up to quantifier rank \(q\).

**Necessity, recovering both coordinate sizes without coordinate predicates.** For \(q=1\), all nonempty loopless graphs satisfy the same sentences of rank at most one, and both cutoffs equal \(1\). Now let \(q\ge2\). The rank-two sentence \(\exists x\exists y\,(x\ne y\wedge\neg E(x,y))\) is true exactly when **both** rook factors have size at least \(2\). Thus the complete-graph cases are separated from the genuinely two-dimensional cases. If one factor equals \(1\), the rook graph is a complete graph on the other factor's number of vertices. For every \(2\le s\le q\), the rank-\(s\) formula asserting \(s\) mutually distinct vertices detects whether that size is at least \(s\), and hence determines its truncation at \(q\).

Suppose next that \(a,b\ge2\). For \(s\ge3\), a set of \(s\) pairwise adjacent cells must lie in a single row or a single column: once three cells form a clique, the first two share one coordinate, and every further cell adjacent to both must also share that coordinate (the only alternative would be the same cell twice). Therefore the rank-\(s\) sentence asserting \(s\) mutually distinct pairwise adjacent vertices holds exactly when \(\max(a,b)\ge s\). It detects the larger truncated factor through all \(3\le s\le q\).

For the smaller factor use the rank-\(s\) sentence, for every \(s\ge3\),
\[
\forall x\,\forall y\,\bigl(E(x,y)\to
\exists z_1\cdots\exists z_{s-2}\,
[\mathrm{Distinct}(x,y,z_1,\ldots,z_{s-2})\wedge
\bigwedge_{i=1}^{s-2}(E(x,z_i)\wedge E(y,z_i))]\bigr).
\]
Here \(\mathrm{Distinct}\) is the quantifier-free conjunction of pairwise inequalities. Two adjacent cells lying in a row of length \(b\) have exactly \(b-2\) common neighbors; cells lying in a column of length \(a\) have exactly \(a-2\). Since \(a,b\ge2\), both orientations of adjacent edges occur. Consequently this sentence holds exactly when \(\min(a,b)\ge s\). Together, the clique and common-neighbor tests recover the unordered pair \(\{\operatorname{cut}_q(a),\operatorname{cut}_q(b)\}_{\mathrm{multi}}\); for \(q=2\) the two-dimensional case yields just the pair \(\{2,2\}\). Distinct truncated pairs therefore have a distinguishing sentence of rank no more than \(q\), proving necessity.

**Exact class count and optimal representatives.** The unordered truncated pair ranges over all multisets of size two in \(\{1,\ldots,q\}\). Every such pair is represented by the rectangle with those two factor sizes, and necessity shows that none of these types merge. The number is \(\binom{q+1}{2}=q(q+1)/2\). For a fixed truncated pair \(\{u,v\}\), each realizing rook graph has each corresponding factor at least the indicated cutoff, so it has at least \(uv\) vertices; \(R_{u,v}\) attains that minimum. Maximizing \(uv\) gives \(q^2\), attained by the type \(\{q,q\}\). Finally the equivalence law implies the asserted exact minimum distinguishing rank simply by taking the first cutoff at which two distinct factor multisets separate. These arguments also cover \(q=1\).

## Verification

The proof above is symbolic and covers **all positive factor sizes and all ranks**. The independent finite checker `check_rook_ef.py` explicitly evaluates the recursive Spoiler/Duplicator game on all 21 unordered pairs among rook graphs with \(1\le a\le b\le3\) for ranks one and two, and all 55 pairs with \(1\le a\le b\le4\) for rank three. It separately checks three representative rank-four comparisons, including the crucial stable pair \(R_{4,4}\equiv_4 R_{5,5}\). The full command is `python3 check_rook_ef.py`; exact observed stdout is included in `checker_output.txt`. The finite tests corroborate the theorem and **do not** substitute for the unbounded EF-game proof.

## Relationship to prior work

The classical graph-definability and finite-graph EF-game literature (Pikhurko, Veith and Verbitsky; Pikhurko and Verbitsky) studies rank/quantifier-depth bounds for graph distinction and isomorphism. Klavžar and Peterin treat Cartesian products of complete graphs as Hamming graphs, studying their subgraph characterizations and the triangle coordinate property. Those results give mathematical background but do not themselves state the rank-by-rank quotient count or the exact cutoff equivalence criterion above. Targeted searches for rook graph, lattice graph, line graph of a complete bipartite graph, first-order rank, and Ehrenfeucht–Fraïssé equivalence found no stronger directly covering published theorem. The literature check is substantial but not exhaustive; an elementary equivalent statement could be recorded elsewhere.

## Limitations

This is a full classification within the two-factor rook-graph family, not a classification of arbitrary Hamming graphs with more factors, arbitrary first-order interpretations, or smallest models outside the rook family. It concerns ordinary quantifier rank without counting quantifiers or coordinate labels. Small exhaustive games provide finite corroboration only. Priority remains subject to unindexed/folklore equivalences and external expert audit.

## References

1. O. Pikhurko, H. Veith and O. Verbitsky, *The First Order Definability of Graphs: Upper Bounds for Quantifier Rank*, arXiv:math/0311041, first posted 2003-11-04, https://arxiv.org/abs/math/0311041 (full primary text inspected).
2. S. Klavžar and I. Peterin, *Characterizing Subgraphs of Hamming Graphs*, *Journal of Graph Theory* 49 (2005), 302–312, https://doi.org/10.1002/jgt.20084; author open-access full text https://users.fmf.uni-lj.si/klavzar/preprints/20084-scan.pdf (online 2005-04-08, relevant statements and proof inspected).
3. O. Pikhurko and O. Verbitsky, *Logical Complexity of Graphs: a Survey*, arXiv:1003.4865, 2010-03-25, https://arxiv.org/abs/1003.4865 (relevant definability and game sections inspected).
