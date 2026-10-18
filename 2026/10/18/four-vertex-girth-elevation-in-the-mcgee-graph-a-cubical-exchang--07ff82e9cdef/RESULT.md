# Four-vertex girth elevation in the McGee graph: a cubical exchange component and four frozen optima

## Finding

The unique cubic \((3,7)\)-cage, the McGee graph \(M\), admits a vertex set of size four meeting every shortest cycle, and no smaller vertex set has this property. There are exactly twenty such optimal sets. Under one-vertex replacement, their exchange graph is \(Q_4\sqcup4K_1\): sixteen configurations form a four-dimensional cube, and the other four cannot be changed by a single optimal exchange. Deleting any of the twenty sets raises girth from seven to **exactly eight**.

The four-cube structure is a classification of feasible solutions, not merely a count. In particular, the graph contains both movable and frozen optimal ways to eliminate all of its shortest cycles.

## Assumptions and scope

All graphs are finite, simple and undirected. Label the vertices of \(M\) by \(\mathbb Z/24\mathbb Z\). Include cycle edges \(\{i,i+1\}\) modulo twenty-four, and for each \(i\) add the chord \(\{i,i+d_i\}\), where \((d_0,\ldots,d_{23})=(12,7,-7)^8\). Since the chords are counted without orientation, this is the usual \((-12,7,-7)^8\) LCF representation. It has twenty-four vertices and thirty-six edges, each vertex of degree three, and girth seven.

A *seven-cycle transversal* is a set \(S\subseteq V(M)\) such that \(S\cap V(C)\ne\varnothing\) for every simple seven-cycle \(C\) of \(M\). Equivalently, \(g(M-S)>7\), since \(M\) has girth seven. Only shortest cycles, **not every cycle**, must be hit. Let \(\tau_7(M)\) be its minimum size. The *optimal exchange graph* has one vertex per seven-cycle transversal of cardinality \(\tau_7(M)\), and edges join sets whose intersection has cardinality \(\tau_7(M)-1\).

Define four disjoint pairs
\[
P_1=\{0,12\},\quad P_2=\{3,15\},\quad
P_3=\{6,18\},\quad P_4=\{9,21\}.
\]
Let \(\mathcal A\) consist of the sixteen sets \(\{p_1,p_2,p_3,p_4\}\) with \(p_j\in P_j\). Let \(\mathcal B\) comprise
\[
\{1,5,13,17\},\quad\{2,10,14,22\},\quad
\{4,8,16,20\},\quad\{7,11,19,23\}.
\]

## Proof

**Short-cycle incidence and lower bound.** Root a simple cycle at its least numbered vertex and require its second vertex to be smaller than its final vertex. A complete depth-first enumeration to length seven finds no shorter cycle and exactly thirty-two distinct seven-cycles. The eight vertices divisible by three each occur in ten of these cycles; each of the other sixteen occurs in nine. The aggregate incidence check is \(8\cdot10+16\cdot9=32\cdot7=224\). Thus any three vertices hit at most thirty of the thirty-two seven-cycles, establishing \(\tau_7(M)\ge4\).

**Complete optimum classification.** For each of the \(\binom{24}{4}=10626\) four-element subsets \(S\), compare its binary incidence mask to every one of the thirty-two cycle masks. The condition that every bitwise intersection is nonzero is logically equivalent to hitting every shortest cycle. The exhaustive finite comparison returns precisely \(\mathcal A\cup\mathcal B\), consisting of twenty sets. The complete enumerator, all assumptions, reconstruction of the graph, and assertions against the explicit classification are supplied as `verify_cycles.py`. This is a finite exhaustive argument over the whole declared search space, not a sampling argument. The existence of these sets proves \(\tau_7(M)\le4\), hence equality.

