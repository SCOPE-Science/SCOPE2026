# Online shattering of vertex geodesics in trees of diameter at most four

## Finding

Let \(T\) be any finite nonempty simple undirected tree with graph diameter \(D\le 4\). Consider the concept class
\[
\mathcal P(T)=\{\{w\in V(T):w\text{ belongs to the unique }u\!\!\text{--}\!\!v\text{ path}\}:u,v\in V(T)\}.
\]
Singleton paths (\(u=v\)) are included. Every concept is tested by asking whether a specified **vertex** lies on that path. Then
\[
\operatorname{Ldim}\mathcal P(T)=
\begin{cases}
D,&0\le D\le 3,\\
3,&D=4\ \text{and the unique center has degree }2,\\
4,&D=4\ \text{and the unique center has degree at least }3.
\end{cases}
\]
Consequently a realizable deterministic online learner has optimal worst-case mistake bound at most four for every diameter-four tree, independent of its number of vertices, and branching at the unique center causes the first distinction among trees of the same small diameter. For \(D\ge2\), the same path family has VC dimension exactly two; this static bound is established in the unique-shortest-path literature and can also be checked directly in trees.

## Assumptions and scope

A tree is connected, finite, undirected, simple and nonempty. Diameter counts edges; the singleton tree has diameter zero. The unique path from \(u\) to \(v\) includes both endpoints. A complete binary mistake tree of depth \(d\) is shattered if every binary sequence of length \(d\) admits some concept with the corresponding membership labels at the successive, possibly adaptive, vertex queries. There are no weights, directed edges, omitted singleton paths or empty-path concepts. The statement does not classify trees of diameter at least five.

For \(D=4\), the unique central vertex \(r\) has neighbors \(c_1,\ldots,c_m\). Each \(c_i\) is adjacent to exactly \(a_i\ge0\) leaves other than \(r\). At least two of the integers \(a_i\) are positive. The cases \(m=2\) and \(m\ge3\) are exhaustive. Denote \(B_i=\{c_i\}\cup L_i\), with \(L_i\) its attached leaves.

## Proof

**Version-space lemma.** For a nonempty finite set \(F\) of concepts, write \(F_{x,b}\) for the restriction to those concepts taking label \(b\) at vertex \(x\). The shattering recurrence is
\[
\operatorname{Ldim}(F)=\max\bigl(\{1+\min(\operatorname{Ldim}F_{x,0},\operatorname{Ldim}F_{x,1}):F_{x,0},F_{x,1}\ne\varnothing\}\cup\{0\}\bigr).
\]
Thus if for every vertex query at least one branch has dimension at most \(k-1\), then \(\operatorname{Ldim}(F)\le k\). If all hypotheses have at most \(k\) positive labels on the variable coordinates (other coordinates constant across the class), then \(\operatorname{Ldim}(F)\le k\): the all-positive path through a shattered mistake tree must ask distinct variable coordinates, all present in one concept. A one-of-\(t\) family with the all-zero option has dimension at most one.

**Diameter-four leaf lemma.** Fix a leaf \(z\in L_i\). Every path containing \(z\) is uniquely \(P(z,v)\), since \(z\) must be an endpoint. In this restricted class, a query to a second leaf has a singleton positive branch; querying \(c_i\) leaves only \(P(z,z)\) on the negative branch; querying a different \(c_j\) makes the positive branch a one-of-leaf family in \(B_j\), of dimension at most one; and querying \(r\) makes the negative branch the paths from \(z\) to vertices in \(B_i\), again of dimension at most one (split first at \(c_i\)). All possible queries therefore have a branch of dimension at most one. Consequently paths constrained to contain \(z\) have Littlestone dimension at most two.

**Diameter-four neighbor lemma.** Fix \(c_i\), and consider the paths containing it. A leaf query has a positive branch contained in the preceding leaf class and hence has dimension at most two. For a distinct neighbor \(c_j\), paths containing both \(c_i\) and \(c_j\) have endpoints \(u\in B_i\) and \(v\in B_j\). All their variable positive coordinates lie among leaves in \(L_i\cup L_j\), with at most one chosen leaf from each, so this class has dimension at most two. Finally, conditioning a path containing \(c_i\) to omit \(r\) confines it to the star on \(B_i\); its only variable positive coordinates are at most two leaves. Hence each query into the class containing \(c_i\) has a branch of dimension at most two, proving its dimension at most three.

**Diameter-four root-negative lemma.** Paths avoiding \(r\) lie in a single star on \(B_i\). Conditioning on the inclusion of a leaf gives paths through that leaf within its star, a family of dimension at most one. Conditioning on the inclusion of some \(c_i\) gives star paths with at most two variable positive leaf coordinates, of dimension at most two. Querying \(r\) is constant zero. Therefore the class of all paths avoiding \(r\) has dimension at most three.

These lemmas establish the universal upper bound four: at a leaf query choose the positive branch (dimension at most two), at \(c_i\) choose the positive branch (dimension at most three), and at \(r\) choose the negative branch (dimension at most three).

