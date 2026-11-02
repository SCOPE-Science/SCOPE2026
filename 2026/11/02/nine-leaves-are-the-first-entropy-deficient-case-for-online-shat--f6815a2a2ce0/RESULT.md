# Nine leaves are the first entropy-deficient case for online shattering by tree geodesics

## Finding

For a finite, undirected tree \(T\) with leaf set \(L(T)\), let
\[
\mathcal P(T)=\{V(P_T(a,b)):\{a,b\}\in\tbinom{L(T)}2\},
\]
where \(P_T(a,b)\) is the unique simple path joining distinct leaves \(a,b\). The examples are Boolean vertex-membership concepts: on query \(v\in V(T)\), the response is whether \(v\) lies on the unknown path. For \(m\ge2\), set
\[
U(m)=\max_{T:\,|L(T)|=m}\operatorname{Ldim}(\mathcal P(T)).
\]
The maximum is taken over all finite trees, with no restriction on internal degrees or edge subdivisions.

**Theorem.** The complete initial extremal spectrum is
\[
\begin{array}{c|rrrrrrrrr}
m&2&3&4&5&6&7&8&9&10\\\hline
U(m)&0&1&2&3&3&4&4&4&5.
\end{array}
\]
In particular, \(U(m)=\lfloor\log_2\binom m2\rfloor\) at every \(2\le m\le8\), but
\[
\boxed{U(9)=4<5=\lfloor\log_2\binom92\rfloor,\qquad U(10)=5.}
\]
Thus nine is the first leaf count where the elementary hypothesis-count upper bound is unattainable for *every* tree, even when arbitrarily many subdivision vertices may be queried; the bound is attained again at ten leaves.

For every finite tree with \(m\ge2\) leaves, the same concept class has
\[
\operatorname{VCdim}(\mathcal P(T))=
\begin{cases}0,&m=2,\\1,&m=3,\\2,&m\ge4.\end{cases}
\]
The threshold is about **maximum attainable** online dimension for a fixed number of leaves; it does not assert that all trees with nine leaves have Littlestone dimension four.

## Assumptions and scope

All trees are finite, simple, connected and acyclic, and have at least two leaves. A path includes both endpoints and all intervening vertices. Two distinct unordered leaf pairs yield distinct concepts because the two leaves belonging to any path identify its endpoints. No empty path, single-leaf path, arbitrary-endpoint path, edge query or topology-selection hypothesis is included. A complete Littlestone tree of depth \(d\) has \(2^d\) leaves, with vertex queries at its internal nodes, and every binary answer sequence has a consistent path witness.

## Proof

**1. VC dimension.** For any three distinct vertices \(x,y,z\) of a tree, either one lies on the path between the other two, in which case their all-positive and both-outer-positive traces cannot separate the middle vertex, or no one lies between the other two, in which case no simple path contains all three. Thus no three-point set is shattered. Since there are exactly \(\binom m2\) distinct hypotheses, the dimensions for \(m=2,3\) are at most zero and one, respectively; when \(m=3\) a leaf query realizes both answers. For \(m\ge4\), choose two distinct leaves \(a,b\) and two other leaves \(c,d\). The four paths \(P_T(c,d),P_T(a,c),P_T(b,c),P_T(a,b)\) realize, on the query support \(\{a,b\}\), the traces \(00,10,01,11\), respectively. Hence the VC dimension is two. (For the three-point argument, the forbidden pattern in the collinear case is \(101\) on the two outer vertices and the middle vertex.)

**2. Counting and the first-query reduction.** There are \(N=\binom m2\) distinct concepts, so \(\operatorname{Ldim}\le\lfloor\log_2 N\rfloor\). If an internal query vertex \(v\) has components with \(m_1,\ldots,m_s\) original leaves after deletion, the negative and positive version spaces have cardinalities
\[
N_0(v)=\sum_{i=1}^s\binom{m_i}2,\qquad N_1(v)=\sum_{i<j}m_i m_j,
\quad \sum_i m_i=m.
\]
The formulas also hold when \(v\) is a leaf by treating its own leaf endpoint separately: \(N_1(v)=m-1\). Each component in an internal-vertex deletion has at least one original leaf. If a depth-five tree is shattered with \(m=9\), both responses to its first query must admit depth four and therefore contain at least 16 hypotheses. A direct check of the positive partitions of nine leaves shows that, apart from a leaf query (whose positive part has only eight hypotheses), the *only* possible first-query component-size partitions are
\[
(3,6): (N_1,N_0)=(18,18),\quad
(4,5): (20,16),\quad
(1,2,6): (20,16).
\]
In particular, no vertex of degree four or higher can be the first query.

**3. A crucial eight-hypothesis lemma.** Suppose a concept class consists of all six paths joining pairs of four leaves in some tree component, plus two additional paths, each vertex-disjoint from all six and from the other additional path. This eight-element class has Littlestone dimension at most two. Indeed, if it shattered depth three, its first query would split exactly \(4+4\). A query on either additional path has at most one positive hypothesis. A query inside the four-leaf component selects exactly four of its six pair paths only when it separates those four leaves into two pairs. This is because a leaf query selects three, a two-component split selects \(ab\) with \(a+b=4\), and a three- or four-component split selects at least five. After a \(2+2\) split, the negative branch consists of the two paths internal to the two leaf pairs, together with the two additional paths: all four are pairwise vertex-disjoint. An arbitrary family of distinct pairwise disjoint nonempty concepts has Littlestone dimension at most one, because every positive query has at most one consistent hypothesis. Hence the negative branch cannot shatter depth two, a contradiction. The argument also allows degree-two query vertices arising from subdivisions.

