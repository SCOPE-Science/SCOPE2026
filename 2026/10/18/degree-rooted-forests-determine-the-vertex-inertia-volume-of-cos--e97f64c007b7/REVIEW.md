# Mathematical review

## Correctness — PASS

For a connected simple graph with \(n\ge2\), \(m\ge1\), the three canonical points for each edge have moment sum \(M=\begin{psmallmatrix}3D-A&-B\\-B^{\mathsf T}&3I\end{psmallmatrix}\). The incidence identity \(BB^{\mathsf T}=D+A\) reduces the determinant to \(3^m(4/3)^n\det(2D-A)\). Centering by the vector of all ones gives the exact rank-\(n+m-1\) pseudodeterminant scaling \((n+m)\det M/(3m)^{n+m}\). A Cauchy–Binet expansion of \(L+D\) proves the positive rooted-forest formula. Schur complementation and a tridiagonal continuant prove the star and path formulas and the exponential volume ratio. Exact computation of the degree-sequence twins verifies graph determinants \(492\) and \(483\). The packaged checker evaluates actual vertex moments independently, all tested cases passing. The infinite statements depend on the analytic proof, not the finite checks.

## Originality — PASS, with limits

The 2017 original paper [1] supplies the object; the 2022 study [2] proves its face descriptions and tree normalized volume; the 2023 study [3] treats regular unimodular triangulations and their volumes. The classical weighted matrix–forest identity [4] is not claimed as new. The assessed statement couples the vertex covariance pseudodeterminant to this forest polynomial and proves volume-matched exponential separation and a degree-sequence-twin example. These do not follow from the cited normalized-volume or face formulas without calculating the Euclidean vertex moments. The examined full-text portions and focused literature searches identified no covering result. Prior work could formulate an equivalent vertex inertia identity under alternative matrix-tree or statistical terminology, and that possibility remains open.

## Mathematical value — PASS

Vertex inertia measures an intrinsic aspect of the *chosen Euclidean realization*, namely the shape and hypervolume of the equal-vertex-mass dispersion ellipsoid. In a natural infinite family whose intrinsic polytope volumes are identical, the inertia-ellipsoid volumes differ by an exponentially growing factor. At six vertices, the invariant also separates two trees with the same degree multiset and exactly equal covariance traces. The rooted-forest interpretation explains the structural source of this difference and yields an exact computation for every connected graph, rather than an arbitrary finite numerical datum. This is distinct from optimizing enclosing or inscribed ellipsoids.

## Sources and residual risks

[1] Arkani-Hamed, Benincasa, Postnikov, arXiv:1709.02813, 2017-09-08. [2] Kühne and Monin, arXiv:2209.08069, 2022-09-16. [3] Juhnke-Kubitzke, Solus, Venturello, arXiv:2303.05876, 2023-03-10. [4] Chebotarev and Shamis, arXiv:math/0602575, preexisting matrix–forest theorem. This review is not an independent validation or a guarantee of exhaustive bibliography. The normalization applies to equal vertex masses, not volume measure.

Self-review: passed. Independent audit: not yet performed.
