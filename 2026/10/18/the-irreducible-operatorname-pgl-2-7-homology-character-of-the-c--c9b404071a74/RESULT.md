# The irreducible \(\operatorname{PGL}(2,7)\)-homology character of the Coxeter independence complex

## Finding

Let \(\mathcal L=\{\{j,j+1,j+3\}:j\in\mathbb Z/7\mathbb Z\}\) be the seven lines of the Fano plane (arithmetic modulo seven). Define the Coxeter graph \(C\) on the 28 non-line three-element subsets of \(\mathbb Z/7\mathbb Z\); two vertices are adjacent precisely when the subsets are disjoint. Let \(K=\operatorname{Ind}(C)\). Its full automorphism group is \(G=\operatorname{Aut}(C)\cong\operatorname{PGL}(2,7)\), of order 336.

The reduced integral homology is \(\widetilde H_i(K;\mathbb Z)\cong\mathbb Z^7\) for \(i=6\), and zero for every other integer \(i\). On the rational sixth homology, the natural \(G\)-representation is **absolutely irreducible**. Its complete character is the seven-dimensional character \(\rho_7\) in the standard character table of \(\operatorname{PGL}(2,7)\):

| Conjugacy class | 1 | 2A | 2B | 3 | 4 | 6 | 7 | 8A | 8B |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Class size | 1 | 21 | 28 | 56 | 42 | 56 | 48 | 42 | 42 |
| Homology trace | 7 | -1 | -1 | 1 | -1 | -1 | 0 | 1 | 1 |

The restriction of this homology representation to the order-168 Fano-plane collineation group \(\operatorname{PSL}(2,7)\) is also absolutely irreducible. The full group and its order-168 subgroup both have zero-dimensional fixed homology.

## Assumptions and scope

All graphs are finite, simple and undirected. The Fano incidence system uses the seven three-subsets \(\{j,j+1,j+3\}\) for \(j=0,\dots,6\), with labels read modulo seven. The Coxeter graph has 28 vertices and 42 edges. Homology is reduced simplicial homology of the independence complex, including the empty face in degree \(-1\) for the augmented chain complex. The representation claim is over \(\mathbb Q\), with absolute irreducibility meaning irreducibility after extension of scalars to \(\mathbb C\). No assertion about the isomorphism type of the **integral** \(\mathbb Z[G]\)-lattice is made.

## Proof

**Integral homology.** Order the 28 graph vertices lexicographically as the non-line triples of \(\{0,\dots,6\}\). Represent each independent face by a 28-bit integer. A complete recursion on allowed vertices enumerates 196,009 faces including the empty face; by cardinality, the numbers are

\[ (1,28,336,2268,9506,25788,45836,52928,38556,16660,3752,336,14). \]

Perform a deterministic matching: for each vertex label \(v=0,\dots,27\), match every *currently unmatched* independent face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\), whenever both faces remain unmatched. The construction has exactly 97,999 matched pairs and critical faces comprising eight in degree six, two in degree seven, and one in degree eight. Its associated directed Hasse graph, oriented upward on matched incidences and downward otherwise, is acyclic: the standalone checker exhaustively removes all 196,009 faces by Kahn's topological-sort algorithm. The standard algebraic Morse cancellation theorem therefore applies over \(\mathbb Z\), because each matched incidence coefficient is \(\pm1\).

For an explicit certificate, order the critical degree-six faces by integer masks

`44707840, 52301824, 53030912, 76861440, 85348352, 109457408, 137486336, 202694656`,

the critical degree-seven faces by masks `127275008, 186523648`, and the critical degree-eight face by mask `263331840`. Exact signed cancellation yields the Morse boundary matrices

\[
\partial_7=\begin{pmatrix}
-1&1\\1&-1\\1&-1\\1&-1\\-1&1\\1&-1\\0&0\\0&0
\end{pmatrix},\qquad
\partial_8=\begin{pmatrix}1\\1\end{pmatrix}.
\]

Both maps have integral rank one, their composition is zero, and their nonzero invariant factors are units. Hence the only nonzero reduced integral homology is \(\mathbb Z^7\) in degree six. This is independently established here; an earlier published calculation already reports a wedge of seven six-spheres, and no new nonequivariant homotopy classification is claimed.

**Equivariant Lefschetz calculation.** For \(g\in G\), partition the 28 vertices into cycles of its permutation action. Discard any cycle containing an edge of \(C\); among the remaining cycles, connect two quotient vertices if an original graph edge joins their constituents. Denote this finite incompatibility graph by \(Q_g\), and let \(I(Q_g;t)\) be its ordinary independence polynomial. A \(g\)-fixed independent face is uniquely a union of compatible vertex cycles. If it contains \(r\) such cycles and \(k\) original vertices, the orientation sign is \((-1)^{k-r}\), and its reduced Lefschetz contribution is \((-1)^{r+1}\). Including the empty face therefore gives

