# One-defect rigidity and exact counts of optimal burning sequences on paths and cycles

## Finding

For every integer \(k\ge2\), let \(P_n\) and \(C_n\) be respectively the labelled path and labelled cycle on \(n\) vertices. An *optimal burning sequence* is a time-ordered tuple of vertices \((v_1,\ldots,v_k)\) which burns the entire graph in the minimum possible \(k\) rounds, with each ignition chosen among vertices unburned at the end of the preceding round. A last ignition is *redundant* when it would also catch fire from propagation during its own round.

For both graph families, at either of the two orders \(n=k^2\) or \(n=k^2-1\), the burning number is exactly \(k\). Let \(B(G)\) count distinct ordered optimal burning sequences and \(R(G)\) those whose last ignition is redundant. Then the exact values are

\[
\begin{array}{c|c|c}
G & B(G) & R(G)\\ \hline
P_{k^2}&k!&0\\
C_{k^2}&k^2(k-1)!&0\\
P_{k^2-1}&(k-1)(k+2)(k-1)!&2(k-1)(k-1)!\\
C_{k^2-1}&(k^2-1)k!&2(k^2-1)(k-1)!
\end{array}
\]

Thus the proportions of optimal sequences with a redundant last ignition at the first sub-square order are exactly \(2/(k+2)\) for paths and \(2/k\) for cycles. They vanish completely at the square order. These counts are for actual, non-repeating, legally timed ignitions, not relaxed vertex tuples which permit already burned sources.

The structural statement is sharper than the counts: at the square order, the final burning neighborhoods form a partition of the path/cycle into arcs of the prescribed odd sizes; at one below the square, the **only** possibilities are a one-vertex truncation at one end of a path, or a single shared endpoint of two arcs. On a cycle only the shared-endpoint case occurs. The redundant-last sequences are exactly the shared-endpoint arrangements in which the one-vertex final neighborhood participates in that overlap.

## Assumptions and scope

Graphs are finite, simple, undirected, and vertex-labelled: \(P_n\) has vertices \(0,\ldots,n-1\) in order; \(C_n\) has those vertices cyclically, where \(n\ge3\). We fix \(k\ge2\) and \(n\in\{k^2-1,k^2\}\). At round \(i\), a still-unburned vertex \(v_i\) is selected first, then fire propagates from vertices burned at the end of round \(i-1\). The selected vertex may also catch fire by that propagation during round \(i\) (a redundant ignition). A legal burning sequence satisfies \(d(v_i,v_j)\ge j-i\) whenever \(i<j\), and every vertex is within distance \(k-i\) of at least one \(v_i\). Sources are necessarily distinct. No quotient by path reversal or cycle dihedral symmetry is taken.

Write \(r_i=k-i\), \(\ell_i=2r_i+1\), and \(I_i=N_{r_i}[v_i]\). On a path, \(I_i\) is the intersection with the path of an integer interval of ideal length \(\ell_i\); on a cycle, \(I_i\) is a cyclic interval of length \(\ell_i\). Since \(\sum_i\ell_i=k^2\) and \(2k-1\le n\), the latter assertion also holds at the small boundary \(k=2,n=3\).

## Proof

**1. Optimal length.** A single ignition at round \(i\) reaches at most \(2(k-i)+1\) vertices by the end of round \(k\), on either a path or a cycle. Hence \(k-1\) rounds cover at most \((k-1)^2\) vertices, strictly fewer than either allowed \(n\). Conversely, the arc arrangements constructed below cover all \(n\) vertices in \(k\) legal rounds. Therefore the burning number equals \(k\).

**2. Capacity and one-defect rigidity.** Put \(t_i=\ell_i-|I_i|\), the number of ideal interval vertices truncated by the ends of the path (always zero on a cycle), and let \(q=\sum_i|I_i|-n\) be the overlap multiplicity, counting each vertex covered \(s\) times with excess \(s-1\). For any burning sequence, the intervals cover all vertices, so

\[
\sum_i t_i+q=k^2-n\in\{0,1\}.
\]

At \(n=k^2\), each term is zero: there is no truncation or overlap, and the intervals tile the path or cycle. At \(n=k^2-1\), precisely one of the nonnegative integers equals one. If there is truncation, it must be a one-vertex loss at precisely one path endpoint, and the intervals are otherwise disjoint. If there is overlap, there is exactly one vertex belonging to two intervals, with no truncation. For two positive-radius intervals this intersection must be their common endpoint; otherwise an intersection of at least two vertices would occur. The sole radius-zero interval is \(I_k=\{v_k\}\). If it were strictly inside a positive-radius interval \(I_i\), then \(d(v_i,v_k)<r_i=k-i\), contradicting legality. Therefore its possible overlap is also at an endpoint. An arrangement without gaps consequently has a unique left-to-right order on a path, or unique clockwise cyclic order on a cycle (with fixed graph labelling and orientation), and at most one overlap junction. The cyclic assertion includes \(C_3\): its radius-one neighborhood has the unique clockwise three-vertex order centred on its ignition.

**3. All indicated arrangements are realizable.** Take the \(k\) intervals of respective odd lengths \(\ell_1,\ldots,\ell_k\). On a path, lay them in any order edge-to-edge, either with no defect, with exactly one common endpoint at a selected junction, or with one endpoint interval protruding by one vertex beyond the host path. A protrusion is possible only when that endpoint interval has positive radius. On a cycle, put them in any circular order, either edge-to-edge or with one common endpoint at a chosen junction. The center of the interval labelled \(i\) is the proposed round-\(i\) ignition. By construction all vertices are covered.

