# The first branching obstruction to three-colouring shattering on trees

## Finding

For a finite tree, the family of proper three-colourings is a natural Boolean concept class under the queries “does vertex \(v\) have colour \(a\)?” A set of vertices \(S\) is **colour-query shatterable** when one can choose a single target colour at each vertex of \(S\) so that every binary answer pattern is realized by some proper three-colouring of the whole tree.

**Theorem (sharp first branching obstruction).** For every nonempty tree \(T\) with \(1\le |V(T)|\le7\) and every \(S\subseteq V(T)\), the set \(S\) is colour-query shatterable if and only if \(T[S]\) is a star forest (has no path on four vertices), with exactly one exception up to isomorphism of the marked pair \((T,S)\): the tree \(B\) with a central vertex \(r\) and three internally disjoint arms of lengths \(3,2,1\), taking \(S=V(B)\setminus\{r\}\). This exception has \(|S|=6\), is a star forest when induced, but is not colour-query shatterable.

Moreover, whenever \(T\) contains \(B\) as an induced subtree and a queried set includes all six noncentral vertices of this copy, that set cannot be shattered. For the exceptional seven-vertex tree,
\[
\max\{|S|:T[S]\text{ is a star forest}\}=6,\qquad
\operatorname{VCdim}(\mathcal C_3(T))=5.
\]

## Assumptions and scope

All graphs are finite, simple, undirected, connected trees, including the single-vertex tree. Colours are exactly \(\{0,1,2\}\) and are labelled. For each proper colouring \(f:V(T)\to\{0,1,2\}\), let \(h_f(v,a)=1\) iff \(f(v)=a\), where the query domain is \(V(T)\times\{0,1,2\}\). A family shatters a query set if it realizes all binary assignments on that set. No shattered query set can contain two distinct colours for one vertex, because the all-one labeling would be impossible. Thus a shattered query set corresponds to distinct vertices \(S\) and a target-colour function \(a:S\to\{0,1,2\}\). The empty query set is shattered because every tree has a proper three-colouring.

A **star forest** is a forest all of whose components are stars, allowing isolated vertices. For an induced subgraph of a tree this is equivalent to containing no four-vertex path. The \((3,2,1)\)-spider \(B\) has one center and three disjoint branches whose respective numbers of noncentral vertices are \(3\), \(2\), and \(1\). Its order is seven.

## Proof

**1. A universal necessary condition.** Suppose the four consecutive vertices \(v_1,v_2,v_3,v_4\) are all queried. The all-one pattern requires their target colours \(a_1,a_2,a_3,a_4\) to be proper on the path. If three consecutive targets are pairwise different, the binary pattern positive at their endpoints and negative in the middle is impossible: their two different fixed endpoint colours force the third colour at the middle, exactly its negative target. Thus to avoid an immediate obstruction, each consecutive target triple must alternate between two colours; for four positions this implies \((a,b,a,b)\) with \(a\ne b\). For the binary pattern \((1,0,0,1)\), the first and last actual colours are \(a\) and \(b\). The second must be the third colour (it differs from \(a\) by properness and from its target \(b\) by the negative label), and the third must also be that third colour (it differs from target \(a\) and from the last actual colour \(b\)), violating properness. Therefore every shattered vertex set induces a star forest. This argument restricts from any larger tree to the four selected vertices.

**2. Structural obstruction at branching.** Let \(B\) have center \(r\) and arms with \(3,2,1\) selected vertices. For a fixed target-colour sequence along an arm and a binary labeling on it, let \(R\subseteq\{0,1,2\}\) be the set of center colours allowing a proper colouring of the arm with those labels. A shattered arm must have proper target sequence (by all-positive labeling). On the length-three arm, the three targets must be \((a,b,a)\), rather than three distinct colours, by the triple obstruction above. Let \(c\) be the third colour. There are three arm labelings for which the allowed center-colour sets are exactly the complements of \(\{a\}\), \(\{b\}\), and \(\{c\}\): respectively \((1,1,1)\), \((0,0,1)\), and \((0,1,0)\). On the length-two arm with proper targets \((d,e)\), writing \(g\) for the third colour, the outcomes \((1,1)\) and \((0,1)\) exclude exactly \(d\) and \(g\) respectively. On the length-one arm, the positive outcome excludes exactly its target \(z\). Choose an excluded colour \(y\) from \(\{d,g\}\) different from \(z\), then the unique third colour \(x\) outside \(\{y,z\}\). The length-three arm admits a labeling excluding \(x\). These three chosen labelings exclude all three possible colours at the center. Therefore they cannot be realized jointly, for **any** target assignment on the six vertices. This also proves the claimed obstruction in larger trees: a colouring of the larger tree would restrict to a forbidden colouring of the seven-vertex induced subtree.

