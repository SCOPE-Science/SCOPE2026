# Color refinement recovers automorphism orbits on every connected graph of cycle rank at most one
## Finding
Let \(G\) be a finite connected simple graph and write
\[
\beta(G)=|E(G)|-|V(G)|+1
\]
for its cyclomatic number. Run ordinary color refinement from the uniform coloring, and let \(\mathcal P_{\mathrm{CR}}(G)\) denote its stable vertex partition. Let \(\mathcal P_{\mathrm{orb}}(G)\) be the orbit partition of \(\operatorname{Aut}(G)\).

If \(\beta(G)\le 1\), then
\[
\mathcal P_{\mathrm{CR}}(G)=\mathcal P_{\mathrm{orb}}(G).
\]
Equivalently, every tree and every connected unicyclic graph is refinable in the terminology of Arvind--Köbler--Rattan--Verbitsky.

The cycle-rank threshold is sharp. There is a connected graph of cyclomatic number \(2\) for which the two partitions differ: take two triangles, distinguish one vertex in each triangle, and join the two distinguished vertices by a path with two new internal vertices. Color refinement stabilizes after the degree round with one class consisting of the two distinguished degree-\(3\) vertices and a second class consisting of all six degree-\(2\) vertices. The latter class contains two different automorphism orbits: the four triangle vertices and the two internal path vertices.

Connectedness is essential. For example, \(C_3\mathbin{\dot\cup}C_4\) is \(2\)-regular, so color refinement leaves all seven vertices in one class, while automorphisms cannot exchange vertices between the two components.

## Assumptions and scope
Graphs are finite, simple, undirected, and initially uncolored. A graph is called refinable when the stable partition produced by color refinement coincides with the orbit partition of its automorphism group. For connected \(G\), the condition \(\beta(G)=0\) means that \(G\) is a tree, while \(\beta(G)=1\) means that \(G\) is unicyclic.

For a connected graph \(G\) and a vertex \(x\), let \(U_x(G)\) denote the rooted universal cover obtained by unfolding non-backtracking walks from \(x\). Krebs and Verbitsky prove that the color of a vertex after \(r\) rounds is exactly the isomorphism type of the depth-\(r\) truncation of its rooted universal cover. Consequently, two vertices have the same stable color if and only if their rooted universal covers are isomorphic.

## Proof
Automorphisms preserve every color-refinement round, so every automorphism orbit is contained in a stable color class. It remains to prove the converse.

First suppose that \(G\) is a tree. Its universal cover is \(G\) itself. If two vertices \(x,y\) have the same stable color, then their rooted universal covers are isomorphic, hence the rooted trees \((G,x)\) and \((G,y)\) are isomorphic. Such an isomorphism is an automorphism of \(G\) sending \(x\) to \(y\). Thus stable color classes are exactly automorphism orbits.

Now suppose that \(G\) is unicyclic. Let
\[
C=c_0c_1\cdots c_{q-1}c_0
\]
be its unique cycle. Delete the cycle edges. For each \(i\), let \(A_i\) be the finite rooted tree component containing \(c_i\), rooted at \(c_i\).

A universal cover \(U\) of \(G\) has a concrete description. Its distinguished infinite part is a bi-infinite path
\[
\cdots-z_{-1}-z_0-z_1-\cdots ,
\]
and at \(z_j\) one attaches a copy of \(A_{j\bmod q}\), identifying its root with \(z_j\). The covering map sends \(z_j\) to \(c_{j\bmod q}\).

The bi-infinite path is intrinsic in \(U\). Indeed, its vertices are exactly those vertices \(z\) for which \(U-z\) has two infinite connected components. Every vertex outside this path lies in a finite hanging tree and its deletion leaves only one infinite component. Hence every automorphism of \(U\) preserves the bi-infinite path setwise.

Let \(x,y\in V(G)\) have the same stable color. Choose lifts \(\tilde x,\tilde y\in U\). By the universal-cover characterization of stable colors, there is an automorphism \(\phi\) of the tree \(U\) with
\[
\phi(\tilde x)=\tilde y.
\]
Because \(\phi\) preserves the bi-infinite path, its restriction to that path is an automorphism of the two-way infinite path. Therefore there exist \(t\in\mathbb Z\) and \(\varepsilon\in\{1,-1\}\) such that
\[
\phi(z_j)=z_{\varepsilon j+t}
\qquad\text{for every }j\in\mathbb Z.
\]

At each \(z_j\), the finite rooted tree hanging from the path is a copy of \(A_{j\bmod q}\). The restriction of \(\phi\) therefore gives a rooted-tree isomorphism
\[
A_{j\bmod q}\cong A_{(\varepsilon j+t)\bmod q}.
\]
Thus the map
\[
\sigma(i)=\varepsilon i+t\pmod q
\]
is a dihedral automorphism of the cycle that preserves the rooted-tree isomorphism type attached at every cycle position.

