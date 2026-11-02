# A sharp degree threshold for an unbounded VC–Littlestone gap in maximal-independent-set families

## Finding
For any finite simple graph \(G\), let \(\mathcal I(G)\) be its family of **inclusion-maximal independent vertex sets**, represented by vertex-membership indicators. A query names a vertex and receives its indicator in the unknown set. Let \(P_{10}\) be the path on ten vertices in their natural order, and let \(F_m\) be the disjoint union of \(m\) copies of \(P_{10}\), for any integer \(m\ge1\). Then
\[
\operatorname{VCdim}(\mathcal I(P_{10}))=3,\qquad
\operatorname{Ldim}(\mathcal I(P_{10}))=4,
\]
and, for every \(m\ge1\),
\[
\boxed{\operatorname{VCdim}(\mathcal I(F_m))=3m,\quad
\operatorname{Ldim}(\mathcal I(F_m))=4m.}
\]
Consequently, the difference is \(m\), unbounded among **linear forests** (disjoint unions of paths), which have maximum degree two. In sharp contrast, every graph with maximum degree at most one has equal VC and Littlestone dimensions for this concept class: both equal the number of its edges.

Furthermore, among paths, \(P_{10}\) is the smallest with a strict gap: for path orders \(1,\ldots,10\), the respective \((\operatorname{VCdim},\operatorname{Ldim})\) pairs are
\[
(0,0),(1,1),(1,1),(1,1),(2,2),(2,2),(2,2),(3,3),(3,3),(3,4).
\]
This last finite minimality assertion is certified by exhaustive computation, not by a general formula for all paths.

## Assumptions and scope
Graphs are finite, simple, and undirected. A vertex set is maximal independent if it is independent and dominates every vertex outside it. VC dimension is the maximum size of a fixed vertex set on which every Boolean pattern occurs as a restriction of some concept. Littlestone dimension is the greatest depth of a complete binary tree with vertex queries at internal nodes for which each root-to-leaf binary response path is realized by some concept. The empty tree has depth zero. No connectedness is asserted for \(F_m\), and no exact formula for all connected paths is asserted.

## Proof
**One path block.** In every maximal independent set of \(P_n\), either vertex 1 belongs to the set (so vertex 2 does not, and vertices 3 through \(n\) form a maximal independent set of their subpath), or vertex 1 does not belong to the set (forcing vertex 2 to belong, vertex 3 to be absent, and the remaining vertices to form a maximal independent set). Therefore the counts \(a_n=|\mathcal I(P_n)|\) obey \(a_n=a_{n-2}+a_{n-3}\) for \(n\ge3\), with \(a_0=a_1=1\) and \(a_2=2\). In particular, \(a_{10}=16\). This decomposition does not claim any analogous shattering-dimension recursion.

Enumerating precisely these sixteen concepts gives the vertex-membership frequencies, in vertex order 1 to 10,
\[
(9,7,5,8,6,6,8,5,7,9).
\]
These numbers can also be reproduced directly by the standalone checker. Suppose four vertices were VC-shattered. Every one of the sixteen Boolean patterns would then occur exactly once, since there are only sixteen concepts. Each queried vertex would consequently belong to exactly eight concepts. But only vertices 4 and 7 have frequency eight, so four such vertices do not exist. Hence the VC dimension is at most three. The three fixed queries at vertices \(\{1,4,7\}\) are shattered: `certificate.json` contains one explicit valid maximal independent set for each of the eight response patterns. Thus the VC dimension equals three.

For adaptive shattering, `certificate.json` contains a complete depth-four binary query tree, with fifteen internal nodes and sixteen leaves. Every leaf explicitly identifies a maximal independent set that realizes every answer on its root-to-leaf path. The checker independently reconstructs all maximal independent sets from the path edges and validates these witness paths, proving a depth-four lower bound. Conversely a complete depth-five tree would require at least \(2^5=32\) distinct concepts, whereas only sixteen exist. So the Littlestone dimension equals four.

**Disjoint-union amplification.** Every maximal independent set of a disjoint union of graphs is precisely a union of independently chosen maximal independent sets of its components. Thus \(\mathcal I(F_m)\) is the Cartesian product of \(m\) copies of \(\mathcal I(P_{10})\), and it contains \(16^m\) concepts. A fixed set of vertex queries is VC-shattered by this product if and only if its restriction to each component is shattered locally. It follows that its VC dimension is the sum of the component dimensions, namely \(3m\). For Littlestone dimension, concatenate the depth-four shattered trees of the components in order, using whichever tree node is reached in an earlier component before proceeding to the next. Independence of component choices realizes every concatenated response path, so the product shatters a complete tree of depth \(4m\). No tree can have depth greater than \(4m\), because \(16^m=2^{4m}\) concepts cannot realize more than \(2^{4m}\) distinct leaves. This proves both identities for all positive integers \(m\).

