# Sharp online depth bounds for laminar leaf clusters and a five-leaf threshold

## Finding

For a finite laminar family \(\mathcal F\) of distinct nonempty subsets of a ground set, let \(H\ge1\) be the maximum number of members in a strict inclusion chain. Under element-membership queries, its Littlestone dimension satisfies
\[
\operatorname{Ldim}(\mathcal F\cup\{\varnothing\})\le1+\lfloor\log_2 H\rfloor.
\]
This is sharp for every positive integer \(H\), even when the concepts are precisely the leaf clusters of a full regular rooted tree, together with the empty cluster. Every such laminar family has VC dimension at most two.

More precisely, let \(T_{b,h}\) be the complete rooted \(b\)-ary tree of edge-height \(h\), with \(b\ge2\) and \(h\ge0\). Each vertex \(v\) defines the set \(C_v\) of descendant leaves. The concept family is \(\mathcal C(T_{b,h})=\{\varnothing\}\cup\{C_v:v\in V(T_{b,h})\}\), and queries are indexed only by leaves. Then
\[
\operatorname{Ldim}(\mathcal C(T_{b,h}))=1+\lfloor\log_2(h+1)\rfloor,
\qquad
\operatorname{VCdim}(\mathcal C(T_{b,h}))=
\begin{cases}1,&h=0,\\2,&h\ge1.\end{cases}
\]
For any rooted leaf hierarchy \(T\) with \(N\ge2\) distinct leaves, all singleton clusters and its root cluster included, the VC dimension is two and **every two-leaf support is shattered**. Its shattering polynomial is therefore \(1+Nz+\binom N2z^2\). In the class of hierarchies without unary internal vertices, four or fewer leaves never yield Littlestone dimension above two; five leaves are necessary and sufficient for dimension three. Among the twelve nonisomorphic rooted hierarchies on five leaves, exactly the three fully binary ones have dimension three.

## Assumptions and scope

A concept is a subset of a finite ground set \(X\); an instance query is \(x\in X\) and its response is whether \(x\) belongs to the unknown concept. The VC dimension is the largest cardinality of a static support realizing every binary trace. The Littlestone dimension is the largest depth of a complete binary instance-labeled tree with at least one consistent hypothesis on every root-to-leaf path. An empty concept is included in the rooted-tree applications and in the general laminar height bound.

A family is **laminar** if any two intersecting members are comparable by inclusion. Repeated identical clusters are treated as one concept. The integer \(H\) counts distinct nonempty clusters, not edges, on a longest inclusion chain. A rooted hierarchy has its original leaves as the query domain and one concept per *distinct* nonempty leaf-descendant set, plus the empty set. Unary nodes may be suppressed without changing the concept class. For the finite-shape census, rooted trees have no unary internal vertices, children are unordered, and leaves are initially unlabeled; the independent verifier also enumerates every labeled hierarchy.

## Proof

**Laminar VC upper bound.** If three distinct points \(a,b,c\) were shattered, concepts with traces \(\{a,b\}\) and \(\{a,c\}\) would meet at \(a\) but have incomparable traces on the triple. This contradicts laminarity. Thus \(\operatorname{VCdim}\le2\). For a rooted hierarchy with at least two leaves, any distinct \(a,b\) are shattered: the empty concept realizes neither, the singleton leaf concepts realize each individually, and the root cluster realizes both. Therefore every pair is shattered. No triple is; consequently the complete shattering polynomial is \(1+Nz+\binom N2z^2\), including the zero- and one-element supports. With one leaf the class is \(\{\varnothing,\{x\}\}\) and both dimensions equal one.

**Universal online height bound.** Fix any query point \(x\). Since the nonempty concepts containing \(x\) are pairwise intersecting, they form a chain and number at most \(H\). A complete binary tree of depth \(d\ge1\) must leave a complete depth-\((d-1)\) tree on *both* responses to its first query. In particular the positive branch contains at least \(2^{d-1}\) distinct hypotheses. Hence \(2^{d-1}\le H\), or \(d\le1+\lfloor\log_2 H\rfloor\). The argument also covers \(d=0\) trivially. No assumption about branching number or about the sizes of the individual sets is needed.

**Sharpness for regular trees.** In \(T_{b,h}\), any leaf \(x\) lies in exactly \(h+1\) distinct nonempty clusters: the clusters associated with its ancestors, in order of increasing size. In the positive version space of the query \(x\), querying a leaf from the appropriate sibling branch gives every possible threshold cut between consecutive ancestor clusters. Thus that positive version space is exactly a threshold class on a chain of \(h+1\) hypotheses and has Littlestone dimension \(\lfloor\log_2(h+1)\rfloor\). For completeness, the rank of a full set of \(r\) ordered thresholds is \(\lfloor\log_2r\rfloor\): midpoint queries construct that depth, and \(2^d\) distinct hypotheses are necessary for depth \(d\).

The negative response to the first query \(x\) retains the empty set and all clades of any sibling subtree under the root. For \(b\ge2\), this includes an isomorphic copy of \(\mathcal C(T_{b,h-1})\). Set \(L_h=\operatorname{Ldim}(\mathcal C(T_{b,h}))\). Since \(L_0=1\), induction shows \(L_{h-1}=1+\lfloor\log_2 h\rfloor\ge\lfloor\log_2(h+1)\rfloor\) for \(h\ge1\). The positive and negative branches therefore both support depth \(\lfloor\log_2(h+1)\rfloor\). They yield depth one greater at the first query, matching the universal height bound with \(H=h+1\). The VC formula follows from the preceding argument and the existence of two leaves for \(h\ge1\). This proof works for every integer \(b\ge2\) and every \(h\ge0\).

