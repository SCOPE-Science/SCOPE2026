# Ten four-round theories of generalized Petersen graphs with step two

## Finding

For each integer \(n\ge5\), let \(P_n=\operatorname{GP}(n,2)\) be the generalized Petersen graph with vertices \(u_i,v_i\), \(i\in\mathbb Z/n\mathbb Z\), and edges
\[
\{u_i,u_{i+1}\},\quad \{u_i,v_i\},\quad \{v_i,v_{i+2}\},
\qquad i\in\mathbb Z/n\mathbb Z.
\]
Regard \(P_n\) as a first-order structure in the *pure undirected adjacency-and-equality language*: neither the two kinds of vertices nor cyclic indices are named.

**Theorem.** For all integers \(m,n\ge5\), the graphs \(P_m\) and \(P_n\) satisfy the same first-order sentences of quantifier rank at most four if and only if
\[
 m=n,\quad\text{or}\quad\{m,n\}=\{11,13\},\quad\text{or}\quad m,n\ge15.
\]
Consequently there are exactly ten rank-four theories in the family, with parameter classes
\[
\{5\},\{6\},\{7\},\{8\},\{9\},\{10\},\{11,13\},\{12\},\{14\},\{15,16,17,\ldots\}.
\]
Each class has a representative with at most \(30\) vertices; this bound is sharp *within this graph family*. In particular, \(P_{11}\) and \(P_{13}\) are four-round equivalent, even though the intervening graph \(P_{12}\) is equivalent to neither.

## Assumptions and scope

Quantifier rank is the usual nesting depth of first-order quantifiers, with no restriction on the total number of variables. Two graphs are rank-\(q\) equivalent if they agree on all first-order sentences of rank at most \(q\), equivalently if Duplicator wins the \(q\)-round Ehrenfeucht–Fraïssé game. All graphs here are finite, simple, undirected, and exactly of the displayed form. The range \(n\ge5\) ensures the standard cubic generalized Petersen graph.

## Proof

**1. Uniform infinite tail by a cyclic-gap strategy.** For any pair of graphs of the displayed form, temporarily retain the two vertex kinds and cyclic indices as *auxiliary strategy data*, never as relations in the first-order language. After at least one coordinate index has been selected, list the distinct selected indices in cyclic order. Maintain a correspondence of these indices, their selected vertex kinds, and their circular successive positive gaps. With \(r\) rounds left, impose the invariant that each pair of corresponding gaps is either equal and smaller than \(B_r=3\cdot 2^r\), or both are at least \(B_r\). Repeated selections at an old index are copied to its corresponding index, with the same vertex kind.

For a selection at a new index, one gap is split into two positive gaps. If the old gap is smaller than \(B_r\), both structures have the same gap and the identical split is used. If the old gap is at least \(B_r=2B_{r-1}\), then its counterpart is also at least \(2B_{r-1}\). For the selected split, either one subgap is smaller than \(B_{r-1}\) (copy its exact length, leaving the opposite subgap at least \(B_{r-1}\)), or both subgaps are at least \(B_{r-1}\) (choose both counterpart subgaps to be at least that threshold). This maintains the invariant with \(r-1\) rounds remaining. Choosing an old index also preserves the invariant when the threshold decreases.

At \(r=0\), the cutoff is \(B_0=3\). Equality and adjacency among all selected vertices are determined by the selected kinds and by whether two indices agree or are separated in one circular direction by one or two steps. The preserved gap data determine exactly these relations: any oriented distance at most two consists entirely of preserved short gaps, whereas any gap at least three precludes such a distance through that gap. The invariant therefore gives a partial graph isomorphism.

When \(m,n\ge24\), the first vertex can be matched with the same auxiliary kind at any coordinate index. The unique circular gap after that first move has lengths \(m,n\), both at least \(B_3=24\). The remaining three rounds follow the strategy just proved. Thus
\[
P_m\equiv_4P_n\qquad(m,n\ge24).
\]

