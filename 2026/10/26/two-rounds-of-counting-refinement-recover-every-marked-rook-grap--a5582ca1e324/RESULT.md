# Two rounds of counting refinement recover every marked rook-graph orbit

## Finding

**Theorem.** Fix arbitrary integers \(m,n\ge 2\). Let \(R_{m,n}=K_m\square K_n\) be the undirected simple rook graph on \([m]\times[n]\), where distinct \((r,c)\) and \((r',c')\) are adjacent if \(r=r'\) or \(c=c'\). Let \(S\) be **any** subset of cells, possibly empty or the entire board. Give every cell in \(S\) its own distinct initial colour and all cells outside \(S\) one common other colour. Run synchronous counting colour refinement, retaining the previous colour at each round.

The partition \(\mathcal P_2\) after **at most two strict refinement rounds** is precisely the orbit partition of the pointwise stabilizer \(\operatorname{Aut}(R_{m,n})_{(S)}\). Hence the partition is stable after at most two strict rounds, uniformly in board size and number and placement of marks.

Put \(t=|S|\); let \(a\) and \(b\) be the numbers of distinct rows and columns meeting \(S\), respectively. If \(m\ne n\), or if \(S\) contains two cells sharing a row or a column, the exact number of stable colour classes is

\[
(a+\mathbf 1_{a<m})(b+\mathbf 1_{b<n}).
\]

If \(m=n\) and the marked cells form a nonattacking rook placement (including the empty placement), the exact class count is

\[
\frac{t(t+1)}2+(t+1)\mathbf 1_{t<m}.
\]

Both formulas count **actual classes**, not classes modulo re-labelling of the marked colours. In the first case, let the row types be the \(a\) individual marked rows and, if present, one aggregate unmarked-row type; let columns be treated analogously. A class indexed by one row type and one column type has size the product of their multiplicities \(1\) or \(m-a\), and \(1\) or \(n-b\), respectively. In the equal-square nonattacking case, after labelling the \(t\) marks by their distinct labels, the classes have sizes \(1\) (each marked cell), \(2\) (each unordered pair of different marked labels), \(2(m-t)\) (each marked label versus the unmarked coordinate type, if any), and \((m-t)^2\) (both coordinates unmarked, if any).

The two-round bound is sharp whenever \(m\ne n\), witnessed by a single marked cell, and whenever \(m=n\ge4\), witnessed by the three marks \((0,0),(0,1),(1,2)\) using zero-based coordinates.

## Assumptions and scope

All graphs are finite, undirected, loopless and simple. We use ordinary one-dimensional counting colour refinement with the recursion \(c_{j+1}(v)=(c_j(v),\operatorname{multiset}\{c_j(w):w\sim v\})\), where colours are compared by equivalence classes rather than incidental integer names. A **strict round** means the resulting partition is strictly finer. In particular, an additional equality-check iteration used by software to detect termination is *not* counted as a strict round. The pointwise stabilizer fixes each marked vertex individually; it does not merely preserve their set. The empty set and a fully individualized graph are included.

## Proof

**1. Automorphisms and orbit types.** The full automorphism group of \(R_{m,n}\) consists of arbitrary independent permutations of the rows and columns, and, when \(m=n\), their compositions with coordinate interchange. One proof recognizes rows and columns as the two families of maximal coordinate cliques, with the same conclusion directly for the four-cycle \(R_{2,2}\). Any automorphism must permute these two coordinate directions globally, and their intersections determine the action on all vertices.

If two marked cells share a row, a direction-interchanging automorphism cannot fix both (their distinct columns would have to become a common column after interchange). The same holds when they share a column. If \(m\ne n\), interchange is impossible. In either case the pointwise stabilizer permutes only **unmarked rows among themselves** and **unmarked columns among themselves**: every row and every column occupied by a mark is fixed separately. Thus its vertex orbits are exactly the products of marked/unmarked row and column types, with the first displayed class-count and class-size formulas.

