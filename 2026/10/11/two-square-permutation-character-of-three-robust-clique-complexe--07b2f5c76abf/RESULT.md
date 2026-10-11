# Two-square permutation character of three-robust clique complexes of even grids
## Finding
Let \(m=2a\) and \(n=2b\), with integers \(a,b\geq1\), and let \(G=P_m\square P_n\) be the rectangular grid graph. Put \(K=\mathsf{Cliq}_3(G)\), the simplicial complex whose faces are vertex sets containing no independent triple. Let \(H=\langle h,v\rangle\cong C_2\times C_2\), where \(h\) reverses the row coordinate and \(v\) reverses the column coordinate. Let \(Q\) be the set of elementary unit-square cells of the grid and \(t=|Q|=(m-1)(n-1)\).

**Theorem.** There is an isomorphism of rational \(H\)-modules
\[
\widetilde H_3(K;\mathbb Q)\cong\mathbb Q\bigl[\binom Q2\bigr],
\]
where the right side is the permutation module on the unordered pairs of distinct elements of \(Q\). For every \(i\ne3\), \(\widetilde H_i(K;\mathbb Q)=0\). The assertion is an abstract module isomorphism; it does not specify a canonical basis of homology classes indexed by pairs of squares.

Writing \(z=hv\), its complete character on \(H\) is
\[
\begin{aligned}
\chi(1)&=\binom{(m-1)(n-1)}2,\\
\chi(h)&=\frac{(n-1)(m+n-4)}2,\\
\chi(v)&=\frac{(m-1)(m+n-4)}2,\\
\chi(z)&=\frac{mn-m-n}{2}.
\end{aligned}
\]
For \(\varepsilon,\delta\in\{-1,1\}\), the one-dimensional character on which \(h\) acts by \(\varepsilon\) and \(v\) by \(\delta\) occurs with multiplicity
\[
\frac{\chi(1)+\varepsilon\chi(h)+\delta\chi(v)+\varepsilon\delta\chi(z)}4.
\]
For example, on the \(4\times6\) grid the rank is \(105\), the character values are \((105,15,9,7)\), and the multiplicities corresponding to \((\varepsilon,\delta)=(+,+),(+,-),(-,+),(-,-)\) are \(34,26,23,22\).

## Assumptions and scope
The paths have exactly \(m\) and \(n\) vertices; row and column indices run from \(0\) to \(m-1\) and \(0\) to \(n-1\), respectively. The edge relation is Manhattan distance one. A three-robust clique face means **no independent three-element subset** of the induced graph. The action on an oriented face is the usual signed vertex permutation. The source theorem supplying the homology concentration is Filakovský's Theorem 1 for \(k=3\); that theorem applies to every grid with \(m,n\ge2\). Evenness is imposed here to obtain the fixed-point-free reflection actions used in the new character calculation.

## Proof
**1. Faces of bounded size.** The grid is bipartite, so every five-vertex subset contains three vertices in one bipartition class and hence an independent triple. Thus \(K\) has dimension at most three. Every pair is a face; a triple is a face exactly when it contains a graph edge. By König's equality between the independence number and the complement of the maximum matching number in a bipartite graph, a four-vertex set is a face exactly when its induced graph admits a perfect matching. This criterion will be applied only to sets of four distinct vertices.

**2. Fixed-simplex trace.** Each nonidentity element \(g\in H\) is a fixed-point-free involution on the \(mn\) grid vertices, because both side lengths are even. Its vertex-orbits are \(q=mn/2\) two-element sets. A nonempty \(g\)-stable simplex consists of one such orbit or of two orbits. Every one-orbit set is a face. Let \(P_g\) count unordered pairs of different orbits whose union admits a perfect matching. The augmented simplicial Lefschetz supertrace on reduced chains equals
\[
-1+q-P_g,
\]
since a union of \(j\) two-element orbits has orientation sign \((-1)^j\) and simplicial degree \(2j-1\). The same supertrace is \(-\chi(g)\), because Filakovský's grid theorem places all reduced rational homology in degree three. Therefore
\[
\chi(g)=1-q+P_g. \tag{1}
\]
There is no reliance on any cancellation not justified by the chain-map trace identity.

**3. A single-coordinate reflection.** For \(h\), choose representatives in the first \(a=m/2\) rows. The quotient orbit graph, ignoring loops, is \(J=P_a\square P_n\). If two orbit representatives are adjacent in \(J\), their two reflected grid edges form a perfect matching across the combined orbits. In addition, any two representatives in row \(a-1\) give a perfect matching using the two edges that cross the central row-reflection axis. There are no other perfect matchings: without internal orbit edges every perfect matching needs a crossing between the two orbits, hence a quotient adjacency, and internal orbit edges occur only for the central representatives. The two classes overlap in the \(n-1\) neighboring pairs of central-row representatives. Consequently,
\[
P_h=((a-1)n+a(n-1))+\binom n2-(n-1).
\]
Substituting \(q=an\) into (1) and simplifying yields
\[
\chi(h)=\frac{(n-1)(m+n-4)}2.
\]
Interchanging coordinates gives \(\chi(v)=(m-1)(m+n-4)/2\).

