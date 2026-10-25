# Review of the sharp polygon-pyramid curvature threshold

## Correctness

PASS. The one-skeleton is the join of a clique with a cycle. Its Laplacian splits orthogonally into the constant line, the apex-direction eigenspace at eigenvalue \(n+r\), and the nonconstant cycle Fourier modes at eigenvalues \(r+\lambda_j\). This gives exactly the apex-to-rim resistance, the apex-to-apex resistance, and the displayed apex curvature. Foster's theorem gives the rim curvature. The trace identities for the nonzero cycle Laplacian modes fix the weighted mean at two; Jensen's lower bound and a chord upper bound straddle two at **consecutive** integer values of the pyramiding parameter. The boundary dimensions \(n=3,4\) are treated separately. The independent grounded-Laplacian checker and symbolic cycle-characteristic checker agree with the formula in all tested cases. No finite computation is used to infer the general theorem.

## Originality

PASS, subject to historical priority limitations. The 2025 polytopal-curvature paper identifies general obstructions and families but not the two-parameter unit-conductance integer phase diagram. Sedlák and Slavík's general resistance-distance formula for joins specializes to the intermediate electrical identities; **that part is prior work**, not an originality claim. Extracting a closed exact *sign threshold* for all base sizes and all pyramid counts requires additional two-moment inequalities; it is not stated in the inspected join or curvature papers. The 2025 weighted-existence graph classes and the 2026 graph-product paper do not cover the unweighted sign classification. A residual risk remains from older equivalent cycle-join specializations or uninspected graph-resistance literature.

## Mathematical value

PASS. Pyramiding is one of the basic operations on convex polytopes. The result answers a concrete structural question: how many successive pyramids over a polygon are required before all vertices of the one-skeleton acquire positive *unweighted* resistance curvature? The exact minimum is \((n(n-3)-2)/2\) for \(n\ge5\), and its proof explains the sharp phase using only the first two cycle-Laplacian moments and spectral interval bounds. It also establishes that no vertex has zero curvature at integer parameters and that the polygon vertices are positive throughout. The distinction from existence of some positive weighting is mathematically essential.

## Scope and residual risk

Only unit-conductance one-skeleta of iterated pyramids over convex polygons are classified. General join resistance formulas imply the resistance computations but do not, in the inspected material, provide the exact phase transition. Independent historical priority assessment remains to be done.

Self-review: passed. Independent audit: not yet performed.