**2. Exact finite reduction and exhaustive rank-type recursion.** It remains to compute the rank-four theories of \(P_n\) for \(5\le n\le24\), since every larger index is equivalent to \(24\). For an ordered selected tuple \(\bar a\) of length \(s\), let \(A(\bar a)\) be the ordered list of all pairwise equality/adjacency truth values. Define recursively
\[
T_0(\bar a)=A(\bar a),\qquad
T_{r+1}(\bar a)=\bigl(A(\bar a),\{T_r(\bar a,z):z\in V(P_n)\}\bigr).
\]
All sets are genuine mathematical sets: repetition of an extension type does not matter for a single existential quantifier, while later quantifiers can distinguish multiple witnesses through equality in longer tuples. By induction on formulas, two pointed tuples have the same \(T_r\) if and only if they agree on all formulas of quantifier rank at most \(r\) with those free variables. In particular, the root value \(T_4(())\) is a complete rank-four sentence invariant, *not* an approximation.

`verify_orbit.py` evaluates this recursion for all integer indices \(5\le n\le24\), retaining shared exact interners for recursively defined types across different graphs. Its only symmetry shortcut is to normalize selected tuples by an index translation and optional index reflection. Both maps are true automorphisms because edges use index differences \(0,\pm1,\pm2\) according to vertex kind. This reduction never omits a possible one-point extension: the program explicitly examines every vertex. Thus every computed root type is exact.

The output `class_table.csv` gives the complete finite classification. In increasing index order, the class identifiers for \(n=5,6,\ldots,24\) are
\[
(0,1,2,3,4,5,6,7,6,8,9,9,9,9,9,9,9,9,9,9).
\]
The labels only name equivalence classes, not numerical invariants. Exactly ten labels occur, and the first occurrence of the last one is \(n=15\). Together with the infinite-tail lemma this proves the theorem, including the sharp within-family \(30\)-vertex representative bound.

## Verification

From the directory containing this document run `python verify_orbit.py` and `python verify_direct.py` using the Python standard library. The first produces `class_table.csv` and checks the twenty exact root types for \(5\le n\le24\). The second independently constructs edge sets and evaluates the same logical type recursion on **all ordered tuples without symmetry reduction** for \(5\le n\le16\). It gives the same class identifiers for their common range. Recorded executions are included as `verify_orbit_output.txt` and `verify_direct_output.txt`. The infinite range is covered by Step 1 rather than by computation.

## Relationship to prior work

Pikhurko and Verbitsky, *Logical complexity of graphs: a survey* (arXiv:1003.4865, initially posted 2010-03-25), Section 3, supplies the graph Ehrenfeucht–Fraïssé framework, including the equivalence of games and quantifier-depth distinguishability. The survey does not state an exact ten-class partition of \(\operatorname{GP}(n,2)\). Daneshgar and Madani, *On the odd girth and the circular chromatic number of generalized Petersen graphs* (arXiv:1501.06551, initially posted 2015-01-26), studies exactly this broader graph family, but its results calculate odd girth and related colouring invariants, not the four-round logical partition. None of these graph invariants implies the claimed classification.

The known mathematical distinction between graph structure and bounded first-order expressibility matters here: graph size, global graph connectivity and long-cycle information need not be expressible at a fixed quantifier rank. An independently indexed analysis of \(\operatorname{GP}(n,2)\) concerns a scale-two Vietoris–Rips collapse at \(n=13\); its homotopy-type conclusion is not a first-order rank-four implication. No claim of exhaustive priority clearance is made.

## Limitations

The result is specific to step-two generalized Petersen graphs and to ordinary first-order quantifier rank four in the adjacency/equality language. The proof does not determine higher-rank partitions, other step parameters, or logical equivalence relative to structures with distinguished outer/inner vertex colours. Although exact code and a mathematical infinite-tail argument are provided, independent external mathematical verification and complete historical-priority determination have not been performed.

## References

1. O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865 (first posted 2010-03-25), especially Section 3. https://arxiv.org/abs/1003.4865
2. A. Daneshgar and M. Madani, *On the odd girth and the circular chromatic number of generalized Petersen graphs*, arXiv:1501.06551 (first posted 2015-01-26). https://arxiv.org/abs/1501.06551
