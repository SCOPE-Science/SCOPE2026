# Exact signed-line frustration and minimum-signature census for vertex-disjoint-cycle cacti

## Finding

Let \(G\) be any finite connected simple graph whose cycles are pairwise vertex-disjoint; this includes trees, unicyclic graphs, and cacti formed by joining vertex-disjoint cycle blocks through trees. An isolated vertex is permitted. Let \(\mathcal C_{\mathrm{odd}}(G)\) be its set of odd cycles and write \(d(v)\) for the degree of vertex \(v\). Form the signed antisymmetric line graph \(\mathcal A(G)\) from any oriented incidence matrix \(D\), using signed adjacency \(D^{\mathsf T}D-2I\). The frustration index \(\ell(\mathcal A(G))\) is the minimum number of negative edges across the switching class.

**Theorem.** The exact frustration index is

\[
\boxed{\ell(\mathcal A(G))=\sum_{C\in\mathcal C_{\mathrm{odd}}(G)}\left(\min_{v\in V(C)} d(v)-1\right).}
\]

For each odd cycle \(C\), put \(m_C=\min_{v\in V(C)}d(v)\) and \(Q_C=\{v\in V(C):d(v)=m_C\}\). The exact number \(N(G)\) of **distinct labeled edge-sign assignments** within the switching class that have precisely \(\ell(\mathcal A(G))\) negative edges is

\[
\boxed{N(G)=\prod_{C\in\mathcal C_{\mathrm{odd}}(G)}\left(\sum_{v\in Q_C}\left(1+\mathbf 1_{\{d(v)>2\}}\right)\right).}
\]

An empty sum in the frustration formula is zero, and an empty product in the count is one. Sign assignments are distinguished on the fixed vertices and edges of the signed line graph, not modulo graph automorphisms; orientations of \(G\) that reverse every edge simultaneously give the same sign assignment.

For a unicyclic graph with odd cycle \(C\), the frustration index is the minimum degree on \(C\), minus one. If \(t\) vertices of \(C\) attain that degree, the number of optimal sign assignments is \(t\) when the minimum degree is two, and \(2t\) otherwise. In particular, attaching \(h\ge1\) leaves to every vertex of an odd cycle of length \(r\ge3\) yields frustration \(h+1\) and exactly \(2r\) optimal signatures, although just one edge deletion makes the base graph bipartite.

## Assumptions and scope

All graphs are finite, simple, undirected and connected. Different cycles have no common vertex. A cactus with cycles meeting at cut vertices is **not** covered by this hypothesis. A tree or isolated vertex has no odd cycles, so the formula gives frustration zero and one all-positive signature. There are no restrictions on the number or lengths of attached trees, bridges, or vertex degrees. The degree \(d(v)\) is measured in the entire graph, not only along its cycle.

For an oriented edge \(e\), the incidence entry \(D_{ve}\) is \(+1\) at its head and \(-1\) at its tail, and zero otherwise. For distinct adjacent base edges \(e,f\) sharing \(v\), their signed-line adjacency has sign \(D_{ve}D_{vf}\). Switching at the signed-line vertex \(e\) is achieved by reversing the base-edge orientation of \(e\). In particular the minimum is over the entire switching class.

## Proof

**1. Translation to an orientation objective.** The negative edges of the signed line graph correspond exactly to pairs of incident base edges oriented in opposite directions at their common vertex. In any orientation \(\vec G\), their number is

\[
F(\vec G)=\sum_{v\in V(G)}d^+_{\vec G}(v)d^-_{\vec G}(v).
\]

All switchings correspond to reorienting subsets of the base edges. Hence \(\ell(\mathcal A(G))=\min_{\vec G}F(\vec G)\). This translation is the orientation characterization already established in Bal's Lemma 2 and is used here as prior work.

**2. Sharp lower bound.** Call \(v\) *mixed* when it has at least one incoming and at least one outgoing incident edge. On an odd cycle \(C\), if no cycle vertex were mixed, the two cycle edges would be simultaneously incoming or outgoing at every vertex. Those statuses would alternate around \(C\), contradicting odd length. Thus every odd cycle contains a mixed vertex \(v\). At any mixed vertex of degree \(d(v)\), both indegree and outdegree are positive integers summing to \(d(v)\), so their product is at least \(d(v)-1\). Because the odd cycles are vertex-disjoint, their contributions to \(F\) occur at distinct vertices. Therefore

\[
F(\vec G)\ge\sum_{C\in\mathcal C_{\mathrm{odd}}(G)}(m_C-1).
\]

**3. Construction attaining the lower bound.** For each odd cycle \(C\), independently select a vertex \(q_C\in Q_C\). Orient its two incident cycle edges one in and one out. Orient the remaining cycle edges so that every other vertex of that cycle has both cycle edges directed inward or both outward; this is possible because the cycle has odd length. Orient each even cycle with alternating inward/outward pure vertices. The bridge edges, together with cycle blocks, form a tree of blocks. Work along this tree: at any pure vertex, direct all other incident edges in the same sense as its cycle edges (or as the previously oriented edge at a bridge-only vertex). At every designated \(q_C\), direct all edges external to \(C\) uniformly either inward or outward. Crossing a bridge into another cycle fixes its alternating phase if the endpoint is pure, and is compatible with either phase if that endpoint is designated mixed. Thus the orientations extend consistently throughout the block tree. Every undesignated vertex has either indegree zero or outdegree zero, and every \(q_C\) has indegree/outdegree pair \((1,d(q_C)-1)\) or \((d(q_C)-1,1)\). It follows that \(F(\vec G)=\sum_C(m_C-1)\), proving the first formula.