**4. Excluding the three potential first-query types at nine leaves.** For a \((3,6)\) split, the 18 positive hypotheses join a leaf in the three-leaf component to a leaf in the six-leaf component. Every query within one side depends only on its endpoint on that side; the root query is constant. Therefore the positive class is a direct product of two rooted leaf-path concept classes on disjoint query domains. Littlestone dimension is additive under such products (by the usual two-branch recurrence), and each factor has at most respectively three and six hypotheses. Its dimension is thus at most \(\lfloor\log_2 3\rfloor+\lfloor\log_2 6\rfloor=3\), not four.

For a \((4,5)\) split, the negative class has \(\binom42+\binom52=6+10=16\) hypotheses, with disjoint supports in the two components. A depth-four tree would require a \(8+8\) first split. The query cannot lie in the four-leaf component, which contains only six hypotheses. Within the five-leaf component, selecting exactly eight of its ten leaf-pair paths forces a vertex separation of type \((1,2,2)\): a leaf selects four, a two-part split selects at most six, and other multiparts select seven, nine or ten. The negative branch of this second query consists of all six paths from the four-leaf component plus the unique internal pair path in each of the two two-leaf components. These two extra paths are mutually vertex-disjoint and disjoint from the original four-leaf component. By Step 3 this eight-element negative branch has rank at most two, whereas depth four would require rank at least three. Contradiction.

For a \((1,2,6)\) split, the negative class consists of one path from the two-leaf component plus all fifteen paths from the six-leaf component, again totaling sixteen. Its first query must split \(8+8\); this is possible only within the six-leaf component. Selecting eight of fifteen pair paths forces a two-part split of \((2,4)\): a leaf selects five, two-part splits select \(5,8,9\), and three or more nonempty parts select at least nine. Its negative branch comprises all six paths within the four-leaf part and one path in each of two other, mutually disjoint components. Step 3 again bounds the branch rank by two, contradicting the rank-three requirement. Thus no nine-leaf tree shatters depth five, and \(U(9)\le4\) without any bound on the number of subdivision vertices.

**5. Matching lower bounds and the ten-leaf return.** Let \(Q_m\) for \(m\ge4\) be the unrooted binary caterpillar with an internal spine of \(m-2\) vertices: attach two leaves to each endpoint of the spine and one leaf to each other spine vertex. Take \(Q_3\) to be the three-leaf star and \(Q_2\) to be a single edge. The accompanying finite certificates give complete adaptive decision trees of the following depths:
\[
\begin{array}{c|rrrrrrrrr}
m&2&3&4&5&6&7&8&9&10\\\hline
\operatorname{Ldim}(\mathcal P(Q_m))&0&1&2&3&3&4&4&4&5.
\end{array}
\]
Every certificate specifies the adjacency lists, every internal query vertex, and an actual unordered leaf pair at every terminal node. The independent verifier reconstructs the paths, checks all answers on each root-to-leaf branch, confirms that all terminal witnesses are distinct, and separately computes the exact online rank for these nine explicit trees. The hypothesis-count upper bound proves the optimality of the displayed witnesses for \(m\le8\) and \(m=10\), and Step 4 proves it for \(m=9\). Consequently this establishes the entire asserted extremal table.

## Verification

The reproducibility files are `certificates.json`, `verify_cert.py` and `make_cert.py`. From their common directory, execute `python verify_cert.py`; it requires only the Python standard library. `certificates.json` contains a complete tree and witness for each \(m=2,\ldots,10\). The verifier uses independent breadth-first path reconstruction and the exact recurrence
\[
\operatorname{Ldim}(H)=\max_{v:\,H_0(v),H_1(v)\ne\varnothing}
\left(1+\min\{\operatorname{Ldim}(H_0(v)),\operatorname{Ldim}(H_1(v))\}\right)
\]
with rank zero for nonempty singleton version spaces. It also enumerates all integer partitions of nine, confirming the three candidate first-query splits. Running `python make_cert.py` independently regenerates the certificates through a bitmask-based recurrence. The proof of the universal nine-leaf upper bound is mathematical, not an extrapolation from the finite examples.

## Relationship to prior work

Fox, Pach and Suk (2021) develop general VC and Littlestone theory for sunflower problems and use a *root-to-leaf* path class as a VC-one construction; their definitions and general bounds do not determine leaf-*pair* geodesic online ranks. Walker (2022) studies the combinatorial tree dimension of arbitrary collections of branches of a Boolean tree, deriving general Sauer–Shelah bounds and maximality classifications. Its hypotheses and queries differ from the fixed-tree leaf-pair incidence family here. The present theorem concerns a sharp obstruction to attaining the basic hypothesis-count bound in this restricted geometric concept family, not a new general bound for all classes. The closest previous graph-path and rooted-comb results concern different endpoint restrictions or different concept classes and do not imply the nine-leaf obstruction.

## Limitations

The theorem determines the extremal function only for \(2\le m\le10\); it does not classify every tree attaining the maximum, nor determine the extremal rank for \(m\ge11\). The nine-leaf upper bound holds even for subdivided trees, but the supplied examples use unsplit finite caterpillars. Literature searches and inspected primary text do not certify historical priority under all possible synonyms, particularly split systems, phylogenetic path incidence and learning from tree-metric probes. These mathematical claims have not been independently externally audited.

## References

1. J. Fox, J. Pach and A. Suk, *Sunflowers in Set Systems of Bounded Dimension*, arXiv:2103.10497, first submitted 2021-03-18, SoCG 2021, DOI 10.4230/LIPIcs.SoCG.2021.37. Open version: https://arxiv.org/abs/2103.10497 .
2. R. Walker, *Tree Dimension and the Sauer–Shelah Dichotomy*, arXiv:2203.12211, first submitted 2022-03-23. Open version: https://arxiv.org/abs/2203.12211 .
