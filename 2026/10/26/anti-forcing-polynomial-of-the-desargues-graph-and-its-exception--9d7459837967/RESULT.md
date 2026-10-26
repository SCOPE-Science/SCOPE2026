# Anti-forcing polynomial of the Desargues graph and its exceptional Petersen lifts

## Finding
Let \(D\) be the twenty-vertex Desargues graph, realized as the bipartite double of the Petersen graph. For each perfect matching \(M\) of \(D\), its **anti-forcing number** \(\operatorname{af}(D,M)\) is the minimum number of edges outside \(M\) whose deletion leaves \(M\) as the unique perfect matching. Then \(D\) has exactly sixty perfect matchings and its complete anti-forcing polynomial is
\[
 A_D(z)=\sum_{M\text{ perfect}}z^{\operatorname{af}(D,M)}=6z^5+54z^6.
\]
The six matchings of anti-forcing number five are **exactly** the symmetric lifts of the six perfect matchings of the Petersen graph. More precisely, the natural action of \(S_5\times C_2\) partitions the sixty matchings into three orbits:

| Orbit size | Cycle type of its bijection on Petersen vertices | Lengths of cycles in the complementary spanning two-factor | Anti-forcing number |
| ---: | --- | --- | ---: |
| \(6\) | \((2,2,2,2,2)\) | \((10,10)\) | \(5\) |
| \(24\) | \((5,5)\) | \((20)\) | \(6\) |
| \(30\) | \((2,8)\) | \((10,10)\) | \(6\) |

In particular, identical complementary two-factor cycle lengths do not determine a matching's anti-forcing number: both the six-element and thirty-element orbits have two ten-cycles but require respectively five and six deleted edges.

## Assumptions and scope
Write \(X=\binom{\{0,1,2,3,4\}}2\), a ten-element set. The graph \(D\) has vertices \(A_0,A_1\) for each \(A\in X\), with edges \(A_0B_1\) exactly when \(A\cap B=\varnothing\). Thus there are twenty vertices and thirty edges; the underlying graph on \(X\) with adjacency by disjointness is the Petersen graph \(KG(5,2)\). Equivalently, \(D\cong GP(10,3)\), or the incidence graph between the two- and three-subsets of a five-set after complementing the latter.

A perfect matching is uniquely represented by a bijection \(f:X\to X\) satisfying \(A\cap f(A)=\varnothing\) for every \(A\in X\), namely \(M_f=\{A_0f(A)_1:A\in X\}\). Ground-set permutations act by conjugating \(f\); the involution interchanging the two bipartition layers sends \(f\) to \(f^{-1}\). A symmetric lift means \(f=f^{-1}\), which then pairs the ten vertices of the Petersen graph into five disjoint edges.

The statement concerns the ordinary (unrestricted) anti-forcing number of each *fixed* perfect matching, not the anti-Kekulé invariant, not the ordinary zero-forcing invariant, and not a claim about all generalized Petersen graphs.

## Proof
**1. Exhaustion of perfect matchings and the three orbits.** Fix the lexicographic ordering
\[
 (01,02,03,04,12,13,14,23,24,34)
\]
of the ten two-subsets, abbreviating \(01=\{0,1\}\), etc. Each row \(A\) has precisely three eligible images disjoint from it. The backtracking recursion in `verify.py` chooses an unused eligible image for each consecutive row and hence visits every permitted bijection exactly once. The independent subset-permanent recurrence counts sixty bijections, agreeing with the backtracking list of sixty distinct matchings.

Apply each of the \(120\) ground-set permutations and the optional layer exchange to a bijection. Direct enumeration gives three disjoint orbits of cardinalities \(6,24,30\), totaling sixty. The orbit representatives below are lists of image *indices* for rows \(0,\ldots,9\) in the displayed ordering:
\[
\begin{aligned}
 f_{6}&=(7,6,8,5,9,3,1,0,2,4),\\
 f_{24}&=(7,5,6,4,9,8,1,3,2,0),\\
 f_{30}&=(7,5,6,4,9,8,2,3,0,1).
\end{aligned}
\]
Their permutation-cycle types are respectively \((2,2,2,2,2)\), \((5,5)\), and \((2,8)\). Removing the ten edges of each matching from the thirty-edge cubic graph leaves a two-factor, whose component lengths are respectively \((10,10)\), \((20)\), and \((10,10)\). The verifier checks that each invariant is constant throughout the corresponding orbit.

**2. Alternating cycles as directed cycles.** Fix \(f\). Contract every edge \(A_0f(A)_1\in M_f\) to the vertex \(A\). For every remaining edge \(A_0B_1\), direct an arc from \(f^{-1}(B)\) to \(A\). The resulting directed graph \(Q_f\) has ten vertices, twenty arcs and no loops. Directed cycles of \(Q_f\) correspond exactly to \(M_f\)-alternating cycles of \(D\). Any second perfect matching differs from \(M_f\) in a nonempty union of such alternating cycles. Consequently, deleting a set of nonmatching edges isolates \(M_f\) if and only if their corresponding arcs meet every directed cycle: \(\operatorname{af}(D,M_f)\) is the minimum feedback-arc-set cardinality of \(Q_f\).

