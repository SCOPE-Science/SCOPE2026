# Incidence forests of two equivalences are identified by separate counting refinement

## Finding
Let \(A=(X,E,F)\) be a finite nonempty structure in which both named binary relations are equivalence relations. Construct the two-sorted bipartite **incidence multigraph** \(I(A)\): the left vertices are the \(E\)-classes, the right vertices are the \(F\)-classes, and each element \(x\in X\) is a distinct edge joining its two classes. Parallel edges are retained.

Start with a common colour \(c_0(x)\), and refine every element simultaneously by
\[
c_{r+1}(x)=\bigl(c_r(x),\ \operatorname{MSet}\{c_r(y)\mid E(x,y)\},\ \operatorname{MSet}\{c_r(y)\mid F(x,y)\}\bigr).
\]
Here the right-hand expressions are canonically comparable between structures, including multiplicities, and \(\operatorname{MSet}\{\cdots\}\) denotes a finite multiset (the relation classes include \(x\) itself).

**Theorem.** If \(I(A)\) is a forest, then every finite two-equivalence structure \(B\) having the same multisets of element colours as \(A\) after \(|X|+1\) rounds is isomorphic to \(A\). Consequently \(A\) is identified among **all finite structures with two named equivalences** by two-variable first-order logic with counting \(C^2\). A characteristic \(C^2\) sentence can be chosen with quantifier rank at most \(|X|+2\). Moreover, within such an \(A\), stable refinement colour classes coincide with automorphism orbits.

The assertion is not that all two-equivalence structures are distinguishable: incidence cycles and parallel edges can obstruct identification. Nor does the theorem claim identification among interpretations where \(E,F\) are not equivalences.

## Assumptions and scope
Both relations are reflexive, symmetric, and transitive; no unary predicates are present. The universe is finite and nonempty, the two sorts of incidence vertices are distinguished, and multiple incidence edges count separately. An isomorphism preserves the names \(E,F\), hence the bipartition. Graph-theoretic forest means no cycles in the multigraph, including length-two cycles formed by parallel edges. The incidence graph has no isolated vertices because its class vertices are nonempty.

The displayed refinement is deliberately weaker than full atomic-type refinement for a language with two binary symbols: it counts \(E\)-neighbours and \(F\)-neighbours separately. Full \(C^2\) equivalence still implies agreement under this refinement, which is all that is needed.

## Proof
**1. Two-sided rooted unfoldings.** For an element \(x\), define finite rooted, side-labelled trees \(L_r(x),R_r(x)\) recursively. At depth zero let \(L_0(x)\) be one node labelled \(L\) and \(R_0(x)\) one node labelled \(R\). Recursively set
\[
L_{r+1}(x)=\left[L;\ \operatorname{MSet}\{R_r(y)\mid E(x,y),\ y\ne x\}\right],
\qquad
R_{r+1}(x)=\left[R;\ \operatorname{MSet}\{L_r(y)\mid F(x,y),\ y\ne x\}\right],
\]
where brackets specify a root of the displayed type with one separate child subtree for every listed occurrence. Isomorphism types of rooted trees are used, rather than any chosen vertex labels. These are unfoldings along alternating sides of the incidence graph, disallowing immediate reversal across the same incidence edge. They are defined for arbitrary incidence multigraphs, not only forests.

**2. Refinement recovers these unfoldings.** For each integer \(r\ge0\), the colour \(c_r(x)\) uniquely determines the ordered pair \((L_r(x),R_r(x))\). At \(r=0\) this is immediate. Assume the assertion at \(r\). The colour \(c_{r+1}(x)\) gives both \(c_r(x)\) and the multiset of \(c_r(y)\) for all \(y\) in its \(E\)-class. By induction, that multiset gives all \(R_r(y)\); from it remove exactly one occurrence of \(R_r(x)\), which is known from \(c_r(x)\). The remainder is precisely the child multiset defining \(L_{r+1}(x)\). Interchanging \(E,F\) proves the assertion for \(R_{r+1}(x)\). This also handles any multiplicities without a uniqueness assumption.

**3. Finite incidence forests are fully reconstructed.** Suppose \(|X|=n\) and \(I(A)\) is a forest. Deleting an incidence edge \(x\) splits its component into the left and right rooted parts. Because paths are unique, the unfoldings \(L_{n+1}(x),R_{n+1}(x)\) are exactly these finite parts with the distinguished half-edge removed; no vertex or other edge is repeated. Their union along the marked edge reconstructs the entire side-labelled incidence component, rooted at \(x\). Each of the two unfoldings has at most \(n-1\) child-edge occurrences.

