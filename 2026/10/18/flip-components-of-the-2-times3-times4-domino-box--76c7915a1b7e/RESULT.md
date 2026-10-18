# Flip components of the \(2\times3\times4\) domino box

## Finding

Let \(B\) consist of the twenty-four unit cubes with integer coordinates \((i,j,k)\), where \(0\le i<2\), \(0\le j<3\), and \(0\le k<4\). Let \(\mathcal T(B)\) be its coverings by twelve face-adjacent dominoes. The **flip graph** \(\mathcal F(B)\) joins two tilings when two parallel dominoes filling a \(2\times2\times1\) slab are replaced by the other parallel pair, in any of the three orientations.

The exact finite classification is
\[
|V(\mathcal F(B))|=1845,\qquad |E(\mathcal F(B))|=6949,
\qquad \mathcal F(B)\cong G_0\sqcup4P_5.
\]
Here \(P_5\) is a path on five vertices and \(G_0\) is connected with \(1825\) vertices and \(6933\) edges. The four path components lie in a single orbit under the coordinate-reflection symmetries of the box. **Every tiling has at least one legal flip**, despite the five disconnected components.

The large component has radius \(10\) and diameter \(16\). Its eccentricity distribution, listed as \((\text{eccentricity}:\text{number of vertices})\), is
\[
(10:100),\ (11:1041),\ (12:473),\ (13:163),\ (14:32),\ (15:10),\ (16:6).
\]
Each path component has radius \(2\) and diameter \(4\). These are exact claims about this fixed box only.

## Assumptions and scope

The unit cubes are distinct labeled positions; dominoes are *unoriented* unordered pairs of cubes sharing a face. Tilings differing only in the order in which dominoes are listed count as the same tiling. The box has ordinary, nonperiodic boundary conditions. A flip is possible only on a complete axis-aligned four-cube unit square; trits, extra volume, and intermediate nontilings are not permitted.

The associated grid graph has \(24\) vertices, \(46\) edges, and \(29\) elementary four-cycles. A tiling is a perfect matching in that graph. There is no claim about boxes of arbitrary dimensions, and no claim that all disconnectedness of three-dimensional tilings is newly discovered.

## Proof

**Exhaustion of the vertices.** Label the cubes by the lexicographic triples \((i,j,k)\). Given a partially selected matching, take the first cube not yet covered and branch over every face-adjacent *uncovered* neighbor. Add their domino and recurse. At each recursive call the number of uncovered cubes decreases by exactly two. Every full tiling belongs to one branch because its domino covering the first uncovered cube is unique; distinct branches cannot produce the same tiling. Thus the recursion terminates and produces each perfect matching exactly once. The exact output contains \(1845\) distinct perfect matchings.

Independently, divide the box into four \(2\times3\) floors. For incoming occupied positions \(U\) and outgoing positions \(W\), let \(m(U,W)\) count the completions of the remaining positions of one floor by horizontal dominoes and outgoing half-dominoes, forbidding outgoing half-dominoes on the last floor. Start with \(F_0(\varnothing)=1\) and use
\[
F_{r+1}(W)=\sum_U F_r(U)m(U,W),\qquad 0\le r<4.
\]
The final value \(F_4(\varnothing)=1845\) agrees with the direct enumeration. The transfer and direct enumerator have separate recursions and cell representations.

**Exact flip adjacency.** Enumerate the \(29\) elementary four-cycles of the rectangular grid. In each possible tiling, replacing either pair of opposite cycle edges by the other pair gives precisely one legal flip. Conversely, if two perfect matchings have symmetric difference consisting of exactly four edges, those edges form a single alternating four-cycle: every vertex of their symmetric difference has degree two and every alternating cycle has length at least four. Every four-cycle in this nonperiodic orthogonal grid is an elementary square. Hence the rule 'the edge sets differ in exactly four elements' is an independent *if and only if* test for adjacency. Both tests give the same set of \(6949\) undirected flip edges.