**3. Exact finite feedback-arc calculation.** An arc subset is acyclic precisely when it admits a linear ordering of its vertices with every retained arc pointing forward. For \(S\subseteq X\), let \(d_f(S)\) denote the maximum number of forward arcs in an ordering of \(S\), counting only arcs with both endpoints in \(S\). The exact recurrence is
\[
 d_f(\varnothing)=0,\qquad
 d_f(S)=\max_{v\in S}\left(d_f(S\setminus\{v\})+
 \#\{u\in S\setminus\{v\}:u\to v\text{ in }Q_f\}\right).
\]
Indeed, in any ordering \(v\) is the last vertex for some \(v\), and exactly the displayed incoming arcs become new forward arcs. Conversely, adjoining \(v\) last achieves the right side. Thus \(\operatorname{af}(D,M_f)=20-d_f(X)\). The complete \(2^{10}\)-subset recurrence gives \(d_{f_6}(X)=15\), \(d_{f_{24}}(X)=14\), and \(d_{f_{30}}(X)=14\), so the anti-forcing numbers are respectively \(5,6,6\). Symmetry transports optimal deletion sets, proving these values for every matching in each orbit.

**4. Identification of the exceptional orbit.** The condition \(f=f^{-1}\) holds exactly for the six bijections of permutation-cycle type \((2,2,2,2,2)\). Each transposition exchanges two disjoint two-subsets, hence is an edge of the Petersen graph. Therefore every such involution is exactly a perfect matching of the Petersen graph, lifted across both layers. The six-element orbit has anti-forcing number five, while both other orbits have six. The polynomial and the stated characterization follow.

## Verification
Run `python3 verify.py` with Python 3.10 or later. The script uses only the standard library and outputs `VERIFY_OK` after the following exhaustive checks: all sixty perfect matchings are enumerated independently by backtracking and a subset-permanent recurrence; all \(240\) explicit \(S_5\times C_2\) actions preserve the graph and matching set; three orbit sizes, cycle types and complementary two-factors are checked; the exact feedback-arc dynamic program runs on every matching; and a **second** exact transversal calculation examines subsets of the twenty nonmatching edges against all fifty-nine competing perfect matchings for each orbit representative, independently confirming both optimum sizes and their lower bounds.

The linear-order recurrence is a finite exhaustive proof for the displayed ten-vertex contracted graphs, not an approximation. All source files needed for the verification are embedded with the statement in its distribution package.

## Relationship to prior work
Lei, Yeh and Zhang introduced the fixed-perfect-matching anti-forcing invariant and proved its alternating-cycle transversal characterization. Their 2014 public preprint treats general bounds and, for plane bipartite graphs, a minimax theorem, but does not state this Desargues-specific three-orbit anti-forcing classification in the inspected introductory and central sections. In particular, the Desargues graph is nonplanar (its girth is six, and a planar cubic bipartite graph on twenty vertices with thirty edges would have twelve faces requiring total facial length at least seventy-two, versus sixty edge-sides), so the plane-bipartite theorem is not directly applicable.

Shi, Zhang and collaborators obtain a general maximum anti-forcing upper bound. At twenty vertices and thirty edges, their bound gives at most ten and does not determine the present values five and six, their multiplicities, or the exceptional orbit. The published existence theorem for arbitrary anti-forcing spectra and the hexagonal-system results likewise do not logically imply the exact invariant for this specific nonplanar graph.

A 2025 published matching-polynomial table for the Desargues–Levi graph gives constant coefficient \(60\), matching the independent perfect-matching count here; that table does not supply any fixed-matching anti-forcing values. (The same article contains a conflicting prose reference to 120, apparently referring to its separate Levi-30 graph table. The actual displayed Desargues row gives 60.)

Previously recorded Desargues perfect-matching reconfiguration results give sixty matchings and a \(6+24+30\) symmetry partition under short alternating-cycle exchanges. Those reconfiguration-adjacency counts do not determine a minimum transversal of *all* alternating cycles. The new assertion is the anti-forcing distribution and its structural exceptional-lift characterization, not the pre-existing number of matchings or orbit partition.

## Limitations
This is an exact statement for one named finite graph, not a formula for an infinite family. Exhaustion works because the graph has only sixty perfect matchings and ten contracted vertices. The full text of Deng and Zhang's 2017 paper on general anti-forcing spectra was not available for inspection; its accessible abstract concerns realizability and hexagonal systems, not a Desargues table. An unindexed prior finite computation or supplementary table remains a residual originality risk. No independent audit has been performed.

## References
1. H. Lei, Y.-N. Yeh, H. Zhang, *Anti-forcing numbers of perfect matchings of graphs*, arXiv:1406.3796v1, first submitted 2014-06-15; later *Discrete Applied Mathematics* 202 (2016), 95–105. https://arxiv.org/html/1406.3796v1
2. L. Shi et al., *Tight upper bound on the maximum anti-forcing numbers of graphs*, arXiv:1704.04124v3. https://arxiv.org/html/1704.04124v3
3. K. Deng, H. Zhang, *Anti-forcing spectra of perfect matchings of graphs*, *Journal of Combinatorial Optimization* 33 (2017), 660–680, DOI:10.1007/s10878-015-9986-3 (accessible abstract; full text not inspected).
4. K. Deng, H. Zhang, *Extremal anti-forcing numbers of perfect matchings of graphs*, arXiv:1607.05392v1 (2016). https://arxiv.org/abs/1607.05392

5. *Matching Polynomials of Symmetric, Semisymmetric, Double Group Graphs, Polyacenes, Wheels, Fans, and Symmetric Solids in Third and Higher Dimensions*, *Symmetry* **17** (2025), article 133; matching-polynomial Table 1, Desargues–Levi row. https://www.mdpi.com/2073-8994/17/1/133
