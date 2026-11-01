# The Petersen forest filtration has a homotopy plateau and a six-sphere transition

## Finding

For the Petersen graph \(P=\operatorname{KG}(5,2)\), the vertex-induced forest filtration has the following integral homotopy types:
\[
\mathcal F_d(P)\simeq
\begin{cases}
\bigvee^4 S^2,&d=0,\\
S^3,&d=1,2,\\
\bigvee^6 S^5,&d\geq3.
\end{cases}
\]
In addition, the **actual inclusion** \(\mathcal F_1(P)\hookrightarrow\mathcal F_2(P)\) is a homotopy equivalence; this is stronger than equality of their Betti numbers or abstract homotopy types. Accordingly, the reduced integral persistent homology consists of four degree-two intervals \([0,1)\), one degree-three interval \([1,3)\), and six degree-five intervals \([3,\infty)\), with no others. The pure five-dimensional complex \(\mathcal F_2(P)\) is nonshellable.

The value of the result is the complete homotopy and inclusion classification for a natural symmetric, noncactus cubic graph at all admissible degree bounds. The stages \(d=0,1\) are included for context and are not presented as new standalone calculations.

## Assumptions and scope

Write \([5]=\{0,1,2,3,4\}\). The ten vertices of \(P\) are the lexicographically ordered unordered pairs of elements of \([5]\). Distinct vertices \(u,v\) are adjacent exactly when the corresponding pairs are disjoint. This defines a cubic graph on ten vertices and fifteen edges. For an integer \(d\geq0\), a set \(S\subseteq V(P)\) is a simplex of \(\mathcal F_d(P)\) exactly when the induced graph \(P[S]\) is a forest and its maximum degree is at most \(d\). The empty face is included. Because \(P\) is cubic, \(\mathcal F_d(P)=\mathcal F_3(P)\) for every \(d\geq3\).

This is the *vertex-induced* forest filtration. It is not the usual graphic-matroid complex of edge forests; nor is \(\mathcal F_2\) a component-size-bounded higher-independence complex. In particular \(\mathcal F_1(P)=\operatorname{Ind}_2(P)\), whereas \(\operatorname{Ind}_3(P)\) is a proper subcomplex of \(\mathcal F_2(P)\): their total face counts are respectively \(381\) and \(621\), including the empty face.

## Proof

**Finite, exhaustive construction.** Associate to each subset \(S\) its integer bitmask from \(0\) through \(2^{10}-1\). The standalone verifier constructs all fifteen graph edges directly from disjointness of the corresponding two-subsets. It tests the degree bound and acyclicity once by union-find, and independently by degree counts and the identity \(|E(P[S])|=|S|-c(P[S])\), with components found by depth-first search. Every mask agrees between the two tests. The face counts, including the empty face, are \(76,261,621,786\) for bounds \(0,1,2,3\), respectively.

**Integral homotopy certificates.** On the nonempty face poset use the following deterministic repeated-toggle matching. Fix an order of the graph vertices. At each vertex, visit currently unmatched faces in order of cardinality and then integer mask; pair an unmatched face not containing the vertex with its unmatched single-vertex extension when both exist. At bound \(2\) use reverse vertex order, and at bounds \(0,1,3\) use forward order. Acyclicity is checked, not presumed: orient every cover incidence downward except that matched incidences point upward, and topologically sort the entire directed Hasse graph.

The numbers of matched pairs for bounds \(0,1,2,3\) are \(35,129,309,389\), and the numbers of oriented Hasse incidences checked are \(170,860,2540,3470\). All four complete directed graphs are acyclic. Their critical cells are, respectively, one zero-cell and four two-cells; one zero-cell and one three-cell; one zero-cell and one three-cell; and one zero-cell and six five-cells. Forman's discrete Morse theorem supplies a homotopy-equivalent CW complex with exactly these cells. Since all positive-dimensional cells are attached to the single zero-cell, these CW complexes are the stated wedges of spheres. This is an integral homotopy argument, not a deduction from field-valued Betti numbers.

