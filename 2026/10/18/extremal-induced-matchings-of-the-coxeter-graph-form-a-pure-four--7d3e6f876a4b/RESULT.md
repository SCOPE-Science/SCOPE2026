# Extremal induced matchings of the Coxeter graph form a pure four-packing geometry

## Finding
Let \(G\) be the Coxeter graph, with vertices the \(28\) noncollinear triples in the seven-point Fano plane and with two triples adjacent exactly when disjoint. An **induced matching** is a set of edges whose endpoints induce a disjoint union of single edges. Then the largest induced matching has \(7\) edges, and there are exactly \(84\) such matchings. The natural group of \(168\) Fano-plane collineations acts transitively on them.

Form the **extremal-disjointness graph** \(D\): its vertices are these \(84\) size-seven induced matchings, and two are adjacent precisely when the two sets of Coxeter-graph edges are disjoint. Then \(D\) is \(26\)-regular, and every maximal clique of \(D\) has size **exactly four**. In particular, the largest number of pairwise edge-disjoint maximum induced matchings is \(4\), and the clique complex of \(D\) is pure of dimension \(3\). Its numbers of cliques of sizes \(0,1,2,3,4\) are respectively
\[
1,\quad 84,\quad 1092,\quad 3528,\quad 2478,
\]
and there are no larger cliques. Thus every disjoint family of one, two, or three maximum induced matchings extends to one of the \(2478\) four-member families.