**Exchange graph.** Each member of \(\mathcal A\) chooses one of the two vertices in each \(P_j\). Two such sets share three vertices exactly when their four binary choices differ in one coordinate. Therefore the induced exchange graph on \(\mathcal A\) is \(Q_4\), with sixteen vertices and thirty-two edges. Any two distinct members of \(\mathcal B\), or one member of \(\mathcal B\) and one of \(\mathcal A\), have fewer than three vertices in common. Thus each of the four members of \(\mathcal B\) is isolated, proving \(Q_4\sqcup4K_1\).

**Resulting girth.** An independent breadth-first shortest-cycle calculation checks \(g(M-S)=8\) for all twenty classified sets. It also checks that every one of the \(\binom{24}{3}=2024\) three-element deletions still leaves girth seven, and independently recovers the same twenty sets and exchange components. This complete second algorithm is `verify_deletion.py`. It requires no cycle list produced by the first algorithm.

## Verification

Run `python3 verify_cycles.py` and `python3 verify_deletion.py` in any Python installation supporting the standard library. Expected exact stdout is in `verify_cycles.out` and `verify_deletion.out`; both end with `VERIFY_OK`. The first enumerates all simple cycles of length at most seven and all four-subsets, and derives the lower bound from cycle incidences. The second examines girth of every three- and four-vertex deletion by a distinct breadth-first method. Both independently reconstruct the labeled graph from its chord formula.

The finite proof requires the correctness of the short, readable routines `extend`, `girth_after`, and the complete `combinations(range(24),4)` traversal. The scripts are part of the finding; the recorded outputs are not substituted for executable evidence. No claim is made for other cages or arbitrary cubic graphs.

## Relationship to prior work

McGee constructed a smallest cubic graph of girth seven in 1960. Exoo and Jajcay's *Dynamic Cage Survey* (first publicly released 29 September 2008; Section 2.1.3 of the accessible 2013 full version) records its twenty-four vertices, its two vertex orbits, and the size of its automorphism group. Those graph-identification facts are established and not claimed as new. Kortsarz, Langberg and Nutov study edge transversals for prescribed cycle lengths in general graphs and obtain approximation theorems; their definition removes **edges**, whereas the present theorem deletes **vertices** and classifies all exact optimal configurations for one cage. Neither the examined cage survey nor the full relevant definitions and main theorems of the edge-transversal work state this twenty-set vertex classification or its optimal exchange geometry.

The additional contribution is the exact vertex girth-elevation optimum and its mixed mobile/frozen solution landscape. This cannot be inferred merely from the named graph's order, degree, girth, or two automorphism orbits. Other studies of the McGee graph's independence complex concern a different invariant and do not imply an exact seven-cycle transversal classification.

## Limitations

The result is restricted to this twenty-four-vertex labeled cage; it is not a general formula for cages. Exhaustive finite verification constitutes a proof only because all relevant cycles and all candidate four-vertex sets are covered. The oldest construction paper's complete text was not accessible in this review; an overlooked enumeration, unpublished computation, or unindexed table could overlap. No claim of publication priority or independent external validation is made. If all seven-cycles are removed, longer cycles remain: none of the twenty optimal transversals is asserted to be a feedback vertex set.

## References

1. W. F. McGee, *A Minimal Cubic Graph of Girth Seven*, Canadian Mathematical Bulletin 3 (1960), 149–152, doi:10.4153/CMB-1960-018-1.
2. G. Exoo and R. Jajcay, *Dynamic Cage Survey*, Electronic Journal of Combinatorics, Dynamic Survey DS16, first published 2008-09-29, doi:10.37236/37; accessible version 3 (2013), Section 2.1.3.
3. G. Kortsarz, M. Langberg and Z. Nutov, *Approximating Maximum Subgraphs without Short Cycles*, SIAM Journal on Discrete Mathematics 24 (2010), 255–269, doi:10.1137/09074944X. The available full-text author copy treats edge-cycle transversals.
4. E. W. Weisstein, *McGee Graph*, MathWorld, https://mathworld.wolfram.com/McGeeGraph.html (standard LCF identification).
