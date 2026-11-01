# The complete Petersen cut-complex filtration and its unique mixed-dimensional stage

## Finding
Let \(P=\mathrm{KG}(5,2)\) be the Petersen graph. For integers \(2\le k\le10\), let \(\Delta_k(P)\) be its **ordinary** \(k\)-cut complex, whose facets are complements of disconnected induced \(k\)-vertex subsets. The complete integral homotopy classification is
\[
\Delta_k(P)\simeq
\begin{cases}
\bigvee^6S^6,&k=2,3,\\
\bigvee^{26}S^5,&k=4,\\
S^3\vee\bigvee^5S^4,&k=5,\\
\bigvee^{11}S^3,&k=6,\\
\bigvee^{11}S^1,&k=7,\\
\varnothing,&k=8,9,10.
\end{cases}
\]
Here \(\varnothing\) denotes the void simplicial complex (no faces, even the empty face). The genuinely new classification is for \(k=5,6,7\), which completes the family in the previously unclassified range; the cases \(k=2,3,4\) are included for context and are not claimed as new. In particular, \(k=5\) is the **unique** nonempty mixed-dimensional homotopy type in the filtration and is a pure four-dimensional but nonshellable complex.

## Assumptions and scope
Identify the ten vertices with the unordered pairs in \(\{0,1,2,3,4\}\) in lexicographic order, and join two vertices precisely when their two-element sets are disjoint. For every \(k\), include the complement of each disconnected induced \(k\)-subset as a facet and all of its subsets as faces. The face set can also be characterized as all \(\sigma\subseteq V(P)\) whose complement contains a disconnected induced \(k\)-subset. These are *ordinary* cut complexes, not total cut complexes formed from independent sets.

Orient each simplex by the increasing vertex-index order, and encode faces as integers with vertex-index bits. The classification concerns geometric realizations and integral homotopy equivalence. No assertion is made for other graphs or \(k>10\).

## Proof
**Exhaustive finite face construction.** Independently enumerate (a) every complement of a disconnected induced \(k\)-subset and downward-close its faces; and (b) every nonempty vertex subset and directly test whether its complement has a disconnected induced \(k\)-subset. These two procedures return identical face sets for each \(2\le k\le10\). The respective numbers of facets and nonempty faces are:

| \(k\) | Facets | Nonempty faces |
|---|---:|---:|
| 2 | 30 | 997 |
| 3 | 90 | 937 |
| 4 | 140 | 765 |
| 5 | 120 | 495 |
| 6 | 65 | 210 |
| 7 | 10 | 50 |
| 8, 9, 10 | 0 | 0 |

**Complete discrete Morse reduction.** For each nonvoid complex, designate a root singleton and visit vertex indices successively. At stage \(v\), pair all still-unmatched \(\sigma\ne\text{root}\) not containing \(v\) with \(\sigma\cup\{v\}\) whenever both faces survive; remove the pairs, and continue. All pairs at a stage are disjoint. In the directed Hasse diagram, matched incidence arrows point upward and all other codimension-one arrows downward. An exhaustive topological sort proves acyclicity on *every* face and incidence. Forward and reverse vertex orders give independent finite Morse reductions with the same final integral homology.

In forward vertex order, the unmatched critical cells are exactly one degree-zero cell and, respectively, six degree-six cells (\(k=2,3\)), 26 degree-five cells (\(k=4\)), eight degree-three plus twelve degree-four cells (\(k=5\)), eleven degree-three cells (\(k=6\)), and eleven degree-one cells (\(k=7\)). Thus all cases other than \(k=5\) have immediate sphere-bouquet homotopy types, with the \(k=7\) complex having a one-vertex, eleven-loop graph CW model.

