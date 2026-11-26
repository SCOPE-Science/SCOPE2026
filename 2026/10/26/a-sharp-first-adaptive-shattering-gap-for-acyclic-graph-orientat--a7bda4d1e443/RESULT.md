# The first bipartite adaptive-shattering gap and an unbounded gap in connected planar subcubic graphs

## Finding

Let \(G\) be a finite simple undirected graph. After fixing a reference direction for each edge, let \(\mathcal A(G)\subseteq\{0,1\}^{E(G)}\) be the class of acyclic orientations, with edge directions as the query coordinates. By the forest criterion of Kozma and Moran, its VC dimension is \(|V(G)|-c(G)\), where \(c(G)\) counts connected components, including isolated vertices. We use this known formula as the benchmark for the following Littlestone-dimension results.

1. VC and Littlestone dimensions coincide for pseudoforests (graphs with at most one cycle per component).
2. For \(K_{2,3}\), there are \(46\) acyclic orientations, the VC dimension is \(4\), and the Littlestone dimension is \(5\). There is no strict gap on fewer than five vertices in the bipartite class, and \(K_{2,3}\) is the only five-vertex bipartite graph with a strict gap, up to isomorphism.
3. For each \(s\ge1\), there is a connected planar bipartite graph \(G_s\) of maximum degree three on \(5s\) vertices with VC dimension \(5s-1\) and Littlestone dimension \(6s-1\). Thus the gap is unbounded even under these restrictions.

Littlestone dimension measures realizable online mistake complexity, not the number of queries needed to identify a hidden orientation.

## Assumptions and scope

A coordinate set is VC-shattered if every labeling extends to a concept. A complete binary query tree is Littlestone-shattered if every path of labeled answers extends to a concept; different nodes at the same depth may query different coordinates. At any node the two outgoing edges carry opposite binary labels. Changing the reference directions complements coordinates and does not change either dimension. The empty query domain has dimension zero.

## Proof

**Known forest criterion.** For completeness, a set of edges containing a cycle cannot be shattered: the cyclic orientation of that cycle has no acyclic extension. Any orientation of a forest has a topological ordering; directing the other edges forward in that order extends it acyclically. The maximum forest size is \(|V(G)|-c(G)\).

**Product rule.** On disjoint query domains, VC dimension is additive for Cartesian products of nonempty concept classes, since traces factor. Littlestone dimension is additive too. Concatenating shattered trees gives the lower bound. For the upper bound, the optimal realizable mistake-bound algorithms run separately on each query domain. Each query contributes to only its own factor's mistake bound, so the total bound is the sum of the factors' Littlestone dimensions. These arguments iterate for any finite number of factors.

**Pseudoforests.** Forests have unrestricted edge orientations, so both dimensions equal their edge count. A cycle with \(r\) edges excludes exactly two of the \(2^r\) orientations. Any shattered tree of depth \(r\) would need \(2^r\) distinct witnesses, one per leaf, since witnesses in distinct branches disagree at their first divergence. Hence the Littlestone dimension is at most \(r-1\), and the VC dimension equals \(r-1\) by the forest criterion. Since VC dimension is always at most Littlestone dimension (query a fixed shattered set in order), equality holds. In a unicyclic component every edge outside the unique cycle is a bridge, whose orientation is unrestricted. The product rule applies to these bridges and to disjoint components, proving equality for every pseudoforest.

**The six-edge example.** Write the parts of \(K_{2,3}\) as \(\{a,b\}\) and \(\{u,v,w\}\). The certificate coordinates, in order, are \((a,u),(a,v),(a,w),(b,u),(b,v),(b,w)\); bit zero directs an edge from its listed first endpoint to its second. All directed cycles would have length four. For each \(z\in\{u,v,w\}\), put the two incident bits into the pair \((p_z,q_z)\), with the \(a\)-edge first. A directed four-cycle occurs exactly when both pairs \(01\) and \(10\) occur at distinct vertices \(z\). The allowed words are therefore the union of \(\{00,01,11\}^3\) and \(\{00,10,11\}^3\), with intersection \(\{00,11\}^3\). This gives \(2\cdot3^3-2^3=46\) words. Because \(46<64\), depth six is impossible. The 31 queries and 32 witnesses in the accompanying `certificate.json` give a shattered depth-five tree, so the Littlestone dimension is five. The VC dimension is four by the forest criterion.

