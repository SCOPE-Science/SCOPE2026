# Dodecahedral majority dynamics: an exact recurrent, basin and symmetry census

## Finding

For synchronous binary majority voting on the labelled dodecahedral graph \(D\), there are exactly **118 fixed configurations and 9,679 primitive two-cycle temporal orbits**. There are no other recurrent periods. The global update satisfies
\[
F^{9}=F^{7},
\]
so all configurations first enter a periodic orbit by step seven, and this bound is attained. The total fixed-point and two-cycle basin populations are **188,128** and **860,448**. Under the full 120-element spatial automorphism group, with temporal phase shifts identified for two-cycles, there are exactly **nine** fixed-point geometric classes and **145** two-cycle geometric classes.

The exact first-periodic-entry census is:

| Entry time \(t\) | Eventual fixed point | Eventual two-cycle | Total |
| --- | ---: | ---: | ---: |
| 0 | 118 | 19,358 | 19,476 |
| 1 | 4,710 | 351,490 | 356,200 |
| 2 | 14,700 | 344,880 | 359,580 |
| 3 | 27,320 | 105,000 | 132,320 |
| 4 | 61,600 | 33,960 | 95,560 |
| 5 | 60,960 | 5,760 | 66,720 |
| 6 | 15,840 | 0 | 15,840 |
| 7 | 2,880 | 0 | 2,880 |
| **Total** | **188,128** | **860,448** | **1,048,576** |

All configurations that approach two-cycles enter them by step five; the only configurations requiring six or seven steps approach fixed points.

The 118 fixed configurations are exactly the labelled binary colorings for which the set of bichromatic edges is a matching; hence there are **59** fixed colorings up to global complementation.

## Assumptions and scope

The graph is the 20-vertex, 30-edge 3-regular dodecahedral graph, isomorphic to the generalized Petersen graph \(GP(10,2)\). Its labelled adjacency list (vertex labels 0 through 19) is specified as a 20-by-3 integer array in `dodeca_majority.cpp`. These labels are **fixed** when counting temporal orbits: no graph symmetries identify states until the separate geometric classification. A configuration is a bit vector \(x=(x_0,\ldots,x_{19})\). The update rule is
\[
F(x)_v=1\quad\Longleftrightarrow\quad \sum_{u\sim v} x_u\ge2.
\]
All updates are simultaneous. A temporal cycle of least length \(d\) is counted once under shifts in time; a geometric class additionally identifies the action of the full graph automorphism group. A state's first-entry time is the least \(t\ge0\) for which \(F^t(x)\) lies on a periodic orbit. The basin of a periodic orbit includes all starting states that eventually visit that orbit.

## Proof

The graph identity itself is witnessed by an explicit vertex bijection to the usual generalized Petersen definition in `gp10_2_isomorphism.tsv`; `verify_graph_identity.cpp` checks all 400 ordered vertex pairs for edge/nonedge preservation.

**1. Exhaustive finite reduction.** There are precisely \(2^{20}=1{,}048{,}576\) labelled starting configurations. Encode them as unsigned integers \(0\le x<2^{20}\). `dodeca_majority.cpp` implements the displayed local rule by summing the three neighbor bits. It computes the successor of each possible integer, writing all 1,048,576 successors in little-endian unsigned 32-bit format to `transition_u32le.bin`. Thus the certificate contains a value for **every** state, not a statistical sample.

**2. Exact functional-digraph classification.** The directed graph with one edge \(x\to F(x)\) at every state is a finite functional graph. Repeated removal of zero-indegree vertices leaves precisely its directed cycles: a vertex on a directed cycle cannot be removed, while every vertex not on one is removed inductively by following the finite distance to a cycle. `dodeca_majority.cpp` carries out this exact removal, traverses every remaining cycle, records each least period, and propagates periods, basin membership, and first-entry times backwards through the removal order. The resulting full census has 118 period-one cycles and 9,679 period-two cycles, with no other remaining lengths. The total 19,476 recurrent states equal \(118+2(9{,}679)\). Its basin/entry table is the table above. The maximum computed entry time is seven, with state integer `5608` providing a witness. It follows for every state that \(F^7(x)\) has period dividing two, equivalently \(F^9=F^7\), and that no smaller uniform entrance bound works.

**3. Independent exhaustive replay.** `verify_dodeca.cpp` computes the successor function again by the independent Boolean formula \((a\land b)\lor(a\land c)\lor(b\land c)\), and compares its value against **every** entry of `transition_u32le.bin`. It then, for every state, directly walks forward to the first state satisfying \(F^2(y)=y\) and checks each of the 16 entrance-time/eventual-period cells. This second procedure does not use indegree removal or the first program's cycle IDs. It reproduced the entire table and sharp bound. The source and console outputs are embedded. Together the explicit algorithm and complete input range establish the exact finite claim, without extrapolation.

