# First VC–Littlestone separation for minimal dominating sets of paths

## Finding
For a finite simple graph \(G\), let \(\mathcal D(G)\) be the concept class of membership indicators of **all inclusion-minimal dominating sets** of \(G\), with graph vertices as the query domain. A dominating set need not have minimum cardinality.

For paths \(P_n\) on \(n\) vertices, \(n\ge1\), the first strict disparity between static and adaptive shattering occurs at \(n=11\). Precisely, for every \(1\le n\le10\),
\[
\operatorname{VCdim}(\mathcal D(P_n))=\operatorname{Ldim}(\mathcal D(P_n)),
\]
while
\[
|\mathcal D(P_{11})|=36,\quad
\operatorname{VCdim}(\mathcal D(P_{11}))=4,\quad
\operatorname{Ldim}(\mathcal D(P_{11}))=5.
\]
Moreover, if \(F_s\) is the disjoint union of \(s\ge1\) copies of \(P_{11}\), then
\[
\boxed{\operatorname{VCdim}(\mathcal D(F_s))=4s,\qquad
\operatorname{Ldim}(\mathcal D(F_s))=5s.}
\]
Thus the VC–Littlestone gap is unbounded for membership concepts of inclusion-minimal dominating sets, even on forests of maximum degree two. These are graph-solution concepts, not the concept class of graph neighborhoods.

## Assumptions and scope
All graphs are finite, loopless and undirected. The path \(P_n\) has vertices \(\{1,\ldots,n\}\) with edges between consecutive indices. A set \(D\subseteq V(G)\) dominates if \(N[v]\cap D\ne\varnothing\) for every vertex \(v\). It is inclusion-minimal if no proper subset dominates. Each \(D\) determines \(h_D(v)=1\) precisely when \(v\in D\). The VC dimension is the maximum size of a vertex set on which all binary labelings occur. The Littlestone dimension is the largest depth of a complete adaptively queried binary tree whose root-to-leaf labels are each consistent with some \(h_D\). An empty shattered tree has depth zero.

## Proof
**Private-neighbor test.** A dominating set \(D\) is minimal if and only if each \(u\in D\) has a vertex \(v\) with \(N[v]\cap D=\{u\}\). Indeed removing \(u\) destroys domination exactly if such a \(v\) exists. Consequently the complete family \(\mathcal D(P_n)\) is given by all binary masks passing the two explicit finite tests: every closed neighborhood intersects the mask; and removing any set bit makes one neighborhood empty. The program `verify.py` implements these predicates, and independently reproduces the family as the inclusion-minimal transversals of the path's closed-neighborhood hypergraph.

**Sharp finite base.** On \(P_{11}\), the tests return 36 distinct concepts. The vertex set \(\{1,3,8,10\}\) is VC-shattered: `certificates.json` specifies one distinct minimal dominating set for each of its 16 labelings. To prove the upper bound, the checker examines all \(\binom{11}{5}=462\) five-vertex subsets and explicitly finds strictly fewer than 32 membership traces on each. As every larger shattered set would contain a shattered five-set, the VC dimension is exactly four.

For the adaptive lower bound, `certificates.json` also supplies a complete depth-five query tree: 31 internal vertex queries and 32 leaves, each with a minimal dominating set realizing every answer along its path. The verifier checks all 32 root-to-leaf traces and that the leaves are distinct. Conversely, a depth-six binary shattering tree needs at least 64 distinct concepts, while there are only 36. Thus the Littlestone dimension is exactly five. For each \(1\le n\le10\), the same exact recurrence and exhaustive VC trace test produce the following pairs of dimensions in increasing order of \(n\):
\[
(0,0),(1,1),(1,1),(2,2),(2,2),(2,2),(3,3),(3,3),(4,4),(4,4).
\]
This proves minimality of the eleven-vertex threshold without extrapolating from an incomplete census.