With at most four vertices a bipartite graph cannot have two independent cycles. On five vertices, a component with two independent cycles needs at least five vertices and at least six edges. The only bipartition on five vertices admitting six edges is the \(2+3\) partition, and all six edges must be present. All other bipartite graphs on at most five vertices are pseudoforests. This proves minimality and uniqueness.

**The connected family.** Take \(s\) disjoint copies of \(K_{2,3}\) and label their degree-two vertices \(u_j,v_j,w_j\) in copy \(j\). For each \(1\le j<s\) join \(w_j\) to \(u_{j+1}\) by a single bridge. This connects the copies without making any degree exceed three, as bridge endpoints are distinct within a copy. Each block is planar and joining components by a bridge preserves planarity. Reverse the bipartitions of alternate copies to preserve bipartiteness. No directed cycle can use a bridge, so the class is a Cartesian product of the \(s\) orientation classes of the copies and \(s-1\) unrestricted bits. Its Littlestone dimension is \(5s+s-1=6s-1\). Its VC dimension is \(5s-1\) by connectedness and the forest criterion.

## Verification

The frozen `certificate.json`, `verify.py`, `independent.cpp`, `verify_output.txt`, and `cpp_output.txt` are unchanged. The certificate stores the 31 internal labels in breadth-first heap order and the 32 witnesses in lexicographic branch order. At depth \(t\) after branch prefix \(j\), the query is at index \(2^t-1+j\). Each witness must be an acyclic orientation and agree with all five branches on its path. The supplied Python and C++ checkers encode these finite conditions. The all-\(s\) conclusion uses the product proof, not finite extrapolation.

## Relationship to prior work

Kozma and Moran, *Shattering, Graph Orientations, and Connectivity*, [arXiv:1211.1319](https://arxiv.org/abs/1211.1319), §3.1, Lemma 12(ii) and Proposition 15(i), already prove the forest criterion and the VC formula. Neither is claimed as new here. Walker, [arXiv:2203.12211](https://arxiv.org/abs/2203.12211), gives general tree-shattering bounds; Pradeep, Nachum and Gastpar, [arXiv:2206.13257](https://arxiv.org/abs/2206.13257), study the information complexity associated with Littlestone dimension. Neither inspected result determines the gap here. Pikhurko, [arXiv:0904.1229](https://arxiv.org/abs/0904.1229), studies adaptive identification queries, a different invariant. Manurangsi, [DOI 10.4230/LIPIcs.ITCS.2023.85](https://doi.org/10.4230/LIPIcs.ITCS.2023.85), gives general hardness results for computing the dimensions, not this explicit class.

Two records indexed after the frozen version also cover parts of the theorem. [*The cactus boundary for adaptive shattering of acyclic orientations*](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-the-cactus-boundary-for-adaptive-shattering-of-acyclic-orientati--8e8760549ada) gives the equality criterion for cacti and a strict gap for noncacti, covering the pseudoforest equality and implying the five-vertex bipartite minimum. [*Exact online shattering for acyclic orientations of complete bipartite graphs*](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-exact-online-shattering-for-acyclic-orientations-of-complete-bip--266cc45dc40e) gives formulas for \(K_{2,n}\) that include \(46,4,5\) at \(n=3\). These overlaps do not determine historical priority. Neither comparison states the connected bridge-chain construction with the displayed dimensions.

## Limitations

The minimality statement is specific to bipartite graphs. The connected family uses bridges and does not settle the question under two-edge-connectivity. No claim is made about active identification cost, the dimensions of arbitrary orientation classes, or exhaustive literature priority.