In the remaining case the board is square and the marks form a matching. After independent coordinate relabellings, write them as \((i,i)\) for \(1\le i\le t\). Automorphisms fixing them allow independent permutations of the unmarked row and column coordinates and also the global transpose. Their cell orbits are precisely unordered pairs of coordinate types drawn from \(\{1,\ldots,t,*\}\), except that both coordinates equal to an occupied label occur at the already marked singleton; the symbol \(*\) may be used only when \(t<m\). This gives the second count and its class sizes.

**2. Recovering a coordinate line from a marked adjacency.** Let \(N(v)\) denote the **open** neighborhood of \(v\). Since each marked vertex is a singleton initially, \(N(v)\) is a union of \(\mathcal P_1\)-classes for each marked \(v\). Every Boolean combination of such sets is again a union of \(\mathcal P_1\)-classes. If two marked cells \(e=(r,c_1)\) and \(f=(r,c_2)\) share a row, then \(c_1\ne c_2\) and

\[
\operatorname{Row}(r)=\{e,f\}\cup(N(e)\cap N(f)).
\]

Indeed a common neighbor must share their row: an off-row vertex cannot simultaneously lie in both distinct columns. Therefore this entire row is a union of first-round colour classes. The column-sharing case is symmetric.

**3. Propagating the line to all marked coordinates.** Suppose the row \(L=\operatorname{Row}(r)\) is known as a union of first-round classes. For any marked \(f=(r,c_f)\) on \(L\), its entire column is

\[
\operatorname{Col}(c_f)=\{f\}\cup(N(f)\setminus L),
\]

hence a union of first-round classes. For a marked \(f=(r_f,c_f)\) off \(L\), the set \(N(f)\cap L\) is the **singleton** \(\{x\}\), where \(x=(r,c_f)\). Thus \(x\) is already a first-round singleton, and its neighborhood is a union of second-round colour classes. Then

\[
\operatorname{Col}(c_f)=\{x\}\cup(N(x)\setminus L)
\]

is a union of second-round classes. For **every** marked \(f=(r_f,c_f)\), after its column is recovered the row is

\[
\operatorname{Row}(r_f)=\{f\}\cup(N(f)\setminus\operatorname{Col}(c_f)),
\]

also a union of second-round classes. Consequently, every marked row and column is a union of second-round classes. Intersecting and complementing these line sets shows that **each pointwise-stabilizer orbit** in Part 1 is a union of \(\mathcal P_2\)-classes. Conversely, every automorphism fixing all initial singleton colours preserves every refinement colour, so an orbit is contained in a colour class. The two partitions must coincide. The proof for two marks sharing a column is obtained by exchanging coordinate names.

**4. The nonattacking case.** With matching marks \((i,i)\), for every unmarked vertex \(v\) the set of initially marked neighbors is exactly the set of occupied coordinate labels at its row and column, excluding the impossible marked diagonal itself. Its first-round colour thus reveals an unordered pair \(\{i,j\}\) of distinct occupied labels, a singleton \(\{i\}\), or the empty set; initially marked diagonal cells are already singletons. On a square board this is precisely the orbit classification in Part 1, so one round suffices.

On a nonsquare board, the first round can merge **two orientation types**: the two orders of two distinct marked labels \(i,j\), and the two orientations of a singleton marked label \(i\) paired with an unmarked coordinate \(*\). For each marked label \(i\), write \(S_i\) for its first-round colour class consisting of \((i,u)\) with unmarked column \(u\) and \((v,i)\) with unmarked row \(v\), omitting whichever family is empty. The class \(S_i\) is nonempty because \(m\ne n\) and \(t\le\min(m,n)\). A cell \((i,j)\) with distinct occupied labels has exactly \(n-t\) neighbors in \(S_i\), while the reverse cell \((j,i)\) has exactly \(m-t\) neighbors there. These differ. For single-label orientations, a cell \((i,u)\) with unmarked column has \(n-t-1\) neighbors in \(S_i\), while a cell \((v,i)\) with unmarked row has \(m-t-1\). Again these differ whenever both types exist. Therefore the second round separates all different ordered coordinate profiles, and two rounds always suffice.

