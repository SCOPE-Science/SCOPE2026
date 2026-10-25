# A sharp positivity frontier on the six-cell alternating periodic finite-element mesh

## Finding

For unit-diffusivity heat flow discretized by periodic, continuous, piecewise-linear finite elements on six alternating-length intervals \(a,b,a,b,a,b\), with \(a,b>0\), the consistent-mass backward-Euler matrix \(P_\tau=(M+\tau K)^{-1}M\) preserves entrywise nonnegativity for every nonnegative nodal vector exactly for

\[
\tau=0\quad\text{or}\quad \tau\ge\frac{\max\{a^2,b^2\}}6.
\]

The result establishes necessity, not merely the usual sufficient lower-step restriction, for the smallest three-period alternating mesh. The formula is valid at arbitrary positive mesh contrast. At positive steps below the threshold, an explicitly identified nonadjacent matrix entry is negative.

## Assumptions and scope

The domain is a circle comprising six elements with lengths \(h_i=a\) for even \(i\) and \(h_i=b\) for odd \(i\), with indices in \(\mathbb Z/6\mathbb Z\). Diffusivity is \(1\); periodic nodal unknowns are ordered \(0,\ldots,5\). No mass lumping is performed. An element of length \(h\) contributes \(h\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}/6\) to the mass matrix and \(\begin{psmallmatrix}1&-1\\-1&1\end{psmallmatrix}/h\) to stiffness. Thus \(M_{ii}=(a+b)/3\), \(K_{ii}=1/a+1/b\), and for neighboring vertices \(i,i+1\), \(M_{i,i+1}=h_i/6\), \(K_{i,i+1}=-1/h_i\). All other offdiagonal entries vanish. At \(\tau=0\), \(P_0=I\). Both matrices are symmetric; \(M\) is positive definite and \(K\) positive semidefinite, so \(D_\tau=M+\tau K\) is invertible for all \(\tau\ge0\).

## Proof

For \(\tau>0\), define the strictly positive expression

\[
H=(ab+6\tau)(ab+12\tau)(a^2+3ab+b^2+6\tau).
\]

Direct elimination in the displayed cyclic six-by-six matrices, or the adjugate formula \(P_\tau=\operatorname{adj}(D_\tau)M/\det(D_\tau)\), gives these **exact identities**:

\[
(P_\tau)_{0,2}=\frac{2\tau(6\tau-a^2)(ab+b^2+6\tau)}{H},
\qquad
(P_\tau)_{0,4}=\frac{2\tau(6\tau-b^2)(a^2+ab+6\tau)}{H}.
\]

The indices are read modulo six. To reproduce the algebra without numerical approximation, construct the two cyclic matrices from the preceding element contributions, solve \(D_\tau u=M e_2\) and \(D_\tau v=M e_4\) by Gaussian elimination over the rational-function field \(\mathbb Q(a,b,\tau)\), and simplify their zeroth coordinates; the two rational identities above are the factorizations. For positive \(a,b,\tau\), every factor except \(6\tau-a^2\) and \(6\tau-b^2\) is positive. Hence entrywise nonnegativity necessitates both \(\tau\ge a^2/6\) and \(\tau\ge b^2/6\).

Conversely, for \(\tau\ge\max\{a^2,b^2\}/6\), each nonzero offdiagonal of \(D_\tau\) is \(h/6-\tau/h\le0\), with \(h\in\{a,b\}\). Its diagonal is \((a+b)/3+\tau(1/a+1/b)\); the diagonal exceeds the sum of the absolute offdiagonals because \(D_\tau\mathbf1=M\mathbf1=(a+b)\mathbf1/2>0\). Thus \(D_\tau\) is a nonsingular strictly diagonally dominant symmetric \(M\)-matrix, so \(D_\tau^{-1}\) is entrywise nonnegative. Since every entry of \(M\) is nonnegative, \(P_\tau=D_\tau^{-1}M\ge0\). Finally \(P_\tau\mathbf1=\mathbf1\), so entrywise nonnegativity also implies preservation of every nodal interval bound. This proves both directions, including equality at the threshold.

## Verification

The proof is algebraic and covers all positive real \(a,b\), not merely sample grids. The accompanying standard-library script `verify.py` assembles \(M\) and \(K\) using exact rational arithmetic, inverts \(D_\tau\) by Gauss-Jordan elimination, and compares both displayed identities exactly for an explicit grid of rational parameter triples. These finite checks supplement, but do not replace, the symbolic adjugate identities and the \(M\)-matrix proof. The script also checks the update is stochastic and the sign classification on its parameter grid.

## Relationship to prior work

Li and Huang (arXiv:1209.5657, first posted 2012-09-25, Theorem 3.1) derive sufficient mesh-dependent lower time-step conditions for consistent-mass finite-element maximum principles. Their treatment of arbitrary meshes does not assert necessity for this six-element periodic alternating family; their examples are in two dimensions. The present calculation establishes exact necessity in a fixed, highly symmetric nonuniform one-dimensional test family. The usual sufficient \(M\)-matrix criterion coincides with the actual frontier here, but sufficiency alone does not imply this equality. Earlier finite-element positivity literature can contain related special cases; no general novelty or independent certification is claimed here.

## Limitations

Only the periodic six-element mesh, positive element lengths, constant unit diffusivity, and consistent-mass backward Euler are covered. Four-element periodic meshes may exhibit positivity below the displayed bound; no statement for eight or more elements follows from this six-cell calculation. The sufficient large-step assertion for general meshes is classical; the new content assessed here is the exact necessity for this first three-repeat heterogeneous cycle. Specialized earlier analyses may cover the same finite model.

## References

1. X. Li and W. Huang, *Maximum principle for the finite element solution of time dependent anisotropic diffusion problems*, arXiv:1209.5657 (first public preprint 2012-09-25), especially Theorem 3.1 and its proof. https://arxiv.org/abs/1209.5657
2. The reproducibility script `verify.py` packaged with this note (exact rational tests of the two matrix-entry identities).