For any two distinct ignition centers labelled \(i<j\), a path through the arcs in either relevant direction travels from the first center to a boundary of its arc and from a boundary of the other arc to its center. The center distance is therefore at least \(r_i+r_j\); the only permissible shared boundary can save one unit from the disjoint-arc distance \(r_i+r_j+1\). This holds for both directions on a cycle, including the boundary \(C_3\). Hence

\[
d(v_i,v_j)\ge r_i+r_j=2k-i-j\ge j-i,
\]

since \(j\le k\). Every such arrangement is a legal burning sequence. Together with Step 2, this is an exact bijection between configurations and valid sequences.

**4. Enumeration at capacity.** A path tiling is determined by a permutation of its \(k\) distinctly labelled intervals, giving \(k!\) sequences. On a labelled cycle, anchor the interval of label \(1\) at any of the \(n\) possible starting vertices (with a fixed clockwise orientation), then order the other \(k-1\) labelled intervals. This gives \(n(k-1)!\) sequences, with \(n=k^2\). No last ignition is redundant because the intervals are disjoint.

**5. Enumeration at one defect.** For a path, a one-vertex overlap is specified by a permutation and one of its \(k-1\) junctions, contributing \(k!(k-1)\). To truncate by one at the left endpoint, the first interval must have positive radius: choose its label in \(k-1\) ways and order all others in \((k-1)!\) ways. The same holds at the right endpoint, contributing \(2(k-1)(k-1)!\) truncation configurations. Their sum is

\[
k!(k-1)+2(k-1)(k-1)!=(k-1)(k+2)(k-1)!.
\]

On a cycle, a defect must be one overlap. Choose the start vertex of the anchored first interval (\(n\) choices), the circular order of the remaining intervals (\((k-1)!\) choices), and one of the \(k\) cyclic junctions to overlap. This gives \(nk!\), with \(n=k^2-1\). The two junctions on \(C_3\) distinguish the two possible terminal ignition positions and are not double counted.

**6. Redundancy.** Legality of the final source gives \(d(v_i,v_k)\ge k-i=r_i\) for each earlier source. It is redundant exactly when at least one of these is an equality, because then fire from an earlier source reaches a neighbor of \(v_k\) by the preceding round. Equivalently, its singleton final neighborhood is the unique overlapping interval. In a path permutation, the singleton is incident to one junction when at an endpoint of the interval order and two when internal. Across all \(k!\) permutations the number of incident junction choices is \(2(k-1)(k-1)!\). For a cycle every circular order has exactly two junctions incident to the singleton, so there are \(2n(k-1)!\) such sequences. No truncated configuration is redundant. At capacity no overlap can exist. This proves every displayed count and proportion.

## Verification

The accompanying standalone `verify.py` uses two independently specified constructions. One enumerates all tuples of possible ignition vertices for both path and cycle for \(k=2,3,4\), performing the original round-by-round propagation and refusing an ignition already burned at the previous round. The other generates the exact interval arrangements from the proof and checks distinctness, legality and terminal redundancy. The direct and constructive counts agree with the stated formulas in every one of the 12 small cases. Additional constructive tests cover \(k=5,6\) for both families and both orders. Execute `python3 verify.py` (Python standard library only), and require the terminal line `VERIFY_OK`. Finite tests are corroboration, not the proof for unbounded \(k\).

## Relationship to prior work

The usual path/cycle burning-number identity \(b(P_n)=b(C_n)=\lceil\sqrt n\rceil\) and the equivalent covering-by-radius-neighborhoods model are established in earlier literature. The present work does not claim these bounds as new. Abiad and Mallee (2026) give the legal-sequence characterization in their Theorem 2.4, use existence of a redundant final source in their Proposition 4.4, and note that square-order paths cannot have a redundant last source. Those statements do not supply the exact enumerations or the one-defect structural classification above. Recent mixed-integer-programming and graph-burning work treats shortest-length optimization rather than the number and redundancy profile of all optimal solutions. The new content here is the complete one-defect classification, the four enumerators, and the exact redundant-last subcounts. Earlier and unindexed enumeration under different terminology remains a historical-priority risk.

## Limitations

The statements concern labelled, time-ordered, legally chosen sources on paths and cycles at exactly the two orders \(k^2\) and \(k^2-1\). They do not count relaxed source tuples that permit igniting previously burned vertices, do not classify other graph families, and do not give counts at deficits of two or more. The proof is self-reviewed; no independent mathematical audit or comprehensive priority certification has occurred.

## References

1. A. Abiad and P. Mallee, *Propagation processes on (hyper)graphs: where zero forcing and burning meet*, arXiv:2602.13149v1 (first posted 2026-02-13), subsequently *Annals of Combinatorics* (2026), DOI 10.1007/s00026-026-00820-2. Particularly Theorem 2.4, Proposition 4.4, and the following square-order path discussion. https://arxiv.org/abs/2602.13149
2. A. Bonato, *A survey of graph burning*, *Contributions to Discrete Mathematics* 16 (2021), DOI 10.55016/ojs/cdm.v16i1.71194. https://cdm.ucalgary.ca/article/view/71194
3. F. de Carvalho Pereira, P. J. de Rezende, T. Yunes, and L. F. B. Morato, *A Row Generation Algorithm for Finding Optimal Burning Sequences of Large Graphs*, ESA 2024, DOI 10.4230/LIPIcs.ESA.2024.94. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2024.94
4. N. Prado and R. Colares, *Dominance and symmetry-breaking rules for the Graph Burning Problem*, arXiv:2606.10966v2 (2026-06-10). https://arxiv.org/abs/2606.10966
