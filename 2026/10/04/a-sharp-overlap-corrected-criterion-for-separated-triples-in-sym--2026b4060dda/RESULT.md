# A sharp overlap-corrected criterion for separated triples in symmetric designs
## Finding
Let \(\mathcal D\) be a symmetric \(2\text{-}(v,k,\lambda)\) design. If \[v-2>\lambda(k-2)-(\lambda-1)(\lambda-2),\] then \(\mathcal D\) contains three points that lie in no common block (equivalently, a pairwise separated triple in the incidence terminology of the motivating storage problem). The bound is sharp: for every prime power \(q\), the point-hyperplane design of \(\mathrm{PG}(3,q)\) has \(v=q^3+q^2+q+1\), \(k=q^2+q+1\), \(\lambda=q+1\), every three points lie in a hyperplane, and equality holds in the displayed bound.

The inequality strengthens the \(p=3\) sufficient condition \(v-2>\lambda(k-2)\) in Luo--Li--Zhang--Wang by the explicit overlap correction \((\lambda-1)(\lambda-2)\). For \(\lambda\ge3\) the correction is positive.

## Assumptions and scope
A symmetric \(2\text{-}(v,k,\lambda)\) design has \(v\) points and \(v\) blocks, every block has size \(k\), and every pair of distinct points lies in exactly \(\lambda\) blocks. In a symmetric design every two distinct blocks also meet in exactly \(\lambda\) points. A triple is called separated here when no block contains all three of its points.

The statement is a design-theoretic structural lemma. It does not by itself determine the universal replica threshold in the remaining storage-code case where no separated triple exists.

## Proof
Fix two distinct points \(x,y\), and let \(B_1,\ldots,B_\lambda\) be the blocks containing both. Put \(C_i=B_i\setminus\{x,y\}\). Then each \(C_i\) has size \(k-2\).

For every point \(z\notin\{x,y\}\), let \(m_z\) be the number of sets \(C_i\) containing \(z\), and let \(U=\{z:m_z>0\}\). Double counting incidences gives
\[\sum_z m_z=\lambda(k-2).\]
For \(\lambda\ge2\), two distinct blocks through \(x,y\) meet in exactly \(\lambda\) points, so beyond \(x,y\) they have exactly \(\lambda-2\) common points. Hence
\[\sum_z \binom{m_z}{2}=\binom{\lambda}{2}(\lambda-2).\]
For \(1\le m\le\lambda\),
\[2\binom{m}{2}=m(m-1)\le\lambda(m-1).\]
Summing this inequality over \(z\in U\) yields
\[2\sum_z\binom{m_z}{2}\le\lambda\left(\sum_zm_z-|U|\right).\]
Substituting the two counts gives
\[|U|\le\lambda(k-2)-(\lambda-1)(\lambda-2).\]
The same conclusion holds for \(\lambda=1\), where there is only one block through \(x,y\) and the correction term is zero. Therefore, if
\[v-2>\lambda(k-2)-(\lambda-1)(\lambda-2),\]
some point \(z\notin\{x,y\}\) lies outside every block through \(x,y\). No block contains \(x,y,z\), proving existence of a separated triple.

For completeness, the block-intersection fact used above follows directly from the square incidence matrix \(A\). The point-pair axioms give \(AA^\mathsf{T}=(k-\lambda)I+\lambda J\). Since \(A\) is square and the right side is nonsingular, \(A\) is invertible; because every row and column sum equals \(k\), conjugating by \(A\) preserves \(J\). Thus \(A^\mathsf{T}A=(k-\lambda)I+\lambda J\), so distinct blocks meet in \(\lambda\) points.

For sharpness, in the point-hyperplane design of \(\mathrm{PG}(3,q)\),
\[v=q^3+q^2+q+1,\qquad k=q^2+q+1,\qquad \lambda=q+1.\]
Every three projective points span a subspace of projective dimension at most two, hence are contained in a hyperplane. Meanwhile
\[\lambda(k-2)-(\lambda-1)(\lambda-2)=q^3+q^2+q-1=v-2.\]
So the strict inequality cannot be weakened to a non-strict one in general.

## Verification
`verify_separated_triples.py` checks the scalar inequality for \(1\le\lambda\le50\), constructs the point-hyperplane incidence designs of \(\mathrm{PG}(3,2)\) and \(\mathrm{PG}(3,3)\) from normalized projective vectors, verifies their design and block-intersection parameters, verifies that every triple is contained in a hyperplane, and checks equality in the bound. The finite checks support the proof but are not used to infer the all-parameter theorem.

## Relationship to prior work
Luo, Li, Zhang, and Wang introduce pairwise separated failure sets for stripeless erasure coding based on symmetric block designs and leave the \(\lambda>1\), no-separated-set case as the remaining non-exact threshold regime. Their Proposition V.1 gives the parameter-only sufficient condition \(v-2>\lambda(k-2)\) when \(p=3\). The present lemma uses the mandatory \(\lambda\)-point intersections among the \(\lambda\) blocks through a fixed point-pair to subtract \((\lambda-1)(\lambda-2)\) from that union estimate.

Focused searches for the displayed overlap-corrected inequality, the union of blocks through a point-pair, and the \(\mathrm{PG}(3,q)\) boundary did not locate a statement implying this criterion. Standard design references confirm the symmetric-design block intersection property, which is also proved above.

## Limitations
The result gives a sufficient condition for existence of a separated triple, not a classification of all symmetric designs lacking one. Equality can occur without the projective-space example being the only possibility. The result also does not settle the exact replica threshold for designs on the no-separated side of the boundary.

## References
1. G. Luo, X. Li, Y. Zhang, and K. Wang, “Replica Thresholds for Stripeless Erasure Coding Based on Symmetric Block Designs,” arXiv:2609.29149v1, 24 Sep 2026. https://arxiv.org/abs/2609.29149
2. M. Buratti, M. Garonzi, and E. Rinaldi, “Additivity of symmetric and subspace 2-designs,” *Designs, Codes and Cryptography* (2024), for the standard fact that two blocks of a symmetric design meet in \(\lambda\) points. https://link.springer.com/article/10.1007/s10623-024-01452-4
