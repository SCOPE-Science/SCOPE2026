# Quadratic-time general-position polynomials of all block graphs

## Finding

For every finite, connected, simple **block graph** \(G\) on \(n\ge 1\) vertices (that is, every maximal nontrivial biconnected block is a clique), the entire general-position polynomial
\[
\psi_G(z)=\sum_{S\subseteq V(G)\text{ general position}}z^{|S|}
\]
can be computed in \(O(n^2)\) coefficient-arithmetic operations after constructing the block decomposition. No fixed bound on clique sizes, vertex degrees, or number of articulation vertices is assumed.

A vertex subset \(S\) is in general position when no shortest path between two distinct vertices of \(S\) contains a third vertex of \(S\). Form the **vertex–block incidence tree** \(T\) with one node for every original vertex, one for every nontrivial clique block, and incidence edges between each block and its vertices. Root \(T\) at any block node. Its original-vertex nodes carry a selection weight \(z\); its block nodes cannot be selected.

For a node \(v\), let \(A_v(z)\) count nonempty internally valid choices below \(v\) that remain valid after attaching one selected vertex on the parent side of \(v\). Let \(B_v(z)\) count nonempty internally valid choices below \(v\) that do **not** remain valid under such an attachment. For the children \(u\) of \(v\), put
\[
P_v(z)=\prod_{u}(1+A_u(z)),\qquad U_v(z)=\sum_u A_u(z),\qquad V_v(z)=\sum_u B_u(z),
\]
with empty product \(1\) and empty sums \(0\). The exact recursion is
\[
\begin{array}{c|cc}
\text{node type}&A_v(z)&B_v(z)\\ \hline
\text{clique-block node}&P_v(z)-1&V_v(z)\\
\text{original-vertex node}&P_v(z)-1+z&V_v(z)+zU_v(z).
\end{array}
\]
If the root is \(r\), then
\[
\boxed{\psi_G(z)=1+A_r(z)+B_r(z).}
\]
For the one-vertex graph, \(\psi_{K_1}(z)=1+z\).

As a concrete mixed-clique example, the block chain consisting of three triangles with vertex sets \(\{0,1,2\}\), \(\{2,3,4\}\), and \(\{4,5,6\}\) has
\[
\psi_G(z)=1+7z+21z^2+19z^3+7z^4+z^5.
\]

## Assumptions and scope

All graphs are finite, undirected, simple and connected. Every edge belongs to exactly one maximal clique block; block nodes of order two are included. Selection is over original graph vertices only. The definitions count labeled vertex subsets rather than equivalence classes under automorphisms. For a single vertex the special case above applies. Polynomial-operation complexity counts additions and multiplications of integer coefficients, not constant-time arithmetic on unbounded integers; each coefficient has at most \(n+1\) bits.

## Proof

**Step 1: Geodesic obstruction.** In a block graph, the block–vertex incidence graph is a tree. The unique graph geodesic between distinct vertices follows the unique incidence-tree route between them, taking a single clique edge whenever the route traverses a block node. Indeed, a simple route through clique blocks exists, and any detour cannot shorten a direct edge inside a clique; a path between different branches must visit their common articulation vertex. Consequently, an original vertex internal to a graph geodesic is necessarily an articulation vertex. For distinct original vertices \(x,y,w\), the vertex \(w\) is internal to an \(x,y\) geodesic exactly when removing the incidence-tree node \(w\) separates \(x\) from \(y\). Thus \(S\) is general position if and only if every selected original vertex \(w\) sees selected vertices in **at most one** component of \(T-w\). No constraint is imposed at unselected nodes.

**Step 2: External-attachment states.** Fix a node \(v\) and its rooted subtree \(T_v\). Let the \(A_v\)-sets be the nonempty subsets of original vertices of \(T_v\) satisfying the Step 1 criterion and still satisfying it after adding one fictitious selected original vertex beyond the parent edge of \(v\). Let the \(B_v\)-sets be those satisfying Step 1 within \(T_v\) but becoming invalid after that exterior attachment. Since the only incidence-tree access to \(T_v\) is through \(v\), the status is independent of the precise exterior vertex. No actual graph vertex is double-counted at a block node: the incidence tree contains one node for each original vertex.