**Sharpness in maximum degree.** A finite graph with maximum degree at most one is a disjoint union of isolated vertices and \(k\) separate edges, for some \(k\ge0\). Every maximal independent set includes every isolate and exactly one endpoint of each edge. Thus exactly \(2^k\) concepts exist. Selecting one query vertex per edge shatters every static labeling of \(k\) queries and every adaptive response sequence of length \(k\); the number of concepts supplies the matching upper bounds. Hence both dimensions equal \(k\).

**The first path threshold.** The optional finite minimality assertion for path orders one through nine follows by complete enumeration of every candidate independent dominating set, of every candidate fixed query support, and of every residual state in the exact recursive Littlestone test. `verify.py` performs these calculations without relying on the displayed dimensions; its printed pairs are included under Verification.

## Verification
Run `python3 verify.py` with `certificate.json` in the same directory. Only the Python standard library is required. The program reconstructs the graph and all maximal independent sets; checks the exact set of sixteen certificates, the eight fixed-query witness patterns, the balanced-column upper bound and all sixteen root-to-leaf adaptive paths; directly computes both dimensions for every path order from one through ten using a separate memoized residual-set recursion; and checks the two-component product count.

The observed deterministic output is:
```
PATH10_CERTIFICATE_PASS concepts=16 balanced_positions=2 VC=3 Ldim=4 tree_leaves=16
FIRST_PATH_GAP_PASS [(0, 0), (1, 1), (1, 1), (1, 1), (2, 2), (2, 2), (2, 2), (3, 3), (3, 3), (3, 4)]
TWO_COMPONENT_PRODUCT_PASS maximal_independent_sets=256
ALL_NEW_FINITE_CHECKS_PASS
```
The unrestricted formula for all \(m\) is proved by the component argument above; no finite experiment is used as a substitute for that argument.

## Relationship to prior work
Chase and Freitag (first available 2018) give the general thicket/Littlestone framework and Sauer–Shelah type bounds. Guingona, Kolesnikov, Nierwinski, and Soucy (2021) prove equality of the two dimensions for zero sets of full nontrivial linear-combination families under hypotheses not satisfied by the present strictly separating example. Song and Yao (first available 2020) count maximal independent sets of prescribed cardinality in extremal graphs; their main theorem does not calculate shattering dimensions of the fixed path. Ghazi, Golowich, Kumar, and Manurangsi (2021) give general dimension bounds for Boolean aggregates, not this exact membership class and degree-two threshold. Krivelevich, Mészáros, Michaeli, and Shikhelman (first available 2019; later publication) study random greedy maximal independent sets, including on paths, rather than the VC/Littlestone dimensions of **all** maximal independent sets.

The present claim combines a verified smallest connected path witness with product amplification and the degree-one obstruction. A search of published research records and selected primary text identified no prior result implying this exact degree threshold. Lack of a matching record is not proof of historical priority; alternate terminology, especially **independent dominating sets**, remains a residual risk.

## Limitations
The unbounded-gap graphs are disconnected forests. The proof does not establish an unbounded gap on connected paths or trees and does not claim novelty of the generic dimension definitions, graph counting recurrence, or direct-product observation individually. The sixteen-concept census is a finite proof component, and the resulting infinite family follows through a separate general argument. The claim has received a self-review only; no independent audit has been performed.

## References
1. H. Chase and J. Freitag, *Model Theory and Combinatorics of Banned Sequences*, arXiv:1801.07640v1 (January 23, 2018), subsequently *Journal of Symbolic Logic* 87 (2022), 1–20. https://arxiv.org/abs/1801.07640
2. V. Guingona, A. Kolesnikov, J. Nierwinski, and R. Soucy, *Littlestone and VC-Dimension of Families of Zero Sets*, arXiv:2109.04805v1 (September 10, 2021). https://arxiv.org/abs/2109.04805
3. C. Song and B. Yao, *Maximizing the Number of Maximal Independent Sets of a Fixed Size*, arXiv:2012.06066v1 (December 11, 2020). https://arxiv.org/abs/2012.06066
4. B. Ghazi, N. Golowich, R. Kumar, and P. Manurangsi, *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions*, *Proceedings of Machine Learning Research* 132 (2021), 686–696. https://proceedings.mlr.press/v132/ghazi21a.html
5. M. Krivelevich, T. Mészáros, P. Michaeli, and C. Shikhelman, *Greedy Maximal Independent Sets via Local Limits*, arXiv:1907.07216v1 (July 16, 2019), later *Random Structures & Algorithms* 64 (2024), 986–1015. https://arxiv.org/abs/1907.07216
