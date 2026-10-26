# Two recolouring chambers of the Grötzsch graph

## Finding

Let \(G=\mu(C_5)\) be the eleven-vertex Grötzsch graph, with the standard four named colours \(\{0,1,2,3\}\). A *recolouring* changes the colour of exactly one vertex and keeps the colouring proper. Let \(\mathcal R_4(G)\) be the graph of all proper four-colourings with these recolouring edges.

The recolouring graph has exactly \(12,480\) vertices, \(45,240\) edges and **exactly two connected components**. Both components have \(6,240\) vertices and diameter exactly \(17\). Their common degree distribution is
\[
\begin{array}{c|rrrrr}
\text{degree}&5&6&7&8&9\\\hline
\text{multiplicity in either component}&240&1320&1920&2160&600.
\end{array}
\]

The components are exchanged by **every odd permutation of the named palette** and by **every reflection** of the underlying five-cycle. Every even palette permutation and every rotation of the cycle preserves both components. Consequently the two components are isomorphic, no proper four-colouring is frozen, and the recolouring graph modulo global colour renaming is connected. Together with the known degeneracy mixing bound, the exact ordinary mixing number and mixing threshold of \(G\) are both \(5\).

These are assertions about the single, naturally distinguished eleven-vertex graph; no larger Mycielski-graph family is claimed. The count \(12,480\) of four-colourings itself is previously available in the literature and is **not** asserted to be new. The contribution here is the *complete recolouring-component classification*, including palette handedness, spectra and diameter.

## Assumptions and scope

All graphs are finite and simple. The graph is specified without relying on a library convention: write \(v_i\), \(u_i\) for \(i\in\mathbb Z/5\mathbb Z\) and one apex \(w\). For every \(i\), include exactly the edges \(v_iv_{i+1}\), \(v_iu_{i+1}\), \(u_iv_{i+1}\), and \(u_iw\). Thus there are eleven vertices and twenty edges. The colour set is precisely the four distinct symbols \(0,1,2,3\), and all colourings are labelled maps \(V(G)\to\{0,1,2,3\}\). Because \(G\) is four-chromatic, every proper such map uses all four colours.

Global permutations of the four named colours act on \(\mathcal R_4(G)\). A rotation sends \(v_i\) to \(v_{i+s}\) and \(u_i\) to \(u_{i+s}\), fixing \(w\); a reflection sends them to \(v_{-i+s}\) and \(u_{-i+s}\) and also fixes \(w\). These graph automorphisms act on colourings by precomposition.

Two concrete four-colourings, written in the vertex order \((v_0,\ldots,v_4,u_0,\ldots,u_4,w)\), are
\[
(0,1,0,1,2,0,1,0,1,2,3),\qquad
(0,1,0,1,2,0,1,0,1,3,2).
\]
Both are proper and lie in different recolouring components.

## Proof

This is a **finite exhaustive proof** of the exact recolouring statement. The accompanying standalone source file `verify.cpp` implements the complete finite universe and verifies each of the following steps using integer operations. The checks below rely on its inspected control flow and the successful replay, not on uninspected program output or sample-based inference.

**Enumeration lemma.** Encode a colouring as an eleven-digit base-four integer. Integers from \(0\) through \(4^{11}-1=4,194,303\) enumerate each named colouring exactly once. A colouring is proper if and only if the colours at the endpoints of each of the twenty explicitly constructed edges differ. The verifier checks the predicate over all \(4,194,304\) assignments and finds exactly \(12,480\) valid. A second, recursive partial-colouring search generates \(12,480\) states, each valid by the same edge condition and with a distinct base-four index; its complete recursive branching establishes that these are all proper assignments.

**Exchange lemma.** For each generated valid state \(c\), each of its eleven vertices and each of the three other palette colours is tested. The resulting state is made an edge precisely if it is proper. Every pair of proper states differing in one vertex is encountered, and no other pair is admitted. The program verifies that every constructed directed transition has its reverse. Dividing the directed-transition count by two yields \(45,240\) undirected edges, and the global degree histogram is \(480,2640,3840,4320,1200\) at degrees \(5,6,7,8,9\) respectively.

**Component and distance lemma.** Standard breadth-first search from each as-yet-unseen state visits exactly its whole connected component: every one-step neighbour is traversed, and no non-neighbour is. This yields two components, of sizes \(6,240\) and \(6,240\). For every vertex \(c\) of each component, a separate exhaustive breadth-first search computes the exact length of the shortest path to every state in that component (and verifies that precisely all \(6,240\) are reached). Taking the maximum over all starting vertices and all reachable targets gives diameter \(17\) in each component. Counting neighbour lists within the components gives the degree distribution displayed above.