For each residue class \(i\), choose a rooted isomorphism
\[
f_i:A_i\longrightarrow A_{\sigma(i)}
\]
induced by \(\phi\) on one lift of the \(i\)-th hanging tree. For the residue containing \(\tilde x\), choose the lift on which \(\phi\) sends \(\tilde x\) to \(\tilde y\). The maps \(f_i\), together with \(c_i\mapsto c_{\sigma(i)}\) on the cycle, glue to an automorphism \(F\) of \(G\). By construction,
\[
F(x)=y.
\]
Hence any two vertices with the same stable color lie in the same automorphism orbit. This proves
\[
\mathcal P_{\mathrm{CR}}(G)=\mathcal P_{\mathrm{orb}}(G)
\]
for every connected unicyclic graph.

For completeness, the stated cycle-rank-\(2\) obstruction is immediate. In the graph formed from two triangles joined through two new internal path vertices, the two distinguished triangle vertices have degree \(3\), while the remaining six vertices have degree \(2\). Every degree-\(2\) vertex has one neighbor in the degree-\(3\) class and one neighbor in the degree-\(2\) class, so the degree partition is already equitable. However, a triangle vertex lies on a \(3\)-cycle and an internal path vertex does not, so no automorphism can exchange the two kinds of vertices.

## Verification
The accompanying `verify.py` performs a finite independent consistency check. It contains graph6 representatives for all \(79\) connected Graph Atlas graphs on at most \(7\) vertices with cyclomatic number at most \(1\). For each representative it computes color refinement directly and computes the automorphism orbits by exhaustive permutation testing, then checks that the two partitions agree.

The same program also checks the explicit \(8\)-vertex cyclomatic-number-\(2\) obstruction described above and confirms that its stable color partition is strictly coarser than its orbit partition.

The checker returns:

`VERIFY_OK atlas_graphs=79 n<=7 beta<=1 counterexample_beta2=PASS`

The finite computation is corroborative only. The all-order theorem is established by the universal-cover argument above.

## Relationship to prior work
Arvind, Köbler, Rattan, and Verbitsky define a graph to be refinable when the stable color partition coincides with the automorphism-orbit partition, and place refinable graphs at the top of the hierarchy
\[
\text{Discrete}\subset \text{Amenable}\subset \text{Compact}\subset \text{Godsil}\subset \text{Tinhofer}\subset \text{Refinable}.
\]
They explicitly note that trees were already known to be refinable. Their full text contains no occurrence of “unicyclic” or “pseudoforest”.

Kiefer, Schweitzer, and Selman prove that every graph identified by two-variable counting logic has its \(C^2\)-partition equal to its orbit partition. That result does not cover the theorem here: a cycle of length at least \(6\) is already a connected unicyclic graph that is not identified by \(C^2\), while it is refinable. The present result therefore concerns orbit recovery on a strictly larger natural class than the amenable/identified graphs supplied by that implication.

Krebs and Verbitsky provide the key local tool: round-\(r\) colors coincide exactly with depth-\(r\) rooted universal-cover types, and equality through all rounds yields an isomorphism of the full rooted universal covers.

Targeted searches for “unicyclic refinable graph”, “coarsest equitable partition orbit partition unicyclic graph”, “1-WL unicyclic orbit partition”, and “pseudoforest color refinement automorphism” did not locate this class theorem. The main residual priority risk is an older or unindexed statement under different terminology, especially in the literature on equitable partitions or fractional automorphisms.

## Limitations
The result is about the stable vertex partition of one connected graph. It does not say that every unicyclic graph is amenable to color refinement as a graph-isomorphism test; this is false, since sufficiently long cycles are not identified by two-variable counting logic.

The theorem does not extend to disconnected pseudoforests without additional hypotheses, as shown by \(C_3\mathbin{\dot\cup}C_4\). It also does not claim that every connected bicyclic graph is non-refinable; the cyclomatic-number-\(2\) example only proves that the class-wide guarantee cannot be extended past cycle rank \(1\).

## References
1. A. Krebs and O. Verbitsky, *Universal covers, color refinement, and two-variable counting logic: Lower bounds for the depth*, arXiv:1407.3175, first posted 11 July 2014; LICS 2015, DOI: 10.1109/LICS.2015.69.
2. V. Arvind, J. Köbler, G. Rattan, and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first posted 4 February 2015; Comput. Complex. 26 (2017), 627--685.
3. S. Kiefer, P. Schweitzer, and E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792, first posted 30 March 2015; MFCS 2015.
