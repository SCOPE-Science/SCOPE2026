# Well-f-covered rook graphs and their complete induced-forest enumeration

## Finding
Let \(2\le p\le q\) be integers, and let \(R_{p,q}=K_p\square K_q=L(K_{p,q})\) be the rectangular rook graph. An **induced-forest set** is a vertex subset inducing an acyclic graph; it is **inclusion-maximal** if adjoining any omitted vertex creates a cycle. Every inclusion-maximal induced-forest set has the same cardinality:
\[
 f(R_{p,q})=\min\{2p,p+q-1\}=\begin{cases}2p-1,&p=q,\\2p,&p<q.\end{cases}
\]
Thus every rectangular rook graph is well-f-covered. In particular, *every* inclusion-minimal feedback vertex set is a *minimum* feedback vertex set, of size \(pq-f(R_{p,q})\).

The complete induced-forest polynomial \(I_{p,q}(z)=\sum_{S\subseteq V(R_{p,q}),\,R_{p,q}[S]\text{ a forest}}z^{|S|}\) satisfies
\[
 I_{p,q}(z)=p!q!\,[x^p y^q]\exp\!\left(x+y+\frac{xyz+\frac12(x+y)xyz^2}{1-xyz^2}\right).
\]
If \(p=q\), the number of inclusion-maximal induced-forest sets is \((p!)^2\). If \(p<q\), those sets are counted by their number \(c\) of nonempty induced-path components:
\[
 M_{p,q,c}=\frac{p!q!}{2^c c!(q-p-c)!}\binom{p-1}{c-1},\qquad 1\le c\le\min\{p,q-p\},
\]
and \(M_{p,q,c}=0\) otherwise. In the balanced case every maximum forest has one component. For \(p<q\), every integer in \(\{1,\ldots,\min(p,q-p)\}\) occurs as \(c\).

## Assumptions and scope
All graphs are finite, undirected, and simple. A rook-graph vertex \((i,j)\) corresponds to edge \(i j\) of the complete bipartite graph whose ordered parts have sizes \(p,q\). Two rook-graph vertices are adjacent if their respective edges share a bipartite endpoint. All sets are labeled by the fixed row and column labels. Isolated bipartite vertices are retained for counting purposes; only selected bipartite edges become vertices in the induced rook graph. Coefficient extraction is formal, with \(z\) marking selected rook-graph vertices. The theorem assumes \(2\le p\le q\), including the balanced boundary.

## Proof
**1. Linear-forest equivalence.** Given \(S\subseteq V(R_{p,q})\), let \(F\subseteq E(K_{p,q})\) be the corresponding edge set. By construction \(R_{p,q}[S]=L((A\cup B,F))\). If the bipartite subgraph contains a vertex of degree at least three, its three incident edges produce a triangle in the line graph. If it contains a cycle, the corresponding edges produce a cycle in its line graph. Conversely, if all degrees are at most two and no cycle occurs, all nontrivial components are paths, whose line graphs are paths; hence the line graph is acyclic. Therefore \(S\) is an induced-forest set if and only if \(F\) is a bipartite linear forest (a disjoint union of paths and isolated vertices).

**2. Maximality.** Call a vertex of the bipartite graph *free* when its degree in \(F\) is zero or one. Two free vertices \(a\in A\) and \(b\in B\) in different components can be joined by the edge \(ab\) without creating a cycle or degree three, so \(F\) cannot be inclusion-maximal. Every component of a linear forest has a free vertex. If some \(a\in A\) is free, at least one \(b\in B\) is free: otherwise every \(b\) has degree two, implying \(|F|=2q\ge p+q\), impossible for a forest on \(p+q\) vertices. In an inclusion-maximal \(F\), all free vertices on opposite shores must belong to the same component. A different component would contain a free vertex on at least one shore and thereby contradict this requirement. Hence \(F\) has exactly one component and is a spanning path. An alternating spanning path with a free vertex of \(A\) has at least as many \(A\)-vertices as \(B\)-vertices; since \(p\le q\), this is possible only when \(p=q\), and then it has one endpoint on each shore. Thus if \(p<q\), inclusion-maximality forces all \(A\)-vertices to have degree two. If \(p=q\), this alternative is impossible because \(2p\) edges would exceed the \(2p-1\) forest bound, so exactly the spanning Hamiltonian paths occur.

Conversely, if every vertex of \(A\) has degree two, adding any missing bipartite edge would give an \(A\)-vertex degree three, hence a triangle in the induced line graph. Any alternating spanning path is also inclusion-maximal: adding any missing edge either creates degree three or a cycle. Therefore the listed families are exactly all inclusion-maximal induced forests. A spanning Hamiltonian path has \(p+q-1=2p-1\) edges when \(p=q\). In the unbalanced case each \(A\)-vertex has degree two, so every maximal set has \(2p\) edges; such a linear forest exists by selecting an alternating path on all \(p\) vertices of \(A\) and \(p+1\) vertices of \(B\), leaving other \(B\)-vertices isolated. Hence all maximal sets are maximum and the size formula follows. The feedback vertex statement follows by complementation.