**4. Classification of equality.** Equality in step 2 requires each odd cycle to contain exactly one mixed vertex, that vertex to have degree \(m_C\), and every other vertex to be pure. Indeed, another mixed vertex on an odd cycle, on an even cycle, or outside a cycle adds a strictly positive term beyond the sharp lower bound. The designated mixed vertex must have its two cycle edges one in and one out, since otherwise odd-cycle alternation forces another mixed cycle vertex. Its remaining incident edges must be uniformly oriented, as only indegree one or outdegree one attains the product \(m_C-1\). Conversely every orientation meeting those conditions attains equality by step 3. This is an exact characterization, not merely a construction.

**5. Enumeration.** Fix one designated minimum-degree vertex \(q_C\) on each odd cycle. Root the tree of blocks, choose the direction/phase on its first block, and propagate along bridges. There are two globally opposite initial phases. More formally, assign one common incidence sign to each pure vertex and one cycle-phase sign to each designated mixed vertex; when that mixed vertex has external edges, assign one further common incidence sign to those edges. Opposite signs are required at the two ends of each base edge. Alternation around any even cycle imposes no additional parity obstruction, and a designated mixed vertex resolves the odd-cycle obstruction. The graph of these incidence-sign constraints is connected before separating the cycle and external sign variables at designated mixed vertices, and since the cycles are vertex-disjoint and the connecting block structure is a tree, each such separation creates one independent binary component. Thus after fixing the first global phase, every other incidence sign is forced apart from one binary choice per designated mixed vertex with external edges. At each designated \(q_C\) with \(d(q_C)>2\) this extra choice is: its external incident edges can be directed all inward or all outward (equivalently, if the rooted bridge enters that vertex, the odd-cycle alternating phase can be selected either way). At a designated degree-two vertex there is no such extra choice. Consequently the number of optimal base-edge orientations with the fixed designated vertices equals

\[
2\prod_{C\in\mathcal C_{\mathrm{odd}}(G)}\left(1+\mathbf 1_{\{d(q_C)>2\}}\right).
\]

An orientation uniquely determines the set of mixed vertices, so different selections of designated vertices give disjoint collections. If \(G\) has at least one edge, its ordinary line graph is connected. Two orientations induce the same signed-line sign assignment exactly when the reorientation sign is constant on this connected line graph; they therefore differ by global reversal of *all* base edges. Hence the orientation-to-signature map is exactly two-to-one. Summing over all selections of \(q_C\) and dividing by two gives the displayed product for \(N(G)\). If \(G\) is an isolated vertex, there is a single empty sign assignment and the product is one directly. This completes the proof.

## Verification

The accompanying standard-library script `verify.py` directly constructs labeled graphs, independently enumerates all orientations, and checks both the minimum of \(F\) and the number of minimizing orientations. A separate routine forms the signed-line adjacency and explicitly enumerates switching assignments with one switching variable fixed, comparing its exact minimum and optimal count against the orientation results. It exhaustively examines 5,428 connected vertex-disjoint-cycle cacti on labeled vertex sets of orders three through six. It additionally tests 169 seeded randomly generated cacti containing up to three vertex-disjoint cycles, with up to 15 base edges, as well as odd-cycle sun families. Its recorded replay result is in `VERIFY_OUTPUT.txt`.

These are finite cross-checks. All-order correctness rests on the block-tree construction and equality classification in the proof, not on the enumeration.

## Relationship to prior work

Bal, *The Antisymmetric Line Graph* (arXiv:2603.03087, first posted March 3, 2026), introduced the studied frustration comparisons and gave the general orientation identity, bounds involving Max-Cut defect, and exact results for selected other graph families. Those identities and the facts for individual odd cycles are not claimed as new. The present theorem **evaluates** the general optimization exactly on the entire vertex-disjoint-cycle cactus class and separately counts all minimizing labeled signatures. Bal's paper, including its relevant frustration and spectral sections, was checked for direct coverage and does not state this family theorem or its signature count.

Belardo, Stanić, and Zaslavsky, *Total graph of a signed graph* (arXiv:1908.02001), discuss signed line graphs and frustration inequalities under closely related, but convention-dependent, constructions. Their inspected sections provide general relations rather than this degree-weighted odd-cycle evaluation or its optimal-switching census. Signed-line sign conventions are fixed above to avoid inferring a theorem from a different signing. Searches under unicyclic/cactus graphs, directed two-path minimization, signed-line frustration, and minimizing switchings did not locate covering formulas. These searches are not a proof of global novelty.

## Limitations

The theorem requires vertex-disjoint cycle blocks; if cycles share a vertex, the lower-bound summands can compete for that vertex and the formula need not hold. The count is for distinct labeled sign assignments in the *one canonical switching class*, not the number of switching classes or isomorphism types. No polynomial-time theorem for arbitrary graphs, independent external review, or exhaustive search beyond the stated finite test families is claimed. Literature indexing, alternate terminology, and unexamined sources are residual originality risks.

## References

1. H. S. Bal, *The Antisymmetric Line Graph*, arXiv:2603.03087 (first public March 3, 2026), https://arxiv.org/abs/2603.03087 . Full text: https://arxiv.org/html/2603.03087 , particularly Sections 3, 8, and 9.
2. F. Belardo, Z. Stanić, and T. Zaslavsky, *Total graph of a signed graph*, arXiv:1908.02001 (2019), https://arxiv.org/html/1908.02001v3 , particularly Sections 2 and 3.
