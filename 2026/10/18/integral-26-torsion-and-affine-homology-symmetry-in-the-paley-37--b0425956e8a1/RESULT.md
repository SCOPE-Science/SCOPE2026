# Integral \(26\)-torsion and affine homology symmetry in the Paley-\(37\) flag complex

## Finding
Let \(P_{37}\) be the Paley graph on the prime field \(\mathbb F_{37}\). For its flag (clique) complex \(X=\operatorname{Cl}(P_{37})\), the **complete integral homology** is
\[
H_k(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&k=0,\\
\mathbb Z^{36}\oplus\mathbb Z/26\mathbb Z,&k=2,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, degree two has both \(2\)-primary and \(13\)-primary torsion. Under the natural affine graph-automorphism group \(A=\mathbb F_{37}\rtimes(\mathbb F_{37}^{\times})^2\) of order \(666\),
\[
\widetilde H_2(X;\mathbb Q)\cong
\ker\bigl(\mathbb Q^{37}\xrightarrow{\text{sum}}\mathbb Q\bigr)
\]
as rational \(A\)-modules, where \(A\) acts by permuting the \(37\) field elements. This is an integral-homology and rational-symmetry theorem; no assertion about the full homotopy type or fundamental group is made.

## Assumptions and scope
The vertex set is \(\{0,1,\ldots,36\}\). For distinct \(i,j\), the pair \(\{i,j\}\) is an edge exactly when \((j-i)\bmod37\) belongs to the set of nonzero quadratic residues. Every clique is included as a simplex; each simplex is oriented by increasing vertex order. All chains have coefficients in \(\mathbb Z\) unless explicitly stated. The theorem concerns this single graph, not all conference graphs or all prime powers. Multiplication by the nonsquare \(2\) maps the graph to its complement, so the same integral-homology statement holds for the ordinary independence complex \(\operatorname{Ind}(P_{37})\), with an explicit simplicial isomorphism.

## Proof
**Face enumeration.** Start from singleton vertices. Extend each increasing clique by each larger vertex adjacent to all its members. An exhaustive execution yields the face vector
\[
(f_0,f_1,f_2,f_3)=(37,333,888,555)
\]
and no cliques of size five. Thus the unaugmented integral simplicial chain groups are \(C_0=\mathbb Z^{37}\), \(C_1=\mathbb Z^{333}\), \(C_2=\mathbb Z^{888}\), \(C_3=\mathbb Z^{555}\). The signed boundary is
\[
\partial_k[v_0,\ldots,v_k]=\sum_{i=0}^k(-1)^i[v_0,\ldots,\widehat v_i,\ldots,v_k]
\]
for increasing vertices.

**Exact integral elimination.** The accompanying JSON certificate records elementary, invertible integer row and column eliminations of the matrices \(\partial_2\) and \(\partial_3\). Each listed pivot is \(+1\) or \(-1\), and each elimination uses only integer multiples of rows and columns and deletion of an isolated unit diagonal entry. Independent replay from graph-defined matrices checks every pivot and every surviving entry. For \(\partial_2\), the certificate exhibits \(297\) unit Smith factors and an all-zero residual matrix of size \(36\times591\). For \(\partial_3\), it exhibits \(554\) unit factors and a residual \(334\times1\) column with precisely \(37\) entries \(+26\), \(37\) entries \(-26\), and all other entries zero. Its last Smith factor is therefore exactly \(26\) (the gcd of that column), yielding
\[
\operatorname{coker}\partial_3\cong \mathbb Z^{333}\oplus\mathbb Z/26\mathbb Z,\qquad
\operatorname{im}\partial_2\cong\mathbb Z^{297}.
\]
The Paley graph is connected, so \(\operatorname{rank}\partial_1=36\). Because \(\operatorname{im}\partial_2\) is primitive in \(C_1\) and has the same rank as \(\ker\partial_1\), the first integral homology vanishes. The chain identity \(\partial_2\partial_3=0\) is checked on all \(555\) columns, and \(\partial_3\) has full column rank, so \(H_3=0\). Since \(C_2/\operatorname{im}\partial_3\) maps onto the free group \(\operatorname{im}\partial_2\cong\mathbb Z^{297}\) with kernel \(H_2\), that exact sequence splits; subtracting the free ranks gives \(H_2\cong\mathbb Z^{36}\oplus\mathbb Z/26\mathbb Z\). All other homology vanishes because there are no higher faces.

**Affine character.** The square subgroup of \(\mathbb F_{37}^{\times}\) has \(18\) elements. Each affine map \(g_{a,b}:x\mapsto ax+b\), for nonzero square \(a\) and arbitrary \(b\), induces an automorphism of \(X\). Compute its simplicial Lefschetz number by adding signed traces of its permutation on the oriented faces, and subtract the degree-zero trace of \(1\). The exact exhaustive calculation for all \(666\) elements gives
\[
\operatorname{tr}(g\mid\widetilde H_2(X;\mathbb Q))=
\begin{cases}
36,&g=1,\\
-1,&g\text{ is a nonidentity translation},\\
0,&g\text{ has a nonidentity linear multiplier}.
\end{cases}
\]
The augmentation module of the \(37\)-point permutation representation has precisely this character: it is the number of fixed field elements minus one. The finite-group character criterion over characteristic zero gives the asserted rational \(A\)-module isomorphism.

## Verification
Run `python3 verify_paley37.py paley37_integral_certificate.json` in a directory containing both supplied files. The verifier uses the Python standard library only and builds the entire complex directly from quadratic residues, not from an external graph table. It checks the absence of higher cliques, the face counts, every integer pivot and residual certificate entry, the signed chain identity, self-complementarity, and the complete affine character on all \(666\) elements. The accompanying `paley37_verification_output.txt` is a recorded successful execution. The certificate is finite but exhaustive for the explicitly specified finite complex; it does not infer statements for larger Paley graphs.

## Relationship to prior work
Cioabă, Guo, Ji and Mim (2025) establish a criterion and computer-check its hypotheses for the vanishing of first clique cohomology of several Paley graphs, including the order-\(37\) graph. Consequently, first-homology vanishing **alone is already covered**; it is not proposed as a new contribution here. Cioabă and Mim (2026) prove a large-conference-graph vanishing theorem for first homology and complete homology formulas for *Latin-square* graphs. Neither result entails the integral degree-two \(26\)-torsion or the full affine rational character for \(P_{37}\). Wesołowski (2026) establishes complexity results for detecting torsion using projective-plane joins; its constructions do not identify intrinsic order-\(13\) torsion of this vertex-transitive graph. Previously reported Paley-\(29\) clique homology has only order-\(2\) torsion and does not imply the order-\(37\) calculation. Searches of closely related statements and records did not uncover the present exact invariant; this is not a proof of exhaustive bibliographic uniqueness.

## Limitations
The homology computation is an exact finite integer calculation supported by a replayable certificate, not an infinite-family theorem. No simple-homotopy classification, claim of simple connectivity, equivariant integral torsion-module classification, or presentation of torsion cycles is asserted. The rational character cannot by itself determine the integral action on the order-\(26\) torsion. Unindexed publications or computations may overlap despite the documented searches. Independent scientific audit has not been performed.

## References
1. Sebastian M. Cioabă, Krystal Guo, Chunxu Ji and Mutasim Mim, *Clique complexes of strongly regular graphs, their eigenvalues, and cohomology groups*, first public 2025-08-07, arXiv:2508.05871. https://arxiv.org/abs/2508.05871
2. Sebastian M. Cioabă and Mutasim Mim, *On the homology groups of clique complexes of strongly regular graphs*, first public 2026-06-25, arXiv:2606.27328. https://arxiv.org/abs/2606.27328
3. Adam Wesołowski, *Torsion detection in clique complexes is conditionally QMA1-hard*, first public 2026-09-12, arXiv:2609.14110. https://arxiv.org/abs/2609.14110
