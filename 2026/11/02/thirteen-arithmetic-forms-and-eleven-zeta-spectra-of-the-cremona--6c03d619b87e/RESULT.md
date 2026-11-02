# Thirteen arithmetic forms and eleven zeta spectra of the Cremona–Richmond stable curve

## Finding

Let \(k=\mathbb F_q\) be **any** finite field. Let \(\Gamma\) be the bipartite incidence graph with fifteen vertices indexed by two-element subsets (duads) of \(\{0,1,2,3,4,5\}\), fifteen vertices indexed by partitions of the same six labels into three disjoint duads (synthemes), and an edge whenever a duad belongs to a syntheme. Construct a curve \(C_\Gamma/k\) from thirty three-pointed copies of \(\mathbb P^1\), with rational marks \(0,1,\infty\), by identifying the two marked points belonging to every edge. This is a geometrically connected stable nodal curve of genus \(16\).

The finite-field isomorphism classes of all forms of \(C_\Gamma\) are in bijection with precisely **thirteen** conjugacy classes of \(\operatorname{Aut}(\Gamma)\), a group of order \(1440\). Among those thirteen forms there are precisely **eleven** different Hasse–Weil zeta functions. Exactly **two** forms have no \(k\)-rational points: the forms given by the unique order-five class and the unique order-ten class. Two different pairs of nonisomorphic forms have equal zeta functions over every extension. All claims hold in every characteristic.

For a representative \(g\) of a class let \(v_d(g),e_d(g),b_d(g)\) denote the numbers of length-\(d\) Frobenius orbits, respectively, on the thirty normalization components, forty-five nodes, and ninety branches above the nodes. Then the complete zeta function is
\[
Z(C_g/k,T)=\prod_{d\ge1}\frac{(1-T^d)^{b_d(g)-v_d(g)-e_d(g)}}{(1-q^dT^d)^{v_d(g)}}.
\]
Consequently for every \(n\ge1\),
\[
\#C_g(\mathbb F_{q^n})=(q^n+1)\sum_{d\mid n}d\,v_d(g)+\sum_{d\mid n}d\,e_d(g)-\sum_{d\mid n}d\,b_d(g).
\]

The complete thirteen-class table follows. Orbit entries have the format `orbit length : number of orbits`, not a multiplication or exponent. The class indices are the deterministic indices in `classification.json`.

