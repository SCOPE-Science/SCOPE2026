# Thirteen linear families of minimum zero-forcing sets in cycle prisms

## Finding
For every integer \(n\ge 6\), put \(P_n=C_n\square K_2\), the circular ladder or ordinary prism on \(2n\) vertices. Its zero forcing number is \(4\) (previously known). The exact number of minimum zero forcing sets is \(13n\), falling into five disjoint orbits under the prism's dihedral and layer-exchange symmetries, of sizes \(n,2n,2n,4n,4n\). The one-vertex exchange graph of these sets is **connected**, has \(13n\) vertices and \(48n\) edges, and has degree-enumerator
\[
D_n(t)=nt^{12}+8nt^8+4nt^5.
\]
Thus the fourth zero-forcing-polynomial coefficient is \(13n\), and the exchange graph is nonregular, with precisely three degrees \(5,8,12\).

## Assumptions and scope
All graphs are finite, simple, and undirected. For \(n\ge6\), label vertices \(T_i\) and \(B_i\), where \(i\in\mathbb Z/n\mathbb Z\). Edges are \(T_iT_{i+1}\), \(B_iB_{i+1}\), and \(T_iB_i\). Starting from a set \(S\) of black vertices, a black vertex with exactly one white neighbor may force that neighbor black. The set \(S\) is zero forcing if these moves can make every vertex black. A *minimum* set has cardinality \(Z(P_n)\). Exchange adjacency means symmetric difference of size two, without any restriction on the distance between the two exchanged original vertices.

The five orbit representatives are:

1. \(Q=\{T_0,T_1,B_0,B_1\}\);
2. \(X=\{T_0,T_1,B_0,B_{-1}\}\);
3. \(H=\{T_0,T_1,T_2,T_3\}\);
4. \(A=\{T_0,T_1,T_2,B_0\}\);
5. \(Y=\{T_0,T_1,T_3,B_1\}\).

Take their translates, reflected translates, and layer swaps, always modulo \(n\). These are *all* minimum sets, without further identifications between the five orbits. Their sizes and exchange degrees in the displayed order are \((n,2n,2n,4n,4n)\) and \((12,8,8,8,5)\).

## Proof
**1. Fort characterization.** A *fort* is a nonempty set \(F\) of vertices such that each vertex outside \(F\) has either zero or at least two neighbors in \(F\). A set \(S\) is zero forcing if and only if it meets every fort. Indeed, if a forcing process stalls, its nonempty remaining white set is a fort; conversely, a fort disjoint from the initially black vertices cannot be entered by a first force.

**2. Complete finite-state criterion.** Encode each column's chosen initial vertices and each candidate fort's vertices by a two-bit mask in \(\{0,1,2,3\}\). A transition from state \((a,c)\) to \((c,b)\) is permitted at a column with initial mask \(s\) when \(c\mathbin{\&}s=0\), and for each layer not occupied in \(c\), the number of fort neighbors in its preceding column \(a\), succeeding column \(b\), and opposite-layer vertex of \(c\) differs from one. There are \(16\) possible states \((a,c)\). A closed walk around the \(n\)-column ring specifies a fort disjoint from \(S\), and conversely. A marked Boolean transfer records whether at least one traversed fort column is nonempty; this excludes the empty fort. Accordingly, \(S\) is zero forcing precisely when the marked transfer product around the cycle has no diagonal entry.

The supplied certificate `prism_infinite_certificate.py` implements the state transitions and multiplication as explicit sixteen-row bit matrices, with marked and unmarked components. Its exact assertions verify
\[
T_0^5=T_0^6
\]
in the *marked* Boolean matrix monoid, where \(T_0\) is the empty-initial-column transfer. Multiplication then gives \(T_0^k=T_0^5\) for every integer \(k\ge5\); this equality preserves the existence of **nonempty** disjoint forts, not just unmarked walks.

**3. Exhaustive reduction for every length.** A nonempty initial set of at most four vertices can be written as a cyclic word of \(k\) nonzero column masks \(s_1,\ldots,s_k\) separated by \(k\) gaps of zeros, with \(\sum_i\operatorname{popcount}(s_i)\le4\). By the transfer identity, every gap longer than five may be truncated to length five without changing whether a disjoint fort exists. The certificate exhaustively examines **every** sequence of \(s_i\in\{1,2,3\}\) of total population weight at most four and **every** gap vector in \(\{0,\ldots,5\}^k\) with resulting cyclic length at least six. The enumerated case counts are \(2,105,1752,23154\) for weights \(1,2,3,4\), respectively (total \(25013\)). No weight below four is forcing. At weight four, the forcing property agrees exactly with membership in the five orbit families above, tested by constructing the families under cyclic dihedral and layer-swap actions.

The orbit members fit inside at most four consecutive columns. Enlarging any truncated gap of length five leaves the pattern's membership in the five families unchanged: no family occupies sites on both sides of such a gap. Therefore the finite transfer check and the five-template comparison apply to **all** ring lengths \(n\ge6\), not merely the finite range used to construct the certificate. Independently, `prism_direct_check.py` implements ordinary forcing moves without using the fort transfer, and checks the same 25,013 reduced cases and every four-subset on rings \(6\le n\le15\).