**4. Full automorphism census.** `verify_automorphism_group.cpp` independently enumerates every adjacency-preserving permutation by backtracking, mapping each unassigned vertex to an unused vertex whose adjacency/nonadjacency relationship with all previously mapped vertices agrees. Exhaustiveness follows from considering every compatible image at each recursion level. It finds exactly 120 automorphisms and verifies equality with the 120 stored in `automorphisms.csv`. `symmetry_classes.cpp` checks all permutations preserve edges, acts on every periodic configuration and identifies time reversal by using the smaller integer of a pair \(\{x,F(x)\}\). Its exhaustive resulting class list in `symmetry_classes.tsv` contains nine fixed-point and 145 two-cycle classes, covering all 118 and 9,679 temporal orbits. Class-size frequency tables appear in `symmetry_output.txt`.

**5. Matching-cut structural interpretation.** In any cubic graph, a binary coloring is fixed under neighbor-majority exactly when every vertex has at most one neighbor of the opposite color. Equivalently, the set of edges crossing the two color classes is a matching. `verify_matching_cuts.cpp` independently checks this equivalence on every dodecahedral coloring and returns the fixed-point count 118. Complementing all bits is a fixed-point-free involution on these 118 colorings, yielding 59 complementary pairs. This matching-cut equivalence is elementary; the dodecahedral count comes from the exhaustive computation.

## Verification

The standalone C++17 sources were compiled and executed against the embedded data. For the binary-state transition record there is no reliance on a black-box external solver: the transition table can be reconstructed by running the included generator. A reproduction from an extracted directory with a C++17 compiler is:

```sh
g++ -O2 -std=c++17 verify_graph_identity.cpp -o graph && ./graph
g++ -O2 -std=c++17 dodeca_majority.cpp -o majority && ./majority
g++ -O2 -std=c++17 verify_dodeca.cpp -o check_majority && ./check_majority
g++ -O2 -std=c++17 verify_automorphism_group.cpp -o check_symmetry && ./check_symmetry
g++ -O2 -std=c++17 symmetry_classes.cpp -o classes && ./classes
g++ -O2 -std=c++17 verify_matching_cuts.cpp -o matching && ./matching
```

Running the generator writes its binary transition table and the temporal cycle representatives. `verify_dodeca.cpp` compares all 1,048,576 binary records with an independent transition implementation before checking all states' first-entry times. The checks report `VERIFY_ALL_1048576_TRANSITIONS_AND_BASINS_OK`, `AUTOMORPHISM_GROUP_EXHAUSTIVE=120`, `EXPLICIT_ISOMORPHISM_TO_GP_10_2_VERIFIED`, and `CUBIC_MAJORITY_FIXED_IFF_BICHROMATIC_EDGES_MATCHING=YES`. `transition_u32le.bin` contains exactly 4,194,304 bytes, with SHA-256 `231454f9198ec28f2950bcf9004b75978c9275ac53635cbe93ba6a5fcc741fc6`.

## Relationship to prior work

The general eventual-period-one-or-two theorem of Goles and Olivos is **not new**; the accessible treatment by Benjamini, Chan, O'Donnell, Tamuz and Tan (2014, §1) states it explicitly. Tošić and Agha (2004) consider parallel majority threshold cellular automata primarily in one dimension and describe their generic fixed/cycle/transient structure. Maldonado and collaborators (2023, §2.2) recall a general transient bound by the number of edges. None of these general results specifies the exact dodecahedral counts or the sharp seven-step clock. The same graph is also known as \(GP(10,2)\). The new contribution assessed here is the **exact graph-specific recurrent/basin/symmetry census**, not the general period-two restriction or the elementary matching-cut equivalence.

## Limitations

This is a finite, exhaustive classification for a **single** natural graph, not a theorem for all cubic, planar, or generalized Petersen graphs. The argument uses a complete, reproducible computation; the data files and algorithms must be preserved to replay every integer count. Exact novelty cannot be guaranteed against unindexed historical enumerations or alternate graph-labelling conventions. The matchings interpretation does not imply a generic closed formula for larger graph families. No external independent audit has been performed.

## References

1. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, *Convergence, Unanimity and Disagreement in Majority Dynamics on Unimodular Graphs and Random Graphs*, arXiv:1405.2486v1 (11 May 2014), https://arxiv.org/pdf/1405.2486.
2. P. T. Tošić and G. A. Agha, *Characterizing Configuration Spaces of Simple Threshold Cellular Automata*, ACRI (2004), https://osl.cs.illinois.edu/media/papers/tosic-2004-acri-characterizing_configuration_spaces_of_simple_threshold_cellular_automata.pdf.
3. D. Maldonado, P. Montealegre, M. Ríos-Wilson, and G. Theyssier, *Local Certification of Majority Dynamics*, arXiv:2309.01852v1 (4 September 2023), https://arxiv.org/pdf/2309.01852.
4. E. W. Weisstein, *Dodecahedral Graph*, MathWorld, https://mathworld.wolfram.com/DodecahedralGraph.html.