**Disjoint-union amplification.** A set dominates a disjoint union minimally exactly when its restrictions dominate each component minimally. Thus \(\mathcal D(F_s)\) is the Cartesian product of \(s\) copies of \(\mathcal D(P_{11})\), on disjoint query domains.

Both dimensions are additive on such products. VC additivity follows because a query subset in the union is shattered exactly when its intersection with each component is shattered. For Littlestone dimension, the lower bound is given by concatenating a shattered tree for the first factor with a shattered tree for the second at every leaf. For the upper bound, induct on the total number of hypotheses in the two factors. Every nontrivial root query belongs to one domain, say the first, and splits its hypothesis class into two strict nonempty subfamilies. By induction the two branches have dimensions at most their first-factor dimensions plus the second-factor dimension. Their minimum is at most one below the first-factor dimension, by the defining minimax recurrence for Littlestone dimension. Hence the product's dimension is at most the sum. The same argument covers queries in the second domain. Iteration gives the stated exact values for every \(s\ge1\).

## Verification
Run `python3 verify.py` from the directory containing the script. It uses only the Python standard library and rewrites `certificates.json`. It independently enumerates minimal dominating sets both by exhaustive masks and by recursive neighborhood-transversal search. It then computes exact adaptive split recurrences and static trace projections through eleven vertices, checks equality below the threshold, verifies all 462 five-set failures on the eleven-vertex path, and constructs/rechecks the complete depth-five tree. The expected terminal marker is `ALL_CHECKS_PASS`; `verification_output.txt` records the inspected execution. The certificate stores zero-based vertex indices and integer bit masks, whereas the mathematical display uses one-based indices. The file `certificates.json` contains all required finite witnesses; no external dataset or solver is needed.

## Relationship to prior work
Mofidi, *On dominating graph of graphs, median graphs and partial cubes, and graphs in which complement of every minimal dominating set is minimal dominating* (arXiv:2212.04570, initial public release December 8, 2022), studies structural properties of dominating-set reconfiguration graphs. Its componentwise factorization of minimal dominating sets agrees with the elementary factorization used here, but the inspected manuscript does not supply VC/Littlestone values for path minimal-dominator families.

Guingona, Kolesnikov, Nierwinski and Soucy, *Littlestone and VC-dimension of families of zero sets* (arXiv:2109.04805, first released September 10, 2021), proves equality of these dimensions in an unrelated linear zero-set system. That theorem neither implies equality nor contradiction for minimal dominating sets. Mary, *Enumeration of minimal transversals of hypergraphs of bounded VC-dimension* (arXiv:2407.00694, June 30, 2024), studies enumeration from VC properties of the **input** hypergraph; its abstract was checked, but no full-document noncoverage assertion is made. The finite minimal-dominator gap requires the separate calculation above. An analogous exact-cardinality matching construction on path forests uses edge-membership hypotheses; it gives no implication determining minimal dominating sets of \(P_{11}\).

## Limitations
The theorem concerns **inclusion-minimal** (not necessarily cardinality-minimum) dominating sets. The exact values for connected paths are established only up to eleven vertices; no general formula for larger connected paths is asserted. The unbounded family uses disjoint unions, and it does not establish a connected-forest gap of arbitrary magnitude. The finite base is computer-assisted but exhaustive, with inspectable source and a complete adaptive witness. The author-side checks are not an independent scientific audit. Publication priority outside the inspected literature and accessible research records is not certified.

## References
- A. Mofidi, *On dominating graph of graphs, median graphs and partial cubes, and graphs in which complement of every minimal dominating set is minimal dominating*, arXiv:2212.04570 (first posted 2022-12-08), https://arxiv.org/abs/2212.04570.
- V. Guingona, A. Kolesnikov, J. Nierwinski, R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805 (first posted 2021-09-10), https://arxiv.org/abs/2109.04805.
- A. Mary, *Enumeration of minimal transversals of hypergraphs of bounded VC-dimension*, arXiv:2407.00694 (first posted 2024-06-30), https://arxiv.org/abs/2407.00694.