**4. Degrees and connectivity.** A one-vertex exchange neighbor must itself belong to one of the five classified orbits. Because every orbit representative is contained in four consecutive columns, its possible neighbors can be enumerated by removing one of four vertices and restoring a fourth in a bounded interval around the retained vertices. The standalone `prism_symbolic.py` performs the corresponding integer-line template calculation, with no cyclic modulus, obtaining degrees \(12,8,8,8,5\). For \(n\ge14\), any candidate exchange lies within a cyclic three-step neighborhood of a retained vertex. The integer representatives then lie in the column interval \([-4,6]\), whose width ten is less than \(n-3\); hence an otherwise distant wraparound three-column arc cannot produce an additional neighbor. This reduces all \(n\ge14\) to the integer-line calculation. Direct cyclic checks separately handle \(6\le n\le13\). The five orbit stabilizers, or the same bounded-support classification, give orbit sizes \(n,2n,2n,4n,4n\). Degree summation gives \(48n\) undirected edges and the polynomial asserted above.

For connectedness, each orbit representative reaches \(Q\) by one-vertex exchanges: \(X\to Q\), \(A\to Q\), \(Y\to Q\), and \(H\to Y\to Q\). Every translated/reflected/swapped representative therefore reaches a translated square. Finally consecutive squares \(Q_i=\{T_i,T_{i+1},B_i,B_{i+1}\}\) and \(Q_{i+1}\) are joined in two moves through \(\{T_{i+1},T_{i+2},B_i,B_{i+1}\}\), a member of the classified families. These paths connect every minimum set. This completes the infinite-family proof.

## Verification
Run the three self-contained Python 3 files in any directory with a standard Python interpreter:

```
python3 prism_infinite_certificate.py
python3 prism_direct_check.py
python3 prism_symbolic.py
```

Expected completion markers are `CIRCULAR_TEMPLATE_EXHAUSTION_ALL_LENGTHS_PASS`, `INDEPENDENT_DIRECT_EXCHANGE_ALL_TESTS_PASS`, and `SYMBOLIC_INFINITE_LADDER_LOCAL_DEGREES_PASS`. The finite-state calculation exhausts \(25013\) compressed cyclic words; the independent calculation checks their forcing property without the finite-state criterion; cyclic exchange degrees and graph connectedness are checked directly for lengths \(6\) through \(25\), while the integer-line test handles the uniform local degree calculation. All code and all required data are contained in these three files; no external packages or tables are needed. The finite-state reduction, not extrapolation from the direct checks, establishes the infinite scope.

## Relationship to prior work
The result \(Z(C_n\square P_2)=4\) is established by the AIM Minimum Rank–Special Graphs Work Group, Theorem 3.8 (first online November 26, 2007); **that minimum is not new**. Geneson, Haas, and Hogben introduced the one-vertex-exchange zero forcing graph and studied general reconfiguration properties, but their inspected cycle/path/forest results do not calculate this prism family. Boyer et al. studied zero-forcing polynomials broadly, but their accessible treatment did not provide the fourth coefficient for these prisms. Fort methods are established tools. The present claim adds the complete five-orbit minimum-set classification, exact linear count, full exchange-degree distribution, and connectivity across the prism family; those statements do not follow from knowing the minimum forcing number alone.

## Limitations
The theorem is restricted to ordinary zero forcing and single-vertex exchanges on \(C_n\square K_2\) for \(n\ge6\). It does not concern skew, positive-semidefinite, connected, or throttling variants of forcing, nor does it assert a full zero-forcing polynomial. The comparison of earlier literature leaves a priority risk that an equivalent classification might have appeared under generalized-Petersen, circular-ladder, or forcing-chain terminology. A related older prism-specific treatment on zero forcing number could not be inspected in full; it is not assumed non-covering. No independent scholarly audit has been performed.

## References
1. AIM Minimum Rank–Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, **Linear Algebra and its Applications** 428 (2008), 1628–1648, DOI: 10.1016/j.laa.2007.10.009 (first publicly online 2007-11-26), Theorem 3.8. Available at https://draganstevanovic.wordpress.com/wp-content/uploads/2012/09/published-version2.pdf.
2. J. Geneson, R. Haas, L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220v1 (first posted 2020-09-01), https://arxiv.org/pdf/2009.00220.
3. M. Boyer et al., *The zero forcing polynomial of a graph*, arXiv:1801.08910v1 (2018), https://arxiv.org/pdf/1801.08910.
4. A. Cameron et al., *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904v1 (2023), https://arxiv.org/pdf/2310.17904.
5. O. Petruk, *Zero Forcing Number of Some Families of Graphs*, **Mohyla Mathematical Journal** 3 (2020), 48–52. Full-text comparison was not completed; the available description concerns forcing numbers of gear and prism graphs.