\[
\widetilde L(g)=-I(Q_g;-1).
\]

Since reduced homology is concentrated in **even** degree six, \(\widetilde L(g)=\operatorname{tr}(g\mid\widetilde H_6(K;\mathbb Q))\). Exhaustive enumeration of all 336 automorphisms, with an exact signed independence-polynomial recursion on \(Q_g\), produces the following complete grouping by element order:

| Element order | 1 | 2 | 3 | 4 | 6 | 7 | 8 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Number of elements | 1 | 49 | 56 | 42 | 56 | 48 | 84 |
| Trace | 7 | -1 | 1 | -1 | -1 | 0 | 1 |

The two involution classes have the same trace, as do the two order-eight classes. Refining using their known class sizes yields exactly the nine-class table in the finding. A separate implementation computes the signed fixed-face sum **directly over the complete independent-face list**, agreeing for representatives of every possible element order; this does not use the quotient independence-polynomial recursion.

**Irreducibility.** The exact character inner product is

\[
\langle\chi,\chi\rangle_G=\frac{7^2+49+56+42+56+0+84}{336}=1.
\]

For the 168 Fano collineations, an independent enumeration of all permutations of seven labels preserving the set of Fano lines gives

\[
\langle\chi|_{\operatorname{PSL}(2,7)},\chi|_{\operatorname{PSL}(2,7)}\rangle=1.
\]

Both character averages are zero, proving absence of invariant rational homology. The character's class values agree with \(\rho_7\) in the published \(\operatorname{PGL}(2,7)\) character table; this establishes the claimed **identification**, not a new abstract irreducible character.

## Verification

Run `python verify_coxeter.py` with Python 3.10 or later and `networkx` 3.x installed. The supplied standalone checker constructs the graph from the Fano lines; verifies its degrees and edges; enumerates all 196,009 augmented faces; builds 97,999 Morse pairs; topologically sorts the entire matched Hasse graph; derives the exact integral Morse differentials; enumerates all 336 automorphisms and their traces; compares quotient-polynomial and direct signed-face traces on seven representatives; and checks character inner products for the full group and its 168-element Fano collineation subgroup. All listed checks were executed from the actual checker before acceptance. The exact computations are finite exhaustive verifications, not probabilistic numerical samples.

## Relationship to prior work

Coxeter's 1983 paper supplies the exceptional cubic graph and its geometric setting. Barmak (2010) gives general topology of independence complexes, including the triangle-free suspension theorem, not this action on homology. Berghoff (2020) supplies a general homology spectral-sequence method, again not this evaluated character. A publicly indexed 2026 finding reports that the Coxeter graph independence complex is a wedge of seven six-spheres; its nonequivariant conclusion is included as prior knowledge and was independently recomputed above. The known \(\operatorname{PGL}(2,7)\) character table already contains \(\rho_7\), but does not identify it with this independence-complex homology representation. The new part is the **identification of the complete natural homology action** and its irreducibility, including on the Fano subgroup.

## Limitations

The proof identifies only the **rational equivariant** module and independently computes ordinary **integral homology**. It does not classify the integral equivariant lattice, furnish an equivariant wedge decomposition, or establish an infinite family statement. Full text of Coxeter (1983) and of the indexed 2026 Coxeter-complex note was not available during the literature comparison; their accessible abstracts and summaries do not state this homology character, but complete overlap is not ruled out solely by that fact. Unindexed related representations remain a bibliographic risk.

## References

1. H. S. M. Coxeter, *My Graph*, Proceedings of the London Mathematical Society 46 (1983), 117–136, DOI `10.1112/plms/s3-46.1.117`; publisher records publication on 1983-01-01.
2. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1 (2010-07-02), especially §§1–4.
3. M. Berghoff, *On the homology of independence complexes*, arXiv:2008.06267v2 (2020-09-30), especially §§1, 5–6.
4. *The Coxeter graph independence complex is \(\bigvee^7 S^6\)*, publicly indexed published-finding corpus research note, 2026-10-11, record ID `2026/10/11/SCOPE-the-coxeter-graph-independence-complex-is-bigvee-7-s-6--8a1bdfa47e09` (summary available).
5. T. Connor and D. P. Roberts, *GroupNames: Character tables*, entry for \(\operatorname{PGL}(2,7)\), `https://people.maths.bris.ac.uk/~matyd/GroupNames/characters.html` (nine classes and \(\rho_7\)).
