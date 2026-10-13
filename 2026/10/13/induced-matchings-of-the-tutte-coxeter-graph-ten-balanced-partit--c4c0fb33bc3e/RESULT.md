# Induced matchings of the Tutte–Coxeter graph: ten balanced-partition maxima and an eight-edge completion law

## Finding
Let \(X\) be a six-element set. The Tutte–Coxeter graph \(G\) has as its bipartition the fifteen duads (two-element subsets of \(X\)) and the fifteen synthemes (partitions of \(X\) into three duads); a duad is adjacent to a syntheme exactly when it occurs in that partition. An *induced matching* is a set of pairwise disjoint edges whose endpoints induce no additional edges. The induced-matching polynomial, with the empty matching included, is
\[
I_G(z)=1+45z+720z^2+5160z^3+16920z^4+22680z^5+8520z^6+720z^7+90z^8+10z^9.
\]
Thus \(G\) has \(54{,}866\) induced matchings, and its induced matching number is \(9\). Exactly ten induced matchings attain size \(9\). They correspond bijectively to the ten unordered balanced bipartitions \(X=A\sqcup B\) with \(|A|=|B|=3\): for each cross-duad \(\{a,b\}\), where \(a\in A\) and \(b\in B\), choose its unique syntheme \(\{\{a,b\},A\setminus\{a\},B\setminus\{b\}\}\).

Every one of the \(90\) induced matchings of size \(8\) extends to a matching of size \(9\) in **exactly one way**. The inclusion-maximal induced matchings have size and multiplicity \(5:3060\), \(6:5520\), \(7:360\), and \(9:10\); in particular there are no inclusion-maximal matchings of size \(8\), and there are exactly \(8950\) inclusion-maximal induced matchings.

## Assumptions and scope
The objects are simple finite graphs, with ordinary *induced* (also called strong) edge matchings, not arbitrary matchings or perfect matchings. Duads and synthemes are regarded as distinct types of vertices even though both parts have fifteen vertices. All numbers apply to the single order-two generalized-quadrangle incidence graph, equivalently the Tutte eight-cage; no higher-order generalized-quadrangle claim is made. An inclusion-maximal matching cannot be extended by one graph edge, whereas a maximum matching has the largest possible number of edges.

## Proof
**Private-syntheme lemma.** For a set \(S\) of duads, let
\[
a_S(p)=\#\{\ell\text{ a syntheme}:\ell\cap S=\{p\}\}\qquad (p\in S).
\]
Every induced matching selects a distinct duad set \(S\) and, for each selected duad \(p\), one syntheme intersecting \(S\) only at \(p\). Conversely, any such independent choices give an induced matching: no chosen syntheme can serve two selected duads, and neither cross-incidences nor shared endpoints are possible. Consequently
\[
I_G(z)=\sum_{S\subseteq\binom X2}z^{|S|}\prod_{p\in S}a_S(p).
\tag{1}
\]
The empty product equals one. Formula (1) involves exactly \(2^{15}=32768\) explicitly defined duad subsets; its complete evaluation, with a separate edge-conflict enumeration, is provided by the embedded source files and checked certificate `spectrum.csv`. Their algorithms enumerate all finite cases and produce exactly the coefficients displayed above.

**Sharp upper bound and classification.** View the duads as edges of \(K_6\). For a selected duad set \(S\), let \(C=E(K_6)\setminus S\). Every private syntheme for \(p\in S\) consists of \(p\) and two disjoint edges of \(C\), which cover the other four vertices. Choosing one private syntheme for each \(p\) therefore injects \(S\) into the set of unordered pairs of disjoint edges of \(C\), because such a pair determines the remaining duad \(p\).

If \(|S|\ge10\), then \(|C|\le5\). A simple graph with five edges on six vertices must have two edges sharing a vertex, so it has at most nine pairs of disjoint edges; with at most four edges, it has at most six. This contradicts the injection, proving \(|S|\le9\). If \(|S|=9\), then \(|C|=6\). The number of pairs of disjoint edges of \(C\) is
\[
\binom62-\sum_{v\in X}\binom{d_C(v)}2\le 15-6=9,
\]
because the six degrees sum to twelve, and the convex sum is at least six, with equality only when every degree equals two. To attain nine private flags, equality is necessary; thus \(C\) is a six-cycle or the disjoint union of two triangles. A six-cycle has a perfect matching consisting of three \(C\)-edges: the pair formed by any two of those edges leaves a third \(C\)-edge, so the injection cannot be onto all nine disjoint pairs. Therefore \(C\) is the union of two triangles. Its complement \(S\) is the nine-edge complete bipartite graph across a unique unordered \(3+3\) partition. Every cross edge has precisely one private syntheme, the one stated in the finding. There are \(\binom63/2=10\) partitions, all yielding the stated maximum configurations, and the permutations of \(X\) act transitively on them.