**3. All-cardinality enumerator.** Treat the two bipartition classes as disjoint labeled sorts, marked by \(x,y\). Isolated vertices contribute \(x+y\) to the connected-component exponential generating function. A nontrivial alternating path with equal positive numbers \(r\) of vertices of both sorts has \(2r-1\) edges and \((r!)^2\) labeled realizations. Its two shores therefore contribute \((xy)^r z^{2r-1}\). A path with \(r+1\) vertices of one sort and \(r\ge1\) of the other has \(2r\) edges and \((r+1)!r!/2\) labeled realizations, accounting for reversal; its contribution is \(\frac12(x+y)(xy)^r z^{2r}\). Summing gives the connected nontrivial path series \(\big(xyz+\frac12(x+y)xyz^2\big)/(1-xyz^2)\). The labeled exponential formula, followed by coefficient extraction and multiplication by \(p!q!\), proves \(I_{p,q}(z)\).

**4. Counts of maximum sets.** For \(p=q\), a Hamiltonian alternating path is specified by separate orders of the \(p\) vertices on each shore. Choosing the first endpoint in \(A\) resolves reversal, so there are \((p!)^2\) sets. For \(p<q\), every nontrivial path component of a maximum forest has both endpoints on shore \(B\). If the component uses \(r\ge1\) vertices of \(A\), it uses \(r+1\) of \(B\), with \(r!(r+1)!/2\) undirected labeled realizations. Marking components with \(u\), the two-sort exponential generating function for maximum forests is
\[
 \exp\left(y+\frac{u y}{2}\frac{xy}{1-xy}\right).
\]
The coefficient of \(x^p y^q u^c\), multiplied by \(p!q!\), is exactly \(M_{p,q,c}\) above: distributing the \(p\) vertices of \(A\) into \(c\) positive path lengths contributes \(\binom{p-1}{c-1}\), while \(q-p-c\) vertices of \(B\) remain isolated. Every allowed \(c\) has a positive count, proving the component spectrum.

## Verification
The standalone script `verify.py` independently enumerates every subset of \(R_{p,q}\) on the ten boards listed in `verification_output.txt` and checks acyclicity using rook-graph adjacency, without relying on the path equivalence. It compares every coefficient against an independent two-sort component recurrence, checks that every inclusion-maximal forest has the proposed maximum size, and checks the component-count formula. It inspected exactly 104290 subsets; all assertions passed. For instance
\[
 I_{3,5}(z)=1+15z+105z^2+420z^3+960z^4+1170z^5+540z^6,
\]
where the \(540\) maximum sets comprise \(360\) connected cases and \(180\) with two components. The finite test does not replace the preceding general proof.

## Relationship to prior work
Jafarpour-Golzari (2021), arXiv:2105.14339, introduces *well-f-coveredness* and classifies several graph families. Its Theorem 6.15 and Corollary 6.16 establish that **the complete bipartite graph itself** is well-f-covered only under a balancing or singleton condition. Our theorem instead concerns **its line graph**, the rectangular rook graph, and holds for every pair of factor orders. The primary paper's definitions, graph operations, and complete-bipartite subsection were inspected; no line-graph/rook-graph result there implies this classification. The classical well-coveredness of rook graphs only constrains maximal independent sets (matchings in the bipartite graph), not maximal induced forests (linear forests). Generic feedback-vertex-set methods and generic labeled exponential formulas do not themselves supply the all-maximal size theorem or the specialized coefficient and component profiles. The claim is not that any of these general principles is new.

## Limitations
The theorem applies only to the line graphs of complete bipartite graphs, not to all line graphs, all Cartesian products, or the bipartite complete graphs themselves. The explicit formula counts labeled sets; it is not an isomorphism-class count. The finite checks end at a sixteen-vertex rook graph, and the infinite result follows from the proof. Bibliographic priority cannot be guaranteed against unindexed or inaccessible treatments of maximal linear forests in complete bipartite graphs. There has been no independent mathematical audit.

## References
1. R. Jafarpour-Golzari, *Graphs whose all maximal induced forests are of the same order*, arXiv:2105.14339v1 (first public 2021-05-29), https://arxiv.org/abs/2105.14339. In particular, Sections 3 and 6 and Corollary 6.16.
2. R. Jafarpour-Golzari, *On well-f-coveredness of lexicographic product of graphs*, arXiv:2108.09146v1 (2021-08-20), https://arxiv.org/abs/2108.09146. This treats lexicographic, not Cartesian, products.
3. S. Mertens, *Domination Polynomial of the Rook Graph*, Journal of Integer Sequences 27 (2024), https://cs.uwaterloo.ca/journals/JIS/VOL27/Mertens/mertens6.pdf. The invariant there is domination, not induced-forest maximality.
4. G. Gutin and A. Yeo, *Perfect Forests in Graphs and Their Extensions*, arXiv:2105.00254 (2021), https://arxiv.org/abs/2105.00254. Its perfect-forest condition differs from vertex-induced forests of rook graphs.
