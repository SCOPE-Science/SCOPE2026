# Complete mod-two component-budget persistence of the Petersen graph

## Finding

Let \(P\) be the Petersen graph, realized as the Kneser graph whose ten vertices are the two-element subsets of \(\{1,2,3,4,5\}\), with edges between disjoint subsets. For each integer \(r\geq1\), put \(K_r=\operatorname{Ind}_r(P)\): its faces are vertex subsets for which every connected component of the induced subgraph has at most \(r\) vertices. The inclusions \(K_r\subseteq K_{r+1}\) give a filtration ending at the full nine-simplex \(K_{10}\).

**Complete positive-degree reduced persistence over \(\mathbf F_2\).** The nonzero intervals (each right endpoint exclusive) are precisely

\[
\begin{array}{c|c|r}
\text{degree}&\text{interval}&\text{multiplicity}\\\hline
2 &[1,2)&4\\
3 &[2,5)&1\\
3 &[4,5)&10\\
4 &[5,6)&61\\
5 &[6,7)&74\\
6 &[7,8)&36\\
7 &[8,9)&9\\
8 &[9,10)&1
\end{array}
\]

There are no other nonzero reduced persistence intervals for \(r\geq1\), including none in degrees zero or one. In particular, the unique three-dimensional class present at threshold \(2\) persists through thresholds \(3\) and \(4\), and disappears at threshold \(5\); ten additional three-dimensional classes appear at threshold \(4\) but die at \(5\).

**Stronger simple-homotopy statement.** The complex \(K_3\) simplicially collapses onto \(K_2\) by exactly sixty elementary free-face/coface removals. Thus the inclusion \(K_2\hookrightarrow K_3\) is a simple-homotopy equivalence over every coefficient ring, not merely an isomorphism on mod-two homology.

## Assumptions and scope

All computations concern the *specified ten-vertex graph*, not an arbitrary generalized Petersen graph. The filtration parameter is an integer \(r\geq1\). Persistence coefficients in the barcode are exactly \(\mathbf F_2\); no claim of an integral persistence decomposition is made. The elementary-collapse assertion is an integral topological statement.

The index set \(\{1,\ldots,10\}\) suffices because every component of an induced subgraph of the ten-vertex graph has at most ten vertices. Vertex identifiers in the reproducibility files are zero-based lexicographic indices of the two-element subsets of \(\{0,1,2,3,4\}\); changing labels preserves the mathematical graph.

## Proof

**1. Complete face enumeration.** Encode each nonempty vertex subset by its unique ten-bit integer mask. On each of the \(2^{10}-1=1023\) masks, determine the sizes of all connected components using the disjointness adjacency of the two-subset labels, and set \(\lambda(F)\) equal to the maximum of these sizes. Consequently \(F\in K_r\) holds if and only if \(\lambda(F)\leq r\). Taking a subset cannot enlarge an induced connected component, so \(\lambda\) is an admissible simplicial filtration function. Two separately implemented graph traversals in `verify.py` agree on all 1023 values, eliminating dependence on a hand-tabulated face list.

**2. Exact finite filtered-chain reduction.** Order the 1023 nonempty faces by the triple \((\lambda(F),\lvert F\rvert,\operatorname{mask}(F))\). Every proper face occurs before its coface. For every face, construct its full simplicial boundary over \(\mathbf F_2\) by deleting each one-bit vertex. Reduce columns from left to right by exclusive-or against the stored column with the same highest nonzero row. A zero reduced column births a class; a nonzero reduced column pairs its highest row with the column's face. This is the standard exact persistence reduction: its pairs yield interval decompositions of the finite filtered chain complex. Pairs born and killed at the same integer threshold represent zero-length intervals and are omitted. The unique unpaired class is the ordinary degree-zero class, removed by reducing homology. All other intervals are exactly those displayed in the finding.

This is an *exhaustive proof for the fixed finite graph*: there are no unexamined vertex subsets, unproved finite-range extrapolations, random samples, or numerical tolerances. The full algorithm, constants and asserted output are provided in standalone `verify.py`; its run output is recorded in `verification_output.txt`.