**Unique completion.** Any two distinct unordered \(3+3\) partitions have at most five cross-duads in common: after possibly interchanging parts, one partition is obtained from the other by swapping one element from each part, retaining four cross-duads between the unmoved elements and one connecting the swapped pair. Their maximum induced matchings consequently share at most five edges. Deleting one edge from each of the ten maximum matchings produces \(10\cdot9=90\) distinct size-eight induced matchings. The evaluation of (1), independently checked by direct conflict-graph enumeration, gives exactly \(90\) size-eight matchings. Thus this construction exhausts them, and none has a second size-nine extension.

**Inclusion-maximal spectrum.** For a matching represented by duad set \(S\) and private synthemes \(\ell_p\), an additional flag \((q,\ell)\) is legal precisely when \(q\notin S\), \(q\) belongs to no chosen \(\ell_p\), and \(\ell\) contains \(q\) but no member of \(S\). The point-subset verifier tests this exact condition for every matching produced by (1). Independently, `verify_conflict.py` generates every compatible subset of the 45 graph edges and tests one-step extendibility against all 45 edges. Both give the inclusion-maximal multiplicities reported in the finding.

## Verification
Execute `python3 verify_duad.py` and `python3 verify_conflict.py` from a directory containing these programs and `spectrum.csv` and `maxima.csv`; both use only Python's standard library. The first checks all 32,768 duad subsets, the polynomial, every extension count, the ten partition-based maxima, and both certificates. The second directly enumerates all 54,866 induced matchings as compatible subsets of 45 flags, recomputes the polynomial and maximal spectrum, and checks the certificate of all ten maxima. Both executions completed successfully with the outputs recorded in `VERIFICATION.md`. Their agreement is a cross-check between different finite enumeration formulations; the geometric maximum classification is proved separately above.

## Relationship to prior work
Cimráková and Fack, *Clique Algorithms for Finding Substructures in Generalized Quadrangles* (2007), study maximal partial ovoids and spreads in generalized quadrangles. Those are sets of pairwise noncollinear points or nonconcurrent lines; their results do not count or classify sets of noninterfering incident point–line flags in the Levi graph. Balasubramanian, *Matching Polynomials of Symmetric, Semisymmetric, Double Group Graphs, Polyacenes, Wheels, Fans, and Symmetric Solids in Third and Higher Dimensions* (2025), gives the **ordinary** Tutte–Coxeter matching polynomial; for example, its number of two-edge matchings is \(900\), whereas the number of induced two-edge matchings here is \(720\). Neither an ordinary-matching enumeration nor a partial-ovoid classification determines formula (1), the maximal induced-matching spectrum or the unique size-eight completion law.

## Limitations
This is an exact finite-graph result and does not assert a uniform enumeration for generalized quadrangles of other orders. The coefficient computation and inclusion-maximal census are proved by exhaustive finite algorithms whose complete source is included; the upper bound and all ten maxima also have the structural proof above. An unindexed earlier graph-specific enumeration could have obtained related numbers; no unqualified worldwide priority claim is made. Reproduction requires executing the supplied finite checks, not treating a log alone as proof.

## References
1. M. Cimráková and V. Fack, *Clique Algorithms for Finding Substructures in Generalized Quadrangles*, Journal of Combinatorial Mathematics and Combinatorial Computing **63** (2007), 129–143. https://combinatorialpress.com/jcmcc-articles/volume-063/clique-algorithms-for-finding-substructures-in-generalized-quadrangles/ . Public date: 2007-11-30.
2. K. Balasubramanian, *Matching Polynomials of Symmetric, Semisymmetric, Double Group Graphs, Polyacenes, Wheels, Fans, and Symmetric Solids in Third and Higher Dimensions*, Symmetry **17** (2025), article 133. https://doi.org/10.3390/sym17010133 . Public date: 2025-01-17.