**4. The half-turn.** The half-turn \(z=hv\) preserves the bipartition coloring: its changes of both coordinate indices have odd parity, so their total parity is even. Every orbit therefore consists of two vertices of the same color. A pair of distinct orbits spans a perfect-matching four-set if and only if there is at least one grid edge between those orbits; any such edge and its half-turn image are disjoint and constitute a perfect matching. Every grid edge belongs to a two-edge orbit under \(z\), so there are \(|E(G)|/2\) edge-orbits. Exactly **one** unordered pair of vertex-orbits is joined by two different edge-orbits: the two opposite-vertex pairs of the unique central \(2\times2\) square. Indeed, if an orbit pair were joined in two ways, a vertex would neighbor both a point and its half-turn image. Their graph distance would be at most two; as both coordinate displacements are positive odd integers, each must equal one, forcing the central square. With
\[
|E(G)|=(m-1)n+m(n-1),
\]
it follows that
\[
P_z=\frac{|E(G)|}{2}-1,
\quad \chi(z)=1-\frac{mn}{2}+P_z=\frac{mn-m-n}{2}.
\]

**5. Identification with the two-square permutation module.** In the reflection action on the \(t=(m-1)(n-1)\) elementary squares, \(h\) fixes precisely the \(n-1\) central-row squares. A fixed unordered pair of squares is either a pair of individually fixed squares or one transposed two-square orbit. Hence the trace on \(\mathbb Q[\binom Q2]\) at \(h\) is
\[
\binom{n-1}{2}+\frac{t-(n-1)}2
=\frac{(n-1)(m+n-4)}2.
\]
The formula for \(v\) is symmetric. The half-turn fixes exactly the central elementary square, hence has \((t-1)/2=(mn-m-n)/2\) fixed pairs. The identity trace is \(\binom t2\). These four traces coincide with the homology character. Over \(\mathbb Q\), all irreducible representations of \(C_2\times C_2\) are the four one-dimensional sign characters, and characters determine semisimple modules. The claimed rational-module isomorphism and the Fourier multiplicity formula follow.

## Verification
Run `python3 verify_grid_reflections.py` with Python 3 standard library. The checker builds grid faces from the forbidden independent-triple definition; independently tests the equivalent perfect-matching criterion on four-element faces; computes signed augmented simplicial traces directly; enumerates vertex orbit unions for reflection traces; and calculates exact mod-two boundary ranks on small grids. Its completed execution produced `VERIFY_OK reflection_characters 48 tetrahedra 387 direct_signed_trace_cases 15 independent_mod2_homology_cases 6`. Among the grids checked by boundary rank was the \(4\times4\) grid, with mod-two Betti numbers \((0,0,0,36)\). These experiments independently check bounded cases and **do not prove** the theorem for arbitrary even side lengths; the five uniform arguments above supply the proof.

## Relationship to prior work
M. Filakovský, *The Topology of \(k\)-Robust Clique Complexes in Grid-like Graphs* (arXiv:2602.11365, originally public February 11, 2026), Theorem 1, establishes the ordinary homotopy type \(K\simeq\bigvee^{\binom{(m-1)(n-1)}2} S^3\), including the reduced-homology concentration used here. The full text treats homotopy types by combinatorial decompositions, without the character of the grid-reflection group. Earlier work on total cut and cut complexes of grids, including arXiv:2408.07646, likewise treats homotopy types rather than the four reflection traces. Those results determine the identity trace but do not determine the other three character values. The present result supplies all four, and thereby the complete rational reflection representation; it is not a reinterpretation of Betti numbers as an equivariant theorem.

## Limitations
This theorem treats even-by-even grids. On square grids, only the specified subgroup \(H\) is analyzed, not the additional coordinate-interchange symmetries. It neither constructs a canonical square-pair-indexed homology basis nor claims an integral module isomorphism or an equivariant homotopy equivalence. The existing homotopy-type theorem is an externally established premise; finite computation alone would not justify it. Undiscovered equivalent representation calculations remain possible.

## References
1. M. Filakovský, *The Topology of \(k\)-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365 (v1 February 11, 2026; full-text v4 August 10, 2026), Theorem 1 and proof in Section 3. https://arxiv.org/html/2602.11365
2. P. Chandrakar, A. Hazra, J. K. Rout, and A. Singh, *Topology of total cut complexes and cut complexes of grid graphs*, arXiv:2408.07646, Sections 1–4. https://arxiv.org/html/2408.07646v3
