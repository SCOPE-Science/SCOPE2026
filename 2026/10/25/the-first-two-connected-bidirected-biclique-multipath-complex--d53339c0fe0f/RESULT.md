# The first two-connected bidirected biclique multipath complex

## Finding
Let \(D_n\) be the **bidirected** complete bipartite graph \(K_{2,n}\), with both arcs along every undirected edge, and let \(X_n\) be its multipath simplicial complex: a simplex is an arc set whose directed graph is a vertex-disjoint union of directed simple paths and isolated vertices. Then, for \(n=6\),
\[
X_6\simeq\bigvee^{169}S^3.
\]
Moreover, among the family \(\{X_n:n\geq1\}\), \(X_6\) is the **first two-connected member**: none of \(X_1,\ldots,X_5\) is two-connected. No assertion about the homotopy type of \(X_n\) for \(n\geq7\) is made.

## Assumptions and scope
The two hubs are vertices \(0,1\); the leaves are \(2,\ldots,n+1\). Arc labels, in order, are \((h,2+i)\) for \(h=0,1\) and \(0\leq i<n\), followed by \((2+i,h)\) for \(h=0,1\) and \(0\leq i<n\). Thus there are \(4n\) distinct vertices in the simplicial complex, each corresponding to one directed arc. A face is precisely a set of arcs with indegree and outdegree at most one at each graph vertex and with no directed cycle. Since each arc meets one of the two hubs and each hub supports at most one arc of each orientation, every face has at most four arcs. This is the **multipath** complex, not the graph's independence, matching, ordinary Morse, or strong Morse matching complex.

We use standard reduced homology; a space is two-connected when its homotopy groups in degrees \(0,1,2\) are trivial. The exact statement concerns this finite family at \(1\leq n\leq6\), with a complete integral homotopy-type conclusion at \(n=6\).

## Proof
**Step 1: finite face model.** The preceding indegree/outdegree and directed-acyclicity conditions are equivalent to the graph being a disjoint union of directed paths and isolated vertices. The forward implication holds because a finite directed graph of indegree/outdegree at most one decomposes into directed paths and directed cycles, and all cycles are excluded. The reverse implication is immediate. Checking every nonempty arc subset of cardinality at most four therefore exhausts the simplicial complex.

**Step 2: an explicit elementary-collapse/discrete-Morse certificate.** The accompanying `morse_certificate.json` lists a sequence of 793 operations on all nonempty faces of \(X_6\), encoded by the bitmask of their arcs. Every `P` operation removes a free face together with its unique immediate coface; every `C` operation removes one maximal face as critical. In the supplied independent checker each `P` is verified to have a unique remaining codimension-one coface, itself maximal, and each `C` to be maximal. Every step preserves a subcomplex, and all 1416 nonempty faces are exhausted. There are exactly 623 matched pairs, one critical vertex and 169 critical tetrahedra, with no critical edges or triangles. The checker also verifies acyclicity directly by topologically sorting the directed Hasse diagram with matched incidences reversed.

An ordered sequence of elementary free-face removals and removals of maximal critical cells defines an acyclic discrete-Morse matching. The elementary discrete-Morse CW theorem therefore gives a CW model with one zero-cell, no one- or two-cells, and 169 three-cells. All the three-cells attach to the sole zero-cell through constant attaching maps, and the resulting CW space is precisely a wedge of 169 three-spheres. Since simple-homotopy reductions preserve homotopy type, this proves the integral homotopy equivalence.

**Step 3: sharpness at six leaves.** Independently of the matching, exact reduced boundary-matrix ranks over \(\mathbb F_2\) give the following vectors \((\widetilde\beta_0,\widetilde\beta_1,\widetilde\beta_2,\widetilde\beta_3)\):

| \(n\) | Betti vector over \(\mathbb F_2\) |
| --- | --- |
| 1 | \((1,0,0,0)\) |
| 2 | \((0,3,2,0)\) |
| 3 | \((0,1,6,0)\) |
| 4 | \((0,0,8,1)\) |
| 5 | \((0,0,1,32)\) |
| 6 | \((0,0,0,169)\) |

A two-connected complex must have zero reduced homology in degrees zero, one and two over \(\mathbb F_2\). Every entry at \(1\leq n\leq5\) violates this condition, whereas the sphere wedge at \(n=6\) is two-connected. Thus six is the first two-connected parameter.

## Verification
The reproducible artifacts are `morse_certificate.json` (the complete 793-step witness) and `verify.py` (standard-library-only checker). Run `python verify.py` in a directory containing these two files. The checker independently reconstructs all simplices directly from arc sets and directed cycle detection, verifies the exact face vector
\[
(f_0,f_1,f_2,f_3)=(24,192,600,600),
\]
checks every elementary operation, verifies the no-cycle condition in the resulting gradient Hasse orientation, and independently recomputes all six small-parameter mod-two homology vectors by binary Gaussian elimination. The script was executed against the two companion artifacts with all checks passing. Since the claimed integral homotopy type is certified by an acyclic matching with critical cells only in dimensions zero and three, it is not inferred from mod-two computations.

## Relationship to prior work
Caputi, Collari and Smith (arXiv:2601.05670, originally public January 9, 2026), study bidirected **paths and cycles**, determine their connectivity and homology, and discuss the unresolved sphere-wedge question for bidirected cycles. The biclique \(K_{2,6}\) is neither a path nor a cycle; no result in the inspected article supplies this biclique homotopy classification or the first two-connected biclique threshold.

Caputi, Collari, Di Trani and Smith (arXiv:2208.04656, first posted August 9, 2022) compute an Euler-characteristic generating function for **one-way oriented** complete bipartite graphs, which yields chessboard complexes, as well as homotopy types for different directed-graph families. A bidirected biclique has directed cycles and is not the one-way graph of their bipartite formula. Also distinct are already-known calculations of ordinary or strong discrete-Morse **matching** complexes of undirected \(K_{2,n}\); their simplices and invariants differ from multipaths. Related published classifications for bidirected double-star **trees** do not include bicliques containing multiple four-cycles. These comparisons support originality to the extent of inspected materials but cannot exclude every unindexed equivalent theorem.

## Limitations
The sharp threshold has only been checked against smaller parameters, so nothing is claimed about all higher parameters. The complete integral homotopy type is established only for \(n=6\); mod-two ranks for other listed values are not integral homotopy classifications. An equivalent result in uninspected literature remains possible. The standard discrete-Morse CW theorem is used as a known result, and the attached certificate is a finite, exactly checkable witness rather than an independent human audit.

## References
1. L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1 (January 9, 2026), https://arxiv.org/abs/2601.05670 . In particular Definition 1.2, Propositions 2.2 and 2.3, Theorems 2.8 and 2.10, and Section 3.
2. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (August 9, 2022), https://arxiv.org/abs/2208.04656 . In particular Section 3.2 and Theorem 3.7.
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145, DOI: 10.1006/aima.1997.1650. Standard discrete-Morse CW correspondence.
