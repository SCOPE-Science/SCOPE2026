# A flag-complex realization theorem for maximal-independent-set shattering on whiskered graphs

## Finding
Let \(G=(V,E)\) be any finite simple graph, possibly empty, and let \(t\ge1\) be an integer. Construct \(W_t(G)\) by attaching \(t\) distinct degree-one vertices to every \(v\in V\). Let \(\mathcal M_t(G)\) be the Boolean vertex-membership concept family consisting of all inclusion-maximal independent vertex sets of \(W_t(G)\). A query at vertex \(x\) returns whether \(x\) belongs to the chosen set. Define \(\mathscr S_t(G)\) to be the simplicial complex of shattered sets of queried vertices.

**Theorem.** A support \(S\subseteq V(W_t(G))\) is shattered exactly when it contains at most one vertex from each module \(B_v=\{v\}\cup\{v^{(1)},\ldots,v^{(t)}\}\), and the set of module indices \(\pi(S)=\{v:S\cap B_v\ne\varnothing\}\) is independent in \(G\). Equivalently, \(\mathscr S_t(G)\) is isomorphic to \(\operatorname{Ind}(G[K_{t+1}])\), the independence complex of the clique blow-up of \(G\) (this blow-up is the *support conflict graph*, not \(W_t(G)\)). If \(I_G(u)=\sum_{j\ge0}i_j(G)u^j\) is the ordinary independence polynomial, then the complete shattered-support polynomial is
\[
\Phi_t(G;z)=\sum_{S\in\mathscr S_t(G)}z^{|S|}=I_G((t+1)z)=\sum_{j\ge0}(t+1)^ji_j(G)z^j.
\]
Moreover,
\[
\operatorname{VCdim}(\mathcal M_t(G))=\operatorname{Ldim}(\mathcal M_t(G))=\alpha(G).
\]
Here \(\alpha(G)\) is the largest cardinality of an independent set of \(G\), with \(\alpha(\varnothing)=0\), and the Littlestone dimension is defined using binary adaptive vertex-membership queries.

For \(t=1\), the graph \(W_1(G)\) is well-covered: every maximal independent set has \(|V|\) vertices; it is also pure vertex-decomposable by the established whiskering theorem [2]. Nonetheless every finite flag simplicial complex occurs as the induced subcomplex of \(\mathscr S_1(G)\) on its core vertices, by choosing the complement of its one-skeleton as \(G\). In particular, for \(G=K_{1,m}\), \(m\ge2\), the facets of \(\mathscr S_1(G)\) have cardinalities exactly \(1\) and \(m\), and
\[
\Phi_1(K_{1,m};z)=(1+2z)^m+2z.
\]
Thus a pure vertex-decomposable, well-covered graph can have a nonpure maximal-independent-set shattering complex with an arbitrarily large facet-cardinality gap \(m-1\).

## Assumptions and scope
All graphs are finite, simple, undirected and labeled. Leaves attached to distinct core vertices are distinct. The maximality of a concept is inclusion-maximality, not maximum cardinality. A support is shattered if **all** binary assignments on its vertices occur as traces of concepts; the empty support is shattered. The clique blow-up \(G[K_{t+1}]\) replaces each vertex by a complete \((t+1)\)-vertex module and joins all pairs between modules whenever their core vertices are adjacent. The distinction between \(W_t(G)\) and its support conflict graph is essential. \(\operatorname{Ldim}\) is the greatest depth of a complete binary tree of vertex queries with every root-to-leaf labeling realized; repeated or redundant queries cannot increase depth.

## Proof
**Maximal independent sets.** Each leaf \(v^{(j)}\) has only \(v\) as neighbor. If \(v\) belongs to a maximal independent set \(M\), then none of its leaves belongs to \(M\). If \(v\notin M\), every one of its \(t\) leaves belongs to \(M\), because otherwise the omitted leaf could be added. The core set \(A=M\cap V\) must therefore be independent in \(G\). Conversely, for any independent \(A\subseteq V\),
\[
M(A)=A\cup\bigcup_{v\in V\setminus A}\{v^{(1)},\ldots,v^{(t)}\}
\]
is independent in \(W_t(G)\) and maximal: every omitted core vertex is adjacent to one of its selected leaves and every omitted leaf is adjacent to its selected core vertex. Thus \(A\mapsto M(A)\) is a bijection from \(\operatorname{Ind}(G)\) to \(\mathcal M_t(G)\).

**Necessary support conditions.** Within any module \(B_v\), all leaves have identical membership labels and the core vertex has the complementary label. No two distinct vertices from the same module can therefore be shattered: the pattern demanding both the core and a leaf is impossible, while for two leaves the mixed pattern is impossible. Thus a shattered support has at most one vertex from each module. If two distinct indices \(u,v\in\pi(S)\) are adjacent in \(G\), prescribe labels demanding that both cores \(u\) and \(v\) belong to the chosen maximal independent set. At a core query demand label \(1\); at a leaf query demand label \(0\). No independent core set can realize both demands. Hence \(\pi(S)\) must be independent.