**5. Sharpness.** If \(m\ne n\), individualize \((0,0)\). At round one the vertices \((0,1)\) and \((1,0)\) both see exactly that marker, but no automorphism interchanges row and column when their sizes differ. They are separated at round two by the neighbor counts in Part 4. If \(m=n\ge4\), mark \((0,0),(0,1),(1,2)\). The vertices \((1,3)\) and \((2,2)\) see exactly the third marker at round one, but one has a marked row and an unmarked column while the other has an unmarked row and a marked column. Coordinate interchange cannot fix the two marks sharing row zero. They are different stabilizer orbits, hence the second round is needed. This completes the proof.

## Verification

Run `python3 rook_verify.py` from the directory containing the embedded program. It enumerates every subset of vertices as the individually coloured set for the six board sizes \((2,2),(2,3),(2,4),(3,3),(3,4),(4,4)\), totaling \(70{,}480\) complete marked configurations, and tests \(2{,}500\) further reproducibly sampled configurations in five larger boards. For all cases it compares exact counting-refinement partitions to explicit coordinate orbit signatures, verifies the class-count formulas, and checks the two-round bound. For all exhaustive boards containing at most nine vertices it also enumerates every coordinate-permutation automorphism (including transpose when available) and compares the resulting orbits independently of the orbit-signature formula. The program checks the sharp square-board witness separately. See `rook_verify_output.txt` for the recorded output.

The finite tests are not an infinite proof. The argument in the preceding section is the all-size certificate.

## Relationship to prior work

Colour refinement and its relation to individualization and automorphisms are classical. Arvind, Köbler, Rattan and Verbitsky prove the Tinhofer property for the triangular graphs \(J(n,2)=L(K_n)\); the family here instead consists of line graphs \(L(K_{m,n})\), with marked rows and columns and a distinct rectangular/square symmetry dichotomy. Their triangular-graph theorem does not state or imply the present exact two-round result for these induced subgraphs. Work on recognizing subgraphs of Hamming graphs addresses embeddings, not individualized colour-refinement depth. General Tinhofer characterizations do not supply the rook-graph classification or bound. Papers on Hamming-graph structure, rook-graph homology, and graph products address different invariants. No equivalent two-round statement was identified in the completed targeted searches; this is not an exhaustive novelty guarantee.

## Limitations

The theorem concerns **two-dimensional** products of complete graphs only. Nothing is claimed for higher-dimensional Hamming graphs, arbitrary initial colouring partitions, automorphism groups that preserve the marked set merely setwise, or exact behaviour of every intermediate first-round class beyond the matching case. A known or undiscovered general theorem giving these same orbit partitions in every case would cover the orbit-equality part; the sharp uniform two-round bound and class-count formulas would still require an implication check. Publication-priority uncertainty remains. Independent scientific audit has not been performed.

## References

1. S. Klavžar, "Characterizing subgraphs of Hamming graphs," *Journal of Graph Theory* 49 (2005), 302–312. DOI: `10.1002/jgt.20084` (first published 2005-04-08).
2. K. Kersting, M. Mladenov, R. Garnett and M. Grohe, "Power Iterated Color Refinement," *AAAI* 28 (2014). DOI: `10.1609/aaai.v28i1.8992` (published 2014-06-21).
3. V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, "Graph Isomorphism, Color Refinement, and Compactness," arXiv:`1502.01255` (2015), especially the section on Tinhofer graphs and Appendix A.2 on \(J(n,2)\).
4. S. Bhattacharjee, A. Panse and J. Sarma, "A Hierarchy of Tinhofer Graphs: Separations and Membership Testing," arXiv:`2605.19702` (2026), general orbit-characterization context; not an archive-dating source.
