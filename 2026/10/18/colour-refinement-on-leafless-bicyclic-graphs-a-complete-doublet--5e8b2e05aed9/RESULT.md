# Colour refinement on leafless bicyclic graphs: a complete doubleton classification

## Finding

**Theorem.** Let \(\mathcal B\) be the class of finite connected simple undirected graphs \(G\) with minimum degree at least two and \(|E(G)|=|V(G)|+1\). Two graphs are called \(C^2\)-equivalent when they satisfy the same sentences of two-variable first-order logic with counting; equivalently, synchronous one-dimensional colour refinement gives the same multiplicity for every stable vertex colour.

For integers \(a\geq3\) and \(c\geq1\), let \(\Theta(a,a,c)\) have two distinct poles joined by three internally vertex-disjoint paths of edge lengths \(a,a,c\), and let \(B(a,c)\) consist of two vertex-disjoint cycles of length \(a\) joined by a path of edge length \(c\). These graphs each have \(2a+c-1\) vertices and \(2a+c\) edges.

Every non-singleton \(C^2\)-equivalence class **within \(\mathcal B\)** consists of exactly the nonisomorphic pair
\[
 \{\Theta(a,a,c),\ B(a,c)\}\qquad(a\ge3,\ c\ge1).
\]
Distinct parameter pairs yield distinct equivalence classes. Thus, among the members of \(\mathcal B\) with exactly \(n\) vertices, all non-singleton equivalence classes are doubletons, and their number is
\[
 d_n=\max\!\bigl\{0,\lfloor n/2\rfloor-2\bigr\} \qquad(n\ge4).
\]
In particular the first failure occurs at six vertices and has exactly one exceptional pair: a six-cycle with a chord joining opposite vertices (two length-three paths and a direct edge between the poles), versus two triangles joined by an edge.

## Assumptions and scope

All graphs are finite, uncoloured, loopless, without multiple edges, and considered up to unlabelled graph isomorphism. The class is restricted to connected graphs of cyclomatic number two that have no pendant trees. Comparison is *relative to this class*: we make no claim that its members are identifiable among arbitrary disconnected graphs or graphs with different cycle rank. A path length always counts edges. A cycle in \(B(a,c)\) is simple, hence \(a\ge3\).

## Proof

**1. The three core shapes.** Let \(G\in\mathcal B\). Since \(\sum_v(\deg(v)-2)=2\) and every degree is at least two, either one vertex has degree four and every other vertex has degree two, or exactly two vertices have degree three and every other vertex has degree two. Suppress the degree-two vertices, retaining the lengths of the suppressed paths as positive integers. In the degree-four case the core is two loops at one vertex (a figure-eight); in the degree-three case it is either three parallel edges between two vertices (a theta graph) or one loop at each vertex joined by one edge (a barbell). The figure-eight is determined by the unordered lengths \(\{a,b\}\) of its cycles, both at least three. The theta is determined by its unordered triple of path lengths, with at most one path of length one; the barbell is determined by the unordered pair of cycle lengths \(a,b\ge3\) and its joining-path length \(c\ge1\). These statements also establish completeness of the three shape families and uniqueness of their parameters within each family.

**2. A necessary colour-refinement invariant.** A standard rooted-cover characterization of colour refinement says that two vertices have the same colour at all refinement rounds precisely when their rooted universal covering trees are isomorphic. The forward direction can be proved by comparing every finite-depth unfolding and using finite branching; the reverse follows by induction on refinement rounds. This is the ordinary colour-refinement/universal-cover correspondence, not an additional hypothesis. In the universal covering tree of a member of \(\mathcal B\), mark vertices of degree at least three. For any marked root, follow each incident edge until the next marked vertex, and record the number of edges traversed. The resulting multiset of three or four positive integers is therefore determined by its ultimate colour. The same is true for the degree of the marked root. Consequently, \(C^2\)-equivalent members of \(\mathcal B\) have identical multisets of these marked-root length signatures.

**3. Excluding all shapes except the stated pairs.** The degree-four figure-eight has one marked vertex, with length signature \(\{a,a,b,b\}\); it cannot be confused with a degree-three core, and its signature determines the unordered pair \(\{a,b\}\). A theta graph with path lengths \(p,q,r\) has two marked vertices, each with signature \(\{p,q,r\}\). Hence two equivalent theta graphs are isomorphic. A barbell with cycle lengths \(a,b\) and bridge length \(c\) has two marked vertices, with signatures \(\{a,a,c\}\) and \(\{b,b,c\}\). If \(a\ne b\), these signatures are distinct, whereas the two theta signatures coincide. Moreover, the unordered pair of these two distinct signatures determines the unordered cycle lengths \(\{a,b\}\) (their duplicated entries) and the bridge length \(c\); thus two equivalent unequal-cycle barbells are isomorphic. If \(a=b\), the common barbell signature is \(\{a,a,c\}\), which determines \(a,c\), and it can equal a theta signature only when the theta path lengths are precisely \(\{a,a,c\}\). This exhausts all possible nonisomorphic equivalences.