**3. Exact small-order exhaustion.** The attached Python verifiers independently enumerate every unlabeled tree with \(1\le n\le7\). The first builds all labeled trees using Prüfer sequences and deduplicates by canonical center-rooted tree codes; the second uses an independent nonisomorphic-tree generator. For each tree they enumerate **all** selected vertex subsets whose induced subgraph is a star forest. For each such subset they test all proper target-colour assignments. The first compares all binary patterns against exhaustive proper three-colourings, and the second independently checks realizability of every pattern by a bottom-up allowed-colour recurrence on the tree. Thus a positive result certifies a full shattered target assignment, and a negative result exhausts all assignments.

The numbers of unlabeled trees for orders \(1,2,3,4,5,6,7\) are \(1,1,1,2,3,6,11\); the numbers of tested marked pairs are \(2,4,8,31,90,343,1209\). There are no failures through order six and exactly one failure among the \(1209\) order-seven pairs. It is precisely the \((3,2,1)\)-spider with its center unselected, as checked by arm lengths, and is already explained structurally in step 2. These checks complete the if direction and uniqueness under the stated finite order cutoff.

**4. Dimension of the exceptional tree.** That spider has exactly one six-vertex induced star-forest subset: all noncentral vertices. Step 2 rules out shattering it; step 1 rules out every other six-vertex set. Hence the VC dimension is at most five. The attached file `witness_5.json` supplies proper three-colourings realizing every one of the \(32\) binary patterns on vertices \((0,1,3,4,6)\) of the explicitly specified labeled spider with edges \((0,1),(0,2),(1,4),(1,6),(2,3),(4,5)\), with target colours \((0,1,0,0,0)\). The independent `verify_witness.py` checks each of these \(32\) witnesses, proving VC dimension at least five.

## Verification

Run `python3 verify_prufer.py`; it uses only the Python standard library. Run `python3 verify_dp.py` with the publicly available NetworkX package (tested in the supplied environment), and `python3 verify_witness.py`. The matching outputs are included as `output_prufer.txt`, `output_dp.txt`, and `output_witness.txt`. The scripts test actual pattern realization, not only total counts. No unbounded conclusion is extrapolated from the finite enumeration; the assertion about every larger tree is proved by the restriction argument in step 2.

## Relationship to prior work

Blanca, Chen, Štefankovič, and Vigoda (2017), *Structure Learning of H-colorings*, work with proper graph colourings as graph-homomorphism configurations, but infer hidden graph structure from random colouring samples, not coordinate-equality shattering. Walker (2022), *Tree Dimension and the Sauer–Shelah Dichotomy*, develops general VC/Littlestone shattering theory, without a classification of tree-colouring query sets. Manurangsi (2022), *Improved Inapproximability of VC Dimension and Littlestone's Dimension via (Unbalanced) Biclique*, proves general computational hardness for explicit concept classes, not this special seven-vertex obstruction. A published result on forced three-colouring polynomials of degree-two graphs studies a distinct extension/forcing invariant rather than shattering of branching trees. These distinctions concern mathematical implication, not merely titles or dates.

## Limitations

The exact finite uniqueness statement is limited to trees with at most seven vertices. For larger trees the result gives a necessary induced-path obstruction and a necessary marked-spider obstruction, but does **not** assert these conditions are sufficient or provide a general formula for VC dimension. The uniqueness of the seven-vertex failure rests on independently reproducible exhaustive finite enumeration; it is not claimed as a purely human case classification. Uninspected or unindexed literature may contain equivalent or stronger results.

## References

1. A. Blanca, Z. Chen, D. Štefankovič, and E. Vigoda, *Structure Learning of H-colorings*, arXiv:1708.05118, first public version August 17, 2017, https://arxiv.org/abs/1708.05118.
2. R. Walker, *Tree Dimension and the Sauer–Shelah Dichotomy*, arXiv:2203.12211, first public version March 23, 2022, https://arxiv.org/abs/2203.12211.
3. P. Manurangsi, *Improved Inapproximability of VC Dimension and Littlestone's Dimension via (Unbalanced) Biclique*, arXiv:2211.01443, first public version November 2, 2022, https://arxiv.org/abs/2211.01443.
