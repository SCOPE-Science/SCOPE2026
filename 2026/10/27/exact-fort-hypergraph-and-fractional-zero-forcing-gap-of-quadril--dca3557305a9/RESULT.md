# Exact fort hypergraph and fractional zero-forcing gap of quadrilateral book graphs

## Finding

For every integer \(r\ge2\), let \(B_r=K_{1,r}\mathbin{\square}K_2\), the quadrilateral book consisting of \(r\) four-cycle pages sharing a single edge. Every inclusion-minimal fort of \(B_r\) belongs to exactly one of three explicit families described below. There are precisely
\[
\boxed{2^r+\binom r2}
\]
such forts. Moreover, the minimum zero-forcing number, the number of distinct minimum zero-forcing sets (labeled vertices), and the fractional zero-forcing number are, respectively,
\[
\boxed{Z(B_r)=r,\qquad \#\{X\subseteq V(B_r):|X|=r,\ X\text{ is zero forcing}\}=r\bigl((r+3)2^{r-2}-2\bigr),\qquad Z^*(B_r)=\max\{2,r/2\}.}
\]
Consequently, the ratio \(Z(B_r)/Z^*(B_r)=2\) for every \(r\ge4\). In particular, the factor two between the integral fort transversal number and its fractional relaxation is attained by an infinite family of connected, planar, bipartite, two-vertex-connected graphs.

## Assumptions and scope

All graphs are finite, simple, undirected; vertices are distinguished for counts. Put \(V(B_r)=\{u,v\}\cup\{a_i,b_i:1\le i\le r\}\), with edges \(uv\), \(ua_i\), \(a_ib_i\), and \(b_iv\) for each \(i\). A **fort** is a nonempty vertex set \(F\) such that every vertex outside \(F\) has either zero or at least two neighbors in \(F\). A fort is **inclusion-minimal** if it contains no smaller nonempty fort. A **zero-forcing set** colors all vertices by repeatedly coloring the unique white neighbor of a blue vertex; \(Z(G)\) is its minimum cardinality. Equivalently, a zero-forcing set meets every fort. The fractional fort transversal number \(Z^*(G)\) is the minimum of \(\sum_{x\in V(G)}w_x\) over real \(0\le w_x\le1\) satisfying \(\sum_{x\in F}w_x\ge1\) for every inclusion-minimal fort \(F\).

The complete list of inclusion-minimal forts is:

1. Two full pages \(\{a_i,b_i,a_j,b_j\}\) for distinct \(i,j\).
2. The two hub-opposite families \(\{u,b_1,\ldots,b_r\}\) and \(\{v,a_1,\ldots,a_r\}\).
3. The mixed hub transversals \(\{u,v,c_1,\ldots,c_r\}\), choosing exactly one \(c_i\in\{a_i,b_i\}\) on each page, with at least one \(a_i\) choice and at least one \(b_i\) choice.

The minimum zero-forcing sets are exactly the following, and their two classes are disjoint:

* No spine vertex is selected; one page is entirely selected, another page is omitted, and one arbitrary internal vertex is selected on each remaining page.
* Exactly one of \(u,v\) is selected; one page is omitted and one internal vertex is selected on each remaining page, with at least one \(a_i\) selected when the hub is \(u\), or at least one \(b_i\) selected when the hub is \(v\).

## Proof

**Fort classification.** Inspect membership of \(u\) and \(v\). If neither belongs to a fort, the two internal vertices of any page must be either both included or both excluded: a lone selected internal vertex would leave its partner outside with exactly one selected neighbor. Also each hub outside sees the number of full selected pages, so there must be at least two; inclusion-minimality leaves exactly two full pages.

If \(u\) belongs to the fort but \(v\) does not, then \(b_i\) must belong to the fort for every \(i\). Indeed, if \(b_i\) is outside and \(a_i\) is inside then \(b_i\) sees exactly one selected neighbor; if both are outside then \(a_i\) sees only \(u\). The set \(\{u,b_1,\ldots,b_r\}\) is itself a fort, since each outside \(a_i\) sees both \(u\) and \(b_i\), and \(v\) sees \(u\) and all \(b_i\). Every such fort therefore contains this one, so inclusion-minimality forces equality. The case with \(v\) selected and \(u\) absent is symmetric.

Finally, if both hubs belong to a fort, each page has at least one selected internal vertex; otherwise an excluded internal vertex has just its selected adjacent hub. If both internal vertices on a page are selected, removing one of them preserves the fort property and cannot yield an inclusion-minimal fort. Thus an inclusion-minimal fort has exactly one chosen vertex per page. The all-\(b\) choice contains \(\{u,b_1,\ldots,b_r\}\), and the all-\(a\) choice contains the symmetric fort, so neither is minimal. Every mixed choice is minimal: a proper fort subset containing both hubs would still need every selected page vertex, one containing just one hub would need an all-\(a\) or all-\(b\) page choice, and one containing no hubs would need two full pages. This proves all three types, disjointness, and the count \(\binom r2+2+(2^r-2)=\binom r2+2^r\).

**Integral zero forcing and all optimizers.** A set intersects every two-full-page fort only if it leaves at most one completely empty page. If its size is less than \(r\), it cannot have both hubs selected and it cannot occupy \(r-1\) pages while meeting the appropriate opposite-hub fort. With no hub selected, at most \(r-1\) vertices leave at least one empty page; if exactly \(r-1\) pages are represented, each is a singleton. Either all selected vertices lie on the same side and one hub-opposite fort is missed, or there are both types and the mixed transversal choosing the opposite internal vertex on every page is disjoint from the selection. Thus every forcing set has size at least \(r\).

Now suppose a fort transversal has size exactly \(r\). With both hubs selected, at least two pages are empty, violating a two-page fort. With exactly one hub, the remaining \(r-1\) selections must occupy \(r-1\) distinct pages, leaving one empty. For hub \(u\), the opposite-hub fort \(\{v,a_1,\ldots,a_r\}\) is hit if and only if at least one selected internal vertex is an \(a_i\); the other minimal forts are then hit automatically. Similarly, with hub \(v\), at least one \(b_i\) must be selected. With no hub selected, the selected vertices must occupy at least \(r-1\) pages. Occupying all \(r\) pages with one vertex each does not suffice: a uniform choice misses a hub-opposite fort and a mixed choice misses the complementary mixed-transversal fort. Hence exactly \(r-1\) pages are occupied, with one full page, one empty page and singletons elsewhere; these sets intersect each listed fort. This proves the optimizer classification and \(Z(B_r)=r\) by the fort-hitting characterization. The first class has \(r(r-1)2^{r-2}\) choices. The second has \(2r(2^{r-1}-1)\) choices. Their sum simplifies to \(r((r+3)2^{r-2}-2)\).

**Fractional optimum.** Summing the two hub-opposite fort inequalities gives \(\sum_x w_x\ge2\), since those two forts partition the vertex set. Summing the inequalities for all \(\binom r2\) two-full-page forts yields \((r-1)\sum_i(w_{a_i}+w_{b_i})\ge\binom r2\), hence \(\sum_xw_x\ge r/2\). For the matching upper bound, assign \(w_{a_i}=w_{b_i}=1/4\) on every page and \(w_u=w_v=\max\{0,1-r/4\}\). Every two-full-page fort has weight one; every hub-opposite fort has weight at least one; and each mixed hub-transversal fort has weight at least one. All weights lie in \([0,1]\). The total weight is \(r/2+2\max\{0,1-r/4\}=\max\{2,r/2\}\), completing the proof.

The graphs are connected and bipartite by construction, planar by embedding the pages alongside the shared edge, and two-vertex-connected because removing either hub leaves a connected star-like graph through the other hub, while deleting any page vertex leaves every other vertex connected through the spine.

## Verification

The standalone Python 3 standard-library program `artifacts/verify_book.py` independently tests the original fort definition against the complete claimed minimal-fort family for every \(2\le r\le7\). It tests the original synchronous zero-forcing rule against every candidate of cardinality at most \(r\), and exactly checks rational fractional feasible assignments for \(2\le r\le30\). Reproduce with `python3 artifacts/verify_book.py`; the expected output is embedded as `artifacts/verification_output.txt`. The finite tests confirm examples and detect implementation errors; the proof above, not enumeration, establishes the infinite assertions.

## Relationship to prior work

Cameron, Hogben, Kenter, Mojallal and Schuerger (arXiv:2310.17904, first posted 27 October 2023) develop the fort-hitting and fractional zero-forcing framework and examine various Cartesian products. Becker, Cameron, Hanely, Ong and Previte (arXiv:2404.05963, first posted 9 April 2024) enumerate minimal forts on several other graph families. Cameron and Pulaj (arXiv:2508.07293, 2025) provide integer-programming formulations. These works motivate the precise obstruction-hypergraph and fractional/integer comparison; their inspected discussions do not give the above complete quadrilateral-book classification, minimum-set enumeration, and fractional exactness jointly. Generic equivalence of zero forcing to fort transversals is used, not claimed as new. The precise scalar equality \(Z(B_r)=r\) is presented as part of the complete classification, not independently as a priority claim. A bibliographic search cannot exclude unindexed equivalents.

## Limitations

The enumeration is for labeled vertices and quadrilateral book graphs with \(r\ge2\), not triangular book graphs and not arbitrary Cartesian products. There is no claimed algorithmic improvement for arbitrary graphs, no isomorphism-class enumeration, and no independent mathematical audit. Relevant unindexed or inaccessible literature could contain equivalent statements.

## References

1. J. Cameron, L. Hogben, F. Kenter, H. Mojallal, B. Schuerger, *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904, version 1 publicly posted 27 October 2023, https://arxiv.org/abs/2310.17904.
2. S. Becker, J. Cameron, J. Hanely, O. Ong, B. Previte, *On the number of minimal forts of a graph*, arXiv:2404.05963, version 1 publicly posted 9 April 2024, https://arxiv.org/abs/2404.05963.
3. J. Cameron, A. Pulaj, *IP Models for Minimum Zero Forcing Sets, Forts, and Related Graph Parameters*, arXiv:2508.07293, https://arxiv.org/abs/2508.07293.
