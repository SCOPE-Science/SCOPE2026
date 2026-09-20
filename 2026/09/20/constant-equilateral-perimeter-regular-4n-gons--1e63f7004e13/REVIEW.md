# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof reduces the problem by dihedral symmetry to half of one edge of a regular \(N\)-gon. On each of two parameter intervals it constructs three boundary points and tracks the three difference vectors. The edge-vector determinant identity places each derivative parallel to the edge of a fixed cone on which the polygonal gauge is linear. Endpoint determinant checks keep each affine difference path inside that cone, so each side norm is constant. Reflection symmetries at the joining endpoints force the three constants to agree.

The two residue classes \(N=12m+4\) and \(N=12m+8\) were checked separately. The transition parameters agree because \(\tau(1+s)=1-\tau\), and the second pieces meet continuously. The endpoint identity
\[
(1/2-\tau)/s=\tau/2
\]
gives the final edge-midpoint reflection in both cases. The sine signs used in all cone checks follow from
\[
0\le \alpha-\theta<\alpha<\alpha+\theta<\alpha+2\theta<\pi/2.
\]

A direct implementation of the regular-polygon gauge reproduces the construction numerically for representative values in both residue classes. In particular it gives perimeters
\(5.205252779825\ldots\) for \(H_{16}\) and
\(5.195027526095\ldots\) for \(H_{32}\), agreeing with the 2025 approximations.

The reduction from a constructed equilateral triangle through each boundary point to all triangles in \(\mathcal T_3\) uses Proposition 7 of Alonso--Martín--Papini (2025), which states that the side length of a \(\mathcal T_3\)-triangle through a prescribed unit-sphere point is unique.

## Originality

**PASS, to the best of our knowledge.** The 2025 perimeter paper explicitly marks \(L_3=M_3\) for \(H_{16}\) and \(H_{32}\) as numerical questions and asks more generally about the equality. The July 2026 follow-up proves the equality for unit spheres invariant under \(\pi/6\)-rotation, which includes regular \(N\)-gons only when \(12\mid N\). It therefore does not settle the \(N\equiv4,8\pmod{12}\) families treated here.

Searches were made for the exact \(H_{16}\)/\(H_{32}\) claims and for synonymous formulations involving regular \(4n\)-gonal polygonal norms, equilateral triangles, constant perimeter, \(L_3=M_3\), and Jung constants. No statement proving these two residue classes, or a stronger theorem implying them, was found. The older Minkowski-equilateral literature and the references of the 2025 and 2026 papers were also checked for likely coverage.

Residual originality risk remains from unindexed, inaccessible, or differently phrased work in the broader literature on polygonal normed planes. No specific inaccessible source was identified whose title or available metadata substantially suggests that it contains this theorem.

## Value

**PASS.** The result converts two explicit numerical conjectures from 2025 into exact theorems and simultaneously proves an infinite-family statement: every regular polygonal norm with \(4\mid N\) has constant \(\mathcal T_3\)-perimeter. Together with the already known \(4,8\), and \(12\mid N\) cases, this completes the regular-\(4n\)-gon family. The construction also yields exact trigonometric formulas for the common perimeter in the two previously uncovered residue classes.

## Scientific limitations

The theorem is restricted to regular polygonal unit spheres and does not characterize all normed planes with \(L_3=M_3\). The broader characterization questions in the 2025 paper are not resolved. The numerical verification artifact is only a consistency check; correctness rests on the analytic cone-and-symmetry proof.
