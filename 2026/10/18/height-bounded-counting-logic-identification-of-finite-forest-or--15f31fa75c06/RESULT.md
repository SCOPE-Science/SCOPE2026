# Height-bounded counting-logic identification of finite forest orders, and its sharp acyclic boundary

## Finding

A **forest order** is a nonempty finite strict poset \((P,<)\) such that the strict predecessor set \(\{y:y<x\}\) is a chain for every \(x\). Put
\[
h=\max_{x\in P}|\{y:y<x\}|,\qquad t=\max\{1,h\}.
\]
In the signature containing just \(<\), the following statements hold.

**Relative identification and orbits.** The multiset of vertex colours after \(t\) rounds of directed counting refinement identifies \(P\) up to isomorphism **among all finite strict posets**. Thus a \(C^2\) sentence of quantifier rank at most \(t+1=\max\{2,h+1\}\) identifies \(P\) relative to finite strict posets. After at most \(t+1\) rounds, refinement classes on \(P\) are exactly its automorphism orbits.

**Logical-rank witness.** Already at height \(h=2\), rank two does not suffice for every forest order: the nonisomorphic seven-element forest orders described below agree on all \(C^2\) sentences of quantifier rank at most two and are separated at rank three. Therefore the bound \(h+1=3\) is attained for the height-two family.

**Transitivity boundary.** Among all finite *acyclic directed graphs* (one binary arc predicate), every forest-order relation on at most five vertices is \(C^2\)-identifiable, but some six-vertex forest order is not. In fact, the disjoint union of two three-element strict chains is \(C^2\)-equivalent to an explicitly given nontransitive acyclic digraph on six vertices. Thus the poset assumption in the unbounded identification theorem cannot be dropped.

## Assumptions and scope

All structures are finite and nonempty. A strict poset means irreflexivity and transitivity (hence asymmetry); the binary symbol \(<\) is interpreted as **all** strict comparisons, not just the Hasse covers. Height \(h\) counts edges in a longest chain, so an antichain has \(h=0\). The positive theorem compares against all finite strict posets; it does *not* assert identification among all arbitrary binary structures. The finite acyclic boundary compares against simple loopless acyclic digraphs that need not be transitively closed. The counting constants of identifying sentences may depend on the finite target structure; only quantifier rank is bounded by height.

For precision, let \(c_0\) be the constant colour. Obtain \(c_{r+1}(x)\) from \(c_r(x)\) and the multisets of \(c_r\)-colours of strict predecessors and strict successors of \(x\). Colour names are canonical across structures being compared. In a comparison with equal global colour histograms, the incomparable-neighbour counts are determined by these two multisets and the total colour multiplicities. Hence this two-direction refinement has the usual \(C^2\) distinguishing power for the single strict binary relation. A colour after round \(r\) has a characteristic one-free-variable \(C^2\) formula of rank at most \(r\); prescribing its multiplicity adds at most one quantifier level.

## Proof

**1. Detecting the forest condition under a poset promise.** Let \(a(x)=|\{y:y<x\}|\). The value \(a(x)\) appears in \(c_1(x)\). In a forest order, \(a(x)\) is the depth of \(x\), and each vertex of depth \(d\) has exactly one predecessor at each depth \(0,\ldots,d-1\). This list of predecessor-depth multiplicities appears in \(c_2(x)\).

Suppose a strict poset \(Q\) has the same global \(c_2\)-histogram as a forest order. It therefore satisfies that same predecessor-depth multiplicity property. We show that every strict predecessor set in \(Q\) is a chain. For \(x\) with \(a(x)=d\ge1\), take its unique predecessor \(z\) of depth \(d-1\). All \(d-1\) predecessors of \(z\) are predecessors of \(x\), by transitivity. The unique predecessor of \(x\) at each depth below \(d-1\) must therefore occur below \(z\). Along with \(z\), these exhaust the predecessors of \(x\); they are linearly ordered by applying the same observation recursively. Hence \(Q\) is a forest order. When \(h\le1\), equality of \(c_1\)-histograms already forces every vertex of \(Q\) to have at most one predecessor, so \(Q\) is automatically a forest order without needing round two.

**2. Rooted descendants from few refinement rounds.** For a vertex \(x\) in a forest order let \(T_x\) be the rooted tree consisting of \(x\) and all its strict successors, with cover edges. We prove by induction that for every \(r\ge1\), the colour \(c_r(x)\) determines the rooted isomorphism type of \(T_x\) whenever \(T_x\) has height at most \(r\). For \(r=1\), the subtree is a star and its number of leaves is just the number of strict successors, recorded by \(c_1(x)\). For \(r\ge2\), the immediate children of \(x\) are precisely its strict successors with predecessor count \(a(x)+1\). The \(c_r\)-colour records their \(c_{r-1}\)-colour multiset: predecessor count is itself determined by every positive-round colour. Each child has descendant-subtree height at most \(r-1\), so the induction hypothesis determines each child subtree type. Their multiset determines \(T_x\), proving the assertion.

Let \(P,Q\) be finite strict posets with equal global \(c_t\)-histograms, with \(P\) a forest order of height \(h\) and \(t=\max\{1,h\}\). Step 1 makes \(Q\) a forest order. Each root has predecessor count zero and a descendant subtree of height at most \(h\). Step 2 shows that its \(c_t\)-colour determines the entire rooted component. Equality of the global colour histograms therefore gives identical multisets of rooted components, whence \(P\cong Q\). Characteristic colour-count formulas yield the claimed \(C^2\) rank bound.