**The mixed-dimensional attaching matrix.** For \(k=5\), the 495 simplices support 237 pairs; the remaining CW complex has one zero-cell, eight three-cells and twelve four-cells. The complete directed Hasse graph has 1,850 arrows, and its topological sort verifies acyclicity. Let \(F(\sigma)\) project an oriented three-simplex to the critical three-cells. A critical face projects to itself; an upper matched face projects to zero; a face matched upward to a four-simplex \(\tau\) satisfies
\[
F(\sigma)=-[\tau:\sigma]^{-1}\sum_{\rho\subset\tau,\ \dim\rho=3,\ \rho\ne\sigma}[\tau:\rho]F(\rho),
\]
where the incidence signs are the standard oriented simplicial boundary coefficients. Acyclicity ensures termination. Evaluating the signed boundary of each critical four-cell produces an integral \(8\times12\) Morse matrix with Smith factors seven units and five zero columns. A reverse-order computation has ten critical three-cells and fourteen critical four-cells, with a \(10\times14\) matrix having nine unit factors. The two computations independently give \(\widetilde H_3\cong\mathbb Z\), \(\widetilde H_4\cong\mathbb Z^5\), and no torsion.

**Homotopy upgrade.** The Morse model has a single zero-cell, no cells of dimension one or two, and eight degree-three cells. Its three-skeleton is \(\bigvee^8 S^3\), hence is 2-connected and the Hurewicz isomorphism identifies its \(\pi_3\) with \(\mathbb Z^8\). Therefore the integral degree matrix fully determines the homotopy classes of the four-cell attaching maps. Unimodular changes of basis and elementary cancellation of seven unit-boundary cell pairs give \(S^3\vee\bigvee^5S^4\). This establishes **homotopy equivalence**, not merely homology. A pure shellable four-complex has homology only in top degree; the nonzero degree-three homology therefore proves nonshellability of \(\Delta_5(P)\).

## Verification
The standalone Python 3 verifier `verify_petersen_cuts.py` reconstructs the labeled Petersen graph, independently checks every face by two methods, proves each forward and reverse Morse matching acyclic by a topological sort, computes all signed Morse boundary matrices, and reduces them to integer Smith normal form using explicit unimodular operations. The complete deterministic output is `verify_petersen_cuts_output.json`. Both vertex orders yield the same integral reduced Betti numbers. The two independent finite reconstructions and the integral calculations exhaust the full finite complexes, not a parameter sample.

The nontrivial forward-stage certificate data for \(k=5,6,7\), respectively, are 495, 210, and 50 nonempty faces; 237, 99, and 19 Morse pairs; and 1,850, 620, and 90 checked Hasse incidences. For \(k=5\), the essential integer boundary matrix has seven unit Smith factors.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue (2023, arXiv:2304.13675), Theorem 6.4 and Corollary 6.6, already give \(\Delta_2(P)\simeq\bigvee^6S^6\); their listed classifications do not determine the five-, six-, or seven-cut cases for this nonchordal, non-cycle, nonmultipartite graph. Bayer, Denker, Jelić Milutinović, Sundaram and Xue (2024, arXiv:2407.08158) consider disjoint unions, squared paths, and grids, not the Petersen five-cut stage. Previous finite and graph-girth classifications address the four-cut case, whose \(\bigvee^{26}S^5\) type is taken as known here; they do not determine this new mixed-dimensional five-cut complex. The general theorems for girth at least \(k+2\) also fail at \(k=5\), because the Petersen graph has girth five. Existing related *total* cut results apply a different face condition.

The value is the complete sequence for a canonical graph and, more pointedly, its unique transition through a mixed-dimensional nonshellable stage. Exact implication comparisons were used: a result for \(k\le4\), a different graph, or a total cut complex is not a theorem for \(k=5\). An equivalent unindexed calculation remains a bibliographic risk; searches cannot certify priority.

## Limitations
This is a finite, graph-specific homotopy classification. It supplies no general all-graph theorem or formula for other Kneser graphs. The computation is independently reproducible but has not undergone external independent audit. The cases \(k=2,3,4\) have earlier coverage and are included only to make the new filtration classification complete.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (initial public submission 2023-04-26); https://arxiv.org/abs/2304.13675 .
2. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram and L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158 (initial public submission 2024-07-11); https://arxiv.org/abs/2407.08158 .
3. M. Bayer et al., *Total Cut Complexes of Graphs*, arXiv:2209.13503 (initial public submission 2022-09-27); https://arxiv.org/abs/2209.13503 .