**4. The exceptional pairs really are equivalent.** Fix \(a\ge3\) and \(c\ge1\). Give both graphs the following common partition into putative vertex colours. Colour the two degree-three vertices with a single colour \(P\). For each internal vertex at position \(j\) along a degree-two path of length \(L\) between marked endpoints, give the colour \((L,\min\{j,L-j\})\), where each of the two cycles in the barbell is viewed as a path from its marked vertex back to itself. Merge identical colour names if \(a=c\). In either graph each marked vertex has two incident path ends of length \(a\) and one of length \(c\); all internal vertices with a given colour have the same multiset of neighbour colours. The partition is therefore equitable in each graph with identical neighbour-count data. The colour-class sizes also agree, since each graph contains two path pieces of length \(a\) and one of length \(c\). Starting from the uniform colour, simultaneous colour refinement cannot distinguish their stable colour histograms. Thus the pair is \(C^2\)-equivalent.

**5. Nonisomorphism and enumeration.** Each barbell has a bridge (the joining path contains bridges), whereas each theta has no bridge; hence the two members of every displayed pair are nonisomorphic. A pair has \(n=2a+c-1\) vertices. For fixed \(n\), this is possible exactly when \(3\le a\le\lfloor n/2\rfloor\), with uniquely determined positive \(c=n+1-2a\). Distinct such parameters give distinct length signatures and hence distinct classes. Their number is \(d_n\), as stated. The smallest admissible choice is \((a,c)=(3,1)\), giving the unique six-vertex ambiguity.

## Verification

Two separately structured executable checks are included. `check_small.py` enumerates **every labelled connected** simple graph with \(n+1\) edges for \(n=4,5,6\), groups them under exact NetworkX graph isomorphism, and checks the potentially ambiguous degree/neighbour-degree buckets with synchronous colour refinement. It obtains respectively \(1,5,19\) isomorphism classes and \(1,5,18\) degree/neighbour-degree signature buckets, the sole doubleton appearing for \(n=6\). Since every refinement equivalence implies equality of these early signatures, no additional small-order collision is possible. `check_core.py` enumerates the three complete core parameter families independently for \(4\le n\le17\), compares all \(9619\) pairs of parameter classes using synchronous refinement, and confirms precisely the classification above. The exact stdout is included. These are finite corroborations; the unbounded theorem rests on the preceding proof rather than on extrapolating the experiment. Run using Python with NetworkX installed: `python check_small.py` and `python check_core.py`.

## Relationship to prior work

The equivalence of \(C^2\) and one-dimensional colour refinement, and the general theory of which graphs are identifiable by this logic, are established in the existing literature and are not novel claims here. Arvind, Köbler, Rattan, and Verbitsky (2015) classify general amenability to colour refinement; Kiefer, Schweitzer, and Selman (2015) classify graphs identified by \(C^2\). The present result instead gives an explicit **complete equivalence-class classification** within all leafless connected bicyclic graphs, including the exact exceptional parameter family and number of doubletons at each order. The later Verbitsky–Zhukovskii (2025) treatment of universal covers and unicyclic graphs is compatible with the rooted-cover step, but its unicyclic statement does not classify bicyclic-core collisions. No identical explicit theorem was found in the inspected passages; the general classification literature remains a priority caveat, as the exact statement might be derivable from it with additional work.

## Limitations

The result does not address pendant trees, disconnected graphs, multigraphs, directed graphs, higher cyclomatic rank, or distinguishability by stronger logics. We do not claim an independent literature audit; a specialised earlier description of theta/barbell fractional isomorphism might exist. The formula counts only non-singleton equivalence classes **inside** \(\mathcal B\), not all unlabeled bicyclic graphs or all logical theories on graphs of order \(n\).

## References

- V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first public version 2015-02-04; https://arxiv.org/abs/1502.01255 .
- S. Kiefer, P. Schweitzer, E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792, first public version 2015-03-30; https://arxiv.org/abs/1503.08792 .
- O. Verbitsky, M. Zhukovskii, *Canonical Labeling of Sparse Random Graphs*, STACS 2025, DOI:10.4230/LIPIcs.STACS.2025.75, §2.2–2.3 (universal covering trees and unicyclic graphs); https://doi.org/10.4230/LIPIcs.STACS.2025.75 .