**3. Independent rank and inclusion checks.** For every \(r\in\{1,\ldots,10\}\), the verifier separately constructs the boundary matrices in each simplicial degree and computes their exact mod-two ranks. Its resulting reduced Betti numbers agree with the interval counts at each level. More stringently, it independently constructs mod-two cycle bases at earlier thresholds, embeds them into later chain groups, and computes the rank of each induced map on homology as the rank increase beyond the later boundary space. The program compares all 279 applicable positive-degree rank values with those implied by the claimed intervals. These calculations do not reuse the persistence column-pairing output as a substitute for the rank computations.

**4. Explicit relative elementary-collapse certificate.** `collapse_pairs.json` contains sixty ordered pairs of face masks. Starting from all 380 nonempty faces of \(K_3\), for every consecutive pair \((\tau,\sigma)\) the checker verifies that \(\tau\notin K_2\), \(\sigma\notin K_2\), \(\tau\subset\sigma\), that their dimensions differ by one, and that \(\sigma\) is the *unique strict coface* of \(\tau\) among all faces still present. Removing these two faces is therefore an elementary simplicial collapse. After all sixty removals, precisely the 260 nonempty faces of \(K_2\) remain. Each check runs on the complete current face set, establishing every free-face premise and the claimed inclusion equivalence.

## Verification

Run `python3 verify.py` from the directory containing `verify.py` and `collapse_pairs.json` (Python standard library only). The expected final line is `VERIFY_OK`. The deterministic run checks 1023 nonempty faces, 511 boundary pivot pairs, ten full homology levels, 279 inclusion-rank equalities, and sixty free-face collapses. The recorded output lists each nonzero barcode interval. The exact finite enumeration and replayable matching, rather than merely the summarized counts, are the mathematical certificate.

## Relationship to prior work

The definition of higher independence complexes and current interest in their topology are documented by Sawant (2026). Berghoff (2020, Example 6.2) computes the ordinary Petersen independence homology at threshold \(1\), including the previously known rank-four group in degree two. A previously published Petersen two-independence calculation likewise establishes the homotopy type at threshold \(2\). Neither separate snapshot determines the inclusion maps or the later threshold groups. The present statement is the **complete component-budget filtration**, especially its unique length-three bar, together with the explicit relative collapse across thresholds \(2\) and \(3\). It should not be confused with previously computed *graph-metric* Čech or Vietoris–Rips persistence of the Petersen graph: those filtrations have different faces and maps.

Deshpande, Roy and Sawant (2025) develop Alexander-dual and shellability methods for higher independence complexes. Their classes and structural results do not supply the present Petersen barcode or elementary-collapse certificate.

## Limitations

The barcode is proved only with \(\mathbf F_2\) coefficients. Agreement of finite mod-two ranks does not establish integral torsion-freeness, integral persistence, or the homotopy types at thresholds \(4\) through \(9\). The sixty collapses do establish the integral simple-homotopy equivalence \(K_3\searrow K_2\). Bibliographic priority cannot be guaranteed by indexed searches; the closest independently published threshold-two calculation was available as an indexed summary but its full-text repository page could not be fetched during comparison.

## References

1. R. Sawant, *On the Vertex Decomposability of r-Independence Complexes of Trees*, arXiv:2605.25150, first posted 2026-05-24, https://arxiv.org/abs/2605.25150.
2. M. Berghoff, *On the homology of independence complexes*, arXiv:2008.06267, 2020, especially Example 6.2, https://arxiv.org/abs/2008.06267.
3. P. Deshpande, A. Roy and R. Sawant, *The complex of r-co-connected subgraphs, chordality and Fröberg's theorem*, arXiv:2510.25710, first posted 2025-10-29, https://arxiv.org/abs/2510.25710.
4. Published mathematical calculation, *The Petersen two-independence complex is a three-sphere*, public research index record `2026/10/11/...0d53a7f4e76a` (full text not accessible in this comparison).