| Type | Order | Class size | Interchanges sides? | Component-orbit lengths | Node-orbit lengths | Branch-orbit lengths | \(\#C_g(\mathbb F_q)\) |
|---:|---:|---:|:---:|---|---|---|---:|
| 1 | 1 | 1 | no | 1:30 | 1:45 | 1:90 | \(30q-15\) |
| 2 | 2 | 30 | no | 1:10, 2:10 | 1:9, 2:18 | 1:18, 2:36 | \(10q+1\) |
| 3 | 2 | 45 | no | 1:6, 2:12 | 1:5, 2:20 | 1:10, 2:40 | \(6q+1\) |
| 4 | 2 | 36 | yes | 2:15 | 1:5, 2:20 | 2:45 | \(5\) |
| 5 | 3 | 80 | no | 1:3, 3:9 | 3:15 | 3:30 | \(3q+3\) |
| 6 | 4 | 90 | no | 1:2, 2:2, 4:6 | 1:1, 2:2, 4:10 | 1:2, 2:4, 4:20 | \(2q+1\) |
| 7 | 4 | 90 | no | 1:2, 2:2, 4:6 | 1:1, 2:2, 4:10 | 1:2, 2:4, 4:20 | \(2q+1\) |
| 8 | 4 | 180 | yes | 2:3, 4:6 | 1:1, 2:2, 4:10 | 2:5, 4:20 | \(1\) |
| 9 | 5 | 144 | no | 5:6 | 5:9 | 5:18 | \(0\) |
| 10 | 6 | 240 | no | 1:1, 2:1, 3:3, 6:3 | 3:3, 6:6 | 3:6, 6:12 | \(1q+1\) |
| 11 | 8 | 180 | yes | 2:1, 4:1, 8:3 | 1:1, 4:1, 8:5 | 2:1, 4:2, 8:10 | \(1\) |
| 12 | 8 | 180 | yes | 2:1, 4:1, 8:3 | 1:1, 4:1, 8:5 | 2:1, 4:2, 8:10 | \(1\) |
| 13 | 10 | 144 | yes | 10:3 | 5:1, 10:4 | 10:9 | \(0\) |


The two point-free classes have order \(5\) (class index \(9\)) and order \(10\) (class index \(13\)). Their complete zeta functions simplify respectively to
\[
Z(C_5,T)=\frac{(1-T^5)^3}{(1-q^5T^5)^6},\qquad
Z(C_{10},T)=\frac{(1-T^{10})^2}{(1-T^5)(1-q^{10}T^{10})^3}.
\]
The two zeta collisions occur between class indices \(6,7\) and \(11,12\).

## Assumptions and scope

The curve is abstractly constructed by gluing *three-pointed projective lines*, not as a chosen embedding of the Cremona–Richmond configuration in projective three-space. Every component has three distinct rational marked points. All nodes are ordinary. Every finite-field form means an isomorphism class after geometric base change to this particular stable curve; no extra markings are retained on the resulting unmarked stable curve. The graph and all combinatorial group actions are explicitly reconstructed in `verify.py`.

## Proof

**1. Stable geometry and genus.** Each syntheme contains three duads, while each duad occurs in three synthemes: the four leftover labels can be paired in exactly three ways. Thus the incidence graph has \(30\) vertices, \(45\) edges, and is trivalent. It is connected, as verified by the elementary incidence structure and exactly checked by breadth-first traversal in the verifier. Gluing yields a connected projective nodal curve, stable because each rational component has exactly three special points. Normalization gives
\[
p_a(C_\Gamma)=45-30+1=16.
\]

**2. Full automorphisms and descent.** Any automorphism of the stable curve permutes the thirty irreducible components and preserves incidence, hence gives a graph automorphism. An automorphism fixing every component must fix its three incident nodes and is therefore the identity on each projective line. Conversely every graph automorphism lifts uniquely: on each component there is exactly one projective automorphism taking its ordered triple of distinct marks to the ordered triple prescribed by the image halfedges. The lifts are defined over \(k\), and composition agrees with graph composition by uniqueness. Thus \(\operatorname{Aut}(C_{\bar k})\cong\operatorname{Aut}(\Gamma)\) as a constant finite group over any field. Its conjugacy classes classify forms over \(\mathbb F_q\), since the absolute Galois group is procyclic with trivial action on this constant group: a continuous cocycle is specified by a finite-order image \(g\) of Frobenius, modulo conjugation.

**3. Exact finite group calculation.** All graph automorphisms are enumerated by a finite backtracking graph-isomorphism search in `verify.py`. The verifier reconstructs the graph from duads and synthemes, checks \(1440\) distinct graph automorphisms, independently constructs all \(720\) label permutations, supplies and verifies an explicit bipartition-swapping involution, and proves that the resulting \(720+720\) transformations exhaust the graph automorphisms. It then computes the orbit signatures of vertices, edges, and edge-end branches, and conjugacy classes by explicit conjugation \(hgh^{-1}\). The resulting thirteen class sizes total \(1440\), and the signatures in `classification.json` are the full exhaustive output. This is a finite exact computation, not an approximation or probabilistic group search.

**4. Arithmetic zeta and branches.** Let \(\nu:\widetilde C_g\to C_g\) be normalization and let \(B_g\) denote its reduced preimage of the node scheme \(N_g\). Point counting on the finite morphism, including nodes at which Frobenius switches the two branches, yields
\[
\#C_g(\mathbb F_{q^n})=\#\widetilde C_g(\mathbb F_{q^n})+\#N_g(\mathbb F_{q^n})-\#B_g(\mathbb F_{q^n}).
\]
Each degree-\(d\) component orbit descends to a smooth genus-zero curve over \(\mathbb F_{q^d}\); every such curve is a projective line over its finite field (equivalently, \(H^1(\mathbb F_{q^d},\mathrm{PGL}_2)=1\)). It contributes \((1-T^d)^{-1}(1-q^dT^d)^{-1}\) to zeta. The node and branch zero-dimensional zeta factors are the products \((1-T^d)^{-1}\) for their corresponding orbits. Taking zeta quotients proves the displayed formula, with the three distinct orbit inventories essential when an edge is fixed but its two branches are switched.

**5. Completeness and collisions.** Two zeta functions can coincide if and only if the induced expressions agree after cancellation; here the precise data are encoded in the denominator component-orbit signature \(v_d\) and numerator exponent \(b_d-v_d-e_d\). These rational factors cannot cancel across the \((1-q^dT^d)\) factors versus cyclotomic \((1-T^d)\) factors over the indeterminate \(q\). The computed thirteen signatures yield eleven different rational functions, two doubletons and nine singletons. For \(q\ge2\), the point-count polynomial table has exactly two identically zero rows, and all other rows strictly positive; their representative graph automorphisms have orders \(5\) and \(10\). The class table therefore establishes the claimed point-free criterion for every finite field, not only for sampled characteristics or extension degrees.

## Verification

Run `python verify.py` from a directory containing the bundled files and `networkx`. This reconstructs the graph, checks connectivity and degree, enumerates all graph automorphisms, verifies the independent explicit \(S_6\) and outer-involution description, computes all conjugacy classes, creates `classification.json`, and cross-checks each orbit expression against the zeta log derivative through extension degree \(24\). The finite verification is exhaustive for the graph and automorphism group, while the infinite assertions follow from the normalization and descent arguments above. `verification_output.txt` records the successful command output, and `classification.json` contains all orbit and class certificates, including explicit representative permutations.

## Relationship to prior work

The Cremona–Richmond incidence geometry, its duad/syntheme description, and its \(S_6\) symmetry predate this calculation; Prażmowska and Prażmowski study these configurations and the automorphisms preserving the point/line bipartition. The geometry of nodal stable curves and their graph-theoretic generalized Jacobians is also established: Casalaina-Martin, Kass, and Viviani describe graph-dependent local compactified Jacobian geometry. Here the evaluated contribution is the unmarked stable *curve* associated to this particular incidence graph, its full bipartition-swapping automorphism descent, the exhaustive thirteen finite-field forms, eleven zeta types, and two point-free types. General normalization identities are used, not presented as new. The previously studied arithmetic Igusa fifteen-line boundary has different geometric components and singularities, despite its related \(S_6\) combinatorics.

## Limitations

This does not classify all stable curves of genus \(16\) or all stable curves with thirty components. It concerns only the unmarked stable curve with the specified dual graph, not the embedded Cremona–Richmond configuration or the Igusa quartic. The classification is over finite fields; over other base fields the Galois cohomology is different. The calculation establishes complete Hasse–Weil zeta functions and does not claim a complete integral classification of the generalized Jacobian tori. The finite checks use installed `networkx`; an independent proof of the graph automorphism count may alternatively use generalized-quadrangle theory. Mathematical priority remains provisional against unexamined historical treatments of graph-curve twists.

## References

1. M. Prażmowska and K. Prażmowski, *The Cremona–Richmond Configuration revisited and generalized*, arXiv:1404.7166v1 (first submitted 2014-04-28), especially Sec. 1 and Sec. 1.1, https://arxiv.org/abs/1404.7166.
2. S. Casalaina-Martin, J. L. Kass, and F. Viviani, *The Local Structure of Compactified Jacobians*, arXiv:1107.4166v1 (first submitted 2011-07-21), especially Introduction and Sec. 3, https://arxiv.org/abs/1107.4166.
