# The sharp eight-vertex threshold for rooted tournament orbit refinement

## Finding

Let \(T\) be a finite nonempty *tournament*: between each two distinct vertices exactly one directed arc is present. Distinguish one root \(r\) by a singleton initial colour, and assign all other vertices the same initial colour. Perform synchronous one-dimensional *directed counting colour refinement*, replacing each colour by its previous colour together with the multiplicities of the previous colours in its outgoing and incoming neighbourhoods.

**Theorem.** For every rooted tournament \((T,r)\) with \(|V(T)|\leq 7\), the stable colour classes are exactly the automorphism orbits of \(T\) under automorphisms fixing \(r\). At \(|V(T)|=8\) there are **exactly two rooted isomorphism types** for which this property fails. Both consist of the same seven-vertex regular tournament \(R\), together with a uniquely marked eighth vertex that either beats every vertex of \(R\), or loses to every vertex of \(R\).

One explicit presentation of \(R\) on vertices \(0,1,2,3,4,5,6\) is the following outgoing-neighbour list (each unordered vertex pair occurs in one direction):

```text
0: 2 5 6
1: 0 5 6
2: 1 4 6
3: 0 1 2
4: 0 1 3
5: 2 3 4
6: 3 4 5
```

In both exceptional rooted tournaments the stable colour classes have sizes \(1\) and \(7\), while the rooted automorphism orbits have sizes \(1,1,3,3\). In particular, the seven vertices other than the root stay monochromatic but are not one orbit. The rooted automorphism group has order \(3\).

## Assumptions and scope

All tournaments are finite, loopless, and have exactly one of the two possible arcs between each distinct pair. Isomorphisms and automorphisms preserve arc directions. A *rooted* isomorphism sends the distinguished root to the distinguished root; roots are part of the input, not subsequently selected by an invariant. Refinement keeps the old colour as part of every new signature and distinguishes outgoing from incoming arcs. The theorem concerns exactly the orders \(1\) through \(8\), with no classification asserted at higher orders.

For a colour class \(C\) and a vertex \(v\), the incoming count is \(|C|-\operatorname{out}_C(v)-\mathbf 1_{v\in C}\). Thus the exhaustive code's old-colour/outgoing-count signatures are mathematically equivalent to the specified full directed signatures.

## Proof

**Exhaustive reduction lemma.** Let \(\mathcal U_s\) be a list of one representative of each isomorphism type of tournament on \(s\) vertices. All rooted tournaments on \(s+1\) vertices are obtained, up to rooted isomorphism, by adjoining a distinguished new vertex to a member of \(\mathcal U_s\) with an arbitrary orientation for each of the \(s\) incident arcs. Indeed, deleting the root gives a tournament isomorphic to an entry of \(\mathcal U_s\), and transporting all root incidences along that isomorphism gives the stated extension. Every possible incidence pattern is one of the \(2^s\) binary masks tested by `cpp/rooted_tournament_census.cpp`.

**Canonical-representative lemma.** The program builds \(\mathcal U_s\) inductively. To canonize a tournament, it first arranges vertices in nondecreasing outdegree and then takes the lexicographically least upper-triangle orientation bit string over all permutations *within each equal-outdegree block*. This is an exact isomorphism invariant: every isomorphism preserves outdegree, and if two such canonical bit strings coincide the corresponding vertex permutations give an isomorphism. Hence deleting repeated canonical strings leaves exactly one representative per unrooted isomorphism class. The computed numbers of representatives through order seven are, respectively, \(1,1,2,4,12,56,456\) (orders one through seven). These match the independently published tournament counts in McKay's catalogue.

**Refinement and orbit lemma.** For each extension, the program iterates colour signatures until equality of consecutive partitions. Its test for stabilization compares equality relations, not numerical colour labels. It then enumerates all possible colour-preserving automorphisms by backtracking over partial bijections consistent with every oriented edge. Every automorphism must preserve every refinement colour, so restricting the search to stable colour cells omits none. Conversely every completed, arc-preserving bijection is an automorphism. The union of image pairs under these bijections is therefore *exactly* the rooted automorphism-orbit relation. It follows that the test reports a failure if and only if some stable colour cell meets at least two distinct rooted orbits.