**Components and distances.** A full breadth-first traversal of the resulting finite adjacency lists gives component orders \(1825,5,5,5,5\). The large component has \(6933\) edges, and each small one has four. Within each small component the degrees are \(1,1,2,2,2\); connectedness and this degree sequence imply it is exactly \(P_5\). The minimum degree over all \(1845\) states is one, proving the absence of frozen tilings. Reversing any subset of the three coordinate axes induces a graph automorphism; applying the eight such reflections to one small component reaches all four small components.

For every vertex of the large component, breadth-first search assigns distances successively by \(d(s)=0\) and \(d(v)=1+\min_{u\sim v}d(u)\) at first discovery. All \(1825\) vertices are reached from each source. The resulting eccentricity counts are those in the Finding; their minimum and maximum are \(10\) and \(16\). As an additional complete finite check, the numbers of unordered vertex pairs at distances \(1,\ldots,16\) are
\[
(6933,28954,82937,175354,281394,345558,324438,231738,
124562,48770,12096,1325,278,47,12,4).
\]
They sum to \(\binom{1825}{2}=1664400\), so no pair was omitted. Every enumeration boundary is explicitly finite and covered by the supplied executable certificate.

## Verification

Run `python3 verify_box_flips.py` in the same directory as this file. Only the Python standard library is needed; a successful run prints `verification: PASS`. The companion `verification_output.txt` records one successful full execution. The checker contains a direct perfect-matching generator, an independent six-cell transfer count, an elementary-square flip generator, a symmetric-difference flip test over every pair of tilings, component and symmetry checks, and an all-source shortest-path verification of the main component. Its assertions check every displayed numerical result, not merely aggregate log messages.

## Relationship to prior work

Milet and Saldanha introduced the three-dimensional flip and polynomial invariants and proved that nontrivial rectangular boxes need not be flip-connected [1]. That established disconnectedness is *not* new here. Their explicit small-box component table concerns the \(3\times3\times2\) example and a separate \(7\times3\times2\) example, rather than the above complete graph metric [1].

Saldanha later used a \(2\times3\times4\) subbox explicitly as a **generator construction for the domino group** [2, Section 9, Lemma 9.2]. Thus the box itself and certain distinguished tilings have definitely appeared previously. The group-theoretic assertions do not give the full \(1845\)-state, five-component, \(4P_5\) metric classification at fixed volume. The theorem about connectivity after refinement [3] concerns another equivalence relation, and the later survey [4, Section 3] tabulates the \(3\times3\times2\) and \(4\times4\times4\) boxes but does not present this finite metric. The originality claim is solely for this exact fixed-volume classification, subject to the limitations below.

## Limitations

The proof is an independently checkable exhaustive finite computation, not a closed symbolic formula or an infinite-family theorem. The checker is still software and has not undergone independent external validation. Web-indexed and database searches cannot establish absolute priority: equivalent unpublished enumerations, code repositories, or unindexed tables may exist. The four exceptional components have a symmetry classification, but no separate identification of their polynomial flip invariants is claimed. No assertion is made about flip-plus-trit accessibility.

## References

1. P. H. Milet and N. C. Saldanha, *Flip invariance for domino tilings of three-dimensional regions with two floors*, arXiv:1404.6509 (first public version 25 April 2014), Sections 1 and 6. https://arxiv.org/abs/1404.6509
2. N. C. Saldanha, *Domino tilings of cylinders: the domino group and connected components under flips*, arXiv:1912.12102 (first public version 27 December 2019), Section 9. https://arxiv.org/abs/1912.12102
3. J. Freire, C. J. Klivans, P. H. Milet and N. C. Saldanha, *On the connectivity of spaces of three-dimensional domino tilings*, arXiv:1702.00798 (first public version 2 February 2017), Theorem 1. https://arxiv.org/abs/1702.00798
4. C. J. Klivans and N. C. Saldanha, *Domino tilings beyond 2D*, arXiv:2507.22625 (first public version 30 July 2025), Section 3. https://arxiv.org/abs/2507.22625
