# Two windmill components in the Pappus graph three-edge-coloring interchange graph

## Finding

Let \(P\) be the eighteen-vertex Pappus graph specified below. Form \(\mathcal K(P)\) with one vertex per proper three-edge-coloring modulo global permutations of the three colors. Two distinct vertices are adjacent if one coloring can be changed to the other by interchanging two colors on exactly one connected two-colored cycle and then renaming colors globally. The complete graph is
\[
\boxed{\mathcal K(P)\cong 2\bigl(K_1\vee(3K_3)\bigr).}
\]
Thus there are exactly twenty configurations and thirty-six exchange edges, arranged as two components of ten configurations each. Within either component, one universal vertex is joined to three mutually nonadjacent triangles. Its center has degree nine; every other vertex has degree three. Both components have diameter two. In every center coloring, each two-color spanning subgraph has cycle profile \((6,6,6)\). In each peripheral coloring, precisely one of the three color pairs has profile \((6,6,6)\), and the other two have profile \((18)\).

## Assumptions and scope

The vertex set is \(\mathbb Z/18\mathbb Z\). Include the eighteen cycle edges \(\{i,i+1\}\), with indices reduced modulo eighteen, and the nine additional chords \(\{i,i+s_i\}\), where the shifts repeat \((5,7,-7,7,-7,-5)\) three times. Taking undirected edges gives a simple cubic graph with eighteen vertices and twenty-seven edges, a standard labeled realization of the Pappus graph. Every proper three-edge-coloring partitions these twenty-seven edges into three perfect matchings. Colorings differing only by a global renaming of colors are identified. Only switches on one entire connected alternating cycle are allowed; the empty operation and a switch that induces only a global color permutation do not generate edges. Vertices of \(P\) are labeled and are **not** identified under graph automorphisms.

## Proof

The exhaustive finite argument has four logically complete stages, recorded independently in `verify_matchings.py`, `verify_colorings.py`, and the explicit `classification_certificate.json`.

**1. Matchings and canonical representatives.** Every perfect matching is found recursively: take the smallest unmatched graph vertex, select each incident edge joining it to an unmatched neighbor in turn, and recurse on the remaining vertices. Every perfect matching contains exactly one such incident edge, so the branches are disjoint and exhaustive. This gives exactly forty-two distinct perfect matchings. For each disjoint ordered pair of those matchings, its edge-complement is forced to be the third class; retain the triple exactly when the complement is itself a perfect matching. This procedure enumerates *all* proper three-edge-colorings, because every color class in a cubic graph is a perfect matching. Normalize each triple by demanding that the three edges at graph vertex zero receive colors zero, one, and two in the fixed sorted incident-edge order; this removes precisely the six permutations of the color names. The resulting twenty canonical edge-color vectors exhaust the vertex set of \(\mathcal K(P)\).

**2. Complete adjacency.** Given a canonical coloring and one unordered pair of colors, those two color classes form a spanning two-regular graph, hence are a disjoint union of even cycles. Traversing connected components enumerates every permissible Kempe cycle, with no missed switch. Reverse the two colors on that component, normalize again at vertex zero, and record an edge if the canonical coloring changes. The resulting full twenty-row adjacency relation is included in the certificate, indexed by its complete canonical twenty-vector list. It has thirty-six unordered edges. All row pairs are checked symmetric and complete by the enumerating program.

**3. Exact component structure.** Breadth-first traversal of those explicitly enumerated adjacency rows produces precisely two blocks, of ten vertices each. Each block contains exactly one vertex adjacent to the other nine. Delete that vertex: all nine remaining vertices have degree two in the induced subgraph and partition into three disconnected triangles. Therefore each block is \(K_1\vee(3K_3)\), establishing the graph isomorphism (and hence all claimed numerical invariants). Direct inspection of all three two-color cycle decompositions for all twenty canonical vectors produces exactly two signatures \(((6,6,6),(6,6,6),(6,6,6))\) and eighteen signatures \(((6,6,6),(18),(18))\); the two former vectors are exactly the component centers.

**4. Independent enumeration.** A distinct verifier starts from the twenty-seven graph edges, fixes the three colors at vertex zero, and enumerates assignments to the other twenty-four edges by a direct recursive proper-coloring backtrack. It finds twenty colorings independently of the perfect-matching list. For every color pair, it separately computes connected alternating-cycle vertex sets, flips all their edges, normalizes, and builds adjacency. Both verifiers produce the same canonical twenty-vertex/twenty-seven-coordinate coloring list and thirty-six-edge set. The SHA-256 digest of their common deterministic compact JSON serialization is `56ffa0b44d5b539ae41cc4056f5b6ca8821b12eaae1cad70608a02a36680ada6`.

Both searches are exhaustive over finite stated objects; no extrapolation from small examples or sampling is used.

## Verification

Use Python 3 and only its standard library. Run `python3 verify_matchings.py --certificate` and `python3 verify_colorings.py` in the directory containing these files. The first command writes `classification_certificate.json`, exposing the graph's entire edge set, every canonical color vector, all twenty adjacency lists, all three two-color profiles per vector, both component lists, and their digest. The independent second command reconstructs the same graph without using the matchings algorithm or its certificate. Compare their printed common graph digests and compare the generated certificate with the packaged certificate. Exact replayed output is in `matching_run.txt` and `coloring_run.txt`.

## Relationship to prior work

Belcastro and Haas (2012) introduced systematic counting of edge-Kempe-equivalence classes of cubic three-edge-colorings. Their 2017 treatment studies the entire edge-Kempe-equivalence graph, with all color names distinguished, and its vertex-fixed version, as well as structural theorems and crossed-prism examples. The present graph is the **full global-color-permutation quotient**, which can have triangles even though the all-named-colorings graph in their Proposition 2.1 does not. Their vertex-fixed version has the same configurations but can have fewer edges, because it omits switches involving the chosen root vertex. Their results do not explicitly classify the Pappus full quotient. Goedgebeur and Östergård (2021), especially their algorithm and aggregate Tables 1–4, enumerate **numbers of** Kempe equivalence classes of cubic graphs and cover corresponding finite-order connectivity computations in principle; their algorithm suppresses root-cycle moves, which preserves component counts but does not necessarily preserve the entire color-permutation-quotient adjacency. The present claim is instead the *entire Pappus-specific twenty-vertex transition graph*, including its two windmill components and the exact three-bichromatic-cycle characterization of its two centers. No novelty is asserted for the definition of Kempe changes or for computational enumeration of Kempe class counts in general.

## Limitations

The result holds for exactly the indicated eighteen-vertex graph, with labels retained and only global **color** permutations factored out. It does not assert anything for arbitrary cubic graphs, graph-automorphism quotients, or the all-named-colorings switch graph. The classification is a fully replayable finite exhaustive proof, not a general structural derivation. Earlier finite computational databases might permit reconstruction of some of these data; no claim of absolute publication priority is made. Independent external audit has not been carried out.

## References

1. S.-M. belcastro and R. Haas, *Counting edge-Kempe-equivalence classes for 3-edge-colored cubic graphs*, arXiv:1209.1730 (first public posting 8 September 2012), https://arxiv.org/abs/1209.1730 .
2. S.-M. belcastro and R. Haas, *Edge-Kempe-equivalence graphs of class-1 regular graphs*, Australasian Journal of Combinatorics 69(2) (2017), 197–214, https://ajc.maths.uq.edu.au/pdf/69/ajc_v69_p197.pdf .
3. J. Goedgebeur and P. R. J. Östergård, *Switching 3-edge-colorings of cubic graphs*, arXiv:2105.01363 (2021), https://arxiv.org/abs/2105.01363 .
