# Mod-2 homology of the Desargues matching complex
## Finding
Let \(D=G(10,3)\) be the Desargues graph and \(\mathcal M(D)\) its ordinary matching complex. Then
\[
\widetilde H_j(\mathcal M(D);\mathbb F_2)\cong
\begin{cases}
\mathbb F_2^5,&j=5,\\
\mathbb F_2^{45},&j=6,\\
0,&\text{otherwise}.
\end{cases}
\]
Consequently \(\mathcal M(D)\) is not homotopy equivalent to a wedge of spheres all having one common dimension.

## Assumptions and scope
Write the vertices of \(D\) as \(u_i,v_i\) for \(i\in\mathbb Z/10\mathbb Z\), with edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\), indices modulo \(10\). The statement concerns ordinary simplicial homology over \(\mathbb F_2\) for this single finite graph. It does not determine integral torsion or the full homotopy type.

## Proof
The graph has \(30\) edges. Exhaustive recursive enumeration of vertex-disjoint edge sets gives the matching counts
\[
(1,30,375,2540,10155,24486,34945,27840,11040,1720,60)
\]
for cardinalities \(0,1,\ldots,10\).

For \(k\ge1\), use the \(k\)-edge matchings as the basis of the chain group in dimension \(k-1\). Over \(\mathbb F_2\), each boundary is the sum of the \(k\) faces obtained by deleting one edge. Exact Gaussian elimination gives boundary ranks
\[
(1,29,346,2194,7961,16525,18415,9380,1660,60)
\]
for cardinalities \(1,\ldots,10\). Thus
\[
\beta_j=c_{j+1}-r_{j+1}-r_{j+2},
\]
which yields \(\beta_5=5\), \(\beta_6=45\), and zero otherwise. The degree-zero calculation gives one connected component, so the displayed groups are the reduced homology groups in positive degree. A wedge of spheres in a single fixed dimension has reduced homology in only that dimension, proving the final consequence.

## Verification
The bundled `verify_desargues_matching.py` reconstructs \(G(10,3)\), enumerates every matching, builds every mod-2 boundary column, and performs exact bitwise Gaussian elimination over \(\mathbb F_2\). It checks the full count and rank vectors and also verifies
\[
\chi(\mathcal M(D))=41,\qquad \widetilde\chi(\mathcal M(D))=40=-5+45.
\]
A separate row-elimination calculation on the central boundary maps returned the same ranks \(16525\), \(18415\), and \(9380\). The bundled verifier prints `DESARGUES_MATCHING_VERIFY_OK` only after all assertions pass.

## Relationship to prior work
Donovan and Scoville define the graph matching complex as the complex of independent edge sets and compute exact homotopy types for paths, cycles, and Dutch windmill graphs, while citing the known forest case. The Desargues graph is not among these families. Searches using “Desargues graph,” “generalized Petersen \(G(10,3)\),” “matching complex,” and the equivalent “independence complex of the line graph” formulation found no source stating the homology calculation above. The closest published-corpus records naming the Desargues graph concern metric distortion and graph lifts, which do not imply this claim.

The calculation gives an exact benchmark for a canonical cubic symmetric graph, and its two adjacent nonzero reduced homology degrees distinguish it from the single-degree wedge patterns occurring in several familiar matching-complex families.

## Limitations
Only mod-2 homology is proved. Integral homology, torsion, attaching maps, and the full homotopy type are not determined. Literature searches cannot prove absolute absence from all unindexed or unpublished sources; no decisive covering source was found among the inspected primary literature and database records.

## References
Connor Donovan and Nicholas A. Scoville, “Star clusters in the Matching, Morse, and Generalized Morse complex,” arXiv:2207.13780v1, first public 2022-07-27.