Now suppose \(B\) has the same round-\(n+1\) colour histogram. It has exactly \(n\) elements because the total size of that histogram is \(n\). If \(I(B)\) contained a cycle (a parallel-edge 2-cycle is included), an element \(b\) on that cycle would have an alternating nonbacktracking incidence walk of every length. Consequently at depth \(n+1\), at least one of \(L_{n+1}(b),R_{n+1}(b)\) would contain at least \(n\) child-edge occurrences. By Step 2 its colour cannot equal any colour in \(A\), contradicting histogram equality. Thus \(I(B)\) is also a forest.

Step 2 now shows that every colour in the common histogram determines the **complete edge-rooted incidence component** of any element carrying it, up to side-preserving isomorphism. For each unrooted component type \(T\), the number of elements whose edge-rooted component is of type \(T\) equals \(|E(T)|\) times the multiplicity of \(T\). Hence the common colour histogram recovers the entire multiset of connected components, yielding \(I(A)\cong I(B)\), and therefore \(A\cong B\).

**4. Counting logic and orbits.** Each colour condition at round \(r\) is defined recursively by a one-free-variable \(C^2\) formula of quantifier rank at most \(r\), using exact-counting quantifiers for the two classwise multisets and only the variable names \(x,y\). Exact multiplicities of these colours in the whole structure are expressible by \(C^2\) sentences of rank at most \(r+1\). Taking \(r=n+1\) gives a characteristic sentence on the class of finite two-equivalence structures of rank at most \(n+2\). Finally, equal colours in \(A\) determine isomorphic edge-rooted components; an isomorphism between their components, followed where necessary by interchanging isomorphic connected components, extends to an automorphism carrying one element to the other. Automorphisms always preserve every refinement colour, proving the orbit assertion.

## Verification
The accompanying self-contained script `verify_two_equivalence_forests.py` runs exact *global* colour interning on all structures with at most eight elements, modulo relabelling of the first equivalence partition. It checks acyclicity of the incidence multigraph by union-find and compares side-labelled forest isomorphism types by canonical rooted-tree codes. All possible second equivalence partitions are included; cyclic candidates are tracked regardless of enumeration order.

Run `python verify_two_equivalence_forests.py 8` (Python 3, no dependencies). It tests 91,080 partition-pair configurations at order eight, including 17,378 forest configurations and 388 distinct forest isomorphism types, with zero collisions between a forest and a nonisomorphic two-equivalence structure. This is a bounded consistency check; the all-size theorem is established by the argument above, not by enumeration.

## Relationship to prior work
Arvind, Köbler, Rattan and Verbitsky (2015) establish amenability of ordinary undirected forests to usual graph colour refinement. The result here concerns a **different relational presentation**: its elements are incidence edges, while both named equivalences induce cliques in the Gaifman graph. The essential extra transfer step is the subtraction-of-the-marked-edge unfolding reconstruction in Step 2; the ordinary-forest theorem by itself does not state that the weaker relation-wise refinement on the edge universe recovers the incidence forest. This is a close conceptual antecedent rather than a claim that forest amenability is new.

Kieroński and Otto (2005/2012) investigate decidability for two-variable logic constrained by equivalence relations, while Pratt-Hartmann (2015) treats counting logic with equivalences, including undecidability with two equivalences. Their subject is satisfiability, not the present exact finite isomorphism-identification property. Esperet, Gimbel and King (2009) study decompositions of line-graph edges into equivalence subgraphs, not counting-logical reconstruction of a named pair of equivalence relations. None of the inspected material states this two-sided unfolding theorem. General results on relational colour refinement and on tree unfoldings remain a potential route to an unrecognized earlier implication.

## Limitations
The comparison target is required to have both relations as equivalences. No claim is made for arbitrary binary interpretations or infinite structures. The \(n+2\) quantifier-rank bound is sufficient, not asserted optimal. The separate refinement may be strictly weaker than full \(C^2\) in other families. Priority remains subject to specialist verification, particularly work on edge-coloured line graphs, universal covers and relational colour refinement.

## References
1. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first posted 2015-02-04, https://arxiv.org/abs/1502.01255.
2. N. Immerman, E. Lander, *Describing Graphs: A First-Order Approach to Graph Canonization*, in *Complexity Theory Retrospective*, 1990, pp. 59–81.
3. E. Kieroński, M. Otto, *Small Substructures and Decidability Issues for First-Order Logic with Two Variables*, LICS 2005, pp. 448–457, doi:10.1109/LICS.2005.49; expanded J. Symbolic Logic 77 (2012), pp. 729–765.
4. I. Pratt-Hartmann, *The Two-Variable Fragment with Counting and Equivalence*, Mathematical Logic Quarterly 61 (2015), pp. 474–515, doi:10.1002/malq.201400102.
5. L. Esperet, J. Gimbel, A. King, *Covering Line Graphs with Equivalence Relations*, 2009 manuscript, https://kam.mff.cuni.cz/kamserie/clanky/2009/s927.pdf.