For context, the already-published strong chromatic index is \(\chi'_s(G)=7\). The structural classification here explains why the naive edge-count lower bound \(\lceil42/7\rceil=6\) cannot be attained: a six-coloring would require six pairwise edge-disjoint maximum induced matchings, but even five are impossible. A separately checked seven-color witness is included; the **value seven is credited as prior work**, not retained as new.

## Assumptions and scope
Use the cyclic seven-point model: for each \(i\in\mathbb Z/7\mathbb Z\), the Fano line \(L_i=\{i,i+1,i+3\}\) has indices reduced modulo \(7\). These are seven different triples and every pair of points occurs in a unique line, as can also be seen from the distinct nonzero differences of \(\{0,1,3\}\). Let \(V\) consist of all three-element subsets of \(\{0,\ldots,6\}\) other than these seven lines, ordered lexicographically. Two triples are adjacent if disjoint, and the \(42\) edges of \(G\) are ordered by increasing endpoint indices in that vertex ordering. All finite certificates use zero-based edge indices \(0,\ldots,41\).

An extremal-disjointness clique requires **edge-disjointness of the size-seven induced matchings**, not vertex-disjointness of their combined graph supports. The theorem is confined to the standard finite \(28\)-vertex Coxeter graph, not an assertion about every cubic graph or every generalized Coxeter graph.

## Proof
**1. Graph and compatibility reduction.** A pair of distinct graph edges \(e=ab\) and \(f=cd\) may appear together in an induced matching if and only if \(a,b,c,d\) are four distinct vertices and none of \(ac,ad,bc,bd\) is a graph edge. This predicate is checked directly using the Fano-triple adjacency definition; it is equivalent to nonadjacency in the square of the Coxeter line graph. The seven Fano lines leave \(\binom73-7=28\) vertices; direct incidence inspection verifies degree three, hence \(42\) edges.

**2. Exhaustive, nonprobabilistic matching recurrence.** Label the edges \(e_0,\ldots,e_{41}\). For each edge index \(i\), form the bitset \(C_i\) of strictly larger indices \(j>i\) compatible with \(e_i\). Starting from the empty chosen sequence and the full candidate set \(P\), visit a node once; then for every \(i\in P\), in increasing order, recurse on \(P_{>i}\cap C_i\) with \(i\) appended. Here \(P_{>i}\) means candidates larger than \(i\). Every induced matching has one unique increasing index sequence, and each is visited exactly once by induction on its length. Because the code continues until no candidate remains, it does not assume the maximum size in advance. The complete counts by size \(0\) through \(8\) are
\[
(1,42,609,3808,10374,11172,4242,84,0),
\]
with no counts beyond size \(8\). Thus the maximum is \(7\), with exactly \(84\) witnesses. The provided `certificate.json` lists all \(84\) as \(42\)-bit edge masks. A separate C++17 program directly checks each new edge against every previously chosen edge instead of relying on precomputed compatibility bitsets; it reproduces the same complete list.

**3. Disjoint packing recurrence and purity.** Construct a second graph on the \(84\) masks, where two masks are adjacent when their bitwise intersection is zero. The same strictly-increasing recursion, this time imposing pairwise zero intersection, enumerates each clique once. The full count vector by clique size \(0\) through \(5\) is
\[
(1,84,1092,3528,2478,0),
\]
and there are no larger cliques. An additional exhaustive maximality check considers every enumerated clique of sizes one, two, and three and tests all other \(84\) masks for an additional compatible member. None is maximal. Every four-member clique is maximal because five-member cliques do not exist. Degree inspection finds exactly \(26\) neighbors for each of the \(84\) vertices. Hence every maximal clique has size four and there are exactly \(2478\) of them. These assertions are independently checked by both programs, with the C++ implementation testing disjointness directly against each existing member.

**4. Transitivity.** Enumerate all \(7!\) permutations of the Fano points and retain precisely those preserving the seven line triples. There are exactly \(168\). Each acts on the graph vertices and thus on its ordered edge set. Applying these \(168\) permutations to one of the enumerated maximum masks yields exactly the same \(84\) masks found in Step 2; the two sets are compared for equality, not just cardinality. Therefore the natural collineation group acts transitively on the maximum induced matchings.

**5. Relation to strong coloring.** A strong edge color class is an induced matching, so a hypothetical six-coloring would partition \(42\) edges into six maximum seven-edge matchings; Step 3 forbids even five such pairwise disjoint sets. The `certificate.json` field `seven_strong_color_classes_edge_indices` gives seven explicit edge-index classes that partition all \(42\) edges. Both checkers verify every pair within every class satisfies the compatibility predicate. This rederives the previously known \(\chi'_s(G)=7\) and proves that the packing structure, rather than just a generic spectral bound, supplies a direct six-color obstruction.

## Verification
Run `python3 verify_python.py`; this writes `certificate.json` and prints its exact census. Independently compile and run `g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_cpp.cpp -o verifier && ./verifier`. Compare the sorted hexadecimal maximum-mask lines between `cpp_output.txt` and `certificate.json`; they agree entry for entry. The output files `python_output.txt` and `cpp_output.txt` record the actual checks. The two programs reconstruct the graph from the Fano lines, enumerate all induced matchings and all disjointness cliques, verify purity and check the seven-color witness; the Python verifier also enumerates the collineation action. No external data, optimization solver, or unprovided input is needed.

## Relationship to prior work
The Coxeter graph's Fano-triangle realization and automorphisms are classical; see the graph description of Brouwer and Orel's 2015 full-text paper. Abiad and Reijnders explicitly report \(\chi'_2(G)=7\) for the Coxeter graph in the 2025 preprint, Table 1 (2026 revision). Their accompanying lower-bound comparison reports a spectral lower bound of \(6\); the present extremal-disjointness geometry explains this one-unit shortfall through an exact packing obstruction. The prior paper's table **already covers the numerical strong chromatic index**, and no priority claim is made for it. The available publications and mathematical-record searches did not identify the \(84\)-element single-orbit classification, the \(26\)-regular disjointness graph or the pure four-packing theorem.

Brouwer's description and a 2025 matching-polynomial table discuss \(84\) **perfect matchings** (each has \(14\) edges); this is a different set of objects from the \(84\) **induced matchings of size seven** classified here. Equality of the two counts is not an implication between the assertions. Separate work on maximum induced matchings of the Tutte–Coxeter graph concerns another graph and does not determine this Coxeter packing geometry.

## Limitations
This is an exact finite classification proved by exhaustively checkable enumeration, with two separately implemented verifiers; it is not a general parameter theorem. The numeric strong chromatic index is previously published. The \(84\) extremal induced matchings, single collineation orbit, clique counts and four-packing purity are retained as the proposed new contribution. Indexed or inaccessible literature or supplementary data could still contain an equivalent classification; no absolute priority or independent external validation is asserted. The proof uses complete exhaustive finite searches, not extrapolation from samples. All scientific assertions can be checked from the bundled source files and their regenerated outputs.

## References
1. M. Orel, *On generalizations of the Petersen graph and the Coxeter graph*, Electronic Journal of Combinatorics 22(4), P4.27 (published 2015-11-13), DOI 10.37236/3759. Full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v22i4p27/pdf/ .
2. A. Abiad and H. Reijnders, *Eigenvalue bounds for distance-edge colourings*, arXiv:2506.20976 (first posted 2025-06-26), Appendix, Table 1, Coxeter row. https://arxiv.org/abs/2506.20976 .
3. A. E. Brouwer, *Coxeter graph*, descriptive mathematical graph record. https://aeb.win.tue.nl/graphs/Coxeter.html .
4. *Matching Polynomials of Symmetric, Semisymmetric, Double Group Graphs, Polyacenes, Wheels, Fans, and Symmetric Solids in Third and Higher Dimensions*, Symmetry 17 (2025), 133, matching-polynomial table. https://www.mdpi.com/2073-8994/17/1/133 .