**Step 3: Choices at an unselected node.** The selected sets from distinct child subtrees can coexist precisely when every nonempty child choice is of type \(A\), or when exactly one child choice is of type \(B\) and every other child is empty. To see necessity, a \(B\)-choice already has a selected original vertex that becomes internal to a geodesic when any exterior selection is present. For sufficiency, an \(A\)-choice tolerates all other selections exterior to its subtree, and no selected original vertex at another child subtree can be internal to a path entirely outside it. The first case contributes \(P_v-1\), is itself of type \(A\), and the single-\(B\) case contributes \(V_v\), of type \(B\). This applies to every clique-block node and to an original vertex excluded from the selection.

**Step 4: A selected original vertex.** If original vertex \(v\) is selected, at most one child subtree may contain selected vertices, by Step 1. Such a nonempty child must be of type \(A\), since \(v\) acts as an exterior selected point for that child. Selecting \(v\) with every child empty contributes \(z\) to \(A_v\), whereas selecting \(v\) with exactly one nonempty \(A\)-child contributes \(zU_v\) to \(B_v\): a further exterior selected point would put \(v\) on the path between that point and a chosen descendant. Combining with Step 3 proves the displayed recurrence by induction on subtree height.

**Step 5: Root, termination and complexity.** The root has no exterior, so all internally valid choices are counted by the empty choice and its two disjoint nonempty states: \(1+A_r+B_r\). There are \(n+b\le 2n-1\) incidence-tree nodes when \(n\ge2\), with \(b\) clique blocks. Coefficient-vector degrees never exceed the number of original vertices of their subtrees. A sequential child product requires \(O((1+s)(1+t))\) arithmetic operations when a partial product involves \(s\) original vertices and the next child involves \(t\). The cross terms \(st\) can be charged to pairs of original vertices from distinct child subtrees at their unique lowest common ancestor; the remaining linear terms contribute at most \(O(n^2)\) over all rooted subtrees. Polynomial additions also total at most \(O(n^2)\). A depth-first block decomposition of the input graph uses \(O(n+|E(G)|)\) graph operations; for a simple graph this is within \(O(n^2)\). Hence the complete polynomial is obtained with \(O(n^2)\) coefficient-arithmetic operations. Each coefficient is at most \(2^n\), so standard integer arithmetic remains polynomial-time as well.

## Verification

The accompanying `block_gp.py` includes a standalone decomposition of an input edge list into biconnected clique blocks, rejects non-block graphs, and performs the recurrence. `gp_block_verify.py` independently constructs block graphs, finds all graph distances with breadth-first search, tests every vertex subset against all three-point geodesic obstructions, and compares the resulting coefficient arrays. The verifier tested 3,000 generated small labeled block graphs and exhaustively inspected 2,068,500 vertex subsets; it also compared two independent recurrence implementations on block structures of 30, 50, 100 and 200 blocks. For each case it checked the known degree formula equating \(\deg\psi_G\) with the number of simplicial vertices. All reported checks passed on the actual embedded files.

## Relationship to prior work

Manuel and Klavžar proved in 2018 that the general-position number of a block graph equals its number of simplicial vertices (Theorem 3.6). Their theorem determines only the highest nonzero exponent, not all coefficients. Iršič, Klavžar, Rus and Tuite introduced and studied general-position polynomials in 2024, including particular trees and a general inclusion–exclusion expression over maximal feasible sets (Proposition 2.2). Their paper does not provide a block-incidence polynomial-time recurrence for arbitrary block graphs. Closed formulas previously developed for paths, spiders, caterpillars and generalized windmills concern proper subfamilies and do not give this all-block-graph algorithm. The contribution here is the two-state enumeration and its polynomial-time bound; it does not claim the known general-position number formula as new.

## Limitations

The recurrence is established only for connected block graphs. A nonclique biconnected component can introduce internal geodesic vertices that are not graph cut vertices, invalidating Step 1. The result counts labeled subsets and is not a general formula for maximal general-position sets or an automorphism-orbit census. Exhaustive computation covered finitely many examples and is supportive, not proof of the unrestricted claim. Bibliographic priority remains subject to independent comprehensive examination; no independent scientific audit has been performed.

## References

1. P. Manuel and S. Klavžar, *A General Position Problem in Graph Theory*, Bulletin of the Australian Mathematical Society 98 (2018), 177–187, DOI: 10.1017/S0004972718000473. First publicly available online 18 July 2018.
2. V. Iršič, S. Klavžar, G. Rus and J. Tuite, *General Position Polynomials*, arXiv:2401.05696 (first posted 11 January 2024); Results in Mathematics 79 (2024), article 110.