**3. Recovering automorphism orbits.** At round \(t\), every vertex's colour determines its rooted successor-subtree type. At the next round, the colour also records the colours of every strict predecessor. Because a forest order has exactly one predecessor at each smaller depth and those depths are already recorded by their colours, this determines the ordered sequence of successor-subtree types along the unique path from its component root to the vertex. Two vertices have the same such sequence if and only if a component-preserving (or component-swapping) rooted-forest automorphism takes one to the other: construct an isomorphism successively along their matched child-subtree types. Conversely automorphisms preserve every refinement round. Thus the \(c_{t+1}\)-partition is exactly the orbit partition.

**4. Rank-three necessity at height two.** Let \(A\) be the disjoint union of a root with three leaf children and a three-vertex chain. Let \(B\) be the disjoint union of a four-vertex rooted tree whose root has two children, one of which has one child, and a root with two leaf children. Both have seven vertices and height two, but their rooted-component shapes differ. In both structures the multiset of \((\text{number of predecessors},\text{number of successors})\) is
\[
\{(0,2),(0,3),(1,0),(1,0),(1,0),(1,1),(2,0)\}.
\]
Hence their round-one colour histograms agree and they satisfy exactly the same \(C^2\) sentences of rank at most two. They are separated at rank three by the sentence saying that some minimal element has exactly three strict successors, one of which has a strict successor. One two-variable spelling is
\[
\exists x\bigl[(\exists^{=0}y\;y<x)\land(\exists^{=3}y\;x<y)\land\exists y\,(x<y\land\exists x\;y<x)\bigr].
\]
The inner reuse of \(x\) shadows the outer binding only within its own subformula.

**5. Six vertices expose the poset promise.** Let \(F\) be the transitive union of chains \(0<1<5\) and \(2<3<4\), with all other pairs incomparable. Let \(D\) have exactly the six arcs
\[
0\to3,\quad0\to5,\quad1\to2,\quad1\to4,\quad2\to5,\quad3\to4.
\]
It is acyclic but not transitive, since \(0\to3\to4\) and \(0\not\to4\). Both structures have three refinement classes of cardinality two, specified by indegree/outdegree \((0,2)\), \((1,1)\), and \((2,0)\). Each vertex in the first class has one arc into each higher class, and each vertex in the middle class has one arc into the last class; conversely every vertex of the last class receives one arc from each earlier class. Therefore this common equitable partition is stable after the first round. The two digraphs are \(C^2\)-equivalent, although they are not isomorphic.

For the minimum-size assertion, the exhaustive verifier enumerates every upper-triangular arc relation on \(n\le5\) vertices, covering every acyclic digraph under some topological labelling. It compares the globally normalized refinement histograms with those of every forest-order relation of the same size, and tests isomorphism via canonical rooted-component codes. There are \(2^{\binom n2}\) such upper-triangular relations at size \(n\); the verifier finds no smaller obstruction. This is a finite exhaustive computational certificate, not an extrapolation from a sample.

## Verification

Run `python3 check_forest_orders.py` and `python3 check_boundary_dags.py` with a standard Python 3 installation; no third-party modules are needed. The first program enumerates all topologically labelled strict posets of sizes one through six, checks the asserted height-based refinement criterion against every competing strict poset, and tests the orbit claim across all \(7!=5040\) increasing-labelled rooted forests on seven vertices (and all smaller sizes). The second checks every topologically presented DAG through six vertices, including all \(32768\) on six vertices, and verifies the first failure at six. Both programs assert their stated conclusions and exit unsuccessfully if they fail. Their exact successful output is provided in `verification_output.txt`. The hand proof establishes the infinite-family claim; the finite runs corroborate it and establish the asserted finite cutoff by complete enumeration.

## Relationship to prior work

Arvind, Köbler, Rattan and Verbitsky establish identification of undirected forests by ordinary graph colour refinement. That theorem concerns the graph of cover edges, not the strict ancestor relation, which includes all transitive comparisons. Recovering covers from a strict order by the usual formula uses a third variable, so the graph theorem alone does not directly supply this two-variable, height-sensitive statement.

Kiefer, Schweitzer and Selman give a general classification of relational structures globally identified by \(C^2\). The present positive conclusion is explicitly *relative to finite posets*, and the six-vertex witness shows that it fails in the unrestricted relational signature. Their general global classification consequently cannot itself be substituted for this promised-class result. No theorem giving the stated relative forest-order rank bound, orbit partition, and sharp acyclic boundary was located in the inspected sources. This is a best-knowledge comparison, not a priority certificate.

## Limitations

The positive theorem relies essentially on the competing structures being strict posets. The logical-height bound is established but is not claimed optimal in all heights; optimality is proved here only at height two. The minimal acyclic obstruction assertion is supported by an exhaustive finite checker, whose domain and source code are provided; it is not a hand classification of all small DAGs. Full priority certainty would require additional specialist literature review. No independent mathematical validation is asserted.

## References

1. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first posted 2015-02-04, https://arxiv.org/abs/1502.01255.
2. S. Kiefer, P. Schweitzer, E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792, first posted 2015-03-30, https://arxiv.org/abs/1503.08792.