**Finite complete enumeration.** For orders \(2,3,4,5,6,7,8\), the extension counts are \(2,4,16,64,384,3584,58368\), respectively. The corresponding numbers of failures among these (potentially redundant) extensions are \(0,0,0,0,0,0,2\). For the eight-vertex cases, rooted canonicalization (the root is fixed, and remaining vertices may be relabelled within outdegree classes) gives two distinct canonical orientation integers, `85042` and `220421234`, when bits are ordered \((0,1),(0,2),\ldots,(0,7),(1,2),\ldots,(6,7)\) and 1 means the lower-index vertex beats the higher-index vertex. The two words restrict to the same seven-vertex word `22066`; the eighth vertex has outdegree \(7\) in the first and \(0\) in the second. This proves both completeness and inequivalence of the two exceptions. The trivial one-vertex case has a single orbit and colour.

**Direct explanation of the exceptions.** Every vertex of the displayed seven-vertex tournament \(R\) beats exactly three others in \(R\). The unique root either beats all seven vertices or loses to all seven, so all vertices of \(R\) have identical root-directed counts and identical within-\(R\) out- and indegrees. The initial two-colour partition is already equitable and never splits. Exact enumeration of the automorphisms of \(R\), independently reproduced by `python/witness_crosscheck.py`, gives three orbits of sizes \(1,3,3\) on \(R\), with group order \(3\). Adding a unique source or sink as root does not change these orbits. The two stable colour cells therefore strictly coarsen the rooted orbit partition in exactly the stated way.

## Verification

Three embedded standalone programs provide two distinct exhaustive strategies and a separate witness calculation. `cpp/rooted_tournament_census.cpp` performs isomorphism-class augmentation and complete rooted orbit comparisons through eight vertices. `cpp/independent_labelled_check.cpp` independently tests **every labelled orientation** with the root fixed at vertex zero through seven vertices, including all \(2^{21}=2,097,152\) cases at order seven; no failure appears. `python/witness_crosscheck.py` independently recomputes the arcs, stable directed colours, and all root-preserving automorphisms of both exceptional rooted tournaments without dependencies beyond the Python standard library. Every program was executed from the indicated package paths and its exact output is embedded under `evidence/`; commands and output expectations appear in `README.md` and `VERIFICATION.md`.

These are exhaustive finite proofs of the stated finite bound: their validity depends on the explicitly justified search-space coverage and on the inspectable exact algorithms, not on extrapolating a sample. The independent labelled computation verifies the seven-vertex lower bound using a different enumeration route. No higher-order case follows merely from these calculations.

## Relationship to prior work

Arvind, Köbler, Rattan and Verbitsky (2015), *Graph Isomorphism, Color Refinement, and Compactness*, formalize refinability as equality of a colour-refinement partition and an automorphism-orbit partition and develop general structural and complexity results. Arvind, Fuhlbrück, Köbler, Kuhnert and Rattan (2016), *The Parameterized Complexity of Fixing Number and Vertex Individualization in Graphs*, motivate individualization followed by refinement. Both papers treat graph-theoretic frameworks rather than the present complete pointed-tournament census; neither states the two eight-vertex tournaments or the sharp threshold. The direction-sensitive signature used here is the natural tournament analogue of the general framework.

McKay's publicly available tournament census lists \(456\) nonisomorphic tournaments of order seven, including three regular types. Those known enumeration totals alone do not say which rooted tournaments fail orbit-exact refinement, nor identify the precise two first rooted obstructions. The present classification therefore adds a distinct invariant and a complete minimal layer rather than recomputing only the known tournament counts. Existing results on general coloured-graph refinability are not automatically equivalent to a classification within rooted tournaments.

## Limitations

The theorem concerns directed tournaments with a single fixed root and colours that separately count incoming and outgoing arcs. It does not assert the analogous result for symmetric graphs, for unrooted tournaments, for two independently marked vertices, or beyond eight vertices. The uniqueness assertion is a finite computer-assisted exhaustive proof; its reproducibility requires a C++17 compiler and Python 3, and it has not been independently formally verified. The inspected literature did not reveal exact covering work, but a specialized prior result could exist. Publication priority and independent scientific audit remain unverified.

## References

1. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first posted 2015-02-04. https://arxiv.org/abs/1502.01255
2. V. Arvind, F. Fuhlbrück, J. Köbler, S. Kuhnert, G. Rattan, *The Parameterized Complexity of Fixing Number and Vertex Individualization in Graphs*, arXiv:1606.04383, first posted 2016-06-14. https://arxiv.org/abs/1606.04383
3. B. D. McKay, *Combinatorial Data: Digraphs / Tournaments*, publicly available exact isomorphism-type tables, consulted for enumeration comparison; catalogue posting date not established. https://users.cecs.anu.edu.au/~bdm/data/digraphs.html