**The actual inclusion.** Consider the relative cellular chain complex \(C_*(\mathcal F_2(P),\mathcal F_1(P);\mathbb Z)\) supported on the \(360\) faces present in the former but not the latter. Apply the same forward-order toggle matching, only pairing faces within this relative set. It has \(179\) matched pairs and precisely two critical cells, represented by bitmasks \(538\) in degree three and \(914\) in degree four. All \(960\) relative Hasse incidences are checked for acyclicity. Starting from oriented simplicial incidence coefficients \((-1)^j\) for deletion of the \(j\)-th occupied vertex, eliminate every matched pair using exact integer unit-pivot chain cancellation. The surviving differential is the one-by-one matrix \((-1)\). Thus every relative integral homology group vanishes. Both \(\mathcal F_1(P)\) and \(\mathcal F_2(P)\) are simply connected CW complexes of homotopy type \(S^3\). The long exact sequence of the pair and Whitehead's theorem therefore prove that the inclusion is a homotopy equivalence.

**Persistent groups and shellability.** The only nonzero reduced integral groups at the four distinct stages are \(\mathbb Z^4\) in degree two at bound zero; \(\mathbb Z\) in degree three at bounds one and two; and \(\mathbb Z^6\) in degree five from bound three onward. The map from bound one to two is an isomorphism, and every other interstage map between nonzero groups has incompatible degree. This determines the asserted integral interval decomposition. All \(65\) facets of \(\mathcal F_2(P)\) have dimension five, yet its reduced \(H_3\) is nonzero. A pure shellable complex has reduced homology only in its top dimension, so this complex is not shellable.

## Verification

Run `python3 verify_petersen_forest.py` with Python 3 and its standard library. The program independently reconstructs both face enumerations, checks graph degree and strongly regular common-neighbor counts, reconstructs the actual matchings, verifies acyclicity for every nonempty Hasse incidence, performs signed integral cancellations, and computes independent mod-two simplicial boundary ranks. Its output is reproduced in `verification_output.json`. The required success string is `PETERSEN_FOREST_FILTRATION_EXACT_INTEGRAL_MORSE_OK`.

The complete face counts by dimension (starting with the empty face) are: bound zero \((1,10,30,30,5)\), bound one \((1,10,45,90,80,30,5)\), bound two \((1,10,45,120,200,180,65)\), and bound three \((1,10,45,120,210,240,140,20)\). Exact integral cancellation and an independent mod-two rank computation corroborate the homotopy classifications. The bound-two relative critical differential is \((-1)\); no modular calculation is used to infer that integral unit.

## Relationship to prior work

Carnero Bravo introduced the vertex-induced forest filtration and computed it for paths, cycles, double stars, cactus graphs, certain graph joins, complete multipartite graphs and several graph products [1]. The Petersen graph is not among these families as treated in the paper, and the exact degree-two stage, degree-three transition and inclusion certificate are not consequences of its stated family classifications. The relevant introduction and computational sections of the full paper were inspected.

Existing higher-independence-complex theory [2] concerns restrictions on induced *component size*. At the first cutoff it agrees with the forest filtration, but its next stages are different: \(\operatorname{Ind}_3(P)\) has \(240\) fewer faces than \(\mathcal F_2(P)\). A previous calculation that the induced-component cutoff-two stage has type \(S^3\), or that its inclusion into the cutoff-three stage is an equivalence, does not imply the new result for arbitrary induced linear forests or the terminal forest complex.

## Limitations

The classification concerns exactly \(\operatorname{KG}(5,2)\), not other Kneser graphs or a family of cubic graphs. It gives ordinary nonequivariant homotopy types and integral persistence, not the action of the automorphism group on homology. An independent external audit has not been performed. Published-literature coverage cannot rule out an equivalent calculation in unindexed literature.

## References

[1] Andrés Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271 (first public version July 25, 2023; full text latest revision March 12, 2025), https://arxiv.org/abs/2307.13271 .

[2] Fred M. Abdelmalek, Priyavrat Deshpande, Shuchita Goyal, Amit Roy and Anurag Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863, https://arxiv.org/abs/2106.10863 .

[3] Robin Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