**Degree-two improvement.** Suppose \(m=2\), say the two branches are \(B_1,B_2\). The class of paths containing \(r\) has dimension at most two: querying any child \(c_i\) leaves, on the negative side, the nested root-to-vertex paths in the other branch (rank at most one); querying a leaf in \(L_i\) leaves, on the positive side, root-containing paths from that fixed leaf to \(r,c_j\) or one leaf of \(L_j\) (rank at most one). The query \(r\) is constant. A path avoiding \(c_i\) is either a singleton leaf in \(L_i\), or a path in the star centered at \(c_j\) with leaves \(L_j\cup\{r\}\). This union has dimension at most two: a leaf query yields a positive family of rank at most one, a \(c_j\) query yields a negative family of singleton concepts of rank at most one, and \(c_i\) is constantly absent. Thus for every query of the full path class, either the root-positive branch, a child-negative branch, or a leaf-positive branch has dimension at most two; the whole class has dimension at most three.

**Small diameters.** For diameter two, the tree is a star. At a leaf query the positive paths have rank at most one; at the center query the negative paths are singleton leaves and have rank at most one. Hence the rank is at most two. For diameter three, the tree is a double star with two adjacent centers. Paths containing a fixed leaf have rank at most two by exactly the same second-leaf/own-center/opposite-center argument. Paths avoiding either center form a star-path class together with isolated singleton leaves, of rank at most two. Thus the rank is at most three. For diameter one there are precisely three concepts, the two singletons and the full edge; its rank is one. The singleton tree has one concept, hence rank zero.

**Matching lower bounds.** A geodesically embedded subtree contributes a subfamily of concepts on its own queried vertices; every shattered tree there remains valid in the larger tree. The path on three vertices has a depth-two shattered tree; the path on four vertices has a depth-three tree. The path on five vertices has a depth-three tree. For diameter four with central degree at least three, choose two deep branches and a third neighboring vertex. Their six vertices form the smallest example with edges
\[
\{\{0,1\},\{0,2\},\{2,3\},\{0,4\},\{4,5\}\}.
\]
Its complete depth-four shattered tree is explicitly stored in `tree_geodesic_certificates.json`, including a witnessing endpoint pair for each of the sixteen label sequences. The independent path-membership replay in `verify_tree_geodesic_rank.py` checks every one of those paths. Likewise, the same certificate file supplies the depth-three five-vertex path witness and the lower-diameter witnesses. This completes all cases.

## Verification

Run `python3 verify_tree_geodesic_rank.py` in a Python 3 standard-library environment, with write access to the current directory (or adjust its output file destination). The program enumerates each pair of endpoints and its unique tree path. It independently applies the exact version-space rank recurrence to canonical representatives of all diameter-four trees with five through twelve vertices, grouped by multisets \((a_i)\). There are 128 canonical shapes in that range. It also tests all double stars with one through six leaves on each side, stars of up to nine leaves, two smaller singleton/edge cases, and additional unequal-branch samples. For the explicit extremal certificates the checker traverses all two, four, eight, and sixteen root-to-leaf binary sequences as applicable and verifies the claimed membership answers directly from the endpoint pair.

The output log records `DIAMETER_FOUR_CLASSIFICATION_OK`. The universal upper bound is proved above; the finite verification is a separate consistency test and is not used to extrapolate an infinite theorem.

## Relationship to prior work

Ghazi, Golowich, Kumar and Manurangsi (arXiv:2007.03668v1, publicly posted July 7, 2020) establish general closure bounds for Littlestone and threshold dimensions. Those bounds do not specify exact ranks for unique-path systems nor classify the center-degree transition at diameter four. Earlier, Abraham, Delling, Fiat, Goldberg and Werneck proved that unique-shortest-path hypergraphs have VC dimension at most two; this applies to the present path family but does not determine adaptive mistake-tree depth. A finite-path interval analysis handles trees that themselves are paths; path cases alone do not determine the branching-sensitive rank of diameter-four trees. Rooted descendant-cone concepts are also different: those concepts are anchored subtrees rather than paths between arbitrary endpoint pairs.

## Limitations

The theorem applies only to unweighted vertex-membership geodesic concepts of trees with diameter at most four. Its proof does not classify diameter-five or larger trees, weighted shortest paths in graphs with multiple geodesics, edge-membership questions, nonrealizable learning, or computational running time of an online algorithm. The large-tree upper bounds are exact mathematical statements; finite verification is additional evidence, not an infinite certificate. Prior-publication priority beyond the specifically inspected literature and indexed comparisons remains a residual risk. Independent mathematical audit has not been performed.

## References

1. Badih Ghazi, Noah Golowich, Ravi Kumar, Pasin Manurangsi, *Near-tight closure bounds for Littlestone and threshold dimensions*, arXiv:2007.03668v1 (July 7, 2020), https://arxiv.org/abs/2007.03668. Main dated literature source.
2. Ittai Abraham, Daniel Delling, Amos Fiat, Andrew V. Goldberg, Renato F. Werneck, *VC-Dimension and Shortest Path Algorithms*, https://renatowerneck.wordpress.com/wp-content/uploads/2016/06/adfgw11-vc-dimension.pdf. Earlier VC-theoretic background; Theorem 2 concerns unique shortest paths, not Littlestone dimension.
3. Badih Ghazi et al., *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions*, ALT 2021, PMLR 132:686–696, https://proceedings.mlr.press/v132/ghazi21a.html. Later version of [1].