**Sufficiency and enumeration.** Suppose the two conditions hold. For any binary labeling \(\eta:S\to\{0,1\}\), define \(A\) to consist precisely of those indices in \(\pi(S)\) whose requested label demands selection of the core. As a subset of the independent set \(\pi(S)\), \(A\) is independent. The maximal independent set \(M(A)\) realizes \(\eta\). So \(S\) is shattered. For each independent \(j\)-subset of the core there are exactly \((t+1)^j\) corresponding shattered supports, one choice of a vertex per module. This proves the complex isomorphism, polynomial and VC dimension (including the empty graph).

**Adaptive dimension.** The restriction to core queries realizes all \(2^{\alpha(G)}\) assignments on a fixed maximum independent core set; a complete oblivious tree of depth \(\alpha(G)\) follows, giving the lower bound. Every query of the full concept class asks for the core membership of its module or its negation. In a complete binary query tree of depth \(d\), follow, at each split, the branch demanding that the corresponding core vertex is selected. A module cannot be asked twice along this path, since one of the two children of a repeated query would be inconsistent. The resulting \(d\) distinct selected core vertices must form an independent set in \(G\). Consequently \(d\le\alpha(G)\), proving the upper bound.

**Flag complexes, nonpurity, and complexity.** A finite flag complex on vertex set \(V\) is the independence complex of the graph joining precisely the pairs that are not its edges. Restrict the shattered-support complex of \(W_1(G)\) to the core queries to recover that complex. A facet of \(\mathscr S_t(G)\) projects precisely to a maximal independent set of \(G\), since any independent projection extension supplies a larger shattered support. For the star \(K_{1,m}\), the maximal independent core sets are the singleton center and the collection of all \(m\) leaves, giving the claimed facet sizes and polynomial. Each maximal independent set of \(W_1(G)\) contains one vertex from each core–leaf pair, so the graph is well-covered; its pure vertex-decomposability is the previously established full-whiskering fact [2], not a new claim. Finally, the equality of VC dimension and \(\alpha(G)\) gives a polynomial-time reduction from Independent Set to computing the VC dimension of these promised, explicitly represented fully whiskered graphs. Thus the threshold problem is NP-complete when input is given as \((G,k)\), equivalently as \((W_1(G),\text{marked core–leaf modules},k)\): membership in NP is witnessed by an independent core set of size \(k\).

## Verification
The standalone Python 3 script `check_whiskered_shattering.py` independently enumerates all maximal independent sets and all support traces, and compares direct shattering with the structural criterion and the polynomial coefficients. It exhausts every base graph on up to five labeled vertices for one pendant leaf per vertex, every base graph on up to four vertices for two leaves, and every base graph on up to three vertices for three leaves. Run with `python3 check_whiskered_shattering.py`. Expected final line:

`WHISKERED_MIS_SHATTERING_PASS 1188 49190`

The figures count base-graph/leaf-multiplicity test cases and total shattered-support instances across them. The unrestricted theorem is established by the preceding arguments; the finite computations are independent checks, not proofs of the universal quantifiers.

## Relationship to prior work
Independence complexes, their topology, and higher-independence variants are established objects [1]. The full-whiskering construction is known to yield a pure vertex-decomposable graph [2]; that structural property is used as a **prior theorem**. Neither inspected source asserts the maximal-independent-set *shattering* correspondence, its all-degree polynomial, the exact adaptive dimension, or the nonpurity of the shattering complex despite purity of the original graph's independence complex. The same formula is not the independence polynomial of \(W_t(G)\) itself; it is the polynomial of its shattered **query supports**. Prior structural criteria on forests and cographs, as well as calculations on paths and cycles, cover some special cases of maximal-independent-set shattering. Those restricted graph classes do not imply the unrestricted all-core transfer or the universal induced flag-complex realization. In particular, the whiskered-star nonpurity example is an illustration of the general theorem, not asserted as an independently new special case. The familiar identity expressing any finite flag complex as an independence complex is acknowledged, not claimed as new.

## Limitations
The main equivalence uses the pendant leaves and need not hold for arbitrary graph modifications or arbitrary maximal-independent-set concept classes. The restricted-input complexity consequence does not imply an NP-membership theorem for the VC dimension problem on completely unrestricted graphs without a whiskering promise. The topological assertion is an **induced-subcomplex** realization, not an assertion that the entire shattering complex equals the original flag complex. No general claim is made about higher \(r\)-independence complexes for \(r\ge2\). The mathematical correspondence is elementary enough that undocumented prior appearance under different terminology remains a genuine historical-priority risk. Independent validation has not been performed.

## References
1. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, first public 2021-06-21. https://arxiv.org/abs/2106.10863.
2. J. Baker, K. N. Vander Meulen, A. Van Tuyl, *Shedding vertices of vertex decomposable graphs*, arXiv:1606.04447, first public 2016-06-14; revised and published under a related title. https://arxiv.org/abs/1606.04447.
3. Standard graph-theoretic Independent Set decision problem and the usual VC/Littlestone definitions; their use is explained explicitly above rather than attributed as new.