**Symmetry lemma.** Permuting colour names, or applying any automorphism of \(G\), sends proper four-colourings to proper four-colourings and preserves the property of differing in exactly one vertex. Hence these operations are automorphisms of the recolouring graph, necessarily permuting its connected components. The verifier checks all \(24\) palette permutations and all ten dihedral automorphisms on a representative of one component. An odd palette permutation sends this representative into the other component; an even permutation stays in its component. All five rotations preserve it and all five reflections switch it. Because these maps are automorphisms and the components are connected, their actions on the single representative determine their actions on the entire component. In particular an odd palette permutation is an explicit isomorphism between the two components, and all odd colour permutations exchange them. The program checks the two displayed concrete colourings as a further separate component witness.

**Mixing corollary.** The known Mycielski construction yields \(\chi(G)=4\). The graph has degeneracy exactly \(3\): the original eleven-vertex graph has minimum degree \(3\), while every subgraph with minimum degree at least \(4\) would have to omit all five degree-three shadow vertices; what remains is a five-cycle together with an isolated apex, so such a subgraph is impossible. The connectedness theorem of Cereceda, van den Heuvel and Johnson states that a graph of degeneracy \(d\) is \(k\)-mixing for every integer \(k\ge d+2\). Hence all \(k\ge5\) are mixing. Since \(\mathcal R_4(G)\) has two components, \(4\) is not mixing. Both the least mixing number and the eventual mixing threshold are therefore \(5\).

## Verification

Compile the self-contained accompanying C++17 file with assertions enabled, for example:

```sh
g++ -std=c++17 -O2 verify.cpp -o verify
./verify
```

The source uses no external graph libraries, files, network or randomized routines. It outputs these terminal markers after completing the stated checks:

```text
EXHAUSTIVE_UNIVERSE_OK 4194304 assignments, proper=12480
RECOLOR_GRAPH_OK vertices=12480 edges=45240 degrees 5:480 6:2640 7:3840 8:4320 9:1200
COMPONENTS_OK sizes=6240,6240
COMPONENT_DETAIL_OK component=0 diameter=17
COMPONENT_DETAIL_OK component=1 diameter=17
SYMMETRY_OK odd_color_permutations_and_reflections_swap_components
VERIFY_OK
```

The enumeration and all-pairs breadth-first-search steps are exhaustive for the single eleven-vertex graph and prove the finite assertions when their implementation is inspected and executed. They do **not** establish an analogous result for larger Mycielski graphs.

## Relationship to prior work

Cereceda, van den Heuvel and Johnson introduced the graph of single-vertex recolourings and proved the degeneracy-based connectivity theorem used only in the mixing corollary. Brewster and Noel developed the general homomorphism recolouring and mixing framework. Their general statements do not imply the number, diameter or palette-parity action of the specific Grötzsch recolouring components. The widely reported total of \(12,480\) proper four-colourings is prior numerical information; it does not determine adjacency or connected components. Collins and Tysdal study dependent edges of acyclic orientations in Mycielski graphs, a different mathematical property; only its abstract was accessible, so a remote possibility of additional relevant discussion is retained as a literature risk.

The precise new statement is the two-chamber decomposition, exact component degree and distance invariants, and the parity/reflection exchange law, not the existence or chromatic number of the Grötzsch graph or the general mixing bound.

## Limitations

A finite exhaustive proof is sensitive to implementation errors; the full universe scan, separate recursive enumeration, adjacency-symmetry checks, component exploration from all states, and a saved-source replay reduce but do not eliminate that risk. The proof is not a symbolic family classification. An equivalent description under graph-homomorphism, Glauber-state-space or chromatic-partition terminology might exist in unindexed literature.

## References

1. L. Cereceda, J. van den Heuvel, M. Johnson, *Connectedness of the Graph of Vertex-Colourings*, LSE-CDAM-2005-11 (July 2005), especially Theorem 3. https://matthewjohnsondurham.github.io/papers/cdam-2005-11.pdf
2. R. C. Brewster, J. A. Noel, *Mixing Homomorphisms, Recolourings, and Extending Circular Precolourings*, arXiv:1412.3493, originally submitted 2014-12-10. https://arxiv.org/abs/1412.3493
3. *No triangle, and four colours*, Matpic, section “Eleven vertices, no triangle, four colours” (previously recorded proper-colouring count). https://www.matpic.com/essays/no-triangle-and-four-colours/
4. K. L. Collins, K. Tysdal, *Dependent edges in Mycielski graphs and 4-colorings of 4-skeletons*, J. Graph Theory 46 (2004), 285–296; abstract inspected. https://doi.org/10.1002/jgt.20007