**Sharp five-leaf onset.** A rooted hierarchy with \(N\) leaves and no unary nodes has at most \(2N-1\) nonempty clades, with equality only when every internal vertex has two children. Thus it has at most \(2N\) hypotheses including the empty one. For \(N\le3\), the hypothesis-count bound precludes depth three. If \(N=4\) and depth three were possible, exactly eight hypotheses would be needed; hence the tree must be fully binary. Up to rooted isomorphism its two forms are (i) a pair of cherries under the root and (ii) a four-leaf comb. The first has only three clusters on any leaf-to-root chain, and the online height bound gives dimension at most two. In the comb, querying a leaf outside the deepest cherry gives at most three positive hypotheses, so it cannot start a depth-three tree. Querying either leaf of the deepest cherry yields four positive hypotheses, but on the negative side there are only the empty concept and the other three singleton leaf concepts. This negative subfamily has Littlestone dimension one because every positive response singles out at most one hypothesis. Depth three is impossible in the comb as well. Since the VC dimension is two, all these trees with at least two leaves have Littlestone dimension exactly two.

For \(N=5\), take a root with a two-leaf cherry on one side and a three-leaf subtree on the other, the latter consisting of a singleton and a cherry. Query either deepest leaf \(x\) in the three-leaf subtree. The four ancestor clusters containing \(x\) form a fully accessible four-threshold positive class of dimension two. The negative class contains the full four-hypothesis Boolean class \(\{\varnothing,\{a\},\{b\},\{a,b\}\}\) from the other two-leaf subtree, also of dimension two. Therefore a complete depth-three tree exists. There are only ten hypotheses, so depth four is impossible. Together this proves the exact first five-leaf threshold. The subsidiary statement counting the three attaining shapes among the twelve five-leaf rooted hierarchies is established by two separate exhaustive generators in the supplied verification programs; it is finite and is not used to prove either universal formula.

## Verification

Run `python3 CHECK_LAMINAR.py` and `python3 CHECK_LABELED.py` using Python's standard library only. The first program recursively generates all unordered rooted hierarchy shapes with at most five leaves, evaluates exact VC and Littlestone dimensions from the definitions, and directly checks complete regular trees for branching factors two, three and four at the stated small heights. The second uses labeled set partitions rather than unordered-shape recursion, independently generating all 236 labeled five-leaf hierarchies and recomputing the adaptive ranks. Both programs agree on the shape counts \((1,1,2,5,12)\) and exactly three five-leaf shapes of rank three. The complete binary tree calculations through height four include a 16-leaf instance with 32 hypotheses. All universal assertions above are proved symbolically; exhaustive checks are finite corroboration, not extrapolation.

## Relationship to prior work

Hierarchical clustering literature uses exactly these rooted leaf-descendant clusters as the underlying geometric objects; see Menon et al. (2019), Definition 1 and the accompanying discussion, but their objective is a streaming-clustering approximation guarantee rather than membership-query VC or Littlestone dimension. Walker (2022) studies tree dimension of subsets of branches and a generalized Sauer–Shelah bound, including the standard Littlestone notion; neither its stated tree-embedding dimension nor its counting bound alone gives the present *dual* concept system in which a fixed tree's clusters are hypotheses and leaves are query instances. The present work is not an online clustering approximation algorithm, a new definition of tree dimension, or a claim that a prior general Sauer–Shelah lemma is false.

Related previously recorded mathematical results concern root-to-leaf *paths as hypotheses* queried at tree vertices, or whole phylogenetic *trees as hypotheses* queried by candidate clades. Transposing the path-versus-vertex incidence matrix does not preserve Littlestone dimension in general; those theorems do not give the cluster-as-hypothesis formula, the laminar height extremum, or the five-leaf threshold. Standard finite-class counting bounds alone also do not imply the sharp \(1+\lfloor\log_2 H\rfloor\) height dependence, since a fixed-height laminar family may have arbitrarily many disjoint concepts.

## Limitations

The tree is fixed while the unknown hypothesis ranges over its individual clades; no claim about learning an unknown entire hierarchy or reconstructing its topology is made. The height ceiling can be strict for imbalanced trees; the exact formula is asserted for regular complete trees, not arbitrary hierarchies. The five-leaf isomorphism-type count is supported by complete finite enumeration. The comparison with published literature is bounded by the accessible full texts and index; independently established priority is not claimed. Independent mathematical audit has not been performed.

## References

1. A. K. Menon, A. Rajagopalan, B. Sumengen, G. Citovsky, Q. Cao, S. Kumar, *Online Hierarchical Clustering Approximations*, arXiv:1909.09667 (first publicly available 2019-09-20), especially Definition 1 and Sections 2–3. https://arxiv.org/abs/1909.09667
2. R. Walker, *Tree Dimension and the Sauer–Shelah Dichotomy*, arXiv:2203.12211 (first publicly available 2022-03-23), especially Sections 1–2. https://arxiv.org/abs/2203.12211
