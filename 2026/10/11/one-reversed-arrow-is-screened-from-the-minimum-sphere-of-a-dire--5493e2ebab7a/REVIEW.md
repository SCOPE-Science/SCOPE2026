# Same-model review

## Correctness
PASS. Reconstructing the signed path-incidence Gram matrix gives two tridiagonal positive blocks and positive links to the single reversed vertex. The quadratic Dirichlet weights solve the exact normal equations, sum to one, and vanish only at the flipped vertex. The weighted squared-distance identity is a global minimax lower bound for every center and proves uniqueness. All unreversed vertices contact the sphere; the flipped vertex has exact positive squared-distance deficit \(\lambda(m-3)\) for \(m\ge4\), and equality at \(m=3\). The polynomial identity for the two run lengths yields the announced radius and position extremality.

## Originality
PASS. The primary source's Example 5.2 identifies arbitrary path orientations as simplices but does not compute Euclidean minimum spheres. The second directed-root full text concerns triangulations and Ehrhart data. Indexed searches under Dynkin quiver, type-A root simplex, oriented path, one reversal, Chebyshev ball, and circumradius names found no dominating radius/contact theorem. An all-vertex sphere criterion would only decide whether that *particular* sphere is optimal; here the flipped vertex is strictly interior to a smaller sphere and the formula explicitly solves the smaller active set. The consistently oriented path has a different signed Gram matrix.

## Value
PASS. The result answers a natural first orientation-perturbation question for a canonical simplex family: a single reversed arrow causes strict contact screening in every larger dimension. The exact radius is sensitive to defect position, with sharp central and endpoint extremizers. The complete contact and center formulas give a useful geometric test case for broader directed-root-polytope and active-set optimization problems.

## Closest literature and limitations
Numata--Takahashi--Tamaki classify the simplex combinatorics; Kálmán--Tóthmérész analyze directed-root dissection and Ehrhart data. Classical minimum-ball dual certificates are known, and priority under alternative root-system terminology remains a residual risk. Multiple arrow reversals, general trees, inradii and ellipsoids are not covered.

Same-model review: passed. Independent audit: not yet performed.
